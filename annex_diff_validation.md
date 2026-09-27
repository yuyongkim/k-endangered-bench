# Validation of the diff step on the 2022 amendment

Written by `paper02_bench/scripts/validate_annex_diff.py` (local files only).

- Before: Enforcement Rule as amended by Ministry of Environment Ordinance No. 942 (환경부령 제942호), promulgated and in force 2021-09-16; law.go.kr MST 235675; https://www.law.go.kr/LSW/flDownload.do?flSeq=107653023 (SHA256 `f7de4c2052e0070a43d83065385973e244e660e2a191faa8a0aa5357a9958ca3`)
- After: the pinned annex (SHA256 `4f75d4f8f92b8d7381b345cd89757672fc2e869bb75264eec2ab580a579945b4`)
- Reference: Ministry of Environment, Nature Conservation Bureau, Biodiversity Division (환경부 자연보전국 생물다양성과), "멸종위기 야생생물, 267종에서 282종으로 개정", 2022-12-09; https://www.korea.kr/common/download.do?fileId=197531828&tblKey=GMN (SHA256 `19c7f5912d64d5aef5799d2b62ddc80824be018189f57b633d931db2d66efab5`)
- Rows parsed: before 266 (+1 recovered: 화경버섯 Lampteromyces japonicus), after 282

## Totals by group (Class I / Class II)

| Group | Press release, before | Parsed, before | Press release, after | Parsed, after |
|---|---|---|---|---|
| 포유류 | [12, 8] | [12, 8] | [14, 6] | [14, 6] |
| 조류 | [14, 49] | [14, 49] | [16, 53] | [16, 53] |
| 양서류·파충류 | [2, 6] | [2, 6] | [2, 6] | [2, 6] |
| 어류 | [11, 16] | [11, 16] | [11, 18] | [11, 18] |
| 곤충류 | [6, 20] | [6, 20] | [8, 21] | [8, 21] |
| 무척추동물 | [4, 28] | [4, 28] | [4, 28] | [4, 28] |
| 육상식물 | [11, 77] | [11, 77] | [13, 79] | [13, 79] |
| 해조류 | [0, 2] | [0, 2] | [0, 2] | [0, 2] |
| 고등균류 | [0, 1] | [0, 0] | [0, 1] | [0, 1] |

## Diff step against the press release

| Change | Press release | Diff step | Matched | Only in diff step | Only in press release |
|---|---|---|---|---|---|
| new | 19 | 21 | 19 | 한국꼬마잠자리, 화경솔밭버섯 | - |
| removed | 4 | 5 | 4 | 꼬마잠자리 | - |
| upgraded_II_to_I | 8 | 8 | 8 | - | - |
| downgraded_I_to_II | 1 | 1 | 1 | - | - |

With the unnumbered row recovered:

| Change | Press release | Diff step | Matched | Only in diff step | Only in press release |
|---|---|---|---|---|---|
| new | 19 | 21 | 19 | 한국꼬마잠자리, 화경솔밭버섯 | - |
| removed | 4 | 6 | 4 | 꼬마잠자리, 화경버섯 | - |
| upgraded_II_to_I | 8 | 8 | 8 | - | - |
| downgraded_I_to_II | 1 | 1 | 1 | - | - |

Renamed entries reported by the diff step: 25

- 토끼박쥐 Plecotus auritus -> 토끼박쥐 Plecotus ognevi
- 수원청개구리 Hyla suweonensis -> 수원청개구리 Dryophytes suweonensis
- 고리도룡뇽 Hynobius yangi -> 고리도롱뇽 Hynobius yangi
- 닻무늬길앞잡이 Cicindela anchoralis -> 닻무늬길앞잡이 Cicindela (Abroscelis) anchoralis
- 비단벌레 Chrysochroa coreana -> 비단벌레 Chrysochroa (Chrysochroa) coreana
- 장수하늘소 Callipogon relictus -> 장수하늘소 Callipogon (Eoxenus) relictus
- 멋조롱박딱정벌레 Damaster mirabilissimus mirabilissimus -> 멋조롱박딱정벌레 Acoptolabrus mirabilissimus mirabilissimus
- 물방개 Cybister chinensis -> 물방개 Cybister (Cybister) chinensis
- 소똥구리 Gymnopleurus mopsus -> 소똥구리 Gymnopleurus (Gymnopleurus) mopsus
- 애기뿔소똥구리 Copris tripartitus -> 애기뿔소똥구리 Copris (Copris) tripartitus
- 참호박뒤영벌 Bombus koreanus -> 참호박뒤영벌 Bombus (Megabombus) koreanus
- 창언조롱박딱정벌레 Damaster changeonleei -> 창언조롱박딱정벌레 Acoptolabrus changeonleei
- 큰자색호랑꽃무지 Osmoderma opicum -> 큰자색호랑꽃무지 Osmoderma caeleste
- 나팔고둥 Charonia lampas sauliae -> 나팔고둥 Charonia lampas
- 두드럭조개 Lamprotula coreana -> 두드럭조개 Aculamprotula coreana
- 기수갈고둥 Clithon retropictus -> 기수갈고둥 Clithon retropictum
- 별혹산호 Verrucella stellata -> 별혹산호 Ellisella ceratophyta
- 흰발농게 Uca lactea -> 흰발농게 Austruca lactea
- 한라솜다리 Leontopodium hallaisanense -> 한라솜다리 Leontopodium coreanum var. hallaisanense
- 구름병아리난초 Gymnadenia cucullata -> 구름병아리난초 Neottianthe cucullata
- 기생꽃 Trientalis europaea ssp. arctica -> 기생꽃 Trientalis europaea subsp. arctica
- 백운란 Vexillabium yakusimensis var. nakaianum -> 백운란 Kuhlhasseltia nakaiana
- 섬개현삼 Scrophularia takesimensis -> 섬현삼 Scrophularia takesimensis
- 참닻꽃 Halenia corniculata -> 참닻꽃 Halenia coreana
- 홍월귤 Arctous alpinus var. japonicus -> 홍월귤 Arctous rubra

## Classes of the renamed entries (not validated against the press release)

Source: `data/statute/amendment_2022_rename_classes.json` (by the authors with AI assistance). concept 6, nomenclatural 8, spelling 4, subgenus 7; subclasses: nomenclatural/rank_change 2, spelling/korean_name_only 2, spelling/scientific_name_spelling 2.

| From | To | Class | Note |
|---|---|---|---|
| 토끼박쥐 Plecotus auritus | 토끼박쥐 Plecotus ognevi | concept | Korean populations assigned to P. ognevi after the split of P. auritus |
| 수원청개구리 Hyla suweonensis | 수원청개구리 Dryophytes suweonensis | nomenclatural | genus transfer; since v1.0.6 the IUCN relation is uncertain (southern populations described as D. flaviventris, Borzee et al. 2020) |
| 고리도룡뇽 Hynobius yangi | 고리도롱뇽 Hynobius yangi | spelling | Korean name 고리도룡뇽 -> 고리도롱뇽 |
| 닻무늬길앞잡이 Cicindela anchoralis | 닻무늬길앞잡이 Cicindela (Abroscelis) anchoralis | subgenus |  |
| 비단벌레 Chrysochroa coreana | 비단벌레 Chrysochroa (Chrysochroa) coreana | subgenus |  |
| 장수하늘소 Callipogon relictus | 장수하늘소 Callipogon (Eoxenus) relictus | subgenus |  |
| 멋조롱박딱정벌레 Damaster mirabilissimus mirabilissimus | 멋조롱박딱정벌레 Acoptolabrus mirabilissimus mirabilissimus | nomenclatural | genus placement |
| 물방개 Cybister chinensis | 물방개 Cybister (Cybister) chinensis | subgenus |  |
| 소똥구리 Gymnopleurus mopsus | 소똥구리 Gymnopleurus (Gymnopleurus) mopsus | subgenus |  |
| 애기뿔소똥구리 Copris tripartitus | 애기뿔소똥구리 Copris (Copris) tripartitus | subgenus |  |
| 참호박뒤영벌 Bombus koreanus | 참호박뒤영벌 Bombus (Megabombus) koreanus | subgenus |  |
| 창언조롱박딱정벌레 Damaster changeonleei | 창언조롱박딱정벌레 Acoptolabrus changeonleei | nomenclatural | genus placement |
| 큰자색호랑꽃무지 Osmoderma opicum | 큰자색호랑꽃무지 Osmoderma caeleste | concept | Korean populations re-identified as O. caeleste |
| 나팔고둥 Charonia lampas sauliae | 나팔고둥 Charonia lampas | concept | subspecies widened to the species |
| 두드럭조개 Lamprotula coreana | 두드럭조개 Aculamprotula coreana | nomenclatural | genus transfer |
| 기수갈고둥 Clithon retropictus | 기수갈고둥 Clithon retropictum | spelling | epithet ending |
| 별혹산호 Verrucella stellata | 별혹산호 Ellisella ceratophyta | concept | re-identification under another genus and epithet |
| 흰발농게 Uca lactea | 흰발농게 Austruca lactea | nomenclatural | genus transfer |
| 한라솜다리 Leontopodium hallaisanense | 한라솜다리 Leontopodium coreanum var. hallaisanense | nomenclatural | species reduced to a variety; same populations |
| 구름병아리난초 Gymnadenia cucullata | 구름병아리난초 Neottianthe cucullata | nomenclatural | genus transfer |
| 기생꽃 Trientalis europaea ssp. arctica | 기생꽃 Trientalis europaea subsp. arctica | spelling | rank abbreviation |
| 백운란 Vexillabium yakusimensis var. nakaianum | 백운란 Kuhlhasseltia nakaiana | nomenclatural | new combination at species rank; variety raised to species (change of rank) |
| 섬개현삼 Scrophularia takesimensis | 섬현삼 Scrophularia takesimensis | spelling | Korean name 섬개현삼 -> 섬현삼 |
| 참닻꽃 Halenia corniculata | 참닻꽃 Halenia coreana | concept | Korean populations treated as a separate species |
| 홍월귤 Arctous alpinus var. japonicus | 홍월귤 Arctous rubra | concept | re-identification; the IUCN relation of A. rubra is uncertain in this release |

Pairs that appear as one addition and one removal:

- Lampteromyces japonicus -> Omphalotus guepiniiformis: nomenclatural (the same fungus transferred to Omphalotus (GBIF Backbone: L. japonicus is a synonym of O. guepiniiformis); Korean name 화경버섯 -> 화경솔밭버섯)
- Nannophya pygmaea -> Nannophya koreana: concept (the Korean populations described as a new species, N. koreana Bae, 2020 (Bae et al. 2020, J Species Res 9:1-10, doi:10.12651/JSR.2020.9.1.001); the unit narrows to Korea)
