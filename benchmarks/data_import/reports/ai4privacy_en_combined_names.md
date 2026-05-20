## `combine_names` transform - attrition

- Rows in: **5,000**
- Rows out: **3,940** (78.8% survival)
- Dropped, only-one-kind (had GIVENNAME xor SURNAME): **484**
- Dropped, unpaired/separated names: **576**
- PERSON_NAME pairs merged: **3,656**

# ai4privacy (en) - dataset audit

Rows analyzed: **3,940**

Total spans: **30,541**

## Length distributions

### Text length (characters)

| min | p25 | p50 | p75 | p95 | max | mean |
|---|---|---|---|---|---|---|
| 57.0 | 233.0 | 384.0 | 599.2 | 986.0 | 1200.0 | 445.5 |

### Text length (whitespace tokens)

| min | p25 | p50 | p75 | p95 | max | mean |
|---|---|---|---|---|---|---|
| 5.0 | 35.0 | 56.0 | 87.2 | 143.0 | 200.0 | 65.3 |

### Spans per row

| min | p25 | p50 | p75 | p95 | max | mean |
|---|---|---|---|---|---|---|
| 1.0 | 4.0 | 7.0 | 10.0 | 16.0 | 28.0 | 7.8 |

### Span length (characters)

| min | p25 | p50 | p75 | p95 | max | mean |
|---|---|---|---|---|---|---|
| 1.0 | 6.0 | 10.0 | 15.0 | 23.0 | 50.0 | 11.4 |

## Label distribution

| Label | Count | % of spans | Example value |
|---|---:|---:|---|
| `DATE` | 4078 | 13.35 | November 24th, 1959 |
| `PERSON_NAME` | 3656 | 11.97 | Dushyant Herta Wagen Thompson-McNicol |
| `EMAIL` | 2567 | 8.41 | 1959P@yahoo.com |
| `CITY` | 2405 | 7.87 | Vienna |
| `TITLE` | 2305 | 7.55 | Mr |
| `TELEPHONENUM` | 1912 | 6.26 | +36 774 580.0503 |
| `STREET` | 1727 | 5.65 | Mount Hope Road |
| `BUILDINGNUM` | 1668 | 5.46 | 703 |
| `ZIPCODE` | 1584 | 5.19 | V2P |
| `AGE` | 1574 | 5.15 | 60 |
| `CREDITCARDNUMBER` | 1022 | 3.35 | 60115140036341395 |
| `DRIVERLICENSENUM` | 993 | 3.25 | RRH1ZZBPCA |
| `IDCARDNUM` | 974 | 3.19 | BEKD82TLNP |
| `GENDER` | 938 | 3.07 | Female |
| `TAXNUM` | 905 | 2.96 | 4686135601 |
| `SOCIALNUM` | 835 | 2.73 | 2492368319 |
| `SEX` | 710 | 2.32 | O |
| `PASSPORTNUM` | 688 | 2.25 | IG1622654 |

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

**id**: `ai4p-en-20904643`  •  **spans**: 28

```
Master Thamiliniyan Santinelli\nModern Climbing Challenges – Registration Form\n\nDear Kélia Yin Intaglietta,\n\nThank you for your interest in our upcoming climbing event on 16th September 2003. To complete your registration, please provide the following details:\n\n1. Full Name: Master Aurika Ayoub Sieczewicz\n2. Date of Birth: 18th March 1998\n3. Age: 1\n4. Sex: Male\n5. Gender Identity: Agender\n6. Ema...
```

  - `TITLE` [0:6] = `Master`
  - `PERSON_NAME` [7:30] = `Thamiliniyan Santinelli`
  - `PERSON_NAME` [84:105] = `Kélia Yin Intaglietta`
  - `DATE` [170:189] = `16th September 2003`
  - `TITLE` [275:281] = `Master`
  - `PERSON_NAME` [282:305] = `Aurika Ayoub Sieczewicz`
  - `DATE` [324:339] = `18th March 1998`
  - `AGE` [348:349] = `1`
  - `SEX` [358:362] = `Male`
  - `GENDER` [383:390] = `Agender`
  - `EMAIL` [409:425] = `L@protonmail.com`
  - `TELEPHONENUM` [443:459] = `0000-47-350-5404`
  - `BUILDINGNUM` [484:486] = `41`
  - `STREET` [487:500] = `Grid Road 744`
  - `CITY` [502:510] = `Bluffton`
  - `ZIPCODE` [512:519] = `T0C 1L0`
  - `DRIVERLICENSENUM` [563:573] = `I9QR4QZ91Z`
  - `IDCARDNUM` [603:613] = `BTQM1P6LDU`
  - `SOCIALNUM` [642:652] = `3084460004`
  - `TAXNUM` [684:694] = `8089897283`
  - ... and 8 more spans

## Random samples

**id**: `ai4p-en-20901966`  •  **spans**: 16

```
Mr Dushyant Herta Wagen Thompson-McNicol,\n\nWe are delighted to inform you that a new series of volunteer programmes targeting retirees has been launched in Vienna, and we believe your experience and passion would be a perfect match. As a seasoned professional aged 60 with a background in Female community service, you are invited to join the "Silver Mentors" initiative, which pairs seasoned volu...
```

  - `TITLE` [0:2] = `Mr`
  - `PERSON_NAME` [3:40] = `Dushyant Herta Wagen Thompson-McNicol`
  - `CITY` [156:162] = `Vienna`
  - `AGE` [265:267] = `60`
  - `GENDER` [289:295] = `Female`
  - `STREET` [448:463] = `Mount Hope Road`
  - `BUILDINGNUM` [479:482] = `703`
  - `IDCARDNUM` [579:589] = `BEKD82TLNP`
  - `DRIVERLICENSENUM` [625:635] = `RRH1ZZBPCA`
  - `EMAIL` [658:673] = `1959P@yahoo.com`
  - `TELEPHONENUM` [688:704] = `+36 774 580.0503`
  - `DATE` [735:754] = `November 24th, 1959`
  - `DATE` [947:964] = `27th January 1990`
  - `PERSON_NAME` [1031:1044] = `Zimrije Niemz`
  - `ZIPCODE` [1073:1076] = `V2P`
  - `CITY` [1077:1086] = `Thorndale`

**id**: `ai4p-en-20902380`  •  **spans**: 18

```
Change Management Procedure Overview\n\n1. Initiation: The change request must be submitted by Mstr Djihan Wanninger Mangerico Qestaj via email to ferzaakat@gmail.com. Include the proposed change description, impact assessment, and required approval.\n2. Assessment: The Change Review Board, chaired by Delma Dunic, will evaluate the request. Board members can be reached at +57.51.682 7722 and 0025-...
```

  - `TITLE` [93:97] = `Mstr`
  - `PERSON_NAME` [98:131] = `Djihan Wanninger Mangerico Qestaj`
  - `EMAIL` [145:164] = `ferzaakat@gmail.com`
  - `PERSON_NAME` [300:311] = `Delma Dunic`
  - `TELEPHONENUM` [372:387] = `+57.51.682 7722`
  - `TELEPHONENUM` [392:407] = `0025-24112 8647`
  - `DATE` [488:507] = `2019-03-10T00:00:00`
  - `STREET` [536:555] = `63 Avenue Northwest`
  - `BUILDINGNUM` [557:561] = `1196`
  - `CITY` [563:569] = `Simcoe`
  - `ZIPCODE` [570:577] = `S0G 3W0`
  - `PERSON_NAME` [613:635] = `Sarwar Henchoz Guinand`
  - `AGE` [641:643] = `31`
  - `SEX` [645:651] = `Female`
  - `DRIVERLICENSENUM` [714:724] = `4V4BM2D6M6`
  - `TAXNUM` [755:766] = `99771 56538`
  - `EMAIL` [865:882] = `NJQP@tutanota.com`
  - `TELEPHONENUM` [893:909] = `+41 391-554 4760`

**id**: `ai4p-en-20902767`  •  **spans**: 6

```
Contact Form Submission – Blog Collaboration Request\nName: Iwo Al Atrat Baros Panglungtshang\nEmail: ZTG@protonmail.com\nPhone: 05876 99972 \nLocation: Copetown, J0W 1A0\nMessage: I am interested in partnering on a series of sponsored posts about travel gear. Please let me know your rates, preferred payment method (e.g., credit card ending in 67631288601623), and any required media kits. Looking fo...
```

  - `PERSON_NAME` [59:92] = `Iwo Al Atrat Baros Panglungtshang`
  - `EMAIL` [100:118] = `ZTG@protonmail.com`
  - `TELEPHONENUM` [126:138] = `05876 99972 `
  - `CITY` [149:157] = `Copetown`
  - `ZIPCODE` [159:166] = `J0W 1A0`
  - `CREDITCARDNUMBER` [341:355] = `67631288601623`

**id**: `ai4p-en-20903167`  •  **spans**: 4

```
By allocating a budget of $36761642179576 per staff member and tracking results through EK@aol.com and (83)-0156-1052, HR teams can quantify the ROI of human‑capital development across our Lévis offices.
```

  - `CREDITCARDNUMBER` [27:41] = `36761642179576`
  - `EMAIL` [88:98] = `EK@aol.com`
  - `TELEPHONENUM` [103:117] = `(83)-0156-1052`
  - `CITY` [189:194] = `Lévis`

**id**: `ai4p-en-20903542`  •  **spans**: 9

```
Subject: Your next adventure with travel‑friendly boardgames\n\nDear Mayoress Abrehet Lévénez,\n\nWe are excited to announce our new "Road‑Trip Game Kit" that fits perfectly in a carry‑on bag and includes compact versions of classics like Settlers of Catan, Ticket to Ride, and Pandemic. The kit will be shipped to your address at Township Road 280 # 570, Mission, G6G on October/96 and you can tr...
```

  - `TITLE` [69:77] = `Mayoress`
  - `PERSON_NAME` [78:93] = `Abrehet Lévénez`
  - `STREET` [331:348] = `Township Road 280`
  - `BUILDINGNUM` [351:354] = `570`
  - `CITY` [356:363] = `Mission`
  - `ZIPCODE` [365:368] = `G6G`
  - `DATE` [372:382] = `October/96`
  - `EMAIL` [434:447] = `39N@yahoo.com`
  - `TELEPHONENUM` [515:532] = `0100.499 559.5202`

