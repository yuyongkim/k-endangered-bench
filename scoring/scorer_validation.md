# Held-out validation of the reference scorer

Written by `paper02_bench/scripts/scorer_validation.py`.

- Population: 284 held-out answers (Supplementary File S3, set = heldout); sample: 60, random.Random(20260926).sample
- Labels: `scorer_validation_labels.json`, the authors with AI assistance (see the Generative AI disclosure), 2026-09-26
- Models: population {'gemini-2.5-flash': 1, 'deepseek-v4-flash': 10, 'deepseek-chat': 273}; sample {'deepseek-v4-flash': 2, 'deepseek-chat': 58} (no GPT answer)
- Frozen scorer SHA256 `8a23e5b9eaf513d236c728b63d26b6c5d125e13dbbbe953a3556f92eda0b6302`; frozen copy matches the hash recorded in the labels file: True (a self-check, not an external timestamp)
- Answers with the class written as 'Class I Endangered ...', 'Endangered Species Class I' or 'first-class': 34 of 60

## All sampled answers

| Measure | Agree | % (exact 95% CI) |
|---|---|---|
| IUCN categories extracted | 51/60 | 85% (73-93%) |
| National class extracted | 60/60 | 100% (94-100%) |
| Unclassed flag | 50/60 | 83% (71-92%) |
| Status-aware IUCN verdict | 51/60 | 85% (73-93%) |

- Precision of verdict 'correct': 30/30 (88-100%)
- Precision of verdict 'wrong': 13/13 (75-100%)
- Precision of verdict 'unverified': 8/8 (63-100%)

## Word-order subset

| Measure | Agree | % (exact 95% CI) |
|---|---|---|
| IUCN categories extracted | 31/34 | 91% (76-98%) |
| National class extracted | 34/34 | 100% (90-100%) |
| Unclassed flag | 34/34 | 100% (90-100%) |
| Status-aware IUCN verdict | 31/34 | 91% (76-98%) |

- Precision of verdict 'correct': 21/21 (84-100%)
- Precision of verdict 'wrong': 7/7 (59-100%)
- Precision of verdict 'unverified': 3/3 (29-100%)

## Precision and recall by class

| Class | Scorer | Precision | Recall |
|---|---|---|---|
| unclassed | frozen | 5/15 (12-62%) | 5/5 (48-100%) |
| unclassed | released | 5/13 (14-68%) | 5/5 (48-100%) |
| ne | frozen | 12/12 (74-100%) | 12/20 (36-81%) |
| ne | released | 12/12 (74-100%) | 12/20 (36-81%) |

- Held-out answers that attribute a category to a Korean agency's Red List: 22 of 284 (a131, a132, a150, a157, a165, a229, a230, a231, a242, a243, a248, a250, a255, a256, a266, a268, a274, a277, a281, a285, a288, a294); in the sample: a132, a266, a277, a288. The frozen scorer reads that list as an IUCN statement in 8 of them:
  - a231: frozen ['CR', 'VU'] (wrong); released ['VU'] (wrong)
  - a242: frozen ['LC', 'NE'] (wrong); released ['NE'] (correct)
  - a243: frozen ['CR', 'NE'] (ambiguous); released ['NE'] (wrong)
  - a250: frozen ['CR', 'LC', 'NE'] (unverified); released ['LC', 'NE'] (unverified)
  - a255: frozen ['CR', 'NE'] (wrong); released ['NE'] (correct)
  - a274: frozen ['CR', 'DD'] (unverified); released ['DD'] (unverified)
  - a277: frozen ['CR', 'NE'] (ambiguous); released ['NE'] (wrong)
  - a294: frozen ['CR', 'NE'] (unverified); released ['NE'] (unverified)

## Whole held-out pool: frozen against released scorer

- Unclassed flag differs in 11 of 284 answers (a150 deepseek-chat True->False, a188 deepseek-chat True->False, a193 deepseek-chat True->False, a198 deepseek-chat True->False, a199 deepseek-chat True->False, a202 deepseek-chat True->False, a214 deepseek-chat True->False, a216 deepseek-chat True->False, a218 deepseek-chat True->False, a229 deepseek-chat True->False, a248 deepseek-chat True->False)
- IUCN extraction differs in 9 (a231, a242, a243, a250, a255, a274, a277, a279, a294); verdict differs in 5 (a242, a243, a255, a277, a279)
- Answers with neither a class nor the unclassed flag only because their Korean status sentence names the IUCN or the Red List: 0 (none); because it is about a national Red List: 36 (a146, a150, a153, a165, a174, a224, a229, a230, a231, a237, a242, a245, a248, a250, a252, a255, a256, a260, a261, a265, a272, a274, a277, a279, a281, a285, a288, a290, a294, a295, a297, a298, a300, a301, a306, a313)

## Marine Protected Species (another instrument): released scorer

- heldout: 17 answers mention it (0 in the reversed order 'Protected Marine ...'); the frozen scorer flags 17, the released scorer clears 8 and still flags 9: {'negation': 2, 'class_numeral_not_read': 1, 'other_cue_same_sentence': 4, 'later_sentence_national_status': 2}
  - a194 negation: "However, in South Korea, this species is not listed under any specific national conservation designation (e.g., Endangered Species or Marine Protected Species)."
  - a196 class_numeral_not_read: "In South Korea, this cold-water coral species is designated as a marine protected species under the Ministry of Oceans and Fisheries, classified as an "Endangered Marine Species" (Category II)."
  - a201 other_cue_same_sentence: "In South Korea, this soft coral species is designated as a **Marine Protected Species** under the Ministry of Oceans and Fisheries, specifically listed as an endangered marine organism."
  - a205 other_cue_same_sentence: "In South Korea, this soft coral species is designated as a **Marine Protected Species** under the Ministry of Oceans and Fisheries, specifically listed as an endangered marine organism."
  - a208 later_sentence_national_status: "This national status means it is legally protected from harvesting, trade, and habitat destruction."
  - a210 other_cue_same_sentence: "In South Korea, this soft coral species is designated as a **Marine Protected Species** under the Ministry of Oceans and Fisheries, specifically classified as an endangered marine organism."
  - a211 other_cue_same_sentence: "In South Korea, this stony coral is designated as a **Marine Protected Species** under the Ministry of Oceans and Fisheries, specifically listed as an endangered marine organism."
  - a217 later_sentence_national_status: "This national listing aims to protect its tidal flat habitats, which are threatened by coastal development and pollution."
  - a311 negation: "In South Korea, it is not listed under the national protected species designations (e.g., Endangered Wildlife or Marine Protected Species)."
- section3: 0 answers mention it (0 in the reversed order 'Protected Marine ...'); the frozen scorer flags 0, the released scorer clears 0 and still flags 0: {}

## Breadth of the Korea cue

Released cue `\b(korea|korean|national|nationally|ministry)\b|대한민국|국내|환경부`; narrow cue `\b(korea|korean)\b|대한민국|국내|환경부|\bministry\s+of\s+(?:the\s+)?environment\b|\bnational\s+designation\b`.

- heldout: the flag changes in 3 of 284 answers under the narrow cue: a106 (deepseek-chat) True->False; a208 (deepseek-chat) True->False; a217 (deepseek-chat) True->False
  - a106: "228** and classified as an **Endangered Species** under the national wildlife protection law."
  - a208: "This national status means it is legally protected from harvesting, trade, and habitat destruction."
  - a217: "This national listing aims to protect its tidal flat habitats, which are threatened by coastal development and pollution."
- section3: the flag changes in 0 of 30 answers under the narrow cue

- Section 3 answers counted as omitted only because of one of the two exclusions: 0 ({'names_iucn_or_red_list': [], 'national_red_list': []})

## Unclassed test met but flag off (class stated elsewhere in the answer)

- heldout: 45 of 284 (a034, a035, a039, a042, a045, a049, a051, a057, a058, a059, a067, a071, a076, a079, a081, a085, a087, a088, a094, a096, a097, a100, a102, a105, a107, a108, a111, a118, a135, a160, a163, a170, a179, a180, a207, a222, a226, a232, a254, a264, a275, a280, a283, a292, a303)
- section3: 2 of 30 (a006, a009)

## Released scorer on the same sample (not an independent estimate)

The released keb_score.py (SHA256 `0e4bdcba8b8d001bea9b2140940db2a9a6a80a34a92c5e693a9b1c1f9f82f593`) differs from the frozen version in three rules changed after this validation (see its docstring): 'protected' is not a cue inside 'Marine Protected Species' or 'protected area'; a Korean agency's Red List is a national list; 'not listed on the IUCN Red List as a threatened species' is not NE.

- IUCN categories 52/60; national class 60/60; unclassed flag 52/60; verdict 52/60

## Disagreements (frozen scorer)

- a124 *Sibynophis chinensis*: IUCN label ['NE'] / scorer []; national label ['II급'] / scorer ['II급']; unclassed label False / scorer False
- a132 *Microphysogobio koreensis*: IUCN label ['LC'] / scorer ['LC']; national label [] / scorer []; unclassed label False / scorer True
- a152 *Phoxinus phoxinus*: IUCN label ['NE'] / scorer []; national label [] / scorer []; unclassed label False / scorer True
- a188 *Charonia lampas*: IUCN label ['LC'] / scorer ['LC']; national label [] / scorer []; unclassed label False / scorer True
- a202 *Ellisella ceratophyta*: IUCN label ['NE'] / scorer ['NE']; national label [] / scorer []; unclassed label False / scorer True
- a209 *Nacospatangus alta*: IUCN label ['NE'] / scorer ['NE']; national label [] / scorer []; unclassed label False / scorer True
- a217 *Austruca lactea*: IUCN label ['NE'] / scorer ['NE']; national label [] / scorer []; unclassed label False / scorer True
- a234 *Eleutherococcus senticosus*: IUCN label ['NE'] / scorer []; national label [] / scorer []; unclassed label False / scorer True
- a241 *Drosera peltata var. nipponica*: IUCN label ['NE'] / scorer []; national label ['II급'] / scorer ['II급']; unclassed label False / scorer False
- a246 *Viola mirabilis*: IUCN label ['NE'] / scorer []; national label [] / scorer []; unclassed label False / scorer True
- a266 *Viburnum burejaeticum*: IUCN label ['NE'] / scorer ['NE']; national label [] / scorer []; unclassed label False / scorer True
- a277 *Aconitum austrokoreense*: IUCN label ['NE'] / scorer ['CR', 'NE']; national label [] / scorer []; unclassed label False / scorer False
- a298 *Isoetes coreana*: IUCN label ['NE'] / scorer []; national label [] / scorer []; unclassed label False / scorer False
- a308 *Habenaria radiata*: IUCN label ['NE'] / scorer []; national label ['I급'] / scorer ['I급']; unclassed label False / scorer False
- a311 *Dictyosphaeria cavernosa*: IUCN label ['NE'] / scorer []; national label [] / scorer []; unclassed label False / scorer True
