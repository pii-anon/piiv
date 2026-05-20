# Imported-dataset eval - ai4privacy_de

- Rows evaluated: **1,000**
- Rows with zero gold spans (after label-map filter): **37**
- Elapsed: **2611.4s** (2611ms/row)
- Projection-symmetric scoring: **on** (gold placeholder space: `[DATE], [EMAIL], [PERSON_NAME], [PHONE], [STREET_ADDRESS]`)

## Per-placeholder precision / recall

| Placeholder | Precision (95% CI) | Recall (95% CI) | F1 (95% CI) | TP | FP | FN | Support |
|---|---|---|---|---:|---:|---:|---:|
| `[DATE]` | 0.914 [0.885, 0.940] | 1.000 [1.000, 1.000] | 0.955 [0.939, 0.969] | 328 | 31 | 0 | 328 |
| `[EMAIL]` | 0.998 [0.994, 1.000] | 0.974 [0.959, 0.987] | 0.986 [0.978, 0.993] | 524 | 1 | 14 | 538 |
| `[PERSON_NAME]` | 0.991 [0.983, 0.997] | 0.936 [0.916, 0.955] | 0.962 [0.951, 0.973] | 744 | 7 | 51 | 795 |
| `[PHONE]` | 0.933 [0.904, 0.963] | 0.571 [0.523, 0.619] | 0.709 [0.669, 0.746] | 236 | 17 | 177 | 413 |
| `[STREET_ADDRESS]` | 0.958 [0.930, 0.980] | 0.569 [0.532, 0.611] | 0.714 [0.681, 0.746] | 317 | 14 | 240 | 557 |
| **macro** | 0.959 [0.948, 0.968] | 0.810 [0.796, 0.823] | 0.878 [0.869, 0.887] | 2149 | 70 | 482 | 2631 |
| **micro** | 0.968 [0.961, 0.975] | 0.817 [0.802, 0.831] | 0.886 [0.877, 0.895] | 2149 | 70 | 482 | 2631 |

## Per-length-bucket precision / recall

Row distribution across buckets: `sentence`: 690, `paragraph`: 114, `multi_paragraph`: 54, `structured`: 142

### `sentence` (690 rows)

| Placeholder | Precision (95% CI) | Recall (95% CI) | F1 (95% CI) | TP | FP | FN | Support |
|---|---|---|---|---:|---:|---:|---:|
| `[DATE]` | 0.928 [0.892, 0.960] | 1.000 [1.000, 1.000] | 0.963 [0.943, 0.980] | 181 | 14 | 0 | 181 |
| `[EMAIL]` | 1.000 [1.000, 1.000] | 0.977 [0.959, 0.991] | 0.988 [0.979, 0.995] | 297 | 0 | 7 | 304 |
| `[PERSON_NAME]` | 0.991 [0.981, 0.998] | 0.936 [0.914, 0.957] | 0.963 [0.950, 0.974] | 426 | 4 | 29 | 455 |
| `[PHONE]` | 0.957 [0.919, 0.986] | 0.587 [0.522, 0.651] | 0.727 [0.674, 0.778] | 132 | 6 | 93 | 225 |
| `[STREET_ADDRESS]` | 0.965 [0.934, 0.990] | 0.545 [0.499, 0.596] | 0.697 [0.656, 0.738] | 192 | 7 | 160 | 352 |
| **macro** | 0.968 [0.956, 0.979] | 0.809 [0.792, 0.827] | 0.881 [0.869, 0.894] | 1228 | 31 | 289 | 1517 |
| **micro** | 0.975 [0.967, 0.983] | 0.809 [0.791, 0.828] | 0.885 [0.872, 0.896] | 1228 | 31 | 289 | 1517 |

### `paragraph` (114 rows)

| Placeholder | Precision (95% CI) | Recall (95% CI) | F1 (95% CI) | TP | FP | FN | Support |
|---|---|---|---|---:|---:|---:|---:|
| `[DATE]` | 0.855 [0.754, 0.936] | 1.000 [1.000, 1.000] | 0.922 [0.860, 0.967] | 47 | 8 | 0 | 47 |
| `[EMAIL]` | 1.000 [1.000, 1.000] | 0.975 [0.936, 1.000] | 0.987 [0.967, 1.000] | 77 | 0 | 2 | 79 |
| `[PERSON_NAME]` | 0.968 [0.930, 1.000] | 0.958 [0.916, 0.991] | 0.963 [0.936, 0.989] | 92 | 3 | 4 | 96 |
| `[PHONE]` | 1.000 [1.000, 1.000] | 0.515 [0.397, 0.642] | 0.680 [0.568, 0.782] | 34 | 0 | 32 | 66 |
| `[STREET_ADDRESS]` | 0.969 [0.903, 1.000] | 0.443 [0.324, 0.554] | 0.608 [0.488, 0.709] | 31 | 1 | 39 | 70 |
| **macro** | 0.958 [0.936, 0.977] | 0.778 [0.742, 0.814] | 0.859 [0.833, 0.882] | 281 | 12 | 77 | 358 |
| **micro** | 0.959 [0.936, 0.978] | 0.785 [0.746, 0.822] | 0.863 [0.836, 0.889] | 281 | 12 | 77 | 358 |

### `multi_paragraph` (54 rows)

| Placeholder | Precision (95% CI) | Recall (95% CI) | F1 (95% CI) | TP | FP | FN | Support |
|---|---|---|---|---:|---:|---:|---:|
| `[DATE]` | 0.875 [0.750, 0.972] | 1.000 [1.000, 1.000] | 0.933 [0.857, 0.986] | 28 | 4 | 0 | 28 |
| `[EMAIL]` | 1.000 [1.000, 1.000] | 0.980 [0.933, 1.000] | 0.990 [0.966, 1.000] | 48 | 0 | 1 | 49 |
| `[PERSON_NAME]` | 1.000 [1.000, 1.000] | 0.963 [0.917, 1.000] | 0.981 [0.957, 1.000] | 78 | 0 | 3 | 81 |
| `[PHONE]` | 0.800 [0.632, 0.952] | 0.432 [0.270, 0.594] | 0.561 [0.391, 0.706] | 16 | 4 | 21 | 37 |
| `[STREET_ADDRESS]` | 0.920 [0.760, 1.000] | 0.561 [0.400, 0.722] | 0.697 [0.540, 0.831] | 23 | 2 | 18 | 41 |
| **macro** | 0.919 [0.872, 0.967] | 0.787 [0.744, 0.828] | 0.848 [0.815, 0.881] | 193 | 10 | 43 | 236 |
| **micro** | 0.951 [0.921, 0.980] | 0.818 [0.778, 0.858] | 0.879 [0.850, 0.907] | 193 | 10 | 43 | 236 |

### `structured` (142 rows)

| Placeholder | Precision (95% CI) | Recall (95% CI) | F1 (95% CI) | TP | FP | FN | Support |
|---|---|---|---|---:|---:|---:|---:|
| `[DATE]` | 0.935 [0.881, 0.985] | 1.000 [1.000, 1.000] | 0.966 [0.937, 0.993] | 72 | 5 | 0 | 72 |
| `[EMAIL]` | 0.990 [0.968, 1.000] | 0.962 [0.922, 0.991] | 0.976 [0.953, 0.995] | 102 | 1 | 4 | 106 |
| `[PERSON_NAME]` | 1.000 [1.000, 1.000] | 0.908 [0.831, 0.964] | 0.952 [0.908, 0.982] | 148 | 0 | 15 | 163 |
| `[PHONE]` | 0.885 [0.810, 0.955] | 0.635 [0.531, 0.734] | 0.740 [0.656, 0.813] | 54 | 7 | 31 | 85 |
| `[STREET_ADDRESS]` | 0.947 [0.895, 0.987] | 0.755 [0.667, 0.842] | 0.840 [0.779, 0.894] | 71 | 4 | 23 | 94 |
| **macro** | 0.951 [0.929, 0.971] | 0.852 [0.819, 0.884] | 0.899 [0.876, 0.920] | 447 | 17 | 73 | 520 |
| **micro** | 0.963 [0.946, 0.978] | 0.860 [0.825, 0.892] | 0.909 [0.886, 0.929] | 447 | 17 | 73 | 520 |


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
- `ai4p-de-20694966` [opf] value=`Frau Müller`  context: ...'n.\nFür Rückfragen steht Ihnen Frau Müller unter +43.110.380-4965 zur Ve'...
- `ai4p-de-20695228` [opf] value=`Professorin Orion`  context: ...'r feiern die Entdeckung der **Professorin Orion**‑Galaxie! 🎉\n📅 Datum des Even'...
- `ai4p-de-20695372` [opf] value=`Graz Gries Gries`  context: ...'r Stille des Raumes hallt ihr Graz Gries Gries wider, während die Straße vor'...
- `ai4p-de-20695671` [opf] value=`Redakteur`  context: ...'echt Männlich) schrieb an den Redakteur, dass die revolutionären Stof'...
- `ai4p-de-20695800` [opf] value=`Alois-Huber`  context: ...'gt an der Info‑Station in der Alois-Huber-Straße\u202f3364 in Linz; dort prü'...

### `[PHONE]`
- `ai4p-de-20694958` [regex] value=`0901 700729
12`  context: ...'. Sozialversicherungs‑Nummer: 0901 700729\n12. Steuer‑Identifikationsnummer'...
- `ai4p-de-20695082` [regex] value=`0331 620902`  context: ...'ine Sozialversicherungsnummer 0331 620902 an, während das System seine '...
- `ai4p-de-20695249` [regex] value=`0432 570801`  context: ...'FW\nSozialversicherungsnummer: 0432 570801\nSteuer‑Identifikationsnummer:'...
- `ai4p-de-20695439` [regex] value=`0404 031110`  context: ...'ogene Daten nur im Rahmen von 0404 031110 nutzen)\n\nBitte bis zum 3. Mai'...
- `ai4p-de-20695690` [regex] value=`0652 370604`  context: ...'. Sozialversicherungs‑Nummer: 0652 370604\n9. Steuer‑Identifikationsnumm'...

### `[STREET_ADDRESS]`
- `ai4p-de-20695083` [opf] value=`6020`  context: ...'d die zugehörige Postleitzahl 6020 automatisch mit der Personala'...
- `ai4p-de-20695715` [opf] value=`Innsbruck Saggen Saggen – 6020`  context: ...'mannstraße 768\n10. Stadt/PLZ: Innsbruck Saggen Saggen – 6020\n11. Ihre Kurz‑Rückmeldung zum'...
- `ai4p-de-20695998` [opf] value=`5020 Linz Hafenviertel`  context: ...'tte prüft eure Postanschrift (5020 Linz Hafenviertel) und bestätigt die Richtigkei'...
- `ai4p-de-20696508` [opf] value=`Innsbruck Sankt Nikolaus`  context: ...'stenstraße\nPostleitzahl: 6020 Innsbruck Sankt Nikolaus\nEinlass ab 19:00 Uhr. Viel Sp'...
- `ai4p-de-20696705` [opf] value=`radmuñez@outlook.com`  context: ...'ine Bestätigung per E‑Mail an radmuñez@outlook.com.'...


## False-negative samples

### `[EMAIL]`
- `ai4p-de-20694974` value=`noëdoggweiler@yahoo.com`  context: ...'tsidentität: Bigender\nE‑Mail: noëdoggweiler@yahoo.com\nTelefon: (66) 6903 1936\n\nGewü'...
- `ai4p-de-20695275` value=`guizoppè@gmail.com`  context: ...'ren Sie uns bitte per E‑Mail (guizoppè@gmail.com) oder Telefon (0042-13 158 04'...
- `ai4p-de-20695432` value=`çinarrowan@hotmail.com`  context: ...'e Ansprechpartner per E‑Mail (çinarrowan@hotmail.com) und Telefon (+78.63887-6542)'...
- `ai4p-de-20695554` value=`maliilühmann@yahoo.com`  context: ...'burtsdatum: Mai/61\n5. E‑Mail: maliilühmann@yahoo.com\n6. Telefon: +435 38.964-3663\n'...
- `ai4p-de-20695871` value=`tomysodré@gmail.com`  context: ...' Sie Ihre Bewerbung inklusive tomysodré@gmail.com und +84 26874 5996 bis zum 11'...

### `[PERSON_NAME]`
- `ai4p-de-20694945` value=`Maria-Rosa Mielsch`  context: ...'ben.\nMit freundlichen Grüßen,\nMaria-Rosa Mielsch\nInhaberin Bone‑and‑Shell‑Desi'...
- `ai4p-de-20694971` value=`Büsranur Monzeglio`  context: ...'e‑Teams enthält Einträge wie: Büsranur Monzeglio (Geschlecht: Geschlechtsfluid'...
- `ai4p-de-20695025` value=`Pao Aynal`  context: ...'Name: Pao Aynal\nGeburtsdatum: 2024-01-22T00:0'...
- `ai4p-de-20695135` value=`Dod Stehly`  context: ...'Meister Dod Stehly,\n\nich hoffe, es geht Ihnen gu'...
- `ai4p-de-20695161` value=`Khunaf Záchenská`  context: ...'Magistrat Khunaf Záchenská lädt Sie herzlich zu den neue'...

### `[PHONE]`
- `ai4p-de-20694924` value=`+54-685227296`  context: ...'ta.com oder telefonisch unter +54-685227296 zur Verfügung. Wir freuen uns'...
- `ai4p-de-20694943` value=`+878.63.973.9334`  context: ...'‑Mail: M@hotmail.com\nTelefon: +878.63.973.9334\nPersonalausweis‑Nr.: 84394318'...
- `ai4p-de-20694954` value=`009929046 2990`  context: ...'C7977252. Ein kurzer Anruf an 009929046 2990 bestätigt, dass das Set im al'...
- `ai4p-de-20694958` value=`+20-459.555.0277`  context: ...'otmail.com\n7. Telefonkontakt: +20-459.555.0277\n8. Anschrift: Bahnhofstraße 1'...
- `ai4p-de-20694974` value=`(66) 6903 1936`  context: ...'doggweiler@yahoo.com\nTelefon: (66) 6903 1936\n\nGewünschte Ausrüstung:\n- Kam'...

### `[STREET_ADDRESS]`
- `ai4p-de-20694945` value=`Sandgasse 1437
6020 Linz`  context: ...'eisterin Lourin Buffo Kottler\nSandgasse 1437\n6020 Linz\nE‑Mail: LI@hotmail.com\nTelefo'...
- `ai4p-de-20694963` value=`Innsbruck`  context: ...' den Hallen des Rathauses von Innsbruck ausgelegt liegt, fordert die '...
- `ai4p-de-20694968` value=`Roittnerstraße 2 in Linz sowie die Postleitzahl 5020`  context: ...'her, dass Ihre Kontaktadresse Roittnerstraße\u202f2 in Linz sowie die Postleitzahl 5020 aktuell sind.'...
- `ai4p-de-20695015` value=`4020`  context: ...'schließlich (336).7147153 und 4020, damit Support‑Teams weltweit'...
- `ai4p-de-20695039` value=`Wien`  context: ...'len, die am Juli 14., 1987 in Wien abgeschlossen wurde; bitte se'...

