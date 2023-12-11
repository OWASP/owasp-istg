# 3.8. User Interfaces (IOT-UI)

## Table of Contents
- [3.8. User Interfaces (IOT-UI)](#38-user-interfaces-iot-ui)
	- [Table of Contents](#table-of-contents)
	- [Overview](#overview)
	- [Authorization (IOT-UI-AUTHZ)](#authorization-iot-ui-authz)
		- [Unauthorized Access to the Interface (IOT-UI-AUTHZ-001)](#unauthorized-access-to-the-interface-iot-ui-authz-001)
		- [Privilege Escalation (IOT-UI-AUTHZ-002)](#privilege-escalation-iot-ui-authz-002)
	- [Information Gathering (IOT-UI-INFO)](#information-gathering-iot-ui-info)
		- [Disclosure of Implementation Details (IOT-UI-INFO-001)](#disclosure-of-implementation-details-iot-ui-info-001)
		- [Disclosure of Ecosystem Details (IOT-UI-INFO-002)](#disclosure-of-ecosystem-details-iot-ui-info-002)
		- [Disclosure of User Data (IOT-UI-INFO-003)](#disclosure-of-user-data-iot-ui-info-003)
	- [Configuration and Patch Management (IOT-UI-CONF)](#configuration-and-patch-management-iot-ui-conf)
		- [Usage of Outdated Software (IOT-UI-CONF-001)](#usage-of-outdated-software-iot-ui-conf-001)
		- [Presence of Unnecessary Software and Functionalities (IOT-UI-CONF-002)](#presence-of-unnecessary-software-and-functionalities-iot-ui-conf-002)
	- [Secrets (IOT-UI-SCRT)](#secrets-iot-ui-scrt)
		- [Access to Confidential Data (IOT-UI-SCRT-001)](#access-to-confidential-data-iot-ui-scrt-001)
	- [Cryptography (IOT-UI-CRYPT)](#cryptography-iot-ui-crypt)
		- [Usage of Weak Cryptographic Algorithms (IOT-UI-CRYPT-001)](#usage-of-weak-cryptographic-algorithms-iot-ui-crypt-001)
	- [Business Logic (IOT-UI-LOGIC)](#business-logic-iot-ui-logic)
		- [Circumvention of the Intended Business Logic (IOT-UI-LOGIC-001)](#circumvention-of-the-intended-business-logic-iot-ui-logic-001)
	- [Input Validation (IOT-UI-INPV)](#input-validation-iot-ui-inpv)
		- [Insufficient Input Validation (IOT-UI-INPV-001)](#insufficient-input-validation-iot-ui-inpv-001)
		- [Code or Command Injection (IOT-UI-INPV-002)](#code-or-command-injection-iot-ui-inpv-002)



## Overview

This section includes test cases and categories for the component user interface. Based on its implementation and intended use, a user interface might be accessible with all physical access levels.

In regards to test case categories that are relevant for a user interface, the following were identified:

- **Authorization:** Focuses on vulnerabilities that allow to get unauthorized access to the user interface or to elevate privileges in order to access restricted functionalities.

- **Information Gathering:** Focuses on information that is handled by the user interface and that might be disclosed to potential attackers if not being properly protected or removed.

- **Configuration and Patch Management:** Focuses on vulnerabilities and issues in the configuration of a user interface and its software components.

- **Secrets:** Focuses on secrets that are handled by the user interface in an insecure manner.

- **Cryptography:** Focuses on vulnerabilities in the cryptographic implementation.

- **Business Logic:** Focuses on vulnerabilities in the implementation of the user interface.

- **Input Validation:** Focuses on vulnerabilities regarding the validation and processing of input from untrustworthy sources.



## Authorization (IOT-UI-AUTHZ)

Depending on the access model for a given device, only certain individuals might be allowed to access a user interface. Thus, proper authentication and authorization procedures need to be in place, which ensure that only authorized users can get access.

### Unauthorized Access to the Interface (IOT-UI-AUTHZ-001)
**Required Access Levels**

<table width="100%">
	<tr valign="top">
		<th width="1%" align="left">Physical</th>
 <td><i>PA-1</i> - <i>PA-4</i><br>(depending-on-how-the-user-interface-can-be-accessed,-e.g.,-if-they-were-designed-for-remote-access)</td>
	</tr>
	<tr valign="top">
		<th align="left">Authorization</th>
		<td><i>AA-1</i></tr>
</table>

**Summary**

Depending on the specific implementation of a given device, access to a user interface might be restricted to individuals with a certain authorization access level, e.g., *AA-2*, *AA-3* or *AA-4*. If the device fails to correctly verify access permissions, any attacker (*AA-1*) might be able to get access.

**Test Objectives**

- It must be checked if authorization checks for access to the user interface are implemented.

- In case that authorization checks are in place, it must be determined whether there is a way to bypass them.

**Remediation**

Proper authorization checks need to be implemented, which ensure that access to the user interface is only possible for authorized individuals.

**References**

For this test case, data from the following sources was consolidated:

* OWASP ["Web Security Testing Guide"][owasp_wstg]
* OWASP ["Mobile Security Testing Guide"][owasp_mstg]
* ["IoT Penetration Testing Cookbook"][iot_penetration_testing_cookbook] by Aaron Guzman and Aditya Gupta
* ["The IoT Hacker's Handbook"][iot_hackers_handbook] by Aditya Gupta
* ["Practical IoT Hacking"][practical_iot_hacking] by Fotios Chantzis, Ioannis Stais, Paulino Calderon, Evangelos Deirmentzoglou, and Beau Woods
* Key aspects of testing of the T-Systems Multimedia Solutions GmbH

This test case is based on: [IOT-DES-AUTHZ-001](../data_exchange_services/README.md#unauthorized-access-to-the-data-exchange-service-iot-des-authz-001).

### Privilege Escalation (IOT-UI-AUTHZ-002)
**Required Access Levels**

<table width="100%">
	<tr valign="top">
		<th width="1%" align="left">Physical</th>
 <td><i>PA-1</i> - <i>PA-4</i><br>(depending-on-how-the-user-interface-can-be-accessed,-e.g.,-if-they-were-designed-for-remote-access)</td>
	</tr>
	<tr valign="top">
		<th align="left">Authorization</th>
		<td><i>AA-2</i> - <i>AA-3</i><br>(depending-on-the-access-model-for-the-given-device)</tr>
</table>

**Summary**

Depending on the specific implementation of a given device, access to some functionalities via a user interface might be restricted to individuals with a certain authorization access level, e.g., *AA-3* or *AA-4*. If the interface fails to correctly verify access permissions, an attacker with a lower authorization access level than intended might be able to get access to the restricted functionalities.

**Test Objectives**

- Based on [IOT-UI-AUTHZ-001](#unauthorized-access-to-the-interface-iot-ui-authz-001), it must be determined whether there is a way to elevate the given access privileges and thus to access restricted functionalities.

**Remediation**

Proper authorization checks need to be implemented, which ensure that access to restricted functionalities is only possible for individuals with the required authorization access levels.

**References**

For this test case, data from the following sources was consolidated:

* OWASP ["Web Security Testing Guide"][owasp_wstg]
* OWASP ["Mobile Security Testing Guide"][owasp_mstg]
* ["IoT Penetration Testing Cookbook"][iot_penetration_testing_cookbook] by Aaron Guzman and Aditya Gupta
* ["The IoT Hacker's Handbook"][iot_hackers_handbook] by Aditya Gupta
* ["Practical IoT Hacking"][practical_iot_hacking] by Fotios Chantzis, Ioannis Stais, Paulino Calderon, Evangelos Deirmentzoglou, and Beau Woods
* Key aspects of testing of the T-Systems Multimedia Solutions GmbH

This test case is based on: [IOT-DES-AUTHZ-002](../data_exchange_services/README.md#privilege-escalation-iot-des-authz-002).



## Information Gathering (IOT-UI-INFO)

User interface might disclose various information, which could reveal details regarding the inner workings of the device or the surrounding IoT-ecosystem to potential attackers. This could enable and facilitate further, more advanced attacks.

### Disclosure of Implementation Details (IOT-UI-INFO-001)
**Required Access Levels**

<table width="100%">
	<tr valign="top">
		<th width="1%" align="left">Physical</th>
 <td><i>PA-1</i> - <i>PA-4</i><br>(depending-on-how-the-user-interface-can-be-accessed,-e.g.,-if-they-were-designed-for-remote-access)</td>
	</tr>
	<tr valign="top">
		<th align="left">Authorization</th>
		<td><i>AA-1</i> - <i>AA-4</i><br>(depending-on-the-access-model-for-the-given-device)</tr>
</table>

**Summary**

If details about the implementation, e.g., algorithms in use or the authentication procedure, are available to potential attackers, flaws and entry points for successful attacks are easier to detect. While the disclosure of such details alone is not considered to be a vulnerability, it facilitates the identification of potential attack vectors, thus allowing an attacker to exploit insecure implementations faster.

For example, relevant information might be included in service banners, response headers or error messages.

**Test Objectives**

- Accessible details regarding the implementation must be assessed in order to prepare further tests. For example, this includes:

 - Cryptographic algorithms in use

 - Authentication and authorization mechanisms

 - Local paths and environment details

**Remediation**

As mentioned above, the disclosure of such information is not considered a vulnerability. However, in order to impede exploitation attempts, only information, necessary for the device operation, should be displayed.

**References**

For this test case, data from the following sources was consolidated:

* OWASP ["Web Security Testing Guide"][owasp_wstg]
* OWASP ["Mobile Security Testing Guide"][owasp_mstg]
* ["IoT Penetration Testing Cookbook"][iot_penetration_testing_cookbook] by Aaron Guzman and Aditya Gupta
* ["The IoT Hacker's Handbook"][iot_hackers_handbook] by Aditya Gupta
* ["Practical IoT Hacking"][practical_iot_hacking] by Fotios Chantzis, Ioannis Stais, Paulino Calderon, Evangelos Deirmentzoglou, and Beau Woods
* Key aspects of testing of the T-Systems Multimedia Solutions GmbH

This test case is based on: [IOT-FW-INFO-002](../firmware/README.md#disclosure-of-implementation-details-iot-fw-info-002).

### Disclosure of Ecosystem Details (IOT-UI-INFO-002)
**Required Access Levels**

<table width="100%">
	<tr valign="top">
		<th width="1%" align="left">Physical</th>
 <td><i>PA-1</i> - <i>PA-4</i><br>(depending-on-how-the-user-interface-can-be-accessed,-e.g.,-if-they-were-designed-for-remote-access)</td>
	</tr>
	<tr valign="top">
		<th align="left">Authorization</th>
		<td><i>AA-1</i> - <i>AA-4</i><br>(depending-on-the-access-model-for-the-given-device)</tr>
</table>

**Summary**

A user interface might disclose information about the surrounding IoT-ecosystem, e.g., sensitive URLs, IP addresses, software in use etc. An attacker might be able to use this information to prepare and execute attacks against the ecosystem.

For example, relevant information might be included in service banners, response headers or error messages.

**Test Objectives**

- It must be determined if the user interface discloses relevant information about the surrounding ecosystem.

**Remediation**

The disclosure of information should be reduced to the minimum, which is required for operating the device. The disclosed information it has to be assessed and all unnecessarily included data should be removed.

**References**

For this test case, data from the following sources was consolidated:

* OWASP ["Web Security Testing Guide"][owasp_wstg]
* OWASP ["Mobile Security Testing Guide"][owasp_mstg]
* ["IoT Penetration Testing Cookbook"][iot_penetration_testing_cookbook] by Aaron Guzman and Aditya Gupta
* ["The IoT Hacker's Handbook"][iot_hackers_handbook] by Aditya Gupta
* ["Practical IoT Hacking"][practical_iot_hacking] by Fotios Chantzis, Ioannis Stais, Paulino Calderon, Evangelos Deirmentzoglou, and Beau Woods
* Key aspects of testing of the T-Systems Multimedia Solutions GmbH

This test case is based on: [IOT-FW-INFO-003](../firmware/README.md#disclosure-of-ecosystem-details-iot-fw-info-003).

### Disclosure of User Data (IOT-UI-INFO-003)
**Required Access Levels**

<table width="100%">
	<tr valign="top">
		<th width="1%" align="left">Physical</th>
 <td><i>PA-1</i> - <i>PA-4</i><br>(depending-on-how-the-user-interface-can-be-accessed,-e.g.,-if-they-were-designed-for-remote-access)</td>
	</tr>
	<tr valign="top">
		<th align="left">Authorization</th>
		<td><i>AA-1</i> - <i>AA-4</i><br>(depending-on-the-access-model-for-the-given-device)</tr>
</table>

**Summary**

During runtime, a device is accumulating and processing data of different kinds, such as personal data of its users. If this data is disclosed, an attacker might be able to get access to it.

**Test Objectives**

- It has to be checked whether user data can be accessed by unauthorized individuals.

**Remediation**

Access to user data should only be granted to individuals and processes that need to have access to it. No unauthorized or not properly authorized individual should be able to access user data.

**References**

For this test case, data from the following sources was consolidated:

* OWASP ["Web Security Testing Guide"][owasp_wstg]
* OWASP ["Mobile Security Testing Guide"][owasp_mstg]
* ["IoT Penetration Testing Cookbook"][iot_penetration_testing_cookbook] by Aaron Guzman and Aditya Gupta
* ["The IoT Hacker's Handbook"][iot_hackers_handbook] by Aditya Gupta
* ["Practical IoT Hacking"][practical_iot_hacking] by Fotios Chantzis, Ioannis Stais, Paulino Calderon, Evangelos Deirmentzoglou, and Beau Woods
* Key aspects of testing of the T-Systems Multimedia Solutions GmbH

This test case is based on: [IOT-FW[INST]-INFO-001](../firmware/installed_firmware.md#disclosure-of-user-data-iot-fw[inst]-info-001).



## Configuration and Patch Management (IOT-UI-CONF)

Since IoT-devices can have a long lifespan, it is important to make sure that the software, running on the device, is regularly updated in order to apply the latest security patches. The update process of the firmware itself will be covered by [IOT-FW[UPDT]](../firmware/firmware_update_mechanism.md). However, it must also be verified that software packages, which are running on the device and listening on interfaces, are up-to-date as well.

### Usage of Outdated Software (IOT-UI-CONF-001)
**Required Access Levels**

<table width="100%">
	<tr valign="top">
		<th width="1%" align="left">Physical</th>
 <td><i>PA-1</i> - <i>PA-4</i><br>(depending-on-how-the-user-interface-can-be-accessed,-e.g.,-if-they-were-designed-for-remote-access)</td>
	</tr>
	<tr valign="top">
		<th align="left">Authorization</th>
		<td><i>AA-1</i> - <i>AA-4</i><br>(depending-on-the-access-model-for-the-given-device)</tr>
</table>

**Summary**

Every piece of software is potentially vulnerable to attacks. For example, coding errors could lead to undefined program behavior, which then can be exploited by an attacker to gain access to data, processed by the application, or to perform actions in the context of the runtime environment. Furthermore, vulnerabilities in the used frameworks, libraries and other technologies might also affect the security level of a given piece of software.

Usually, developers release an update once a vulnerability was detected in their software. These updates should be installed as soon as possible in order to reduce the probability of successful attacks. Otherwise, attackers could use known vulnerabilities to perform attacks against the device.

**Test Objectives**

- The version identifiers of installed software packages as well as libraries and frameworks in use must be determined.

- Based on the detected version identifiers, it must be determined if the software version in use is up-to-date, e.g., by consulting the website of the software developer or public repositories.

- By using vulnerability databases, such as the [National Vulnerability Database](https://nvd.nist.gov) of the NIST, it has to be checked whether any vulnerabilities are known for the detected software versions.

**Remediation**

No outdated software packages should be running on the device. A proper patch management process, which ensures that applicable updates are installed once being available, should be implemented.

**References**

For this test case, data from the following sources was consolidated:

* OWASP ["Web Security Testing Guide"][owasp_wstg]
* Key aspects of testing of the T-Systems Multimedia Solutions GmbH

This test case is based on: [IOT-FW-CONF-001](../firmware/README.md#usage-of-outdated-software-iot-fw-conf-001).

### Presence of Unnecessary Software and Functionalities (IOT-UI-CONF-002)
**Required Access Levels**

<table width="100%">
	<tr valign="top">
		<th width="1%" align="left">Physical</th>
 <td><i>PA-1</i> - <i>PA-4</i><br>(depending-on-how-the-user-interface-can-be-accessed,-e.g.,-if-they-were-designed-for-remote-access)</td>
	</tr>
	<tr valign="top">
		<th align="left">Authorization</th>
		<td><i>AA-1</i> - <i>AA-4</i><br>(depending-on-the-access-model-for-the-given-device)</tr>
</table>

**Summary**

Every piece of software, which is available on the device, broadens the attack surface since it might be used to perform attacks against the device. Even if the installed software is up-to-date, it might still be affected by unpublished vulnerabilities. It is also possible that a software program facilitates an attack without being vulnerable, e.g., by providing access to specific files or processes.

**Test Objectives**

- A list of functionalities, available via the interface, should be assembled.

- Based on the device documentation, its behavior and the intended use cases, it must be determined whether any of the available functionalities are not mandatory for the device operation.

**Remediation**

The attack surface should be minimized as much as possible by removing or disabling every software that is not required for the device operation.

Especially in case of general-purpose operating systems, such as Windows and Linux systems, it must be ensured that any unnecessary operating system features are disabled.

**References**

For this test case, data from the following sources was consolidated:

* OWASP ["Web Security Testing Guide"][owasp_wstg]
* Key aspects of testing of the T-Systems Multimedia Solutions GmbH

This test case is based on: [IOT-FW-CONF-002](../firmware/README.md#presence-of-unnecessary-software-and-functionalities-iot-fw-conf-002).



## Secrets (IOT-UI-SCRT)

IoT-devices are often operated outside of the control space of their manufacturer. Still, they need to establish connections to other network nodes within the IoT-ecosystem, e.g., to request and receive firmware updates or to send data to a cloud API. Hence, it might be required that the device has to provide some kind of authentication credential or secret. These secrets need to be stored on the device in a secure manner to prevent them from being stolen and used to impersonate the device.

### Access to Confidential Data (IOT-UI-SCRT-001)
**Required Access Levels**

<table width="100%">
	<tr valign="top">
		<th width="1%" align="left">Physical</th>
 <td><i>PA-1</i> - <i>PA-4</i><br>(depending-on-how-the-user-interface-can-be-accessed,-e.g.,-if-they-were-designed-for-remote-access)</td>
	</tr>
	<tr valign="top">
		<th align="left">Authorization</th>
		<td><i>AA-1</i> - <i>AA-4</i><br>(depending-on-the-access-model-for-the-given-device)</tr>
</table>

**Summary**

Malfunctions, unintended behavior or improper implementation of a user interface might enable an attacker to get access to secrets.

**Test Objectives**

- It has to be determined whether secrets can be accessed via the user interface.

**Remediation**

Access to secrets should only be granted to individuals and processes that need to have access to them. No unauthorized or not properly authorized individual should be able to access secrets.

**References**

For this test case, data from the following sources was consolidated:

* OWASP ["Web Security Testing Guide"][owasp_wstg]
* OWASP ["Mobile Security Testing Guide"][owasp_mstg]
* ["IoT Penetration Testing Cookbook"][iot_penetration_testing_cookbook] by Aaron Guzman and Aditya Gupta
* ["The IoT Hacker's Handbook"][iot_hackers_handbook] by Aditya Gupta
* ["Practical IoT Hacking"][practical_iot_hacking] by Fotios Chantzis, Ioannis Stais, Paulino Calderon, Evangelos Deirmentzoglou, and Beau Woods
* Key aspects of testing of the T-Systems Multimedia Solutions GmbH

This test case is based on: [IOT-DES-SCRT-001](../data_exchange_services/README.md#access-to-confidential-data-iot-des-scrt-001).



## Cryptography (IOT-UI-CRYPT)

Many IoT-devices need to implement cryptographic algorithms, e.g., to securely store sensitive data, for authentication purposes or to receive and verify encrypted data from other network nodes. Failing to implement secure, state of the art cryptography might lead to the exposure of sensitive data, device malfunctions or loss of control over the device.

### Usage of Weak Cryptographic Algorithms (IOT-UI-CRYPT-001)
**Required Access Levels**

<table width="100%">
	<tr valign="top">
		<th width="1%" align="left">Physical</th>
 <td><i>PA-1</i> - <i>PA-4</i><br>(depending-on-how-the-user-interface-can-be-accessed,-e.g.,-if-they-were-designed-for-remote-access)</td>
	</tr>
	<tr valign="top">
		<th align="left">Authorization</th>
		<td><i>AA-1</i> - <i>AA-4</i><br>(depending-on-the-access-model-for-the-given-device)</tr>
</table>

**Summary**

Cryptography can be implemented in various ways. However, due to evolving technologies, new algorithms and more computing power becoming available, many old cryptographic algorithms are nowadays considered weak or insecure. Thus, either new and stronger cryptographic algorithms have to be used or existing algorithms must be adapted, e.g., by increasing the key length or using alternative modes of operation.

The usage of weak cryptographic algorithms might allow an attacker to recover the plaintext from a given ciphertext in a timely manner.

**Test Objectives**

- The data, processed by the interface, must be checked for the presence of encrypted data segments. In case that encrypted data segments are found, it must be checked whether the cryptographic algorithms in use can be identified.

- Furthermore, based on [IOT-UI-INFO-001](#disclosure-of-implementation-details-iot-ui-info-001), it must be checked whether headers, system messages etc. disclose the usage of certain cryptographic algorithms.

- In case that cryptographic algorithms can be identified, it must be determined whether the algorithms in use and their configuration are providing a sufficient level of security at the time of testing, e.g., by consulting cryptography guidelines like the technical guideline [TR-02102-1](https://www.bsi.bund.de/SharedDocs/Downloads/EN/BSI/Publications/TechGuidelines/TG02102/BSI-TR-02102-1.pdf?__blob=publicationFile&v=10) by the BSI.

**Remediation**

Only strong, state of the art cryptographic algorithms should be used. Furthermore, these algorithms must be used in a secure manner by setting proper parameters, such as an appropriate key length or mode of operation.

**References**

For this test case, data from the following sources was consolidated:

* OWASP ["Web Security Testing Guide"][owasp_wstg]
* Key aspects of testing of the T-Systems Multimedia Solutions GmbH

This test case is based on: [IOT-FW-CRYPT-001](../firmware/README.md#usage-of-weak-cryptographic-algorithms-iot-fw-crypt-001).



## Business Logic (IOT-UI-LOGIC)

Even if all other aspects of the user interface are securely implemented and configured, issues in the underlying logic itself might render the device vulnerable to attacks. Thus, it must be verified if the user interface and its functionalities are working as intended and if exceptions are detected and properly handled.

### Circumvention of the Intended Business Logic (IOT-UI-LOGIC-001)
**Required Access Levels**

<table width="100%">
	<tr valign="top">
		<th width="1%" align="left">Physical</th>
 <td><i>PA-1</i> - <i>PA-4</i><br>(depending-on-how-the-user-interface-can-be-accessed,-e.g.,-if-they-were-designed-for-remote-access)</td>
	</tr>
	<tr valign="top">
		<th align="left">Authorization</th>
		<td><i>AA-1</i> - <i>AA-4</i><br>(depending-on-the-access-model-for-the-given-device)</tr>
</table>

**Summary**

Flaws in the implementation of the business logic might result in unintended behavior or malfunctions of the device. For example, if an attacker intentionally misses to provide relevant input data or tries to skip or change important steps in the processing workflow the device might end up in an unknown, potentially insecure state.

**Test Objectives**

- Based on the specific business logic implementation, it has to be determined whether deviations from the defined workflows are properly detected and handled.

**Remediation**

The device should not end up in an unknown state. Anomalies in the workflow must be detected and exceptions have to be handled properly.

**References**

For this test case, data from the following sources was consolidated:

* OWASP ["Web Security Testing Guide"][owasp_wstg]
* OWASP ["Mobile Security Testing Guide"][owasp_mstg]
* ["IoT Penetration Testing Cookbook"][iot_penetration_testing_cookbook] by Aaron Guzman and Aditya Gupta
* ["The IoT Hacker's Handbook"][iot_hackers_handbook] by Aditya Gupta
* ["Practical IoT Hacking"][practical_iot_hacking] by Fotios Chantzis, Ioannis Stais, Paulino Calderon, Evangelos Deirmentzoglou, and Beau Woods
* Key aspects of testing of the T-Systems Multimedia Solutions GmbH

This test case is based on: [IOT-DES-LOGIC-001](../data_exchange_services/README.md#circumvention-of-the-intended-business-logic-iot-des-logic-001).



## Input Validation (IOT-UI-INPV)

In order to ensure that only valid and well-formed data enters the processing flows of a device, the input from a all untrustworthy sources, e.g., users or external systems, has to be verified and validated.

### Insufficient Input Validation (IOT-UI-INPV-001)
**Required Access Levels**

<table width="100%">
	<tr valign="top">
		<th width="1%" align="left">Physical</th>
 <td><i>PA-1</i> - <i>PA-4</i><br>(depending-on-how-the-user-interface-can-be-accessed,-e.g.,-if-they-were-designed-for-remote-access)</td>
	</tr>
	<tr valign="top">
		<th align="left">Authorization</th>
		<td><i>AA-1</i> - <i>AA-4</i><br>(depending-on-the-access-model-for-the-given-device)</tr>
</table>

**Summary**

If no input validation is performed or only an insufficient input validation mechanism is in place an attacker might be able to submit arbitrary and malformed data. Thus, the process, which handles the user input, or another downstream component might stop working properly due to not being able to process the data. This could result in malfunctions that might enable an attacker to manipulate the device behavior or render it unavailable.

**Test Objectives**

- It must be determined whether input to the user interface is validated.

- In case that an input validation mechanism is implemented, it hast to be checked if there is a way to submit data, which does not comply with the intended data structure and value ranges.

**Remediation**

The device has to validate all input from untrustworthy sources. Malformed or otherwise invalid input must either be rejected or converted into a proper data structure, e.g., by encoding the input. However, it must be ensured that the input is not interpreted or executed when converting it.

**References**

For this test case, data from the following sources was consolidated:

* OWASP ["Web Security Testing Guide"][owasp_wstg]
* OWASP ["Mobile Security Testing Guide"][owasp_mstg]
* ["IoT Penetration Testing Cookbook"][iot_penetration_testing_cookbook] by Aaron Guzman and Aditya Gupta
* ["The IoT Hacker's Handbook"][iot_hackers_handbook] by Aditya Gupta
* ["Practical IoT Hacking"][practical_iot_hacking] by Fotios Chantzis, Ioannis Stais, Paulino Calderon, Evangelos Deirmentzoglou, and Beau Woods
* Key aspects of testing of the T-Systems Multimedia Solutions GmbH

This test case is based on: [IOT-DES-INPV-001](../data_exchange_services/README.md#insufficient-input-validation-iot-des-inpv-001).

### Code or Command Injection (IOT-UI-INPV-002)
**Required Access Levels**

<table width="100%">
	<tr valign="top">
		<th width="1%" align="left">Physical</th>
 <td><i>PA-1</i> - <i>PA-4</i><br>(depending-on-how-the-user-interface-can-be-accessed,-e.g.,-if-they-were-designed-for-remote-access)</td>
	</tr>
	<tr valign="top">
		<th align="left">Authorization</th>
		<td><i>AA-1</i> - <i>AA-4</i><br>(depending-on-the-access-model-for-the-given-device)</tr>
</table>

**Summary**

If no input validation is performed or only an insufficient input validation mechanism is in place an attacker might be able to submit code or commands, which then might be executed by the system. It strictly depends on the specific implementation of the device and the user interface which code and commands are potentially executable. For example, possible injection attacks are Cross Site Scripting, SQL injection and OS command injection.

**Test Objectives**

- Based on [IOT-UI-INPV-001](#insufficient-input-validation-iot-ui-inpv-001), it must be checked whether it is possible to submit code or commands, which are then executed by the system.

**Remediation**

The device has to validate all input from untrustworthy sources. Malformed or otherwise invalid input must either be rejected or converted into a proper data structure, e.g., by encoding the input. However, it must be ensured that the input is not interpreted or executed when converting it.

**References**

For this test case, data from the following sources was consolidated:

* OWASP ["Web Security Testing Guide"][owasp_wstg]
* OWASP ["Mobile Security Testing Guide"][owasp_mstg]
* ["IoT Penetration Testing Cookbook"][iot_penetration_testing_cookbook] by Aaron Guzman and Aditya Gupta
* ["The IoT Hacker's Handbook"][iot_hackers_handbook] by Aditya Gupta
* ["Practical IoT Hacking"][practical_iot_hacking] by Fotios Chantzis, Ioannis Stais, Paulino Calderon, Evangelos Deirmentzoglou, and Beau Woods
* Key aspects of testing of the T-Systems Multimedia Solutions GmbH

This test case is based on: [IOT-DES-INPV-002](../data_exchange_services/README.md#code-or-command-injection-iot-des-inpv-002).



[owasp_wstg]: https://owasp.org/www-project-web-security-testing-guide/	"OWASP Web Security Testing Guide"
[owasp_mstg]: https://owasp.org/www-project-mobile-security-testing-guide/	"OWASP Mobile Security Testing Guide"
[iot_penetration_testing_cookbook]: https://www.packtpub.com/product/iot-penetration-testing-cookbook/9781787280571	"IoT Penetration Testing Cookbook"
[iot_hackers_handbook]: https://link.springer.com/book/10.1007/978-1-4842-4300-8	"The IoT Hacker's Handbook"
[practical_iot_hacking]: https://nostarch.com/practical-iot-hacking	"Practical IoT Hacking"