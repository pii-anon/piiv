# Imported-dataset eval - ai4privacy_de

- Rows evaluated: **1,000**
- Rows with zero gold spans (after label-map filter): **37**
- Elapsed: **735.3s** (735ms/row)
- Projection-symmetric scoring: **on** (gold placeholder space: `[DATE], [EMAIL], [PERSON_NAME], [PHONE], [STREET_ADDRESS]`)

## Per-placeholder precision / recall

| Placeholder | Precision (95% CI) | Recall (95% CI) | F1 (95% CI) | TP | FP | FN | Support |
|---|---|---|---|---:|---:|---:|---:|
| `[DATE]` | 0.914 [0.885, 0.940] | 1.000 [1.000, 1.000] | 0.955 [0.939, 0.969] | 328 | 31 | 0 | 328 |
| `[EMAIL]` | 0.998 [0.994, 1.000] | 0.974 [0.959, 0.987] | 0.986 [0.978, 0.993] | 524 | 1 | 14 | 538 |
| `[PERSON_NAME]` | 0.990 [0.974, 1.000] | 0.250 [0.216, 0.284] | 0.400 [0.355, 0.441] | 199 | 2 | 596 | 795 |
| `[PHONE]` | 0.933 [0.904, 0.963] | 0.571 [0.523, 0.619] | 0.709 [0.669, 0.746] | 236 | 17 | 177 | 413 |
| `[STREET_ADDRESS]` | 0.905 [0.847, 0.961] | 0.189 [0.155, 0.222] | 0.312 [0.266, 0.356] | 105 | 11 | 452 | 557 |
| **macro** | 0.948 [0.933, 0.962] | 0.597 [0.580, 0.613] | 0.732 [0.719, 0.745] | 1392 | 62 | 1239 | 2631 |
| **micro** | 0.957 [0.946, 0.967] | 0.529 [0.509, 0.548] | 0.682 [0.664, 0.698] | 1392 | 62 | 1239 | 2631 |

## Per-length-bucket precision / recall

Row distribution across buckets: `sentence`: 690, `paragraph`: 114, `multi_paragraph`: 54, `structured`: 142

### `sentence` (690 rows)

| Placeholder | Precision (95% CI) | Recall (95% CI) | F1 (95% CI) | TP | FP | FN | Support |
|---|---|---|---|---:|---:|---:|---:|
| `[DATE]` | 0.928 [0.892, 0.960] | 1.000 [1.000, 1.000] | 0.963 [0.943, 0.980] | 181 | 14 | 0 | 181 |
| `[EMAIL]` | 1.000 [1.000, 1.000] | 0.977 [0.959, 0.991] | 0.988 [0.979, 0.995] | 297 | 0 | 7 | 304 |
| `[PERSON_NAME]` | 0.983 [0.960, 1.000] | 0.262 [0.221, 0.304] | 0.413 [0.361, 0.466] | 119 | 2 | 336 | 455 |
| `[PHONE]` | 0.957 [0.919, 0.986] | 0.587 [0.522, 0.651] | 0.727 [0.674, 0.778] | 132 | 6 | 93 | 225 |
| `[STREET_ADDRESS]` | 0.912 [0.849, 0.970] | 0.176 [0.138, 0.218] | 0.295 [0.239, 0.351] | 62 | 6 | 290 | 352 |
| **macro** | 0.956 [0.940, 0.973] | 0.600 [0.578, 0.620] | 0.737 [0.720, 0.754] | 791 | 28 | 726 | 1517 |
| **micro** | 0.966 [0.954, 0.977] | 0.521 [0.496, 0.547] | 0.677 [0.655, 0.698] | 791 | 28 | 726 | 1517 |

### `paragraph` (114 rows)

| Placeholder | Precision (95% CI) | Recall (95% CI) | F1 (95% CI) | TP | FP | FN | Support |
|---|---|---|---|---:|---:|---:|---:|
| `[DATE]` | 0.855 [0.754, 0.936] | 1.000 [1.000, 1.000] | 0.922 [0.860, 0.967] | 47 | 8 | 0 | 47 |
| `[EMAIL]` | 1.000 [1.000, 1.000] | 0.975 [0.936, 1.000] | 0.987 [0.967, 1.000] | 77 | 0 | 2 | 79 |
| `[PERSON_NAME]` | 1.000 [1.000, 1.000] | 0.146 [0.067, 0.237] | 0.255 [0.125, 0.383] | 14 | 0 | 82 | 96 |
| `[PHONE]` | 1.000 [1.000, 1.000] | 0.515 [0.397, 0.642] | 0.680 [0.568, 0.782] | 34 | 0 | 32 | 66 |
| `[STREET_ADDRESS]` | 1.000 [0.000, 1.000] | 0.029 [0.000, 0.072] | 0.056 [0.000, 0.135] | 2 | 0 | 68 | 70 |
| **macro** | 0.971 [0.761, 0.987] | 0.533 [0.503, 0.564] | 0.688 [0.613, 0.715] | 174 | 8 | 184 | 358 |
| **micro** | 0.956 [0.926, 0.982] | 0.486 [0.444, 0.529] | 0.644 [0.605, 0.683] | 174 | 8 | 184 | 358 |

### `multi_paragraph` (54 rows)

| Placeholder | Precision (95% CI) | Recall (95% CI) | F1 (95% CI) | TP | FP | FN | Support |
|---|---|---|---|---:|---:|---:|---:|
| `[DATE]` | 0.875 [0.750, 0.972] | 1.000 [1.000, 1.000] | 0.933 [0.857, 0.986] | 28 | 4 | 0 | 28 |
| `[EMAIL]` | 1.000 [1.000, 1.000] | 0.980 [0.933, 1.000] | 0.990 [0.966, 1.000] | 48 | 0 | 1 | 49 |
| `[PERSON_NAME]` | 1.000 [1.000, 1.000] | 0.160 [0.071, 0.283] | 0.277 [0.133, 0.441] | 13 | 0 | 68 | 81 |
| `[PHONE]` | 0.800 [0.632, 0.952] | 0.432 [0.270, 0.594] | 0.561 [0.391, 0.706] | 16 | 4 | 21 | 37 |
| `[STREET_ADDRESS]` | 0.875 [0.692, 1.000] | 0.171 [0.054, 0.308] | 0.286 [0.103, 0.456] | 7 | 1 | 34 | 41 |
| **macro** | 0.910 [0.845, 0.974] | 0.549 [0.497, 0.612] | 0.685 [0.637, 0.735] | 112 | 9 | 124 | 236 |
| **micro** | 0.926 [0.874, 0.972] | 0.475 [0.413, 0.548] | 0.627 [0.570, 0.690] | 112 | 9 | 124 | 236 |

### `structured` (142 rows)

| Placeholder | Precision (95% CI) | Recall (95% CI) | F1 (95% CI) | TP | FP | FN | Support |
|---|---|---|---|---:|---:|---:|---:|
| `[DATE]` | 0.935 [0.881, 0.985] | 1.000 [1.000, 1.000] | 0.966 [0.937, 0.993] | 72 | 5 | 0 | 72 |
| `[EMAIL]` | 0.990 [0.968, 1.000] | 0.962 [0.922, 0.991] | 0.976 [0.953, 0.995] | 102 | 1 | 4 | 106 |
| `[PERSON_NAME]` | 1.000 [1.000, 1.000] | 0.325 [0.243, 0.426] | 0.491 [0.390, 0.597] | 53 | 0 | 110 | 163 |
| `[PHONE]` | 0.885 [0.810, 0.955] | 0.635 [0.531, 0.734] | 0.740 [0.656, 0.813] | 54 | 7 | 31 | 85 |
| `[STREET_ADDRESS]` | 0.895 [0.769, 1.000] | 0.362 [0.272, 0.460] | 0.515 [0.415, 0.611] | 34 | 4 | 60 | 94 |
| **macro** | 0.941 [0.910, 0.969] | 0.657 [0.618, 0.697] | 0.774 [0.743, 0.804] | 315 | 17 | 205 | 520 |
| **micro** | 0.949 [0.922, 0.971] | 0.606 [0.555, 0.656] | 0.739 [0.698, 0.778] | 315 | 17 | 205 | 520 |


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
- `ai4p-de-20695375` [opf] value=`Hermannstädter Weg`  context: ...'n mit dem Bild einer Straße – Hermannstädter Weg – die endlos in den Horizont '...
- `ai4p-de-20696020` [opf] value=`Klagenfurt am Wörthersee St. Veiter Vorstadt`  context: ...'arf während der Probenahme in Klagenfurt am Wörthersee St. Veiter Vorstadt begleite.'...

### `[PHONE]`
- `ai4p-de-20694958` [regex] value=`0901 700729
12`  context: ...'. Sozialversicherungs‑Nummer: 0901 700729\n12. Steuer‑Identifikationsnummer'...
- `ai4p-de-20695082` [regex] value=`0331 620902`  context: ...'ine Sozialversicherungsnummer 0331 620902 an, während das System seine '...
- `ai4p-de-20695249` [regex] value=`0432 570801`  context: ...'FW\nSozialversicherungsnummer: 0432 570801\nSteuer‑Identifikationsnummer:'...
- `ai4p-de-20695439` [regex] value=`0404 031110`  context: ...'ogene Daten nur im Rahmen von 0404 031110 nutzen)\n\nBitte bis zum 3. Mai'...
- `ai4p-de-20695690` [regex] value=`0652 370604`  context: ...'. Sozialversicherungs‑Nummer: 0652 370604\n9. Steuer‑Identifikationsnumm'...

### `[STREET_ADDRESS]`
- `ai4p-de-20695501` [opf] value=`St. Ruprecht`  context: ...' aus Klagenfurt am Wörthersee St. Ruprecht St. Ruprecht zeigt das Tagebu'...
- `ai4p-de-20695827` [opf] value=`Hausnummer: 77b`  context: ...'\nAdresse:\n  Straße: Rennweg\n  Hausnummer: 77b\n  PLZ: 5020\n  Stadt: Linz Kap'...
- `ai4p-de-20695827` [opf] value=`Linz Kaplanhof`  context: ...'mer: 77b\n  PLZ: 5020\n  Stadt: Linz Kaplanhof\n\nWie bewerten Sie die Attrakt'...
- `ai4p-de-20695925` [opf] value=`St. Veiter Vorstadt`  context: ...' aus Klagenfurt am Wörthersee St. Veiter Vorstadt mit Wohnsitz an der Augarten\u202f'...
- `ai4p-de-20695998` [opf] value=`5020 Linz Hafenviertel`  context: ...'tte prüft eure Postanschrift (5020 Linz Hafenviertel) und bestätigt die Richtigkei'...


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
- `ai4p-de-20694936` value=`Ricco Tsakalos`  context: ...'Der Projektleiter, Meister Ricco Tsakalos, weist darauf hin, dass das E'...
- `ai4p-de-20694937` value=`Xhyle Dinouard`  context: ...'eten, wobei die Kontaktperson Xhyle Dinouard ebenfalls unter der Telefonnu'...
- `ai4p-de-20694945` value=`Lourin Buffo Kottler`  context: ...'\nKundendaten:\nBürgermeisterin Lourin Buffo Kottler\nSandgasse 1437\n6020 Linz\nE‑Ma'...

### `[PHONE]`
- `ai4p-de-20694924` value=`+54-685227296`  context: ...'ta.com oder telefonisch unter +54-685227296 zur Verfügung. Wir freuen uns'...
- `ai4p-de-20694943` value=`+878.63.973.9334`  context: ...'‑Mail: M@hotmail.com\nTelefon: +878.63.973.9334\nPersonalausweis‑Nr.: 84394318'...
- `ai4p-de-20694954` value=`009929046 2990`  context: ...'C7977252. Ein kurzer Anruf an 009929046 2990 bestätigt, dass das Set im al'...
- `ai4p-de-20694958` value=`+20-459.555.0277`  context: ...'otmail.com\n7. Telefonkontakt: +20-459.555.0277\n8. Anschrift: Bahnhofstraße 1'...
- `ai4p-de-20694974` value=`(66) 6903 1936`  context: ...'doggweiler@yahoo.com\nTelefon: (66) 6903 1936\n\nGewünschte Ausrüstung:\n- Kam'...

### `[STREET_ADDRESS]`
- `ai4p-de-20694920` value=`Goethestraße 315, 1090 Wien Wieden`  context: ...'n Sie Ihre neue Anschrift an: Goethestraße 315, 1090 Wien Wieden.'...
- `ai4p-de-20694923` value=`Bertha-von-Suttner-Weg 3E in Klagenfurt am Wörthersee`  context: ...'neigenes Fitnessstudio in der Bertha-von-Suttner-Weg 3E in Klagenfurt am Wörthersee an. Mitarbeiter, die das Ange'...
- `ai4p-de-20694945` value=`Sandgasse 1437
6020 Linz`  context: ...'eisterin Lourin Buffo Kottler\nSandgasse 1437\n6020 Linz\nE‑Mail: LI@hotmail.com\nTelefo'...
- `ai4p-de-20694954` value=`Weingartshofstraße 6`  context: ...'Set im alten Lagerhaus in der Weingartshofstraße 6 aufgebaut wird. Der Regisseur'...
- `ai4p-de-20694958` value=`Bahnhofstraße 15, 8020 Linz`  context: ...'20-459.555.0277\n8. Anschrift: Bahnhofstraße 15, 8020 Linz\n9. Personalausweis‑Nummer: 49'...

