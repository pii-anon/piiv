# Quality scan - ai4privacy_de

- Rows scanned: **10,000**
- Rows with at least one quality issue: **9,634** (96.3%)

## Per-label quality

| Label | Spans | Anchor rate | Format pass | Format fails | Junk |
|---|---:|---:|---:|---|---:|
| `AGE` | 3808 | 24.9% | n/a | — | 435 |
| `BUILDINGNUM` | 3698 | n/a | n/a | — | 729 |
| `CITY` | 5317 | 9.3% | n/a | — | 0 |
| `CREDITCARDNUMBER` | 2508 | n/a | 9.5% | `luhn_fail`=2270 | 0 |
| `DATE` | 9516 | 37.4% | 48.6% | `not_date_format`=4888 | 0 |
| `DRIVERLICENSENUM` | 2137 | 46.7% | n/a | — | 0 |
| `EMAIL` | 5503 | n/a | 96.3% | `not_email_format`=206 | 0 |
| `GENDER` | 2365 | 47.3% | n/a | — | 0 |
| `GIVENNAME` | 8887 | n/a | n/a | — | 0 |
| `IDCARDNUM` | 2074 | 26.9% | 0.0% | `not_personalausweis_shape`=2074 | 0 |
| `PASSPORTNUM` | 1572 | 31.1% | n/a | — | 0 |
| `SEX` | 1998 | 88.2% | n/a | — | 996 |
| `SOCIALNUM` | 2034 | 47.1% | n/a | — | 0 |
| `STREET` | 3733 | 71.7% | n/a | — | 0 |
| `SURNAME` | 7790 | n/a | n/a | — | 0 |
| `TAXNUM` | 2302 | 52.4% | 0.0% | `not_steuerid_shape`=2302 | 0 |
| `TELEPHONENUM` | 4100 | 30.3% | n/a | — | 0 |
| `TITLE` | 4197 | 42.3% | n/a | — | 0 |
| `ZIPCODE` | 3338 | 26.3% | n/a | — | 0 |

## Sample anchor failures (first 5 per label)

### `AGE`  (2861 / 3808 no-anchor)
- `ai4p-de-20694919` value=`22`  context: ` Ihrer Karriere, wobei Mitarbeiter über 22 Jahren ein zusätzliches Dienstalterbonu`
- `ai4p-de-20694922` value=`80`  context: `pektiven die Fluktuationsrate um bis zu 80 % reduziert. Daher haben wir ein Mentor`
- `ai4p-de-20694928` value=`13`  context: `rtsdatum: Oktober 19., 1963    • Alter: 13    • Geschlecht: M / Geschlechtsidentit`
- `ai4p-de-20694939` value=`79`  context: `chterverteilung (O) und Altersstruktur (79), um zukünftige Vergleiche zu erleichte`
- `ai4p-de-20694948` value=`68`  context: `Rechnung Nr. 2023‑6080-68 für das Weinberg‑Picknick‑Paket, ausges`

### `CITY`  (4824 / 5317 no-anchor)
- `ai4p-de-20694920` value=`Wien Wieden`  context: `ue Anschrift an: Goethestraße 315, 1090 Wien Wieden.`
- `ai4p-de-20694923` value=`Klagenfurt am Wörthersee`  context: `dio in der Bertha-von-Suttner-Weg 3E in Klagenfurt am Wörthersee an. Mitarbeiter, die das Angebot nutzen`
- `ai4p-de-20694928` value=`Natters`  context: `  • Anschrift: Industriezeile 250, 1080 Natters 3. Identitätsnachweis:    • Personalaus`
- `ai4p-de-20694928` value=`Innsbruck`  context: `falls abweichend): Idlhofgasse 41, 8020 Innsbruck  Bitte überprüfen Sie alle Angaben sorg`
- `ai4p-de-20694930` value=`Graz Geidorf`  context: `cht über das Sedimentationsverhalten im Graz Geidorf Becken verfasst, wobei die Proben von H`

### `DATE`  (5961 / 9516 no-anchor)
- `ai4p-de-20694919` value=`Mai/04`  context: `rüfen. Bitte geben Sie Ihr Geburtsdatum Mai/04 an, damit wir das Gehalt nach gesetzlic`
- `ai4p-de-20694928` value=`Oktober 19., 1963`  context: `name: Garbani-Nerini    • Geburtsdatum: Oktober 19., 1963    • Alter: 13    • Geschlecht: M / Ges`
- `ai4p-de-20694938` value=`2004-10-28T00:00:00`  context: `nummer 4549 380311 und dem Geburtsdatum 2004-10-28T00:00:00 überwacht, um eine hohe Datenintegrität`
- `ai4p-de-20694943` value=`März/75`  context: `ka Strauch Titel: Meister Geburtsdatum: März/75 Alter: 87 Jahre Geschlecht (biologisch)`
- `ai4p-de-20694945` value=`05/06/1980`  context: `Bitte überweisen Sie den Betrag bis zum 05/06/1980 auf das unten stehende Konto: IBAN: 311`

### `DRIVERLICENSENUM`  (1140 / 2137 no-anchor)
- `ai4p-de-20694921` value=`UVX174QMWB`  context: `Kontoinformationen an, die Sie in Ihrem UVX174QMWB finden. Die Auszahlung erfolgt monatlic`
- `ai4p-de-20694932` value=`XZ9W2CTOPF`  context: `us Klagenfurt am Wörthersee (Flugnummer XZ9W2CTOPF) sowie die Unterkunft im Hotel Puchstra`
- `ai4p-de-20694936` value=`CAQZNPVEN4`  context: `pfiehlt, die Datenbank mit den neuesten CAQZNPVEN4‑Einträgen zu aktualisieren.`
- `ai4p-de-20694974` value=`K3GPZJGKW4`  context: `usrüstung: - Kameragehäuse, Modellcode: K3GPZJGKW4 - Objektiv (24‑70 mm f/2,8) - Stativ (l`
- `ai4p-de-20695002` value=`P38VL7NF5G`  context: `am vor, die Zugriffsrechte mithilfe der P38VL7NF5G und der 07-9586608 jedes Mitarbeiters z`

### `GENDER`  (1247 / 2365 no-anchor)
- `ai4p-de-20694948` value=`Nicht-binär`  context: `ia (Geburtsdatum: 1943-01-28T00:00:00), Nicht-binär. Leistungen: privater Weinberg‑Guide, 3`
- `ai4p-de-20694958` value=`Androgyn`  context: `biologisch): M 5. Geschlechtsidentität: Androgyn 6. E‑Mail‑Adresse: 1963K@hotmail.com 7.`
- `ai4p-de-20694960` value=`Geschlechterqueer`  context: `e Fenster die Worte mit einem Hauch von Geschlechterqueer streichelt. Am Abend, wenn der Himmel s`
- `ai4p-de-20694963` value=`Transgender`  context: `lgt von einer Frage nach dem 14 und dem Transgender. Weiter unten wird nach der 9412 180517`
- `ai4p-de-20694991` value=`Transgender`  context: `ogisch): Männlich Geschlechtsidentität: Transgender Personalausweis‑Nr.: 31005651 Führersch`

### `IDCARDNUM`  (1516 / 2074 no-anchor)
- `ai4p-de-20694931` value=`18292463`  context: `ternen Datenbank unter dem Zugriffscode 18292463 gespeichert sind; ein detaillierter Ber`
- `ai4p-de-20694940` value=`62142070`  context: `mmer E9375947 und Personalausweisnummer 62142070, im System hinterlegt, bevor die Daten `
- `ai4p-de-20694956` value=`92683491`  context: `ätzlich muss der Identitätsnachweis mit 92683491 vorgelegt werden, damit das Filmbudget `
- `ai4p-de-20694971` value=`45854576`  context: `gänzen Sie fehlende Angaben zu ID‑Karte 45854576 bis zum 14/01/2011.`
- `ai4p-de-20694987` value=`35545487`  context: `hlen enthält:\n- Identifikationsnummer: 35545487\n- Steuernummer: 28-8758018\n- Sozialve`

### `PASSPORTNUM`  (1083 / 1572 no-anchor)
- `ai4p-de-20694930` value=`G0809984`  context: `hsten Peer‑Review‑Journal unter der DOI G0809984 veröffentlicht.`
- `ai4p-de-20694940` value=`E9375947`  context: ` aller Beteiligten, wie Reisepassnummer E9375947 und Personalausweisnummer 62142070, im `
- `ai4p-de-20694974` value=`V0246252`  context: `assnummer (falls Grenzübertritt nötig): V0246252  Zahlungsmodalität: Die Leihgebühr von `
- `ai4p-de-20694978` value=`M5300651`  context: `falls erforderlich für Grenzübertritt): M5300651  Bitte senden Sie das ausgefüllte Formu`
- `ai4p-de-20695003` value=`J4818709`  context: `für die Gültigkeit des 14073184 und des J4818709 jedes Remote‑Mitarbeiters, um Identität`

### `SEX`  (236 / 1998 no-anchor)
- `ai4p-de-20694939` value=`O`  context: `hrer jeweiligen Geschlechterverteilung (O) und Altersstruktur (79), um zukünftige`
- `ai4p-de-20694962` value=`F`  context: `ählen. Jede Zeile ist ein Spiegel ihrer F Identität, ein Tanz aus Licht und Schat`
- `ai4p-de-20695100` value=`Andere`  context: `. Herrn/Frau Ampa Vakilzadeh, 30 Jahre, Andere) aufzunehmen, das über die Bedeutung vo`
- `ai4p-de-20695139` value=`M`  context: `en wir um die Angabe Ihres Geschlechts (M) bzw. Ihrer Geschlechtsidentität (Nicht`
- `ai4p-de-20695200` value=`F`  context: `dan Haljime Ramacher Papleka, 14 Jahre, F, E‑Mail: 1W@aol.com`

### `SOCIALNUM`  (1075 / 2034 no-anchor)
- `ai4p-de-20694958` value=`0901 700729`  context: `PFE4DBD 11. Sozialversicherungs‑Nummer: 0901 700729 12. Steuer‑Identifikationsnummer: 90-35`
- `ai4p-de-20694963` value=`9412 180517`  context: `Transgender. Weiter unten wird nach der 9412 180517 gefragt, während das Feld für die Steue`
- `ai4p-de-20694987` value=`7351 480505`  context: `-8758018\n- Sozialversicherungs‑Nummer: 7351 480505\nBitte stellen Sie sicher, dass alle Da`
- `ai4p-de-20694991` value=`3965 770416`  context: `r.: PXUIMLJO25 Sozialversicherungs‑Nr.: 3965 770416 Steuer‑ID: 47-2401829 Reisepass‑Nr.: E7`
- `ai4p-de-20695002` value=`7412 550811`  context: `8 jedes Mitarbeiters zu verknüpfen. Die 7412 550811 dient dabei als zusätzlicher Authentifi`

### `STREET`  (1056 / 3733 no-anchor)
- `ai4p-de-20694928` value=`Industriezeile`  context: `ummer: +43 544-031.3327    • Anschrift: Industriezeile 250, 1080 Natters 3. Identitätsnachweis`
- `ai4p-de-20694928` value=`Idlhofgasse`  context: ` • Rechnungsadresse (falls abweichend): Idlhofgasse 41, 8020 Innsbruck  Bitte überprüfen Si`
- `ai4p-de-20694945` value=`Sandgasse`  context: `n: Bürgermeisterin Lourin Buffo Kottler Sandgasse 1437 6020 Linz E‑Mail: LI@hotmail.com T`
- `ai4p-de-20694960` value=`Neufeldweg`  context: ` an den alten Eichenschreibtisch in der Neufeldweg 1334 und lässt die Feder über das perga`
- `ai4p-de-20694993` value=`Kaserngasse`  context: `rmitteln, das am 1982-02-28T00:00:00 im Kaserngasse 100b in Linz Franckviertel Franckvierte`

### `TAXNUM`  (1096 / 2302 no-anchor)
- `ai4p-de-20694920` value=`79-1853093`  context: `en wir Ihre Steueridentifikationsnummer 79-1853093 und Ihre aktuelle Adresse. Bitte geben `
- `ai4p-de-20694952` value=`08-6974878`  context: `Details finden Sie unter Referenznummer 08-6974878.`
- `ai4p-de-20694963` value=`58-5747319`  context: `eld für die Steueridentifikationsnummer 58-5747319 mit einem leichten Zittern der Feder ge`
- `ai4p-de-20694976` value=`93-3441040`  context: `ng des Haushaltsplans – Referenznummer: 93-3441040. 3. Diskussion über neue Förderprojekte`
- `ai4p-de-20694999` value=`56-7434781`  context: `rr/Frau Batsang Kiowani, aufgrund Ihrer 56-7434781 müssen wir die neue Preisgestaltung für`

### `TELEPHONENUM`  (2858 / 4100 no-anchor)
- `ai4p-de-20694924` value=`+54-685227296`  context: `SHV@tutanota.com oder telefonisch unter +54-685227296 zur Verfügung. Wir freuen uns, gemeinsa`
- `ai4p-de-20694928` value=`+43 544-031.3327`  context: `ramyan@tutanota.com    • Telefonnummer: +43 544-031.3327    • Anschrift: Industriezeile 250, 108`
- `ai4p-de-20694937` value=`+438 81.897-6120`  context: `ouard ebenfalls unter der Telefonnummer +438 81.897-6120 erreichbar ist, um offene Fragen zur Me`
- `ai4p-de-20694948` value=`0153-82 761-9847`  context: `56. Bei Rückfragen können Sie uns unter 0153-82 761-9847 oder per E‑Mail an 1948B@gmail.com erre`
- `ai4p-de-20694958` value=`+20-459.555.0277`  context: `e: 1963K@hotmail.com 7. Telefonkontakt: +20-459.555.0277 8. Anschrift: Bahnhofstraße 15, 8020 Li`

### `TITLE`  (2421 / 4197 no-anchor)
- `ai4p-de-20694922` value=`Doktorin`  context: ` das von erfahrenen Führungskräften wie Doktorin Jadranka Landhou Enevoldsen Sekat gelei`
- `ai4p-de-20694928` value=`Richt`  context: `ch)  1. Persönliche Daten:    • Anrede: Richt    • Vorname: Goretta    • Nachname: Ga`
- `ai4p-de-20694934` value=`Hr`  context: `ie Bioindikator‑Arten‑Analyse wurde von Hr Kaj Samin am 06/12/2011 verfasst; er en`
- `ai4p-de-20694936` value=`Meister`  context: `Der Projektleiter, Meister Ricco Tsakalos, weist darauf hin, dass `
- `ai4p-de-20694943` value=`Meister`  context: `kshop Name: Esranur Anka Strauch Titel: Meister Geburtsdatum: März/75 Alter: 87 Jahre G`

### `ZIPCODE`  (2459 / 3338 no-anchor)
- `ai4p-de-20694920` value=`1090`  context: `re neue Anschrift an: Goethestraße 315, 1090 Wien Wieden.`
- `ai4p-de-20694928` value=`1080`  context: `327    • Anschrift: Industriezeile 250, 1080 Natters 3. Identitätsnachweis:    • Per`
- `ai4p-de-20694928` value=`8020`  context: `sse (falls abweichend): Idlhofgasse 41, 8020 Innsbruck  Bitte überprüfen Sie alle An`
- `ai4p-de-20694943` value=`4040`  context: `hlechterqueer Adresse: Zollerstraße 15, 4040 Zirl E‑Mail: M@hotmail.com Telefon: +87`
- `ai4p-de-20694945` value=`6020`  context: `rin Lourin Buffo Kottler Sandgasse 1437 6020 Linz E‑Mail: LI@hotmail.com Telefon: 06`

## Sample format failures

### `CREDITCARDNUMBER`  (2270 fails)
- `ai4p-de-20694923` value=`2200906163294476`  reason=`luhn_fail`
- `ai4p-de-20694928` value=`5276996182916431`  reason=`luhn_fail`
- `ai4p-de-20694933` value=`3858252627749792`  reason=`luhn_fail`
- `ai4p-de-20694941` value=`347474758766342`  reason=`luhn_fail`
- `ai4p-de-20694943` value=`6208564371898157`  reason=`luhn_fail`

### `DATE`  (4888 fails)
- `ai4p-de-20694921` value=`1989-12-03T00:00:00`  reason=`not_date_format`
- `ai4p-de-20694928` value=`Oktober 19., 1963`  reason=`not_date_format`
- `ai4p-de-20694930` value=`17. Dezember 1991`  reason=`not_date_format`
- `ai4p-de-20694933` value=`März 15., 1980`  reason=`not_date_format`
- `ai4p-de-20694938` value=`2004-10-28T00:00:00`  reason=`not_date_format`

### `EMAIL`  (206 fails)
- `ai4p-de-20694974` value=`noëdoggweiler@yahoo.com`  reason=`not_email_format`
- `ai4p-de-20694999` value=`kajeevan bla@hotmail.com`  reason=`not_email_format`
- `ai4p-de-20695091` value=`tiberidall'a@outlook.com`  reason=`not_email_format`
- `ai4p-de-20695100` value=`roda piedad@outlook.com`  reason=`not_email_format`
- `ai4p-de-20695267` value=`fiohoddé@yahoo.com`  reason=`not_email_format`

### `IDCARDNUM`  (2074 fails)
- `ai4p-de-20694928` value=`03690080`  reason=`not_personalausweis_shape`
- `ai4p-de-20694931` value=`18292463`  reason=`not_personalausweis_shape`
- `ai4p-de-20694940` value=`62142070`  reason=`not_personalausweis_shape`
- `ai4p-de-20694943` value=`84394318`  reason=`not_personalausweis_shape`
- `ai4p-de-20694956` value=`92683491`  reason=`not_personalausweis_shape`

### `TAXNUM`  (2302 fails)
- `ai4p-de-20694920` value=`79-1853093`  reason=`not_steuerid_shape`
- `ai4p-de-20694928` value=`35-6658095`  reason=`not_steuerid_shape`
- `ai4p-de-20694932` value=`88-9927886`  reason=`not_steuerid_shape`
- `ai4p-de-20694936` value=`20-2182949`  reason=`not_steuerid_shape`
- `ai4p-de-20694943` value=`93-2661087`  reason=`not_steuerid_shape`

## Same-row format collisions

Two labels in the same row carrying values of identical (length, charclass).
Forces context-only disambiguation.

| Label pair | Same-row collisions |
|---|---:|
| `DATE` ↔ `TAXNUM` | 793 |
| `GIVENNAME` ↔ `SURNAME` | 682 |
| `AGE` ↔ `BUILDINGNUM` | 575 |
| `BUILDINGNUM` ↔ `ZIPCODE` | 313 |
| `GIVENNAME` ↔ `TITLE` | 217 |
| `SURNAME` ↔ `TITLE` | 160 |
| `CITY` ↔ `GIVENNAME` | 157 |
| `CITY` ↔ `SURNAME` | 146 |
| `GENDER` ↔ `SEX` | 143 |
| `CITY` ↔ `TITLE` | 120 |
| `EMAIL` ↔ `GIVENNAME` | 90 |
| `GENDER` ↔ `GIVENNAME` | 88 |
| `DATE` ↔ `EMAIL` | 86 |
| `GENDER` ↔ `SURNAME` | 82 |
| `SEX` ↔ `SURNAME` | 63 |
| `STREET` ↔ `SURNAME` | 61 |
| `CITY` ↔ `EMAIL` | 54 |
| `GIVENNAME` ↔ `SEX` | 50 |
| `EMAIL` ↔ `SURNAME` | 43 |
| `GIVENNAME` ↔ `STREET` | 42 |

## Label leakage (same value, multiple labels)

| Value | Labels seen |
|---|---|
| `22` | `AGE`, `BUILDINGNUM` |
| `80` | `AGE`, `BUILDINGNUM` |
| `13` | `AGE`, `BUILDINGNUM` |
| `1080` | `BUILDINGNUM`, `ZIPCODE` |
| `41` | `AGE`, `BUILDINGNUM` |
| `Sen` | `GIVENNAME`, `TITLE` |
| `12` | `AGE`, `BUILDINGNUM` |
| `79` | `AGE`, `BUILDINGNUM` |
| `87` | `AGE`, `BUILDINGNUM` |
| `Weiblich` | `GENDER`, `SEX` |
| `15` | `AGE`, `BUILDINGNUM` |
| `68` | `AGE`, `BUILDINGNUM` |
| `32` | `AGE`, `BUILDINGNUM` |
| `18` | `AGE`, `BUILDINGNUM` |
| `6` | `AGE`, `BUILDINGNUM` |
| `2` | `AGE`, `BUILDINGNUM` |
| `36` | `AGE`, `BUILDINGNUM` |
| `14` | `AGE`, `BUILDINGNUM` |
| `3` | `AGE`, `BUILDINGNUM` |
| `49` | `AGE`, `BUILDINGNUM` |

