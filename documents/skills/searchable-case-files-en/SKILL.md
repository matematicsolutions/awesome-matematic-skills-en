---
name: searchable-case-files-en
description: >
  Turns a folder of case files (PDFs, including scans with no text layer) into text with
  page numbers, a local search tool and a report: unreadable pages, duplicate files and
  files with IDENTICAL text under different names (sometimes a sign that a document is
  missing). OCR runs locally on the CPU - the case text never leaves the computer, no
  account, no cloud. Use when: "search the case files", "make the bundle searchable",
  "where in the file is", "OCR the documents", "scanned bundle", "what is missing from
  the case file", "digitize the case file".
attribution:
  - source: run-llama/liteparse
    url: https://github.com/run-llama/liteparse
    license: Apache-2.0
    relationship: dependency
    note: >
      Dependency (PyPI `liteparse`, pinned 2.14.6): PDF parser with Tesseract OCR on the CPU.
      `scripts/liteparse_extract.py` is a copy from doc-intel-contract-pl (PL hub), where the
      canonical version lives with its measurements and five safeguards against the
      library's silent failure modes.
metadata:
  author: Wieslaw Mazur / MateMatic
  version: 0.1.0
  license: MIT
  cost: no LLM, no cloud (local OCR)
  twin: akta-przeszukiwalne-pl
---

# Searchable case files

A folder of scanned case files becomes text you can search. Every hit shows the file and
the page, so you can check it against the original right away.

## Quick start

```bash
python -m pip install liteparse==2.14.6
python scripts/akta.py "C:/Cases/2024-CV-123/bundle"
cd "C:/Cases/2024-CV-123/bundle-text"
python szukaj.py "expert report"
```

The script names are Polish (the code is shared with the Polish twin): `akta.py` means
"case files", `szukaj.py` means "search".

**Pick the language of the documents, not of the user.** English is the default;
Portuguese case files (Brazil, Portugal) need `--lang por`, Polish ones `--lang pol`. The
report and messages follow the same language. Reading Portuguese scans with the English
model loses most accents and about one word in six (measured, see Limits).

The first run downloads the OCR model for the chosen language (Tesseract language data,
12-15 MB, Apache-2.0). To work offline, download it once and pass its folder with
`--tessdata`.

## What you get (next to the case folder; originals are untouched)

- `<document>.txt` - text with `===== page N =====` markers;
- `REPORT.md` - status of every file, unreadable pages, duplicates by bytes and by text;
- `szukaj.py` + `indeks.sqlite` - search tool: file, page, snippet.

Search ignores letter case and accents. It matches whole words: `contract` does not find
`contractor`. Add `--prefix` to match word beginnings as well.

## How to read REPORT.md

- **Same text in different files** - two PDFs with different names contain identical text.
  Often just a copy - but sometimes a misnamed file, and the document the name promises is
  not in the set.
- **Unreadable pages** - the page has an image, but OCR read nothing. Marked
  `[UNREADABLE PAGE - check the original]`; read that page in the PDF.
- Status `BLOCKED` (exit code 20) - a file is incomplete or would not open. Do not treat
  its text as complete.

## What the skill enforces

- OCR text is for SEARCHING. Always check a quote against the original before relying on it.
- Currency is left as read. The `$` -> `§` repair runs only for Polish (`--lang pol`);
  in English and Portuguese documents `$ 5,000` and `R$ 5.000` are amounts.
- The page count of every file is compared with the pages actually read; a mismatch is a
  block, not a silent success.
- Only numbers are printed to the screen. The case text stays in the output folder.
- An interrupted run resumes with the same command - finished documents are skipped.

## Limits

- Poor scans produce more OCR errors. Measured on a public US appellate opinion rendered
  as a scan: 98.7% of its words are findable at 300 dpi, 93.2% on a deliberately degraded
  scan (rotated, blurred, noisy). Character error rate is higher (1.5% and 22%) mostly
  because lines come out in a different order - that hurts reading, not searching.
  Portuguese (public Brazilian judgment rendered as a scan, `--lang por`): 99.3% of words
  findable at 300 dpi, 92.6% degraded; the English model on the same scan found 83.9% and
  kept 39 of 272 accented letters.
- Speed: about 2 s per page (measured on one Windows 11 laptop); a thousand pages take
  about half an hour. Slower on weaker hardware.
- Windows with Smart App Control may block the OCR library's unsigned files
  (`pdfium.dll`, `_liteparse.pyd`). The skill turns "DLL load failed" into a message that
  names Smart App Control - verified on a simulated error, not on a machine with SAC on.
  Changing that setting is the computer owner's decision.
- PDF only. Save DOCX files as PDF first.

## Tests

```bash
python -m pytest tests -q
```
