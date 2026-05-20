# Imported-dataset eval - ai4privacy_de

- Rows evaluated: **1,000**
- Rows with zero gold spans (after label-map filter): **37**
- Elapsed: **17.7s** (18ms/row)
- Projection-symmetric scoring: **on** (gold placeholder space: `[DATE], [EMAIL], [PERSON_NAME], [PHONE], [STREET_ADDRESS]`)

## Per-placeholder precision / recall

| Placeholder | Precision (95% CI) | Recall (95% CI) | F1 (95% CI) | TP | FP | FN | Support |
|---|---|---|---|---:|---:|---:|---:|
| `[DATE]` | 0.914 [0.885, 0.940] | 1.000 [1.000, 1.000] | 0.955 [0.939, 0.969] | 328 | 31 | 0 | 328 |
| `[EMAIL]` | 0.998 [0.994, 1.000] | 1.000 [1.000, 1.000] | 0.999 [0.997, 1.000] | 538 | 1 | 0 | 538 |
| `[PERSON_NAME]` | 0.740 [0.714, 0.767] | 0.889 [0.869, 0.912] | 0.808 [0.788, 0.828] | 707 | 249 | 88 | 795 |
| `[PHONE]` | 0.933 [0.904, 0.963] | 0.571 [0.523, 0.619] | 0.709 [0.669, 0.746] | 236 | 17 | 177 | 413 |
| `[STREET_ADDRESS]` | 0.442 [0.421, 0.462] | 0.925 [0.901, 0.946] | 0.598 [0.578, 0.616] | 515 | 649 | 42 | 557 |
| **macro** | 0.805 [0.794, 0.816] | 0.877 [0.866, 0.888] | 0.840 [0.831, 0.848] | 2324 | 947 | 307 | 2631 |
| **micro** | 0.710 [0.695, 0.724] | 0.883 [0.872, 0.895] | 0.788 [0.777, 0.798] | 2324 | 947 | 307 | 2631 |

## Per-length-bucket precision / recall

Row distribution across buckets: `sentence`: 690, `paragraph`: 114, `multi_paragraph`: 54, `structured`: 142

### `sentence` (690 rows)

| Placeholder | Precision (95% CI) | Recall (95% CI) | F1 (95% CI) | TP | FP | FN | Support |
|---|---|---|---|---:|---:|---:|---:|
| `[DATE]` | 0.928 [0.892, 0.960] | 1.000 [1.000, 1.000] | 0.963 [0.943, 0.980] | 181 | 14 | 0 | 181 |
| `[EMAIL]` | 1.000 [1.000, 1.000] | 1.000 [1.000, 1.000] | 1.000 [1.000, 1.000] | 304 | 0 | 0 | 304 |
| `[PERSON_NAME]` | 0.771 [0.740, 0.804] | 0.903 [0.875, 0.930] | 0.832 [0.809, 0.856] | 411 | 122 | 44 | 455 |
| `[PHONE]` | 0.957 [0.919, 0.986] | 0.587 [0.522, 0.651] | 0.727 [0.674, 0.778] | 132 | 6 | 93 | 225 |
| `[STREET_ADDRESS]` | 0.461 [0.439, 0.489] | 0.918 [0.887, 0.947] | 0.614 [0.591, 0.640] | 323 | 377 | 29 | 352 |
| **macro** | 0.823 [0.811, 0.836] | 0.882 [0.867, 0.896] | 0.851 [0.841, 0.862] | 1351 | 519 | 166 | 1517 |
| **micro** | 0.722 [0.705, 0.741] | 0.891 [0.876, 0.905] | 0.798 [0.784, 0.811] | 1351 | 519 | 166 | 1517 |

### `paragraph` (114 rows)

| Placeholder | Precision (95% CI) | Recall (95% CI) | F1 (95% CI) | TP | FP | FN | Support |
|---|---|---|---|---:|---:|---:|---:|
| `[DATE]` | 0.855 [0.754, 0.936] | 1.000 [1.000, 1.000] | 0.922 [0.860, 0.967] | 47 | 8 | 0 | 47 |
| `[EMAIL]` | 1.000 [1.000, 1.000] | 1.000 [1.000, 1.000] | 1.000 [1.000, 1.000] | 79 | 0 | 0 | 79 |
| `[PERSON_NAME]` | 0.719 [0.655, 0.792] | 0.906 [0.845, 0.960] | 0.802 [0.749, 0.857] | 87 | 34 | 9 | 96 |
| `[PHONE]` | 1.000 [1.000, 1.000] | 0.515 [0.397, 0.642] | 0.680 [0.568, 0.782] | 34 | 0 | 32 | 66 |
| `[STREET_ADDRESS]` | 0.470 [0.403, 0.552] | 0.900 [0.828, 0.961] | 0.618 [0.550, 0.693] | 63 | 71 | 7 | 70 |
| **macro** | 0.809 [0.782, 0.833] | 0.864 [0.829, 0.897] | 0.836 [0.810, 0.858] | 310 | 113 | 48 | 358 |
| **micro** | 0.733 [0.692, 0.774] | 0.866 [0.830, 0.899] | 0.794 [0.763, 0.824] | 310 | 113 | 48 | 358 |

### `multi_paragraph` (54 rows)

| Placeholder | Precision (95% CI) | Recall (95% CI) | F1 (95% CI) | TP | FP | FN | Support |
|---|---|---|---|---:|---:|---:|---:|
| `[DATE]` | 0.875 [0.750, 0.972] | 1.000 [1.000, 1.000] | 0.933 [0.857, 0.986] | 28 | 4 | 0 | 28 |
| `[EMAIL]` | 1.000 [1.000, 1.000] | 1.000 [1.000, 1.000] | 1.000 [1.000, 1.000] | 49 | 0 | 0 | 49 |
| `[PERSON_NAME]` | 0.767 [0.691, 0.855] | 0.852 [0.759, 0.934] | 0.807 [0.743, 0.867] | 69 | 21 | 12 | 81 |
| `[PHONE]` | 0.800 [0.632, 0.952] | 0.432 [0.270, 0.594] | 0.561 [0.391, 0.706] | 16 | 4 | 21 | 37 |
| `[STREET_ADDRESS]` | 0.352 [0.303, 0.415] | 0.902 [0.800, 0.977] | 0.507 [0.443, 0.574] | 37 | 68 | 4 | 41 |
| **macro** | 0.759 [0.712, 0.808] | 0.837 [0.795, 0.881] | 0.796 [0.760, 0.830] | 199 | 97 | 37 | 236 |
| **micro** | 0.672 [0.619, 0.731] | 0.843 [0.795, 0.892] | 0.748 [0.708, 0.791] | 199 | 97 | 37 | 236 |

### `structured` (142 rows)

| Placeholder | Precision (95% CI) | Recall (95% CI) | F1 (95% CI) | TP | FP | FN | Support |
|---|---|---|---|---:|---:|---:|---:|
| `[DATE]` | 0.935 [0.881, 0.985] | 1.000 [1.000, 1.000] | 0.966 [0.937, 0.993] | 72 | 5 | 0 | 72 |
| `[EMAIL]` | 0.991 [0.969, 1.000] | 1.000 [1.000, 1.000] | 0.995 [0.984, 1.000] | 106 | 1 | 0 | 106 |
| `[PERSON_NAME]` | 0.660 [0.604, 0.722] | 0.859 [0.807, 0.910] | 0.747 [0.699, 0.793] | 140 | 72 | 23 | 163 |
| `[PHONE]` | 0.885 [0.810, 0.955] | 0.635 [0.531, 0.734] | 0.740 [0.656, 0.813] | 54 | 7 | 31 | 85 |
| `[STREET_ADDRESS]` | 0.409 [0.373, 0.447] | 0.979 [0.945, 1.000] | 0.577 [0.540, 0.614] | 92 | 133 | 2 | 94 |
| **macro** | 0.776 [0.753, 0.798] | 0.895 [0.871, 0.916] | 0.831 [0.812, 0.848] | 464 | 218 | 56 | 520 |
| **micro** | 0.680 [0.653, 0.709] | 0.892 [0.868, 0.915] | 0.772 [0.749, 0.794] | 464 | 218 | 56 | 520 |


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
- `ai4p-de-20694931` [opf] value=`E‑Mail`  context: ...'etaillierter Bericht wird per E‑Mail an P@yahoo.com gesendet.'...
- `ai4p-de-20694945` [opf] value=`Buffo Kottler
Sandgasse`  context: ...'daten:\nBürgermeisterin Lourin Buffo Kottler\nSandgasse 1437\n6020 Linz\nE‑Mail: LI@hot'...
- `ai4p-de-20694971` [opf] value=`Geschlechtsfluid`  context: ...'sranur Monzeglio (Geschlecht: Geschlechtsfluid, Sex: F), erreichbar unter ST'...
- `ai4p-de-20694974` [opf] value=`Bigender`  context: ...'ht: M / Geschlechtsidentität: Bigender\nE‑Mail: noëdoggweiler@yahoo.c'...
- `ai4p-de-20694974` [opf] value=`UHS‑II`  context: ...'rken)\n- Speicherkarte 128\u202fGB (UHS‑II)\n\nVerwendungszweck: Landschaf'...

### `[PHONE]`
- `ai4p-de-20694958` [regex] value=`0901 700729
12`  context: ...'. Sozialversicherungs‑Nummer: 0901 700729\n12. Steuer‑Identifikationsnummer'...
- `ai4p-de-20695082` [regex] value=`0331 620902`  context: ...'ine Sozialversicherungsnummer 0331 620902 an, während das System seine '...
- `ai4p-de-20695249` [regex] value=`0432 570801`  context: ...'FW\nSozialversicherungsnummer: 0432 570801\nSteuer‑Identifikationsnummer:'...
- `ai4p-de-20695439` [regex] value=`0404 031110`  context: ...'ogene Daten nur im Rahmen von 0404 031110 nutzen)\n\nBitte bis zum 3. Mai'...
- `ai4p-de-20695690` [regex] value=`0652 370604`  context: ...'. Sozialversicherungs‑Nummer: 0652 370604\n9. Steuer‑Identifikationsnumm'...

### `[STREET_ADDRESS]`
- `ai4p-de-20694920` [opf] value=`Wien`  context: ...'ft an: Goethestraße 315, 1090 Wien Wieden.'...
- `ai4p-de-20694920` [opf] value=`Wieden`  context: ...': Goethestraße 315, 1090 Wien Wieden.'...
- `ai4p-de-20694923` [opf] value=`Wörthersee`  context: ...'ttner-Weg 3E in Klagenfurt am Wörthersee an. Mitarbeiter, die das Ange'...
- `ai4p-de-20694943` [opf] value=`Geschlechterqueer`  context: ...'h\nGeschlecht (identifiziert): Geschlechterqueer\nAdresse: Zollerstraße 15, 404'...
- `ai4p-de-20694943` [opf] value=`Zirl
E‑Mail`  context: ...'dresse: Zollerstraße 15, 4040 Zirl\nE‑Mail: M@hotmail.com\nTelefon: +878.'...


## False-negative samples

### `[PERSON_NAME]`
- `ai4p-de-20694963` value=`Maryléne Gossen Alosius Gyárfás`  context: ...'llen“, bevor die Unterschrift Maryléne Gossen Alosius Gyárfás – begleitet von einem Datum M'...
- `ai4p-de-20694969` value=`Heejin Tanoa`  context: ...'l erstellt, das die Daten von Heejin Tanoa enthält, inklusive Passnummer'...
- `ai4p-de-20695138` value=`Praise Dusca de Cubellis Von Zobeltitz Bönsel`  context: ...'Sehr geehrte/r Sen Praise Dusca de Cubellis Von Zobeltitz Bönsel, wir benötigen Ihre Angaben z'...
- `ai4p-de-20695150` value=`Cathie Ruqaya Suslova Tchetchelachvili`  context: ...'Ein internes Memo von Cathie Ruqaya Suslova Tchetchelachvili an das Risikomanagement‑Team '...
- `ai4p-de-20695154` value=`Irina-Gabriela Mongelos Nai Griego`  context: ...'th Report – Dokumentation für Irina-Gabriela Mongelos Nai Griego\n1. Persönliche Angaben: Gebur'...

### `[PHONE]`
- `ai4p-de-20694924` value=`+54-685227296`  context: ...'ta.com oder telefonisch unter +54-685227296 zur Verfügung. Wir freuen uns'...
- `ai4p-de-20694943` value=`+878.63.973.9334`  context: ...'‑Mail: M@hotmail.com\nTelefon: +878.63.973.9334\nPersonalausweis‑Nr.: 84394318'...
- `ai4p-de-20694954` value=`009929046 2990`  context: ...'C7977252. Ein kurzer Anruf an 009929046 2990 bestätigt, dass das Set im al'...
- `ai4p-de-20694958` value=`+20-459.555.0277`  context: ...'otmail.com\n7. Telefonkontakt: +20-459.555.0277\n8. Anschrift: Bahnhofstraße 1'...
- `ai4p-de-20694974` value=`(66) 6903 1936`  context: ...'doggweiler@yahoo.com\nTelefon: (66) 6903 1936\n\nGewünschte Ausrüstung:\n- Kam'...

### `[STREET_ADDRESS]`
- `ai4p-de-20695015` value=`4020`  context: ...'schließlich (336).7147153 und 4020, damit Support‑Teams weltweit'...
- `ai4p-de-20695213` value=`8020`  context: ...'chließlich +4357-007.2584 und 8020, an die unten angegebene Adre'...
- `ai4p-de-20695271` value=`Innsbruck`  context: ...'iche Bankzinssatz, der an der Innsbruck Börse veröffentlicht wird, vo'...
- `ai4p-de-20695331` value=`3109 und Rungges`  context: ...'s System die Gesamtkosten pro 3109 und Rungges korrekt berechnen kann.'...
- `ai4p-de-20695360` value=`4040`  context: ...' Ihre Postleitzahl (ZIPCODE): 4040\nBitte senden Sie die Antworte'...

