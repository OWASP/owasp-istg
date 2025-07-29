# OWASP ISTG Quick Start Guide: EU Radio Equipment Directive (RED)

## Overview

This quick start guide focuses on wireless IoT device testing for EU Radio Equipment Directive compliance. It prioritizes test cases addressing the three core cybersecurity articles effective August 2025.

**Target Audience:** Wireless device manufacturers, EU importers, IoT device certifiers

**Compliance Scope:** EU RED Articles 3.3(d), 3.3(e), 3.3(f) + harmonized standards EN 18031 series

**Deadline:** Mandatory compliance for wireless devices sold in EU from August 1, 2025

## RED Cybersecurity Articles

### Article 3.3(d): Network Protection (HIGH PRIORITY)
**Objective:** Prevent disruption to communication networks

#### Applicable Test Cases:
- **ISTG-MEM-INFO-003** - Disclosure of Ecosystem Details
  - **Focus:** Network topology, infrastructure details that could enable network attacks
  - **Standard:** EN 18031-1:2024 (Internet-connected radio equipment)
  - **Risk:** Network abuse, DoS attacks, infrastructure mapping

- **ISTG-WRLS-LOGIC-001** - Circumvention of Intended Business Logic
  - **Focus:** Wireless protocol manipulation, network flooding
  - **Testing:** RF signal analysis, protocol fuzzing
  - **Priority:** Critical for network stability

#### Network Protection Requirements:
- **Prevent network flooding:** Device cannot generate excessive traffic
- **Avoid protocol abuse:** Proper implementation of wireless standards  
- **Resource consumption limits:** Device respects network capacity
- **Infrastructure protection:** No disclosure of network architecture

### Article 3.3(e): Personal Data Protection (CRITICAL PRIORITY)
**Objective:** Secure handling of personal data, traffic data, and location data

#### Applicable Test Cases:
- **ISTG-MEM-INFO-004** - Disclosure of User Data
  - **Focus:** Personal information, location data, usage patterns
  - **Standard:** EN 18031-2:2024 (Devices processing personal data)
  - **Risk:** GDPR violations, privacy breaches

- **ISTG-MEM-SCRT-001** - Unencrypted Storage of Secrets
  - **Focus:** Personal data encryption, authentication credentials
  - **Testing:** Data extraction, memory analysis
  - **Priority:** Critical for privacy compliance

- **ISTG-MEM-CRYPT-001** - Usage of Weak Cryptographic Algorithms
  - **Focus:** Personal data encryption strength
  - **Testing:** Cryptographic algorithm validation
  - **Priority:** Critical for data protection

#### Personal Data Protection Requirements:
- **Encryption at rest:** Personal data encrypted on device
- **Encryption in transit:** Secure data transmission protocols
- **Access controls:** Restricted access to personal information
- **Data minimization:** Only necessary personal data collected
- **Consent mechanisms:** Clear user consent for data processing

### Article 3.3(f): Financial Transaction Protection (CRITICAL PRIORITY)
**Objective:** Secure money, monetary value, or virtual currency transfers

#### Applicable Test Cases:
- **ISTG-MEM-SCRT-001** - Unencrypted Storage of Secrets
  - **Focus:** Financial credentials, payment tokens, crypto keys
  - **Standard:** EN 18031-3:2024 (Financial transaction devices)
  - **Risk:** Financial fraud, payment interception

- **ISTG-MEM-CRYPT-001** - Usage of Weak Cryptographic Algorithms
  - **Focus:** Financial transaction encryption
  - **Testing:** Payment protocol security analysis
  - **Priority:** Critical for financial security

#### Financial Transaction Requirements:
- **Strong authentication:** Multi-factor authentication for transactions
- **Transaction integrity:** Cryptographic protection of payment data
- **Secure communication:** End-to-end encryption for financial data
- **Anti-fraud measures:** Transaction monitoring and validation

## Device Category Assessment

### Internet-Connected Radio Equipment (EN 18031-1)
**Applicable to:** WiFi devices, cellular IoT, LoRaWAN devices

**Primary Focus:** Article 3.3(d) - Network Protection
- ISTG-WRLS-* test cases
- Network protocol security
- Traffic generation limits
- Infrastructure protection

### Personal Data Processing Devices (EN 18031-2)  
**Applicable to:** Smart home devices, wearables, tracking devices, childcare equipment

**Primary Focus:** Article 3.3(e) - Personal Data Protection
- ISTG-MEM-INFO-004 (User data disclosure)
- ISTG-MEM-SCRT-001 (Data encryption)
- ISTG-UI-* test cases (User consent mechanisms)

**Special Considerations:**
- **Child protection** requirements for toys and childcare devices
- **Location data** protection for tracking devices
- **Biometric data** security for health/fitness wearables

### Financial Transaction Devices (EN 18031-3)
**Applicable to:** Payment terminals, crypto wallets, financial IoT devices

**Primary Focus:** Article 3.3(f) - Financial Protection
- ISTG-MEM-SCRT-001 (Financial credential protection)
- ISTG-MEM-CRYPT-001 (Payment encryption)
- ISTG-DES-* test cases (Payment service security)

## 10-Minute RED Compliance Quick Check

### For All Wireless IoT Devices (3 min):
1. **Network Impact Assessment**
   - ISTG-MEM-INFO-003: Check for network topology disclosure
   - Verify device doesn't enable network mapping

### For Personal Data Devices (4 min):
2. **Personal Data Protection**
   - ISTG-MEM-INFO-004: Verify personal data encryption
   - ISTG-MEM-SCRT-001: Check credential protection
   
3. **Privacy Controls**
   - Verify user consent mechanisms
   - Check data minimization implementation

### For Financial Devices (3 min):
4. **Financial Security**
   - ISTG-MEM-SCRT-001: Validate payment credential protection
   - ISTG-MEM-CRYPT-001: Verify strong financial cryptography

## Wireless Technology Specific Testing

### WiFi Devices
- **WPA3 implementation** validation
- **Network isolation** testing
- **Captive portal** security assessment

### Cellular IoT (LTE-M, NB-IoT)
- **SIM security** validation
- **Network attachment** security
- **Roaming security** assessment

### Bluetooth/BLE Devices
- **Pairing security** validation
- **Data transmission** encryption
- **Device discovery** controls

### LoRaWAN Devices  
- **Join procedure** security
- **Message encryption** validation
- **Network key** management

## EU Market Access Requirements

### CE Marking Requirements
- **Technical documentation** including cybersecurity assessment
- **EU Declaration of Conformity** with RED cybersecurity compliance
- **Notified Body assessment** for cybersecurity aspects (if required)

### Post-Market Surveillance
- **Incident reporting** to national authorities
- **Vulnerability disclosure** procedures
- **Update mechanisms** for security patches

### Supply Chain Requirements
- **Manufacturer responsibility** for cybersecurity compliance
- **Importer obligations** for EU market access
- **Distributor responsibilities** for compliant products

## Risk Assessment Framework

### Critical Risk (Immediate Action Required)
- Personal data exposure in consumer devices
- Financial transaction vulnerabilities
- Network infrastructure threats

### High Risk (Priority Resolution)
- Authentication bypass vulnerabilities
- Cryptographic implementation flaws
- Data transmission security issues

### Medium Risk (Planned Resolution)
- Information disclosure vulnerabilities
- Configuration security issues
- Protocol implementation concerns

## Compliance Documentation

### Required Technical File Contents
- **Cybersecurity risk assessment** results
- **Security testing reports** (penetration testing, vulnerability assessment)
- **Conformity assessment** with EN 18031 standards
- **User documentation** on security features

### Notified Body Assessment
Required for devices with **substantial** or **high** assurance levels:
- Independent security evaluation
- Technical file review
- Ongoing surveillance requirements

## Testing Timeline Recommendations

### 6 Months Before August 2025:
- Complete ISTG assessment for applicable test cases
- Engage Notified Body (if required)
- Begin technical file preparation

### 3 Months Before:
- Finalize security testing and remediation
- Complete conformity assessment
- Prepare CE marking documentation

### 1 Month Before:
- Final compliance validation
- Distributor/importer coordination
- Market preparation

## Common Compliance Pitfalls

### Network Protection (3.3d)
- **Underestimating network impact** of IoT device traffic
- **Ignoring mesh network** effects in multi-device deployments
- **Poor protocol implementation** leading to network instability

### Personal Data Protection (3.3e)
- **Inadequate encryption** of personal data
- **Poor consent mechanisms** not meeting GDPR standards
- **Excessive data collection** beyond functional requirements

### Financial Protection (3.3f)
- **Weak authentication** for financial functions
- **Inadequate transaction integrity** protection
- **Poor key management** for financial credentials

## Next Steps

1. **Full ISTG Assessment:** Complete testing with RED-specific focus
2. **Standards Compliance:** Align with final EN 18031 series standards
3. **Notified Body Engagement:** For complex or high-risk devices
4. **Market Preparation:** Update product documentation and compliance claims

---

**Note:** RED cybersecurity requirements are mandatory from August 2025. Early compliance assessment and remediation is critical for continued EU market access. Consider engaging specialized RED cybersecurity consultants for complex wireless IoT products.