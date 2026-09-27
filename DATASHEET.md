# Datasheet for K-EndangeredBench v1.0.9

Follows Gebru et al. (2021), *Datasheets for Datasets*. Shipped with every release archive.

DOI: https://doi.org/10.5281/zenodo.22969956

---

## 1. Motivation

**Purpose.** There was no public reference against which the factual accuracy of
AI-generated educational content about Korean endangered species could be measured. Korea
designates endangered wildlife nationally (Class I / Class II) and the IUCN assesses global
extinction risk; the two frequently disagree, and that disagreement is both a source of
error in generated text and an evaluation axis. K-EndangeredBench records both grades side
by side for the 16 species of a deployed education card set, and releases the full
statutory census of 282 designated species in the same record schema.

**Creators.** Ji Sun Hong and Yuyong Kim, H-grae Co., Ltd. (BonV Lab).

**Funding.** No specific grant from any funding agency in the public, commercial, or
not-for-profit sectors.

---

## 2. Composition

**Instances.** One record per designated taxon or card species.
`k_endangered_bench_v1.json`: 16 species (10 nationally designated, 6 common control
species) plus 24 non-species cards. `k_endangered_bench_full.json`: all 282 taxa
designated in Annex 1 (as amended 2022-12-09; 261 species, 13 subspecies, 8 varieties),
without card narrative.

**Fields.** Both files share the field list of `common/bench_schema.py`; `schema_notes`
inside each JSON file glosses every field and every subfield of `card`, `gbif_source` and
`warnings`, and the packaging gate refuses a release in which a field or subfield has no
gloss. `warnings` is a list of objects with a machine code (for example
`card_grade_differs_from_statute`) and a Korean message; the codes are listed in
`schema_notes["warnings[].code"]`.

| Field group | Source |
|---|---|
| `korea_nie_grade` (alias `korea_statutory_grade`), `korea_grade_source`, `korea_statute_*`, `statute_rank` | Annex 1 of the Enforcement Rule of the Wildlife Protection and Management Act, parsed from the pinned PDF |
| `iucn_category`, `iucn_scope`, `iucn_assessment_id`, `iucn_assessment_date`, `iucn_assessment_year`, `iucn_population_trend`, `iucn_habitats`, `iucn_threats`, `iucn_conservation_actions` | IUCN Red List API v4 (or the IUCN-via-GBIF checklist when no token is available) |
| `iucn_source`, `iucn_match_status`, `iucn_query_name`, `iucn_concept_relation`, `iucn_retrieved_between_utc` | How, when and under which name the IUCN value was obtained, and whether the IUCN unit is the designated taxon |
| `iucn_assessment_outdated` | Derived: assessment more than 10 years older than the retrieval date |
| `gbif_*`, `gbif_match_accepted`, `gbif_source` | GBIF API v1 and Backbone Taxonomy |
| `mismatch_flag`, `mismatch_type`, `severity_gap`, `mismatch_type_any_concept`, `severity_gap_any_concept` | Derived from the two grades |
| `name_provisional` | Whether the scientific name was assigned from a Korean vernacular |
| `card.*` | BonV Lab card set (16-species file only) |

`korea_nie_grade` keeps its original name so that existing code does not break; the grade
is statutory, and `korea_statutory_grade` carries the same value under a name that says so.

**Provenance.** Top-level `provenance` records the annex amendment date (2022-12-09) and
marker, the annex file name inside the archive, its original file name, size and SHA256,
the text-extraction library and version (pdfplumber 0.11.9, x_tolerance 1), and the UTC
retrieval window of the cached responses. The amendment date, file names and SHA256 are
read from one file, `data/statute/annex1.json` (shipped as `statute/annex1.json`).
`annex_currency_check.md` records a check against the law.go.kr Open API that the Annex 1
text is the same in every version of the Enforcement Rule promulgated since 9 December
2022, up to the version in force on 26 September 2026. Each record carries its own IUCN retrieval
window, including records for which no IUCN taxon was found.

**Assessment scope and unit.** `iucn_category` holds a Global category unless `iucn_scope`
says otherwise. Where a species has no Global assessment, the latest assessment of any
scope is used and `no_global_assessment` is true. Where the statute designates a
subspecies or variety and only the species is assessed, the species' category is kept with
`iucn_match_status = matched_at_species_rank` and `iucn_concept_relation = broader`; such
records, and synonyms that merge the designated taxon into another species, are
`not_comparable` in `mismatch_type`. `mismatch_type_any_concept` gives the label without
that condition, for species-rank assessments and merged synonyms only; values reached
through a GBIF match outside the gate, and relations `uncertain` or `different_taxon`, are
not compared in either field. `iucn_concept_relation` other than `same` occurs, apart from
designated subspecies and varieties that reached their own binomial, for fifteen census
taxa, all listed in `schema_notes` and in `census_tables.md`. `iucn_relation_basis` says for
every record whether its relation was inferred by rule (`inferred`), lowered by the range
check (`range_check`) or set by hand (`hand_override`: *Lycoris chinensis* var. *sinuolata*,
*Strix aluco*, *Phoxinus phoxinus* and *Dryophytes suweonensis*). One hand decision sets no
relation: the Amur tiger's IUCN subspecies taxon was read by a hand-checked identifier for its
warning text (warning code `iucn_taxon_hand_mapped`). To exclude every record touched by a
hand decision, filter on both: `iucn_relation_basis = hand_override`, or
`iucn_taxon_hand_mapped` among the warning codes.

**Split that the range check cannot see.** *Dryophytes suweonensis* (Class I) reaches the
IUCN taxon under its own name, but the IUCN assesses it in the narrow sense: the assessment
gives the Chilgap Hills as the southern boundary of the range, and the populations south of
the Chilgap range were described as *D. flaviventris* (Borzée et al. 2020), which the IUCN
assesses separately (assessment 188099200, EN). The GBIF Backbone (2023) lists
*D. suweonensis* as a synonym of *D. immaculatus*; it took that treatment from its constituent
Catalogue of Life, in the Annual Checklist 2023 (ChecklistBank 9910, DOI 10.48580/dfsr, the only
release of 2023 issued before that Backbone) from the sector whose source is ITIS. Which reference
ITIS cited for the synonymy at that time is not recoverable (the ITIS record read in 2026 is the
current one); a synonymy of the two names had been proposed by Dufresnes et al. (2016), and we do
not know that ITIS followed it. The IUCN and
Borzée et al. (2018, 2020) treat the two as separate species, as do ITIS and the Catalogue of
Life now (the lookups are in `hand_lookups.json`, `synonym_source`). Annex 1 names
*D. suweonensis* alone. Its amendment of 9 December 2022 postdates the description of
*D. flaviventris* and moved the species to *Dryophytes* but did not list *D. flaviventris*,
which suggests that the designated taxon is *D. suweonensis* in the broad sense and the IUCN
unit narrower in taxonomic concept; geographically the two only partly overlap (the IUCN unit
adds KP and omits the southern KR populations). The annex does not say so. Since v1.0.6 the relation is `uncertain` (hand
override; likely direction: IUCN narrower) and the record is not compared. The
narrow species still lists KR, so the range check does not detect this split.

**Range check.** `iucn_range_includes_korea` records whether the range countries of the
selected assessment include the Republic of Korea or the Democratic People's Republic of
Korea. A Global assessment that includes neither is never compared: its relation becomes
`uncertain`, or `different_taxon` where the authors checked the split by hand (*Strix aluco*, whose
Korean population the IUCN places in *S. nivicolum*; *Phoxinus phoxinus*, which the IUCN
restricts to western Europe). For these two, `iucn_counterpart` gives the IUCN taxon that
corresponds to the Korean population: *S. nivicolum* (assessment 264106602, LC, 2024, KR and
KP extant) for the owl, and none identified for the minnow: no current *Phoxinus* assessment
appears in the IUCN country list of KR (API v4 `/countries/KR`), the only current one in that of
KP is *P. tumensis*, and of the current *Phoxinus* assessments only those of *P. tumensis* and
*P. ujmonensis* were read for their range countries. Mitochondrial studies place the South Korean
populations in one Asian lineage, sister to *P. p. tumensis* (Lee et al. 2019) and distinct from
European *P. phoxinus* (Cheng et al. 2022); no study we found names its species. The country
lists also return superseded assessments of *P. phoxinus* in its former broad sense: the KR list
returns the Global assessment of 2008 (LC) and two European regional assessments of 2010 (LC);
the KP list returns the same three and the Global assessment of 1996 (LR/lc, a category of the
pre-3.1 system, `legacy_category = true`), which the KR list omits. The endpoint's rule for
including an assessment is not documented; `hand_lookups.json` records the scope and category of
each entry. The lookups behind these hand decisions are
cached and listed in `cache_manifest.json` (section `hand_lookups`), and `hand_lookups.json`
checks every hand value against its response. Five census taxa are `uncertain` for this reason. The
check cannot see a taxon without an assessment. On the token-free path there are no range
countries; a record compared with a token-free value carries `iucn_range_not_checked`.

**Subspecies without a current assessment.** The Amur leopard (*Panthera pardus
orientalis*) is an IUCN taxon with four superseded assessments (2008 CR, 1996 CR twice, 1994
E) and a 2016 Not Evaluated entry, which is not an assessment; none is marked `latest`, and
the record's warning lists the two separately (since v1.0.6); in `iucn_derived.json` the NE
entry is under `not_evaluated_entries`, not `past_assessments` (since v1.0.7). The Amur tiger (*Panthera tigris
altaica*) returns no IUCN taxon under that name in the API v4 name search, but the taxon
(SIS 15956, *Panthera tigris* ssp. *altaica*) holds superseded assessments only, most
recently Endangered in 2011; the IUCN Cat Classification Task Force placed *altaica* in
*P. t. tigris* (Kitchener et al. 2017). The taxon was read by a hand-checked identifier, and
the record carries the warning `iucn_taxon_hand_mapped`; only the warning text depends on it. Both carry the current assessment of their species
(`matched_at_species_rank`), which is `not_comparable` in `mismatch_type` and compared only in
the any-concept fields; their past subspecies entries are listed in a warning. Superseded
assessments are compared nowhere. Some carry a category of an earlier IUCN system (the tiger's
1965 "N/A", the leopard's 1994 "E"); in `iucn_derived.json` such entries are marked
`legacy_category = true` (since v1.0.8).

**Missing values.** A record with no IUCN category carries `iucn_category = null`,
`iucn_source = iucn_none_returned`, and an `iucn_match_status` that separates an IUCN
taxon without a published assessment (`not_assessed`), a taxon whose assessments are all
superseded (`no_current_assessment`; no record in this release) and a name that could not be resolved to any IUCN
taxon (`name_unresolved`). Of the 70 `not_assessed` census taxa, 65 reached an IUCN taxon of
the same concept; for the other five the unassessed IUCN taxon is broader (3), of uncertain
relation (1) or a different taxon (1). Missing values are never filled with reference
values.

**Sensitive data.** None concerning people. Precise localities of endangered species are
deliberately excluded because of poaching risk; GBIF occurrence data appear only as counts
and country lists.

**Printed card grades.** `card.grade_printed_on_card` stores the grade as printed. The
spotted seal card prints Class II against the statutory Class I. The dataset preserves the
printed value in that field and flags it in `warnings` (`card_grade_differs_from_statute`).
No correction of the printed cards had been made when this release was built; a teacher
using the printed card should teach Class I (I급).

---

## 3. Collection process

1. `python -m common.statute_list --json data/statute/designated_species.json` parses the
   pinned Annex 1 PDF (282 taxa) and checks every scientific name against the name format.
2. `paper02_bench/scripts/check_grade_assignment.py` compares grade assignment by heading
   position and by numbering reset for every row, checks the Class I and Class II totals
   against the amending notice (68 and 214), diffs the list against the previous one, and
   reports the visual check of 30 random rows and of the ten designated species of the
   16-species file (`grade_assignment_check.md`). `validate_annex_diff.py` runs the diff step
   on the 2022 amendment against the ministry's list of changes (`annex_diff_validation.md`).
3. `paper02_bench/scripts/parse_cards.py` normalises the BonV Lab card CSVs.
4. `paper02_bench/scripts/fetch_facts.py` matches each of the 16 names to the GBIF Backbone
   with a per-species kingdom hint, retrieves GBIF facts, verifies the national grade
   against the annex, and resolves the IUCN taxon from the designated name.
5. `paper02_bench/scripts/build_dataset.py` merges and labels divergence.
6. `python -m common.fetch_designated` and `python -m common.build_full_bench` do the same
   for the 282-taxon census, with the same resolution rules and the same GBIF match gate.
7. `paper02_bench/scripts/mismatch_analysis.py` and `package_release.py` produce the
   summary and the archive.

IUCN resolution (common/iucn_resolve.py): the designated name first (with `infra_name` for
a subspecies or variety), then, for a species, the GBIF accepted name and its synonyms,
including infraspecific synonyms whose epithet matches the designated one; for a
subspecies or variety with no assessment of its own, the species and its synonyms.

Every external response is cached with its retrieval timestamp, including empty and
not-found responses. `--offline` rebuilds read the cache regardless of age and never use
the network; `--frozen-cache` keeps cached responses and fetches only missing ones.
`cache_manifest.json` lists every response the build read, per run (`bench`, `census`,
`census_token_free`), and the lookups behind the hand decisions (`hand_lookups`, from
v1.0.7); the IUCN API responses it lists are not shipped. From v1.0.8 each entry carries the
SHA256 of the response body (`value_sha256`), each IUCN assessment response also the SHA256 of the
content the build reads from it (`assessment_sha256`), and `paper02_bench/scripts/verify_iucn_values.py`
lets a reader with an IUCN token fetch every assessment by identifier and compare it. The token-free
census run is shipped as `iucn_via_gbif_census.json` with its log and the per-taxon
comparison `token_free_comparison.json`. Setting `KEB_NO_DOTENV=1` stops the configuration
module from reading `.env` files.

---

## 4. Preprocessing

- Word spacing in annex names lost in PDF extraction is restored; the packaging gate
  refuses a statute name that does not match the name format.
- National grades are normalised to `I급` / `II급`.
- GBIF matches other than EXACT at rank SPECIES/SUBSPECIES are refused in the 16-species
  file unless the species registry sets an explicit override; in the census they are kept
  with `gbif_match_accepted = false`, and IUCN values reached only through them carry
  `via_unaccepted_gbif_match` and are not compared.
- DD, NE, regional-only and missing IUCN categories, species-rank assessments of
  designated subspecies or varieties, and merged synonyms are not placed on the ordinal
  scale (`mismatch_type = not_comparable`, `severity_gap = null`).

---

## 5. Uses

**Intended.** Factual-accuracy and hallucination evaluation of generated text about these
species; comparison of answers against the national and the global authority; relational
evaluation using the non-species cards.

**Not intended.** Conservation decisions, status assessments, environmental impact
statements or regulatory filings; any use that treats `severity_gap` as an interval
quantity; any attempt to derive localities.

---

## 6. Distribution and licence

**Compilation licence: CC BY-NC 4.0.** The build code in the code snapshot
(`k-endangered-bench-code-v1.0.9.zip`, in the same Zenodo record) is under the MIT licence;
that licence covers code only and not the data.

| Component | Source | Terms | Handling in this release |
|---|---|---|---|
| Card narrative | BonV Lab card set | Copyright H-grae Co., Ltd. | Released by the copyright holder, H-grae Co., Ltd., the authors' employer, for non-commercial research use |
| IUCN categories and classifications | IUCN Red List API v4 | IUCN terms of use; commercial use not permitted | Derived values and assessment IDs only; raw API responses are not redistributed |
| IUCN categories via GBIF | IUCN checklist on GBIF (DOI 10.15468/0qnb58) | CC BY 4.0 | Responses shipped in `cached_responses/iucn_gbif/` |
| GBIF facts | GBIF API | Per-dataset licences, CC0 to CC BY-NC | Aggregates only; responses shipped in `cached_responses/gbif/` |
| National designations | Statute (Annex 1) | Not subject to copyright | Pinned PDF and, from v1.0.8, the Annex 1 PDF of the version in force at the currency check shipped in `statute/` |
| Synonym-source lookups | ChecklistBank (Catalogue of Life), ITIS | CC BY 4.0; public domain | Responses shipped in `cached_responses/checklist_sources/` |

**Release of the card narrative by its copyright holder.** H-grae Co., Ltd. holds the
copyright in the BonV Lab card set and employs both authors; the corresponding author founded
BonV Lab. The authors release the card narrative in this dataset on behalf of the company under
CC BY-NC 4.0, the non-commercial condition being the one under which the company makes it
available. No separate signed consent document was prepared for this release, and none is
claimed here.

---

## 7. Maintenance

- Maintainers: the authors. Contact: the corresponding author, Ji Sun Hong (hongji5@gmail.com).
  Problems are received by e-mail; there is no public issue tracker, and one will be linked from
  the Zenodo record if a public source repository is opened. Corrections are issued as new
  versions of the Zenodo record, never by changing a published version.
- Annex currency: rerun `check_annex_currency.py` at least once a year and before relying on
  the national grades at a later date. Without running code, check on law.go.kr that the
  heading of Annex 1 of the Enforcement Rule in force still reads "<개정 2022. 12. 9.>". The
  release is a snapshot; the maintainers do not monitor the annex on a schedule, and checking
  it before use is the user's responsibility.
- Identifiers: each version has its own Zenodo DOI; the concept DOI (reserved record
  22969955, resolving after publication) points to the latest version. A new version is made
  with Zenodo's "New version" on the published record.
- Updates: when the IUCN Red List is updated or Annex 1 is amended. A later amendment of
  Annex 1 becomes a new pinned artefact and a new dataset version (re-verification steps in
  the paper, §2.9, and in `paper02_bench/README.md`).
- Versioning: value changes increment the patch or minor version; adding or removing
  species increments the major version. Earlier versions remain available unchanged.
