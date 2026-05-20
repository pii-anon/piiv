# Quality scan - ai4privacy_en

- Rows scanned: **10,000**
- Rows with at least one quality issue: **9,237** (92.4%)

## Per-label quality

| Label | Spans | Anchor rate | Format pass | Format fails | Junk |
|---|---:|---:|---:|---|---:|
| `AGE` | 4009 | 67.4% | n/a | — | 451 |
| `BUILDINGNUM` | 4141 | n/a | n/a | — | 67 |
| `CITY` | 6004 | 9.5% | n/a | — | 0 |
| `CREDITCARDNUMBER` | 2625 | n/a | 9.9% | `luhn_fail`=2365 | 0 |
| `DATE` | 10609 | 64.1% | 83.2% | `not_date_format`=1786 | 0 |
| `DRIVERLICENSENUM` | 2502 | 47.8% | n/a | — | 0 |
| `EMAIL` | 6571 | n/a | 96.5% | `not_email_format`=233 | 0 |
| `GENDER` | 2444 | 60.0% | n/a | — | 0 |
| `GIVENNAME` | 10695 | n/a | n/a | — | 0 |
| `IDCARDNUM` | 2455 | 55.2% | n/a | — | 0 |
| `PASSPORTNUM` | 1768 | 46.1% | n/a | — | 0 |
| `SEX` | 1809 | 80.8% | n/a | — | 904 |
| `SOCIALNUM` | 2089 | 25.1% | 0.0% | `not_ssn_shape`=2089 | 0 |
| `STREET` | 4333 | 84.4% | n/a | — | 0 |
| `SURNAME` | 9215 | n/a | n/a | — | 0 |
| `TAXNUM` | 2199 | 69.4% | n/a | — | 0 |
| `TELEPHONENUM` | 4842 | 71.8% | n/a | — | 0 |
| `TITLE` | 5864 | 56.4% | n/a | — | 0 |
| `ZIPCODE` | 3837 | 38.9% | n/a | — | 0 |

## Sample anchor failures (first 5 per label)

### `AGE`  (1307 / 4009 no-anchor)
- `ai4p-en-20901969` value=`6`  context: ` ______________________________  (e.g., 6) 5. Sex: ______________________________`
- `ai4p-en-20901971` value=`51`  context: `lude two dozen mugs of hot apple cider (51‑year‑old family recipe) and a selection`
- `ai4p-en-20901978` value=`79`  context: `m Star” badges, noting each recipient’s 79 and Two-spirit for fun statistics. For `
- `ai4p-en-20902009` value=`39`  context: `. Please also share your Two-spirit and 39 so we can tailor the session. Your conf`
- `ai4p-en-20902043` value=`64`  context: `(born March/67), who has dedicated over 64 years to preserving cultural heritage. `

### `CITY`  (5431 / 6004 no-anchor)
- `ai4p-en-20901966` value=`Vienna`  context: `targeting retirees has been launched in Vienna, and we believe your experience and pas`
- `ai4p-en-20901966` value=`Thorndale`  context: `e Niemz Volunteer Coordination Team V2P Thorndale`
- `ai4p-en-20901971` value=`Surrey`  context: `ered to 5 Concession 5 Townsend Road in Surrey by 04/05/2025; please confirm the ZIP c`
- `ai4p-en-20901976` value=`West Vancouver`  context: `309  Shipping Address: 57 Range Road 45 West Vancouver, L9V 2C6, N0C 1B0  Identification Numbe`
- `ai4p-en-20901978` value=`Yale`  context: `terrace, located at Dugald Road 71, S0G Yale; please RSVP by Friday noon. Your host,`

### `DATE`  (3813 / 10609 no-anchor)
- `ai4p-en-20901966` value=`27th January 1990`  context: `k forward to receiving your response by 27th January 1990 and welcoming you to our vibrant volunt`
- `ai4p-en-20901969` value=`1968-05-21T00:00:00`  context: `of Birth: ______________________ (e.g., 1968-05-21T00:00:00) 4. Age: ______________________________`
- `ai4p-en-20901971` value=`04/05/2025`  context: `Concession 5 Townsend Road in Surrey by 04/05/2025; please confirm the ZIP code T0M for ac`
- `ai4p-en-20901974` value=`February 21st, 1981`  context: ` to AD1972@protonmail.com no later than February 21st, 1981 to be considered for the upcoming recru`
- `ai4p-en-20901976` value=`1972-12-25T00:00:00`  context: `Branding Tools – Order Form (Reference: 1972-12-25T00:00:00)  Customer Details: Name: Senator Baris`

### `DRIVERLICENSENUM`  (1305 / 2502 no-anchor)
- `ai4p-en-20901979` value=`C8WYMTG30B`  context: `e participants to bring a copy of their C8WYMTG30B and UM1003851 for the off‑site safety c`
- `ai4p-en-20901988` value=`RSUN0I38UL`  context: `se Order – Porcelain Shard Mosaic (PO # RSUN0I38UL)\nBuyer: Mayoress Somsong Berzia\nShipp`
- `ai4p-en-20901999` value=`M3M5YGKSN4`  context: `d provide a copy of your 3PVWMZ54OP and M3M5YGKSN4 by July/40 so we can complete the lease`
- `ai4p-en-20902018` value=`R1XN75B3V2`  context: `All volunteers must present a valid R1XN75B3V2 and proof of 4312539677 before the firs`
- `ai4p-en-20902068` value=`U30YMWZ6W8`  context: `se fill out the attached form with your U30YMWZ6W8 and 08345 39573.`

### `GENDER`  (977 / 2444 no-anchor)
- `ai4p-en-20901966` value=`Female`  context: `ofessional aged 60 with a background in Female community service, you are invited to j`
- `ai4p-en-20901969` value=`Female`  context: `er: ___________________________  (e.g., Female) 7. Email: ____________________________`
- `ai4p-en-20901978` value=`Two-spirit`  context: ` badges, noting each recipient’s 79 and Two-spirit for fun statistics. For any dietary res`
- `ai4p-en-20901980` value=`Male`  context: `ic A‑AB‑C ballad form. As a 10-year-old Male musician, you already have a strong sen`
- `ai4p-en-20901997` value=`Transgender`  context: `the demographic shift, especially among Transgender shoppers, is influencing demand pattern`

### `IDCARDNUM`  (1099 / 2455 no-anchor)
- `ai4p-en-20901969` value=`0EBDIAQ6LI`  context: `ard #: ________________________  (e.g., 0EBDIAQ6LI) 11. Driver's License #: ______________`
- `ai4p-en-20901979` value=`QGFITSQIGO`  context: `oses please ensure your 17468.48681 and QGFITSQIGO are up‑to‑date in the HR portal. Attend`
- `ai4p-en-20901999` value=`3PVWMZ54OP`  context: `-07T00:00:00 and provide a copy of your 3PVWMZ54OP and M3M5YGKSN4 by July/40 so we can com`
- `ai4p-en-20902011` value=`H1N4KZTLYI`  context: `r the next session, please provide your H1N4KZTLYI and preferred payment method using your`
- `ai4p-en-20902019` value=`4G4UUWITY0`  context: `2683. Attendees can sign up using their 4G4UUWITY0 and will receive a personalized schedul`

### `PASSPORTNUM`  (953 / 1768 no-anchor)
- `ai4p-en-20901979` value=`UM1003851`  context: `to bring a copy of their C8WYMTG30B and UM1003851 for the off‑site safety check, as well `
- `ai4p-en-20901981` value=`JZ1476794`  context: `@yahoo.com Identification: RY8Q1QQ1ZG / JZ1476794 Tax Reference: 9271549102  Please descr`
- `ai4p-en-20902000` value=`FQ2517678`  context: `h participant’s 8907025093 and a recent FQ2517678 for emergency contacts. Also, could the`
- `ai4p-en-20902005` value=`HT1521703`  context: `your spot, please submit a copy of your HT1521703 and your 8518467744 via email. The work`
- `ai4p-en-20902042` value=`AP7680106`  context: `7619387, 0864281188, and a copy of your AP7680106 via the secure portal. A light dinner w`

### `SEX`  (348 / 1809 no-anchor)
- `ai4p-en-20901969` value=`O`  context: ` ______________________________  (e.g., O) 6. Gender: ___________________________`
- `ai4p-en-20902021` value=`F`  context: `entities and respects each individual's F at registration. The consent form requi`
- `ai4p-en-20902021` value=`O`  context: `isting the participant's Two-spirit and O along with emergency contact details.`
- `ai4p-en-20902053` value=`O`  context: `accessibility for students of different O backgrounds, and the adequacy of the re`
- `ai4p-en-20902088` value=`M`  context: ` OX0116702, included individuals of all M and Genderqueer identities, ensuring br`

### `SOCIALNUM`  (1564 / 2089 no-anchor)
- `ai4p-en-20901969` value=`2492368319`  context: `al Security #: ________________  (e.g., 2492368319) 13. Tax ID #: ________________________`
- `ai4p-en-20901978` value=`5435165744`  context: `rictions, email N@outlook.com with your 5435165744 so we can accommodate everyone.`
- `ai4p-en-20901983` value=`0988513161`  context: ` copyright office using the applicant's 0988513161 to ensure proper attribution.`
- `ai4p-en-20901988` value=`7599297658`  context: `r.\nFor compliance, please provide your 7599297658 and verify the purchaser’s age as 74 ye`
- `ai4p-en-20901997` value=`7960166357`  context: `ss is tracked under registration number 7960166357.`

### `STREET`  (676 / 4333 no-anchor)
- `ai4p-en-20902033` value=`Rue Gagné`  context: `ss experience, from welcoming us at 180 Rue Gagné to arranging a private dinner.`
- `ai4p-en-20902082` value=`Concession 4`  context: `of Edmonton. The venue is located at 91 Concession 4, J0K Aurora.  Please confirm your atten`
- `ai4p-en-20902140` value=`Belvedere Way Northwest`  context: `Miss Philippe-Alain Mazard Belvedere Way Northwest 256 Zurich, S0G 0186 92-084 2287 | GT13`
- `ai4p-en-20902150` value=`Route 101 Sud`  context: `73-6236.  Our office, located at 103937 Route 101 Sud, Black Diamond, S7K 2L2, welcomes you t`
- `ai4p-en-20902161` value=`OR-Branch 200`  context: `he fieldwork was conducted in Regina on OR-Branch 200. All stakeholders are requested to revi`

### `TAXNUM`  (672 / 2199 no-anchor)
- `ai4p-en-20901969` value=`4686135601`  context: `ID #: _________________________  (e.g., 4686135601) 14. Credit Card (last 4): ____________`
- `ai4p-en-20902023` value=`77345.18937`  context: `get statement referencing the allocated 77345.18937. Please forward the completed document `
- `ai4p-en-20902025` value=`09262.05840`  context: `0593893473374 and the invoice number is 09262.05840. Shipment will be to 342 Nth Service Ro`
- `ai4p-en-20902042` value=`0864281188`  context: `ration, please provide your 5867619387, 0864281188, and a copy of your AP7680106 via the s`
- `ai4p-en-20902063` value=`90172.68858`  context: `ate. Any discrepancies in 4722608895 or 90172.68858 listed on the student enrollment forms `

### `TELEPHONENUM`  (1365 / 4842 no-anchor)
- `ai4p-en-20901969` value=`01737.306706`  context: `: _____________________________  (e.g., 01737.306706) 9. Address: __________________________`
- `ai4p-en-20901995` value=`+02.47 511 5071`  context: `Michelino Gauß texted at +02.47 511 5071: 'Hey, did you see the clearance aisle?`
- `ai4p-en-20901999` value=`+39 165.114-2795`  context: `s, Zindan Desfourneaux Property Manager +39 165.114-2795 LL@gmail.com`
- `ai4p-en-20902009` value=`+44-52-166 6465`  context: ` to NG1994@protonmail.com or by texting +44-52-166 6465. We look forward to a cruelty‑free, col`
- `ai4p-en-20902012` value=`013 33-867 7888`  context: `ling najarkalamari@gmail.com or calling 013 33-867 7888 before September/09. All participants w`

### `TITLE`  (2558 / 5864 no-anchor)
- `ai4p-en-20901974` value=`Judge`  context: `cruitment questionnaire: 1) Full name – Judge Anastasja Lucisano; 2) Age – 82 years, `
- `ai4p-en-20901976` value=`Senator`  context: `2-25T00:00:00)  Customer Details: Name: Senator Barish Kronberger Date of Birth: June 1`
- `ai4p-en-20901978` value=`Madame`  context: ` please RSVP by Friday noon. Your host, Madame Schahin Mitschke, will share a quick re`
- `ai4p-en-20901980` value=`Madame`  context: `Dear Madame Jochanan Mahbub Codorello, I hope your `
- `ai4p-en-20901988` value=`Mayoress`  context: ` Shard Mosaic (PO # RSUN0I38UL)\nBuyer: Mayoress Somsong Berzia\nShipping Address: Towns`

### `ZIPCODE`  (2344 / 3837 no-anchor)
- `ai4p-en-20901966` value=`V2P`  context: `mrije Niemz Volunteer Coordination Team V2P Thorndale`
- `ai4p-en-20901976` value=`L9V 2C6, N0C 1B0`  context: `dress: 57 Range Road 45 West Vancouver, L9V 2C6, N0C 1B0  Identification Numbers (for verificati`
- `ai4p-en-20901978` value=`S0G`  context: `top terrace, located at Dugald Road 71, S0G Yale; please RSVP by Friday noon. Your `
- `ai4p-en-20901981` value=`T0M 0A0`  context: `s: 315944 Route Antonio-Talbot, Bissett T0M 0A0 Contact: 08.88-19.54.62 | hysehamdia@ya`
- `ai4p-en-20901988` value=`L9W`  context: `ress: Township Road 512 274248, Aylmer, L9W\nContact Information: Phone – +07.62-75`

## Sample format failures

### `CREDITCARDNUMBER`  (2365 fails)
- `ai4p-en-20901969` value=`60115140036341395`  reason=`luhn_fail`
- `ai4p-en-20901971` value=`3573039696158734`  reason=`luhn_fail`
- `ai4p-en-20901976` value=`4688351559785628`  reason=`luhn_fail`
- `ai4p-en-20901979` value=`2203232670615155`  reason=`luhn_fail`
- `ai4p-en-20901988` value=`6299130182591247`  reason=`luhn_fail`

### `DATE`  (1786 fails)
- `ai4p-en-20901969` value=`1968-05-21T00:00:00`  reason=`not_date_format`
- `ai4p-en-20901976` value=`1972-12-25T00:00:00`  reason=`not_date_format`
- `ai4p-en-20901980` value=`1992-06-06T00:00:00`  reason=`not_date_format`
- `ai4p-en-20901992` value=`1974-04-06T00:00:00`  reason=`not_date_format`
- `ai4p-en-20901997` value=`1995-10-03T00:00:00`  reason=`not_date_format`

### `EMAIL`  (233 fails)
- `ai4p-en-20901971` value=`neddymuñez@hotmail.com`  reason=`not_email_format`
- `ai4p-en-20902043` value=`ajdenvan cauwenbe@hotmail.com`  reason=`not_email_format`
- `ai4p-en-20902053` value=`franchboér@yahoo.com`  reason=`not_email_format`
- `ai4p-en-20902091` value=`yuchenwülser@gmail.com`  reason=`not_email_format`
- `ai4p-en-20902155` value=`sárkapron@protonmail.com`  reason=`not_email_format`

### `SOCIALNUM`  (2089 fails)
- `ai4p-en-20901969` value=`2492368319`  reason=`not_ssn_shape`
- `ai4p-en-20901976` value=`7556372895`  reason=`not_ssn_shape`
- `ai4p-en-20901978` value=`5435165744`  reason=`not_ssn_shape`
- `ai4p-en-20901983` value=`0988513161`  reason=`not_ssn_shape`
- `ai4p-en-20901988` value=`7599297658`  reason=`not_ssn_shape`

## Same-row format collisions

Two labels in the same row carrying values of identical (length, charclass).
Forces context-only disambiguation.

| Label pair | Same-row collisions |
|---|---:|
| `DRIVERLICENSENUM` ↔ `IDCARDNUM` | 934 |
| `GIVENNAME` ↔ `SURNAME` | 772 |
| `GIVENNAME` ↔ `TITLE` | 469 |
| `CITY` ↔ `GIVENNAME` | 377 |
| `SURNAME` ↔ `TITLE` | 353 |
| `CITY` ↔ `SURNAME` | 336 |
| `SOCIALNUM` ↔ `TAXNUM` | 235 |
| `CITY` ↔ `TITLE` | 210 |
| `AGE` ↔ `BUILDINGNUM` | 146 |
| `EMAIL` ↔ `STREET` | 98 |
| `GIVENNAME` ↔ `SURNAME` | 93 |
| `EMAIL` ↔ `GIVENNAME` | 88 |
| `GENDER` ↔ `SURNAME` | 85 |
| `DATE` ↔ `EMAIL` | 84 |
| `GENDER` ↔ `GIVENNAME` | 83 |
| `SEX` ↔ `TITLE` | 79 |
| `CITY` ↔ `GENDER` | 78 |
| `DATE` ↔ `STREET` | 77 |
| `GIVENNAME` ↔ `STREET` | 68 |
| `EMAIL` ↔ `SURNAME` | 67 |

## Label leakage (same value, multiple labels)

| Value | Labels seen |
|---|---|
| `60` | `AGE`, `BUILDINGNUM` |
| `Female` | `GENDER`, `SEX` |
| `6` | `AGE`, `BUILDINGNUM` |
| `51` | `AGE`, `BUILDINGNUM` |
| `5` | `AGE`, `BUILDINGNUM` |
| `82` | `AGE`, `BUILDINGNUM` |
| `69` | `AGE`, `BUILDINGNUM` |
| `57` | `AGE`, `BUILDINGNUM` |
| `71` | `AGE`, `BUILDINGNUM` |
| `79` | `AGE`, `BUILDINGNUM` |
| `10` | `AGE`, `BUILDINGNUM` |
| `Male` | `GENDER`, `GIVENNAME`, `SEX` |
| `74` | `AGE`, `BUILDINGNUM` |
| `58` | `AGE`, `BUILDINGNUM` |
| `63` | `AGE`, `BUILDINGNUM` |
| `39` | `AGE`, `BUILDINGNUM` |
| `Master` | `GIVENNAME`, `TITLE` |
| `78` | `AGE`, `BUILDINGNUM` |
| `54` | `AGE`, `BUILDINGNUM` |
| `64` | `AGE`, `BUILDINGNUM` |

