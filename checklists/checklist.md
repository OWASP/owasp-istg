# Testing Checklist

The following is the list of items to test during the assessment:

Note: The `Status` column can be set for values similar to "Pass", "Fail", "N/A".


## Processing Units (IOT-PROC)
|Test ID|Test Name|Status|Notes|
|-|-|-|-|
|**IOT-PROC-AUTHZ**|**Authorization**|||
|IOT-PROC-AUTHZ-001|Unauthorized Access to the Processing Unit|||
|IOT-PROC-AUTHZ-002|Privilege Escalation|||
|**IOT-PROC-LOGIC**|**Business Logic**|||
|IOT-PROC-LOGIC-001|Insecure Implementation of Instructions|||
|**IOT-PROC-SIDEC**|**Side-Channel Attacks**|||
|IOT-PROC-SIDEC-001|Insufficient Protection Against Side-Channel Attacks|||

## Memory (IOT-MEM)
|Test ID|Test Name|Status|Notes|
|-|-|-|-|
|**IOT-MEM-INFO**|**Information Gathering**|||
|IOT-MEM-INFO-001|Disclosure of Source Code|||
|IOT-MEM-INFO-002|Disclosure of Implementation Details|||
|IOT-MEM-INFO-003|Disclosure of Ecosystem Details|||
|IOT-MEM-INFO-004|Disclosure of User Data|||
|**IOT-MEM-SCRT**|**Secrets**|||
|IOT-MEM-SCRT-001|Unencrypted Storage of Secrets|||
|**IOT-MEM-CRYPT**|**Cryptography**|||
|IOT-MEM-CRYPT-001|Usage of Weak Cryptographic Algorithms|||

## Firmware (IOT-FW)
|Test ID|Test Name|Status|Notes|
|-|-|-|-|
|**IOT-FW-INFO**|**Information Gathering**|||
|IOT-FW-INFO-001|Disclosure of Source Code|||
|IOT-FW-INFO-002|Disclosure of Implementation Details|||
|IOT-FW-INFO-003|Disclosure of Ecosystem Details|||
|**IOT-FW-CONF**|**Configuration and Patch Management**|||
|IOT-FW-CONF-001|Usage of Outdated Software|||
|IOT-FW-CONF-002|Presence of Unnecessary Software and Functionalities|||
|**IOT-FW-SCRT**|**Secrets**|||
|IOT-FW-SCRT-001|Secrets Stored in Public Storage|||
|IOT-FW-SCRT-002|Unencrypted Storage of Secrets|||
|IOT-FW-SCRT-003|Usage of Hardcoded Secrets|||
|**IOT-FW-CRYPT**|**Cryptography**|||
|IOT-FW-CRYPT-001|Usage of Weak Cryptographic Algorithms|||

### Installed Firmware (IOT-FW[INST])
|Test ID|Test Name|Status|Notes|
|-|-|-|-|
|**IOT-FW[INST]-AUTHZ**|**Authorization**|||
|IOT-FW[INST]-AUTHZ-001|Unauthorized Access to the Firmware|||
|IOT-FW[INST]-AUTHZ-002|Privilege Escalation|||
|**IOT-FW[INST]-INFO**|**Information Gathering**|||
|IOT-FW[INST]-INFO-001|Disclosure of User Data|||
|**IOT-FW[INST]-CRYPT**|**Cryptography**|||
|IOT-FW[INST]-CRYPT-001|Insufficient Verification of the Bootloader Signature|||

### Firmware Update Mechanism (IOT-FW[UPDT])
|Test ID|Test Name|Status|Notes|
|-|-|-|-|
|**IOT-FW[UPDT]-AUTHZ**|**Authorization**|||
|IOT-FW[UPDT]-AUTHZ-001|Unauthorized Firmware Update|||
|**IOT-FW[UPDT]-CRYPT**|**Cryptography**|||
|IOT-FW[UPDT]-CRYPT-001|Insufficient Firmware Update Signature|||
|IOT-FW[UPDT]-CRYPT-002|Insufficient Firmware Update Encryption|||
|IOT-FW[UPDT]-CRYPT-003|Insecure Transmission of the Firmware Update|||
|IOT-FW[UPDT]-CRYPT-004|Insufficient Verification of the Firmware Update Signature|||
|**IOT-FW[UPDT]-LOGIC**|**Business Logic**|||
|IOT-FW[UPDT]-LOGIC-001|Insufficient Rollback Protection|||

## Data Exchange Services (IOT-DES)
|Test ID|Test Name|Status|Notes|
|-|-|-|-|
|**IOT-DES-AUTHZ**|**Authorization**|||
|IOT-DES-AUTHZ-001|Unauthorized Access to the Data Exchange Service|||
|IOT-DES-AUTHZ-002|Privilege Escalation|||
|**IOT-DES-INFO**|**Information Gathering**|||
|IOT-DES-INFO-001|Disclosure of Implementation Details|||
|IOT-DES-INFO-002|Disclosure of Ecosystem Details|||
|IOT-DES-INFO-003|Disclosure of User Data|||
|**IOT-DES-CONF**|**Configuration and Patch Management**|||
|IOT-DES-CONF-001|Usage of Outdated Software|||
|IOT-DES-CONF-002|Presence of Unnecessary Software and Functionalities|||
|**IOT-DES-SCRT**|**Secrets**|||
|IOT-DES-SCRT-001|Access to Confidential Data|||
|**IOT-DES-CRYPT**|**Cryptography**|||
|IOT-DES-CRYPT-001|Usage of Weak Cryptographic Algorithms|||
|**IOT-DES-LOGIC**|**Business Logic**|||
|IOT-DES-LOGIC-001|Circumvention of the Intended Business Logic|||
|**IOT-DES-INVAL**|**Input Validation**|||
|IOT-DES-INVAL-001|Insufficient Input Validation|||
|IOT-DES-INVAL-002|Code or Command Injection|||

## Internal Interfaces (IOT-INT)
|Test ID|Test Name|Status|Notes|
|-|-|-|-|
|**IOT-INT-AUTHZ**|**Authorization**|||
|IOT-INT-AUTHZ-001|Unauthorized Access to the Interface|||
|IOT-INT-AUTHZ-002|Privilege Escalation|||
|**IOT-INT-INFO**|**Information Gathering**|||
|IOT-INT-INFO-001|Disclosure of Implementation Details|||
|IOT-INT-INFO-002|Disclosure of Ecosystem Details|||
|IOT-INT-INFO-003|Disclosure of User Data|||
|**IOT-INT-CONF**|**Configuration and Patch Management**|||
|IOT-INT-CONF-001|Usage of Outdated Software|||
|IOT-INT-CONF-002|Presence of Unnecessary Software and Functionalities|||
|**IOT-INT-SCRT**|**Secrets**|||
|IOT-INT-SCRT-001|Access to Confidential Data|||
|**IOT-INT-CRYPT**|**Cryptography**|||
|IOT-INT-CRYPT-001|Usage of Weak Cryptographic Algorithms|||
|**IOT-INT-LOGIC**|**Business Logic**|||
|IOT-INT-LOGIC-001|Circumvention of the Intended Business Logic|||
|**IOT-INT-INVAL**|**Input Validation**|||
|IOT-INT-INVAL-001|Insufficient Input Validation|||
|IOT-INT-INVAL-002|Code or Command Injection|||

## Physical Interfaces (IOT-PHY)
|Test ID|Test Name|Status|Notes|
|-|-|-|-|
|**IOT-PHY-AUTHZ**|**Authorization**|||
|IOT-PHY-AUTHZ-001|Unauthorized Access to the Interface|||
|IOT-PHY-AUTHZ-002|Privilege Escalation|||
|**IOT-PHY-INFO**|**Information Gathering**|||
|IOT-PHY-INFO-001|Disclosure of Implementation Details|||
|IOT-PHY-INFO-002|Disclosure of Ecosystem Details|||
|IOT-PHY-INFO-003|Disclosure of User Data|||
|**IOT-PHY-CONF**|**Configuration and Patch Management**|||
|IOT-PHY-CONF-001|Usage of Outdated Software|||
|IOT-PHY-CONF-002|Presence of Unnecessary Software and Functionalities|||
|**IOT-PHY-SCRT**|**Secrets**|||
|IOT-PHY-SCRT-001|Access to Confidential Data|||
|**IOT-PHY-CRYPT**|**Cryptography**|||
|IOT-PHY-CRYPT-001|Usage of Weak Cryptographic Algorithms|||
|**IOT-PHY-LOGIC**|**Business Logic**|||
|IOT-PHY-LOGIC-001|Circumvention of the Intended Business Logic|||
|**IOT-PHY-INVAL**|**Input Validation**|||
|IOT-PHY-INVAL-001|Insufficient Input Validation|||
|IOT-PHY-INVAL-002|Code or Command Injection|||

## Wireless Interfaces (IOT-WRLS)
|Test ID|Test Name|Status|Notes|
|-|-|-|-|
|**IOT-WRLS-AUTHZ**|**Authorization**|||
|IOT-WRLS-AUTHZ-001|Unauthorized Access to the Interface|||
|IOT-WRLS-AUTHZ-002|Privilege Escalation|||
|**IOT-WRLS-INFO**|**Information Gathering**|||
|IOT-WRLS-INFO-001|Disclosure of Implementation Details|||
|IOT-WRLS-INFO-002|Disclosure of Ecosystem Details|||
|IOT-WRLS-INFO-003|Disclosure of User Data|||
|**IOT-WRLS-CONF**|**Configuration and Patch Management**|||
|IOT-WRLS-CONF-001|Usage of Outdated Software|||
|IOT-WRLS-CONF-002|Presence of Unnecessary Software and Functionalities|||
|**IOT-WRLS-SCRT**|**Secrets**|||
|IOT-WRLS-SCRT-001|Access to Confidential Data|||
|**IOT-WRLS-CRYPT**|**Cryptography**|||
|IOT-WRLS-CRYPT-001|Usage of Weak Cryptographic Algorithms|||
|**IOT-WRLS-LOGIC**|**Business Logic**|||
|IOT-WRLS-LOGIC-001|Circumvention of the Intended Business Logic|||
|**IOT-WRLS-INVAL**|**Input Validation**|||
|IOT-WRLS-INVAL-001|Insufficient Input Validation|||
|IOT-WRLS-INVAL-002|Code or Command Injection|||

## User Interfaces (IOT-UI)
|Test ID|Test Name|Status|Notes|
|-|-|-|-|
|**IOT-UI-AUTHZ**|**Authorization**|||
|IOT-UI-AUTHZ-001|Unauthorized Access to the Interface|||
|IOT-UI-AUTHZ-002|Privilege Escalation|||
|**IOT-UI-INFO**|**Information Gathering**|||
|IOT-UI-INFO-001|Disclosure of Implementation Details|||
|IOT-UI-INFO-002|Disclosure of Ecosystem Details|||
|IOT-UI-INFO-003|Disclosure of User Data|||
|**IOT-UI-CONF**|**Configuration and Patch Management**|||
|IOT-UI-CONF-001|Usage of Outdated Software|||
|IOT-UI-CONF-002|Presence of Unnecessary Software and Functionalities|||
|**IOT-UI-SCRT**|**Secrets**|||
|IOT-UI-SCRT-001|Access to Confidential Data|||
|**IOT-UI-CRYPT**|**Cryptography**|||
|IOT-UI-CRYPT-001|Usage of Weak Cryptographic Algorithms|||
|**IOT-UI-LOGIC**|**Business Logic**|||
|IOT-UI-LOGIC-001|Circumvention of the Intended Business Logic|||
|**IOT-UI-INVAL**|**Input Validation**|||
|IOT-UI-INVAL-001|Insufficient Input Validation|||
|IOT-UI-INVAL-002|Code or Command Injection|||
