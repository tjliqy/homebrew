import {BrewTesterFileLocations} from "5etools-utils/lib/BrewTester/BrewTesterFileLocations.js";

BrewTesterFileLocations._ROOT_JSON_FILES.add("edgeone.json");

await new BrewTesterFileLocations().pRun();
