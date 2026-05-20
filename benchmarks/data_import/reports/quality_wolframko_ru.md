# Quality scan - wolframko_ru

- Rows scanned: **10,000**
- Rows with at least one quality issue: **3,907** (39.1%)

## Per-label quality

| Label | Spans | Anchor rate | Format pass | Format fails | Junk |
|---|---:|---:|---:|---|---:|
| `ACCOUNTNUM` | 2055 | 95.8% | n/a | — | 0 |
| `BUILDINGNUM` | 1412 | n/a | n/a | — | 316 |
| `CITY` | 2211 | 78.0% | n/a | — | 0 |
| `CREDITCARDNUMBER` | 1138 | n/a | 100.0% | — | 0 |
| `DATEOFBIRTH` | 1500 | 57.3% | 100.0% | — | 0 |
| `DRIVERLICENSENUM` | 797 | 93.6% | 100.0% | — | 0 |
| `EMAIL` | 2667 | n/a | 100.0% | — | 0 |
| `GIVENNAME` | 4121 | n/a | n/a | — | 0 |
| `IDCARDNUM` | 1273 | 93.2% | 100.0% | — | 0 |
| `PASSWORD` | 1243 | 86.4% | n/a | — | 0 |
| `SOCIALNUM` | 1250 | 95.9% | 1.7% | `snils_checksum_fail`=1229 | 0 |
| `STREET` | 1574 | 92.2% | n/a | — | 0 |
| `SURNAME` | 3409 | n/a | n/a | — | 0 |
| `TAXNUM` | 1750 | 99.1% | 100.0% | — | 0 |
| `TELEPHONENUM` | 2747 | 86.7% | n/a | — | 0 |
| `USERNAME` | 2125 | 63.8% | n/a | — | 0 |
| `ZIPCODE` | 1006 | 72.4% | n/a | — | 0 |

## Sample anchor failures (first 5 per label)

### `ACCOUNTNUM`  (87 / 2055 no-anchor)
- `wolframko-ru-109` value=`RU35MUZK2816850542357`  context: `подписать кредитный договор на сумму до RU35MUZK2816850542357.`
- `wolframko-ru-240` value=`RU37IOEB9993476870146`  context: `. 40 лет Октября, д. 52. Номер договора RU37IOEB9993476870146.`
- `wolframko-ru-801` value=`RU56DOVO2256053134026`  context: `у необходимо перечислить аренду на ИБАН RU56DOVO2256053134026; подтверждение оплаты будет отправлено `
- `wolframko-ru-967` value=`RU71LEMW8341559991015`  context: `афа: сумма — 5000 ₽, платёжный реквизит RU71LEMW8341559991015, а ваш контактный номер 8 (676) 472-29-`
- `wolframko-ru-979` value=`RU86ZQKG8003296334727`  context: `Ваша заявка №RU86ZQKG8003296334727 отклонена. Для уточнения причин свяжите`

### `CITY`  (486 / 2211 no-anchor)
- `wolframko-ru-29` value=`к. Рыбинск`  context: `Уважаемый Жанна Суворова, ваш билет из к. Рыбинск содержит ошибку в индексе: 595148. Пожа`
- `wolframko-ru-110` value=`п. Буйнакск`  context: ` Савельев, СНИЛС 577-738-721 48, адрес: п. Буйнакск, 188805, уполномочил kirillovnazar полу`
- `wolframko-ru-126` value=`к. Сасово`  context: `Для получения груза в к. Сасово вам понадобится предъявить документ 46 `
- `wolframko-ru-136` value=`клх Махачкала`  context: `Доставка в пункт самовывоза клх Махачкала: уточните индекс 364710 и укажите конта`
- `wolframko-ru-158` value=`клх Кировск (Мурм.)`  context: ` Пожалуйста, подтвердите текущий адрес: клх Кировск (Мурм.), ул. ул. Сиреневая. Для связи используй`

### `DATEOFBIRTH`  (641 / 1500 no-anchor)
- `wolframko-ru-8` value=`16.11.2005`  context: `т Сазонов требует указать дату рождения 16.11.2005 и номер банковской карты 34465787133150`
- `wolframko-ru-14` value=`2003-06-30`  context: `ртиры необходима запись о дате рождения 2003-06-30 и номер телефона 8 (468) 723-43-09.`
- `wolframko-ru-19` value=`31.10.1961`  context: `ти арендатора запрашиваем дату рождения 31.10.1961 и логин в системе arhip_35.`
- `wolframko-ru-23` value=`21.02.1987`  context: ` Пожалуйста, подтвердите дату рождения: 21.02.1987 и ваш контактный номер 8 869 232 2602.`
- `wolframko-ru-39` value=`1972-11-01`  context: `ефона 8 (277) 434-87-34 и дату рождения 1972-11-01 для подтверждения возраста.`

### `DRIVERLICENSENUM`  (51 / 797 no-anchor)
- `wolframko-ru-47` value=`90 17 340062`  context: `а на подключение услуги Интернет‑пакет №90 17 340062 успешно принята. Ожидайте звонка от наш`
- `wolframko-ru-121` value=`41 25 578634`  context: `доставку осуществит водитель с правами №41 25 578634.`
- `wolframko-ru-131` value=`87 38 611945`  context: `тель Филипп Зиновьев с номером лицензии 87 38 611945 будет у вас в течение 3 часов, звоните `
- `wolframko-ru-934` value=`55 34 272892`  context: `0797, дата рождения 11/04/1970, подпись 55 34 272892.`
- `wolframko-ru-977` value=`92 30 630126`  context: `редстоящем ТО: ваш автомобиль с номером 92 30 630126 необходимо принести в сервис по адресу `

### `IDCARDNUM`  (87 / 1273 no-anchor)
- `wolframko-ru-43` value=`85 38 107540`  context: `дравствуйте, Роман Громов. Ваш договор №85 38 107540 требует подписания; отправьте скан по а`
- `wolframko-ru-126` value=`46 40 384913`  context: `ово вам понадобится предъявить документ 46 40 384913 и подтвердить ИНН 107414438468 получате`
- `wolframko-ru-251` value=`94 60 387813`  context: `, индекс 411526. Приходите с документом 94 60 387813.`
- `wolframko-ru-297` value=`51 58 726410`  context: `в отделение в г. Приозерск с документом 51 58 726410 и указанным номером телефона 8 (014) 50`
- `wolframko-ru-390` value=`67 75 254506`  context: `рацию, отправив фотографию с документом 67 75 254506 и номер водительского удостоверения 65 `

### `PASSWORD`  (169 / 1243 no-anchor)
- `wolframko-ru-74` value=`i!rPRDOK$oYqBV`  context: `3878282548 и подтвердите запрос паролем i!rPRDOK$oYqBV.`
- `wolframko-ru-147` value=`$O@A$nP6`  context: `енность подтверждена подписью и паролем $O@A$nP6 от Геннадий Фролова.`
- `wolframko-ru-346` value=`uC^m%GWzEhECf8`  context: ` хранится в системе, защищённый паролем uC^m%GWzEhECf8. Платёж выполнен со счёта RU55UAXX41379`
- `wolframko-ru-347` value=`Y55qknQ1Tm2I0`  context: `т через профиль efremovsokrat с паролем Y55qknQ1Tm2I0. Укажите ваш налоговый идентификатор 34`
- `wolframko-ru-423` value=`MwfUvQDWyc`  context: `ароль для доступа к сервисному порталу: MwfUvQDWyc. При возникновении вопросов звоните по `

### `SOCIALNUM`  (51 / 1250 no-anchor)
- `wolframko-ru-130` value=`096-705-466 88`  context: `ля 1967-11-11 и номер страхового полиса 096-705-466 88 для оформления доставки.`
- `wolframko-ru-266` value=`842-474-517 12`  context: ` 56 656639 и справку о страховом номере 842-474-517 12.`
- `wolframko-ru-355` value=`793-597-820 71`  context: `ия 15.04.1977 и номер страхового полиса 793-597-820 71. Оплата будет списана с банковского счё`
- `wolframko-ru-510` value=`620-672-400 49`  context: `в, прошу перенести мой социальный номер 620-672-400 49 в новый реестр, контактный email vsemil`
- `wolframko-ru-524` value=`332-727-956 87`  context: `ва оформил направление с номером полиса 332-727-956 87.`

### `STREET`  (123 / 1574 no-anchor)
- `wolframko-ru-26` value=`алл. Маркса`  context: `Отель в районе алл. Маркса ждёт вашего заселения, оплата возможна `
- `wolframko-ru-91` value=`ш. Больничное`  context: `из ст. Ревда (Сверд.); адрес получения: ш. Больничное д. 5, индекс 198327.`
- `wolframko-ru-98` value=`ш. Ореховое`  context: `2, проживающему по адресу: ст. Джейрах, ш. Ореховое д. 6.`
- `wolframko-ru-773` value=`алл. Интернациональная`  context: ` паспорта 35 27 917823 и укажите адрес: алл. Интернациональная, 785, 630136.`
- `wolframko-ru-804` value=`алл. Учительская`  context: `ова, ИНН 657918999002, адрес проживания алл. Учительская, г. Дагомыс.`

### `TAXNUM`  (15 / 1750 no-anchor)
- `wolframko-ru-1070` value=`427258717416`  context: `Ваш идентификационный номер: 427258717416. Пожалуйста, пришлите копию паспорта 60`
- `wolframko-ru-2018` value=`119477238888`  context: `6340918580558 и номер налогоплательщика 119477238888 для выставления счета.`
- `wolframko-ru-2217` value=`570241463317`  context: `v@example.net с указанием номера полиса 570241463317.`
- `wolframko-ru-2223` value=`489890929000`  context: `4) 901-3249 и назовите ваш номер полиса 489890929000.`
- `wolframko-ru-2231` value=`052093174186`  context: `ртный номер 12 96 243910 и номер полиса 052093174186.`

### `TELEPHONENUM`  (364 / 2747 no-anchor)
- `wolframko-ru-45` value=`82327193745`  context: `твердите согласие отправив SMS на номер 82327193745.`
- `wolframko-ru-53` value=`+7 367 837 77 01`  context: `менить подписку, отправьте сообщение на +7 367 837 77 01.`
- `wolframko-ru-57` value=`+7 (710) 947-77-52`  context: `с номера был одобрен. Новый номер будет +7 (710) 947-77-52. Подтвердите согласие, отправив SMS с к`
- `wolframko-ru-62` value=`89049027874`  context: `aelizaveta@example.net и в SMS на номер 89049027874.`
- `wolframko-ru-70` value=`+75562386922`  context: `а email alekse05@example.org и в SMS на +75562386922.`

### `USERNAME`  (769 / 2125 no-anchor)
- `wolframko-ru-1` value=`sigizmundafanasev`  context: `Контактное лицо по договору аренды: sigizmundafanasev (email: gavrila1984@example.org, телефо`
- `wolframko-ru-44` value=`radovanbolshakov`  context: `Ваш профиль radovanbolshakov был обновлён. Для подтверждения изменен`
- `wolframko-ru-48` value=`kapustinilja`  context: `Привет, kapustinilja! Не забудьте оплатить очередной счёт в `
- `wolframko-ru-49` value=`ljubomir31`  context: `мости измените данные в личном кабинете ljubomir31.`
- `wolframko-ru-52` value=`fedor08`  context: `дите пароль JtHLY9OrH на странице входа fedor08.`

### `ZIPCODE`  (278 / 1006 no-anchor)
- `wolframko-ru-103` value=`177449`  context: `95 528231, адрес: пр. Энергетиков д. 3, 177449 – полномочие на получение почтовых отпр`
- `wolframko-ru-110` value=`188805`  context: `ИЛС 577-738-721 48, адрес: п. Буйнакск, 188805, уполномочил kirillovnazar получать спр`
- `wolframko-ru-113` value=`361530`  context: `0-379 17, адрес: пр. Тимирязева д. 760, 361530, уполномочил valerjan_52 подписать дого`
- `wolframko-ru-161` value=`315274`  context: `ебуется подтверждение места проживания: 315274 г. Нарьян-Мар. Сведения отправьте на fe`
- `wolframko-ru-177` value=`688263`  context: ` Ваш ИНН 600858970570 привязан к адресу 688263 п. Набережные Челны. При необходимости `

## Sample format failures

### `SOCIALNUM`  (1229 fails)
- `wolframko-ru-4` value=`511-615-594 07`  reason=`snils_checksum_fail`
- `wolframko-ru-11` value=`192-832-764 83`  reason=`snils_checksum_fail`
- `wolframko-ru-18` value=`413-953-767 24`  reason=`snils_checksum_fail`
- `wolframko-ru-25` value=`653-287-101 22`  reason=`snils_checksum_fail`
- `wolframko-ru-33` value=`932-528-809 57`  reason=`snils_checksum_fail`

## Same-row format collisions

Two labels in the same row carrying values of identical (length, charclass).
Forces context-only disambiguation.

| Label pair | Same-row collisions |
|---|---:|
| `GIVENNAME` ↔ `SURNAME` | 512 |
| `CITY` ↔ `STREET` | 105 |
| `DRIVERLICENSENUM` ↔ `IDCARDNUM` | 74 |
| `SOCIALNUM` ↔ `TELEPHONENUM` | 19 |
| `IDCARDNUM` ↔ `TELEPHONENUM` | 11 |
| `DRIVERLICENSENUM` ↔ `TELEPHONENUM` | 9 |
| `PASSWORD` ↔ `USERNAME` | 1 |
| `PASSWORD` ↔ `SURNAME` | 1 |
| `CITY` ↔ `PASSWORD` | 1 |

