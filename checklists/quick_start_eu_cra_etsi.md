# OWASP ISTG Quick Start Guide: EU Cyber Resilience Act + ETSI EN 303 645

## Overview

This quick start guide focuses on consumer IoT device testing for EU Cyber Resilience Act (CRA) compliance using ETSI EN 303 645 baseline requirements. It covers essential cybersecurity requirements for consumer IoT products entering the EU market.

**Target Audience:** Consumer IoT manufacturers, EU importers, product certification bodies

**Compliance Scope:** EU CRA Article 11 + ETSI EN 303 645 Consumer IoT Cybersecurity baseline

**Timeline:** Phased implementation starting 2024, full enforcement varies by product category

## EU Cyber Resilience Act Core Requirements

### Article 11: Essential Cybersecurity Requirements

#### Security by Design (Highest Priority)
**Objective:** Cybersecurity integrated throughout product lifecycle

**Key Test Cases:**
- **ISTG-PROC-AUTHZ-001** - Unauthorized Access to the Processing Unit
- **ISTG-PROC-AUTHZ-002** - Privilege Escalation
- **ISTG-MEM-SCRT-001** - Unencrypted Storage of Secrets
- **ISTG-MEM-CRYPT-001** - Usage of Weak Cryptographic Algorithms

**Requirements:**
- No universal default passwords
- Protection against unauthorized access
- Secure cryptographic implementation
- Privacy-preserving design

#### Vulnerability Handling (Critical Priority)
**Objective:** Systematic vulnerability management throughout product lifetime

**Key Test Cases:**
- **ISTG-PROC-LOGIC-001** - Insecure Implementation of Instructions
- **ISTG-FW[UPDT]-AUTHZ-001** - Unauthorized Firmware Update
- **ISTG-FW[UPDT]-CRYPT-001-004** - Firmware Update Security

**Requirements:**
- Coordinated vulnerability disclosure
- Security update mechanisms
- Vulnerability monitoring processes
- Incident response procedures

#### Software Updates (Critical Priority)  
**Objective:** Secure and reliable software update capability

**Key Test Cases:**
- **ISTG-FW[UPDT]-AUTHZ-001** - Unauthorized Firmware Update
- **ISTG-FW[UPDT]-CRYPT-001** - Insufficient Firmware Update Signature
- **ISTG-FW[UPDT]-CRYPT-002** - Insufficient Firmware Update Encryption
- **ISTG-FW[UPDT]-LOGIC-001** - Insufficient Rollback Protection

**Requirements:**
- Automatic security updates
- Update authenticity verification
- Rollback protection mechanisms
- User notification of updates

## ETSI EN 303 645 Provision Mapping

### Provision 1: No Universal Default Passwords
**Test Cases:**
- **ISTG-PROC-AUTHZ-001** - Unauthorized Processing Unit Access
- **ISTG-MEM-SCRT-001** - Unencrypted Storage of Secrets

**Testing Focus:**
- Unique default credentials per device
- Strong password policy enforcement
- Credential change mechanisms
- Authentication bypass prevention

### Provision 2: Implement Security Update Mechanism
**Test Cases:**
- **ISTG-FW[UPDT]-AUTHZ-001** - Unauthorized Firmware Update
- **ISTG-FW[UPDT]-CRYPT-001-004** - Update Cryptographic Security

**Testing Focus:**
- Automatic update capability
- Update server authentication
- Update integrity verification
- Rollback mechanisms

### Provision 4: Secure Default Values
**Test Cases:**
- **ISTG-PROC-LOGIC-001** - Insecure Implementation of Instructions
- **ISTG-MEM-INFO-001** - Disclosure of Source Code and Binaries
- **ISTG-MEM-INFO-002** - Disclosure of Implementation Details

**Testing Focus:**
- Secure configuration baselines
- Unnecessary service disabling
- Debug interface security
- Default encryption settings

### Provision 5: Authentication Mechanisms
**Test Cases:**
- **ISTG-PROC-AUTHZ-001** - Unauthorized Access
- **ISTG-PROC-AUTHZ-002** - Privilege Escalation
- All AUTHZ variants across components

**Testing Focus:**
- Multi-factor authentication support
- Session management security
- Authentication token protection
- Brute force protection

### Provision 6: Authorization Mechanisms  
**Test Cases:**
- **ISTG-PROC-AUTHZ-002** - Privilege Escalation
- All AUTHZ-002 variants across components

**Testing Focus:**
- Role-based access control
- Least privilege implementation
- Authorization bypass prevention
- Privilege escalation protection

### Provision 7: Secure Communication
**Test Cases:**
- **ISTG-MEM-CRYPT-001** - Usage of Weak Cryptographic Algorithms
- **ISTG-DES-CRYPT-001** - Data Exchange Service Cryptography
- **ISTG-WRLS-CRYPT-001** - Wireless Interface Cryptography

**Testing Focus:**
- TLS/SSL implementation security
- Certificate validation
- Cipher suite selection
- Communication authentication

### Provision 8: Data Protection
**Test Cases:**
- **ISTG-MEM-INFO-004** - Disclosure of User Data
- **ISTG-MEM-SCRT-001** - Unencrypted Storage of Secrets
- **ISTG-DES-INFO-003** - User Data Disclosure

**Testing Focus:**
- Personal data encryption
- Data minimization principles
- User consent mechanisms
- Data retention policies

### Provision 9: Cryptographic Security
**Test Cases:**
- **ISTG-MEM-CRYPT-001** - Usage of Weak Cryptographic Algorithms
- **ISTG-PROC-SIDEC-001** - Side-Channel Attack Protection
- All CRYPT-001 variants

**Testing Focus:**
- Strong cryptographic algorithms
- Proper key management
- Random number generation
- Side-channel attack resistance

### Provision 10: System Telemetry Data
**Test Cases:**
- **ISTG-MEM-INFO-003** - Disclosure of Ecosystem Details
- **ISTG-DES-INFO-001** - Implementation Details Disclosure

**Testing Focus:**
- Telemetry data minimization
- Anonymization techniques
- User control over telemetry
- Secure telemetry transmission

## Consumer IoT Device Categories

### Class I (Important Products)
**Examples:** Smart home hubs, security cameras, smart locks
**Enhanced Requirements:**
- Comprehensive vulnerability management
- Mandatory security updates
- Third-party security assessments

**Priority Test Cases:**
- All Authorization tests (AUTHZ-001, AUTHZ-002)
- All Cryptography tests (CRYPT-001)
- All Secrets management tests (SCRT-001)

### Class II (Critical Products)
**Examples:** Medical IoT devices, critical infrastructure components
**Highest Requirements:**
- Continuous security monitoring
- Formal security validation
- Regulatory oversight

**Comprehensive Testing:** Full ISTG assessment required

### Default Category
**Examples:** Smart bulbs, basic sensors, simple automation devices
**Standard Requirements:**
- Basic security by design
- Essential update mechanisms
- Fundamental protection measures

## 12-Minute Consumer IoT Quick Assessment

### Core Security (4 min):
1. **Default Credentials Check**
   - ISTG-PROC-AUTHZ-001: Verify no universal defaults

2. **Cryptographic Implementation**
   - ISTG-MEM-CRYPT-001: Check algorithm strength

### Update Mechanisms (3 min):
3. **Firmware Update Security**
   - ISTG-FW[UPDT]-AUTHZ-001: Test update authorization
   - ISTG-FW[UPDT]-CRYPT-001: Verify update signatures

### Data Protection (3 min):
4. **Personal Data Security**
   - ISTG-MEM-INFO-004: Check user data protection
   - ISTG-MEM-SCRT-001: Verify data encryption

### Communication Security (2 min):
5. **Network Communication**
   - ISTG-DES-CRYPT-001: Validate secure protocols

## Risk-Based Testing Approach

### Critical Priority (Immediate Action)
**Focus:** Authentication, cryptography, update mechanisms
- **ISTG-PROC-AUTHZ-001/002** - Access control failures
- **ISTG-MEM-CRYPT-001** - Cryptographic vulnerabilities
- **ISTG-FW[UPDT]-AUTHZ-001** - Update security

### High Priority (Next Sprint)
**Focus:** Data protection, secure communication
- **ISTG-MEM-INFO-004** - Personal data exposure
- **ISTG-MEM-SCRT-001** - Secret storage security
- **ISTG-DES-CRYPT-001** - Communication encryption

### Medium Priority (Planned Improvement)
**Focus:** Information disclosure, configuration security
- **ISTG-MEM-INFO-001/002** - Implementation disclosure
- **ISTG-PROC-LOGIC-001** - Business logic security

## Consumer-Specific Considerations

### Privacy Requirements (GDPR Alignment)
- **Data minimization** principles
- **User consent** mechanisms
- **Right to erasure** implementation
- **Data portability** support

### User Experience Balance
- **Security vs. usability** trade-offs
- **Simple setup** procedures
- **Clear security indicators**
- **Intuitive update processes**

### Home Network Integration
- **Router compatibility** testing
- **Network segmentation** support
- **Guest network** isolation
- **IoT VLAN** configuration

## Market Surveillance Implications

### CE Marking Requirements
- **Technical file** with cybersecurity documentation
- **EU Declaration of Conformity** including CRA compliance
- **Risk assessment** and mitigation documentation

### Post-Market Obligations
- **Vulnerability monitoring** throughout product lifetime
- **Security incident reporting** to authorities
- **Coordinated disclosure** with security researchers
- **Update provision** for minimum 5 years (or product lifetime)

### Penalties for Non-Compliance
- **Up to €15 million** or 2.5% of worldwide annual turnover
- **Product recall** and market withdrawal
- **Reputational damage** and market access restrictions

## Manufacturer Obligations Timeline

### Product Development Phase
- Security-by-design integration
- Vulnerability management process establishment
- Update mechanism implementation
- Third-party security assessment (if required)

### Market Introduction Phase  
- CE marking and documentation
- Coordinated vulnerability disclosure setup
- Customer security communication
- Support infrastructure establishment

### Post-Market Phase
- Continuous vulnerability monitoring
- Security update provision
- Incident response capability
- Regulatory compliance maintenance

## Testing Evidence Documentation

### Technical File Requirements
- **Security risk assessment** documentation
- **Penetration testing** and vulnerability assessment reports
- **ETSI EN 303 645 compliance** assessment
- **Update mechanism** validation documentation

### Ongoing Compliance Evidence
- **Vulnerability disclosure** process documentation
- **Security update** deployment records
- **Incident response** activity logs
- **Third-party security** assessment reports

## Integration with Other EU Regulations

### GDPR Compliance
- Personal data processing lawfulness
- Data subject rights implementation
- Privacy impact assessments
- Data protection by design

### Product Liability Directive
- Security defect responsibility
- Consumer protection obligations
- Damage compensation frameworks

### Digital Services Act (for platforms)
- Risk assessment and mitigation
- Content moderation systems
- Transparency reporting

## Next Steps

1. **Complete CRA Gap Analysis:** Full ISTG assessment with CRA focus
2. **ETSI EN 303 645 Compliance:** Detailed provision-by-provision assessment
3. **Vulnerability Management:** Establish coordinated disclosure process
4. **Update Infrastructure:** Implement secure, automatic update capabilities
5. **Documentation Preparation:** Technical file and CE marking documentation

---

**Note:** EU CRA requirements are comprehensive and will be strictly enforced. Early compliance preparation is essential for continued EU market access. Consider engaging specialized EU cybersecurity legal and technical consultants for complex consumer IoT products.