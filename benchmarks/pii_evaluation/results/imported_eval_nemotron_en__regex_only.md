# Imported-dataset eval - nemotron_en

- Rows evaluated: **200**
- Rows with zero gold spans (after label-map filter): **0**
- Elapsed: **0.1s** (0ms/row)
- Projection-symmetric scoring: **on** (gold placeholder space: `[CARD], [DATE], [EMAIL], [IP], [LICENSE_PLATE], [PERSONAL_ID], [PERSON_NAME], [PHONE], [SECRET], [STREET_ADDRESS], [URL], [VIN]`)

## Per-placeholder precision / recall

| Placeholder | Precision (95% CI) | Recall (95% CI) | F1 (95% CI) | TP | FP | FN | Support |
|---|---|---|---|---:|---:|---:|---:|
| `[CARD]` | 0.857 [0.500, 1.000] | 1.000 [1.000, 1.000] | 0.923 [0.667, 1.000] | 6 | 1 | 0 | 6 |
| `[DATE]` | 0.969 [0.924, 1.000] | 0.939 [0.865, 0.988] | 0.954 [0.910, 0.988] | 154 | 5 | 10 | 164 |
| `[EMAIL]` | 1.000 [1.000, 1.000] | 1.000 [1.000, 1.000] | 1.000 [1.000, 1.000] | 73 | 0 | 0 | 73 |
| `[IP]` | 1.000 [1.000, 1.000] | 0.971 [0.905, 1.000] | 0.986 [0.950, 1.000] | 34 | 0 | 1 | 35 |
| `[LICENSE_PLATE]` | 1.000 [0.000, 1.000] | 0.667 [0.000, 1.000] | 0.800 [0.000, 1.000] | 2 | 0 | 1 | 3 |
| `[PERSONAL_ID]` | 1.000 [1.000, 1.000] | 1.000 [1.000, 1.000] | 1.000 [1.000, 1.000] | 8 | 0 | 0 | 8 |
| `[PERSON_NAME]` | 0.000 [0.000, 0.000] | 0.000 [0.000, 0.000] | 0.000 [0.000, 0.000] | 0 | 0 | 88 | 88 |
| `[PHONE]` | 0.454 [0.320, 0.588] | 1.000 [1.000, 1.000] | 0.624 [0.485, 0.740] | 49 | 59 | 0 | 49 |
| `[SECRET]` | 0.000 [0.000, 0.000] | 0.000 [0.000, 0.000] | 0.000 [0.000, 0.000] | 0 | 0 | 49 | 49 |
| `[STREET_ADDRESS]` | 0.000 [0.000, 0.000] | 0.000 [0.000, 0.000] | 0.000 [0.000, 0.000] | 0 | 0 | 14 | 14 |
| `[URL]` | 1.000 [1.000, 1.000] | 1.000 [1.000, 1.000] | 1.000 [1.000, 1.000] | 116 | 0 | 0 | 116 |
| **macro** | 0.662 [0.558, 0.684] | 0.689 [0.625, 0.724] | 0.675 [0.590, 0.699] | 442 | 65 | 163 | 605 |
| **micro** | 0.872 [0.833, 0.910] | 0.731 [0.683, 0.774] | 0.795 [0.760, 0.827] | 442 | 65 | 163 | 605 |

## Per-length-bucket precision / recall

Row distribution across buckets: `sentence`: 75, `paragraph`: 4, `multi_paragraph`: 71, `structured`: 50

### `sentence` (75 rows)

| Placeholder | Precision (95% CI) | Recall (95% CI) | F1 (95% CI) | TP | FP | FN | Support |
|---|---|---|---|---:|---:|---:|---:|
| `[CARD]` | 1.000 [0.000, 1.000] | 1.000 [0.000, 1.000] | 1.000 [0.000, 1.000] | 1 | 0 | 0 | 1 |
| `[DATE]` | 1.000 [1.000, 1.000] | 0.976 [0.919, 1.000] | 0.988 [0.958, 1.000] | 40 | 0 | 1 | 41 |
| `[EMAIL]` | 1.000 [1.000, 1.000] | 1.000 [1.000, 1.000] | 1.000 [1.000, 1.000] | 21 | 0 | 0 | 21 |
| `[IP]` | 1.000 [1.000, 1.000] | 1.000 [1.000, 1.000] | 1.000 [1.000, 1.000] | 11 | 0 | 0 | 11 |
| `[LICENSE_PLATE]` | 1.000 [0.000, 1.000] | 1.000 [0.000, 1.000] | 1.000 [0.000, 1.000] | 2 | 0 | 0 | 2 |
| `[PERSONAL_ID]` | 1.000 [1.000, 1.000] | 1.000 [1.000, 1.000] | 1.000 [1.000, 1.000] | 4 | 0 | 0 | 4 |
| `[PERSON_NAME]` | 0.000 [0.000, 0.000] | 0.000 [0.000, 0.000] | 0.000 [0.000, 0.000] | 0 | 0 | 36 | 36 |
| `[PHONE]` | 0.375 [0.211, 0.546] | 1.000 [1.000, 1.000] | 0.545 [0.348, 0.706] | 12 | 20 | 0 | 12 |
| `[SECRET]` | 0.000 [0.000, 0.000] | 0.000 [0.000, 0.000] | 0.000 [0.000, 0.000] | 0 | 0 | 18 | 18 |
| `[STREET_ADDRESS]` | 0.000 [0.000, 0.000] | 0.000 [0.000, 0.000] | 0.000 [0.000, 0.000] | 0 | 0 | 7 | 7 |
| `[URL]` | 1.000 [1.000, 1.000] | 1.000 [1.000, 1.000] | 1.000 [1.000, 1.000] | 37 | 0 | 0 | 37 |
| **macro** | 0.670 [0.486, 0.684] | 0.725 [0.543, 0.727] | 0.697 [0.513, 0.704] | 128 | 20 | 62 | 190 |
| **micro** | 0.865 [0.809, 0.916] | 0.674 [0.609, 0.736] | 0.757 [0.707, 0.802] | 128 | 20 | 62 | 190 |

### `paragraph` (4 rows)

| Placeholder | Precision (95% CI) | Recall (95% CI) | F1 (95% CI) | TP | FP | FN | Support |
|---|---|---|---|---:|---:|---:|---:|
| `[DATE]` | 1.000 [0.000, 1.000] | 1.000 [0.000, 1.000] | 1.000 [0.000, 1.000] | 2 | 0 | 0 | 2 |
| `[EMAIL]` | 1.000 [0.000, 1.000] | 1.000 [0.000, 1.000] | 1.000 [0.000, 1.000] | 1 | 0 | 0 | 1 |
| `[IP]` | 1.000 [0.000, 1.000] | 1.000 [0.000, 1.000] | 1.000 [0.000, 1.000] | 1 | 0 | 0 | 1 |
| `[PERSONAL_ID]` | 1.000 [0.000, 1.000] | 1.000 [0.000, 1.000] | 1.000 [0.000, 1.000] | 1 | 0 | 0 | 1 |
| `[PHONE]` | 0.000 [0.000, 0.000] | 0.000 [0.000, 0.000] | 0.000 [0.000, 0.000] | 0 | 1 | 0 | 0 |
| `[URL]` | 1.000 [0.000, 1.000] | 1.000 [0.000, 1.000] | 1.000 [0.000, 1.000] | 2 | 0 | 0 | 2 |
| **macro** | 0.833 [0.333, 0.833] | 0.833 [0.333, 0.833] | 0.833 [0.333, 0.833] | 7 | 1 | 0 | 7 |
| **micro** | 0.875 [0.700, 1.000] | 1.000 [1.000, 1.000] | 0.933 [0.824, 1.000] | 7 | 1 | 0 | 7 |

### `multi_paragraph` (71 rows)

| Placeholder | Precision (95% CI) | Recall (95% CI) | F1 (95% CI) | TP | FP | FN | Support |
|---|---|---|---|---:|---:|---:|---:|
| `[CARD]` | 0.750 [0.000, 1.000] | 1.000 [0.000, 1.000] | 0.857 [0.000, 1.000] | 3 | 1 | 0 | 3 |
| `[DATE]` | 0.978 [0.914, 1.000] | 0.918 [0.804, 1.000] | 0.947 [0.874, 0.991] | 45 | 1 | 4 | 49 |
| `[EMAIL]` | 1.000 [1.000, 1.000] | 1.000 [1.000, 1.000] | 1.000 [1.000, 1.000] | 33 | 0 | 0 | 33 |
| `[IP]` | 1.000 [1.000, 1.000] | 0.929 [0.625, 1.000] | 0.963 [0.769, 1.000] | 13 | 0 | 1 | 14 |
| `[LICENSE_PLATE]` | 0.000 [0.000, 0.000] | 0.000 [0.000, 0.000] | 0.000 [0.000, 0.000] | 0 | 0 | 1 | 1 |
| `[PERSONAL_ID]` | 1.000 [0.000, 1.000] | 1.000 [0.000, 1.000] | 1.000 [0.000, 1.000] | 1 | 0 | 0 | 1 |
| `[PERSON_NAME]` | 0.000 [0.000, 0.000] | 0.000 [0.000, 0.000] | 0.000 [0.000, 0.000] | 0 | 0 | 32 | 32 |
| `[PHONE]` | 0.483 [0.217, 0.739] | 1.000 [1.000, 1.000] | 0.651 [0.357, 0.850] | 14 | 15 | 0 | 14 |
| `[SECRET]` | 0.000 [0.000, 0.000] | 0.000 [0.000, 0.000] | 0.000 [0.000, 0.000] | 0 | 0 | 21 | 21 |
| `[STREET_ADDRESS]` | 0.000 [0.000, 0.000] | 0.000 [0.000, 0.000] | 0.000 [0.000, 0.000] | 0 | 0 | 3 | 3 |
| `[URL]` | 1.000 [1.000, 1.000] | 1.000 [1.000, 1.000] | 1.000 [1.000, 1.000] | 55 | 0 | 0 | 55 |
| **macro** | 0.565 [0.435, 0.601] | 0.622 [0.511, 0.634] | 0.592 [0.478, 0.613] | 164 | 17 | 62 | 226 |
| **micro** | 0.906 [0.849, 0.955] | 0.726 [0.639, 0.796] | 0.806 [0.747, 0.854] | 164 | 17 | 62 | 226 |

### `structured` (50 rows)

| Placeholder | Precision (95% CI) | Recall (95% CI) | F1 (95% CI) | TP | FP | FN | Support |
|---|---|---|---|---:|---:|---:|---:|
| `[CARD]` | 1.000 [0.000, 1.000] | 1.000 [0.000, 1.000] | 1.000 [0.000, 1.000] | 2 | 0 | 0 | 2 |
| `[DATE]` | 0.944 [0.860, 1.000] | 0.931 [0.767, 1.000] | 0.937 [0.842, 1.000] | 67 | 4 | 5 | 72 |
| `[EMAIL]` | 1.000 [1.000, 1.000] | 1.000 [1.000, 1.000] | 1.000 [1.000, 1.000] | 18 | 0 | 0 | 18 |
| `[IP]` | 1.000 [1.000, 1.000] | 1.000 [1.000, 1.000] | 1.000 [1.000, 1.000] | 9 | 0 | 0 | 9 |
| `[PERSONAL_ID]` | 1.000 [0.000, 1.000] | 1.000 [0.000, 1.000] | 1.000 [0.000, 1.000] | 2 | 0 | 0 | 2 |
| `[PERSON_NAME]` | 0.000 [0.000, 0.000] | 0.000 [0.000, 0.000] | 0.000 [0.000, 0.000] | 0 | 0 | 20 | 20 |
| `[PHONE]` | 0.500 [0.256, 0.750] | 1.000 [1.000, 1.000] | 0.667 [0.408, 0.857] | 23 | 23 | 0 | 23 |
| `[SECRET]` | 0.000 [0.000, 0.000] | 0.000 [0.000, 0.000] | 0.000 [0.000, 0.000] | 0 | 0 | 10 | 10 |
| `[STREET_ADDRESS]` | 0.000 [0.000, 0.000] | 0.000 [0.000, 0.000] | 0.000 [0.000, 0.000] | 0 | 0 | 4 | 4 |
| `[URL]` | 1.000 [1.000, 1.000] | 1.000 [1.000, 1.000] | 1.000 [1.000, 1.000] | 22 | 0 | 0 | 22 |
| **macro** | 0.644 [0.521, 0.669] | 0.693 [0.579, 0.700] | 0.668 [0.554, 0.683] | 143 | 27 | 39 | 182 |
| **micro** | 0.841 [0.739, 0.926] | 0.786 [0.684, 0.871] | 0.812 [0.732, 0.883] | 143 | 27 | 39 | 182 |


## False-positive samples

### `[CARD]`
- `nemotron-en-6a5483ee6c5242009335acde1268695c` [regex] value=`234152987654321`  context: ...'cluding the device identifier 234152987654321. The analysis focused on user'...

### `[DATE]`
- `nemotron-en-d204231bd08a4f0896ce5cd125b79465` [regex] value=`12.34.56.78`  context: ...'k5. The VPN server address is 12.34.56.78. Please use the employee ID 2'...
- `nemotron-en-d6acf3d8d0494e259f02e28be2d54a5f` [regex] value=`2024-01-16`  context: ...' Recruitment of Participants: 2024-01-16 to 2024-02-15\n- Implementatio'...
- `nemotron-en-d6acf3d8d0494e259f02e28be2d54a5f` [regex] value=`2024-02-16`  context: ...'\n- Implementation of Program: 2024-02-16 to 2024-06-15\n- Evaluation an'...
- `nemotron-en-d6acf3d8d0494e259f02e28be2d54a5f` [regex] value=`2024-06-16`  context: ...'5\n- Evaluation and Reporting: 2024-06-16 to 2024-07-15\n\n**Expected Out'...
- `nemotron-en-3ef521773dfa4727888cf20ca3717871` [regex] value=`1310-73-2`  context: ...'ts: Sodium Hydroxide (CAS No. 1310-73-2)\n\n**Section 4: First-Aid Meas'...

### `[PHONE]`
- `nemotron-en-aa68de98f33149b08b231a63a9dc0c6c` [regex] value=`0004382965`  context: ...'plan beneficiary number is PA-0004382965.'...
- `nemotron-en-31ee8fd013e4445d83d6f15169f76ba7` [regex] value=`0004372819`  context: ...'le. The medical record number 0004372819 was assigned to track the pro'...
- `nemotron-en-722a4838747845dfa1fe6eb666ac9372` [regex] value=`0008374925`  context: ...'for the medical record number 0008374925. The event was logged at 7:22'...
- `nemotron-en-aa44bfd07cd340b788cf70f3dcae7dc6` [regex] value=`7256198345`  context: ...' the biometric identifier BIO-7256198345.'...
- `nemotron-en-4d8c14613e2b489688b54575a26d515b` [regex] value=`479-772-7297`  context: ...'rison & Associates via fax at 479-772-7297.'...


## False-negative samples

### `[DATE]`
- `nemotron-en-31a4c4b49a934909b73effcc79ee5d98` value=`November 15, 2023`  context: ...'se schedule is as follows:\n\n- November 15, 2023: Introduction to Childcare Ad'...
- `nemotron-en-31a4c4b49a934909b73effcc79ee5d98` value=`November 22, 2023`  context: ...'to Childcare Administration\n- November 22, 2023: Management and Leadership in'...
- `nemotron-en-31a4c4b49a934909b73effcc79ee5d98` value=`November 29, 2023`  context: ...'and Leadership in Childcare\n- November 29, 2023: Curriculum Development and I'...
- `nemotron-en-31a4c4b49a934909b73effcc79ee5d98` value=`December 6, 2023`  context: ...'elopment and Implementation\n- December 6, 2023: Policy and Regulation in Chi'...
- `nemotron-en-31a4c4b49a934909b73effcc79ee5d98` value=`December 15, 2023`  context: ...'89, the course instructor, on December 15, 2023. Students can contact the ins'...

### `[IP]`
- `nemotron-en-d204231bd08a4f0896ce5cd125b79465` value=`12.34.56.78`  context: ...'k5. The VPN server address is 12.34.56.78. Please use the employee ID 2'...

### `[LICENSE_PLATE]`
- `nemotron-en-5d036b03b45e4e79b40f258943042bd3` value=`V4H-729`  context: ...'ust display the license plate V4H-729.\n\nAll heavy machinery must be'...

### `[PERSON_NAME]`
- `nemotron-en-aa68de98f33149b08b231a63a9dc0c6c` value=`Arnold Varner`  context: ...'urance Enrollment Form is for Arnold Varner, born on 1979-08-22. The Soci'...
- `nemotron-en-5344e719fbb24d86bbb80212eabfbab2` value=`Elisabeth Setzer`  context: ...'mmunity Impact Foundation and Elisabeth Setzer. Elisabeth Setzer can be reac'...
- `nemotron-en-5344e719fbb24d86bbb80212eabfbab2` value=`Elisabeth Setzer`  context: ...'ndation and Elisabeth Setzer. Elisabeth Setzer can be reached at elisabeth.s'...
- `nemotron-en-254b1bb9ddf94a7cacbaad48fe228341` value=`Joseph Zarecki`  context: ...'ore on 2023-09-15. My name is Joseph Zarecki. I can be reached at 727-360-'...
- `nemotron-en-722a4838747845dfa1fe6eb666ac9372` value=`Shirley Clark`  context: ...'r details were requested from Shirley Clark via email at shirley_clark03@'...

### `[SECRET]`
- `nemotron-en-d204231bd08a4f0896ce5cd125b79465` value=`G9t$fR2mXk5`  context: ...'axaben_coder. The password is G9t$fR2mXk5. The VPN server address is 12'...
- `nemotron-en-b30a384018af4fb6a7d490a9a88ae8c8` value=`Michael1995`  context: ...'el.milliner. Your password is Michael1995.\n\n3. Once logged in, you will'...
- `nemotron-en-94c56d76eb244537971a57a72fe78bc2` value=`River77!`  context: ...'effectiveness of our password River77! and make adjustments as neede'...
- `nemotron-en-7436f7124c7440d38c3ab0a405b8eb37` value=`d4a6b9c1-3e2f-4f1a-a76d-3a8c9b1d2e3f`  context: ...'taTech Solutions. The api key d4a6b9c1-3e2f-4f1a-a76d-3a8c9b1d2e3f is provided for authenticatio'...
- `nemotron-en-7436f7124c7440d38c3ab0a405b8eb37` value=`d4a6b9c1-3e2f-4f1a-a76d-3a8c9b1d2e3f`  context: ...'s not to disclose the api key d4a6b9c1-3e2f-4f1a-a76d-3a8c9b1d2e3f to any third party, including'...

### `[STREET_ADDRESS]`
- `nemotron-en-aa68de98f33149b08b231a63a9dc0c6c` value=`116 Thatcher Brook Ln`  context: ...'8-0709. The address listed is 116 Thatcher Brook Ln. The health plan beneficiary '...
- `nemotron-en-08b7ad8f4b574be38d8202bc882512f9` value=`311 Oakwood Ave`  context: ...'The property located at 311 Oakwood Ave was appraised on 2024-08-15. '...
- `nemotron-en-fc306c761d374f9080512075154e49aa` value=`60 School St`  context: ...'**\n\n- **Origin Address**:\n  - 60 School St\n\n- **Destination Coordinates*'...
- `nemotron-en-be5da19493474356b544fa79796d41e5` value=`694 Lennox`  context: ...'-92-7456\n\n**Street Address:**\n694 Lennox\n\n**Assistance Program Type:**'...
- `nemotron-en-cb9787bd466149fc9702669c828a5b0b` value=`240 Senate Ave`  context: ...'white. The patient resides at 240 Senate Ave.  As part of the assessment, '...

