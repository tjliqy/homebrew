#!/usr/bin/env python3
"""Restore translated ``affectsCreatureType`` values to English using the term table."""

from __future__ import annotations

import argparse
import json
import os
from pathlib import Path
import subprocess
import sys

from check_baseitem_left_values import collect_json_files, parse_json_spans


def find_values(root: dict) -> list[tuple[str, int, int]]:
    found: list[tuple[str, int, int]] = []

    def visit(node: dict, in_field: bool = False) -> None:
        if node["kind"] == "string":
            if in_field:
                found.append((node["value"], node["start"], node["end"]))
        elif node["kind"] == "array":
            for child in node["children"]:
                visit(child, in_field)
        elif node["kind"] == "object":
            for key, child in node["pairs"]:
                if key == "affectsCreatureType":
                    visit(child, True)
                else:
                    visit(child, in_field)

    visit(root)
    return found


def lookup_english(terms: list[str], translator_root: Path) -> dict[str, list[str]]:
    if not terms:
        return {}
    interpreter = Path(os.environ.get(
        "FIVE_E_TRANSLATOR_PYTHON", str(translator_root / ".venv/bin/python")
    ))
    if not interpreter.is_file():
        print(f"Term lookup unavailable: Python environment not found: {interpreter}", file=sys.stderr)
        return {}
    worker = r'''
import json, os, sys
from pathlib import Path
import pymysql
from dotenv import load_dotenv
load_dotenv(Path.cwd() / ".env")
terms = json.load(sys.stdin)
if not terms:
    print("{}")
    raise SystemExit
placeholders = ",".join(["%s"] * len(terms))
sql = ("SELECT en, cn FROM term WHERE LOWER(TRIM(cn)) IN (" + placeholders + ") "
       "ORDER BY cn, en")
conn = pymysql.connect(host=os.getenv("DB_HOST"), port=int(os.getenv("DB_PORT", "3306")),
    user=os.getenv("DB_USER"), password=os.getenv("DB_PASSWORD"),
    database=os.getenv("DB_DATABASE"), charset="utf8mb4", connect_timeout=5,
    read_timeout=10, write_timeout=10, cursorclass=pymysql.cursors.DictCursor)
try:
    with conn.cursor() as cursor:
        cursor.execute(sql, terms)
        rows = cursor.fetchall()
finally:
    conn.close()
found = {}
for row in rows:
    found.setdefault(row["cn"].strip().casefold(), set()).add(row["en"].strip())
print(json.dumps({key: sorted(values) for key, values in found.items()}, ensure_ascii=False))
'''
    try:
        result = subprocess.run(
            [str(interpreter), "-c", worker],
            input=json.dumps(terms, ensure_ascii=False), text=True,
            capture_output=True, timeout=20, cwd=translator_root, check=False,
        )
    except (OSError, subprocess.TimeoutExpired) as exc:
        print(f"Term lookup unavailable: {exc}", file=sys.stderr)
        return {}
    if result.returncode:
        detail = result.stderr.strip().splitlines()[-1] if result.stderr.strip() else result.stdout.strip()
        print(f"Term lookup unavailable: {detail or f'exit code {result.returncode}'}", file=sys.stderr)
        return {}
    try:
        return json.loads(result.stdout)
    except json.JSONDecodeError as exc:
        print(f"Term lookup returned invalid JSON: {exc}", file=sys.stderr)
        return {}


def choose_english(chinese: str, candidates: list[str]) -> str | None:
    if len(candidates) == 1:
        print(f"{chinese} → {candidates[0]}")
        return candidates[0]
    if candidates:
        print(f"\n{chinese} 有多个英文候选：")
        for index, candidate in enumerate(candidates, 1):
            print(f"  {index}. {candidate}")
        while True:
            answer = input("编号 / 新英文 / - 跳过：").strip()
            if answer == "-":
                return None
            if answer.isdigit() and 1 <= int(answer) <= len(candidates):
                return candidates[int(answer) - 1]
            if answer:
                return answer
    answer = input(f"\n{chinese} 未找到英文译名，请输入英文（留空或 - 跳过）：").strip()
    return None if answer in {"", "-"} else answer


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("paths", nargs="*", help="JSON files or directories (default: current directory)")
    parser.add_argument("--translator-root", type=Path,
                        default=Path(os.environ.get("FIVE_E_TRANSLATOR_ROOT", "/data/5e-translator")))
    parser.add_argument("--dry-run", action="store_true", help="List values without prompting or writing")
    args = parser.parse_args()
    try:
        files = collect_json_files([Path(raw) for raw in args.paths] if args.paths else [Path.cwd()])
        occurrences: dict[str, list[tuple[Path, int, int, str]]] = {}
        for path in files:
            original = path.read_text(encoding="utf-8")
            root = parse_json_spans(original)
            for value, start, end in find_values(root):
                left = value.partition("|")[0].strip()
                if left and any("\u3400" <= char <= "\u9fff" or "\uf900" <= char <= "\ufaff" for char in left):
                    occurrences.setdefault(left.casefold(), []).append((path, start, end, value))
        if not occurrences:
            print(f"No translated affectsCreatureType values found in {len(files)} JSON file(s).")
            return 0
        display_terms = {key: rows[0][3].partition("|")[0].strip() for key, rows in occurrences.items()}
        candidates = lookup_english(list(display_terms.values()), args.translator_root.resolve())
        translations: dict[str, str] = {}
        for key, chinese in display_terms.items():
            choices = candidates.get(key, [])
            if args.dry_run:
                print(f"{chinese}: {', '.join(choices) if choices else '[no English match]'} ({len(occurrences[key])} occurrence(s))")
                continue
            translations[key] = choose_english(chinese, choices) or ""
        if args.dry_run:
            print(f"Scanned {len(files)} JSON file(s); no files changed.")
            return 0
        changed = 0
        edits_by_file: dict[Path, list[tuple[int, int, str]]] = {}
        for key, rows in occurrences.items():
            english = translations.get(key)
            if not english:
                continue
            for path, start, end, full_value in rows:
                _, separator, suffix = full_value.partition("|")
                edits_by_file.setdefault(path, []).append((start, end, json.dumps(english + separator + suffix, ensure_ascii=False)))
        for path, edits in edits_by_file.items():
            updated = path.read_text(encoding="utf-8")
            for start, end, encoded in sorted(edits, reverse=True):
                updated = updated[:start] + encoded + updated[end:]
            json.loads(updated)
            path.write_text(updated, encoding="utf-8")
            changed += len(edits)
            print(f"Restored {len(edits)} affectsCreatureType value(s): {path}")
        print(f"Restored {changed} value(s) in {len(edits_by_file)} file(s).")
        return 0
    except (OSError, UnicodeError, json.JSONDecodeError, ValueError) as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
