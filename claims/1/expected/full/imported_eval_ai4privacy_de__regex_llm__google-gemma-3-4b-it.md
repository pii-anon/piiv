# Imported-dataset eval - ai4privacy_de

- Rows evaluated: **1,000**
- Rows with zero gold spans (after label-map filter): **37**
- Elapsed: **1483.5s** (1483ms/row)
- Projection-symmetric scoring: **on** (gold placeholder space: `[DATE], [EMAIL], [PERSON_NAME], [PHONE], [STREET_ADDRESS]`)

## Per-placeholder precision / recall

| Placeholder | Precision (95% CI) | Recall (95% CI) | F1 (95% CI) | TP | FP | FN | Support |
|---|---|---|---|---:|---:|---:|---:|
| `[DATE]` | 0.914 [0.885, 0.940] | 1.000 [1.000, 1.000] | 0.955 [0.939, 0.969] | 328 | 31 | 0 | 328 |
| `[EMAIL]` | 0.998 [0.994, 1.000] | 0.974 [0.959, 0.987] | 0.986 [0.978, 0.993] | 524 | 1 | 14 | 538 |
| `[PERSON_NAME]` | 0.919 [0.896, 0.938] | 0.852 [0.822, 0.878] | 0.884 [0.864, 0.901] | 677 | 60 | 118 | 795 |
| `[PHONE]` | 0.933 [0.904, 0.963] | 0.571 [0.523, 0.619] | 0.709 [0.669, 0.746] | 236 | 17 | 177 | 413 |
| `[STREET_ADDRESS]` | 0.680 [0.631, 0.726] | 0.661 [0.619, 0.698] | 0.670 [0.636, 0.701] | 368 | 173 | 189 | 557 |
| **macro** | 0.889 [0.876, 0.901] | 0.812 [0.797, 0.825] | 0.848 [0.837, 0.859] | 2133 | 282 | 498 | 2631 |
| **micro** | 0.883 [0.867, 0.898] | 0.811 [0.796, 0.824] | 0.845 [0.833, 0.856] | 2133 | 282 | 498 | 2631 |

## Per-length-bucket precision / recall

Row distribution across buckets: `sentence`: 690, `paragraph`: 114, `multi_paragraph`: 54, `structured`: 142

### `sentence` (690 rows)

| Placeholder | Precision (95% CI) | Recall (95% CI) | F1 (95% CI) | TP | FP | FN | Support |
|---|---|---|---|---:|---:|---:|---:|
| `[DATE]` | 0.928 [0.892, 0.960] | 1.000 [1.000, 1.000] | 0.963 [0.943, 0.980] | 181 | 14 | 0 | 181 |
| `[EMAIL]` | 1.000 [1.000, 1.000] | 0.977 [0.959, 0.991] | 0.988 [0.979, 0.995] | 297 | 0 | 7 | 304 |
| `[PERSON_NAME]` | 0.916 [0.886, 0.944] | 0.868 [0.835, 0.898] | 0.892 [0.868, 0.913] | 395 | 36 | 60 | 455 |
| `[PHONE]` | 0.957 [0.919, 0.986] | 0.587 [0.522, 0.651] | 0.727 [0.674, 0.778] | 132 | 6 | 93 | 225 |
| `[STREET_ADDRESS]` | 0.644 [0.583, 0.707] | 0.605 [0.556, 0.656] | 0.624 [0.581, 0.666] | 213 | 118 | 139 | 352 |
| **macro** | 0.889 [0.873, 0.905] | 0.807 [0.788, 0.826] | 0.846 [0.832, 0.860] | 1218 | 174 | 299 | 1517 |
| **micro** | 0.875 [0.853, 0.895] | 0.803 [0.782, 0.824] | 0.837 [0.822, 0.852] | 1218 | 174 | 299 | 1517 |

### `paragraph` (114 rows)

| Placeholder | Precision (95% CI) | Recall (95% CI) | F1 (95% CI) | TP | FP | FN | Support |
|---|---|---|---|---:|---:|---:|---:|
| `[DATE]` | 0.855 [0.754, 0.936] | 1.000 [1.000, 1.000] | 0.922 [0.860, 0.967] | 47 | 8 | 0 | 47 |
| `[EMAIL]` | 1.000 [1.000, 1.000] | 0.975 [0.936, 1.000] | 0.987 [0.967, 1.000] | 77 | 0 | 2 | 79 |
| `[PERSON_NAME]` | 0.883 [0.814, 0.941] | 0.865 [0.792, 0.929] | 0.874 [0.822, 0.920] | 83 | 11 | 13 | 96 |
| `[PHONE]` | 1.000 [1.000, 1.000] | 0.515 [0.397, 0.642] | 0.680 [0.568, 0.782] | 34 | 0 | 32 | 66 |
| `[STREET_ADDRESS]` | 0.679 [0.558, 0.803] | 0.757 [0.652, 0.852] | 0.716 [0.623, 0.795] | 53 | 25 | 17 | 70 |
| **macro** | 0.883 [0.848, 0.918] | 0.822 [0.786, 0.856] | 0.852 [0.823, 0.878] | 294 | 44 | 64 | 358 |
| **micro** | 0.870 [0.823, 0.911] | 0.821 [0.784, 0.856] | 0.845 [0.812, 0.874] | 294 | 44 | 64 | 358 |

### `multi_paragraph` (54 rows)

| Placeholder | Precision (95% CI) | Recall (95% CI) | F1 (95% CI) | TP | FP | FN | Support |
|---|---|---|---|---:|---:|---:|---:|
| `[DATE]` | 0.875 [0.750, 0.972] | 1.000 [1.000, 1.000] | 0.933 [0.857, 0.986] | 28 | 4 | 0 | 28 |
| `[EMAIL]` | 1.000 [1.000, 1.000] | 0.980 [0.933, 1.000] | 0.990 [0.966, 1.000] | 48 | 0 | 1 | 49 |
| `[PERSON_NAME]` | 0.913 [0.827, 0.985] | 0.778 [0.696, 0.859] | 0.840 [0.776, 0.897] | 63 | 6 | 18 | 81 |
| `[PHONE]` | 0.800 [0.632, 0.952] | 0.432 [0.270, 0.594] | 0.561 [0.391, 0.706] | 16 | 4 | 21 | 37 |
| `[STREET_ADDRESS]` | 0.619 [0.451, 0.861] | 0.634 [0.475, 0.786] | 0.627 [0.500, 0.769] | 26 | 16 | 15 | 41 |
| **macro** | 0.841 [0.783, 0.909] | 0.765 [0.727, 0.806] | 0.801 [0.763, 0.843] | 181 | 30 | 55 | 236 |
| **micro** | 0.858 [0.786, 0.924] | 0.767 [0.722, 0.814] | 0.810 [0.766, 0.852] | 181 | 30 | 55 | 236 |

### `structured` (142 rows)

| Placeholder | Precision (95% CI) | Recall (95% CI) | F1 (95% CI) | TP | FP | FN | Support |
|---|---|---|---|---:|---:|---:|---:|
| `[DATE]` | 0.935 [0.881, 0.985] | 1.000 [1.000, 1.000] | 0.966 [0.937, 0.993] | 72 | 5 | 0 | 72 |
| `[EMAIL]` | 0.990 [0.968, 1.000] | 0.962 [0.922, 0.991] | 0.976 [0.953, 0.995] | 102 | 1 | 4 | 106 |
| `[PERSON_NAME]` | 0.951 [0.901, 0.992] | 0.834 [0.756, 0.904] | 0.889 [0.838, 0.933] | 136 | 7 | 27 | 163 |
| `[PHONE]` | 0.885 [0.810, 0.955] | 0.635 [0.531, 0.734] | 0.740 [0.656, 0.813] | 54 | 7 | 31 | 85 |
| `[STREET_ADDRESS]` | 0.844 [0.768, 0.914] | 0.809 [0.722, 0.884] | 0.826 [0.761, 0.877] | 76 | 14 | 18 | 94 |
| **macro** | 0.921 [0.894, 0.946] | 0.848 [0.818, 0.878] | 0.883 [0.861, 0.905] | 440 | 34 | 80 | 520 |
| **micro** | 0.928 [0.901, 0.952] | 0.846 [0.813, 0.877] | 0.885 [0.862, 0.907] | 440 | 34 | 80 | 520 |


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
- `ai4p-de-20694924` [opf] value=`+54-685227296`  context: ...'ta.com oder telefonisch unter +54-685227296 zur Verfügung. Wir freuen uns'...
- `ai4p-de-20694966` [opf] value=`Frau Müller`  context: ...'n.\nFür Rückfragen steht Ihnen Frau Müller unter +43.110.380-4965 zur Ve'...
- `ai4p-de-20695083` [opf] value=`13187007`  context: ...'mit der Personalausweisnummer 13187007 abgeglichen.'...
- `ai4p-de-20695085` [opf] value=`Di Santi`  context: ...'Meist Zemir This Di Santi Ureath Ben Younes hat in eine'...
- `ai4p-de-20695085` [opf] value=`Ben Younes`  context: ...'st Zemir This Di Santi Ureath Ben Younes hat in einer Projekt‑Update‑M'...

### `[PHONE]`
- `ai4p-de-20694958` [regex] value=`0901 700729
12`  context: ...'. Sozialversicherungs‑Nummer: 0901 700729\n12. Steuer‑Identifikationsnummer'...
- `ai4p-de-20695082` [regex] value=`0331 620902`  context: ...'ine Sozialversicherungsnummer 0331 620902 an, während das System seine '...
- `ai4p-de-20695249` [regex] value=`0432 570801`  context: ...'FW\nSozialversicherungsnummer: 0432 570801\nSteuer‑Identifikationsnummer:'...
- `ai4p-de-20695439` [regex] value=`0404 031110`  context: ...'ogene Daten nur im Rahmen von 0404 031110 nutzen)\n\nBitte bis zum 3. Mai'...
- `ai4p-de-20695690` [regex] value=`0652 370604`  context: ...'. Sozialversicherungs‑Nummer: 0652 370604\n9. Steuer‑Identifikationsnumm'...

### `[STREET_ADDRESS]`
- `ai4p-de-20694945` [opf] value=`6020 Linz`  context: ...' Buffo Kottler\nSandgasse 1437\n6020 Linz\nE‑Mail: LI@hotmail.com\nTelefo'...
- `ai4p-de-20694966` [opf] value=`Mai/14`  context: ...'berto Hames,\nIhr Geburtsdatum Mai/14 und Ihr Alter von 3 Jahren wu'...
- `ai4p-de-20694991` [opf] value=`letzte 4 Ziffern`  context: ...'ss‑Nr.: E7076823\nKreditkarte (letzte 4 Ziffern): 630485508963\n\nBitte senden '...
- `ai4p-de-20695012` [opf] value=`Barrierefreiheit`  context: ...' und wir diskutieren, wie wir Barrierefreiheit in das neue Rollenspiel integ'...
- `ai4p-de-20695076` [opf] value=`November 8., 1956 in Innsbruck Pradl Pradl`  context: ...'nota.com. Der Kurs beginnt am November 8., 1956 in Innsbruck Pradl Pradl und wird in der Cäcilia-Kappe'...


## False-negative samples

### `[EMAIL]`
- `ai4p-de-20694974` value=`noëdoggweiler@yahoo.com`  context: ...'tsidentität: Bigender\nE‑Mail: noëdoggweiler@yahoo.com\nTelefon: (66) 6903 1936\n\nGewü'...
- `ai4p-de-20695275` value=`guizoppè@gmail.com`  context: ...'ren Sie uns bitte per E‑Mail (guizoppè@gmail.com) oder Telefon (0042-13 158 04'...
- `ai4p-de-20695432` value=`çinarrowan@hotmail.com`  context: ...'e Ansprechpartner per E‑Mail (çinarrowan@hotmail.com) und Telefon (+78.63887-6542)'...
- `ai4p-de-20695554` value=`maliilühmann@yahoo.com`  context: ...'burtsdatum: Mai/61\n5. E‑Mail: maliilühmann@yahoo.com\n6. Telefon: +435 38.964-3663\n'...
- `ai4p-de-20695871` value=`tomysodré@gmail.com`  context: ...' Sie Ihre Bewerbung inklusive tomysodré@gmail.com und +84 26874 5996 bis zum 11'...

### `[PERSON_NAME]`
- `ai4p-de-20694945` value=`Maria-Rosa Mielsch`  context: ...'ben.\nMit freundlichen Grüßen,\nMaria-Rosa Mielsch\nInhaberin Bone‑and‑Shell‑Desi'...
- `ai4p-de-20694956` value=`Huba Tardio Giussani`  context: ...'einem Alter von 2 Jahren weiß Huba Tardio Giussani, dass jede Szene ein Rätsel i'...
- `ai4p-de-20694963` value=`Maryléne Gossen Alosius Gyárfás`  context: ...'llen“, bevor die Unterschrift Maryléne Gossen Alosius Gyárfás – begleitet von einem Datum M'...
- `ai4p-de-20694969` value=`Heejin Tanoa`  context: ...'l erstellt, das die Daten von Heejin Tanoa enthält, inklusive Passnummer'...
- `ai4p-de-20694987` value=`Tatana Alikhashkin`  context: ...'Von: Doktorin Tatana Alikhashkin\\nDatum: 01/05/1989\\nBetreff: '...

### `[PHONE]`
- `ai4p-de-20694924` value=`+54-685227296`  context: ...'ta.com oder telefonisch unter +54-685227296 zur Verfügung. Wir freuen uns'...
- `ai4p-de-20694943` value=`+878.63.973.9334`  context: ...'‑Mail: M@hotmail.com\nTelefon: +878.63.973.9334\nPersonalausweis‑Nr.: 84394318'...
- `ai4p-de-20694954` value=`009929046 2990`  context: ...'C7977252. Ein kurzer Anruf an 009929046 2990 bestätigt, dass das Set im al'...
- `ai4p-de-20694958` value=`+20-459.555.0277`  context: ...'otmail.com\n7. Telefonkontakt: +20-459.555.0277\n8. Anschrift: Bahnhofstraße 1'...
- `ai4p-de-20694974` value=`(66) 6903 1936`  context: ...'doggweiler@yahoo.com\nTelefon: (66) 6903 1936\n\nGewünschte Ausrüstung:\n- Kam'...

### `[STREET_ADDRESS]`
- `ai4p-de-20694920` value=`Goethestraße 315, 1090 Wien Wieden`  context: ...'n Sie Ihre neue Anschrift an: Goethestraße 315, 1090 Wien Wieden.'...
- `ai4p-de-20694923` value=`Bertha-von-Suttner-Weg 3E in Klagenfurt am Wörthersee`  context: ...'neigenes Fitnessstudio in der Bertha-von-Suttner-Weg 3E in Klagenfurt am Wörthersee an. Mitarbeiter, die das Ange'...
- `ai4p-de-20695015` value=`4020`  context: ...'schließlich (336).7147153 und 4020, damit Support‑Teams weltweit'...
- `ai4p-de-20695061` value=`Wien KG Oberdöbling KG Oberdöbling (Postleitzahl: 6020`  context: ...' unserem Forschungszentrum in Wien KG Oberdöbling KG Oberdöbling (Postleitzahl: 6020). Dort wird ein detaillierter'...
- `ai4p-de-20695091` value=`Klagenfurt am Wörthersee (Postleitzahl 6020`  context: ...' am Dezember/60 in der Region Klagenfurt am Wörthersee (Postleitzahl 6020) gebeten, sowie um die Zusend'...

