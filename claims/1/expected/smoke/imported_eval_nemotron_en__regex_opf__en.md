# Imported-dataset eval - nemotron_en

- Rows evaluated: **200**
- Rows with zero gold spans (after label-map filter): **0**
- Elapsed: **1265.5s** (6328ms/row)
- Projection-symmetric scoring: **on** (gold placeholder space: `[CARD], [DATE], [EMAIL], [IP], [LICENSE_PLATE], [PERSONAL_ID], [PERSON_NAME], [PHONE], [SECRET], [STREET_ADDRESS], [URL], [VIN]`)

## Per-placeholder precision / recall

| Placeholder | Precision (95% CI) | Recall (95% CI) | F1 (95% CI) | TP | FP | FN | Support |
|---|---|---|---|---:|---:|---:|---:|
| `[CARD]` | 0.857 [0.500, 1.000] | 1.000 [1.000, 1.000] | 0.923 [0.667, 1.000] | 6 | 1 | 0 | 6 |
| `[DATE]` | 0.969 [0.924, 1.000] | 0.939 [0.865, 0.988] | 0.954 [0.910, 0.988] | 154 | 5 | 10 | 164 |
| `[EMAIL]` | 1.000 [1.000, 1.000] | 1.000 [1.000, 1.000] | 1.000 [1.000, 1.000] | 73 | 0 | 0 | 73 |
| `[IP]` | 1.000 [1.000, 1.000] | 0.971 [0.905, 1.000] | 0.986 [0.950, 1.000] | 34 | 0 | 1 | 35 |
| `[LICENSE_PLATE]` | 1.000 [0.000, 1.000] | 0.667 [0.000, 1.000] | 0.800 [0.000, 1.000] | 2 | 0 | 1 | 3 |
| `[PERSONAL_ID]` | 0.235 [0.097, 0.382] | 1.000 [1.000, 1.000] | 0.381 [0.176, 0.553] | 8 | 26 | 0 | 8 |
| `[PERSON_NAME]` | 0.649 [0.541, 0.748] | 0.989 [0.964, 1.000] | 0.784 [0.699, 0.853] | 87 | 47 | 1 | 88 |
| `[PHONE]` | 0.450 [0.317, 0.583] | 1.000 [1.000, 1.000] | 0.620 [0.482, 0.737] | 49 | 60 | 0 | 49 |
| `[SECRET]` | 0.625 [0.517, 0.734] | 0.918 [0.821, 1.000] | 0.744 [0.655, 0.822] | 45 | 27 | 4 | 49 |
| `[STREET_ADDRESS]` | 0.483 [0.296, 0.688] | 1.000 [1.000, 1.000] | 0.651 [0.457, 0.815] | 14 | 15 | 0 | 14 |
| `[URL]` | 1.000 [1.000, 1.000] | 1.000 [1.000, 1.000] | 1.000 [1.000, 1.000] | 116 | 0 | 0 | 116 |
| **macro** | 0.752 [0.646, 0.790] | 0.953 [0.887, 0.992] | 0.840 [0.749, 0.872] | 588 | 181 | 17 | 605 |
| **micro** | 0.765 [0.729, 0.802] | 0.972 [0.948, 0.989] | 0.856 [0.831, 0.882] | 588 | 181 | 17 | 605 |

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
| `[PERSONAL_ID]` | 0.333 [0.083, 0.615] | 1.000 [1.000, 1.000] | 0.500 [0.154, 0.762] | 4 | 8 | 0 | 4 |
| `[PERSON_NAME]` | 0.783 [0.647, 0.886] | 1.000 [1.000, 1.000] | 0.878 [0.786, 0.940] | 36 | 10 | 0 | 36 |
| `[PHONE]` | 0.375 [0.211, 0.546] | 1.000 [1.000, 1.000] | 0.545 [0.348, 0.706] | 12 | 20 | 0 | 12 |
| `[SECRET]` | 0.640 [0.474, 0.824] | 0.889 [0.750, 1.000] | 0.744 [0.609, 0.862] | 16 | 9 | 2 | 18 |
| `[STREET_ADDRESS]` | 0.538 [0.250, 0.800] | 1.000 [1.000, 1.000] | 0.700 [0.400, 0.889] | 7 | 6 | 0 | 7 |
| `[URL]` | 1.000 [1.000, 1.000] | 1.000 [1.000, 1.000] | 1.000 [1.000, 1.000] | 37 | 0 | 0 | 37 |
| **macro** | 0.788 [0.614, 0.823] | 0.988 [0.806, 1.000] | 0.877 [0.696, 0.898] | 187 | 53 | 3 | 190 |
| **micro** | 0.779 [0.726, 0.826] | 0.984 [0.964, 1.000] | 0.870 [0.835, 0.899] | 187 | 53 | 3 | 190 |

### `paragraph` (4 rows)

| Placeholder | Precision (95% CI) | Recall (95% CI) | F1 (95% CI) | TP | FP | FN | Support |
|---|---|---|---|---:|---:|---:|---:|
| `[DATE]` | 1.000 [0.000, 1.000] | 1.000 [0.000, 1.000] | 1.000 [0.000, 1.000] | 2 | 0 | 0 | 2 |
| `[EMAIL]` | 1.000 [0.000, 1.000] | 1.000 [0.000, 1.000] | 1.000 [0.000, 1.000] | 1 | 0 | 0 | 1 |
| `[IP]` | 1.000 [0.000, 1.000] | 1.000 [0.000, 1.000] | 1.000 [0.000, 1.000] | 1 | 0 | 0 | 1 |
| `[PERSONAL_ID]` | 1.000 [0.000, 1.000] | 1.000 [0.000, 1.000] | 1.000 [0.000, 1.000] | 1 | 0 | 0 | 1 |
| `[PERSON_NAME]` | 0.000 [0.000, 0.000] | 0.000 [0.000, 0.000] | 0.000 [0.000, 0.000] | 0 | 1 | 0 | 0 |
| `[PHONE]` | 0.000 [0.000, 0.000] | 0.000 [0.000, 0.000] | 0.000 [0.000, 0.000] | 0 | 1 | 0 | 0 |
| `[URL]` | 1.000 [0.000, 1.000] | 1.000 [0.000, 1.000] | 1.000 [0.000, 1.000] | 2 | 0 | 0 | 2 |
| **macro** | 0.714 [0.286, 0.714] | 0.714 [0.286, 0.714] | 0.714 [0.286, 0.714] | 7 | 2 | 0 | 7 |
| **micro** | 0.778 [0.700, 1.000] | 1.000 [1.000, 1.000] | 0.875 [0.824, 1.000] | 7 | 2 | 0 | 7 |

### `multi_paragraph` (71 rows)

| Placeholder | Precision (95% CI) | Recall (95% CI) | F1 (95% CI) | TP | FP | FN | Support |
|---|---|---|---|---:|---:|---:|---:|
| `[CARD]` | 0.750 [0.000, 1.000] | 1.000 [0.000, 1.000] | 0.857 [0.000, 1.000] | 3 | 1 | 0 | 3 |
| `[DATE]` | 0.978 [0.914, 1.000] | 0.918 [0.804, 1.000] | 0.947 [0.874, 0.991] | 45 | 1 | 4 | 49 |
| `[EMAIL]` | 1.000 [1.000, 1.000] | 1.000 [1.000, 1.000] | 1.000 [1.000, 1.000] | 33 | 0 | 0 | 33 |
| `[IP]` | 1.000 [1.000, 1.000] | 0.929 [0.625, 1.000] | 0.963 [0.769, 1.000] | 13 | 0 | 1 | 14 |
| `[LICENSE_PLATE]` | 0.000 [0.000, 0.000] | 0.000 [0.000, 0.000] | 0.000 [0.000, 0.000] | 0 | 0 | 1 | 1 |
| `[PERSONAL_ID]` | 0.091 [0.000, 0.333] | 1.000 [0.000, 1.000] | 0.167 [0.000, 0.500] | 1 | 10 | 0 | 1 |
| `[PERSON_NAME]` | 0.633 [0.442, 0.793] | 0.969 [0.909, 1.000] | 0.765 [0.603, 0.872] | 31 | 18 | 1 | 32 |
| `[PHONE]` | 0.483 [0.217, 0.739] | 1.000 [1.000, 1.000] | 0.651 [0.357, 0.850] | 14 | 15 | 0 | 14 |
| `[SECRET]` | 0.679 [0.542, 0.833] | 0.905 [0.727, 1.000] | 0.776 [0.667, 0.885] | 19 | 9 | 2 | 21 |
| `[STREET_ADDRESS]` | 0.273 [0.000, 0.667] | 1.000 [0.000, 1.000] | 0.429 [0.000, 0.800] | 3 | 8 | 0 | 3 |
| `[URL]` | 1.000 [1.000, 1.000] | 1.000 [1.000, 1.000] | 1.000 [1.000, 1.000] | 55 | 0 | 0 | 55 |
| **macro** | 0.626 [0.551, 0.696] | 0.884 [0.702, 0.902] | 0.733 [0.631, 0.780] | 217 | 62 | 9 | 226 |
| **micro** | 0.778 [0.716, 0.841] | 0.960 [0.925, 0.986] | 0.859 [0.810, 0.902] | 217 | 62 | 9 | 226 |

### `structured` (50 rows)

| Placeholder | Precision (95% CI) | Recall (95% CI) | F1 (95% CI) | TP | FP | FN | Support |
|---|---|---|---|---:|---:|---:|---:|
| `[CARD]` | 1.000 [0.000, 1.000] | 1.000 [0.000, 1.000] | 1.000 [0.000, 1.000] | 2 | 0 | 0 | 2 |
| `[DATE]` | 0.944 [0.860, 1.000] | 0.931 [0.767, 1.000] | 0.937 [0.842, 1.000] | 67 | 4 | 5 | 72 |
| `[EMAIL]` | 1.000 [1.000, 1.000] | 1.000 [1.000, 1.000] | 1.000 [1.000, 1.000] | 18 | 0 | 0 | 18 |
| `[IP]` | 1.000 [1.000, 1.000] | 1.000 [1.000, 1.000] | 1.000 [1.000, 1.000] | 9 | 0 | 0 | 9 |
| `[PERSONAL_ID]` | 0.200 [0.000, 0.500] | 1.000 [0.000, 1.000] | 0.333 [0.000, 0.667] | 2 | 8 | 0 | 2 |
| `[PERSON_NAME]` | 0.526 [0.304, 0.757] | 1.000 [1.000, 1.000] | 0.690 [0.467, 0.862] | 20 | 18 | 0 | 20 |
| `[PHONE]` | 0.489 [0.256, 0.727] | 1.000 [1.000, 1.000] | 0.657 [0.408, 0.842] | 23 | 24 | 0 | 23 |
| `[SECRET]` | 0.526 [0.182, 0.741] | 1.000 [1.000, 1.000] | 0.690 [0.308, 0.851] | 10 | 9 | 0 | 10 |
| `[STREET_ADDRESS]` | 0.800 [0.000, 1.000] | 1.000 [0.000, 1.000] | 0.889 [0.000, 1.000] | 4 | 1 | 0 | 4 |
| `[URL]` | 1.000 [1.000, 1.000] | 1.000 [1.000, 1.000] | 1.000 [1.000, 1.000] | 22 | 0 | 0 | 22 |
| **macro** | 0.749 [0.622, 0.806] | 0.993 [0.876, 1.000] | 0.854 [0.724, 0.891] | 177 | 64 | 5 | 182 |
| **micro** | 0.734 [0.656, 0.806] | 0.973 [0.909, 1.000] | 0.837 [0.776, 0.890] | 177 | 64 | 5 | 182 |


## False-positive samples

### `[CARD]`
- `nemotron-en-6a5483ee6c5242009335acde1268695c` [regex] value=`234152987654321`  context: ...'cluding the device identifier 234152987654321. The analysis focused on user'...

### `[DATE]`
- `nemotron-en-d204231bd08a4f0896ce5cd125b79465` [regex] value=`12.34.56.78`  context: ...'k5. The VPN server address is 12.34.56.78. Please use the employee ID 2'...
- `nemotron-en-d6acf3d8d0494e259f02e28be2d54a5f` [regex] value=`2024-01-16`  context: ...' Recruitment of Participants: 2024-01-16 to 2024-02-15\n- Implementatio'...
- `nemotron-en-d6acf3d8d0494e259f02e28be2d54a5f` [regex] value=`2024-02-16`  context: ...'\n- Implementation of Program: 2024-02-16 to 2024-06-15\n- Evaluation an'...
- `nemotron-en-d6acf3d8d0494e259f02e28be2d54a5f` [regex] value=`2024-06-16`  context: ...'5\n- Evaluation and Reporting: 2024-06-16 to 2024-07-15\n\n**Expected Out'...
- `nemotron-en-3ef521773dfa4727888cf20ca3717871` [regex] value=`1310-73-2`  context: ...'ts: Sodium Hydroxide (CAS No. 1310-73-2)\n\n**Section 4: First-Aid Meas'...

### `[PERSONAL_ID]`
- `nemotron-en-31ee8fd013e4445d83d6f15169f76ba7` [opf] value=`80431726`  context: ...'er certificate license number 80431726, was completed on 15/07/2024.'...
- `nemotron-en-077ca101faf34b179e9025cb741888ff` [opf] value=`X92837465183`  context: ...'w. My biometric identifier is X92837465183.'...
- `nemotron-en-fc306c761d374f9080512075154e49aa` [opf] value=`2F57-RE4-KD91`  context: ...'l\n\n- **Tracking Number**:\n  - 2F57-RE4-KD91\n\n**Terms and Conditions**\n\n- '...
- `nemotron-en-32687e8f67c448c4864c4f111f3dd7f2` [opf] value=`84592173`  context: ...'**\n\n**Certification Number:** 84592173\n\n**Issued Date:** 03/15/2024\n'...
- `nemotron-en-32687e8f67c448c4864c4f111f3dd7f2` [opf] value=`84592173`  context: ...'Certificate License Number:** 84592173'...

### `[PERSON_NAME]`
- `nemotron-en-d204231bd08a4f0896ce5cd125b79465` [opf] value=`daxaben_coder`  context: ...'il network:\n\nThe user name is daxaben_coder. The password is G9t$fR2mXk5.'...
- `nemotron-en-5344e719fbb24d86bbb80212eabfbab2` [opf] value=`Impact Foundation`  context: ...' 07/15/2024 between Community Impact Foundation and Elisabeth Setzer. Elisabe'...
- `nemotron-en-722a4838747845dfa1fe6eb666ac9372` [opf] value=`VitalisPharma`  context: ...'e clinical trial conducted by VitalisPharma, we received an adverse event'...
- `nemotron-en-4d8c14613e2b489688b54575a26d515b` [opf] value=`Harrison &`  context: ...'ies, the licensee may contact Harrison & Associates via fax at 479-772'...
- `nemotron-en-b30a384018af4fb6a7d490a9a88ae8c8` [opf] value=`rachel.milliner`  context: ...'redentials. Your user name is rachel.milliner. Your password is Michael1995'...

### `[PHONE]`
- `nemotron-en-aa68de98f33149b08b231a63a9dc0c6c` [regex] value=`0004382965`  context: ...'plan beneficiary number is PA-0004382965.'...
- `nemotron-en-31ee8fd013e4445d83d6f15169f76ba7` [regex] value=`0004372819`  context: ...'le. The medical record number 0004372819 was assigned to track the pro'...
- `nemotron-en-722a4838747845dfa1fe6eb666ac9372` [regex] value=`0008374925`  context: ...'for the medical record number 0008374925. The event was logged at 7:22'...
- `nemotron-en-aa44bfd07cd340b788cf70f3dcae7dc6` [regex] value=`7256198345`  context: ...' the biometric identifier BIO-7256198345.'...
- `nemotron-en-4d8c14613e2b489688b54575a26d515b` [regex] value=`479-772-7297`  context: ...'rison & Associates via fax at 479-772-7297.'...

### `[SECRET]`
- `nemotron-en-0f93bba77e674e24b24ec3190b0764e6` [opf] value=`5f9f1b9b8c6e8b7a3d2f4b7a`  context: ...'   |\n| Unique ID            | 5f9f1b9b8c6e8b7a3d2f4b7a      |\n| Customer ID         '...
- `nemotron-en-34d619d5f0624c61a05408203d242f2d` [opf] value=`b3c9e3e0-4c6f-4a1e-9e8c-4c7a88c25759`  context: ...'A48937216, device identifier: b3c9e3e0-4c6f-4a1e-9e8c-4c7a88c25759. |\n| 2024-06-01T18:42:15 | al'...
- `nemotron-en-34d619d5f0624c61a05408203d242f2d` [opf] value=`18:42:15`  context: ...'-4c7a88c25759. |\n| 2024-06-01T18:42:15 | alexander92   | Facial Reco'...
- `nemotron-en-4df2ece312074e1aaf3947c99424fbd0` [opf] value=`35b7e38b241d221b5f6822f95031b91b05c9a3f38e78c69d29b3e11589a614e6`  context: ...'y.com\n2. Enter the unique ID: 35b7e38b241d221b5f6822f95031b91b05c9a3f38e78c69d29b3e11589a614e6\n3. Create a new password. Ens'...
- `nemotron-en-5d036b03b45e4e79b40f258943042bd3` [opf] value=`=jhb7f5xkp2m8`  context: ...'the **http cookie** csrf_token=jhb7f5xkp2m8; Path=/; Secure for secure ac'...

### `[STREET_ADDRESS]`
- `nemotron-en-ae3fd891114247358a18ebe05f3177ca` [opf] value=`28.6432 N, 81.2886 W.`  context: ...'a1e2 is located at coordinate 28.6432 N, 81.2886 W. This device is a Samsung Gala'...
- `nemotron-en-fc306c761d374f9080512075154e49aa` [opf] value=`41.4145, -72.2991`  context: ...'estination Coordinates**:\n  - 41.4145, -72.2991\n\n- **Shipping Method**:\n  - E'...
- `nemotron-en-2ee34fdf914241a39459c1f8cda26aeb` [opf] value=`40.0123, -89.0987`  context: ...'elp farmers at the coordinate 40.0123, -89.0987, optimize their agricultural '...
- `nemotron-en-7a3973949ee347ef9ede5028939c1ebb` [opf] value=`37.456789,-78.234567`  context: ...'embly point at the coordinate 37.456789,-78.234567.\n\nFor more detailed informati'...
- `nemotron-en-3566f15f70ef46448deafe82853668cc` [opf] value=`946931`  context: ...' related to this agreement is 946931.'...


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
- `nemotron-en-bf86531e50484fefb2d8d9d7499f422d` value=`Ashley Tapper`  context: ...' Fox News**\n\n**Subheadline:** Ashley Tapper to Lead Full-Time English-Spe'...

### `[SECRET]`
- `nemotron-en-b1b29d0311c64cccad49121a6af1d607` value=`Not Provided`  context: ...'liance Officer:**\n- **Name:** Not Provided\n- **Email:** Not Provided\n- *'...
- `nemotron-en-b1b29d0311c64cccad49121a6af1d607` value=`Not Provided`  context: ...':** Not Provided\n- **Email:** Not Provided\n- **Password:** password123'...
- `nemotron-en-041df2b4f38c49f4b02d25008d8a1894` value=`River45$`  context: ...'p Farm Co. using the password River45$ to authenticate the digital s'...
- `nemotron-en-ae7274ec5ba841fdbeb20d0448fbe6d7` value=`robust password`  context: ...'yption key, often requiring a robust password such as Ocean@2023 to protect'...

