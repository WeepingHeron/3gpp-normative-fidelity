import fs from "node:fs/promises";
import { FileBlob, SpreadsheetFile } from "@oai/artifact-tool";

const input = process.argv[2];
const previewDir = process.argv[3];
if (!input || !previewDir) throw new Error("Usage: node inspect_review_workbook.mjs <input.xlsx> <preview-dir>");
await fs.mkdir(previewDir, { recursive: true });
const workbook = await SpreadsheetFile.importXlsx(await FileBlob.load(input));
console.log((await workbook.inspect({ kind: "workbook,sheet,table", maxChars: 8000, tableMaxRows: 5, tableMaxCols: 12, tableMaxCellChars: 80 })).ndjson);
const sheets = JSON.parse(`[${(await workbook.inspect({ kind: "sheet", include: "id,name", maxChars: 5000 })).ndjson.trim().split("\n").filter(Boolean).join(",")}]`);
for (const item of sheets) {
  const name = item.name;
  const preview = await workbook.render({ sheetName: name, autoCrop: "all", scale: 1, format: "png" });
  await fs.writeFile(`${previewDir}/${name.replaceAll(/[^a-zA-Z0-9가-힣_-]/g, "_")}.png`, new Uint8Array(await preview.arrayBuffer()));
}
