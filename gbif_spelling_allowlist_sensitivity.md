# GBIF spelling allow-list: sensitivity of the census

Run with `KEB_GBIF_SPELLING_ALLOWLIST=data/statute/gbif_spelling_allowlist.json`, compared with the release build (allow-list off). Columns: status, category, IUCN name, GBIF gate.

| Designated name | Grade | Release | With allow-list | Relation | mismatch_type |
|---|---|---|---|---|---|
| Gobiobotia nakdongensis | I급 | name_unresolved, None, None, False | matched_via_synonym, CR, Gobiobotia naktongensis, True | same | aligned |
| Pseudopungtungia tenuicorpa | II급 | name_unresolved, None, None, False | not_assessed, None, Pseudopungtungia tenuicorpus, True | same | not_comparable |
| Lethenteron japonicus | II급 | via_unaccepted_gbif_match, LC, Lethenteron camtschaticum, False | matched_via_synonym, LC, Lethenteron camtschaticum, True | uncertain | not_comparable |
| Lethocerus deyrolli | II급 | name_unresolved, None, None, False | name_unresolved, None, None, True | None | not_comparable |
| Acoptolabrus changeonleei | II급 | via_unaccepted_gbif_match, None, Carabus changgeonleei, False | not_assessed, None, Carabus changgeonleei, True | same | not_comparable |
| Nacospatangus alta | II급 | name_unresolved, None, None, False | name_unresolved, None, None, True | None | not_comparable |
| Plumarella adhaerens | II급 | name_unresolved, None, None, False | name_unresolved, None, None, True | None | not_comparable |
| Metanarthecium luteo-viride | II급 | not_assessed, None, Metanarthecium luteo-viride, False | not_assessed, None, Metanarthecium luteo-viride, True | same | not_comparable |

Records that change: 8.
