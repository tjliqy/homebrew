import fs from "node:fs";

import {BrewTesterFileNames} from "5etools-utils/lib/BrewTester/BrewTesterFileNames.js";

const ignoredFilenames = new Set([
	"export-deploy-snapshot.sh",
	"sync-deploy-repo.sh",
]);

const readdirSync = fs.readdirSync;
fs.readdirSync = (...args) => readdirSync(...args)
	.filter(filename => !ignoredFilenames.has(filename));

try {
	await new BrewTesterFileNames().pRun();
} finally {
	fs.readdirSync = readdirSync;
}
