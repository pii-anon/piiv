# Dataset quality audit & eval-fitness verdict

**Date:** 2026-04-30
**Scope:** 10,000 rows from each of three imported PII datasets, no
transforms applied.
**Owner artifacts:** `benchmarks/data_import/quality.py` (analyzer),
`run_quality_scan.py` (driver), `reports/quality_<slug>.md` (per-dataset
detail with verbatim samples).

## Executive verdict

| Dataset | Rows w/ issue | Avg anchor rate | Format-pass rate | Verdict |
|---|---:|---:|---:|---|
| `ai4privacy_en` | **92.4%** | 55.4% | 70.4% | **Disqualified** |
| `ai4privacy_de` | **96.3%** | 38.5% | 46.4% | **Disqualified** |
| `wolframko_ru` | 39.1% | 84.0% | 88.2% | **Eval-grade** |

Drop ai4privacy en + de from primary evaluation. Use wolframko_ru as the
single defensible third-party eval surface. Cover en + de coverage with a
combination of (a) generator-only eval (with the caveat acknowledged),
(b) replacement corpus search (Presidio research set, BigCode PII bench,
BSI/government datasets), or (c) cite this audit *as a finding* in the
paper to justify the eval design.

## Methodology

The analyzer (`quality.py`) runs five checks per labeled span:

1. **Anchor presence.** Does the surrounding text (±40 chars) contain a
   keyword that disambiguates the labeled type? E.g., a `PASSPORTNUM`
   span with no `passport` / `Reisepass` / `паспорт` nearby is suspect.
   The anchor word lists were drawn from real-world PII detector
   keyword sets and the framework's own `keyword_anchors`. Labels that
   are inherently contextual (`GIVENNAME`, `SURNAME`, `BUILDINGNUM`)
   are excluded.
2. **Format compliance.** Where the entity has a strict format
   (Luhn-validated card, СНИЛС/ИНН with checksums, SSN in valid number
   ranges, ISO date, Steuer-ID, Personalausweis, email regex), does
   the value satisfy it?
3. **Junk values.** Empty, single-character, or all-punctuation values.
4. **Label leakage.** The exact same string labeled with two different
   types across the dataset.
5. **Same-row format collisions.** Two distinct labels in the same row
   produce values of identical (length, charclass), forcing the
   detector to disambiguate by context alone.

For #1 and #2, a span fails if it falls outside the expected pattern.
A row is flagged "with quality issue" if any of its spans fail any
check.

## Findings, per dataset

### ai4privacy_en — disqualified

**Critical format failures**:

| Label | Format-pass | Note |
|---|---:|---|
| `CREDITCARDNUMBER` | **9.9%** Luhn pass | 90% of "cards" are random 16-digit strings |
| `SOCIALNUM` | **0.0%** SSN-shape pass | None of 2,089 values are real SSNs |
| `DATE` | 83.2% | 17% have formats like `1968-05-21T00:00:00` |
| `EMAIL` | 96.5% | 3.5% missing `@` or top-level domain |

**Anchor failures** (% of spans with no disambiguating keyword in ±40 chars):

| Label | Anchor rate | Sample non-anchored value + context |
|---|---:|---|
| `CITY` | **9.5%** | `Vienna` in "*launched in Vienna, and we believe*" |
| `SOCIALNUM` | 25.1% | `5435165744` in "*email N@outlook.com with your 5435165744*" |
| `ZIPCODE` | 38.9% | `V2P` (3-char fragment) at "*Volunteer Coordination Team V2P Thorndale*" |
| `PASSPORTNUM` | 46.1% | `UM1003851` in "*copy of their C8WYMTG30B and UM1003851*" |
| `DRIVERLICENSENUM` | 47.8% | `RSUN0I38UL` in "*Order – Porcelain Shard Mosaic (PO # RSUN0I38UL)*" |
| `IDCARDNUM` | 55.2% | `0EBDIAQ6LI` in "*Card #: ____ (e.g., 0EBDIAQ6LI)*" |
| `TITLE` | 56.4% | `Judge` (often part of a name role, not honorific) |
| `GENDER` | 60.0% | `Female` in "*background in Female community service*" |
| `DATE` | 64.1% | reasonable miss rate; non-DOB dates often unanchored |
| `AGE` | 67.4% | `64` in "*has dedicated over 64 years*" |
| `TAXNUM` | 69.4% | many values are dollar amounts (`17468.48937`, `90172.68858`) |
| `TELEPHONENUM` | 71.8% | `+02.47 511 5071`, `+39 165.114-2795` (junk format too) |
| `SEX` | 80.8% | `O` in "*adequacy of different O backgrounds*" |
| `STREET` | 84.4% | best non-skip label |

**TAXNUM red flag:** sample values include `17468.48681`, `77345.18937`,
`09262.05840`, `90172.68858`. These are floats with decimals, not tax
IDs. The label appears to have been misapplied to currency or numeric
fields wholesale.

**Verdict:** the dataset is structurally broken. Random
business-document strings have been label-stamped with PII categories
without regard to semantics, format validation, or even basic span
boundaries. Cannot anchor a defensible evaluation.

### ai4privacy_de — disqualified, worse than en

**Critical format failures:**

| Label | Format-pass | Note |
|---|---:|---|
| `CREDITCARDNUMBER` | **9.5%** Luhn pass | Same problem as en |
| `IDCARDNUM` | **0.0%** Personalausweis-shape | All 2,074 values are 8-digit strings; real Personalausweis is 1 letter + 9 alnum |
| `TAXNUM` | **0.0%** Steuer-ID shape | None match the 11-digit Steuer-ID format |
| `DATE` | 48.6% | 51.4% non-conforming |
| `EMAIL` | 96.3% | OK |

**Anchor failures:**

| Label | Anchor rate |
|---|---:|
| `CITY` | **9.3%** |
| `AGE` | **24.9%** |
| `ZIPCODE` | 26.3% |
| `IDCARDNUM` | 26.9% |
| `TELEPHONENUM` | **30.3%** |
| `PASSPORTNUM` | 31.1% |
| `DATE` | 37.4% |
| `TITLE` | 42.3% |
| `DRIVERLICENSENUM` | 46.7% |
| `SOCIALNUM` | 47.1% |
| `GENDER` | 47.3% |
| `TAXNUM` | 52.4% |
| `STREET` | 71.7% |
| `SEX` | 88.2% |

**Format-shape mismatch with framework regex:** even the best-formatted
de PASSPORTNUM values (`M0839164` = 1 letter + 7 digits = 8 chars) do
not match the framework's de PASSPORTNUM regex (which expects 10 chars,
1 letter + 9 alnum, the real Reisepass shape). The framework regex
calibration is correct; the dataset is wrong.

**Verdict:** same disqualification as en, with the additional structural
problem that several de labels (`IDCARDNUM`, `TAXNUM`, `PASSPORTNUM`)
emit values whose format doesn't match the real-world shape they claim,
making framework-correct regexes unable to match them at all.

### wolframko_ru — eval-grade

**Strong signals on identifier classes:**

| Label | Spans | Anchor rate | Format pass |
|---|---:|---:|---:|
| `TAXNUM` (ИНН) | 1,750 | **99.1%** | **100%** + checksum |
| `DRIVERLICENSENUM` | 797 | **93.6%** | 100% |
| `IDCARDNUM` (RU passport) | 1,273 | **93.2%** | 100% |
| `EMAIL` | 2,667 | n/a | **100%** |
| `CREDITCARDNUMBER` | 1,138 | n/a | **100%** Luhn |
| `STREET` | 1,574 | 92.2% | n/a |
| `TELEPHONENUM` | 2,747 | 86.7% | n/a |
| `PASSWORD` | 1,243 | 86.4% | n/a |
| `CITY` | 2,211 | 78.0% | n/a |
| `ZIPCODE` | 1,006 | 72.4% | n/a |
| `USERNAME` | 2,125 | 63.8% | n/a |
| `DATEOFBIRTH` | 1,500 | 57.3% | **100%** |

**Caveats (not blockers for eval):**

- `SOCIALNUM` (СНИЛС): 95.9% anchored, 98.3% shape-valid, but only 1.7%
  pass the СНИЛС checksum. Implication: usable for *regex-based eval*
  (the framework's SNILS regex doesn't validate checksum); not usable
  for fine-tuning if we want the model to learn checksum-bearing
  values.
- `ACCOUNTNUM`: fake IBAN-shape (`RU45FOMI8350305641395`-style); not
  the real 20-digit RU bank-account format. Already dropped via the
  data_import allowlist.
- `DRIVERLICENSENUM ↔ IDCARDNUM`: 74 same-row format collisions (same
  4+6 digit shape). Forces context-only disambiguation. Discovered in
  the OPF eval (see `imported_eval_wolframko_ru.md`); the model
  collapsed both to `[PASSPORTNUM]`, yielding 0% recall on
  `[RU_DRV_LICENSE]`.
- `DATEOFBIRTH` 57.3% anchor rate: the unanchored ones are still
  format-valid dates; the dataset just doesn't always wrap them in
  `дата рождения` context. Not a noise problem, just a coverage
  characteristic.

**Same-row format collisions** (top 5):
1. `GIVENNAME` ↔ `SURNAME` (512) — expected
2. `CITY` ↔ `STREET` (105) — both can be Cyrillic noun phrases
3. **`DRIVERLICENSENUM` ↔ `IDCARDNUM` (74)** — the eval-blocking one
4. `SOCIALNUM` ↔ `TELEPHONENUM` (19)
5. `IDCARDNUM` ↔ `TELEPHONENUM` (11)

**Verdict:** keep as the primary eval dataset. The 39.1% rows-with-issue
figure is misleadingly high — most issues are non-blocking
(SNILS-checksum-fail, sometimes-unanchored DOB). The structured ID
classes that drive eval signal are 93%+ anchored and 100%
format-valid.

## Why this happened (hypothesis)

ai4privacy is generated by a templated synthetic pipeline whose Faker
backend emits values disjoint from the format/anchor pairings the
labels imply. The label assignment appears to be slot-name-based, not
content-based — a slot named `socialnum` gets stamped on whatever
random 9- or 10-digit string Faker emits, regardless of whether it's
actually an SSN, sits in a "Social Security:" template, or makes any
semantic sense in the surrounding prose.

wolframko, in contrast, appears to have been generated by a pipeline
that emits values *with* their disambiguating context (anchor word +
format-correct value) and then varies the surrounding prose. The
result: 90%+ anchor presence, 100% format on critical IDs.

## Implications for ACSAC eval design

1. **Primary eval surface:** wolframko_ru, with the existing
   `combine_names + combine_addresses + keep_only_allowed` pipeline.
2. **en + de coverage:** three options, in order of preference:
   - Replace ai4privacy with a better-curated corpus. Candidates:
     Microsoft Presidio's research synthetic set, BigCode PII bench
     (English), or government test corpora (BSI for de).
   - Generator-only eval for en + de, with the train/test isolation
     caveat acknowledged and discussed.
   - Cite this audit *as a finding* — "publicly available multilingual
     PII corpora exhibit systematic mislabeling at the 90% level on
     critical classes" is a publishable observation that justifies a
     constrained eval design.
3. **Limitations section content:** "We do not evaluate against
   ai4privacy en/de PII gold despite its prominence in the field, due
   to systematic format failures (≥90% Luhn-fail on credit cards, 100%
   format-fail on SSN/Steuer-ID/Personalausweis) and per-class anchor
   rates as low as 9.3%. See `dataset_quality_verdict.md` for
   methodology and per-class breakdown."

## Open follow-ups

- Implement RU_DRV_LICENSE template additions for retraining (parked
  pending this verdict; **decision: proceed**, since wolframko's DL gold
  is clean and worth fixing the OPF model against).
- Skip DE PASSPORTNUM template additions (Phase 2): the de eval surface
  is disqualified.
- Consider running the same scanner on candidate replacement en/de
  corpora before committing to one.
- Re-run wolframko_ru OPF eval after RU_DRV_LICENSE retrain; expect
  0% → 70%+ recall lift on `[RU_DRV_LICENSE]`.

## File pointers

- `benchmarks/data_import/quality.py` — analyzer (anchors, formats,
  junk, leakage, collisions)
- `benchmarks/data_import/run_quality_scan.py` — driver
  (`PYTHONPATH=src python -m benchmarks.data_import.run_quality_scan
  --rows 10000`)
- `benchmarks/data_import/reports/quality_summary.md` — headline table
- `benchmarks/data_import/reports/quality_ai4privacy_en.md` — full
  per-label detail with verbatim samples
- `benchmarks/data_import/reports/quality_ai4privacy_de.md` — same
- `benchmarks/data_import/reports/quality_wolframko_ru.md` — same
- `benchmarks/data_import/reports/label_mapping.md` — placeholder
  taxonomy mapping (current as of phone-collision fix)
