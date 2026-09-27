# Grade assignment check: heading position vs numbering reset

Annex: `야생생물법_시행규칙_별표1_개정20221209.pdf` (amended 2022-12-09; SHA256 `4f75d4f8f92b8d7381b345cd89757672fc2e869bb75264eec2ab580a579945b4`).
Text extraction: pdfplumber 0.11.9, x_tolerance=1.

Annex 1 restarts its row numbering at 1 for each class within each taxonomic group,
so a grade can be read either from the class heading that precedes a row in the
extracted text or from the point where the numbering resets. This log compares the
two signals in both text extractions the pipeline uses.

## Census extraction (pdfplumber, x_tolerance=1) -- 282 species

- Rows: 282
- Grade by heading position: {'I급': 68, 'II급': 214}
- Grade by numbering reset:  {'I급': 68, 'II급': 214}
- Rows where the two disagree: **0**

The census uses the heading position; in this extraction headings and rows come out in
reading order, so the numbering reset gives the same grade for every row.

## Earlier 16-species extraction (pypdf) -- comparison only

- Rows: 282
- Rows where heading position and numbering reset disagree: **41** (by group: {'조류': 13, '어류': 5, '육상식물': 9, '해조류': 2, '고등균류': 12})
- Rows where the pypdf numbering reset differs from the census grade: **64** (by group: {'어류': 25, '곤충류': 6, '육상식물': 20, '해조류': 2, '고등균류': 11})

pypdf reads the two-column layout out of order: a class heading can precede rows that
belong to the other class, and rows of one table can be interleaved with the next, so
neither signal is reliable across the whole annex in this extraction. Up to v1.0.1 the
16-species file used its numbering reset, which is correct for the ten designated
species but not for the annex as a whole. From v1.0.2 both files use the pdfplumber
extraction above.

## The ten designated species

| Species | Annex name | pypdf heading | pypdf reset | pdfplumber heading | pdfplumber reset | Released |
|---|---|---|---|---|---|---|
| 하늘다람쥐 *Pteromys volans* | *Pteromys volans aluco* | II급 | II급 | II급 | II급 | II급 |
| 수리부엉이 *Bubo bubo* | *Bubo bubo* | II급 | II급 | II급 | II급 | II급 |
| 금개구리 *Pelophylax chosenicus* | *Pelophylax chosenicus* | II급 | II급 | II급 | II급 | II급 |
| 반달가슴곰 *Ursus thibetanus* | *Ursus thibetanus ussuricus* | I급 | I급 | I급 | I급 | I급 |
| 수달 *Lutra lutra* | *Lutra lutra* | I급 | I급 | I급 | I급 | I급 |
| 남생이 *Mauremys reevesii* | *Mauremys reevesii* | II급 | II급 | II급 | II급 | II급 |
| 두루미 *Grus japonensis* | *Grus japonensis* | II급 | I급 | I급 | I급 | I급 |
| 저어새 *Platalea minor* | *Platalea minor* | II급 | I급 | I급 | I급 | I급 |
| 점박이물범 *Phoca largha* | *Phoca largha* | I급 | I급 | I급 | I급 | I급 |
| 맹꽁이 *Kaloula borealis* | *Kaloula borealis* | II급 | II급 | II급 | II급 | II급 |

pypdf heading position misassigns 2 of the ten.

## Totals against the amending notice

- Parsed: {'I급': 68, 'II급': 214}; expected: {'I급': 68, 'II급': 214} -> agree
- Source of the expected totals: Ministry of Environment (Biodiversity Division), press release of 9 December 2022, '멸종위기 야생생물, 267종에서 282종으로 개정', attached PDF (https://www.korea.kr/common/download.do?fileId=197531828&tblKey=GMN; copy data/statute/moe_press_release_2022-12-09_endangered_wildlife_282.pdf, SHA256 19c7f5912d64d5aef5799d2b62ddc80824be018189f57b633d931db2d66efab5), page 3: 'I급 68종과 Ⅱ급 214종 등 최종 282종', and the table by group on page 4. Transcribed changes: data/statute/amendment_2022_expected_changes.json.

## Differences from the previous list (`designated_species_v1.0.2.json`)

- New: 0 []
- Removed: 0 []
- Grade changed: 0 []
- Renamed: 0 []

## Visual check of a random sample

- 30 rows drawn with seed 20260926 were compared with page images of the pinned PDF by the authors with AI assistance on 2026-09-26 (`data/statute/annex1_visual_check.json`): 0 disagreements.
- The rows of the ten designated species of the 16-species file not in the sample: 7 read in the same way, 0 disagreements (not used for the bound); designated rows not read: none
- One-sided 95% upper bound on the row error rate: 9.5%

## Result

- PASS: every released grade agrees with both signals of the pdfplumber extraction,
  and the ten designated species carry the same grade in both release files.
