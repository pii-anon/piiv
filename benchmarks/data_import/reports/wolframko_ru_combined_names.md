## `combine_names` transform - attrition

- Rows in: **5,000**
- Rows out: **4,367** (87.3% survival)
- Dropped, only-one-kind (had GIVENNAME xor SURNAME): **595**
- Dropped, unpaired/separated names: **38**
- PERSON_NAME pairs merged: **1,504**

# wolframko (ru) - dataset audit

Rows analyzed: **4,367**

Total spans: **12,558**

## Length distributions

### Text length (characters)

| min | p25 | p50 | p75 | p95 | max | mean |
|---|---|---|---|---|---|---|
| 57.0 | 113.0 | 130.0 | 149.0 | 179.7 | 263.0 | 131.9 |

### Text length (whitespace tokens)

| min | p25 | p50 | p75 | p95 | max | mean |
|---|---|---|---|---|---|---|
| 7.0 | 14.0 | 17.0 | 20.0 | 24.0 | 34.0 | 17.2 |

### Spans per row

| min | p25 | p50 | p75 | p95 | max | mean |
|---|---|---|---|---|---|---|
| 2.0 | 2.0 | 3.0 | 3.0 | 5.0 | 8.0 | 2.9 |

### Span length (characters)

| min | p25 | p50 | p75 | p95 | max | mean |
|---|---|---|---|---|---|---|
| 1.0 | 11.0 | 14.0 | 16.0 | 23.0 | 37.0 | 14.0 |

## Label distribution

| Label | Count | % of spans | Example value |
|---|---:|---:|---|
| `PERSON_NAME` | 1504 | 11.98 | Гремислав Гришин |
| `TELEPHONENUM` | 1215 | 9.68 | 8 (849) 696-5328 |
| `EMAIL` | 1192 | 9.49 | gavrila1984@example.org |
| `USERNAME` | 1036 | 8.25 | sigizmundafanasev |
| `CITY` | 949 | 7.56 | д. Костомукша |
| `ACCOUNTNUM` | 924 | 7.36 | RU45FOMI8350305641395 |
| `TAXNUM` | 804 | 6.40 | 711305304603 |
| `STREET` | 676 | 5.38 | наб. Санаторная |
| `DATEOFBIRTH` | 655 | 5.22 | 19/03/1976 |
| `BUILDINGNUM` | 608 | 4.84 | 2 |
| `IDCARDNUM` | 590 | 4.70 | 29 37 900581 |
| `PASSWORD` | 585 | 4.66 | uS9zneU2&78AF6ly |
| `SOCIALNUM` | 543 | 4.32 | 192-832-764 83 |
| `CREDITCARDNUMBER` | 517 | 4.12 | 4226916697848015 |
| `ZIPCODE` | 423 | 3.37 | 473829 |
| `DRIVERLICENSENUM` | 337 | 2.68 | 78 25 496922 |

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

**id**: `wolframko-ru-0`  •  **spans**: 5

```
Уважаемый Гремислав Гришин, прошу подтвердить аренду квартиры по адресу: ул. наб. Санаторная, д. 2, д. Костомукша. Для оплаты переведите средства на счёт RU45FOMI8350305641395.
```

  - `PERSON_NAME` [10:26] = `Гремислав Гришин`
  - `STREET` [77:92] = `наб. Санаторная`
  - `BUILDINGNUM` [97:98] = `2`
  - `CITY` [100:113] = `д. Костомукша`
  - `ACCOUNTNUM` [154:175] = `RU45FOMI8350305641395`

**id**: `wolframko-ru-228`  •  **spans**: 3

```
В письме к управлению социальных услуг прошу перевести пособие на карту 340030756220865. Данные получателя: Захар Носков. Телефон для связи: +7 (654) 195-1802.
```

  - `CREDITCARDNUMBER` [72:87] = `340030756220865`
  - `PERSON_NAME` [108:120] = `Захар Носков`
  - `TELEPHONENUM` [141:158] = `+7 (654) 195-1802`

**id**: `wolframko-ru-469`  •  **spans**: 3

```
Для подтверждения личности укажите ФИО Кондрат Симонова, СНИЛС 974-801-624 56 и номер водительского удостоверения 56 15 520040.
```

  - `PERSON_NAME` [39:55] = `Кондрат Симонова`
  - `SOCIALNUM` [63:77] = `974-801-624 56`
  - `DRIVERLICENSENUM` [114:126] = `56 15 520040`

**id**: `wolframko-ru-690`  •  **spans**: 3

```
В системе обнаружена несовпадение ИНН 060420879671 и даты рождения 1957-08-02 у пользователя poljakovkallistrat; уточните данные.
```

  - `TAXNUM` [38:50] = `060420879671`
  - `DATEOFBIRTH` [67:77] = `1957-08-02`
  - `USERNAME` [93:111] = `poljakovkallistrat`

**id**: `wolframko-ru-924`  •  **spans**: 2

```
Уведомление о возврате налога на доходы: ваш ИНН 238415875866 и банковский счёт RU10LUXS5724461767929. Срок перевода – 10 дней.
```

  - `TAXNUM` [49:61] = `238415875866`
  - `ACCOUNTNUM` [80:101] = `RU10LUXS5724461767929`

