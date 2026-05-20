# ai4privacy (en) - dataset audit

Rows analyzed: **5,000**

Total spans: **44,271**

## Length distributions

### Text length (characters)

| min | p25 | p50 | p75 | p95 | max | mean |
|---|---|---|---|---|---|---|
| 57.0 | 241.0 | 391.0 | 614.0 | 997.0 | 1200.0 | 455.3 |

### Text length (whitespace tokens)

| min | p25 | p50 | p75 | p95 | max | mean |
|---|---|---|---|---|---|---|
| 5.0 | 36.0 | 58.0 | 90.0 | 146.0 | 200.0 | 67.1 |

### Spans per row

| min | p25 | p50 | p75 | p95 | max | mean |
|---|---|---|---|---|---|---|
| 1.0 | 5.0 | 8.0 | 12.0 | 19.0 | 32.0 | 8.9 |

### Span length (characters)

| min | p25 | p50 | p75 | p95 | max | mean |
|---|---|---|---|---|---|---|
| 1.0 | 6.0 | 10.0 | 14.0 | 19.0 | 43.0 | 10.0 |

## Label distribution

| Label | Count | % of spans | Example value |
|---|---:|---:|---|
| `GIVENNAME` | 5406 | 12.21 | Dushyant |
| `DATE` | 5252 | 11.86 | November 24th, 1959 |
| `SURNAME` | 4708 | 10.63 | Herta Wagen Thompson-McNicol |
| `EMAIL` | 3317 | 7.49 | 1959P@yahoo.com |
| `CITY` | 3028 | 6.84 | Vienna |
| `TITLE` | 2983 | 6.74 | Mr |
| `TELEPHONENUM` | 2430 | 5.49 | +36 774 580.0503 |
| `STREET` | 2183 | 4.93 | Mount Hope Road |
| `BUILDINGNUM` | 2092 | 4.73 | 703 |
| `AGE` | 2025 | 4.57 | 60 |
| `ZIPCODE` | 1937 | 4.38 | V2P |
| `CREDITCARDNUMBER` | 1312 | 2.96 | 60115140036341395 |
| `DRIVERLICENSENUM` | 1239 | 2.80 | RRH1ZZBPCA |
| `IDCARDNUM` | 1217 | 2.75 | BEKD82TLNP |
| `GENDER` | 1181 | 2.67 | Female |
| `TAXNUM` | 1126 | 2.54 | 4686135601 |
| `SOCIALNUM` | 1061 | 2.40 | 2492368319 |
| `SEX` | 891 | 2.01 | O |
| `PASSPORTNUM` | 883 | 1.99 | IG1622654 |

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

**id**: `ai4p-en-20904643`  •  **spans**: 32

```
Master Thamiliniyan Santinelli\nModern Climbing Challenges – Registration Form\n\nDear Kélia Yin Intaglietta,\n\nThank you for your interest in our upcoming climbing event on 16th September 2003. To complete your registration, please provide the following details:\n\n1. Full Name: Master Aurika Ayoub Sieczewicz\n2. Date of Birth: 18th March 1998\n3. Age: 1\n4. Sex: Male\n5. Gender Identity: Agender\n6. Ema...
```

  - `TITLE` [0:6] = `Master`
  - `GIVENNAME` [7:19] = `Thamiliniyan`
  - `SURNAME` [20:30] = `Santinelli`
  - `GIVENNAME` [84:93] = `Kélia Yin`
  - `SURNAME` [94:105] = `Intaglietta`
  - `DATE` [170:189] = `16th September 2003`
  - `TITLE` [275:281] = `Master`
  - `GIVENNAME` [282:288] = `Aurika`
  - `SURNAME` [289:305] = `Ayoub Sieczewicz`
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
  - ... and 12 more spans

## Random samples

**id**: `ai4p-en-20901966`  •  **spans**: 18

```
Mr Dushyant Herta Wagen Thompson-McNicol,\n\nWe are delighted to inform you that a new series of volunteer programmes targeting retirees has been launched in Vienna, and we believe your experience and passion would be a perfect match. As a seasoned professional aged 60 with a background in Female community service, you are invited to join the "Silver Mentors" initiative, which pairs seasoned volu...
```

  - `TITLE` [0:2] = `Mr`
  - `GIVENNAME` [3:11] = `Dushyant`
  - `SURNAME` [12:40] = `Herta Wagen Thompson-McNicol`
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
  - `GIVENNAME` [1031:1038] = `Zimrije`
  - `SURNAME` [1039:1044] = `Niemz`
  - `ZIPCODE` [1073:1076] = `V2P`
  - `CITY` [1077:1086] = `Thorndale`

**id**: `ai4p-en-20902305`  •  **spans**: 9

```
Meeting Minutes – Team Communication Review – May 18th, 2021\n\nAttendees:\n– Mstr Jocelma Ludivine Özkan Jedrusik Perl\n– Mister Kajenthiran Kabongo Jugnet Buzduga\n\nThe group discussed the recent feedback indicating delays in message routing and the impact on project timelines. Action items include consolidating chat platforms, setting response‑time expectations, and piloting a weekly briefing cal...
```

  - `DATE` [46:60] = `May 18th, 2021`
  - `TITLE` [75:79] = `Mstr`
  - `GIVENNAME` [80:96] = `Jocelma Ludivine`
  - `SURNAME` [97:116] = `Özkan Jedrusik Perl`
  - `TITLE` [119:125] = `Mister`
  - `GIVENNAME` [126:145] = `Kajenthiran Kabongo`
  - `SURNAME` [146:160] = `Jugnet Buzduga`
  - `TELEPHONENUM` [477:492] = `+28.29 453 0446`
  - `CITY` [526:537] = `Saint Marys`

**id**: `ai4p-en-20902624`  •  **spans**: 11

```
Master Juniper Jónsson invites you to the introductory workshop on Music Video Directing, scheduled for January 22nd, 1996 at our downtown studio located on Mississauga Road #3919, Arnes, K1X 1E2.\nThe session, designed for creators aged 0 and above, will cover storyboarding, camera basics, and basic lighting, and participants can confirm their spot by sending a reply to TL@gmail.com with paymen...
```

  - `TITLE` [0:6] = `Master`
  - `GIVENNAME` [7:14] = `Juniper`
  - `SURNAME` [15:22] = `Jónsson`
  - `DATE` [104:122] = `January 22nd, 1996`
  - `STREET` [157:173] = `Mississauga Road`
  - `BUILDINGNUM` [175:179] = `3919`
  - `CITY` [181:186] = `Arnes`
  - `ZIPCODE` [188:195] = `K1X 1E2`
  - `AGE` [237:238] = `0`
  - `EMAIL` [373:385] = `TL@gmail.com`
  - `CREDITCARDNUMBER` [441:459] = `644193614129321845`

**id**: `ai4p-en-20902946`  •  **spans**: 15

```
Subject: Flight Options for Our Upcoming Trip – Cheap Domestic Flights\n\nHi Michée,\nI’ve been scouting for the most affordable routes from Whitby to Stouffville for the dates December/75 to 12th August 1986. The best deal I found is a round‑trip on Air Canada for only 5441716903452984 CAD, departing at 08:15 on 03/09/1953 and returning at 19:45 on 14/06/1951. Please confirm if the schedule works...
```

  - `GIVENNAME` [75:81] = `Michée`
  - `CITY` [138:144] = `Whitby`
  - `CITY` [148:159] = `Stouffville`
  - `DATE` [174:185] = `December/75`
  - `DATE` [189:205] = `12th August 1986`
  - `CREDITCARDNUMBER` [268:284] = `5441716903452984`
  - `DATE` [312:322] = `03/09/1953`
  - `DATE` [349:359] = `14/06/1951`
  - `PASSPORTNUM` [420:429] = `TT2522594`
  - `IDCARDNUM` [434:444] = `TLHM1989BK`
  - `CREDITCARDNUMBER` [633:649] = `6269926523137299`
  - `TITLE` [703:707] = `Mstr`
  - `SURNAME` [708:729] = `Fanfan Gutzeit Djabar`
  - `EMAIL` [730:744] = `ZM@hotmail.com`
  - `TELEPHONENUM` [747:762] = `+91-90 567 5849`

**id**: `ai4p-en-20903249`  •  **spans**: 11

```
The itinerary for the "Mirage Hunt" expedition begins with a briefing at sunrise on 5th August 1988 in the western barracks of Grassie.  Each scout, identified by their Piranavi Vaux-Riera and 18, must submit a signed waiver that includes their 7646602300 for insurance purposes.  A tax clearance certificate (87148.85880) is required to cross the sovereign dunes of the neighboring caliphate, and...
```

  - `DATE` [84:99] = `5th August 1988`
  - `CITY` [127:134] = `Grassie`
  - `GIVENNAME` [169:177] = `Piranavi`
  - `SURNAME` [178:188] = `Vaux-Riera`
  - `AGE` [193:195] = `18`
  - `SOCIALNUM` [245:255] = `7646602300`
  - `TAXNUM` [310:321] = `87148.85880`
  - `EMAIL` [449:465] = `F@protonmail.com`
  - `TITLE` [494:498] = `Mstr`
  - `GIVENNAME` [499:505] = `Somnuk`
  - `DRIVERLICENSENUM` [529:539] = `VCQ29EAV5Z`

