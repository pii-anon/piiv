## `combine_names` - attrition

- Rows in: **5,000**
- Rows out: **3,940** (78.8% survival)
- Dropped, only-one-kind (had GIVENNAME xor SURNAME): **484**
- Dropped, unpaired/separated names: **576**
- PERSON_NAME pairs merged: **3,656**

## `keep_only_allowed` - attrition

- Allowlist for this dataset: `BUILDINGNUM`, `CITY`, `CREDITCARDNUMBER`, `DATE`, `EMAIL`, `GIVENNAME`, `PASSPORTNUM`, `PERSON_NAME`, `SOCIALNUM`, `STREET`, `SURNAME`, `TELEPHONENUM`, `ZIPCODE`
- Rows in: **3,940**
- Rows out: **569** (14.4% survival)
- Rows dropped: **3,371**
- Dropped because of out-of-allowlist label: `TITLE`=2047, `AGE`=1457, `DRIVERLICENSENUM`=988, `IDCARDNUM`=971, `GENDER`=915, `TAXNUM`=904, `SEX`=699

# ai4privacy (en) - dataset audit

Rows analyzed: **569**

Total spans: **2,284**

## Length distributions

### Text length (characters)

| min | p25 | p50 | p75 | p95 | max | mean |
|---|---|---|---|---|---|---|
| 57.0 | 154.0 | 217.0 | 325.0 | 589.4 | 1072.0 | 265.3 |

### Text length (whitespace tokens)

| min | p25 | p50 | p75 | p95 | max | mean |
|---|---|---|---|---|---|---|
| 5.0 | 24.0 | 33.0 | 49.0 | 85.6 | 155.0 | 39.5 |

### Spans per row

| min | p25 | p50 | p75 | p95 | max | mean |
|---|---|---|---|---|---|---|
| 1.0 | 2.0 | 4.0 | 5.0 | 8.0 | 12.0 | 4.0 |

### Span length (characters)

| min | p25 | p50 | p75 | p95 | max | mean |
|---|---|---|---|---|---|---|
| 1.0 | 9.0 | 13.0 | 16.0 | 23.0 | 44.0 | 12.7 |

## Label distribution

| Label | Count | % of spans | Example value |
|---|---:|---:|---|
| `DATE` | 372 | 16.29 | 26/10/2019 |
| `EMAIL` | 267 | 11.69 | LF@aol.com |
| `CITY` | 261 | 11.43 | Langton |
| `PERSON_NAME` | 257 | 11.25 | Ariona Naïa Jäissli |
| `TELEPHONENUM` | 231 | 10.11 | 0392.76019104 |
| `STREET` | 214 | 9.37 | Avenue Road |
| `BUILDINGNUM` | 206 | 9.02 | 133 |
| `ZIPCODE` | 182 | 7.97 | B0J |
| `CREDITCARDNUMBER` | 163 | 7.14 | 3888332920072600 |
| `SOCIALNUM` | 70 | 3.06 | 0342893022 |
| `PASSPORTNUM` | 61 | 2.67 | NH4661879 |

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

**id**: `ai4p-en-20902141`  •  **spans**: 12

```
Donation Receipt – Form A\nDate Issued: 28/08/1982\nDonor: Abit Milliner\nAddress: Book Road West 22224, Nominingue, T0M\nContact: 019572425.6704 | S@outlook.com\n\nThe charitable organization hereby acknowledges receipt of the following contribution:\n- Amount Donated: $6242798175794152 (masked for security)\n- Date of Donation: 22nd March 1942\n- Method of Payment: Credit Card ending in 50186333904320...
```

  - `DATE` [39:49] = `28/08/1982`
  - `PERSON_NAME` [57:70] = `Abit Milliner`
  - `STREET` [80:94] = `Book Road West`
  - `BUILDINGNUM` [95:100] = `22224`
  - `CITY` [102:112] = `Nominingue`
  - `ZIPCODE` [114:117] = `T0M`
  - `TELEPHONENUM` [127:141] = `019572425.6704`
  - `EMAIL` [144:157] = `S@outlook.com`
  - `CREDITCARDNUMBER` [265:281] = `6242798175794152`
  - `DATE` [324:339] = `22nd March 1942`
  - `CREDITCARDNUMBER` [383:402] = `5018633390432092718`
  - `TELEPHONENUM` [715:729] = `018196880.6880`

## Random samples

**id**: `ai4p-en-20902015`  •  **spans**: 2

```
We hope you found the recent meditation retreat at the Langton monastery enriching. As part of our continuous improvement, please share your feedback by replying to this message or contacting us at 0392.76019104. If you wish to join future retreats, let us know your preferred dates and any special accommodations you may require (e.g., dietary restrictions, accessibility needs). Thank you for yo...
```

  - `CITY` [55:62] = `Langton`
  - `TELEPHONENUM` [198:211] = `0392.76019104`

**id**: `ai4p-en-20904450`  •  **spans**: 4

```
To enhance compliance, we’ve partnered with a local pharmacy that will deliver your supplemental vitamins to 4th Line #813, Elkford – just confirm your delivery address and V7Z 1B5 via email.
```

  - `STREET` [109:117] = `4th Line`
  - `BUILDINGNUM` [119:122] = `813`
  - `CITY` [124:131] = `Elkford`
  - `ZIPCODE` [173:180] = `V7Z 1B5`

**id**: `ai4p-en-20907136`  •  **spans**: 5

```
Good morning Marinete Léonora Kom, as part of the Creative City Exploration program we have arranged a culinary tour that includes a reservation at the rooftop restaurant on Leeming Road (suite 731); the cost will be billed to the corporate card ending in 6212830968072184 and the receipt will be sent to your KS@hotmail.com.
```

  - `PERSON_NAME` [13:33] = `Marinete Léonora Kom`
  - `STREET` [174:186] = `Leeming Road`
  - `BUILDINGNUM` [194:197] = `731`
  - `CREDITCARDNUMBER` [256:272] = `6212830968072184`
  - `EMAIL` [310:324] = `KS@hotmail.com`

