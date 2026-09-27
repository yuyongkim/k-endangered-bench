---
license: cc-by-nc-4.0
language:
  - ko
  - en
tags:
  - biodiversity
  - endangered-species
  - korea
  - factuality
  - hallucination-evaluation
  - science-education
pretty_name: K-EndangeredBench
size_categories:
  - n<1K
---

# K-EndangeredBench v1.0.9

DOI of this version: https://doi.org/10.5281/zenodo.22969956
Concept DOI (all versions, resolves to the latest): https://doi.org/10.5281/zenodo.22969955

An open record set for evaluating the factual accuracy of AI-generated content about
Korean endangered species. Each record pairs the Korean national designation (Class I /
Class II under Annex 1 of the Enforcement Rule of the Wildlife Protection and Management
Act, as amended 2022-12-09) with the IUCN Red List category, GBIF taxonomic and occurrence
facts, and expert-authored card narrative. Disagreement between the two authorities is
kept explicit (`mismatch_type`, `severity_gap`) rather than reconciled, and is computed
only where the IUCN assessed the same taxon that the statute designates.

## Contents

| File | Content |
|---|---|
| `k_endangered_bench_v1.json` | 16 species records + 24 non-species cards, with top-level `provenance` and `schema_notes` |
| `k_endangered_bench_v1.csv` | Flattened species table (from v1.0.5 also concept relation, range check, any-concept labels and warning codes; from v1.0.6 also `korea_statutory_grade`, `iucn_counterpart_name`, `iucn_relation_basis` and `warning_messages_ko`, appended so that earlier columns keep their order) |
| `k_endangered_bench_full.json` | All 282 taxa designated in Annex 1, same record schema, no card narrative |
| `k_endangered_bench_full.csv` | Flattened census table, with concept relation, range check, IUCN counterpart and the any-concept labels; from v1.0.6 also `iucn_relation_basis` and `warning_messages_ko` |
| `iucn_derived.json` | IUCN values used in both files, with assessment IDs, name-resolution routes and GBIF name matches (no raw API JSON). Its `concept_relation_basis` is null (relation inferred by rule), `range_check` or `hand_override`, as `iucn_relation_basis` in the records with null for `inferred` (v1.0.9; v1.0.8 carried an internal value, `range_check_hand_checked`, for the two hand-checked splits) |
| `mismatch_analysis.csv`, `mismatch_summary.md` | Divergence records for the 16-species file |
| `census_tables.json`, `census_tables.md` | Census counts, placement sensitivity, relations other than `same` |
| `token_free_comparison.json`, `iucn_via_gbif_census.json`, `iucn_via_gbif_census_run.log` | The census run through the token-free IUCN-via-GBIF path and its per-taxon comparison with the API path. `iucn_via_gbif_census.json` is raw output of that path: its values are not benchmark values, no range check was made on them and they carry no warnings (for example *Brasenia schreberi* shows `same` there, while the benchmark record, with the range check, is `uncertain`). Use `token_free_comparison.json` or the benchmark files instead |
| `gbif_spelling_allowlist_sensitivity.md` | Effect of the optional reviewed spelling allow-list (not used for the release) |
| `BUILD_REPORT.md` | Counts, retrieval window, per-species warnings (with machine codes) |
| `DATASHEET.md` | Datasheet for datasets |
| `CITATION.cff` | Citation metadata |
| `grade_assignment_check.md`, `.json` | Heading position vs numbering reset for every annex row; totals against the amending notice; diff against the previous parsed list; visual check of 30 random rows and of the ten designated species |
| `annex_diff_validation.md`, `.json` | The diff step run on the 2022 amendment (annex in force before 2022-12-09 against the pinned annex), compared with the Ministry of Environment press release |
| `annex_currency_check.md`, `.json` | law.go.kr Open API check that Annex 1 is unchanged in every version of the Enforcement Rule since the pinned amendment, with request URLs and response hashes |
| `cache_manifest.json` | Every cached response the build read, by run: `bench`, `census`, `census_token_free` (namespace, request key, file), and from v1.0.7 `hand_lookups`, the lookups behind the hand decisions. It also lists IUCN Red List API responses (namespace `iucn`), which are read but not shipped. From v1.0.8 every entry carries `value_sha256`, the SHA256 of the response body (JSON with sorted keys), and every IUCN assessment response also `assessment_sha256`, the SHA256 of the content the build reads from it (category, year, dates, scope, range countries, classification codes; the full body changes daily because its citation carries the access date), so that a reader with an IUCN token can check a fresh response against the one the build read (`paper02_bench/scripts/verify_iucn_values.py` in the code snapshot) |
| `hand_lookups.json` | The lookups behind the hand decisions (*Dryophytes flaviventris*, *D. suweonensis*, *Phoxinus tumensis*, *P. ujmonensis*, *Strix nivicolum*, the *Phoxinus* assessments in the IUCN country lists of KR and KP (API v4 `/countries/{code}`) with their scope and category, and from v1.0.8 the source of the GBIF Backbone synonymy of *D. suweonensis* in the Catalogue of Life and ITIS, from v1.0.9 with the metadata of the Catalogue of Life release), with request paths, retrieval times, response SHA256 and a check that every value written in the records matches its response (no raw IUCN JSON) |
| `statute/annex1_wildlife_act_enforcement_rule_amended_2022-12-09.pdf` | The pinned statutory annex (original file name and SHA256 in `provenance.korea_annex`) |
| `statute/annex1_in_force_MST286031_562f73965183.pdf` | (v1.0.8) The Annex 1 PDF attached to the version of the Rule in force at the currency check, kept by `check_annex_currency.py --save-pdf`; its text and parsed rows equal those of the pinned annex (`annex_currency_check.md`) |
| `statute/annex1.json` | The single record of the pinned annex's amendment date, file names and SHA256 that the code reads |
| `statute/annex1_visual_check.json`, `statute/gbif_spelling_allowlist.json` | The visual-check record; the reviewed spelling allow-list |
| `statute/amendment_2022_expected_changes.json` | The changes of the 2022 amendment as listed by the Ministry of Environment, with the source hashes |
| `statute/amendment_2022_rename_classes.json` | Classes of the 25 renames and two addition-plus-removal pairs of the 2022 amendment (not in the press release) |
| `scoring/keb_score.py` | Reference scorer used in the paper's examples (MIT licence, standard library only) |
| `scoring/scorer_validation.md`, `.json` | Agreement of the scorer with hand labels on 60 held-out model answers |
| `cached_responses/gbif/`, `cached_responses/iucn_gbif/`, `cached_responses/checklist_sources/` | GBIF API responses and IUCN-via-GBIF responses read by the three runs; ChecklistBank and ITIS responses of the synonym-source lookup |
| `.zenodo.json`, `CHECKSUMS.txt` | Deposit metadata; SHA256 of every file (LF line endings) |

## Field provenance

Every graded value has a paired source field; `schema_notes` inside each JSON file glosses
every field and every subfield of `card`, `gbif_source` and `warnings`. `iucn_source`:
`iucn_api_v4`, `iucn_via_gbif`, `iucn_none_returned`, `registry_reference` (refused by the
packaging gate). `iucn_match_status` (API path): `matched`, `matched_via_synonym`,
`matched_at_species_rank`, `not_assessed`, `name_unresolved`, `via_unaccepted_gbif_match`,
`no_current_assessment`; (token-free path): `matched_via_gbif`,
`no_global_category_via_gbif`, `name_unresolved_via_gbif`. `iucn_concept_relation`:
`same`, `broader`, `uncertain`, `different_taxon`; `iucn_relation_basis` says whether that
relation was inferred by rule (`inferred`), lowered by the range check (`range_check`) or set
by hand (`hand_override`). One hand decision changes no relation: the IUCN subspecies taxon of
*Panthera tigris altaica* was read by a hand-checked SIS identifier for its warning text
(warning code `iucn_taxon_hand_mapped`). To exclude every record touched by a hand decision,
filter on both: `iucn_relation_basis = hand_override` or `iucn_taxon_hand_mapped` in
`warnings`; `iucn_range_includes_korea` says whether
the range countries of the selected assessment include KR or KP (a Global assessment without
them is never compared). `korea_grade_source`: `statute_verified`,
`api`, `statute_transcribed` (refused), `none`. `mismatch_type`: `korea_stricter`,
`iucn_stricter`, `aligned`, `not_comparable`; `mismatch_type_any_concept` gives the label
without the same-taxon condition (species-rank assessments and merged synonyms only).
`korea_statutory_grade` is an alias of `korea_nie_grade` (kept for compatibility).
`warnings` is a list of `{"code", "message_ko"}` objects. `iucn_counterpart` names, for a
record whose IUCN taxon is a different taxon from the Korean population, the IUCN taxon that
does correspond to it (for *Strix aluco*: *S. nivicolum*), or says that none was found
(*Phoxinus phoxinus*). Superseded assessments (`past_assessments`, `assessment_history` in
`iucn_derived.json`) are listed for reference and compared nowhere; a category of an earlier IUCN
system (for example E, LR/lc or N/A) is marked `legacy_category = true`.

**Answer-bearing fields.** A prompt that asks a model for a conservation status should not
embed `iucn_category`, `korea_nie_grade`, `korea_statutory_grade`, `mismatch_flag`,
`mismatch_type`, `severity_gap`, `mismatch_type_any_concept`, `severity_gap_any_concept`,
`iucn_assessment_id` or `gbif_usage_key` (the last two resolve to pages that state the
category), nor the warning texts, which quote grades.

## Checking the IUCN values with a token

The raw IUCN responses are not shipped. A reader with an IUCN Red List API token can fetch every
assessment the release uses by its identifier and compare category, year, scope, the KR/KP range
entries and the assessment hash (`assessment_sha256`) listed in `cache_manifest.json`:
`python paper02_bench/scripts/verify_iucn_values.py --release /path/to/k-endangered-bench-v1.0.9`
(in the code snapshot). It also reports assessments that are no longer the latest. The hash covers
category and criteria, years, dates, scope, population trend, the `latest` flag, range countries
and classification codes, so a reassessment changes it even when the content is otherwise the
same; the script reports value, hash and `latest` separately and, from v1.0.9, exits non-zero
on any of the three (`--values-only` restores the value-only exit code). Only the 156
assessments the release uses can be checked this way: a record without a category (not
assessed, name unresolved, reached through an unaccepted match) has no assessment identifier.

## Scoring a model answer

```
import json, sys
sys.path.insert(0, "scoring")
from keb_score import score
bench = json.load(open("k_endangered_bench_v1.json", encoding="utf-8"))
rec = next(r for r in bench["entries"] if r["scientific_name"] == "Phoca largha")
print(score(rec, "The spotted seal is listed as Least Concern on the IUCN Red List."))
```

The scorer reads an IUCN category only from a clause that names the IUCN or the Red List, so
"listed as Least Concern" without that attribution is not scored as an IUCN statement. Its
limits and its held-out validation are in `scoring/scorer_validation.md`; the validation sample
holds DeepSeek answers only.

## Rebuilding

Download the code snapshot `k-endangered-bench-code-v1.0.9.zip` from the same Zenodo record
and unzip it; the commands below run in its root directory (Python 3.10 or later;
`pip install -r paper02_bench/requirements-lock.txt`), with this archive unpacked next to it.
The snapshot does not contain `data/statute/designated_species.json`; the first step writes it
from the pinned annex.

```
export KEB_NO_DOTENV=1
export KEB_CACHE_DIR=/path/to/k-endangered-bench-v1.0.9/cached_responses
printf '%s\n%s\n' "10.5281/zenodo.22969956" "10.5281/zenodo.22969955" > doi.txt   # the two DOIs at the top of this README
export KEB_DOI_FILE=doi.txt
cp /path/to/k-endangered-bench-v1.0.9/iucn_derived.json paper02_bench/dataset/
python -m common.statute_list --json data/statute/designated_species.json
python paper02_bench/scripts/check_grade_assignment.py
python paper02_bench/scripts/parse_cards.py
python paper02_bench/scripts/fetch_facts.py --offline
python paper02_bench/scripts/build_dataset.py
python -m common.fetch_designated --offline
python -m common.build_full_bench
python paper02_bench/scripts/mismatch_analysis.py
python -m common.fetch_designated --offline --no-token --out paper02_bench/dataset/iucn_via_gbif_census.json
python paper02_bench/scripts/census_tables.py
python paper02_bench/scripts/validate_annex_diff.py
python paper02_bench/scripts/example_application.py
python paper02_bench/scripts/scorer_validation.py
python paper02_bench/scripts/package_release.py --version 1.0.9 --copy-from /path/to/k-endangered-bench-v1.0.9
```

These are the release steps with `--offline`, including the diff-step validation, the example
application and the scorer validation, whose outputs the packaging step ships; the three
validation scripts must run before the packaging step. Five shipped files are not written by
the build: `annex_currency_check.json` and `.md` (they need network access to law.go.kr),
`gbif_spelling_allowlist_sensitivity.md` (a separate run with the allow-list switched on),
`iucn_via_gbif_census_run.log` (the console output of the release's token-free run) and
`hand_lookups.json` (it reads raw IUCN responses, which are not shipped). `--copy-from` copies
these five from the unpacked archive, and the `hand_lookups` section of `cache_manifest.json`
with them; without them the packaging step stops. The same holds for
a `--frozen-cache` rebuild from the code snapshot. `check_manuscript_numbers.py`, run on a
rebuilt archive instead of this one, fails the one check on the IUCN entries of
`cache_manifest.json` by design, because an offline rebuild reads no IUCN API response.
Without `KEB_DOI_FILE` the rebuild writes a DOI placeholder, and `README.md`, `CITATION.cff`,
`.zenodo.json` and `CHECKSUMS.txt` then also differ from this archive.

`KEB_NO_DOTENV=1` stops the configuration module from reading `.env` files (in the
repository root, in a per-user configuration directory or listed in `KEB_ENV_FILES`), so a
token kept in such a file is not used silently. `--offline` never touches the network. Without an IUCN token,
GBIF matches and synonym candidates are recomputed from the shipped GBIF responses and
checked against the names recorded in `iucn_derived.json`; the IUCN values themselves are
copied from that file, because the raw IUCN responses are not redistributed.
`--frozen-cache` instead fills missing responses from the network while keeping cached
ones, and the default mode re-fetches anything older than 30 days. Without an
`IUCN_API_TOKEN` and outside `--offline` the pipeline uses the IUCN-via-GBIF path
(`iucn_source = iucn_via_gbif`), which carries Global categories only and no habitat,
threat, action or trend fields.

## Annex currency

`paper02_bench/scripts/check_annex_currency.py` (network; not part of the build) asks the
law.go.kr Open API whether Annex 1 has changed since the pinned amendment. It reads the Open
API user id from the environment variable `LAW_OC` (default `test`, the public test id; a
registered id avoids the rate limits of the test id). The check in this archive ran on
26 September 2026. Rerun it before relying on the national grades at a later date, and at
least once a year: the Rule is amended more often than the list is revised (12 versions of
the Rule were promulgated between 9 December 2022 and 12 May 2026). Without running code, the
same check can be made by hand: open the Enforcement Rule of the Wildlife Protection and
Management Act in force on the National Law Information Center (law.go.kr) and look at the
heading of Annex 1; while it still reads "<개정 2022. 12. 9.>", the list this archive was
verified against is in force. This archive is a snapshot: the maintainers do not monitor the
annex on a schedule, and checking it before use is the user's responsibility.

## When Annex 1 has changed

1. Run `check_annex_currency.py --save-pdf data/statute/`; it checks every version of the
   Rule and saves the Annex 1 PDF of the version in force under `data/statute/` (without
   `--save-pdf` the PDF is hashed and parsed in a temporary directory and then discarded; its
   download URL is in `annex_currency_check.md`).
2. Rename the saved PDF with the amendment date in its file name, copy `designated_species.json` to a versioned file,
   and edit `data/statute/annex1.json` only (date, marker, file names, size, SHA256, totals of
   the amending notice, `previous_list`).
3. Run `python -m common.statute_list --json data/statute/designated_species.json`; it must
   report no name-format violations.
4. Run `check_grade_assignment.py`. It lists every taxon added, removed, regraded or renamed.
   Check additions, removals and regrades against the amending notice. The notice does not
   list renames (the 2022 amendment carried 25 renames and two taxa that appear as an
   addition plus a removal): check each rename against the National Species List of Korea
   (NIBR) and classify it as a spelling, subgenus, nomenclatural or concept change. For a
   concept change, re-run the IUCN resolution and check the new relation by hand.
5. Read a random sample of rows against page images of the new PDF and record it in
   `data/statute/annex1_visual_check.json`.
6. Rebuild with `--frozen-cache` and package under a new version number. On Zenodo, create
   a "New version" of this record, which reserves a new version DOI; write it to the file
   named by `KEB_DOI_FILE` before packaging. The concept DOI above keeps pointing to the
   latest version. Without an IUCN token the range check cannot run: every compared record
   then carries `iucn_range_not_checked`. Check the IUCN range by hand for every such record,
   not only for new taxa, because a reassessment or a species split (as for *Strix aluco*)
   can change an existing record; at the least check every record whose category or
   assessment identifier differs from this release, or withhold the comparison.

## Known error in the printed cards

The printed BonV Lab card for the spotted seal (점박이물범) gives Class II (II급); Annex 1
designates it Class I (I급). The record keeps the printed value in `card.grade_printed_on_card`
with the warning `card_grade_differs_from_statute`. Teachers using the printed card should
teach Class I. No correction of the printed cards had been made when this release was built.

## 한국어 안내 (교사·실무자용)

- 이 자료는 평가 연구용 스냅숏입니다. 법정 등급의 근거는 야생생물 보호 및 관리에 관한 법률
  시행규칙 별표 1(2022. 12. 9. 개정)이며, 보전·행정 결정에는 법령과 IUCN 적색목록 원문을
  직접 확인하십시오.
- IUCN 값은 2026-08-22 부터 2026-09-26 사이에 조회한 것입니다. 그 뒤 IUCN 이 다시 평가했을 수 있습니다.
  쓰기 전에 레코드의 평가 ID(`iucn_assessment_id`)로 IUCN 적색목록 누리집에서 현행 범주를
  확인하십시오.
- 점박이물범 카드의 "II급"은 오기입니다. 법정 등급은 I급입니다(`card_grade_differs_from_statute`).
- 국가 등급과 IUCN 범주가 같은 분류군을 가리킬 때만 괴리(`mismatch_type`)를 계산합니다.
  아종 대신 종의 평가, 분포에 한반도가 없는 평가, 분류가 나뉘어 관계를 정할 수 없는 평가는
  `not_comparable` 입니다. 이유가 들어 있는 열은 파일마다 다음과 같습니다(v1.0.6 부터 두 CSV 의
  열 이름이 같습니다).

  | 내용 | `k_endangered_bench_v1.csv`(16종) | `k_endangered_bench_full.csv`(전수 282종) |
  |---|---|---|
  | 법정 등급 | `korea_statutory_grade` (같은 값: `korea_nie_grade`) | `korea_statutory_grade` |
  | 분류군 관계 | `iucn_concept_relation` | `iucn_concept_relation` |
  | 관계를 정한 방법(규칙·분포 대조·손 확인) | `iucn_relation_basis` | `iucn_relation_basis` |
  | 분포에 한국 포함 여부 | `iucn_range_includes_korea` | `iucn_range_includes_korea` |
  | 한국 개체군에 대응하는 IUCN 분류군 | `iucn_counterpart_name` (16종에는 해당 없어 빈칸) | `iucn_counterpart_name` |
  | 경고(코드 / 국문 문장) | `warning_codes` / `warning_messages_ko` | `warning_codes` / `warning_messages_ko` |

- `korea_nie_grade` 는 이름과 달리 국립생태원이 정한 등급이나 국가 적색목록 범주가 아닙니다. 별표 1 의
  법정 등급(I급·II급)이며, 옛 판과 맞추려고 이름만 남겨 둔 열입니다. 같은 값이 `korea_statutory_grade` 에 있습니다.
- 경고 코드의 뜻은 아래와 같습니다. 이 배포본에 실제로 나오는 코드만 적었습니다.

  | 코드 | 뜻 |
  |---|---|
  | `card_grade_differs_from_statute` | 카드에 인쇄된 등급이 법정 등급과 다르다(법정 등급을 따를 것). |
  | `gbif_match_outside_gate` | GBIF 학명 매칭이 정확 일치(EXACT, 종·아종)가 아니다. |
  | `gbif_values_species_rank` | 법은 아종·변종을 지정했으나 GBIF 값은 종의 값이다. |
  | `iucn_assessment_outdated` | IUCN 평가가 조회일보다 10년 넘게 오래됐다. |
  | `iucn_category_not_on_scale` | 범주가 DD 또는 NE 라 위협 순서에 놓을 수 없어 괴리를 계산하지 않는다. |
  | `iucn_concept_broader` | 법정 종이 다른 종에 합쳐져 IUCN 단위가 더 넓다. 같은 분류군 비교에서 뺀다. |
  | `iucn_concept_different_taxon` | IUCN 이름이 법정 분류군과 다른 분류군이다(손 확인). 비교하지 않는다. |
  | `iucn_concept_rank_only` | 속 이동 뒤 같은 종의 평가에 닿았다. IUCN 쪽은 같은 종이며 법정 아종·변종보다 계급만 넓다. |
  | `iucn_concept_uncertain` | IUCN 단위와 법정 분류군의 관계를 정할 수 없다. 비교하지 않는다. |
  | `iucn_matched_at_species_rank` | 법정 아종·변종 대신 종만 평가되어 있다. 괴리를 계산하지 않는다. |
  | `iucn_matched_via_synonym` | IUCN 은 이 분류군을 다른 이름으로 평가한다. |
  | `iucn_name_unresolved` | 시도한 어떤 이름으로도 IUCN 분류군을 찾지 못했다. |
  | `iucn_not_assessed` | IUCN 분류군은 있으나 공개된 평가가 없다. |
  | `iucn_range_excludes_korea` | 전 지구 평가의 분포국에 한국(KR·KP)이 없다. 비교하지 않는다. |
  | `iucn_regional_assessment` | 범주가 전 지구 평가가 아니라 지역(유럽 등) 평가에서 왔다. 법정 등급과 비교하지 않는다(`iucn_scope` 열 참고). |
  | `iucn_taxon_hand_mapped` | 이름 조회로 나오지 않는 IUCN 아종 분류군을 손으로 확인한 식별자로 읽었다(경고 문구에만 쓰임). 손 판단을 모두 빼려면 `iucn_relation_basis` = hand_override 와 이 코드를 함께 거를 것. |
  | `iucn_via_unaccepted_gbif_match` | IUCN 결과가 정확 일치가 아닌 GBIF 매칭에서 나온 이름으로만 얻어졌다. 비교하지 않는다. |

- CSV 의 `warning_codes` 열은 코드를 `|` 로 이어 적고, `warning_messages_ko` 열은 문장을 ` | `
  (앞뒤 공백 포함)로 이어 적습니다. 각 문장 앞에는 `[코드]` 가 붙습니다. Excel 에서는 "텍스트
  나누기"의 구분 기호를 `|` 로 두거나, 필터에서 "포함"으로 코드를 찾으면 됩니다.
- 지난 평가(`iucn_derived.json` 의 `past_assessments`)는 참고로만 적었고 어디서도 비교하지 않습니다.
  E·LR/lc·N/A 같은 옛 범주 체계의 값에는 `legacy_category` 가 붙어 있습니다.
- 손으로 정한 판단을 빼고 쓰려면 `iucn_relation_basis` 가 `hand_override` 인 행과
  `warning_codes` 에 `iucn_taxon_hand_mapped` 가 있는 행(아무르호랑이)을 함께 빼십시오.

- 별표가 바뀌었는지 1년에 한 번 이상 확인하십시오. 마지막 확인: 2026-09-26. 결과: 별표 1 변경 없음(그 사이 시행규칙은 12차례 공포되었고, 확인 시점의 현행 시행규칙은 2026-05-12 공포본입니다. 시행규칙이 개정되었다고 별표 1 이 바뀐 것은 아닙니다). 코드를 쓰지 않아도 됩니다. 국가법령정보센터
  (law.go.kr)에서 「야생생물 보호 및 관리에 관한 법률 시행규칙」 별표 1 머리의 개정 표기가
  "<개정 2022. 12. 9.>" 그대로이면 이 자료가 대조한 목록이 유효합니다. 바뀌었으면 이 자료의
  법정 등급을 확정값으로 쓰지 말고, 쓰려는 종의 등급을 별표 원문에서 직접 확인하십시오. 필요하면
  교신저자 홍지선(hongji5@gmail.com)에게 알려 주십시오. 이 자료는 스냅숏이며, 유지관리자가 정해진 주기로 별표를 점검하지는
  않습니다. 사용 전 확인은 사용자의 몫입니다.
- 별표 개정은 공포 전에 입법예고됩니다. 지정·해제를 미리 알려면 국민참여입법센터(opinion.lawmaking.go.kr)에서
  「야생생물 보호 및 관리에 관한 법률 시행규칙」 입법예고도 함께 확인하십시오.
- 이 배포본의 `statute/annex1_in_force_MST286031_562f73965183.pdf` 가 확인 시점에 시행 중이던 별표 1 원문 PDF 이고,
  `annex_currency_check.md` 에 조회한 주소·시각·해시가 있습니다. 코드를 쓰지 않아도 이 두 파일로
  원문을 대조할 수 있습니다. (코드를 다룰 수 있으면 위 "When Annex 1 has
  changed" 여섯 단계로 새 판을 만들 수 있습니다.)

## Redistribution

The raw IUCN Red List API v4 responses are not included: the IUCN terms of use restrict
their redistribution. The archive carries the derived values and the assessment IDs, from
which any value can be checked against the Red List. The IUCN-via-GBIF responses are CC BY
4.0 (IUCN 2026, DOI 10.15468/0qnb58). GBIF occurrence aggregates derive from datasets with
licences from CC0 to CC BY-NC. The statute is not subject to copyright. Card narrative is
released by its copyright holder, H-grae Co., Ltd., the authors' employer, for
non-commercial research use.

## Licence

CC BY-NC 4.0 for this data compilation; see `DATASHEET.md` section 6 for per-component
terms. The build code in the code snapshot (`k-endangered-bench-code-v1.0.9.zip`) and
`scoring/keb_score.py` are under the MIT licence (code only).

## Issues

Report problems to the corresponding author, Ji Sun Hong (hongji5@gmail.com). An issue tracker will be linked
from the Zenodo record if a public source repository is opened.

## Citation

```bibtex
@dataset{kendangeredbench109,
  title     = {K-EndangeredBench: A Benchmark Dataset and Build Pipeline for
               Evaluating AI-Generated Content on Korean Endangered Species},
  author    = {Hong, Ji Sun and Kim, Yuyong},
  year      = {2026},
  version   = {1.0.9},
  publisher = {Zenodo},
  doi       = {10.5281/zenodo.22969956},
  url       = {https://doi.org/10.5281/zenodo.22969956}
}
```
