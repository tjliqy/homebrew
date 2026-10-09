#!/usr/bin/env node

import {execFileSync} from "node:child_process";
import {createHash} from "node:crypto";
import fs from "node:fs";
import path from "node:path";
import {fileURLToPath} from "node:url";
import {createRequire} from "node:module";

const require = createRequire(import.meta.url);
const utilsRequire = createRequire(require.resolve("5etools-utils/package.json"));
const {parse} = utilsRequire("json-source-map");

function getModifiedJsonPaths (root) {
	const output = execFileSync("git", [
		"diff", "--name-only", "-z", "--diff-filter=ACMR", "HEAD", "--", "*.json",
	], {cwd: root});
	return output.toString("utf8").split("\0").filter(Boolean);
}

function prepareFile (file, timestamp) {
	const source = fs.readFileSync(file, "utf8");
	const {data, pointers} = parse(source);
	if (!data?._meta || typeof data._meta !== "object" || Array.isArray(data._meta)) return null;

	const datePointer = pointers["/_meta/dateLastModified"];
	const hashPointer = pointers["/_meta/_dateLastModifiedHash"];
	if (!datePointer || !hashPointer) {
		throw new Error(`Missing dateLastModified or _dateLastModifiedHash in ${file}`);
	}

	// Match 5etools-utils/lib/BrewTimestamper.js exactly: SHA-512 of JSON.stringify,
	// excluding all timestamp fields, truncated to ten hexadecimal characters.
	const toHash = {...data, _meta: {
		...data._meta,
		dateAdded: undefined,
		dateLastModified: undefined,
		_dateLastModifiedHash: undefined,
	}};
	const hash = createHash("sha512").update(JSON.stringify(toHash)).digest("hex").slice(0, 10);
	const edits = [
		{start: datePointer.value.pos, end: datePointer.valueEnd.pos, replacement: String(timestamp)},
		{start: hashPointer.value.pos, end: hashPointer.valueEnd.pos, replacement: JSON.stringify(hash)},
	].sort((a, b) => b.start - a.start);

	let updated = source;
	for (const {start, end, replacement} of edits) {
		updated = updated.slice(0, start) + replacement + updated.slice(end);
	}
	return {file, updated, changed: updated !== source};
}

export function updateModifiedTimestamps ({root, dryRun = false, timestamp = Math.floor(Date.now() / 1000)} = {}) {
	root = fs.realpathSync(root || execFileSync("git", ["rev-parse", "--show-toplevel"], {encoding: "utf8"}).trim());
	if (!Number.isSafeInteger(timestamp) || timestamp < 0) throw new Error("Invalid Unix timestamp");

	const skipped = [];
	const prepared = [];
	for (const relative of getModifiedJsonPaths(root)) {
		const file = path.join(root, relative);
		if (!fs.lstatSync(file).isFile()) throw new Error(`Not a regular file: ${relative}`);
		const result = prepareFile(file, timestamp);
		if (result) prepared.push({...result, relative});
		else skipped.push(relative);
	}

	if (!dryRun) {
		for (const {file, updated, changed} of prepared) {
			if (changed) fs.writeFileSync(file, updated);
		}
	}
	return {
		updated: prepared.filter(it => it.changed).map(it => it.relative),
		skipped,
		dryRun,
	};
}

if (process.argv[1] && fs.realpathSync(process.argv[1]) === fileURLToPath(import.meta.url)) {
	const args = process.argv.slice(2);
	if (args.some(arg => arg !== "--dry-run")) {
		console.error("Usage: node _node/update-modified-timestamps.js [--dry-run]");
		process.exitCode = 2;
	} else {
		try {
			const result = updateModifiedTimestamps({dryRun: args.includes("--dry-run")});
			for (const file of result.updated) console.log(`${result.dryRun ? "Would update" : "Updated"}: ${file}`);
			for (const file of result.skipped) console.log(`Skipped (no _meta): ${file}`);
			console.log(`${result.dryRun ? "Would update" : "Updated"} ${result.updated.length} JSON file(s); skipped ${result.skipped.length}.`);
		} catch (error) {
			console.error(error);
			process.exitCode = 1;
		}
	}
}
