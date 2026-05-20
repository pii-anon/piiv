## `combine_names` transform - attrition

- Rows in: **5,000**
- Rows out: **3,831** (76.6% survival)
- Dropped, only-one-kind (had GIVENNAME xor SURNAME): **604**
- Dropped, unpaired/separated names: **565**
- PERSON_NAME pairs merged: **2,906**

# ai4privacy (de) - dataset audit

Rows analyzed: **3,831**

Total spans: **25,232**

## Length distributions

### Text length (characters)

| min | p25 | p50 | p75 | p95 | max | mean |
|---|---|---|---|---|---|---|
| 60.0 | 212.0 | 342.0 | 521.0 | 867.5 | 1198.0 | 397.5 |

### Text length (whitespace tokens)

| min | p25 | p50 | p75 | p95 | max | mean |
|---|---|---|---|---|---|---|
| 7.0 | 27.0 | 44.0 | 66.0 | 110.0 | 168.0 | 50.8 |

### Spans per row

| min | p25 | p50 | p75 | p95 | max | mean |
|---|---|---|---|---|---|---|
| 1.0 | 3.0 | 6.0 | 9.0 | 14.0 | 25.0 | 6.6 |

### Span length (characters)

| min | p25 | p50 | p75 | p95 | max | mean |
|---|---|---|---|---|---|---|
| 1.0 | 7.0 | 11.0 | 16.0 | 24.0 | 70.0 | 11.6 |

## Label distribution

| Label | Count | % of spans | Example value |
|---|---:|---:|---|
| `DATE` | 3509 | 13.91 | Mai/04 |
| `PERSON_NAME` | 2906 | 11.52 | Jadranka Landhou Enevoldsen Sekat |
| `CITY` | 1998 | 7.92 | Wien Wieden |
| `EMAIL` | 1996 | 7.91 | SHV@tutanota.com |
| `TELEPHONENUM` | 1509 | 5.98 | +54-685227296 |
| `TITLE` | 1505 | 5.96 | Doktorin |
| `AGE` | 1409 | 5.58 | 22 |
| `STREET` | 1384 | 5.49 | Goethestraße |
| `BUILDINGNUM` | 1360 | 5.39 | 315 |
| `ZIPCODE` | 1274 | 5.05 | 1090 |
| `CREDITCARDNUMBER` | 955 | 3.78 | 2200906163294476 |
| `TAXNUM` | 893 | 3.54 | 79-1853093 |
| `GENDER` | 873 | 3.46 | Androgyn |
| `DRIVERLICENSENUM` | 792 | 3.14 | UVX174QMWB |
| `IDCARDNUM` | 785 | 3.11 | 18292463 |
| `SOCIALNUM` | 758 | 3.00 | 6894 510103 |
| `SEX` | 740 | 2.93 | O |
| `PASSPORTNUM` | 586 | 2.32 | E9375947 |

## Span-level quality checks

| Check | Rows | % of rows | Notes |
|---|---:|---:|---|
| Rows with **zero spans** | 0 | 0.00% | Unusable for recall measurement |
| Rows with **value/text mismatch** | 0 | 0.00% | `text[start:end] != value` (0 bad spans) |
| Rows with **out-of-bounds spans** | 0 | 0.00% | Offsets exceed text length (0 bad spans) |
| Rows with **overlapping spans** | 0 | 0.00% | 0 overlap pairs total |
| Rows with **dropped spans at load** | 0 | 0.00% | Span dict missing required fields |
| Rows with **non-NFC text** | 0 | 0.00% | Inconsistent unicode normalization |
| Rows with **control characters** | 0 | 0.00% | Non-whitespace Cc category |

## Flagged examples (one per failure mode)

### `max_spans`

**id**: `ai4p-de-20701570`  •  **spans**: 25

```
Baugesuch – Antrag auf Baugenehmigung\n\nProjektbezeichnung: **Flood‑Defensive Architectural Study – Modellhaus „AquaShield“**\nBauort: Bahnhofstraße 51, 8010 Linz Rathausviertel\nBauherr: Prof Léonard Kiso Rollón\nGeburtsdatum: 1947-08-10T00:00:00\nAlter: 22\nGeschlecht: O / Geschlechtsidentität: Androgyn\nPersonalausweis‑Nr.: 15412560\nFührerschein‑Nr.: DLK54KZ18M\nSteuernummer: 76-1238249\nSozialversic...
```

  - `STREET` [133:146] = `Bahnhofstraße`
  - `BUILDINGNUM` [147:149] = `51`
  - `ZIPCODE` [151:155] = `8010`
  - `CITY` [156:175] = `Linz Rathausviertel`
  - `TITLE` [185:189] = `Prof`
  - `PERSON_NAME` [190:209] = `Léonard Kiso Rollón`
  - `DATE` [224:243] = `1947-08-10T00:00:00`
  - `AGE` [251:253] = `22`
  - `SEX` [266:267] = `O`
  - `GENDER` [292:300] = `Androgyn`
  - `IDCARDNUM` [322:330] = `15412560`
  - `DRIVERLICENSENUM` [349:359] = `DLK54KZ18M`
  - `TAXNUM` [374:384] = `76-1238249`
  - `SOCIALNUM` [410:421] = `3564 080709`
  - `EMAIL` [430:443] = `D1994@aol.com`
  - `TELEPHONENUM` [453:470] = `0143-575 892 7187`
  - `DATE` [697:714] = `24. Dezember 2014`
  - `DRIVERLICENSENUM` [944:954] = `XVLXZ5SFCA`
  - `DATE` [1044:1060] = `8. Dezember 1966`
  - `TITLE` [1088:1096] = `Doktorin`
  - ... and 5 more spans

## Random samples

**id**: `ai4p-de-20694919`  •  **spans**: 4

```
Die erweiterte Gehaltsstruktur berücksichtigt das Alter Ihrer Karriere, wobei Mitarbeiter über 22 Jahren ein zusätzliches Dienstalterbonus erhalten. Ihre Sozialversicherungsnummer 6894 510103 wird für die Berechnung der Beiträge benötigt. Falls sich Ihre Familienstand verändert hat, teilen Sie uns bitte Ihr Geschlecht Androgyn und Ihren Familienstand mit, um mögliche Steuervergünstigungen zu pr...
```

  - `AGE` [95:97] = `22`
  - `SOCIALNUM` [180:191] = `6894 510103`
  - `GENDER` [320:328] = `Androgyn`
  - `DATE` [436:442] = `Mai/04`

**id**: `ai4p-de-20695375`  •  **spans**: 6

```
Der abschließende Abschnitt ehrt das Andenken an Manoja Emrulahu Kashai, dessen Geschichte in den vergilbten Seiten einer Chronik weiterlebt; ihr 22/09/2004 wird in goldenen Lettern geschrieben, während ihr 61‑jähriges Vermächtnis immer noch in den Herzen derer pulsiert, die sie kannten. Der Klang von +43-12.101.3054 schwingt leise im Hintergrund, ein letztes Signal, das durch die Zeit dringt, ...
```

  - `PERSON_NAME` [49:71] = `Manoja Emrulahu Kashai`
  - `DATE` [146:156] = `22/09/2004`
  - `AGE` [207:209] = `61`
  - `TELEPHONENUM` [303:318] = `+43-12.101.3054`
  - `EMAIL` [417:432] = `BIG@outlook.com`
  - `STREET` [524:542] = `Hermannstädter Weg`

**id**: `ai4p-de-20695820`  •  **spans**: 4

```
Laut einer Studie von Toan Bawart (geb. am 2006-01-22T00:00:00) erhöht das wöchentliche Reflektieren über den eigenen Agender-Zustand das emotionale Gleichgewicht, besonders wenn man dabei die aktuelle 28‑Jahreszeit berücksichtigt.
```

  - `PERSON_NAME` [22:33] = `Toan Bawart`
  - `DATE` [43:62] = `2006-01-22T00:00:00`
  - `GENDER` [118:125] = `Agender`
  - `AGE` [202:204] = `28`

**id**: `ai4p-de-20696273`  •  **spans**: 3

```
Eine aktuelle Umfrage unter Forschern (geschrieben von Vasilka Bentaleb Grizi Piatek, Geschlecht: Nicht spezifiziert) betont die Bedeutung von Langzeitdaten, die im Zirl‑Archiv gespeichert sind.
```

  - `PERSON_NAME` [55:84] = `Vasilka Bentaleb Grizi Piatek`
  - `GENDER` [98:116] = `Nicht spezifiziert`
  - `CITY` [165:169] = `Zirl`

**id**: `ai4p-de-20696687`  •  **spans**: 12

```
Audit‑Checkliste (Kurzfassung)\n\n1. Rollen‑Beschreibung: ___________________________\n2. Verantwortungsbereich: ___________________________\n3. Aktuelle 29 Jahre Berufserfahrung: __________\n4. Geschlecht/Biologisches Weiblich: __________\n5. Wohnort: Rockhgasse 1341, 8041 Salzburg Schallmoos\n6. Identifikatoren:\n   - Personalausweis: 02492364\n   - Führerschein: UM2589D95I\n   - Sozialversicherungs‑Nr...
```

  - `AGE` [150:152] = `29`
  - `SEX` [214:222] = `Weiblich`
  - `STREET` [247:257] = `Rockhgasse`
  - `BUILDINGNUM` [258:262] = `1341`
  - `ZIPCODE` [264:268] = `8041`
  - `CITY` [269:288] = `Salzburg Schallmoos`
  - `IDCARDNUM` [331:339] = `02492364`
  - `DRIVERLICENSENUM` [359:369] = `UM2589D95I`
  - `SOCIALNUM` [400:411] = `3728 720203`
  - `TAXNUM` [429:439] = `41-8601201`
  - `DATE` [469:479] = `31/01/1998`
  - `EMAIL` [514:535] = `agshaymoyer@gmail.com`

