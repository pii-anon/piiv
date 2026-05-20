## `combine_names` - attrition

- Rows in: **5,000**
- Rows out: **3,831** (76.6% survival)
- Dropped, only-one-kind (had GIVENNAME xor SURNAME): **604**
- Dropped, unpaired/separated names: **565**
- PERSON_NAME pairs merged: **2,906**

## `keep_only_allowed` - attrition

- Allowlist for this dataset: `BUILDINGNUM`, `CITY`, `CREDITCARDNUMBER`, `DATE`, `EMAIL`, `GIVENNAME`, `IDCARDNUM`, `PASSPORTNUM`, `PERSON_NAME`, `STREET`, `SURNAME`, `TAXNUM`, `TELEPHONENUM`, `ZIPCODE`
- Rows in: **3,831**
- Rows out: **961** (25.1% survival)
- Rows dropped: **2,870**
- Dropped because of out-of-allowlist label: `TITLE`=1386, `AGE`=1334, `GENDER`=869, `DRIVERLICENSENUM`=786, `SOCIALNUM`=758, `SEX`=724

# ai4privacy (de) - dataset audit

Rows analyzed: **961**

Total spans: **3,602**

## Length distributions

### Text length (characters)

| min | p25 | p50 | p75 | p95 | max | mean |
|---|---|---|---|---|---|---|
| 62.0 | 161.0 | 218.0 | 321.0 | 539.0 | 1091.0 | 258.7 |

### Text length (whitespace tokens)

| min | p25 | p50 | p75 | p95 | max | mean |
|---|---|---|---|---|---|---|
| 7.0 | 21.0 | 29.0 | 42.0 | 73.0 | 141.0 | 33.8 |

### Spans per row

| min | p25 | p50 | p75 | p95 | max | mean |
|---|---|---|---|---|---|---|
| 1.0 | 2.0 | 3.0 | 5.0 | 8.0 | 13.0 | 3.7 |

### Span length (characters)

| min | p25 | p50 | p75 | p95 | max | mean |
|---|---|---|---|---|---|---|
| 1.0 | 8.0 | 13.0 | 16.0 | 24.0 | 70.0 | 12.7 |

## Label distribution

| Label | Count | % of spans | Example value |
|---|---:|---:|---|
| `DATE` | 573 | 15.91 | März 15., 1980 |
| `PERSON_NAME` | 399 | 11.08 | Alpay Solorzano |
| `EMAIL` | 384 | 10.66 | SHV@tutanota.com |
| `CITY` | 372 | 10.33 | Wien Wieden |
| `TELEPHONENUM` | 311 | 8.63 | +54-685227296 |
| `STREET` | 299 | 8.30 | Goethestraße |
| `BUILDINGNUM` | 294 | 8.16 | 315 |
| `CREDITCARDNUMBER` | 270 | 7.50 | 2200906163294476 |
| `ZIPCODE` | 263 | 7.30 | 1090 |
| `TAXNUM` | 153 | 4.25 | 79-1853093 |
| `IDCARDNUM` | 149 | 4.14 | 18292463 |
| `PASSPORTNUM` | 135 | 3.75 | E9375947 |

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

**id**: `ai4p-de-20697090`  •  **spans**: 13

```
Liebe Weinliebhaberinnen und -liebhaber,\nIhr persönlicher Reiseführer Nana François-Louis Joldic hat für Sie ein maßgeschneidertes Programm vom 25/08/1955 bis zum Juli 10., 1967 in der malerischen Region Salzburg Salzburg-Süd Salzburg-Süd zusammengestellt.\nDie erste Etappe führt Sie zum Weingut an der Treppelweg 1, 8020 Wien KG Leopoldstadt, wo Sie an einer exklusiven Verkostung von Riesling un...
```

  - `PERSON_NAME` [70:96] = `Nana François-Louis Joldic`
  - `DATE` [144:154] = `25/08/1955`
  - `DATE` [163:177] = `Juli 10., 1967`
  - `CITY` [204:238] = `Salzburg Salzburg-Süd Salzburg-Süd`
  - `STREET` [303:313] = `Treppelweg`
  - `BUILDINGNUM` [314:315] = `1`
  - `ZIPCODE` [317:321] = `8020`
  - `CITY` [322:342] = `Wien KG Leopoldstadt`
  - `STREET` [506:520] = `Industriezeile`
  - `BUILDINGNUM` [521:523] = `41`
  - `EMAIL` [639:653] = `AN14@yahoo.com`
  - `TELEPHONENUM` [677:691] = `+41-32215.7306`
  - `DATE` [724:740] = `Februar 3., 2000`

## Random samples

**id**: `ai4p-de-20694920`  •  **spans**: 5

```
Für die Steuererklärung benötigen wir Ihre Steueridentifikationsnummer 79-1853093 und Ihre aktuelle Adresse. Bitte geben Sie Ihre neue Anschrift an: Goethestraße 315, 1090 Wien Wieden.
```

  - `TAXNUM` [71:81] = `79-1853093`
  - `STREET` [149:161] = `Goethestraße`
  - `BUILDINGNUM` [162:165] = `315`
  - `ZIPCODE` [167:171] = `1090`
  - `CITY` [172:183] = `Wien Wieden`

**id**: `ai4p-de-20696623`  •  **spans**: 2

```
Die Rechnung für den Spa‑Besuch wird an E@outlook.com gesendet, die Gesamtkosten betragen 75 € plus 10 € für das Reisekennzeichen, das Sie unter 4020 erhalten.
```

  - `EMAIL` [40:53] = `E@outlook.com`
  - `ZIPCODE` [145:149] = `4020`

**id**: `ai4p-de-20698544`  •  **spans**: 3

```
Für die Teilnahme ist ein gültiger 18011460 oder V2301510 erforderlich, und die Eltern sollten das Einverständnisformular mit ihrer Unterschrift bis zum September/79 zurücksenden.
```

  - `IDCARDNUM` [35:43] = `18011460`
  - `PASSPORTNUM` [49:57] = `V2301510`
  - `DATE` [153:165] = `September/79`

**id**: `ai4p-de-20700375`  •  **spans**: 3

```
Abschließend bedanken wir uns für das Vertrauen, das Sie in Interim Leadership Solutions setzen. Wir werden die eingereichten Unterlagen prüfen und uns bis spätestens 23/07/1965 mit einem finalen Angebot bei Ihnen melden. Bei Fragen wenden Sie sich bitte an Simen Nergim Niemelä unter der E‑Mail H@outlook.com.
```

  - `DATE` [167:177] = `23/07/1965`
  - `PERSON_NAME` [258:278] = `Simen Nergim Niemelä`
  - `EMAIL` [296:309] = `H@outlook.com`

**id**: `ai4p-de-20702259`  •  **spans**: 5

```
Social‑Media‑Post:\n🌊🚶‍♀️ Neue Flussufer‑ und Seepfad‑Routen ab sofort begehbar! 📍 Startpunkt: Zusertalgasse 15 in Wien Neubau Neubau.\nTeilnehmerzahl begrenzt – melde dich jetzt an unter ilaripestre@yahoo.com oder ruf an: +43.12-037.2315.
```

  - `STREET` [94:107] = `Zusertalgasse`
  - `BUILDINGNUM` [108:110] = `15`
  - `CITY` [114:132] = `Wien Neubau Neubau`
  - `EMAIL` [186:207] = `ilaripestre@yahoo.com`
  - `TELEPHONENUM` [221:236] = `+43.12-037.2315`

