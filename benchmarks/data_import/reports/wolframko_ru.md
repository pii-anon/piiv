# wolframko (ru) - dataset audit

Rows analyzed: **5,000**

Total spans: **16,161**

## Length distributions

### Text length (characters)

| min | p25 | p50 | p75 | p95 | max | mean |
|---|---|---|---|---|---|---|
| 41.0 | 112.0 | 129.0 | 149.0 | 180.0 | 263.0 | 131.6 |

### Text length (whitespace tokens)

| min | p25 | p50 | p75 | p95 | max | mean |
|---|---|---|---|---|---|---|
| 6.0 | 14.0 | 17.0 | 20.0 | 24.0 | 37.0 | 17.2 |

### Spans per row

| min | p25 | p50 | p75 | p95 | max | mean |
|---|---|---|---|---|---|---|
| 2.0 | 2.0 | 3.0 | 4.0 | 5.0 | 10.0 | 3.2 |

### Span length (characters)

| min | p25 | p50 | p75 | p95 | max | mean |
|---|---|---|---|---|---|---|
| 1.0 | 8.0 | 12.0 | 16.0 | 23.0 | 37.0 | 12.2 |

## Label distribution

| Label | Count | % of spans | Example value |
|---|---:|---:|---|
| `GIVENNAME` | 2016 | 12.47 | Гремислав |
| `SURNAME` | 1664 | 10.30 | Гришин |
| `TELEPHONENUM` | 1382 | 8.55 | 8 (849) 696-5328 |
| `EMAIL` | 1346 | 8.33 | gavrila1984@example.org |
| `CITY` | 1100 | 6.81 | д. Костомукша |
| `USERNAME` | 1077 | 6.66 | sigizmundafanasev |
| `ACCOUNTNUM` | 1057 | 6.54 | RU45FOMI8350305641395 |
| `TAXNUM` | 901 | 5.58 | 659818733147 |
| `STREET` | 780 | 4.83 | наб. Санаторная |
| `DATEOFBIRTH` | 743 | 4.60 | 19/03/1976 |
| `BUILDINGNUM` | 703 | 4.35 | 2 |
| `IDCARDNUM` | 646 | 4.00 | 29 37 900581 |
| `PASSWORD` | 633 | 3.92 | uS9zneU2&78AF6ly |
| `SOCIALNUM` | 628 | 3.89 | 511-615-594 07 |
| `CREDITCARDNUMBER` | 577 | 3.57 | 4226916697848015 |
| `ZIPCODE` | 510 | 3.16 | 462704 |
| `DRIVERLICENSENUM` | 398 | 2.46 | 78 25 496922 |

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

**id**: `wolframko-ru-3290`  •  **spans**: 10

```
Заявление о регистрации брака: жених Степан Ситников, дата рождения 04/05/1976, ИНН 474326806582; невеста Семен Брагина, телефон +7 189 779 5014; адрес: с. Балашиха, ул. бул. Курский, д. 8/3.
```

  - `GIVENNAME` [37:43] = `Степан`
  - `SURNAME` [44:52] = `Ситников`
  - `DATEOFBIRTH` [68:78] = `04/05/1976`
  - `TAXNUM` [84:96] = `474326806582`
  - `GIVENNAME` [106:111] = `Семен`
  - `SURNAME` [112:119] = `Брагина`
  - `TELEPHONENUM` [129:144] = `+7 189 779 5014`
  - `CITY` [153:164] = `с. Балашиха`
  - `STREET` [170:182] = `бул. Курский`
  - `BUILDINGNUM` [187:190] = `8/3`

## Random samples

**id**: `wolframko-ru-0`  •  **spans**: 6

```
Уважаемый Гремислав Гришин, прошу подтвердить аренду квартиры по адресу: ул. наб. Санаторная, д. 2, д. Костомукша. Для оплаты переведите средства на счёт RU45FOMI8350305641395.
```

  - `GIVENNAME` [10:19] = `Гремислав`
  - `SURNAME` [20:26] = `Гришин`
  - `STREET` [77:92] = `наб. Санаторная`
  - `BUILDINGNUM` [97:98] = `2`
  - `CITY` [100:113] = `д. Костомукша`
  - `ACCOUNTNUM` [154:175] = `RU45FOMI8350305641395`

**id**: `wolframko-ru-199`  •  **spans**: 5

```
Уважаемый клиент gtarasova, ваш полис будет отправлен по адресу: ул. ш. Правды д. 258, ст. Кош-Агач. При необходимости уточнений звоните по телефону 8 290 965 6101.
```

  - `USERNAME` [17:26] = `gtarasova`
  - `STREET` [69:78] = `ш. Правды`
  - `BUILDINGNUM` [82:85] = `258`
  - `CITY` [87:99] = `ст. Кош-Агач`
  - `TELEPHONENUM` [149:163] = `8 290 965 6101`

**id**: `wolframko-ru-398`  •  **spans**: 3

```
Уважаемый Клавдия Белова, просим оплатить начисления за ЖКХ через банковский счёт RU44ZDEP3585730652407 до 15 числа текущего месяца.
```

  - `GIVENNAME` [10:17] = `Клавдия`
  - `SURNAME` [18:24] = `Белова`
  - `ACCOUNTNUM` [82:103] = `RU44ZDEP3585730652407`

**id**: `wolframko-ru-597`  •  **spans**: 4

```
Благодарим за отклик, Николай! Ваша информация: дата рождения 31.05.1987, ИНН 177204312329, email osipovdavid@example.net.
```

  - `GIVENNAME` [22:29] = `Николай`
  - `DATEOFBIRTH` [62:72] = `31.05.1987`
  - `TAXNUM` [78:90] = `177204312329`
  - `EMAIL` [98:121] = `osipovdavid@example.net`

**id**: `wolframko-ru-796`  •  **spans**: 4

```
В профиле указаны: имя Всеволод, фамилия Зайцева, город г. Ребриха, пароль n9KS43*2zMH@JB.
```

  - `GIVENNAME` [23:31] = `Всеволод`
  - `SURNAME` [41:48] = `Зайцева`
  - `CITY` [56:66] = `г. Ребриха`
  - `PASSWORD` [75:89] = `n9KS43*2zMH@JB`

