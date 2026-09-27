# National vs IUCN divergence (16-species file)

- Nationally designated species: 10
- Comparable (Global IUCN category on the ordinal scale): 8
- Divergent among comparable: 7 of 8
- Without the same-taxon condition (mismatch_type_any_concept): 9 of 10

## By type

### korea_stricter (6)
national designation more severe than the Global IUCN category

*Phoca largha*, *Lutra lutra*, *Bubo bubo*, *Grus japonensis*, *Kaloula borealis*, *Platalea minor*

### iucn_stricter (1)
Global IUCN category more severe than the national designation

*Mauremys reevesii*

### aligned (1)
same position on the display scale (control case)

*Pelophylax chosenicus*

### not_comparable (2)
no Global IUCN category on the ordinal scale for the designated taxon (includes species-rank assessments of designated subspecies); no gap computed

*Pteromys volans*, *Ursus thibetanus*

## Ordered by absolute gap

| Species | National | IUCN (scope) | Match status | Gap | Type | Gap, any concept |
|---|---|---|---|---|---|---|
| *Phoca largha* | I급 | LC (Global) | matched | +4 | korea_stricter | +4 |
| *Lutra lutra* | I급 | NT (Global) | matched | +3 | korea_stricter | +3 |
| *Bubo bubo* | II급 | LC (Global) | matched | +2 | korea_stricter | +2 |
| *Grus japonensis* | I급 | VU (Global) | matched | +2 | korea_stricter | +2 |
| *Kaloula borealis* | II급 | LC (Global) | matched | +2 | korea_stricter | +2 |
| *Platalea minor* | I급 | VU (Global) | matched | +2 | korea_stricter | +2 |
| *Mauremys reevesii* | II급 | EN (Global) | matched | -1 | iucn_stricter | -1 |
| *Pelophylax chosenicus* | II급 | VU (Global) | matched | +0 | aligned | +0 |
| *Pteromys volans* | II급 | LC (Global) | matched_at_species_rank |  | not_comparable | +2 |
| *Ursus thibetanus* | I급 | VU (Global) | matched_at_species_rank |  | not_comparable | +2 |

The gap is a display ordering (sign and relative magnitude only); see schema_notes.severity_gap in k_endangered_bench_v1.json.
