import assert from "node:assert/strict";
import {execFileSync} from "node:child_process";
import fs from "node:fs";
import os from "node:os";
import path from "node:path";
import test from "node:test";
import {BrewTimestamper} from "5etools-utils";

import {updateModifiedTimestamps} from "./update-modified-timestamps.js";

test("updates only Git-modified JSON metadata using the BrewTimestamper hash", async t => {
	const root = fs.mkdtempSync(path.join(os.tmpdir(), "homebrew-timestamps-"));
	t.after(() => fs.rmSync(root, {recursive: true, force: true}));
	const git = (...args) => execFileSync("git", args, {cwd: root});
	git("init", "-q");
	git("config", "user.name", "Test");
	git("config", "user.email", "test@example.invalid");
	fs.mkdirSync(path.join(root, "collection"));
	const changedPath = path.join(root, "collection", "中文 name.json");
	const untouchedPath = path.join(root, "collection", "untouched.json");
	const noMetaPath = path.join(root, "index.json");
	const original = {
		_meta: {dateAdded: 100, dateLastModified: 200, _dateLastModifiedHash: "oldhash"},
		monster: [{name: "Original"}],
	};
	fs.writeFileSync(changedPath, JSON.stringify(original, null, "\t") + "\n");
	fs.writeFileSync(untouchedPath, JSON.stringify(original, null, "\t") + "\n");
	fs.writeFileSync(noMetaPath, "{}\n");
	git("add", ".");
	git("commit", "-qm", "initial");

	const modified = {...original, monster: [{name: "Modified"}]};
	const source = JSON.stringify(modified, null, "\t") + "\n";
	fs.writeFileSync(changedPath, source);
	fs.writeFileSync(noMetaPath, "{\"generated\":true}\n");
	fs.writeFileSync(path.join(root, "collection", "untracked.json"), "{}\n");
	git("add", "collection/中文 name.json");

	const preview = updateModifiedTimestamps({root, dryRun: true, timestamp: 300});
	assert.deepEqual(preview.updated, ["collection/中文 name.json"]);
	assert.deepEqual(preview.skipped, ["index.json"]);
	assert.equal(fs.readFileSync(changedPath, "utf8"), source);

	const result = updateModifiedTimestamps({root, timestamp: 300});
	assert.deepEqual(result.updated, ["collection/中文 name.json"]);
	const output = JSON.parse(fs.readFileSync(changedPath, "utf8"));
	assert.equal(output._meta.dateAdded, 100);
	assert.equal(output._meta.dateLastModified, 300);
	const expectedHash = await BrewTimestamper._pGetHash({
		...modified,
		_meta: {...modified._meta, dateAdded: undefined, dateLastModified: undefined, _dateLastModifiedHash: undefined},
	});
	assert.equal(output._meta._dateLastModifiedHash, expectedHash);
	assert.deepEqual(output.monster, modified.monster);
	assert.equal(fs.readFileSync(untouchedPath, "utf8"), JSON.stringify(original, null, "\t") + "\n");
	assert.equal(fs.readFileSync(noMetaPath, "utf8"), "{\"generated\":true}\n");
});
