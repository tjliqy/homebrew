import * as fs from "fs";
import * as Uf from "5etools-utils/lib/UtilFs.js";

const PATH_INDEX_META = "_generated/index-meta.json";

function getTranslatorText (translators) {
	if (!translators?.length) return undefined;
	return translators.length > 1 ? `${translators[0]}等` : translators[0];
}

function patchIndexMetaTranslators () {
	const indexMeta = Uf.readJsonSync(PATH_INDEX_META);

	Uf.runOnDirs(folder => {
		Uf.listJsonFiles(folder)
			.map(file => ({
				name: file,
				contents: Uf.readJsonSync(file),
			}))
			.forEach(fileInfo => {
				if (!fileInfo.contents._meta?.sources?.length) return;
				if (fileInfo.contents._meta.unlisted) return;

				const fileName = fileInfo.name.split("/").slice(1).join("/");
				const meta = indexMeta[fileName];
				if (!meta) return;

				const translatorText = getTranslatorText(fileInfo.contents._meta.translators);
				if (translatorText == null) delete meta.t;
				else meta.t = translatorText;
			});
	});

	fs.writeFileSync(PATH_INDEX_META, JSON.stringify(indexMeta), "utf-8");
}

export {patchIndexMetaTranslators};
