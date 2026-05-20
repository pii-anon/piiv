# Imported-dataset eval - nemotron_en

- Rows evaluated: **200**
- Rows with zero gold spans (after label-map filter): **0**
- Elapsed: **8.2s** (41ms/row)
- Projection-symmetric scoring: **on** (gold placeholder space: `[CARD], [DATE], [EMAIL], [IP], [LICENSE_PLATE], [PERSONAL_ID], [PERSON_NAME], [PHONE], [SECRET], [STREET_ADDRESS], [URL], [VIN]`)

## Per-placeholder precision / recall

| Placeholder | Precision (95% CI) | Recall (95% CI) | F1 (95% CI) | TP | FP | FN | Support |
|---|---|---|---|---:|---:|---:|---:|
| `[CARD]` | 0.857 [0.500, 1.000] | 1.000 [1.000, 1.000] | 0.923 [0.667, 1.000] | 6 | 1 | 0 | 6 |
| `[DATE]` | 0.545 [0.475, 0.601] | 1.000 [1.000, 1.000] | 0.705 [0.644, 0.751] | 164 | 137 | 0 | 164 |
| `[EMAIL]` | 1.000 [1.000, 1.000] | 1.000 [1.000, 1.000] | 1.000 [1.000, 1.000] | 73 | 0 | 0 | 73 |
| `[IP]` | 0.694 [0.593, 0.796] | 0.971 [0.905, 1.000] | 0.810 [0.730, 0.884] | 34 | 15 | 1 | 35 |
| `[LICENSE_PLATE]` | 1.000 [0.000, 1.000] | 0.667 [0.000, 1.000] | 0.800 [0.000, 1.000] | 2 | 0 | 1 | 3 |
| `[PERSONAL_ID]` | 0.727 [0.429, 1.000] | 1.000 [1.000, 1.000] | 0.842 [0.600, 1.000] | 8 | 3 | 0 | 8 |
| `[PERSON_NAME]` | 0.680 [0.573, 0.779] | 0.966 [0.910, 1.000] | 0.798 [0.718, 0.867] | 85 | 40 | 3 | 88 |
| `[PHONE]` | 0.434 [0.308, 0.565] | 1.000 [1.000, 1.000] | 0.605 [0.471, 0.722] | 49 | 64 | 0 | 49 |
| `[SECRET]` | 0.000 [0.000, 0.000] | 0.000 [0.000, 0.000] | 0.000 [0.000, 0.000] | 0 | 0 | 49 | 49 |
| `[STREET_ADDRESS]` | 0.053 [0.000, 0.191] | 0.071 [0.000, 0.250] | 0.061 [0.000, 0.194] | 1 | 18 | 13 | 14 |
| `[URL]` | 0.872 [0.790, 0.949] | 1.000 [1.000, 1.000] | 0.932 [0.883, 0.974] | 116 | 17 | 0 | 116 |
| **macro** | 0.624 [0.515, 0.663] | 0.789 [0.722, 0.830] | 0.697 [0.604, 0.730] | 538 | 295 | 67 | 605 |
| **micro** | 0.646 [0.609, 0.688] | 0.889 [0.858, 0.918] | 0.748 [0.720, 0.778] | 538 | 295 | 67 | 605 |

## Per-length-bucket precision / recall

Row distribution across buckets: `sentence`: 75, `paragraph`: 4, `multi_paragraph`: 71, `structured`: 50

### `sentence` (75 rows)

| Placeholder | Precision (95% CI) | Recall (95% CI) | F1 (95% CI) | TP | FP | FN | Support |
|---|---|---|---|---:|---:|---:|---:|
| `[CARD]` | 1.000 [0.000, 1.000] | 1.000 [0.000, 1.000] | 1.000 [0.000, 1.000] | 1 | 0 | 0 | 1 |
| `[DATE]` | 0.569 [0.468, 0.676] | 1.000 [1.000, 1.000] | 0.726 [0.637, 0.806] | 41 | 31 | 0 | 41 |
| `[EMAIL]` | 1.000 [1.000, 1.000] | 1.000 [1.000, 1.000] | 1.000 [1.000, 1.000] | 21 | 0 | 0 | 21 |
| `[IP]` | 0.550 [0.500, 0.647] | 1.000 [1.000, 1.000] | 0.710 [0.667, 0.786] | 11 | 9 | 0 | 11 |
| `[LICENSE_PLATE]` | 1.000 [0.000, 1.000] | 1.000 [0.000, 1.000] | 1.000 [0.000, 1.000] | 2 | 0 | 0 | 2 |
| `[PERSONAL_ID]` | 0.571 [0.181, 1.000] | 1.000 [1.000, 1.000] | 0.727 [0.307, 1.000] | 4 | 3 | 0 | 4 |
| `[PERSON_NAME]` | 0.837 [0.707, 0.939] | 1.000 [1.000, 1.000] | 0.911 [0.829, 0.968] | 36 | 7 | 0 | 36 |
| `[PHONE]` | 0.353 [0.200, 0.516] | 1.000 [1.000, 1.000] | 0.522 [0.333, 0.681] | 12 | 22 | 0 | 12 |
| `[SECRET]` | 0.000 [0.000, 0.000] | 0.000 [0.000, 0.000] | 0.000 [0.000, 0.000] | 0 | 0 | 18 | 18 |
| `[STREET_ADDRESS]` | 0.000 [0.000, 0.000] | 0.000 [0.000, 0.000] | 0.000 [0.000, 0.000] | 0 | 6 | 7 | 7 |
| `[URL]` | 0.925 [0.842, 1.000] | 1.000 [1.000, 1.000] | 0.961 [0.914, 1.000] | 37 | 3 | 0 | 37 |
| **macro** | 0.619 [0.436, 0.652] | 0.818 [0.636, 0.818] | 0.705 [0.517, 0.726] | 165 | 81 | 25 | 190 |
| **micro** | 0.671 [0.608, 0.733] | 0.868 [0.815, 0.917] | 0.757 [0.707, 0.805] | 165 | 81 | 25 | 190 |

### `paragraph` (4 rows)

| Placeholder | Precision (95% CI) | Recall (95% CI) | F1 (95% CI) | TP | FP | FN | Support |
|---|---|---|---|---:|---:|---:|---:|
| `[DATE]` | 0.500 [0.000, 1.000] | 1.000 [0.000, 1.000] | 0.667 [0.000, 1.000] | 2 | 2 | 0 | 2 |
| `[EMAIL]` | 1.000 [0.000, 1.000] | 1.000 [0.000, 1.000] | 1.000 [0.000, 1.000] | 1 | 0 | 0 | 1 |
| `[IP]` | 1.000 [0.000, 1.000] | 1.000 [0.000, 1.000] | 1.000 [0.000, 1.000] | 1 | 0 | 0 | 1 |
| `[PERSONAL_ID]` | 1.000 [0.000, 1.000] | 1.000 [0.000, 1.000] | 1.000 [0.000, 1.000] | 1 | 0 | 0 | 1 |
| `[PERSON_NAME]` | 0.000 [0.000, 0.000] | 0.000 [0.000, 0.000] | 0.000 [0.000, 0.000] | 0 | 3 | 0 | 0 |
| `[PHONE]` | 0.000 [0.000, 0.000] | 0.000 [0.000, 0.000] | 0.000 [0.000, 0.000] | 0 | 1 | 0 | 0 |
| `[URL]` | 1.000 [0.000, 1.000] | 1.000 [0.000, 1.000] | 1.000 [0.000, 1.000] | 2 | 0 | 0 | 2 |
| **macro** | 0.643 [0.286, 0.643] | 0.714 [0.286, 0.714] | 0.677 [0.286, 0.677] | 7 | 6 | 0 | 7 |
| **micro** | 0.538 [0.333, 0.750] | 1.000 [1.000, 1.000] | 0.700 [0.500, 0.857] | 7 | 6 | 0 | 7 |

### `multi_paragraph` (71 rows)

| Placeholder | Precision (95% CI) | Recall (95% CI) | F1 (95% CI) | TP | FP | FN | Support |
|---|---|---|---|---:|---:|---:|---:|
| `[CARD]` | 0.750 [0.000, 1.000] | 1.000 [0.000, 1.000] | 0.857 [0.000, 1.000] | 3 | 1 | 0 | 3 |
| `[DATE]` | 0.462 [0.358, 0.560] | 1.000 [1.000, 1.000] | 0.632 [0.527, 0.718] | 49 | 57 | 0 | 49 |
| `[EMAIL]` | 1.000 [1.000, 1.000] | 1.000 [1.000, 1.000] | 1.000 [1.000, 1.000] | 33 | 0 | 0 | 33 |
| `[IP]` | 0.812 [0.571, 1.000] | 0.929 [0.625, 1.000] | 0.867 [0.667, 0.973] | 13 | 3 | 1 | 14 |
| `[LICENSE_PLATE]` | 0.000 [0.000, 0.000] | 0.000 [0.000, 0.000] | 0.000 [0.000, 0.000] | 0 | 0 | 1 | 1 |
| `[PERSONAL_ID]` | 1.000 [0.000, 1.000] | 1.000 [0.000, 1.000] | 1.000 [0.000, 1.000] | 1 | 0 | 0 | 1 |
| `[PERSON_NAME]` | 0.638 [0.456, 0.796] | 0.938 [0.778, 1.000] | 0.759 [0.600, 0.868] | 30 | 17 | 2 | 32 |
| `[PHONE]` | 0.452 [0.192, 0.714] | 1.000 [1.000, 1.000] | 0.622 [0.323, 0.833] | 14 | 17 | 0 | 14 |
| `[SECRET]` | 0.000 [0.000, 0.000] | 0.000 [0.000, 0.000] | 0.000 [0.000, 0.000] | 0 | 0 | 21 | 21 |
| `[STREET_ADDRESS]` | 0.125 [0.000, 0.429] | 0.333 [0.000, 1.000] | 0.182 [0.000, 0.500] | 1 | 7 | 2 | 3 |
| `[URL]` | 0.887 [0.800, 0.979] | 1.000 [1.000, 1.000] | 0.940 [0.889, 0.989] | 55 | 7 | 0 | 55 |
| **macro** | 0.557 [0.415, 0.603] | 0.745 [0.611, 0.775] | 0.638 [0.500, 0.671] | 199 | 109 | 27 | 226 |
| **micro** | 0.646 [0.578, 0.712] | 0.881 [0.827, 0.923] | 0.745 [0.691, 0.795] | 199 | 109 | 27 | 226 |

### `structured` (50 rows)

| Placeholder | Precision (95% CI) | Recall (95% CI) | F1 (95% CI) | TP | FP | FN | Support |
|---|---|---|---|---:|---:|---:|---:|
| `[CARD]` | 1.000 [0.000, 1.000] | 1.000 [0.000, 1.000] | 1.000 [0.000, 1.000] | 2 | 0 | 0 | 2 |
| `[DATE]` | 0.605 [0.494, 0.720] | 1.000 [1.000, 1.000] | 0.754 [0.662, 0.837] | 72 | 47 | 0 | 72 |
| `[EMAIL]` | 1.000 [1.000, 1.000] | 1.000 [1.000, 1.000] | 1.000 [1.000, 1.000] | 18 | 0 | 0 | 18 |
| `[IP]` | 0.750 [0.571, 1.000] | 1.000 [1.000, 1.000] | 0.857 [0.727, 1.000] | 9 | 3 | 0 | 9 |
| `[PERSONAL_ID]` | 1.000 [0.000, 1.000] | 1.000 [0.000, 1.000] | 1.000 [0.000, 1.000] | 2 | 0 | 0 | 2 |
| `[PERSON_NAME]` | 0.594 [0.379, 0.807] | 0.950 [0.842, 1.000] | 0.731 [0.538, 0.879] | 19 | 13 | 1 | 20 |
| `[PHONE]` | 0.489 [0.250, 0.731] | 1.000 [1.000, 1.000] | 0.657 [0.400, 0.844] | 23 | 24 | 0 | 23 |
| `[SECRET]` | 0.000 [0.000, 0.000] | 0.000 [0.000, 0.000] | 0.000 [0.000, 0.000] | 0 | 0 | 10 | 10 |
| `[STREET_ADDRESS]` | 0.000 [0.000, 0.000] | 0.000 [0.000, 0.000] | 0.000 [0.000, 0.000] | 0 | 5 | 4 | 4 |
| `[URL]` | 0.759 [0.514, 1.000] | 1.000 [1.000, 1.000] | 0.863 [0.679, 1.000] | 22 | 7 | 0 | 22 |
| **macro** | 0.620 [0.491, 0.668] | 0.795 [0.686, 0.800] | 0.696 [0.575, 0.726] | 167 | 99 | 15 | 182 |
| **micro** | 0.628 [0.563, 0.696] | 0.918 [0.857, 0.964] | 0.746 [0.693, 0.794] | 167 | 99 | 15 | 182 |


## False-positive samples

### `[CARD]`
- `nemotron-en-6a5483ee6c5242009335acde1268695c` [regex] value=`234152987654321`  context: ...'cluding the device identifier 234152987654321. The analysis focused on user'...

### `[DATE]`
- `nemotron-en-c607017070564056aea425cf797f78e6` [opf] value=`quarterly`  context: ...'The quarterly revenue report for LumaLens M'...
- `nemotron-en-d204231bd08a4f0896ce5cd125b79465` [regex] value=`12.34.56.78`  context: ...'k5. The VPN server address is 12.34.56.78. Please use the employee ID 2'...
- `nemotron-en-a20670d943794f209595e39a57743041` [opf] value=`2025-02-24T05:36:54`  context: ...'The latest update was made on 2025-02-24T05:36:54. The maintenance task for the'...
- `nemotron-en-a20670d943794f209595e39a57743041` [opf] value=`next week`  context: ...'1F6E7D2C3B4E is scheduled for next week. The technician responsible f'...
- `nemotron-en-4bb3ddfa63e44e42875321914be0d714` [opf] value=`7:30 PM`  context: ...'5. The event will kick off at 7:30 PM, and we are excited to host a'...

### `[IP]`
- `nemotron-en-b716ebf205e842f5b7a5b0c53cd31925` [opf] value=`9b2a:c7d4:f3b6:891e:5a3c:7f2b:1d8a:4e6b`  context: ..."P addresses 186.204.24.15 and 9b2a:c7d4:f3b6:891e:5a3c:7f2b:1d8a:4e6b. The subscriber's phone numbe"...
- `nemotron-en-52868b7ad35b489eb90ee2fc0d5453fb` [opf] value=`2a02:4d60:1031::`  context: ...' ipv4 12.231.152.210 and ipv6 2a02:4d60:1031::85e1:79f2:9122:bc89 has encoun'...
- `nemotron-en-7505f1e6c0564e6cb6a32f5659c615db` [opf] value=`2001:db8:85a3:0:0:8a2e:370:7334`  context: ...'23.67.132\n- **IPv6 Address**: 2001:db8:85a3:0:0:8a2e:370:7334\n- **Retry Attempts**: 3\n- **L'...
- `nemotron-en-5df22403290f4acfb435c84bf55db439` [opf] value=`2001:0db8:85a3::`  context: ...'3.87.175 and the IPv6 address 2001:0db8:85a3::8a2e:0370:7334. These addresse'...
- `nemotron-en-af963c19ee5b4e718eca9d4bce86d289` [opf] value=`2001:db8:85a3::`  context: ...'P addresses 132.24.178.98 and 2001:db8:85a3::8a2e:3707:7334. The MAC addres'...

### `[PERSONAL_ID]`
- `nemotron-en-731699fe2cf24f83b19a340b1c298902` [opf] value=`A7829461`  context: ...'e, bearing the license number A7829461, is valid until 06/15/2024. F'...
- `nemotron-en-cb9787bd466149fc9702669c828a5b0b` [opf] value=`987-14-6327`  context: ...'th a medical record number of 987-14-6327. Brian Edwards was born on 19'...
- `nemotron-en-90b64c7da46f48df897eb8b41807b30b` [opf] value=`G9`  context: ...'fidentiality of the password: G9$kLmQ8z!2Wp, which is required'...

### `[PERSON_NAME]`
- `nemotron-en-4bb3ddfa63e44e42875321914be0d714` [opf] value=`Mark`  context: ...'Mark your calendars for our upcomi'...
- `nemotron-en-4d8c14613e2b489688b54575a26d515b` [opf] value=`mac`  context: ...'t not use the software with a mac address of 00:3F:66:1A:7C:2D '...
- `nemotron-en-42859b33dab94a79b78fd9185b682084` [opf] value=`08:15:23 AM`  context: ...'2 1469 7831 2098\n\nOrder Time: 08:15:23 AM\n\nPlease ensure that your paym'...
- `nemotron-en-fbb0f537c6104acd8b516657128487cb` [opf] value=`user_session=xf98bk7l3p`  context: ...'n and the cookie http cookie: user_session=xf98bk7l3p; Path=/; HttpOnly; Secure; Sa'...
- `nemotron-en-931a0d9108fa4049b5c9b004fa88ea17` [opf] value=`mac`  context: ...'resulting from the use of the mac address 97:F4:CA:2E:7A:1B. Th'...

### `[PHONE]`
- `nemotron-en-aa68de98f33149b08b231a63a9dc0c6c` [regex] value=`0004382965`  context: ...'plan beneficiary number is PA-0004382965.'...
- `nemotron-en-31ee8fd013e4445d83d6f15169f76ba7` [regex] value=`0004372819`  context: ...'le. The medical record number 0004372819 was assigned to track the pro'...
- `nemotron-en-722a4838747845dfa1fe6eb666ac9372` [regex] value=`0008374925`  context: ...'for the medical record number 0008374925. The event was logged at 7:22'...
- `nemotron-en-aa44bfd07cd340b788cf70f3dcae7dc6` [regex] value=`7256198345`  context: ...' the biometric identifier BIO-7256198345.'...
- `nemotron-en-4d8c14613e2b489688b54575a26d515b` [regex] value=`479-772-7297`  context: ...'rison & Associates via fax at 479-772-7297.'...

### `[STREET_ADDRESS]`
- `nemotron-en-aa44bfd07cd340b788cf70f3dcae7dc6` [opf] value=`WA`  context: ...'he certificate license number WA-ENG-573281. The scope of work'...
- `nemotron-en-fbb0f537c6104acd8b516657128487cb` [opf] value=`Path=/`  context: ...'kie: user_session=xf98bk7l3p; Path=/; HttpOnly; Secure; SameSite=L'...
- `nemotron-en-37d5e69390f3450fafaa2a35da02c1d0` [opf] value=`NJ`  context: ...'he certificate license number NJ-MED-539421, which is crucial '...
- `nemotron-en-5d036b03b45e4e79b40f258943042bd3` [opf] value=`Path=/`  context: ...'ie** csrf_token=jhb7f5xkp2m8; Path=/; Secure for secure access to '...
- `nemotron-en-5e11494f47e34b48b912ceae7e5b4da8` [opf] value=`Path=/`  context: ...' csrf_token=zx7q2w9y8v6s5u4t; Path=/; Secure** has been utilized t'...

### `[URL]`
- `nemotron-en-b30a384018af4fb6a7d490a9a88ae8c8` [opf] value=`rachel.mil`  context: ...'redentials. Your user name is rachel.milliner. Your password is Michae'...
- `nemotron-en-9fcbec9cc3b54302b94f55b90bd29648` [opf] value=`angela.br`  context: ...'           |                | angela.brock         |                 '...
- `nemotron-en-52868b7ad35b489eb90ee2fc0d5453fb` [opf] value=`l.mil`  context: ...'al reports from the user name l.miles. The user with the email le'...
- `nemotron-en-4ac284c894874af5a87319025ed67d05` [opf] value=`sony.men`  context: ...' our media relations contact, sony.mendez.'...
- `nemotron-en-c5111e01dcd5413ba104399f591762ec` [opf] value=`t.pe`  context: ...'eement") is between the user, t.perez, and the organization, eff'...


## False-negative samples

### `[IP]`
- `nemotron-en-d204231bd08a4f0896ce5cd125b79465` value=`12.34.56.78`  context: ...'k5. The VPN server address is 12.34.56.78. Please use the employee ID 2'...

### `[LICENSE_PLATE]`
- `nemotron-en-5d036b03b45e4e79b40f258943042bd3` value=`V4H-729`  context: ...'ust display the license plate V4H-729.\n\nAll heavy machinery must be'...

### `[PERSON_NAME]`
- `nemotron-en-41818ce0a8ff4076be22668d598e8398` value=`Catherin Izquierdo`  context: ...'ntioned in-kind donation from Catherin Izquierdo, a hispanic or latino other. '...
- `nemotron-en-a2f83ad566264cd580f6d0e9399a1674` value=`Merrill Bell`  context: ...'s or concerns, please contact Merrill Bell at mbell2@gmail.com or call 5'...
- `nemotron-en-a2f83ad566264cd580f6d0e9399a1674` value=`Merrill Bell`  context: ...'ns, feel free to reach out to Merrill Bell at mbell2@gmail.com or call 5'...

### `[SECRET]`
- `nemotron-en-d204231bd08a4f0896ce5cd125b79465` value=`G9t$fR2mXk5`  context: ...'axaben_coder. The password is G9t$fR2mXk5. The VPN server address is 12'...
- `nemotron-en-b30a384018af4fb6a7d490a9a88ae8c8` value=`Michael1995`  context: ...'el.milliner. Your password is Michael1995.\n\n3. Once logged in, you will'...
- `nemotron-en-94c56d76eb244537971a57a72fe78bc2` value=`River77!`  context: ...'effectiveness of our password River77! and make adjustments as neede'...
- `nemotron-en-7436f7124c7440d38c3ab0a405b8eb37` value=`d4a6b9c1-3e2f-4f1a-a76d-3a8c9b1d2e3f`  context: ...'taTech Solutions. The api key d4a6b9c1-3e2f-4f1a-a76d-3a8c9b1d2e3f is provided for authenticatio'...
- `nemotron-en-7436f7124c7440d38c3ab0a405b8eb37` value=`d4a6b9c1-3e2f-4f1a-a76d-3a8c9b1d2e3f`  context: ...'s not to disclose the api key d4a6b9c1-3e2f-4f1a-a76d-3a8c9b1d2e3f to any third party, including'...

### `[STREET_ADDRESS]`
- `nemotron-en-aa68de98f33149b08b231a63a9dc0c6c` value=`116 Thatcher Brook Ln`  context: ...'8-0709. The address listed is 116 Thatcher Brook Ln. The health plan beneficiary '...
- `nemotron-en-08b7ad8f4b574be38d8202bc882512f9` value=`311 Oakwood Ave`  context: ...'The property located at 311 Oakwood Ave was appraised on 2024-08-15. '...
- `nemotron-en-be5da19493474356b544fa79796d41e5` value=`694 Lennox`  context: ...'-92-7456\n\n**Street Address:**\n694 Lennox\n\n**Assistance Program Type:**'...
- `nemotron-en-cb9787bd466149fc9702669c828a5b0b` value=`240 Senate Ave`  context: ...'white. The patient resides at 240 Senate Ave.  As part of the assessment, '...
- `nemotron-en-3de64e26814c493892f8508673ff5798` value=`56 N Wright Rd`  context: ...'oject involves renovations at 56 N Wright Rd. The scope of work includes s'...

