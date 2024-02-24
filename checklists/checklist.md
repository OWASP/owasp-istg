# Testing Checklist

The following is the list of items to test during the assessment:

Note: The `Status` column can be set for values similar to "Pass", "Fail", "N/A".


## Processing Units (ISTG-PROC)
|Test ID|Test Name|Status|Notes|
|-|-|-|-|
|**ISTG-PROC-AUTHZ**|**Authorization**|||
|ISTG-PROC-AUTHZ-001|Unauthorized Access to the Processing Unit|||
|ISTG-PROC-AUTHZ-002|Privilege Escalation|||
|**ISTG-PROC-LOGIC**|**Business Logic**|||
|ISTG-PROC-LOGIC-001|Insecure Implementation of Instructions|||
|**ISTG-PROC-SIDEC**|**Side-Channel Attacks**|||
|ISTG-PROC-SIDEC-001|Insufficient Protection Against Side-Channel Attacks|||

## Memory (ISTG-MEM)
|Test ID|Test Name|Status|Notes|
|-|-|-|-|
|**ISTG-MEM-INFO**|**Information Gathering**|||
|ISTG-MEM-INFO-001|Disclosure of Source Code and Binaries|||
|ISTG-MEM-INFO-002|Disclosure of Implementation Details|||
|ISTG-MEM-INFO-003|Disclosure of Ecosystem Details|||
|ISTG-MEM-INFO-004|Disclosure of User Data|||
|**ISTG-MEM-SCRT**|**Secrets**|||
|ISTG-MEM-SCRT-001|Unencrypted Storage of Secrets|||
|**ISTG-MEM-CRYPT**|**Cryptography**|||
|ISTG-MEM-CRYPT-001|Usage of Weak Cryptographic Algorithms|||

## Firmware (ISTG-FW)
|Test ID|Test Name|Status|Notes|
|-|-|-|-|
|**ISTG-FW-INFO**|**Information Gathering**|||
|ISTG-FW-INFO-001|Disclosure of Source Code and Binaries|||
|ISTG-FW-INFO-002|Disclosure of Implementation Details|||
|ISTG-FW-INFO-003|Disclosure of Ecosystem Details|||
|**ISTG-FW-CONF**|**Configuration and Patch Management**|||
|ISTG-FW-CONF-001|Usage of Outdated Software|||
|ISTG-FW-CONF-002|Presence of Unnecessary Software and Functionalities|||
|**ISTG-FW-SCRT**|**Secrets**|||
|ISTG-FW-SCRT-001|Secrets Stored in Public Storage|||
|ISTG-FW-SCRT-002|Unencrypted Storage of Secrets|||
|ISTG-FW-SCRT-003|Usage of Hardcoded Secrets|||
|**ISTG-FW-CRYPT**|**Cryptography**|||
|ISTG-FW-CRYPT-001|Usage of Weak Cryptographic Algorithms|||

### Installed Firmware (ISTG-FW[INST])
|Test ID|Test Name|Status|Notes|
|-|-|-|-|
|**ISTG-FW[INST]-AUTHZ**|**Authorization**|||
|ISTG-FW[INST]-AUTHZ-001|Unauthorized Access to the Firmware|||
|ISTG-FW[INST]-AUTHZ-002|Privilege Escalation|||
|**ISTG-FW[INST]-INFO**|**Information Gathering**|||
|ISTG-FW[INST]-INFO-001|Disclosure of User Data|||
|**ISTG-FW[INST]-CRYPT**|**Cryptography**|||
|ISTG-FW[INST]-CRYPT-001|Insufficient Verification of the Bootloader Signature|||

### Firmware Update Mechanism (ISTG-FW[UPDT])
|Test ID|Test Name|Status|Notes|
|-|-|-|-|
|**ISTG-FW[UPDT]-AUTHZ**|**Authorization**|||
|ISTG-FW[UPDT]-AUTHZ-001|Unauthorized Firmware Update|||
|**ISTG-FW[UPDT]-CRYPT**|**Cryptography**|||
|ISTG-FW[UPDT]-CRYPT-001|Insufficient Firmware Update Signature|||
|ISTG-FW[UPDT]-CRYPT-002|Insufficient Firmware Update Encryption|||
|ISTG-FW[UPDT]-CRYPT-003|Insecure Transmission of the Firmware Update|||
|ISTG-FW[UPDT]-CRYPT-004|Insufficient Verification of the Firmware Update Signature|||
|**ISTG-FW[UPDT]-LOGIC**|**Business Logic**|||
|ISTG-FW[UPDT]-LOGIC-001|Insufficient Rollback Protection|||

## Data Exchange Services (ISTG-DES)
|Test ID|Test Name|Status|Notes|
|-|-|-|-|
|**ISTG-DES-AUTHZ**|**Authorization**|||
|ISTG-DES-AUTHZ-001|Unauthorized Access to the Data Exchange Service|||
|ISTG-DES-AUTHZ-002|Privilege Escalation|||
|**ISTG-DES-INFO**|**Information Gathering**|||
|ISTG-DES-INFO-001|Disclosure of Implementation Details|||
|ISTG-DES-INFO-002|Disclosure of Ecosystem Details|||
|ISTG-DES-INFO-003|Disclosure of User Data|||
|**ISTG-DES-CONF**|**Configuration and Patch Management**|||
|ISTG-DES-CONF-001|Usage of Outdated Software|||
|ISTG-DES-CONF-002|Presence of Unnecessary Software and Functionalities|||
|**ISTG-DES-SCRT**|**Secrets**|||
|ISTG-DES-SCRT-001|Access to Confidential Data|||
|**ISTG-DES-CRYPT**|**Cryptography**|||
|ISTG-DES-CRYPT-001|Usage of Weak Cryptographic Algorithms|||
|**ISTG-DES-LOGIC**|**Business Logic**|||
|ISTG-DES-LOGIC-001|Circumvention of the Intended Business Logic|||
|**ISTG-DES-INPV**|**Input Validation**|||
|ISTG-DES-INPV-001|Insufficient Input Validation|||
|ISTG-DES-INPV-002|Code or Command Injection|||

## Internal Interfaces (ISTG-INT)
|Test ID|Test Name|Status|Notes|
|-|-|-|-|
|**ISTG-INT-AUTHZ**|**Authorization**|||
|ISTG-INT-AUTHZ-001|Unauthorized Access to the Interface|||
|ISTG-INT-AUTHZ-002|Privilege Escalation|||
|**ISTG-INT-INFO**|**Information Gathering**|||
|ISTG-INT-INFO-001|Disclosure of Implementation Details|||
|ISTG-INT-INFO-002|Disclosure of Ecosystem Details|||
|ISTG-INT-INFO-003|Disclosure of User Data|||
|**ISTG-INT-CONF**|**Configuration and Patch Management**|||
|ISTG-INT-CONF-001|Usage of Outdated Software|||
|ISTG-INT-CONF-002|Presence of Unnecessary Software and Functionalities|||
|**ISTG-INT-SCRT**|**Secrets**|||
|ISTG-INT-SCRT-001|Access to Confidential Data|||
|**ISTG-INT-CRYPT**|**Cryptography**|||
|ISTG-INT-CRYPT-001|Usage of Weak Cryptographic Algorithms|||
|**ISTG-INT-LOGIC**|**Business Logic**|||
|ISTG-INT-LOGIC-001|Circumvention of the Intended Business Logic|||
|**ISTG-INT-INPV**|**Input Validation**|||
|ISTG-INT-INPV-001|Insufficient Input Validation|||
|ISTG-INT-INPV-002|Code or Command Injection|||

## Physical Interfaces (ISTG-PHY)
|Test ID|Test Name|Status|Notes|
|-|-|-|-|
|**ISTG-PHY-AUTHZ**|**Authorization**|||
|ISTG-PHY-AUTHZ-001|Unauthorized Access to the Interface|||
|ISTG-PHY-AUTHZ-002|Privilege Escalation|||
|**ISTG-PHY-INFO**|**Information Gathering**|||
|ISTG-PHY-INFO-001|Disclosure of Implementation Details|||
|ISTG-PHY-INFO-002|Disclosure of Ecosystem Details|||
|ISTG-PHY-INFO-003|Disclosure of User Data|||
|**ISTG-PHY-CONF**|**Configuration and Patch Management**|||
|ISTG-PHY-CONF-001|Usage of Outdated Software|||
|ISTG-PHY-CONF-002|Presence of Unnecessary Software and Functionalities|||
|**ISTG-PHY-SCRT**|**Secrets**|||
|ISTG-PHY-SCRT-001|Access to Confidential Data|||
|**ISTG-PHY-CRYPT**|**Cryptography**|||
|ISTG-PHY-CRYPT-001|Usage of Weak Cryptographic Algorithms|||
|**ISTG-PHY-LOGIC**|**Business Logic**|||
|ISTG-PHY-LOGIC-001|Circumvention of the Intended Business Logic|||
|**ISTG-PHY-INPV**|**Input Validation**|||
|ISTG-PHY-INPV-001|Insufficient Input Validation|||
|ISTG-PHY-INPV-002|Code or Command Injection|||

## Wireless Interfaces (ISTG-WRLS)
|Test ID|Test Name|Status|Notes|
|-|-|-|-|
|**ISTG-WRLS-AUTHZ**|**Authorization**|||
|ISTG-WRLS-AUTHZ-001|Unauthorized Access to the Interface|||
|ISTG-WRLS-AUTHZ-002|Privilege Escalation|||
|**ISTG-WRLS-INFO**|**Information Gathering**|||
|ISTG-WRLS-INFO-001|Disclosure of Implementation Details|||
|ISTG-WRLS-INFO-002|Disclosure of Ecosystem Details|||
|ISTG-WRLS-INFO-003|Disclosure of User Data|||
|**ISTG-WRLS-CONF**|**Configuration and Patch Management**|||
|ISTG-WRLS-CONF-001|Usage of Outdated Software|||
|ISTG-WRLS-CONF-002|Presence of Unnecessary Software and Functionalities|||
|**ISTG-WRLS-SCRT**|**Secrets**|||
|ISTG-WRLS-SCRT-001|Access to Confidential Data|||
|**ISTG-WRLS-CRYPT**|**Cryptography**|||
|ISTG-WRLS-CRYPT-001|Usage of Weak Cryptographic Algorithms|||
|**ISTG-WRLS-LOGIC**|**Business Logic**|||
|ISTG-WRLS-LOGIC-001|Circumvention of the Intended Business Logic|||
|**ISTG-WRLS-INPV**|**Input Validation**|||
|ISTG-WRLS-INPV-001|Insufficient Input Validation|||
|ISTG-WRLS-INPV-002|Code or Command Injection|||

## User Interfaces (ISTG-UI)
|Test ID|Test Name|Status|Notes|
|-|-|-|-|
|**ISTG-UI-AUTHZ**|**Authorization**|||
|ISTG-UI-AUTHZ-001|Unauthorized Access to the Interface|||
|ISTG-UI-AUTHZ-002|Privilege Escalation|||
|**ISTG-UI-INFO**|**Information Gathering**|||
|ISTG-UI-INFO-001|Disclosure of Implementation Details|||
|ISTG-UI-INFO-002|Disclosure of Ecosystem Details|||
|ISTG-UI-INFO-003|Disclosure of User Data|||
|**ISTG-UI-CONF**|**Configuration and Patch Management**|||
|ISTG-UI-CONF-001|Usage of Outdated Software|||
|ISTG-UI-CONF-002|Presence of Unnecessary Software and Functionalities|||
|**ISTG-UI-SCRT**|**Secrets**|||
|ISTG-UI-SCRT-001|Access to Confidential Data|||
|**ISTG-UI-CRYPT**|**Cryptography**|||
|ISTG-UI-CRYPT-001|Usage of Weak Cryptographic Algorithms|||
|**ISTG-UI-LOGIC**|**Business Logic**|||
|ISTG-UI-LOGIC-001|Circumvention of the Intended Business Logic|||
|**ISTG-UI-INPV**|**Input Validation**|||
|ISTG-UI-INPV-001|Insufficient Input Validation|||
|ISTG-UI-INPV-002|Code or Command Injection|||
