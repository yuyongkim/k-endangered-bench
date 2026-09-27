"""Reference scorer for K-EndangeredBench status answers (English text, standard library only).

Licence: MIT (code). Shipped in the release archive as scoring/keb_score.py and used by the
paper's usage example (§2.9) and by paper02_bench/scripts/example_application.py.

    from keb_score import score
    score(record, "The spotted seal is listed as Least Concern on the IUCN Red List.")

A status answer usually speaks for two authorities at once. The scorer first decides which
authority each passage speaks for, then compares the values stated there with the record:
  - IUCN categories are read only from clauses that mention the IUCN or the Red List. A clause
    about a national or Korean Red List (the National Institute of Biological Resources list)
    is not an IUCN statement. A line that names the IUCN or the Red List but states no category
    (a heading) passes that attribution to the following line.
  - Inside an IUCN clause, a national class phrase ("Class I Endangered", "Endangered Wildlife
    Class II", "first-class endangered species") is removed before categories are read.
  - "Not (yet) (been) (formally) evaluated/assessed", "not (currently) listed on/in the IUCN ...",
    "no (current|global) IUCN (Red List) assessment/category/listing" and "(NE)" are read as NE.
  - National classes ("Class I", "Class-II", "Grade 1", "first-class", "Endangered Species I",
    "I급", "1급") are read from any sentence. national_unclassed is a surface test (v1.0.9
    wording): a sentence that contains a Korea cue (Korea, Korean, national, nationally, any
    ministry, 대한민국, 국내, 환경부), states no class, names neither the IUCN nor the Red List, is not
    about a national Red List, and contains one of the words endangered, threatened, vulnerable
    or protected anywhere in it (whatever the word refers to) sets it, unless the answer states
    a class in any sentence.
Segmentation (v1.0.9 wording; unchanged behaviour):
  - Sentences are split after every ".", "!" or "?" followed by white space and at line breaks,
    including after abbreviations ("No. 228", "var."), so an abbreviation can move a cue or an
    NE phrase into another sentence.
  - Inside a sentence that names the IUCN or the Red List, categories are read only from the
    clauses that do, splitting at ";", " while ", " whereas ", ", but " and " and ".
  - A line shorter than 80 characters that names the IUCN or the Red List and states no category
    passes the IUCN attribution to the next sentence (a heading).
  - "Regional Red List" and "Red Data Book" of a national or Korean body count as national lists.
Matching rules, each with the failing case it prevents:
  - Whole words, longest phrase first: "critically endangered" is CR and is removed before
    "endangered" is looked for, so it never also counts as EN.
  - "endangered wildlife" / "endangered species" (the name of the national list) is not an
    IUCN category.
  - Class numerals are whole tokens: "Class II" is II and never also "Class I".
  - A code in parentheses, e.g. "(VU)", counts as that category.
  - "downlisted from Endangered" / "uplisted from ..." is history, not the current category.
Status-aware verdict (iucn_verdict): the record's iucn_match_status and iucn_concept_relation
decide whether a stated category can be judged at all.
  - correct / wrong: the record carries a category for the designated taxon or its species.
  - For `not_assessed` records of the same concept, NE is correct and any category is wrong
    (no assessment exists to support it).
  - unverified: the record carries no usable reference (name_unresolved, no_current_assessment,
    via_unaccepted_gbif_match, a relation uncertain or different_taxon, or not_assessed of
    another concept); a stated category is neither confirmed nor refuted.
It is a reference implementation for worked examples. Its agreement with hand labels on a
held-out sample is reported in scorer_validation.md. That validation was run on the version
frozen before labelling (keb_score_frozen_for_validation.py in the repository). This file
differs from it in three rules, all changed after the validation, which therefore does not
estimate their effect:
  - "protected" is a cue for national_unclassed, as in the frozen version, except inside the
    name of another instrument ("Marine Protected Species", "protected area"). v1.0.4 had
    dropped the cue altogether, which moved one Section 3 answer ("Protected Wild Animal")
    from unclassed to omitted; v1.0.5 restores it with this exception.
  - A Red List attributed to a Korean agency ("the Korea Forest Service's Red List", "the
    Ministry of Environment's Red List", "the NIBR Red List", "the Red List of Korea") is a
    national list, not the IUCN.
  - "not listed on the IUCN Red List as a (globally) threatened species" is not read as NE.
National class phrases are removed from IUCN clauses in these forms only: "Class I|II
[Endangered [Wildlife|Species|Plant]]", the same with Grade, Category or Level, "Endangered
Wildlife|Species [of] Class|Grade I|II" and "first-|second-class endangered [wildlife|species]".
Other orders ("Endangered, Class I", "Endangered (Class I)", "Class I, Endangered") leave the
IUCN word in place and can make the IUCN reading ambiguous, and "Level I" and "Category I" are
removed but not read as a national class. It does not read negation ("not listed as
endangered" in a Korean sentence still sets national_unclassed) or hedges beyond the NE
phrases above, it misses some NE phrasings ("does not currently assess", "has not formally
assessed"), and it reads English only.
"""

from __future__ import annotations

import re

IUCN_PHRASES = [("CR", "critically endangered"), ("EW", "extinct in the wild"),
                ("EX", "extinct"), ("EN", "endangered"), ("VU", "vulnerable"),
                ("NT", "near threatened"), ("LC", "least concern"), ("DD", "data deficient")]
_CAT = "|".join(p for _, p in IUCN_PHRASES)
NATIONAL = {"i": "I급", "1": "I급", "ii": "II급", "2": "II급", "first": "I급", "second": "II급"}
KOREA = re.compile(r"\b(korea|korean|national|nationally|ministry)\b|대한민국|국내|환경부")
NATIONAL_RED_LIST = re.compile(
    r"\b(?:national|korean|korea's|south korean|regional|korea\s+national)\s+red\s+(?:list|data\s+book)"
    r"|\b(?:korea\s+forest\s+service|ministry\s+of\s+environment|national\s+institute\s+of\s+"
    r"biological\s+resources|nibr|kfs|korea\s+national\s+arboretum)(?:'s|’s)?\s+"
    r"(?:\([a-z]+\)\s+)?red\s+(?:list|data\s+book)"
    r"|\bred\s+(?:list|data\s+book)\s+of\s+(?:south\s+)?korea")
# Names of other instruments that contain "protected"; removed before the unclassed cue test.
OTHER_INSTRUMENT = re.compile(r"\bmarine\s+protected\s+(?:species|organisms?|marine\s+life|animals?)\b"
                              r"|\bprotected\s+areas?\b")
NE_PATTERNS = [r"\bnot\s+(?:yet\s+)?(?:been\s+)?(?:formally\s+)?(?:evaluated|assessed)\b",
               r"\bnot\s+(?:currently\s+)?listed\s+(?:on|in)\s+the\s+iucn\b"
               r"(?!(?:\s+red\s+list)?\s+as\s+(?:a\s+)?(?:globally\s+)?threatened)",
               r"\bno\s+(?:current\s+|global\s+)?iucn\s+(?:red\s+list\s+)?(?:assessment|category|listing)\b",
               r"\(ne\)"]
# National class phrases, removed from IUCN clauses before categories are read.
NATIONAL_PHRASE = re.compile(
    r"\b(?:class|grade|category|level)[\s\-]*(?:ii|i|2|1)\b(?:\s+endangered(?:\s+(?:wildlife|wild\s+animals?|species|plants?))?)?"
    r"|\bendangered\s+(?:wildlife|species)\s+(?:of\s+)?(?:class|grade)[\s\-]*(?:ii|i|2|1)\b"
    r"|\b(?:first|second)[\s\-]class\s+endangered(?:\s+(?:wildlife|species))?")

UNUSABLE_STATUS = ("name_unresolved", "no_current_assessment", "via_unaccepted_gbif_match",
                   "name_unresolved_via_gbif", "no_global_category_via_gbif")


def sentences(text: str) -> list[str]:
    return [s for s in re.split(r"(?<=[.!?])\s+|\n+", text) if s.strip()]


def national_classes(text: str) -> set[str]:
    t = text.replace("Ⅱ", "II").replace("Ⅰ", "I").replace("ⅱ", "ii").replace("ⅰ", "i")
    low = t.lower()
    found = re.findall(r"\b(?:class|grade)[\s\-]*(ii|i|2|1)\b", low)
    found += re.findall(r"(?<![a-z0-9])(ii|i|2|1)\s*급", low)
    found += re.findall(r"\b(first|second)[\s\-]class\b", low)
    # "Endangered Species I" / "Endangered Wildlife II": case-sensitive numeral
    found += [m.lower() for m in re.findall(r"Endangered\s+(?:Wildlife|Species)\s+(II|I)\b", t)]
    return {NATIONAL[m] for m in found}


def iucn_categories(text: str) -> set[str]:
    t = text.lower()
    t = NATIONAL_PHRASE.sub(" ", t)
    t = re.sub(r"\b(?:down|up)?listed\s+from\s+(?:" + _CAT + r")\b", " ", t)
    t = re.sub(r"\bendangered\s+(?:wildlife|wild animals?|species)\b", " ", t)
    found: set[str] = set()
    for pat in NE_PATTERNS:
        if re.search(pat, t):
            found.add("NE")
            t = re.sub(pat, " ", t)
    found |= {m.upper() for m in re.findall(r"\((cr|en|vu|nt|lc|dd|ew|ex)\)", t)}
    for code, phrase in IUCN_PHRASES:
        pat = r"\b" + phrase.replace(" ", r"\s+") + r"\b"
        if re.search(pat, t):
            found.add(code)
            t = re.sub(pat, " ", t)
    return found


def _names_iucn(low: str) -> bool:
    if "iucn" in low:
        return True
    return "red list" in low and not NATIONAL_RED_LIST.search(low)


def iucn_clauses(sentence: str) -> list[str]:
    """The parts of a sentence that speak for the IUCN."""
    parts = re.split(r";|\s+while\s+|\s+whereas\s+|,\s+but\s+|\s+and\s+", sentence)
    keep = [p for p in parts if _names_iucn(p.lower())]
    return keep


def statements(text: str) -> dict:
    iucn, national, unclassed = set(), set(), False
    carry = False
    for s in sentences(text):
        low = s.lower()
        clauses = iucn_clauses(s) if _names_iucn(low) else ([s] if carry else [])
        got: set[str] = set()
        for c in clauses:
            got |= iucn_categories(c)
        iucn |= got
        # A heading such as "IUCN Red List Category:" passes attribution to the next line.
        carry = _names_iucn(low) and not got and len(s) < 80
        cls = national_classes(s)
        national |= cls
        if not cls and KOREA.search(low) and not _names_iucn(low) \
                and not NATIONAL_RED_LIST.search(low) \
                and re.search(r"\bendangered\b|\bvulnerable\b|\bthreatened\b|\bprotected\b",
                              OTHER_INSTRUMENT.sub(" ", low)):
            unclassed = True
    return {"iucn": iucn, "national": national, "national_unclassed": unclassed and not national}


def iucn_verdict(rec: dict, stated: set[str]) -> str:
    """correct | wrong | unverified | ambiguous | not_stated (see module docstring)."""
    if not stated:
        return "not_stated"
    status = rec.get("iucn_match_status")
    rel = rec.get("iucn_concept_relation")
    cat = rec.get("iucn_category")
    if status in UNUSABLE_STATUS or rel in ("uncertain", "different_taxon"):
        return "unverified"
    if status == "not_assessed":
        if rel != "same":
            return "unverified"
        return "correct" if stated == {"NE"} else "wrong"
    if not cat:
        return "unverified"
    if len(stated) > 1:
        return "correct" if stated == {cat} else "ambiguous"
    return "correct" if stated == {cat} else "wrong"


def score(rec: dict, text: str) -> dict:
    st = statements(text)
    iu, na = st["iucn"], st["national"]
    v = iucn_verdict(rec, iu)
    return {"iucn_stated": sorted(iu),
            "iucn_correct": True if v == "correct" else False if v in ("wrong", "ambiguous") else None,
            "iucn_verdict": v,
            "national_stated": sorted(na),
            "national_correct": (na == {rec["korea_statutory_grade"]}) if na else None,
            "national_unclassed": st["national_unclassed"]}
