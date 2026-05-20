# Label coverage: imported datasets vs piiv framework

This document is the working label map for third-party evaluation. It reflects
the current imported-dataset surface:

- `nvidia/Nemotron-PII` for English / US-locale evaluation.
- `wolframko/russian-pii-66k` for Russian evaluation.

The ai4privacy EN/DE scans are kept as historical audit artifacts, but they are
not part of the primary eval surface after the quality verdict.

## Nemotron EN -> `policies/regex/en.yaml`

Nemotron rows are used only after:

```bash
--transform quality_gate_nemotron,combine_names,project_allowed
```

`quality_gate_nemotron` drops rows carrying unsupported labels
(`account_number`, `bank_routing_number`, `swift_bic`, `city`, `state`,
`county`, `country`, `postcode`, `tax_id`), rejects malformed
dates/cards/phones/SSNs, requires HTTP(S) URLs, and requires VIN checksum
validity. `project_allowed` then keeps only supported-label spans and drops
rows only when no supported span remains.

| Dataset label after transforms | Codebase placeholder | Status | Notes |
|---|---|---|---|
| `first_name` + `last_name` -> `PERSON_NAME` | `[PERSON_NAME]` | Direct | After `combine_names` |
| `email` | `[EMAIL]` | Direct | |
| `phone_number` | `[PHONE]` | Direct | US-centric phone regex |
| `credit_debit_card` | `[CARD]` | Direct | Luhn-gated |
| `ssn` | `[US_SSN]` | Direct | |
| `date` | `[DATE]` | Direct | Strict date-shape gate |
| `date_of_birth` | `[DATE]` | Direct | Same placeholder as other dates |
| `street_address` | `[STREET_ADDRESS]` | Direct | |
| `url` | `[URL]` | Direct | HTTP(S)-only gate |
| `ipv4` | `[IP]` | Direct | |
| `license_plate` | `[LICENSE_PLATE]` | Direct | OPF/training placeholder |
| `vehicle_identifier` | `[VIN]` | Direct | VIN checksum-gated |
| `password` | `[SECRET]` | Direct | |
| `api_key` | `[SECRET]` | Direct | |

## wolframko RU -> `policies/regex/ru.yaml`

wolframko rows are used after:

```bash
--transform combine_names,combine_addresses,keep_only_allowed
```

| Dataset label after transforms | Codebase placeholder | Status | Notes |
|---|---|---|---|
| `GIVENNAME` + `SURNAME` -> `PERSON_NAME` | `[PERSON_NAME]` | Direct | After `combine_names` |
| `DATEOFBIRTH` | `[DATE]` | Direct | |
| `EMAIL` | `[EMAIL]` | Direct | |
| `TELEPHONENUM` | `[PHONE]` | Direct | |
| `CREDITCARDNUMBER` | `[CARD]` | Direct | Luhn-valid enough for detector eval |
| `TAXNUM` | `[RU_INN]` | Direct | 10/12-digit INN surface |
| `SOCIALNUM` | `[RU_SNILS]` | Shape-only | SNILS checksum quality remains a caveat |
| `IDCARDNUM` | `[PASSPORTNUM]` | Direct | RU internal passport |
| `DRIVERLICENSENUM` | `[RU_DRV_LICENSE]` | Direct | OPF-only placeholder |
| `STREET` + `BUILDINGNUM` + `CITY` + `ZIPCODE` -> `STREET_ADDRESS` | `[STREET_ADDRESS]` | Direct | After `combine_addresses` |

Dropped wolframko labels:

| Dataset label | Reason |
|---|---|
| `ACCOUNTNUM` | Fake IBAN-like shape, not a real 20-digit Russian bank account |
| `USERNAME` | Not modelled as a standalone framework placeholder |
| `PASSWORD` | Kept out of the Russian third-party eval; `[SECRET]` is tested by generator/Nemotron |

## Coverage disclosure

Third-party evaluation does not cover every framework placeholder. Russian-only
structured classes such as `[RU_OGRN]`, `[RU_BIK]`, `[RU_KPP]`,
`[RU_BANK_ACCOUNT]`, `[RU_STS]`, and `[RU_OSAGO]` still require generator-only
measurement unless a better independent RU corpus is added.

The generator now emits generic `[VIN]` for RU/EN/DE. Nemotron contributes an
independent English `vehicle_identifier` surface for `[VIN]`; wolframko does
not cover VIN.
