## `combine_names` - attrition

- Rows in: **1,000**
- Rows out: **867** (86.7% survival)
- Dropped, only-one-kind (had GIVENNAME xor SURNAME): **130**
- Dropped, unpaired/separated names: **3**
- PERSON_NAME pairs merged: **299**

## `combine_addresses` - attrition

- Rows in: **867**
- Rows out: **866** (99.9% survival)
- Dropped, scattered (multiple address clusters): **1**
- Pass-through, no address components: **638**
- Addresses merged: **228**

## `keep_only_allowed` - attrition

- Allowlist for this dataset: `BUILDINGNUM`, `CITY`, `CREDITCARDNUMBER`, `DATEOFBIRTH`, `DRIVERLICENSENUM`, `EMAIL`, `GIVENNAME`, `IDCARDNUM`, `PERSON_NAME`, `SOCIALNUM`, `STREET`, `STREET_ADDRESS`, `SURNAME`, `TAXNUM`, `TELEPHONENUM`, `ZIPCODE`
- Rows in: **866**
- Rows out: **452** (52.2% survival)
- Rows dropped: **414**
- Dropped because of out-of-allowlist label: `USERNAME`=232, `ACCOUNTNUM`=183, `PASSWORD`=122

# wolframko (ru) - dataset audit

Rows analyzed: **452**

Total spans: **1,125**

## Length distributions

### Text length (characters)

| min | p25 | p50 | p75 | p95 | max | mean |
|---|---|---|---|---|---|---|
| 58.0 | 114.0 | 129.0 | 145.2 | 170.4 | 234.0 | 130.2 |

### Text length (whitespace tokens)

| min | p25 | p50 | p75 | p95 | max | mean |
|---|---|---|---|---|---|---|
| 8.0 | 15.0 | 17.0 | 20.0 | 24.0 | 29.0 | 17.7 |

### Spans per row

| min | p25 | p50 | p75 | p95 | max | mean |
|---|---|---|---|---|---|---|
| 1.0 | 2.0 | 2.0 | 3.0 | 4.0 | 4.0 | 2.5 |

### Span length (characters)

| min | p25 | p50 | p75 | p95 | max | mean |
|---|---|---|---|---|---|---|
| 6.0 | 12.0 | 14.0 | 18.0 | 36.8 | 118.0 | 17.2 |

## Label distribution

| Label | Count | % of spans | Example value |
|---|---:|---:|---|
| `PERSON_NAME` | 209 | 18.58 | Эрнст Сазонов |
| `STREET_ADDRESS` | 166 | 14.76 | ст. Якша |
| `TELEPHONENUM` | 146 | 12.98 | +78932528809 |
| `EMAIL` | 129 | 11.47 | polina_1984@example.net |
| `TAXNUM` | 100 | 8.89 | 318732549912 |
| `DATEOFBIRTH` | 98 | 8.71 | 19/03/1976 |
| `IDCARDNUM` | 89 | 7.91 | 29 37 900581 |
| `SOCIALNUM` | 80 | 7.11 | 192-832-764 83 |
| `CREDITCARDNUMBER` | 57 | 5.07 | 4226916697848015 |
| `DRIVERLICENSENUM` | 51 | 4.53 | 78 25 496922 |

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

**id**: `wolframko-ru-98`  •  **spans**: 4

```
Настоящая доверенность выдана Аверьян Исаков, дата рождения 1964-02-11, паспорт 34 42 146542, проживающему по адресу: ст. Джейрах, ш. Ореховое д. 6.
```

  - `PERSON_NAME` [30:44] = `Аверьян Исаков`
  - `DATEOFBIRTH` [60:70] = `1964-02-11`
  - `IDCARDNUM` [80:92] = `34 42 146542`
  - `STREET_ADDRESS` [118:147] = `ст. Джейрах, ш. Ореховое д. 6`

## Random samples

**id**: `wolframko-ru-2`  •  **spans**: 2

```
В договоре указана дата рождения арендатора: 19/03/1976 и номер паспорта 29 37 900581.
```

  - `DATEOFBIRTH` [45:55] = `19/03/1976`
  - `IDCARDNUM` [73:85] = `29 37 900581`

**id**: `wolframko-ru-490`  •  **spans**: 1

```
Товар будет отправлен на адрес: пер. Автомобилистов д. 29, клх Кропоткин (Краснод.). Укажите ваш почтовый индекс 011947 для ускорения обработки.
```

  - `STREET_ADDRESS` [32:119] = `пер. Автомобилистов д. 29, клх Кропоткин (Красн...`

**id**: `wolframko-ru-905`  •  **spans**: 2

```
Заявление в муниципальный центр: Мефодий Шубина, адрес проживания: ул. пер. Красногвардейский д. 8/6, г. Алапаевск, индекс 272849.
```

  - `PERSON_NAME` [33:47] = `Мефодий Шубина`
  - `STREET_ADDRESS` [71:129] = `пер. Красногвардейский д. 8/6, г. Алапаевск, ин...`

