# Imported-dataset eval - ai4privacy_de

- Rows evaluated: **200**
- Rows with zero gold spans (after label-map filter): **9**
- Elapsed: **0.0s** (0ms/row)
- Projection-symmetric scoring: **on** (gold placeholder space: `[DATE], [EMAIL], [PERSON_NAME], [PHONE], [STREET_ADDRESS]`)

## Per-placeholder precision / recall

| Placeholder | Precision (95% CI) | Recall (95% CI) | F1 (95% CI) | TP | FP | FN | Support |
|---|---|---|---|---:|---:|---:|---:|
| `[DATE]` | 0.971 [0.929, 1.000] | 1.000 [1.000, 1.000] | 0.985 [0.963, 1.000] | 67 | 2 | 0 | 67 |
| `[EMAIL]` | 0.990 [0.965, 1.000] | 0.980 [0.948, 1.000] | 0.985 [0.965, 1.000] | 96 | 1 | 2 | 98 |
| `[PERSON_NAME]` | 0.000 [0.000, 0.000] | 0.000 [0.000, 0.000] | 0.000 [0.000, 0.000] | 0 | 0 | 142 | 142 |
| `[PHONE]` | 0.940 [0.870, 1.000] | 0.644 [0.530, 0.750] | 0.764 [0.672, 0.842] | 47 | 3 | 26 | 73 |
| `[STREET_ADDRESS]` | 0.000 [0.000, 0.000] | 0.000 [0.000, 0.000] | 0.000 [0.000, 0.000] | 0 | 0 | 94 | 94 |
| **macro** | 0.580 [0.564, 0.594] | 0.525 [0.501, 0.548] | 0.551 [0.534, 0.567] | 210 | 6 | 264 | 474 |
| **micro** | 0.972 [0.951, 0.991] | 0.443 [0.409, 0.479] | 0.609 [0.573, 0.642] | 210 | 6 | 264 | 474 |

## Per-length-bucket precision / recall

Row distribution across buckets: `sentence`: 134, `paragraph`: 31, `multi_paragraph`: 4, `structured`: 31

### `sentence` (134 rows)

| Placeholder | Precision (95% CI) | Recall (95% CI) | F1 (95% CI) | TP | FP | FN | Support |
|---|---|---|---|---:|---:|---:|---:|
| `[DATE]` | 0.950 [0.879, 1.000] | 1.000 [1.000, 1.000] | 0.974 [0.935, 1.000] | 38 | 2 | 0 | 38 |
| `[EMAIL]` | 1.000 [1.000, 1.000] | 1.000 [1.000, 1.000] | 1.000 [1.000, 1.000] | 53 | 0 | 0 | 53 |
| `[PERSON_NAME]` | 0.000 [0.000, 0.000] | 0.000 [0.000, 0.000] | 0.000 [0.000, 0.000] | 0 | 0 | 80 | 80 |
| `[PHONE]` | 0.966 [0.880, 1.000] | 0.683 [0.526, 0.821] | 0.800 [0.678, 0.897] | 28 | 1 | 13 | 41 |
| `[STREET_ADDRESS]` | 0.000 [0.000, 0.000] | 0.000 [0.000, 0.000] | 0.000 [0.000, 0.000] | 0 | 0 | 63 | 63 |
| **macro** | 0.583 [0.561, 0.600] | 0.537 [0.505, 0.564] | 0.559 [0.537, 0.578] | 119 | 3 | 156 | 275 |
| **micro** | 0.975 [0.943, 1.000] | 0.433 [0.387, 0.479] | 0.599 [0.552, 0.643] | 119 | 3 | 156 | 275 |

### `paragraph` (31 rows)

| Placeholder | Precision (95% CI) | Recall (95% CI) | F1 (95% CI) | TP | FP | FN | Support |
|---|---|---|---|---:|---:|---:|---:|
| `[DATE]` | 1.000 [1.000, 1.000] | 1.000 [1.000, 1.000] | 1.000 [1.000, 1.000] | 14 | 0 | 0 | 14 |
| `[EMAIL]` | 1.000 [1.000, 1.000] | 1.000 [1.000, 1.000] | 1.000 [1.000, 1.000] | 16 | 0 | 0 | 16 |
| `[PERSON_NAME]` | 0.000 [0.000, 0.000] | 0.000 [0.000, 0.000] | 0.000 [0.000, 0.000] | 0 | 0 | 18 | 18 |
| `[PHONE]` | 1.000 [1.000, 1.000] | 0.846 [0.625, 1.000] | 0.917 [0.769, 1.000] | 11 | 0 | 2 | 13 |
| `[STREET_ADDRESS]` | 0.000 [0.000, 0.000] | 0.000 [0.000, 0.000] | 0.000 [0.000, 0.000] | 0 | 0 | 13 | 13 |
| **macro** | 0.600 [0.600, 0.600] | 0.569 [0.525, 0.600] | 0.584 [0.560, 0.600] | 41 | 0 | 33 | 74 |
| **micro** | 1.000 [1.000, 1.000] | 0.554 [0.468, 0.646] | 0.713 [0.638, 0.785] | 41 | 0 | 33 | 74 |

### `multi_paragraph` (4 rows)

| Placeholder | Precision (95% CI) | Recall (95% CI) | F1 (95% CI) | TP | FP | FN | Support |
|---|---|---|---|---:|---:|---:|---:|
| `[DATE]` | 1.000 [0.000, 1.000] | 1.000 [0.000, 1.000] | 1.000 [0.000, 1.000] | 1 | 0 | 0 | 1 |
| `[EMAIL]` | 1.000 [1.000, 1.000] | 0.800 [0.250, 1.000] | 0.889 [0.400, 1.000] | 4 | 0 | 1 | 5 |
| `[PERSON_NAME]` | 0.000 [0.000, 0.000] | 0.000 [0.000, 0.000] | 0.000 [0.000, 0.000] | 0 | 0 | 6 | 6 |
| `[PHONE]` | 1.000 [0.000, 1.000] | 0.250 [0.000, 0.750] | 0.400 [0.000, 0.857] | 1 | 0 | 3 | 4 |
| `[STREET_ADDRESS]` | 0.000 [0.000, 0.000] | 0.000 [0.000, 0.000] | 0.000 [0.000, 0.000] | 0 | 0 | 3 | 3 |
| **macro** | 0.600 [0.200, 0.600] | 0.410 [0.100, 0.500] | 0.487 [0.133, 0.545] | 6 | 0 | 13 | 19 |
| **micro** | 1.000 [1.000, 1.000] | 0.316 [0.125, 0.529] | 0.480 [0.222, 0.692] | 6 | 0 | 13 | 19 |

### `structured` (31 rows)

| Placeholder | Precision (95% CI) | Recall (95% CI) | F1 (95% CI) | TP | FP | FN | Support |
|---|---|---|---|---:|---:|---:|---:|
| `[DATE]` | 1.000 [1.000, 1.000] | 1.000 [1.000, 1.000] | 1.000 [1.000, 1.000] | 14 | 0 | 0 | 14 |
| `[EMAIL]` | 0.958 [0.864, 1.000] | 0.958 [0.846, 1.000] | 0.958 [0.889, 1.000] | 23 | 1 | 1 | 24 |
| `[PERSON_NAME]` | 0.000 [0.000, 0.000] | 0.000 [0.000, 0.000] | 0.000 [0.000, 0.000] | 0 | 0 | 38 | 38 |
| `[PHONE]` | 0.778 [0.500, 1.000] | 0.467 [0.188, 0.715] | 0.583 [0.300, 0.800] | 7 | 2 | 8 | 15 |
| `[STREET_ADDRESS]` | 0.000 [0.000, 0.000] | 0.000 [0.000, 0.000] | 0.000 [0.000, 0.000] | 0 | 0 | 15 | 15 |
| **macro** | 0.547 [0.489, 0.600] | 0.485 [0.427, 0.541] | 0.514 [0.462, 0.558] | 44 | 3 | 62 | 106 |
| **micro** | 0.936 [0.863, 1.000] | 0.415 [0.347, 0.478] | 0.575 [0.503, 0.636] | 44 | 3 | 62 | 106 |


## False-positive samples

### `[DATE]`
- `ai4p-de-20695161` [regex] value=`74-64.963`  context: ...'k.com oder telefonisch unter +74-64.963 5015. Für die Anmeldung benöt'...
- `ai4p-de-20695280` [regex] value=`27.46.19`  context: ...'rreichen Sie mich unter 03.98 27.46.19 oder per E‑Mail an FML@gmail.'...

### `[EMAIL]`
- `ai4p-de-20695252` [regex] value=`support@company.at`  context: ...'otonmail.com>\nAn: IT‑Support <support@company.at>\nDatum: 12/03/1946\nBetreff: P'...

### `[PHONE]`
- `ai4p-de-20694958` [regex] value=`0901 700729
12`  context: ...'. Sozialversicherungs‑Nummer: 0901 700729\n12. Steuer‑Identifikationsnummer'...
- `ai4p-de-20695082` [regex] value=`0331 620902`  context: ...'ine Sozialversicherungsnummer 0331 620902 an, während das System seine '...
- `ai4p-de-20695249` [regex] value=`0432 570801`  context: ...'FW\nSozialversicherungsnummer: 0432 570801\nSteuer‑Identifikationsnummer:'...


## False-negative samples

### `[EMAIL]`
- `ai4p-de-20694974` value=`noëdoggweiler@yahoo.com`  context: ...'tsidentität: Bigender\nE‑Mail: noëdoggweiler@yahoo.com\nTelefon: (66) 6903 1936\n\nGewü'...
- `ai4p-de-20695275` value=`guizoppè@gmail.com`  context: ...'ren Sie uns bitte per E‑Mail (guizoppè@gmail.com) oder Telefon (0042-13 158 04'...

### `[PERSON_NAME]`
- `ai4p-de-20694922` value=`Jadranka Landhou Enevoldsen Sekat`  context: ...' Führungskräften wie Doktorin Jadranka Landhou Enevoldsen Sekat geleitet wird.'...
- `ai4p-de-20694931` value=`Alpay Solorzano`  context: ...'Die Laborgruppe, geleitet von Alpay Solorzano, hat mittels Massenspektromet'...
- `ai4p-de-20694933` value=`Wajdi Giesenfeld Majima`  context: ...'chen den Instituten wurde von Wajdi Giesenfeld Majima (Telefon: (49) 0268.3035) unt'...
- `ai4p-de-20694936` value=`Ricco Tsakalos`  context: ...'Der Projektleiter, Meister Ricco Tsakalos, weist darauf hin, dass das E'...
- `ai4p-de-20694937` value=`Xhyle Dinouard`  context: ...'eten, wobei die Kontaktperson Xhyle Dinouard ebenfalls unter der Telefonnu'...

### `[PHONE]`
- `ai4p-de-20694924` value=`+54-685227296`  context: ...'ta.com oder telefonisch unter +54-685227296 zur Verfügung. Wir freuen uns'...
- `ai4p-de-20694943` value=`+878.63.973.9334`  context: ...'‑Mail: M@hotmail.com\nTelefon: +878.63.973.9334\nPersonalausweis‑Nr.: 84394318'...
- `ai4p-de-20694954` value=`009929046 2990`  context: ...'C7977252. Ein kurzer Anruf an 009929046 2990 bestätigt, dass das Set im al'...
- `ai4p-de-20694958` value=`+20-459.555.0277`  context: ...'otmail.com\n7. Telefonkontakt: +20-459.555.0277\n8. Anschrift: Bahnhofstraße 1'...
- `ai4p-de-20694974` value=`(66) 6903 1936`  context: ...'doggweiler@yahoo.com\nTelefon: (66) 6903 1936\n\nGewünschte Ausrüstung:\n- Kam'...

### `[STREET_ADDRESS]`
- `ai4p-de-20694920` value=`Goethestraße 315, 1090 Wien Wieden`  context: ...'n Sie Ihre neue Anschrift an: Goethestraße 315, 1090 Wien Wieden.'...
- `ai4p-de-20694923` value=`Bertha-von-Suttner-Weg 3E in Klagenfurt am Wörthersee`  context: ...'neigenes Fitnessstudio in der Bertha-von-Suttner-Weg 3E in Klagenfurt am Wörthersee an. Mitarbeiter, die das Ange'...
- `ai4p-de-20694943` value=`Zollerstraße 15, 4040 Zirl`  context: ...'): Geschlechterqueer\nAdresse: Zollerstraße 15, 4040 Zirl\nE‑Mail: M@hotmail.com\nTelefon'...
- `ai4p-de-20694945` value=`Sandgasse 1437
6020 Linz`  context: ...'eisterin Lourin Buffo Kottler\nSandgasse 1437\n6020 Linz\nE‑Mail: LI@hotmail.com\nTelefo'...
- `ai4p-de-20694954` value=`Weingartshofstraße 6`  context: ...'Set im alten Lagerhaus in der Weingartshofstraße 6 aufgebaut wird. Der Regisseur'...

