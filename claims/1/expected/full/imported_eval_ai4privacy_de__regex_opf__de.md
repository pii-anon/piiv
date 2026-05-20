# Imported-dataset eval - ai4privacy_de

- Rows evaluated: **1,000**
- Rows with zero gold spans (after label-map filter): **37**
- Elapsed: **3270.9s** (3271ms/row)
- Projection-symmetric scoring: **on** (gold placeholder space: `[DATE], [EMAIL], [PERSON_NAME], [PHONE], [STREET_ADDRESS]`)

## Per-placeholder precision / recall

| Placeholder | Precision (95% CI) | Recall (95% CI) | F1 (95% CI) | TP | FP | FN | Support |
|---|---|---|---|---:|---:|---:|---:|
| `[DATE]` | 0.914 [0.885, 0.940] | 1.000 [1.000, 1.000] | 0.955 [0.939, 0.969] | 328 | 31 | 0 | 328 |
| `[EMAIL]` | 0.998 [0.994, 1.000] | 1.000 [1.000, 1.000] | 0.999 [0.997, 1.000] | 538 | 1 | 0 | 538 |
| `[PERSON_NAME]` | 0.873 [0.852, 0.895] | 0.797 [0.769, 0.828] | 0.834 [0.813, 0.852] | 634 | 92 | 161 | 795 |
| `[PHONE]` | 0.721 [0.687, 0.759] | 0.915 [0.887, 0.942] | 0.807 [0.780, 0.835] | 378 | 146 | 35 | 413 |
| `[STREET_ADDRESS]` | 0.732 [0.698, 0.768] | 0.619 [0.579, 0.657] | 0.671 [0.642, 0.697] | 345 | 126 | 212 | 557 |
| **macro** | 0.848 [0.835, 0.860] | 0.866 [0.855, 0.877] | 0.857 [0.847, 0.867] | 2223 | 396 | 408 | 2631 |
| **micro** | 0.849 [0.835, 0.863] | 0.845 [0.831, 0.858] | 0.847 [0.836, 0.857] | 2223 | 396 | 408 | 2631 |

## Per-length-bucket precision / recall

Row distribution across buckets: `sentence`: 690, `paragraph`: 114, `multi_paragraph`: 54, `structured`: 142

### `sentence` (690 rows)

| Placeholder | Precision (95% CI) | Recall (95% CI) | F1 (95% CI) | TP | FP | FN | Support |
|---|---|---|---|---:|---:|---:|---:|
| `[DATE]` | 0.928 [0.892, 0.960] | 1.000 [1.000, 1.000] | 0.963 [0.943, 0.980] | 181 | 14 | 0 | 181 |
| `[EMAIL]` | 1.000 [1.000, 1.000] | 1.000 [1.000, 1.000] | 1.000 [1.000, 1.000] | 304 | 0 | 0 | 304 |
| `[PERSON_NAME]` | 0.881 [0.852, 0.912] | 0.796 [0.755, 0.831] | 0.836 [0.809, 0.861] | 362 | 49 | 93 | 455 |
| `[PHONE]` | 0.743 [0.694, 0.789] | 0.924 [0.889, 0.956] | 0.824 [0.789, 0.856] | 208 | 72 | 17 | 225 |
| `[STREET_ADDRESS]` | 0.755 [0.710, 0.804] | 0.568 [0.515, 0.617] | 0.648 [0.607, 0.687] | 200 | 65 | 152 | 352 |
| **macro** | 0.861 [0.845, 0.878] | 0.858 [0.842, 0.873] | 0.859 [0.846, 0.873] | 1255 | 200 | 262 | 1517 |
| **micro** | 0.863 [0.846, 0.881] | 0.827 [0.807, 0.846] | 0.845 [0.831, 0.859] | 1255 | 200 | 262 | 1517 |

### `paragraph` (114 rows)

| Placeholder | Precision (95% CI) | Recall (95% CI) | F1 (95% CI) | TP | FP | FN | Support |
|---|---|---|---|---:|---:|---:|---:|
| `[DATE]` | 0.855 [0.754, 0.936] | 1.000 [1.000, 1.000] | 0.922 [0.860, 0.967] | 47 | 8 | 0 | 47 |
| `[EMAIL]` | 1.000 [1.000, 1.000] | 1.000 [1.000, 1.000] | 1.000 [1.000, 1.000] | 79 | 0 | 0 | 79 |
| `[PERSON_NAME]` | 0.904 [0.844, 0.959] | 0.781 [0.689, 0.876] | 0.838 [0.774, 0.898] | 75 | 8 | 21 | 96 |
| `[PHONE]` | 0.866 [0.781, 0.944] | 0.879 [0.791, 0.949] | 0.872 [0.803, 0.932] | 58 | 9 | 8 | 66 |
| `[STREET_ADDRESS]` | 0.735 [0.625, 0.849] | 0.514 [0.397, 0.629] | 0.605 [0.509, 0.692] | 36 | 13 | 34 | 70 |
| **macro** | 0.872 [0.834, 0.909] | 0.835 [0.799, 0.870] | 0.853 [0.823, 0.884] | 295 | 38 | 63 | 358 |
| **micro** | 0.886 [0.847, 0.920] | 0.824 [0.782, 0.866] | 0.854 [0.821, 0.886] | 295 | 38 | 63 | 358 |

### `multi_paragraph` (54 rows)

| Placeholder | Precision (95% CI) | Recall (95% CI) | F1 (95% CI) | TP | FP | FN | Support |
|---|---|---|---|---:|---:|---:|---:|
| `[DATE]` | 0.875 [0.750, 0.972] | 1.000 [1.000, 1.000] | 0.933 [0.857, 0.986] | 28 | 4 | 0 | 28 |
| `[EMAIL]` | 1.000 [1.000, 1.000] | 1.000 [1.000, 1.000] | 1.000 [1.000, 1.000] | 49 | 0 | 0 | 49 |
| `[PERSON_NAME]` | 0.853 [0.778, 0.931] | 0.790 [0.694, 0.881] | 0.821 [0.752, 0.882] | 64 | 11 | 17 | 81 |
| `[PHONE]` | 0.615 [0.531, 0.725] | 0.865 [0.750, 0.971] | 0.719 [0.637, 0.800] | 32 | 20 | 5 | 37 |
| `[STREET_ADDRESS]` | 0.718 [0.595, 0.875] | 0.683 [0.537, 0.816] | 0.700 [0.586, 0.800] | 28 | 11 | 13 | 41 |
| **macro** | 0.812 [0.765, 0.865] | 0.868 [0.830, 0.908] | 0.839 [0.801, 0.878] | 201 | 46 | 35 | 236 |
| **micro** | 0.814 [0.762, 0.864] | 0.852 [0.809, 0.895] | 0.832 [0.791, 0.872] | 201 | 46 | 35 | 236 |

### `structured` (142 rows)

| Placeholder | Precision (95% CI) | Recall (95% CI) | F1 (95% CI) | TP | FP | FN | Support |
|---|---|---|---|---:|---:|---:|---:|
| `[DATE]` | 0.935 [0.881, 0.985] | 1.000 [1.000, 1.000] | 0.966 [0.937, 0.993] | 72 | 5 | 0 | 72 |
| `[EMAIL]` | 0.991 [0.969, 1.000] | 1.000 [1.000, 1.000] | 0.995 [0.984, 1.000] | 106 | 1 | 0 | 106 |
| `[PERSON_NAME]` | 0.847 [0.799, 0.900] | 0.816 [0.750, 0.886] | 0.831 [0.792, 0.875] | 133 | 24 | 30 | 163 |
| `[PHONE]` | 0.640 [0.562, 0.713] | 0.941 [0.887, 0.987] | 0.762 [0.701, 0.815] | 80 | 45 | 5 | 85 |
| `[STREET_ADDRESS]` | 0.686 [0.625, 0.755] | 0.862 [0.789, 0.929] | 0.764 [0.711, 0.816] | 81 | 37 | 13 | 94 |
| **macro** | 0.820 [0.794, 0.845] | 0.924 [0.902, 0.944] | 0.869 [0.850, 0.887] | 472 | 112 | 48 | 520 |
| **micro** | 0.808 [0.777, 0.839] | 0.908 [0.879, 0.934] | 0.855 [0.833, 0.876] | 472 | 112 | 48 | 520 |


## False-positive samples

### `[DATE]`
- `ai4p-de-20695161` [regex] value=`74-64.963`  context: ...'k.com oder telefonisch unter +74-64.963 5015. Für die Anmeldung benöt'...
- `ai4p-de-20695280` [regex] value=`27.46.19`  context: ...'rreichen Sie mich unter 03.98 27.46.19 oder per E‑Mail an FML@gmail.'...
- `ai4p-de-20695572` [regex] value=`97.84-776`  context: ...'ail: 27TS@gmail.com\nTelefon: +97.84-776.9908\nAdresse: Dr.-Fritz-Dörfl'...
- `ai4p-de-20695574` [regex] value=`06-67.66`  context: ...' E‑Mail KR@gmail.com, Telefon 06-67.66.92-78. Sollten Sie weitere Fr'...
- `ai4p-de-20695577` [regex] value=`54.28.326`  context: ...' Media mit der Telefonnummer +54.28.326.5276.'...

### `[EMAIL]`
- `ai4p-de-20695252` [regex] value=`support@company.at`  context: ...'otonmail.com>\nAn: IT‑Support <support@company.at>\nDatum: 12/03/1946\nBetreff: P'...

### `[PERSON_NAME]`
- `ai4p-de-20694943` [opf] value=`Meister`  context: ...': Esranur Anka Strauch\nTitel: Meister\nGeburtsdatum: März/75\nAlter: '...
- `ai4p-de-20694963` [opf] value=`Alosius Gyárfás`  context: ...' Unterschrift Maryléne Gossen Alosius Gyárfás – begleitet von einem Datum M'...
- `ai4p-de-20694966` [opf] value=`Frau Müller`  context: ...'n.\nFür Rückfragen steht Ihnen Frau Müller unter +43.110.380-4965 zur Ve'...
- `ai4p-de-20694974` [opf] value=`Bgm`  context: ...')\n\nName: Nedzmi Ai Gob\nTitel: Bgm\nGeburtsdatum: 10/06/1972\nAlte'...
- `ai4p-de-20695049` [opf] value=`Abdelaâziz Bosgiraud`  context: ...':\n\nSehr geehrte/r Bgm Alieren Abdelaâziz Bosgiraud,\nWir freuen uns, Ihnen mittei'...

### `[PHONE]`
- `ai4p-de-20694923` [opf] value=`2200906163294476`  context: ...'n einen monatlichen Bonus von 2200906163294476.'...
- `ai4p-de-20694943` [opf] value=`93-2661087`  context: ...'n‑Nr.: 162MA0EJ50\nSteuer‑Nr.: 93-2661087\nIch bestätige, dass ich die S'...
- `ai4p-de-20694945` [opf] value=`3502726574080664`  context: ...'Rechnung Nr. 3502726574080664\nAusgestellt am: 12/08/2015\nKu'...
- `ai4p-de-20694954` [opf] value=`08-7435422`  context: ...' Steuer‑Identifikationsnummer 08-7435422 im Produktionsdossier.'...
- `ai4p-de-20694958` [regex] value=`0901 700729
12`  context: ...'. Sozialversicherungs‑Nummer: 0901 700729\n12. Steuer‑Identifikationsnummer'...

### `[STREET_ADDRESS]`
- `ai4p-de-20694945` [opf] value=`Bürgermeisterin Lourin Buffo Kottler`  context: ...'t am: 12/08/2015\nKundendaten:\nBürgermeisterin Lourin Buffo Kottler\nSandgasse 1437\n6020 Linz\nE‑Ma'...
- `ai4p-de-20694955` [opf] value=`Asan Kubisa Kodeeswaran Natsvlishvili`  context: ...'Der Kameramann, Asan Kubisa Kodeeswaran Natsvlishvili, gibt seine Sozialversicherun'...
- `ai4p-de-20694978` [opf] value=`Sparbeggweg`  context: ...' +33 757 362 7862\nAdresse: 72 Sparbeggweg, 4020 Wien\nStaatsangehörigkei'...
- `ai4p-de-20694978` [opf] value=`4020 Wien`  context: ...'7862\nAdresse: 72 Sparbeggweg, 4020 Wien\nStaatsangehörigkeit (falls er'...
- `ai4p-de-20695092` [opf] value=`Robert-Alain Nemorino van Lotringen`  context: ...'n Namen des Betriebsinhabers: Robert-Alain Nemorino van Lotringen (Geburtsdatum: 11/12/1951, Al'...


## False-negative samples

### `[PERSON_NAME]`
- `ai4p-de-20694936` value=`Ricco Tsakalos`  context: ...'Der Projektleiter, Meister Ricco Tsakalos, weist darauf hin, dass das E'...
- `ai4p-de-20694945` value=`Lourin Buffo Kottler`  context: ...'\nKundendaten:\nBürgermeisterin Lourin Buffo Kottler\nSandgasse 1437\n6020 Linz\nE‑Ma'...
- `ai4p-de-20694955` value=`Asan Kubisa Kodeeswaran Natsvlishvili`  context: ...'Der Kameramann, Asan Kubisa Kodeeswaran Natsvlishvili, gibt seine Sozialversicherun'...
- `ai4p-de-20694976` value=`Guilain Enric Siudak`  context: ...' – 10/05/1966\n\nAnwesend: Prof Guilain Enric Siudak (Vorsitz), Iakovos Qeshk Arn '...
- `ai4p-de-20694976` value=`Iakovos Qeshk Arn`  context: ...'ilain Enric Siudak (Vorsitz), Iakovos Qeshk Arn (Schatzmeister), Doni Krigl ('...

### `[PHONE]`
- `ai4p-de-20695161` value=`+74-64.963 5015`  context: ...'ok.com oder telefonisch unter +74-64.963 5015. Für die Anmeldung benötigen '...
- `ai4p-de-20695229` value=`0043776 255-5492`  context: ...'hotmail.com\n6. Telefonnummer: 0043776 255-5492\n7. Adresse: Schwimmschulkai 1'...
- `ai4p-de-20695280` value=`03.98 27.46.19`  context: ...'agen erreichen Sie mich unter 03.98 27.46.19 oder per E‑Mail an FML@gmail.'...
- `ai4p-de-20695572` value=`+97.84-776.9908`  context: ...'Mail: 27TS@gmail.com\nTelefon: +97.84-776.9908\nAdresse: Dr.-Fritz-Dörflinger'...
- `ai4p-de-20695574` value=`06-67.66.92-78`  context: ...' E‑Mail KR@gmail.com, Telefon 06-67.66.92-78. Sollten Sie weitere Fragen h'...

### `[STREET_ADDRESS]`
- `ai4p-de-20694923` value=`Bertha-von-Suttner-Weg 3E in Klagenfurt am Wörthersee`  context: ...'neigenes Fitnessstudio in der Bertha-von-Suttner-Weg 3E in Klagenfurt am Wörthersee an. Mitarbeiter, die das Ange'...
- `ai4p-de-20694958` value=`Bahnhofstraße 15, 8020 Linz`  context: ...'20-459.555.0277\n8. Anschrift: Bahnhofstraße 15, 8020 Linz\n9. Personalausweis‑Nummer: 49'...
- `ai4p-de-20694963` value=`Innsbruck`  context: ...' den Hallen des Rathauses von Innsbruck ausgelegt liegt, fordert die '...
- `ai4p-de-20695015` value=`4020`  context: ...'schließlich (336).7147153 und 4020, damit Support‑Teams weltweit'...
- `ai4p-de-20695039` value=`Wien`  context: ...'len, die am Juli 14., 1987 in Wien abgeschlossen wurde; bitte se'...

