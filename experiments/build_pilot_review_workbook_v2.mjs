import fs from "node:fs/promises";
import { FileBlob, SpreadsheetFile, Workbook } from "@oai/artifact-tool";

const [inputXlsx, csvPath, outputXlsx, previewDir] = process.argv.slice(2);
if (!inputXlsx || !csvPath || !outputXlsx || !previewDir) throw new Error("missing workbook paths");

const csvText = await fs.readFile(csvPath, "utf8");
const csvBook = await Workbook.fromCSV(csvText, { sheetName: "CSV" });
const csvSheet = csvBook.worksheets.getItem("CSV");
const csvValues = csvSheet.getUsedRange(true).values;
if (csvValues.length !== 19 || csvValues[0].length !== 17) throw new Error(`unexpected pilot CSV shape ${csvValues.length}x${csvValues[0].length}`);

const workbook = await SpreadsheetFile.importXlsx(await FileBlob.load(inputXlsx));
const cases = workbook.worksheets.getItem("Pilot Cases");
const summary = workbook.worksheets.getItem("Summary");

cases.getRange("A1:Q19").values = csvValues;
cases.freezePanes.freezeRows(1);
cases.freezePanes.freezeColumns(2);
cases.showGridLines = false;
cases.getRange("A1:Q1").format = {
  fill: "#163A63", font: { bold: true, color: "#FFFFFF" },
  horizontalAlignment: "center", verticalAlignment: "center", wrapText: true,
  borders: { preset: "outside", style: "thin", color: "#163A63" },
};
cases.getRange("A2:Q19").format.verticalAlignment = "top";
cases.getRange("A2:Q19").format.wrapText = true;
cases.getRange("A2:Q19").format.borders = { preset: "inside", style: "thin", color: "#D7E3EF" };
cases.getRange("A2:Q19").conditionalFormats.deleteAll();
cases.getRange("A2:Q19").conditionalFormats.addCustom("=MOD(ROW(),2)=0", { fill: "#D9EEF7" });
cases.getRange("A1:A19").format.columnWidthPx = 112;
cases.getRange("B1:B19").format.columnWidthPx = 110;
cases.getRange("C1:D19").format.columnWidthPx = 62;
cases.getRange("E1:E19").format.columnWidthPx = 78;
cases.getRange("F1:F19").format.columnWidthPx = 320;
cases.getRange("G1:H19").format.columnWidthPx = 86;
cases.getRange("I1:I19").format.columnWidthPx = 125;
cases.getRange("J1:K19").format.columnWidthPx = 255;
cases.getRange("L1:L19").format.columnWidthPx = 150;
cases.getRange("M1:N19").format.columnWidthPx = 260;
cases.getRange("O1:O19").format.columnWidthPx = 170;
cases.getRange("P1:Q19").format.columnWidthPx = 92;
cases.getRange("A1:Q1").format.rowHeightPx = 36;
cases.getRange("A2:Q19").format.rowHeightPx = 62;

summary.getRange("B4").formulas = [["=COUNTA('Pilot Cases'!$A$2:$A$19)"]];
summary.getRange("B5").formulas = [["=COUNTIF('Pilot Cases'!$B$2:$B$19,\"3GPP \"&A5)"]];
summary.getRange("B6").formulas = [["=COUNTIF('Pilot Cases'!$B$2:$B$19,\"3GPP \"&A6)"]];
summary.getRange("B7").formulas = [["=COUNTIF('Pilot Cases'!$Q$2:$Q$19,A7)"]];
summary.getRange("F4").formulas = [["=COUNTIF('Pilot Cases'!$G$2:$G$19,D4)"]];
summary.getRange("F4:F9").fillDown();
summary.getRange("A12:B16").values = [
  ["목적", "Pilot은 모델 성능 결론이 아니라 prompt·라벨·채점 규칙의 실행 가능성을 확인한다."],
  ["출처", "동일 Release 18·V18.12.0의 ETSI 공식 TS 23.501 및 TS 24.501만 사용한다."],
  ["Gold label", "18개 라벨은 현재 self_checked이며 독립 전문가 또는 2차 검토자 확정 전이다."],
  ["채점 재현성", "v3 dry run은 24시간 지연 동일 평가자 blind pass 1·2에서 응답 18/18과 적용 판정 105/105가 일치했다."],
  ["분리", "이 18개는 main 72개에 재사용하지 않는다."],
];
summary.getRange("B12:F16").merge(true);
summary.getRange("A12:A16").format.font = { bold: false, color: "#1F2937" };
summary.getRange("B12:B16").format.wrapText = true;
summary.getRange("A12:F16").format.borders = { preset: "inside", style: "thin", color: "#E5E7EB" };
summary.getRange("A12:F16").format.rowHeightPx = 32;
summary.showGridLines = false;

await fs.mkdir(previewDir, { recursive: true });
for (const name of ["Pilot Cases", "Summary", "Source Audit"]) {
  const rendered = await workbook.render({ sheetName: name, autoCrop: "all", scale: 1, format: "png" });
  await fs.writeFile(`${previewDir}/${name.replaceAll(" ", "_")}.png`, new Uint8Array(await rendered.arrayBuffer()));
}
console.log((await workbook.inspect({ kind: "table", sheetId: "Pilot Cases", range: "A1:Q19", include: "values,formulas", tableMaxRows: 20, tableMaxCols: 17, maxChars: 18000 })).ndjson);
console.log((await workbook.inspect({ kind: "table", sheetId: "Summary", range: "A1:F16", include: "values,formulas", tableMaxRows: 20, tableMaxCols: 8, maxChars: 10000 })).ndjson);
console.log((await workbook.inspect({ kind: "match", searchTerm: "#REF!|#DIV/0!|#VALUE!|#NAME\\?|#N/A", options: { useRegex: true, maxResults: 300 }, summary: "final formula error scan" })).ndjson);
await fs.mkdir(outputXlsx.slice(0, outputXlsx.lastIndexOf("/")), { recursive: true });
await (await SpreadsheetFile.exportXlsx(workbook)).save(outputXlsx);
