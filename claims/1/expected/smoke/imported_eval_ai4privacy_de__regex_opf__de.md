# Imported-dataset eval - ai4privacy_de

- Rows evaluated: **200**
- Rows with zero gold spans (after label-map filter): **9**
- Elapsed: **633.6s** (3168ms/row)
- Projection-symmetric scoring: **on** (gold placeholder space: `[DATE], [EMAIL], [PERSON_NAME], [PHONE], [STREET_ADDRESS]`)

## Per-placeholder precision / recall

| Placeholder | Precision (95% CI) | Recall (95% CI) | F1 (95% CI) | TP | FP | FN | Support |
|---|---|---|---|---:|---:|---:|---:|
| `[DATE]` | 0.971 [0.929, 1.000] | 1.000 [1.000, 1.000] | 0.985 [0.963, 1.000] | 67 | 2 | 0 | 67 |
| `[EMAIL]` | 0.990 [0.965, 1.000] | 1.000 [1.000, 1.000] | 0.995 [0.982, 1.000] | 98 | 1 | 0 | 98 |
| `[PERSON_NAME]` | 0.852 [0.801, 0.907] | 0.810 [0.745, 0.878] | 0.830 [0.787, 0.874] | 115 | 20 | 27 | 142 |
| `[PHONE]` | 0.729 [0.653, 0.806] | 0.959 [0.907, 1.000] | 0.828 [0.768, 0.882] | 70 | 26 | 3 | 73 |
| `[STREET_ADDRESS]` | 0.724 [0.633, 0.831] | 0.585 [0.480, 0.688] | 0.647 [0.564, 0.721] | 55 | 21 | 39 | 94 |
| **macro** | 0.853 [0.826, 0.884] | 0.871 [0.846, 0.897] | 0.862 [0.842, 0.884] | 405 | 70 | 69 | 474 |
| **micro** | 0.853 [0.821, 0.884] | 0.854 [0.823, 0.884] | 0.854 [0.831, 0.878] | 405 | 70 | 69 | 474 |

## Per-length-bucket precision / recall

Row distribution across buckets: `sentence`: 134, `paragraph`: 31, `multi_paragraph`: 4, `structured`: 31

### `sentence` (134 rows)

| Placeholder | Precision (95% CI) | Recall (95% CI) | F1 (95% CI) | TP | FP | FN | Support |
|---|---|---|---|---:|---:|---:|---:|
| `[DATE]` | 0.950 [0.879, 1.000] | 1.000 [1.000, 1.000] | 0.974 [0.935, 1.000] | 38 | 2 | 0 | 38 |
| `[EMAIL]` | 1.000 [1.000, 1.000] | 1.000 [1.000, 1.000] | 1.000 [1.000, 1.000] | 53 | 0 | 0 | 53 |
| `[PERSON_NAME]` | 0.863 [0.789, 0.937] | 0.787 [0.694, 0.868] | 0.824 [0.760, 0.877] | 63 | 10 | 17 | 80 |
| `[PHONE]` | 0.780 [0.673, 0.884] | 0.951 [0.872, 1.000] | 0.857 [0.777, 0.923] | 39 | 11 | 2 | 41 |
| `[STREET_ADDRESS]` | 0.766 [0.651, 0.892] | 0.571 [0.448, 0.695] | 0.655 [0.561, 0.744] | 36 | 11 | 27 | 63 |
| **macro** | 0.872 [0.836, 0.909] | 0.862 [0.831, 0.893] | 0.867 [0.840, 0.894] | 229 | 34 | 46 | 275 |
| **micro** | 0.871 [0.826, 0.909] | 0.833 [0.794, 0.871] | 0.851 [0.821, 0.882] | 229 | 34 | 46 | 275 |

### `paragraph` (31 rows)

| Placeholder | Precision (95% CI) | Recall (95% CI) | F1 (95% CI) | TP | FP | FN | Support |
|---|---|---|---|---:|---:|---:|---:|
| `[DATE]` | 1.000 [1.000, 1.000] | 1.000 [1.000, 1.000] | 1.000 [1.000, 1.000] | 14 | 0 | 0 | 14 |
| `[EMAIL]` | 1.000 [1.000, 1.000] | 1.000 [1.000, 1.000] | 1.000 [1.000, 1.000] | 16 | 0 | 0 | 16 |
| `[PERSON_NAME]` | 0.900 [0.789, 1.000] | 1.000 [1.000, 1.000] | 0.947 [0.882, 1.000] | 18 | 2 | 0 | 18 |
| `[PHONE]` | 0.867 [0.688, 1.000] | 1.000 [1.000, 1.000] | 0.929 [0.815, 1.000] | 13 | 2 | 0 | 13 |
| `[STREET_ADDRESS]` | 0.833 [0.400, 1.000] | 0.385 [0.125, 0.667] | 0.526 [0.200, 0.762] | 5 | 1 | 8 | 13 |
| **macro** | 0.920 [0.826, 0.980] | 0.877 [0.825, 0.933] | 0.898 [0.830, 0.945] | 66 | 5 | 8 | 74 |
| **micro** | 0.930 [0.873, 0.974] | 0.892 [0.833, 0.949] | 0.910 [0.867, 0.950] | 66 | 5 | 8 | 74 |

### `multi_paragraph` (4 rows)

| Placeholder | Precision (95% CI) | Recall (95% CI) | F1 (95% CI) | TP | FP | FN | Support |
|---|---|---|---|---:|---:|---:|---:|
| `[DATE]` | 1.000 [0.000, 1.000] | 1.000 [0.000, 1.000] | 1.000 [0.000, 1.000] | 1 | 0 | 0 | 1 |
| `[EMAIL]` | 1.000 [1.000, 1.000] | 1.000 [1.000, 1.000] | 1.000 [1.000, 1.000] | 5 | 0 | 0 | 5 |
| `[PERSON_NAME]` | 0.667 [0.500, 1.000] | 0.667 [0.250, 1.000] | 0.667 [0.400, 1.000] | 4 | 2 | 2 | 6 |
| `[PHONE]` | 0.500 [0.364, 0.800] | 1.000 [1.000, 1.000] | 0.667 [0.533, 0.889] | 4 | 4 | 0 | 4 |
| `[STREET_ADDRESS]` | 1.000 [1.000, 1.000] | 1.000 [1.000, 1.000] | 1.000 [1.000, 1.000] | 3 | 0 | 0 | 3 |
| **macro** | 0.833 [0.680, 0.876] | 0.933 [0.650, 0.967] | 0.881 [0.665, 0.919] | 17 | 6 | 2 | 19 |
| **micro** | 0.739 [0.591, 0.889] | 0.895 [0.769, 1.000] | 0.810 [0.667, 0.941] | 17 | 6 | 2 | 19 |

### `structured` (31 rows)

| Placeholder | Precision (95% CI) | Recall (95% CI) | F1 (95% CI) | TP | FP | FN | Support |
|---|---|---|---|---:|---:|---:|---:|
| `[DATE]` | 1.000 [1.000, 1.000] | 1.000 [1.000, 1.000] | 1.000 [1.000, 1.000] | 14 | 0 | 0 | 14 |
| `[EMAIL]` | 0.960 [0.869, 1.000] | 1.000 [1.000, 1.000] | 0.980 [0.930, 1.000] | 24 | 1 | 0 | 24 |
| `[PERSON_NAME]` | 0.833 [0.730, 0.938] | 0.789 [0.636, 0.935] | 0.811 [0.718, 0.893] | 30 | 6 | 8 | 38 |
| `[PHONE]` | 0.609 [0.474, 0.762] | 0.933 [0.778, 1.000] | 0.737 [0.600, 0.857] | 14 | 9 | 1 | 15 |
| `[STREET_ADDRESS]` | 0.550 [0.429, 0.750] | 0.733 [0.500, 0.933] | 0.629 [0.500, 0.757] | 11 | 9 | 4 | 15 |
| **macro** | 0.790 [0.752, 0.841] | 0.891 [0.832, 0.947] | 0.838 [0.803, 0.877] | 93 | 25 | 13 | 106 |
| **micro** | 0.788 [0.726, 0.852] | 0.877 [0.800, 0.941] | 0.830 [0.785, 0.877] | 93 | 25 | 13 | 106 |


## False-positive samples

### `[DATE]`
- `ai4p-de-20695161` [regex] value=`74-64.963`  context: ...'k.com oder telefonisch unter +74-64.963 5015. Für die Anmeldung benöt'...
- `ai4p-de-20695280` [regex] value=`27.46.19`  context: ...'rreichen Sie mich unter 03.98 27.46.19 oder per E‑Mail an FML@gmail.'...

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

### `[STREET_ADDRESS]`
- `ai4p-de-20694923` value=`Bertha-von-Suttner-Weg 3E in Klagenfurt am Wörthersee`  context: ...'neigenes Fitnessstudio in der Bertha-von-Suttner-Weg 3E in Klagenfurt am Wörthersee an. Mitarbeiter, die das Ange'...
- `ai4p-de-20694958` value=`Bahnhofstraße 15, 8020 Linz`  context: ...'20-459.555.0277\n8. Anschrift: Bahnhofstraße 15, 8020 Linz\n9. Personalausweis‑Nummer: 49'...
- `ai4p-de-20694963` value=`Innsbruck`  context: ...' den Hallen des Rathauses von Innsbruck ausgelegt liegt, fordert die '...
- `ai4p-de-20695015` value=`4020`  context: ...'schließlich (336).7147153 und 4020, damit Support‑Teams weltweit'...
- `ai4p-de-20695039` value=`Wien`  context: ...'len, die am Juli 14., 1987 in Wien abgeschlossen wurde; bitte se'...

