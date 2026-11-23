#!/usr/bin/env python3
"""Translate untranslated 5etools ``baseItem`` and ``attachedSpells`` values.

The script reads exact matches from the 5e-translator term table. If the table
has no unique translation, it asks the user once per English term. For both
fields, it translates the text before ``|`` and preserves the suffix. An
``attachedSpells`` value without ``|`` is translated in full.
"""

from __future__ import annotations

import argparse
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile


SKIP_DIRS = {".git", ".venv", "node_modules", "__pycache__"}
ABILITY_VALUES = {
    "str", "dex", "con", "int", "wis", "cha",
    "strength", "dexterity", "constitution", "intelligence", "wisdom", "charisma",
}


def _term_worker() -> int:
    """Read terms from stdin and return exact term-table matches as JSON."""
    sys.path.insert(0, str(Path.cwd()))
    import pymysql
    from dotenv import load_dotenv

    load_dotenv(Path.cwd() / ".env")
    db_config = {
        "HOST": os.getenv("DB_HOST"),
        "PORT": int(os.getenv("DB_PORT", "3306")),
        "USER": os.getenv("DB_USER"),
        "PASSWORD": os.getenv("DB_PASSWORD"),
        "DATABASE": os.getenv("DB_DATABASE"),
    }

    terms = json.load(sys.stdin)
    if not terms:
        print("{}")
        return 0
    placeholders = ",".join(["%s"] * len(terms))
    sql = (
        "SELECT en, cn, category, source FROM term "
        f"WHERE LOWER(TRIM(en)) IN ({placeholders}) ORDER BY en, category, cn, source"
    )
    connection = pymysql.connect(
        host=db_config["HOST"],
        port=db_config["PORT"],
        user=db_config["USER"],
        password=db_config["PASSWORD"],
        database=db_config["DATABASE"],
        charset="utf8mb4",
        connect_timeout=5,
        read_timeout=10,
        write_timeout=10,
        cursorclass=pymysql.cursors.DictCursor,
    )
    try:
        with connection.cursor() as cursor:
            cursor.execute(sql, terms)
            rows = cursor.fetchall()
    finally:
        connection.close()
    found: dict[str, list[dict[str, str]]] = {}
    for row in rows:
        key = row["en"].strip().casefold()
        found.setdefault(key, []).append({
            "cn": row["cn"],
            "category": row.get("category") or "",
            "source": row.get("source") or "",
        })
    print(json.dumps(found, ensure_ascii=False))
    return 0


def has_chinese(text: str) -> bool:
    return any("\u3400" <= char <= "\u9fff" or "\uf900" <= char <= "\ufaff" for char in text)


def escape_pointer_part(value: object) -> str:
    return str(value).replace("~", "~0").replace("/", "~1")


def parse_json_spans(text: str) -> dict:
    """Parse JSON while retaining source offsets for surgical string edits."""
    decoder = json.JSONDecoder()

    def skip_space(index: int) -> int:
        while index < len(text) and text[index].isspace():
            index += 1
        return index

    def parse_value(index: int) -> tuple[dict, int]:
        index = skip_space(index)
        start = index
        char = text[index]
        if char == "{":
            index = skip_space(index + 1)
            pairs = []
            if text[index] == "}":
                return {"kind": "object", "pairs": pairs, "start": start, "end": index + 1}, index + 1
            while True:
                key, key_end = decoder.raw_decode(text, index)
                index = skip_space(key_end)
                if text[index] != ":":
                    raise ValueError(f"Expected ':' at JSON offset {index}")
                child, index = parse_value(index + 1)
                pairs.append((key, child))
                index = skip_space(index)
                if text[index] == "}":
                    return {"kind": "object", "pairs": pairs, "start": start, "end": index + 1}, index + 1
                if text[index] != ",":
                    raise ValueError(f"Expected ',' or '}}' at JSON offset {index}")
                index = skip_space(index + 1)
        if char == "[":
            index = skip_space(index + 1)
            children = []
            if text[index] == "]":
                return {"kind": "array", "children": children, "start": start, "end": index + 1}, index + 1
            while True:
                child, index = parse_value(index)
                children.append(child)
                index = skip_space(index)
                if text[index] == "]":
                    return {"kind": "array", "children": children, "start": start, "end": index + 1}, index + 1
                if text[index] != ",":
                    raise ValueError(f"Expected ',' or ']' at JSON offset {index}")
                index = skip_space(index + 1)
        value, end = decoder.raw_decode(text, index)
        kind = "string" if isinstance(value, str) else "scalar"
        return {"kind": kind, "value": value, "start": start, "end": end}, end

    root, end = parse_value(0)
    if skip_space(end) != len(text):
        raise ValueError(f"Unexpected trailing content at JSON offset {end}")
    return root


def find_translatable_values(root: dict) -> list[tuple[str, str, str, int, int]]:
    """Return (pointer, value, field, start, end) for relevant string values."""
    found: list[tuple[str, str, str, int, int]] = []

    def visit(node: dict, pointer: str = "", in_attached_spells: bool = False) -> None:
        kind = node["kind"]
        if kind == "string":
            if in_attached_spells:
                found.append((pointer, node["value"], "attachedSpells", node["start"], node["end"]))
            return
        if kind == "array":
            for index, child in enumerate(node["children"]):
                visit(child, f"{pointer}/{index}", in_attached_spells)
            return
        if kind == "object":
            for key, child in node["pairs"]:
                child_pointer = f"{pointer}/{escape_pointer_part(key)}"
                if key == "baseItem" and child["kind"] == "string":
                    found.append((child_pointer, child["value"], "baseItem", child["start"], child["end"]))
                elif key == "attachedSpells":
                    visit(child, child_pointer, True)
                else:
                    visit(child, child_pointer, in_attached_spells)

    visit(root)
    return found


def collect_json_files(paths: list[Path]) -> list[Path]:
    files: set[Path] = set()
    for path in paths:
        if path.is_file():
            if path.suffix.lower() == ".json":
                files.add(path.resolve())
            else:
                raise ValueError(f"Not a JSON file: {path}")
        elif path.is_dir():
            for candidate in path.rglob("*.json"):
                if not any(part in SKIP_DIRS for part in candidate.parts):
                    files.add(candidate.resolve())
        else:
            raise ValueError(f"Path does not exist: {path}")
    return sorted(files)


def query_term_table(terms: list[str], translator_root: Path) -> dict[str, list[dict[str, str]]]:
    if not terms:
        return {}
    interpreter = Path(os.environ.get(
        "FIVE_E_TRANSLATOR_PYTHON", str(translator_root / ".venv/bin/python")
    ))
    if not interpreter.is_file():
        print(f"Term lookup unavailable: Python environment not found: {interpreter}", file=sys.stderr)
        return {}
    try:
        result = subprocess.run(
            [str(interpreter), str(Path(__file__).resolve()), "--term-worker"],
            input=json.dumps(terms, ensure_ascii=False),
            text=True,
            capture_output=True,
            timeout=20,
            cwd=translator_root,
            check=False,
        )
    except (OSError, subprocess.TimeoutExpired) as exc:
        print(f"Term lookup unavailable: {exc}", file=sys.stderr)
        return {}
    if result.returncode:
        detail = result.stderr.strip().splitlines()[-1] if result.stderr.strip() else (
            result.stdout.strip() or f"exit code {result.returncode}"
        )
        print(f"Term lookup unavailable: {detail}", file=sys.stderr)
        return {}
    try:
        return json.loads(result.stdout)
    except json.JSONDecodeError as exc:
        print(f"Term lookup returned invalid JSON: {exc}", file=sys.stderr)
        return {}


def ask_translation(term: str, candidates: list[dict[str, str]], fields: set[str]) -> str | None:
    field_labels = {
        "baseItem": "基础物品（baseItem）",
        "attachedSpells": "法术（attachedSpells）",
    }
    context = "、".join(field_labels[field] for field in sorted(fields))
    print(f"\n{term} 〔{context}〕")
    if candidates:
        translations = sorted({candidate["cn"] for candidate in candidates if candidate.get("cn")})
        if len(translations) == 1:
            print(f"术语库唯一译法：{translations[0]}")
            return translations[0]
        print("术语库有多个译法，请选择或输入新译法：")
        for index, translation in enumerate(translations, 1):
            print(f"  {index}. {translation}")
        while True:
            answer = input("编号 / 新译法 / - 跳过：").strip()
            if answer == "-":
                return None
            if answer.isdigit() and 1 <= int(answer) <= len(translations):
                return translations[int(answer) - 1]
            if answer:
                return answer
    answer = input("术语库无译法，请输入译法（留空或输入 - 跳过）：").strip()
    return None if answer in {"", "-"} else answer


def rewrite_file(path: Path, translations: dict[str, str]) -> int:
    original = path.read_text(encoding="utf-8")
    root = parse_json_spans(original)
    edits = []
    for _, full_value, _, start, end in find_translatable_values(root):
        left, separator, right = full_value.partition("|")
        translation = translations.get(left.strip().casefold())
        if not translation or translation == left:
            continue
        new_value = translation + separator + right
        edits.append((start, end, json.dumps(new_value, ensure_ascii=False)))
    replacements = len(edits)
    if not replacements:
        return 0
    updated = original
    for start, end, encoded in sorted(edits, reverse=True):
        updated = updated[:start] + encoded + updated[end:]
    json.loads(updated)  # Refuse to write a malformed result.
    path_stat = path.stat()
    fd, temporary_name = tempfile.mkstemp(prefix=f".{path.name}.", suffix=".tmp", dir=path.parent)
    try:
        with os.fdopen(fd, "w", encoding="utf-8", newline="") as stream:
            stream.write(updated)
        os.chmod(temporary_name, path_stat.st_mode)
        os.replace(temporary_name, path)
    except Exception:
        try:
            os.unlink(temporary_name)
        except OSError:
            pass
        raise
    return replacements


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("paths", nargs="+", help="JSON files or directories to scan recursively")
    parser.add_argument(
        "--translator-root",
        type=Path,
        default=Path(os.environ.get("FIVE_E_TRANSLATOR_ROOT", "/data/5e-translator")),
        help="5e-translator checkout containing the term table configuration",
    )
    parser.add_argument("--dry-run", action="store_true", help="Show candidates without prompting or writing")
    parser.add_argument("--term-worker", action="store_true", help=argparse.SUPPRESS)
    return parser


def main() -> int:
    if "--term-worker" in sys.argv:
        return _term_worker()
    args = build_parser().parse_args()
    try:
        files = collect_json_files([Path(raw) for raw in args.paths])
        occurrences: dict[str, list[tuple[Path, str, str, str]]] = {}
        for path in files:
            data = json.loads(path.read_text(encoding="utf-8"))
            root = parse_json_spans(path.read_text(encoding="utf-8"))
            for pointer, value, field, _, _ in find_translatable_values(root):
                left = value.partition("|")[0].strip()
                if left and left.casefold() not in ABILITY_VALUES and not has_chinese(left):
                    occurrences.setdefault(left.casefold(), []).append((path, pointer, left, field))
        terms_by_key = {key: rows[0][2] for key, rows in occurrences.items()}
        if not terms_by_key:
            print(f"No untranslated baseItem/attachedSpells values found in {len(files)} JSON file(s).")
            return 0
        candidates = query_term_table(list(terms_by_key.values()), args.translator_root.resolve())
        translations: dict[str, str] = {}
        skipped: list[str] = []
        for key, term in terms_by_key.items():
            matches = candidates.get(key, [])
            fields = {row[3] for row in occurrences[key]}
            if args.dry_run:
                choices = ", ".join(sorted({item["cn"] for item in matches if item.get("cn")}))
                print(f"{term}〔{', '.join(sorted(fields))}〕: "
                      f"{choices if choices else '[需用户填写]'} ({len(occurrences[key])} 处)")
                continue
            if not matches:
                for path, pointer, _, field in occurrences[key]:
                    print(f"  {path}{pointer} ({field})")
            translation = ask_translation(term, matches, fields)
            if translation:
                translations[key] = translation
            else:
                skipped.append(term)
        if args.dry_run:
            print(f"Scanned {len(files)} JSON file(s); no files changed.")
            return 0
        changed_files = 0
        changed_fields = 0
        for path in files:
            count = rewrite_file(path, translations)
            if count:
                changed_files += 1
                changed_fields += count
                print(f"Updated {count} baseItem/attachedSpells value(s): {path}")
        print(f"Updated {changed_fields} field(s) in {changed_files} file(s).")
        if skipped:
            print("Skipped: " + ", ".join(skipped), file=sys.stderr)
        return 0
    except (OSError, UnicodeError, json.JSONDecodeError, ValueError) as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
