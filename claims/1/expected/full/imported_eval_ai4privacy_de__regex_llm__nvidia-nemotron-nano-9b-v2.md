# Imported-dataset eval - ai4privacy_de

- Rows evaluated: **1,000**
- Rows with zero gold spans (after label-map filter): **37**
- Elapsed: **313.1s** (313ms/row)
- Projection-symmetric scoring: **on** (gold placeholder space: `[DATE], [EMAIL], [PERSON_NAME], [PHONE], [STREET_ADDRESS]`)

## Per-placeholder precision / recall

| Placeholder | Precision (95% CI) | Recall (95% CI) | F1 (95% CI) | TP | FP | FN | Support |
|---|---|---|---|---:|---:|---:|---:|
| `[DATE]` | 0.914 [0.885, 0.940] | 1.000 [1.000, 1.000] | 0.955 [0.939, 0.969] | 328 | 31 | 0 | 328 |
| `[EMAIL]` | 0.998 [0.994, 1.000] | 0.974 [0.959, 0.987] | 0.986 [0.978, 0.993] | 524 | 1 | 14 | 538 |
| `[PERSON_NAME]` | 0.979 [0.932, 1.000] | 0.059 [0.042, 0.076] | 0.112 [0.081, 0.142] | 47 | 1 | 748 | 795 |
| `[PHONE]` | 0.933 [0.904, 0.963] | 0.571 [0.523, 0.619] | 0.709 [0.669, 0.746] | 236 | 17 | 177 | 413 |
| `[STREET_ADDRESS]` | 1.000 [1.000, 1.000] | 0.086 [0.065, 0.111] | 0.159 [0.122, 0.200] | 48 | 0 | 509 | 557 |
| **macro** | 0.965 [0.952, 0.976] | 0.538 [0.525, 0.551] | 0.691 [0.679, 0.702] | 1183 | 50 | 1448 | 2631 |
| **micro** | 0.959 [0.949, 0.969] | 0.450 [0.433, 0.467] | 0.612 [0.596, 0.629] | 1183 | 50 | 1448 | 2631 |

## Per-length-bucket precision / recall

Row distribution across buckets: `sentence`: 690, `paragraph`: 114, `multi_paragraph`: 54, `structured`: 142

### `sentence` (690 rows)

| Placeholder | Precision (95% CI) | Recall (95% CI) | F1 (95% CI) | TP | FP | FN | Support |
|---|---|---|---|---:|---:|---:|---:|
| `[DATE]` | 0.928 [0.892, 0.960] | 1.000 [1.000, 1.000] | 0.963 [0.943, 0.980] | 181 | 14 | 0 | 181 |
| `[EMAIL]` | 1.000 [1.000, 1.000] | 0.977 [0.959, 0.991] | 0.988 [0.979, 0.995] | 297 | 0 | 7 | 304 |
| `[PERSON_NAME]` | 0.964 [0.882, 1.000] | 0.059 [0.038, 0.083] | 0.112 [0.074, 0.153] | 27 | 1 | 428 | 455 |
| `[PHONE]` | 0.957 [0.919, 0.986] | 0.587 [0.522, 0.651] | 0.727 [0.674, 0.778] | 132 | 6 | 93 | 225 |
| `[STREET_ADDRESS]` | 1.000 [1.000, 1.000] | 0.080 [0.052, 0.109] | 0.147 [0.099, 0.197] | 28 | 0 | 324 | 352 |
| **macro** | 0.970 [0.951, 0.985] | 0.541 [0.524, 0.557] | 0.694 [0.678, 0.709] | 665 | 21 | 852 | 1517 |
| **micro** | 0.969 [0.956, 0.982] | 0.438 [0.417, 0.459] | 0.604 [0.583, 0.623] | 665 | 21 | 852 | 1517 |

### `paragraph` (114 rows)

| Placeholder | Precision (95% CI) | Recall (95% CI) | F1 (95% CI) | TP | FP | FN | Support |
|---|---|---|---|---:|---:|---:|---:|
| `[DATE]` | 0.855 [0.754, 0.936] | 1.000 [1.000, 1.000] | 0.922 [0.860, 0.967] | 47 | 8 | 0 | 47 |
| `[EMAIL]` | 1.000 [1.000, 1.000] | 0.975 [0.936, 1.000] | 0.987 [0.967, 1.000] | 77 | 0 | 2 | 79 |
| `[PERSON_NAME]` | 1.000 [0.000, 1.000] | 0.010 [0.000, 0.037] | 0.021 [0.000, 0.071] | 1 | 0 | 95 | 96 |
| `[PHONE]` | 1.000 [1.000, 1.000] | 0.515 [0.397, 0.642] | 0.680 [0.568, 0.782] | 34 | 0 | 32 | 66 |
| `[STREET_ADDRESS]` | 1.000 [0.000, 1.000] | 0.014 [0.000, 0.053] | 0.028 [0.000, 0.101] | 1 | 0 | 69 | 70 |
| **macro** | 0.971 [0.556, 0.985] | 0.503 [0.476, 0.532] | 0.663 [0.516, 0.688] | 160 | 8 | 198 | 358 |
| **micro** | 0.952 [0.918, 0.980] | 0.447 [0.409, 0.486] | 0.608 [0.570, 0.647] | 160 | 8 | 198 | 358 |

### `multi_paragraph` (54 rows)

| Placeholder | Precision (95% CI) | Recall (95% CI) | F1 (95% CI) | TP | FP | FN | Support |
|---|---|---|---|---:|---:|---:|---:|
| `[DATE]` | 0.875 [0.750, 0.972] | 1.000 [1.000, 1.000] | 0.933 [0.857, 0.986] | 28 | 4 | 0 | 28 |
| `[EMAIL]` | 1.000 [1.000, 1.000] | 0.980 [0.933, 1.000] | 0.990 [0.966, 1.000] | 48 | 0 | 1 | 49 |
| `[PERSON_NAME]` | 1.000 [0.000, 1.000] | 0.012 [0.000, 0.039] | 0.024 [0.000, 0.076] | 1 | 0 | 80 | 81 |
| `[PHONE]` | 0.800 [0.632, 0.952] | 0.432 [0.270, 0.594] | 0.561 [0.391, 0.706] | 16 | 4 | 21 | 37 |
| `[STREET_ADDRESS]` | 1.000 [0.000, 1.000] | 0.024 [0.000, 0.077] | 0.048 [0.000, 0.143] | 1 | 0 | 40 | 41 |
| **macro** | 0.935 [0.511, 0.968] | 0.490 [0.454, 0.524] | 0.643 [0.489, 0.674] | 94 | 8 | 142 | 236 |
| **micro** | 0.922 [0.869, 0.969] | 0.398 [0.359, 0.438] | 0.556 [0.512, 0.599] | 94 | 8 | 142 | 236 |

### `structured` (142 rows)

| Placeholder | Precision (95% CI) | Recall (95% CI) | F1 (95% CI) | TP | FP | FN | Support |
|---|---|---|---|---:|---:|---:|---:|
| `[DATE]` | 0.935 [0.881, 0.985] | 1.000 [1.000, 1.000] | 0.966 [0.937, 0.993] | 72 | 5 | 0 | 72 |
| `[EMAIL]` | 0.990 [0.968, 1.000] | 0.962 [0.922, 0.991] | 0.976 [0.953, 0.995] | 102 | 1 | 4 | 106 |
| `[PERSON_NAME]` | 1.000 [1.000, 1.000] | 0.110 [0.065, 0.164] | 0.199 [0.122, 0.282] | 18 | 0 | 145 | 163 |
| `[PHONE]` | 0.885 [0.810, 0.955] | 0.635 [0.531, 0.734] | 0.740 [0.656, 0.813] | 54 | 7 | 31 | 85 |
| `[STREET_ADDRESS]` | 1.000 [1.000, 1.000] | 0.191 [0.114, 0.273] | 0.321 [0.204, 0.429] | 18 | 0 | 76 | 94 |
| **macro** | 0.962 [0.944, 0.978] | 0.580 [0.545, 0.616] | 0.724 [0.693, 0.752] | 264 | 13 | 256 | 520 |
| **micro** | 0.953 [0.927, 0.974] | 0.508 [0.462, 0.552] | 0.662 [0.620, 0.701] | 264 | 13 | 256 | 520 |


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
- `ai4p-de-20695925` [opf] value=`Bewerber aus Klagenfurt am Wörthersee St. Veiter Vorstadt`  context: ...'Für Bewerber aus Klagenfurt am Wörthersee St. Veiter Vorstadt mit Wohnsitz an der Augarten\u202f'...

### `[PHONE]`
- `ai4p-de-20694958` [regex] value=`0901 700729
12`  context: ...'. Sozialversicherungs‑Nummer: 0901 700729\n12. Steuer‑Identifikationsnummer'...
- `ai4p-de-20695082` [regex] value=`0331 620902`  context: ...'ine Sozialversicherungsnummer 0331 620902 an, während das System seine '...
- `ai4p-de-20695249` [regex] value=`0432 570801`  context: ...'FW\nSozialversicherungsnummer: 0432 570801\nSteuer‑Identifikationsnummer:'...
- `ai4p-de-20695439` [regex] value=`0404 031110`  context: ...'ogene Daten nur im Rahmen von 0404 031110 nutzen)\n\nBitte bis zum 3. Mai'...
- `ai4p-de-20695690` [regex] value=`0652 370604`  context: ...'. Sozialversicherungs‑Nummer: 0652 370604\n9. Steuer‑Identifikationsnumm'...


## False-negative samples

### `[EMAIL]`
- `ai4p-de-20694974` value=`noëdoggweiler@yahoo.com`  context: ...'tsidentität: Bigender\nE‑Mail: noëdoggweiler@yahoo.com\nTelefon: (66) 6903 1936\n\nGewü'...
- `ai4p-de-20695275` value=`guizoppè@gmail.com`  context: ...'ren Sie uns bitte per E‑Mail (guizoppè@gmail.com) oder Telefon (0042-13 158 04'...
- `ai4p-de-20695432` value=`çinarrowan@hotmail.com`  context: ...'e Ansprechpartner per E‑Mail (çinarrowan@hotmail.com) und Telefon (+78.63887-6542)'...
- `ai4p-de-20695554` value=`maliilühmann@yahoo.com`  context: ...'burtsdatum: Mai/61\n5. E‑Mail: maliilühmann@yahoo.com\n6. Telefon: +435 38.964-3663\n'...
- `ai4p-de-20695871` value=`tomysodré@gmail.com`  context: ...' Sie Ihre Bewerbung inklusive tomysodré@gmail.com und +84 26874 5996 bis zum 11'...

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

