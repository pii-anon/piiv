# ai4privacy (de) - dataset audit

Rows analyzed: **5,000**

Total spans: **38,084**

## Length distributions

### Text length (characters)

| min | p25 | p50 | p75 | p95 | max | mean |
|---|---|---|---|---|---|---|
| 60.0 | 220.0 | 352.5 | 539.0 | 912.1 | 1200.0 | 410.7 |

### Text length (whitespace tokens)

| min | p25 | p50 | p75 | p95 | max | mean |
|---|---|---|---|---|---|---|
| 7.0 | 29.0 | 45.0 | 69.0 | 114.0 | 168.0 | 52.6 |

### Spans per row

| min | p25 | p50 | p75 | p95 | max | mean |
|---|---|---|---|---|---|---|
| 1.0 | 4.0 | 7.0 | 10.0 | 17.0 | 30.0 | 7.6 |

### Span length (characters)

| min | p25 | p50 | p75 | p95 | max | mean |
|---|---|---|---|---|---|---|
| 1.0 | 6.0 | 10.0 | 14.0 | 20.0 | 70.0 | 10.3 |

## Label distribution

| Label | Count | % of spans | Example value |
|---|---:|---:|---|
| `DATE` | 4687 | 12.31 | Mai/04 |
| `GIVENNAME` | 4407 | 11.57 | Jadranka |
| `SURNAME` | 3875 | 10.17 | Landhou Enevoldsen Sekat |
| `EMAIL` | 2731 | 7.17 | SHV@tutanota.com |
| `CITY` | 2611 | 6.86 | Wien Wieden |
| `TITLE` | 2069 | 5.43 | Doktorin |
| `TELEPHONENUM` | 2039 | 5.35 | +54-685227296 |
| `AGE` | 1866 | 4.90 | 22 |
| `STREET` | 1832 | 4.81 | Goethestraße |
| `BUILDINGNUM` | 1798 | 4.72 | 315 |
| `ZIPCODE` | 1664 | 4.37 | 1090 |
| `CREDITCARDNUMBER` | 1263 | 3.32 | 2200906163294476 |
| `GENDER` | 1174 | 3.08 | Androgyn |
| `TAXNUM` | 1165 | 3.06 | 79-1853093 |
| `DRIVERLICENSENUM` | 1064 | 2.79 | UVX174QMWB |
| `IDCARDNUM` | 1033 | 2.71 | 03690080 |
| `SOCIALNUM` | 1021 | 2.68 | 6894 510103 |
| `SEX` | 1000 | 2.63 | M |
| `PASSPORTNUM` | 785 | 2.06 | M0839164 |

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

**id**: `ai4p-de-20701055`  •  **spans**: 30

```
Protokoll – Szenario‑Planungs‑Meeting (Leadership)\n\nDatum: März/90\nUhrzeit: 10:30 – 12:00 Uhr\nOrt: Sitzungszimmer 1191 Am Bindermichl, 6020 Graz\n\nTeilnehmer:\n- Sen Umida Nela Doniselli (Alter: 24, Geschlecht: Bigender)\n- Sen Ushanthan Atacer (Geburtsdatum: 1. September 1976)\n- Frau Vetime Haufgartner (Steuernr.: 80-4558839)\n\nKurzfassung der diskutierten Szenarien:\n1. Marktvolatilität – Auswirku...
```

  - `DATE` [59:66] = `März/90`
  - `BUILDINGNUM` [114:118] = `1191`
  - `STREET` [119:133] = `Am Bindermichl`
  - `ZIPCODE` [135:139] = `6020`
  - `CITY` [140:144] = `Graz`
  - `TITLE` [160:163] = `Sen`
  - `GIVENNAME` [164:169] = `Umida`
  - `SURNAME` [170:184] = `Nela Doniselli`
  - `AGE` [193:195] = `24`
  - `GENDER` [209:217] = `Bigender`
  - `TITLE` [221:224] = `Sen`
  - `GIVENNAME` [225:234] = `Ushanthan`
  - `SURNAME` [235:241] = `Atacer`
  - `DATE` [257:274] = `1. September 1976`
  - `TITLE` [278:282] = `Frau`
  - `GIVENNAME` [283:289] = `Vetime`
  - `SURNAME` [290:301] = `Haufgartner`
  - `TAXNUM` [314:324] = `80-4558839`
  - `GIVENNAME` [446:452] = `Avdush`
  - `SURNAME` [453:460] = `Schiele`
  - ... and 10 more spans

## Random samples

**id**: `ai4p-de-20694919`  •  **spans**: 4

```
Die erweiterte Gehaltsstruktur berücksichtigt das Alter Ihrer Karriere, wobei Mitarbeiter über 22 Jahren ein zusätzliches Dienstalterbonus erhalten. Ihre Sozialversicherungsnummer 6894 510103 wird für die Berechnung der Beiträge benötigt. Falls sich Ihre Familienstand verändert hat, teilen Sie uns bitte Ihr Geschlecht Androgyn und Ihren Familienstand mit, um mögliche Steuervergünstigungen zu pr...
```

  - `AGE` [95:97] = `22`
  - `SOCIALNUM` [180:191] = `6894 510103`
  - `GENDER` [320:328] = `Androgyn`
  - `DATE` [436:442] = `Mai/04`

**id**: `ai4p-de-20695279`  •  **spans**: 7

```
Hallo Raveendran, ich habe gerade meinen Reisepass (J5646652) und meinen Führerschein (B2FT05S51A) überprüft; beide sind noch gültig. Als 0-jähriger Zwei-Geister mit großem Interesse an historischen Flugzeugen freue ich mich besonders auf den Rundflug über die Alpen. Könntest du bitte meine Steueridentifikationsnummer 55-9155006 für die Buchungsunterlagen ergänzen und mir die finale Rechnung an...
```

  - `GIVENNAME` [6:16] = `Raveendran`
  - `PASSPORTNUM` [52:60] = `J5646652`
  - `DRIVERLICENSENUM` [87:97] = `B2FT05S51A`
  - `AGE` [138:139] = `0`
  - `GENDER` [149:161] = `Zwei-Geister`
  - `TAXNUM` [320:330] = `55-9155006`
  - `EMAIL` [398:412] = `M@tutanota.com`

**id**: `ai4p-de-20695622`  •  **spans**: 6

```
Ich, Punit Li La Valle, wurde am 14/02/1959 geboren und bin derzeit 27 Jahre alt. Die Workshops haben mein Verständnis für die unterschiedlichen Kulturen in unserem Unternehmen erheblich erweitert, insbesondere durch den Austausch mit Kolleginnen aus Wien Wieden und Wien Innere Stadt. Ich empfehle allen, die ihre interkulturelle Kompetenz stärken wollen, an den Sitzungen teilzunehmen.
```

  - `GIVENNAME` [5:13] = `Punit Li`
  - `SURNAME` [14:22] = `La Valle`
  - `DATE` [33:43] = `14/02/1959`
  - `AGE` [68:70] = `27`
  - `CITY` [251:262] = `Wien Wieden`
  - `CITY` [267:284] = `Wien Innere Stadt`

**id**: `ai4p-de-20695974`  •  **spans**: 8

```
Liebe Origami‑Enthusiasten, wir laden Sie herzlich ein, am wöchentlichen Origami‑Challenge‑Treffen teilzunehmen, das am 29/11/1989 im Raum 84 Pachmayrstraße in Graz Lend stattfindet. Bitte bestätigen Sie Ihre Teilnahme per E‑Mail an TS@gmail.com oder telefonisch unter +43 188.974.9168, damit wir die Teilnehmerzahlen planen können. Falls Sie spezielle Bedürfnisse haben, teilen Sie uns bitte Ihr ...
```

  - `DATE` [120:130] = `29/11/1989`
  - `BUILDINGNUM` [139:141] = `84`
  - `STREET` [142:156] = `Pachmayrstraße`
  - `CITY` [160:169] = `Graz Lend`
  - `EMAIL` [233:245] = `TS@gmail.com`
  - `TELEPHONENUM` [269:285] = `+43 188.974.9168`
  - `GENDER` [409:417] = `Bigender`
  - `AGE` [430:432] = `27`

**id**: `ai4p-de-20696327`  •  **spans**: 12

```
Sehr geehrte(r) Doktorin Dhikra Arquint, wir konnten Ihre Patientenidentifikation am Februar/62 nicht verifizieren, weil das angegebene Geburtsdatum (13. August 1978), Alter (61) und Geschlecht (Männlich) nicht mit den bei uns hinterlegten Daten übereinstimmen. Zusätzlich fehlt ein gültiger Ausweis (88115853) sowie ein aktueller Führerschein (OVA0Y0M3IQ) und Ihre Sozialversicherungsnummer (4912...
```

  - `TITLE` [16:24] = `Doktorin`
  - `GIVENNAME` [25:31] = `Dhikra`
  - `SURNAME` [32:39] = `Arquint`
  - `DATE` [85:95] = `Februar/62`
  - `DATE` [150:165] = `13. August 1978`
  - `AGE` [175:177] = `61`
  - `SEX` [195:203] = `Männlich`
  - `IDCARDNUM` [301:309] = `88115853`
  - `DRIVERLICENSENUM` [345:355] = `OVA0Y0M3IQ`
  - `SOCIALNUM` [393:404] = `4912 100303`
  - `EMAIL` [473:486] = `S@hotmail.com`
  - `TELEPHONENUM` [512:525] = `+4311273.6786`

