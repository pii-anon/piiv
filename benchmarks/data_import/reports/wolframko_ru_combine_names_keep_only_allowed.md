## `combine_names` - attrition

- Rows in: **5,000**
- Rows out: **4,367** (87.3% survival)
- Dropped, only-one-kind (had GIVENNAME xor SURNAME): **595**
- Dropped, unpaired/separated names: **38**
- PERSON_NAME pairs merged: **1,504**

## `keep_only_allowed` - attrition

- Allowlist for this dataset: `BUILDINGNUM`, `CITY`, `CREDITCARDNUMBER`, `DATEOFBIRTH`, `DRIVERLICENSENUM`, `EMAIL`, `GIVENNAME`, `IDCARDNUM`, `PERSON_NAME`, `SOCIALNUM`, `STREET`, `SURNAME`, `TAXNUM`, `TELEPHONENUM`, `ZIPCODE`
- Rows in: **4,367**
- Rows out: **2,359** (54.0% survival)
- Rows dropped: **2,008**
- Dropped because of out-of-allowlist label: `USERNAME`=1036, `ACCOUNTNUM`=924, `PASSWORD`=585

# wolframko (ru) - dataset audit

Rows analyzed: **2,359**

Total spans: **7,023**

## Length distributions

### Text length (characters)

| min | p25 | p50 | p75 | p95 | max | mean |
|---|---|---|---|---|---|---|
| 57.0 | 110.0 | 126.0 | 145.0 | 173.0 | 241.0 | 128.5 |

### Text length (whitespace tokens)

| min | p25 | p50 | p75 | p95 | max | mean |
|---|---|---|---|---|---|---|
| 7.0 | 15.0 | 17.0 | 20.0 | 25.0 | 34.0 | 17.5 |

### Spans per row

| min | p25 | p50 | p75 | p95 | max | mean |
|---|---|---|---|---|---|---|
| 2.0 | 2.0 | 3.0 | 4.0 | 5.0 | 8.0 | 3.0 |

### Span length (characters)

| min | p25 | p50 | p75 | p95 | max | mean |
|---|---|---|---|---|---|---|
| 1.0 | 11.0 | 12.0 | 16.0 | 23.0 | 35.0 | 13.2 |

## Label distribution

| Label | Count | % of spans | Example value |
|---|---:|---:|---|
| `PERSON_NAME` | 1074 | 15.29 | Эрнст Сазонов |
| `TELEPHONENUM` | 750 | 10.68 | +78932528809 |
| `CITY` | 718 | 10.22 | ст. Якша |
| `EMAIL` | 680 | 9.68 | polina_1984@example.net |
| `STREET` | 537 | 7.65 | ул. Кирпичная |
| `DATEOFBIRTH` | 504 | 7.18 | 19/03/1976 |
| `BUILDINGNUM` | 489 | 6.96 | 131 |
| `TAXNUM` | 487 | 6.93 | 318732549912 |
| `IDCARDNUM` | 476 | 6.78 | 29 37 900581 |
| `SOCIALNUM` | 409 | 5.82 | 192-832-764 83 |
| `ZIPCODE` | 330 | 4.70 | 473829 |
| `CREDITCARDNUMBER` | 300 | 4.27 | 4226916697848015 |
| `DRIVERLICENSENUM` | 269 | 3.83 | 78 25 496922 |

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

**id**: `wolframko-ru-3290`  •  **spans**: 8

```
Заявление о регистрации брака: жених Степан Ситников, дата рождения 04/05/1976, ИНН 474326806582; невеста Семен Брагина, телефон +7 189 779 5014; адрес: с. Балашиха, ул. бул. Курский, д. 8/3.
```

  - `PERSON_NAME` [37:52] = `Степан Ситников`
  - `DATEOFBIRTH` [68:78] = `04/05/1976`
  - `TAXNUM` [84:96] = `474326806582`
  - `PERSON_NAME` [106:119] = `Семен Брагина`
  - `TELEPHONENUM` [129:144] = `+7 189 779 5014`
  - `CITY` [153:164] = `с. Балашиха`
  - `STREET` [170:182] = `бул. Курский`
  - `BUILDINGNUM` [187:190] = `8/3`

## Random samples

**id**: `wolframko-ru-2`  •  **spans**: 2

```
В договоре указана дата рождения арендатора: 19/03/1976 и номер паспорта 29 37 900581.
```

  - `DATEOFBIRTH` [45:55] = `19/03/1976`
  - `IDCARDNUM` [73:85] = `29 37 900581`

**id**: `wolframko-ru-489`  •  **spans**: 2

```
Для получения баллов лояльности укажите номер водительского удостоверения 17 27 643878 и дату рождения 15.12.1951.
```

  - `DRIVERLICENSENUM` [74:86] = `17 27 643878`
  - `DATEOFBIRTH` [103:113] = `15.12.1951`

**id**: `wolframko-ru-904`  •  **spans**: 3

```
Прошу выдать справку о статусе пенсионера: ФИО Андроник Королева, СНИЛС 099-353-875 84, дата рождения 20.11.1977.
```

  - `PERSON_NAME` [47:64] = `Андроник Королева`
  - `SOCIALNUM` [72:86] = `099-353-875 84`
  - `DATEOFBIRTH` [102:112] = `20.11.1977`

**id**: `wolframko-ru-1303`  •  **spans**: 3

```
Уважаемый Светлана Туров, ваш заказ #12345 отправлен в ст. Токсово. Ожидаемый срок доставки — 2 дня, уточнить можно по телефону +7 898 126 5742.
```

  - `PERSON_NAME` [10:24] = `Светлана Туров`
  - `CITY` [55:66] = `ст. Токсово`
  - `TELEPHONENUM` [128:143] = `+7 898 126 5742`

**id**: `wolframko-ru-1645`  •  **spans**: 2

```
Курьер с СНИЛС 108-220-781 13 позвонил вам по номеру +7 414 474 3281 и запросил подтверждение доставки.
```

  - `SOCIALNUM` [15:29] = `108-220-781 13`
  - `TELEPHONENUM` [53:68] = `+7 414 474 3281`

