# Imported-dataset eval - ai4privacy_de

- Rows evaluated: **200**
- Rows with zero gold spans (after label-map filter): **9**
- Elapsed: **3.8s** (19ms/row)
- Projection-symmetric scoring: **on** (gold placeholder space: `[DATE], [EMAIL], [PERSON_NAME], [PHONE], [STREET_ADDRESS]`)

## Per-placeholder precision / recall

| Placeholder | Precision (95% CI) | Recall (95% CI) | F1 (95% CI) | TP | FP | FN | Support |
|---|---|---|---|---:|---:|---:|---:|
| `[DATE]` | 0.971 [0.929, 1.000] | 1.000 [1.000, 1.000] | 0.985 [0.963, 1.000] | 67 | 2 | 0 | 67 |
| `[EMAIL]` | 0.990 [0.965, 1.000] | 1.000 [1.000, 1.000] | 0.995 [0.982, 1.000] | 98 | 1 | 0 | 98 |
| `[PERSON_NAME]` | 0.741 [0.686, 0.801] | 0.887 [0.834, 0.933] | 0.808 [0.764, 0.852] | 126 | 44 | 16 | 142 |
| `[PHONE]` | 0.940 [0.870, 1.000] | 0.644 [0.530, 0.750] | 0.764 [0.672, 0.842] | 47 | 3 | 26 | 73 |
| `[STREET_ADDRESS]` | 0.463 [0.419, 0.509] | 0.936 [0.880, 0.979] | 0.620 [0.576, 0.661] | 88 | 102 | 6 | 94 |
| **macro** | 0.821 [0.801, 0.841] | 0.893 [0.867, 0.918] | 0.856 [0.837, 0.873] | 426 | 152 | 48 | 474 |
| **micro** | 0.737 [0.706, 0.770] | 0.899 [0.874, 0.923] | 0.810 [0.787, 0.832] | 426 | 152 | 48 | 474 |

## Per-length-bucket precision / recall

Row distribution across buckets: `sentence`: 134, `paragraph`: 31, `multi_paragraph`: 4, `structured`: 31

### `sentence` (134 rows)

| Placeholder | Precision (95% CI) | Recall (95% CI) | F1 (95% CI) | TP | FP | FN | Support |
|---|---|---|---|---:|---:|---:|---:|
| `[DATE]` | 0.950 [0.879, 1.000] | 1.000 [1.000, 1.000] | 0.974 [0.935, 1.000] | 38 | 2 | 0 | 38 |
| `[EMAIL]` | 1.000 [1.000, 1.000] | 1.000 [1.000, 1.000] | 1.000 [1.000, 1.000] | 53 | 0 | 0 | 53 |
| `[PERSON_NAME]` | 0.755 [0.680, 0.831] | 0.887 [0.815, 0.950] | 0.816 [0.763, 0.866] | 71 | 23 | 9 | 80 |
| `[PHONE]` | 0.966 [0.880, 1.000] | 0.683 [0.526, 0.821] | 0.800 [0.678, 0.897] | 28 | 1 | 13 | 41 |
| `[STREET_ADDRESS]` | 0.475 [0.424, 0.533] | 0.921 [0.842, 0.983] | 0.627 [0.575, 0.682] | 58 | 64 | 5 | 63 |
| **macro** | 0.829 [0.800, 0.856] | 0.898 [0.862, 0.932] | 0.862 [0.837, 0.886] | 248 | 90 | 27 | 275 |
| **micro** | 0.734 [0.694, 0.776] | 0.902 [0.865, 0.934] | 0.809 [0.780, 0.838] | 248 | 90 | 27 | 275 |

### `paragraph` (31 rows)

| Placeholder | Precision (95% CI) | Recall (95% CI) | F1 (95% CI) | TP | FP | FN | Support |
|---|---|---|---|---:|---:|---:|---:|
| `[DATE]` | 1.000 [1.000, 1.000] | 1.000 [1.000, 1.000] | 1.000 [1.000, 1.000] | 14 | 0 | 0 | 14 |
| `[EMAIL]` | 1.000 [1.000, 1.000] | 1.000 [1.000, 1.000] | 1.000 [1.000, 1.000] | 16 | 0 | 0 | 16 |
| `[PERSON_NAME]` | 0.667 [0.516, 0.818] | 0.889 [0.733, 1.000] | 0.762 [0.638, 0.864] | 16 | 8 | 2 | 18 |
| `[PHONE]` | 1.000 [1.000, 1.000] | 0.846 [0.625, 1.000] | 0.917 [0.769, 1.000] | 11 | 0 | 2 | 13 |
| `[STREET_ADDRESS]` | 0.571 [0.423, 0.739] | 0.923 [0.750, 1.000] | 0.706 [0.563, 0.829] | 12 | 9 | 1 | 13 |
| **macro** | 0.848 [0.804, 0.897] | 0.932 [0.872, 0.982] | 0.888 [0.850, 0.926] | 69 | 17 | 5 | 74 |
| **micro** | 0.802 [0.735, 0.873] | 0.932 [0.875, 0.984] | 0.863 [0.817, 0.908] | 69 | 17 | 5 | 74 |

### `multi_paragraph` (4 rows)

| Placeholder | Precision (95% CI) | Recall (95% CI) | F1 (95% CI) | TP | FP | FN | Support |
|---|---|---|---|---:|---:|---:|---:|
| `[DATE]` | 1.000 [0.000, 1.000] | 1.000 [0.000, 1.000] | 1.000 [0.000, 1.000] | 1 | 0 | 0 | 1 |
| `[EMAIL]` | 1.000 [1.000, 1.000] | 1.000 [1.000, 1.000] | 1.000 [1.000, 1.000] | 5 | 0 | 0 | 5 |
| `[PERSON_NAME]` | 0.750 [0.400, 1.000] | 1.000 [1.000, 1.000] | 0.857 [0.571, 1.000] | 6 | 2 | 0 | 6 |
| `[PHONE]` | 1.000 [0.000, 1.000] | 0.250 [0.000, 0.750] | 0.400 [0.000, 0.857] | 1 | 0 | 3 | 4 |
| `[STREET_ADDRESS]` | 0.429 [0.250, 1.000] | 1.000 [1.000, 1.000] | 0.600 [0.400, 1.000] | 3 | 4 | 0 | 3 |
| **macro** | 0.836 [0.394, 0.900] | 0.850 [0.600, 0.900] | 0.843 [0.476, 0.900] | 16 | 6 | 3 | 19 |
| **micro** | 0.727 [0.545, 0.909] | 0.842 [0.750, 0.923] | 0.780 [0.632, 0.909] | 16 | 6 | 3 | 19 |

### `structured` (31 rows)

| Placeholder | Precision (95% CI) | Recall (95% CI) | F1 (95% CI) | TP | FP | FN | Support |
|---|---|---|---|---:|---:|---:|---:|
| `[DATE]` | 1.000 [1.000, 1.000] | 1.000 [1.000, 1.000] | 1.000 [1.000, 1.000] | 14 | 0 | 0 | 14 |
| `[EMAIL]` | 0.960 [0.869, 1.000] | 1.000 [1.000, 1.000] | 0.980 [0.930, 1.000] | 24 | 1 | 0 | 24 |
| `[PERSON_NAME]` | 0.750 [0.630, 0.870] | 0.868 [0.757, 0.970] | 0.805 [0.697, 0.899] | 33 | 11 | 5 | 38 |
| `[PHONE]` | 0.778 [0.500, 1.000] | 0.467 [0.188, 0.715] | 0.583 [0.300, 0.800] | 7 | 2 | 8 | 15 |
| `[STREET_ADDRESS]` | 0.375 [0.278, 0.500] | 1.000 [1.000, 1.000] | 0.545 [0.435, 0.667] | 15 | 25 | 0 | 15 |
| **macro** | 0.773 [0.718, 0.830] | 0.867 [0.813, 0.918] | 0.817 [0.771, 0.857] | 93 | 39 | 13 | 106 |
| **micro** | 0.705 [0.632, 0.782] | 0.877 [0.825, 0.920] | 0.782 [0.727, 0.831] | 93 | 39 | 13 | 106 |


## False-positive samples

### `[DATE]`
- `ai4p-de-20695161` [regex] value=`74-64.963`  context: ...'k.com oder telefonisch unter +74-64.963 5015. Für die Anmeldung benöt'...
- `ai4p-de-20695280` [regex] value=`27.46.19`  context: ...'rreichen Sie mich unter 03.98 27.46.19 oder per E‑Mail an FML@gmail.'...

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

