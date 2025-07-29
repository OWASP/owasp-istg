# Testing Checklist with Compliance Framework Mappings

The following is the list of items to test during the assessment with mappings to major compliance frameworks:

**Compliance Frameworks:**
- **IEC 62443 Industrial Automation and Control Systems Security** (2024): Security requirements for Industrial Automation and Control Systems (IACS)
- **NIST Cybersecurity Framework 2.0 + IoT Guidance** (2.0 (2024)): US Federal cybersecurity framework with IoT-specific guidance (SP 800-213 series)
- **EU Radio Equipment Directive** (2024 (effective August 2025)): EU security requirements for wireless devices
- **EU Cyber Resilience Act + ETSI EN 303 645** (2024+): EU cybersecurity requirements for consumer IoT devices

Note: The `Status` column can be set for values similar to "Pass", "Fail", "N/A".


## Processing Units (ISTG-PROC)
|Test ID|Test Name|Status|Notes|IEC 62443|NIST CSF 2.0|EU RED|EU CRA/ETSI|
|-|-|-|-|-|-|-|-|
|**ISTG-PROC-AUTHZ**|**Authorization**|||||||||
|ISTG-PROC-AUTHZ-001|Unauthorized Access to the Processing Unit|||SL-2|Protect|N/A|Yes|
|ISTG-PROC-AUTHZ-002|Privilege Escalation|||SL-2|Protect|N/A|Yes|
|**ISTG-PROC-LOGIC**|**Business Logic**|||||||||
|ISTG-PROC-LOGIC-001|Insecure Implementation of Instructions|||SL-2|Protect|N/A|Yes|
|**ISTG-PROC-SIDEC**|**Side-Channel Attacks**|||||||||
|ISTG-PROC-SIDEC-001|Insufficient Protection Against Side-Channel Attacks|||SL-3|Protect|N/A|Yes|

## Memory (ISTG-MEM)
|Test ID|Test Name|Status|Notes|IEC 62443|NIST CSF 2.0|EU RED|EU CRA/ETSI|
|-|-|-|-|-|-|-|-|
|**ISTG-MEM-INFO**|**Information Gathering**|||||||||
|ISTG-MEM-INFO-001|Disclosure of Source Code and Binaries|||SL-1|Protect|N/A|Yes|
|ISTG-MEM-INFO-002|Disclosure of Implementation Details|||SL-1|Protect|N/A|Yes|
|ISTG-MEM-INFO-003|Disclosure of Ecosystem Details|||SL-2|Protect|3.3(d)|Yes|
|ISTG-MEM-INFO-004|Disclosure of User Data|||SL-2|Protect|3.3(e)|Yes|
|**ISTG-MEM-SCRT**|**Secrets**|||||||||
|ISTG-MEM-SCRT-001|Unencrypted Storage of Secrets|||SL-2|Protect|3.3(e)|Yes|
|**ISTG-MEM-CRYPT**|**Cryptography**|||||||||
|ISTG-MEM-CRYPT-001|Usage of Weak Cryptographic Algorithms|||SL-2|Protect|3.3(e)|Yes|

## Firmware (ISTG-FW)
|Test ID|Test Name|Status|Notes|IEC 62443|NIST CSF 2.0|EU RED|EU CRA/ETSI|
|-|-|-|-|-|-|-|-|
|**ISTG-FW-INFO**|**Information Gathering**|||||||||
|ISTG-FW-INFO-001|Disclosure of Source Code and Binaries|||SL-1|TBD|N/A|TBD|
|ISTG-FW-INFO-002|Disclosure of Implementation Details|||SL-1|TBD|N/A|TBD|
|ISTG-FW-INFO-003|Disclosure of Ecosystem Details|||SL-1|TBD|N/A|TBD|
|**ISTG-FW-CONF**|**Configuration and Patch Management**|||||||||
|ISTG-FW-CONF-001|Usage of Outdated Software|||SL-1|TBD|N/A|TBD|
|ISTG-FW-CONF-002|Presence of Unnecessary Software and Functionalities|||SL-1|TBD|N/A|TBD|
|**ISTG-FW-SCRT**|**Secrets**|||||||||
|ISTG-FW-SCRT-001|Secrets Stored in Public Storage|||SL-1|TBD|N/A|TBD|
|ISTG-FW-SCRT-002|Unencrypted Storage of Secrets|||SL-1|TBD|N/A|TBD|
|ISTG-FW-SCRT-003|Usage of Hardcoded Secrets|||SL-1|TBD|N/A|TBD|
|**ISTG-FW-CRYPT**|**Cryptography**|||||||||
|ISTG-FW-CRYPT-001|Usage of Weak Cryptographic Algorithms|||SL-1|TBD|N/A|TBD|

### Installed Firmware (ISTG-FW[INST])
|Test ID|Test Name|Status|Notes|IEC 62443|NIST CSF 2.0|EU RED|EU CRA/ETSI|
|-|-|-|-|-|-|-|-|
|**ISTG-FW[INST]-AUTHZ**|**Authorization**|||||||||
|ISTG-FW[INST]-AUTHZ-001|Unauthorized Access to the Firmware|||SL-1|TBD|N/A|TBD|
|ISTG-FW[INST]-AUTHZ-002|Privilege Escalation|||SL-1|TBD|N/A|TBD|
|**ISTG-FW[INST]-INFO**|**Information Gathering**|||||||||
|ISTG-FW[INST]-INFO-001|Disclosure of User Data|||SL-1|TBD|N/A|TBD|
|**ISTG-FW[INST]-CRYPT**|**Cryptography**|||||||||
|ISTG-FW[INST]-CRYPT-001|Insufficient Verification of the Bootloader Signature|||SL-1|TBD|N/A|TBD|

### Firmware Update Mechanism (ISTG-FW[UPDT])
|Test ID|Test Name|Status|Notes|IEC 62443|NIST CSF 2.0|EU RED|EU CRA/ETSI|
|-|-|-|-|-|-|-|-|
|**ISTG-FW[UPDT]-AUTHZ**|**Authorization**|||||||||
|ISTG-FW[UPDT]-AUTHZ-001|Unauthorized Firmware Update|||SL-1|TBD|N/A|TBD|
|**ISTG-FW[UPDT]-CRYPT**|**Cryptography**|||||||||
|ISTG-FW[UPDT]-CRYPT-001|Insufficient Firmware Update Signature|||SL-1|TBD|N/A|TBD|
|ISTG-FW[UPDT]-CRYPT-002|Insufficient Firmware Update Encryption|||SL-1|TBD|N/A|TBD|
|ISTG-FW[UPDT]-CRYPT-003|Insecure Transmission of the Firmware Update|||SL-1|TBD|N/A|TBD|
|ISTG-FW[UPDT]-CRYPT-004|Insufficient Verification of the Firmware Update Signature|||SL-1|TBD|N/A|TBD|
|**ISTG-FW[UPDT]-LOGIC**|**Business Logic**|||||||||
|ISTG-FW[UPDT]-LOGIC-001|Insufficient Rollback Protection|||SL-1|TBD|N/A|TBD|

## Data Exchange Services (ISTG-DES)
|Test ID|Test Name|Status|Notes|IEC 62443|NIST CSF 2.0|EU RED|EU CRA/ETSI|
|-|-|-|-|-|-|-|-|
|**ISTG-DES-AUTHZ**|**Authorization**|||||||||
|ISTG-DES-AUTHZ-001|Unauthorized Access to the Data Exchange Service|||SL-1|TBD|N/A|TBD|
|ISTG-DES-AUTHZ-002|Privilege Escalation|||SL-1|TBD|N/A|TBD|
|**ISTG-DES-INFO**|**Information Gathering**|||||||||
|ISTG-DES-INFO-001|Disclosure of Implementation Details|||SL-1|TBD|N/A|TBD|
|ISTG-DES-INFO-002|Disclosure of Ecosystem Details|||SL-1|TBD|N/A|TBD|
|ISTG-DES-INFO-003|Disclosure of User Data|||SL-1|TBD|N/A|TBD|
|**ISTG-DES-CONF**|**Configuration and Patch Management**|||||||||
|ISTG-DES-CONF-001|Usage of Outdated Software|||SL-1|TBD|N/A|TBD|
|ISTG-DES-CONF-002|Presence of Unnecessary Software and Functionalities|||SL-1|TBD|N/A|TBD|
|**ISTG-DES-SCRT**|**Secrets**|||||||||
|ISTG-DES-SCRT-001|Access to Confidential Data|||SL-1|TBD|N/A|TBD|
|**ISTG-DES-CRYPT**|**Cryptography**|||||||||
|ISTG-DES-CRYPT-001|Usage of Weak Cryptographic Algorithms|||SL-1|TBD|N/A|TBD|
|**ISTG-DES-LOGIC**|**Business Logic**|||||||||
|ISTG-DES-LOGIC-001|Circumvention of the Intended Business Logic|||SL-1|TBD|N/A|TBD|
|**ISTG-DES-INPV**|**Input Validation**|||||||||
|ISTG-DES-INPV-001|Insufficient Input Validation|||SL-1|TBD|N/A|TBD|
|ISTG-DES-INPV-002|Code or Command Injection|||SL-1|TBD|N/A|TBD|

## Internal Interfaces (ISTG-INT)
|Test ID|Test Name|Status|Notes|IEC 62443|NIST CSF 2.0|EU RED|EU CRA/ETSI|
|-|-|-|-|-|-|-|-|
|**ISTG-INT-AUTHZ**|**Authorization**|||||||||
|ISTG-INT-AUTHZ-001|Unauthorized Access to the Interface|||SL-1|TBD|N/A|TBD|
|ISTG-INT-AUTHZ-002|Privilege Escalation|||SL-1|TBD|N/A|TBD|
|**ISTG-INT-INFO**|**Information Gathering**|||||||||
|ISTG-INT-INFO-001|Disclosure of Implementation Details|||SL-1|TBD|N/A|TBD|
|ISTG-INT-INFO-002|Disclosure of Ecosystem Details|||SL-1|TBD|N/A|TBD|
|ISTG-INT-INFO-003|Disclosure of User Data|||SL-1|TBD|N/A|TBD|
|**ISTG-INT-CONF**|**Configuration and Patch Management**|||||||||
|ISTG-INT-CONF-001|Usage of Outdated Software|||SL-1|TBD|N/A|TBD|
|ISTG-INT-CONF-002|Presence of Unnecessary Software and Functionalities|||SL-1|TBD|N/A|TBD|
|**ISTG-INT-SCRT**|**Secrets**|||||||||
|ISTG-INT-SCRT-001|Access to Confidential Data|||SL-1|TBD|N/A|TBD|
|**ISTG-INT-CRYPT**|**Cryptography**|||||||||
|ISTG-INT-CRYPT-001|Usage of Weak Cryptographic Algorithms|||SL-1|TBD|N/A|TBD|
|**ISTG-INT-LOGIC**|**Business Logic**|||||||||
|ISTG-INT-LOGIC-001|Circumvention of the Intended Business Logic|||SL-1|TBD|N/A|TBD|
|**ISTG-INT-INPV**|**Input Validation**|||||||||
|ISTG-INT-INPV-001|Insufficient Input Validation|||SL-1|TBD|N/A|TBD|
|ISTG-INT-INPV-002|Code or Command Injection|||SL-1|TBD|N/A|TBD|

## Physical Interfaces (ISTG-PHY)
|Test ID|Test Name|Status|Notes|IEC 62443|NIST CSF 2.0|EU RED|EU CRA/ETSI|
|-|-|-|-|-|-|-|-|
|**ISTG-PHY-AUTHZ**|**Authorization**|||||||||
|ISTG-PHY-AUTHZ-001|Unauthorized Access to the Interface|||SL-1|TBD|N/A|TBD|
|ISTG-PHY-AUTHZ-002|Privilege Escalation|||SL-1|TBD|N/A|TBD|
|**ISTG-PHY-INFO**|**Information Gathering**|||||||||
|ISTG-PHY-INFO-001|Disclosure of Implementation Details|||SL-1|TBD|N/A|TBD|
|ISTG-PHY-INFO-002|Disclosure of Ecosystem Details|||SL-1|TBD|N/A|TBD|
|ISTG-PHY-INFO-003|Disclosure of User Data|||SL-1|TBD|N/A|TBD|
|**ISTG-PHY-CONF**|**Configuration and Patch Management**|||||||||
|ISTG-PHY-CONF-001|Usage of Outdated Software|||SL-1|TBD|N/A|TBD|
|ISTG-PHY-CONF-002|Presence of Unnecessary Software and Functionalities|||SL-1|TBD|N/A|TBD|
|**ISTG-PHY-SCRT**|**Secrets**|||||||||
|ISTG-PHY-SCRT-001|Access to Confidential Data|||SL-1|TBD|N/A|TBD|
|**ISTG-PHY-CRYPT**|**Cryptography**|||||||||
|ISTG-PHY-CRYPT-001|Usage of Weak Cryptographic Algorithms|||SL-1|TBD|N/A|TBD|
|**ISTG-PHY-LOGIC**|**Business Logic**|||||||||
|ISTG-PHY-LOGIC-001|Circumvention of the Intended Business Logic|||SL-1|TBD|N/A|TBD|
|**ISTG-PHY-INPV**|**Input Validation**|||||||||
|ISTG-PHY-INPV-001|Insufficient Input Validation|||SL-1|TBD|N/A|TBD|
|ISTG-PHY-INPV-002|Code or Command Injection|||SL-1|TBD|N/A|TBD|

## Wireless Interfaces (ISTG-WRLS)
|Test ID|Test Name|Status|Notes|IEC 62443|NIST CSF 2.0|EU RED|EU CRA/ETSI|
|-|-|-|-|-|-|-|-|
|**ISTG-WRLS-AUTHZ**|**Authorization**|||||||||
|ISTG-WRLS-AUTHZ-001|Unauthorized Access to the Interface|||SL-1|TBD|Yes|TBD|
|ISTG-WRLS-AUTHZ-002|Privilege Escalation|||SL-1|TBD|Yes|TBD|
|**ISTG-WRLS-INFO**|**Information Gathering**|||||||||
|ISTG-WRLS-INFO-001|Disclosure of Implementation Details|||SL-1|TBD|Yes|TBD|
|ISTG-WRLS-INFO-002|Disclosure of Ecosystem Details|||SL-1|TBD|Yes|TBD|
|ISTG-WRLS-INFO-003|Disclosure of User Data|||SL-1|TBD|Yes|TBD|
|**ISTG-WRLS-CONF**|**Configuration and Patch Management**|||||||||
|ISTG-WRLS-CONF-001|Usage of Outdated Software|||SL-1|TBD|Yes|TBD|
|ISTG-WRLS-CONF-002|Presence of Unnecessary Software and Functionalities|||SL-1|TBD|Yes|TBD|
|**ISTG-WRLS-SCRT**|**Secrets**|||||||||
|ISTG-WRLS-SCRT-001|Access to Confidential Data|||SL-1|TBD|Yes|TBD|
|**ISTG-WRLS-CRYPT**|**Cryptography**|||||||||
|ISTG-WRLS-CRYPT-001|Usage of Weak Cryptographic Algorithms|||SL-1|TBD|Yes|TBD|
|**ISTG-WRLS-LOGIC**|**Business Logic**|||||||||
|ISTG-WRLS-LOGIC-001|Circumvention of the Intended Business Logic|||SL-1|TBD|Yes|TBD|
|**ISTG-WRLS-INPV**|**Input Validation**|||||||||
|ISTG-WRLS-INPV-001|Insufficient Input Validation|||SL-1|TBD|Yes|TBD|
|ISTG-WRLS-INPV-002|Code or Command Injection|||SL-1|TBD|Yes|TBD|

## User Interfaces (ISTG-UI)
|Test ID|Test Name|Status|Notes|IEC 62443|NIST CSF 2.0|EU RED|EU CRA/ETSI|
|-|-|-|-|-|-|-|-|
|**ISTG-UI-AUTHZ**|**Authorization**|||||||||
|ISTG-UI-AUTHZ-001|Unauthorized Access to the Interface|||SL-1|TBD|N/A|TBD|
|ISTG-UI-AUTHZ-002|Privilege Escalation|||SL-1|TBD|N/A|TBD|
|**ISTG-UI-INFO**|**Information Gathering**|||||||||
|ISTG-UI-INFO-001|Disclosure of Implementation Details|||SL-1|TBD|N/A|TBD|
|ISTG-UI-INFO-002|Disclosure of Ecosystem Details|||SL-1|TBD|N/A|TBD|
|ISTG-UI-INFO-003|Disclosure of User Data|||SL-1|TBD|N/A|TBD|
|**ISTG-UI-CONF**|**Configuration and Patch Management**|||||||||
|ISTG-UI-CONF-001|Usage of Outdated Software|||SL-1|TBD|N/A|TBD|
|ISTG-UI-CONF-002|Presence of Unnecessary Software and Functionalities|||SL-1|TBD|N/A|TBD|
|**ISTG-UI-SCRT**|**Secrets**|||||||||
|ISTG-UI-SCRT-001|Access to Confidential Data|||SL-1|TBD|N/A|TBD|
|**ISTG-UI-CRYPT**|**Cryptography**|||||||||
|ISTG-UI-CRYPT-001|Usage of Weak Cryptographic Algorithms|||SL-1|TBD|N/A|TBD|
|**ISTG-UI-LOGIC**|**Business Logic**|||||||||
|ISTG-UI-LOGIC-001|Circumvention of the Intended Business Logic|||SL-1|TBD|N/A|TBD|
|**ISTG-UI-INPV**|**Input Validation**|||||||||
|ISTG-UI-INPV-001|Insufficient Input Validation|||SL-1|TBD|N/A|TBD|
|ISTG-UI-INPV-002|Code or Command Injection|||SL-1|TBD|N/A|TBD|
