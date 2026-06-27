#!/usr/bin/env node
/**
 * Markdown → PDF (sin Chromium). Usa PDFKit + fuentes Windows.
 */
import fs from "node:fs";
import path from "node:path";
import PDFDocument from "pdfkit";

const FONT_REGULAR = "C:\\Windows\\Fonts\\arial.ttf";
const FONT_BOLD = "C:\\Windows\\Fonts\\arialbd.ttf";
const FONT_MONO = "C:\\Windows\\Fonts\\consola.ttf";

function mdToPdf(mdPath, pdfPath) {
  const text = fs.readFileSync(mdPath, "utf8");
  const doc = new PDFDocument({
    margin: 50,
    size: "A4",
    bufferPages: true,
    info: {
      Title: path.basename(pdfPath, ".pdf"),
      Author: "Dev Muscle - Sistema Hibrido",
    },
  });

  const stream = fs.createWriteStream(pdfPath);
  doc.pipe(stream);

  doc.registerFont("regular", FONT_REGULAR);
  doc.registerFont("bold", FONT_BOLD);
  doc.registerFont("mono", FONT_MONO);

  const pageWidth = doc.page.width - doc.page.margins.left - doc.page.margins.right;
  let inCode = false;

  for (const rawLine of text.split(/\r?\n/)) {
    const line = rawLine.replace(/\t/g, "  ");

    if (line.trim().startsWith("```")) {
      inCode = !inCode;
      if (inCode) doc.moveDown(0.3);
      continue;
    }

    if (inCode) {
      doc.font("mono").fontSize(8.5).fillColor("#1a1a1a");
      doc.text(line || " ", { width: pageWidth, lineGap: 1 });
      continue;
    }

    doc.fillColor("#111111");

    if (line.startsWith("# ")) {
      doc.moveDown(0.8).font("bold").fontSize(22).text(line.slice(2), { width: pageWidth });
      doc.moveDown(0.3);
    } else if (line.startsWith("## ")) {
      doc.moveDown(0.6).font("bold").fontSize(16).text(line.slice(3), { width: pageWidth });
      doc.moveDown(0.2);
    } else if (line.startsWith("### ")) {
      doc.moveDown(0.4).font("bold").fontSize(13).text(line.slice(4), { width: pageWidth });
    } else if (line.startsWith("#### ")) {
      doc.moveDown(0.3).font("bold").fontSize(11).text(line.slice(5), { width: pageWidth });
    } else if (/^---+$/.test(line.trim())) {
      doc.moveDown(0.4);
      const y = doc.y;
      doc.strokeColor("#cccccc").lineWidth(1);
      doc.moveTo(doc.page.margins.left, y).lineTo(doc.page.width - doc.page.margins.right, y).stroke();
      doc.moveDown(0.4);
    } else if (line.startsWith("|")) {
      doc.font("regular").fontSize(9).text(line, { width: pageWidth, lineGap: 1 });
    } else if (/^[-*] /.test(line)) {
      doc.font("regular").fontSize(10).text("• " + line.slice(2), { width: pageWidth, indent: 10 });
    } else if (/^\d+\. /.test(line)) {
      doc.font("regular").fontSize(10).text(line, { width: pageWidth, indent: 10 });
    } else if (line.trim() === "") {
      doc.moveDown(0.35);
    } else {
      const cleaned = line
        .replace(/\*\*(.+?)\*\*/g, "$1")
        .replace(/`([^`]+)`/g, "$1")
        .replace(/\[([^\]]+)\]\([^)]+\)/g, "$1");
      doc.font("regular").fontSize(10).text(cleaned, { width: pageWidth, lineGap: 2 });
    }

    if (doc.y > doc.page.height - 70) doc.addPage();
  }

  // Footer page numbers
  const range = doc.bufferedPageRange();
  for (let i = range.start; i < range.start + range.count; i++) {
    doc.switchToPage(i);
    doc.font("regular").fontSize(8).fillColor("#666666");
    doc.text(`Página ${i + 1} de ${range.count}`, 50, doc.page.height - 40, {
      align: "center",
      width: pageWidth,
    });
  }

  doc.end();

  return new Promise((resolve, reject) => {
    stream.on("finish", resolve);
    stream.on("error", reject);
  });
}

const [mdPath, pdfPath] = process.argv.slice(2);
if (!mdPath || !pdfPath) {
  console.error("Uso: node md-to-pdf.mjs <input.md> <output.pdf>");
  process.exit(1);
}

await mdToPdf(path.resolve(mdPath), path.resolve(pdfPath));
console.log("PDF OK:", pdfPath);
