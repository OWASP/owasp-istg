# 3.3. Firmware (IOT-FW)

## Table of Contents
* [Overview](#overview)
* [Information Gathering (IOT-FW-INFO)](#information-gathering-iot-fw-info)
  * [Disclosure of Source Code (IOT-FW-INFO-001)](#disclosure-of-source-code-iot-fw-info-001)
  * [Disclosure of Implementation Details (IOT-FW-INFO-002)](#disclosure-of-implementation-details-iot-fw-info-002)
  * [Disclosure of Ecosystem Details (IOT-FW-INFO-003)](#disclosure-of-ecosystem-details-iot-fw-info-003)
* [Configuration and Patch Management (IOT-FW-CONF)](#configuration-and-patch-management-iot-fw-conf)
  * [Usage of Outdated Software (IOT-FW-CONF-001)](#usage-of-outdated-software-iot-fw-conf-001)
  * [Presence of Unnecessary Software and Functionalities (IOT-FW-CONF-002)](#presence-of-unnecessary-software-and-functionalities-iot-fw-conf-002)
* [Secrets (IOT-FW-SCRT)](#secrets-iot-fw-scrt)
  * [Secrets Stored in Public Storage (IOT-FW-SCRT-001)](#secrets-stored-in-public-storage-iot-fw-scrt-001)
  * [Unencrypted Storage of Secrets (IOT-FW-SCRT-002)](#unencrypted-storage-of-secrets-iot-fw-scrt-002)
  * [Usage of Hardcoded Secrets (IOT-FW-SCRT-003)](#usage-of-hardcoded-secrets-iot-fw-scrt-003)
* [Cryptography (IOT-FW-CRYPT)](#cryptography-iot-fw-crypt)
  * [Usage of Weak Cryptographic Algorithms (IOT-FW-CRYPT-001)](#usage-of-weak-cryptographic-algorithms-iot-fw-crypt-001)




## Overview

This section includes test cases and categories for the component firmware and the component specializations installed firmware ([IOT-FW[INST]](./installed_firmware.md)) and firmware update mechanism ([IOT-FW[UPDT]](./firmware_update_mechanism.md)) respectively. The firmware might be accessible with all physical access levels, depending on how this access is implemented in detail.

In regards to test case categories that are relevant for processing units, the following were identified:

- **Information Gathering:** Focuses on information that is stored within the firmware and that might be disclosed to potential attackers if not being properly protected or removed.

- **Configuration and Patch Management:** Focuses on vulnerabilities and issues in the configuration of a firmware and its software components.

- **Secrets:** Focuses on secrets that are stored within the firmware in an insecure manner.

- **Cryptography:** Focuses on vulnerabilities in the cryptographic implementation.

- **Authorization  (Installed Firmware):** Focuses on vulnerabilities that allow to get unauthorized access to the firmware or to elevate privileges in order to access restricted functionalities.

- **Business Logic  (Firmware Update Process):** Focuses on vulnerabilities in the design and implementation of the firmware update process.

All test cases and categories for the component [IOT-FW](./README.md) focus on generic firmware analysis aspects, without regards to the specifics of specializations for this component.



## Information Gathering (IOT-FW-INFO)

The firmware of an IoT device can include various information, which, if disclosed, could reveal details regarding the inner workings of the device or the surrounding IoT ecosystem to potential attackers. This could enable and facilitate further, more advanced attacks.

### Disclosure of Source Code (IOT-FW-INFO-001)

**Required Access Levels**

<table width="100%">
	<tr valign="top">
		<th width="1%" align="left">Physical</th>
 <td><i>PA-1</i> - <i>PA-4</i><br>(depending on how the firmware can be accessed, e.g., via an internal/physical debugging interface or remotely via SSH)</td>
	</tr>
	<tr valign="top">
		<th align="left">Authorization</th>
		<td><i>AA-1</i> - <i>AA-4</i><br>(depending on which component specialization should be tested and how it can be accessed)</td>
	</tr>
</table>

**Summary**

The disclosure of uncompiled source code could accelerate the exploitation of the software implementation since vulnerabilities can be directly identified in the code without the need to perform tests in a trial and error manner. Furthermore, left-over source code might include internal development information, developer comments or hard-coded sensitive data, which were not intended for productive use.

Similar to uncompiled source code, compiled binaries might also disclose relevant information. However, reverse-engineering might be required to retrieve useful data, which could take a considerable amount of time. Thus, the tester has to assess which binaries might be worth analyzing, ideally in coordination with the firmware manufacturer.

**Test Objectives**

- It must be checked if uncompiled source code can be identified within the firmware.

- If uncompiled source code is detected, its content must be analyzed for the presence of sensitive data, which might be useful for potential attackers (also see [IOT-FW-SCRT-003](#usage-of-hardcoded-secrets-iot-fw-scrt-003)).

- Reverse-engineering of selected binaries should be performed in order to obtain useful information regarding the firmware implementation and the processing of sensitive data.

**Remediation**

If possible, uncompiled source code should be removed from firmware, intended for productive use. If the source code has to be included, it must be verified that all internal development data is removed before the firmware is released.

Since it is not possible to prevent reverse-engineering completely, measures to restrict access to the firmware in general should be implemented to reduce the attack surface. Furthermore, the reverse-engineering process can be impeded, e.g., by obfuscating the code.

**References**

For this test case, data from the following sources was consolidated:

* OWASP ["Firmware Security Testing Methodology"][owasp_fstm]
* ["IoT Pentesting Guide"][iot_pentesting_guide] by Aditya Gupta
* ["IoT Penetration Testing Cookbook"][iot_penetration_testing_cookbook] by Aaron Guzman and Aditya Gupta
* ["The IoT Hacker's Handbook"][iot_hackers_handbook] by Aditya Gupta
* ["Practical IoT Hacking"][practical_iot_hacking] by Fotios Chantzis, Ioannis Stais, Paulino Calderon, Evangelos Deirmentzoglou, and Beau Woods
* Key aspects of testing of the T-Systems Multimedia Solutions GmbH

### Disclosure of Implementation Details (IOT-FW-INFO-002)

**Required Access Levels**

<table width="100%">
	<tr valign="top">
		<th width="1%" align="left">Physical</th>
 <td><i>PA-1</i> - <i>PA-4</i><br>(depending on how the firmware can be accessed, e.g., via an internal/physical debugging interface or remotely via SSH)</td>
	</tr>
	<tr valign="top">
		<th align="left">Authorization</th>
		<td><i>AA-1</i> - <i>AA-4</i><br>(depending on the access model for the given device) </td>
	</tr>
</table>

**Summary**

If details about the implementation, e.g., algorithms in use or the authentication procedure, are available to potential attackers, flaws and entry points for successful attacks are easier to detect. While the disclosure of such details alone is not considered to be a vulnerability, it facilitates the identification of potential attack vectors, thus allowing an attacker to exploit insecure implementations faster.

For example, relevant information might be included in files of various types like configuration files, text files, system settings or databases.

**Test Objectives**

- Accessible details regarding the implementation must be assessed in order to prepare further tests. For example, this includes:
  - Cryptographic algorithms in use

  - Authentication and authorization mechanisms

  - Local paths and environment details


**Remediation**

As mentioned above, the disclosure of such information is not considered a vulnerability. However, in order to impede exploitation attempts, only information, necessary for the device operation, should be accessible.

**References**

For this test case, data from the following sources was consolidated:

* OWASP ["Firmware Security Testing Methodology"][owasp_fstm]
* ["IoT Pentesting Guide"][iot_pentesting_guide] by Aditya Gupta
* ["IoT Penetration Testing Cookbook"][iot_penetration_testing_cookbook] by Aaron Guzman and Aditya Gupta
* ["The IoT Hacker's Handbook"][iot_hackers_handbook] by Aditya Gupta
* ["Practical IoT Hacking"][practical_iot_hacking] by Fotios Chantzis, Ioannis Stais, Paulino Calderon, Evangelos Deirmentzoglou, and Beau Woods
* Key aspects of testing of the T-Systems Multimedia Solutions GmbH

### Disclosure of Ecosystem Details (IOT-FW-INFO-003)

**Required Access Levels**

<table width="100%">
	<tr valign="top">
		<th width="1%" align="left">Physical</th>
 <td><i>PA-1</i> - <i>PA-4</i><br>(depending on how the firmware can be accessed, e.g., via an internal/physical debugging interface or remotely via SSH)</td>
	</tr>
	<tr valign="top">
		<th align="left">Authorization</th>
		<td><i>AA-1</i> - <i>AA-4</i><br>(depending on the access model for the given device) </td>
	</tr>
</table>

**Summary**

The contents of the device firmware might disclose information about the surrounding IoT ecosystem, e.g., sensitive URLs, IP addresses, software in use etc. An attacker might be able to use this information to prepare and execute attacks against the ecosystem.

For example, relevant information might be included in files of various types like configuration files and text files.

**Test Objectives**

- It must be determined if (parts of) the firmware, e.g., configuration files, contain relevant information about the surrounding ecosystem.

**Remediation**

The disclosure of information should be reduced to the minimum, which is required for operating the device. The disclosed information has to be assessed and all unnecessarily included data should be removed.

**References**

For this test case, data from the following available sources was consolidated:

* OWASP ["Firmware Security Testing Methodology"][owasp_fstm]
* ["IoT Pentesting Guide"][iot_pentesting_guide] by Aditya Gupta
* ["IoT Penetration Testing Cookbook"][iot_penetration_testing_cookbook] by Aaron Guzman and Aditya Gupta
* ["The IoT Hacker's Handbook"][iot_hackers_handbook] by Aditya Gupta
* ["Practical IoT Hacking"][practical_iot_hacking] by Fotios Chantzis, Ioannis Stais, Paulino Calderon, Evangelos Deirmentzoglou, and Beau Woods
* Key aspects of testing of the T-Systems Multimedia Solutions GmbH



## Configuration and Patch Management (IOT-FW-CONF)

Since IoT devices can have a long lifespan, it is important to make sure that the software, running on the device, is regularly updated in order to apply the latest security patches. The update process of the firmware itself will be covered by [IOT-FW[UPDT]](../firmware/firmware_update_mechanism.md). However, it must also be verified that software packages, which are included in the firmware, are up-to-date as well.

### Usage of Outdated Software (IOT-FW-CONF-001)

**Required Access Levels**

<table width="100%">
	<tr valign="top">
		<th width="1%" align="left">Physical</th>
 <td><i>PA-1</i> - <i>PA-4</i><br>(depending on how the firmware can be accessed, e.g., via an internal/physical debugging interface or remotely via SSH)</td>
	</tr>
	<tr valign="top">
		<th align="left">Authorization</th>
		<td><i>AA-1</i> - <i>AA-4</i><br>(depending on the access model for the given device) </td>
	</tr>
</table>

**Summary**

Every piece of software is potentially vulnerable to attacks. For example, coding errors could lead to undefined program behavior, which then can be exploited by an attacker to gain access to data, processed by the application, or to perform actions in the context of the runtime environment. Furthermore, vulnerabilities in the used frameworks, libraries and other technologies might also affect the security level of a given piece of software.

Usually, developers release an update once a vulnerability was detected in their software. These updates should be installed as soon as possible in order to reduce the probability of successful attacks. Otherwise, attackers could use known vulnerabilities to perform attacks against the device.

**Test Objectives**

- The version identifiers of installed software packages as well as libraries and frameworks in use must be determined.

- Based on the detected version identifiers, it must be determined if the software version in use is up-to-date, e.g., by consulting the website of the software developer or public repositories.

- By using vulnerability databases, such as the [National Vulnerability Database](https://nvd.nist.gov) of the NIST, it has to be checked whether any vulnerabilities are known for the detected software versions.

**Remediation**

The firmware should not include any outdated software packages. A proper patch management process, which ensures that applicable updates are installed once being available, should be implemented.

**References**

For this test case, data from the following available sources was consolidated:

* OWASP ["Firmware Security Testing Methodology"][owasp_fstm]
* ["IoT Penetration Testing Cookbook"][iot_penetration_testing_cookbook] by Aaron Guzman and Aditya Gupta
* ["Practical IoT Hacking"][practical_iot_hacking] by Fotios Chantzis, Ioannis Stais, Paulino Calderon, Evangelos Deirmentzoglou, and Beau Woods
* Key aspects of testing of the T-Systems Multimedia Solutions GmbH

### Presence of Unnecessary Software and Functionalities (IOT-FW-CONF-002)

**Required Access Levels**

<table width="100%">
	<tr valign="top">
		<th width="1%" align="left">Physical</th>
 <td><i>PA-1</i> - <i>PA-4</i><br>(depending on how the firmware can be accessed, e.g., via an internal/physical debugging interface or remotely via SSH)</td>
	</tr>
	<tr valign="top">
		<th align="left">Authorization</th>
		<td><i>AA-1</i> - <i>AA-4</i><br>(depending on the access model for the given device) </td>
	</tr>
</table>

**Summary**

Every piece of software, which is included in the firmware, broadens the attack surface since it might be used to perform attacks against the device. Even if the installed software is up-to-date, it might still be affected by unpublished vulnerabilities. It is also possible that a software program facilitates an attack without being vulnerable, e.g., by providing access to specific files or processes.

**Test Objectives**

- A list of software packages, that are included in the firmware, should be assembled.

- Based on the device documentation, its behavior and the intended use cases, it must be determined whether any of the installed software packages are not mandatory for the device operation.

**Remediation**

The attack surface should be minimized as much as possible by removing or disabling every software that is not required for the device operation.

Especially in case of general-purpose operating systems, such as Windows and Linux systems, it must be ensured that any unnecessary operating system features are disabled.

**References**

For this test case, data from the following sources was consolidated:

* OWASP ["Firmware Security Testing Methodology"][owasp_fstm]
* ["IoT Penetration Testing Cookbook"][iot_penetration_testing_cookbook] by Aaron Guzman and Aditya Gupta
* ["Practical IoT Hacking"][practical_iot_hacking] by Fotios Chantzis, Ioannis Stais, Paulino Calderon, Evangelos Deirmentzoglou, and Beau Woods
* Key aspects of testing of the T-Systems Multimedia Solutions GmbH



## Secrets (IOT-FW-SCRT)

IoT devices are often operated outside of the control space of their manufacturer. Still, they need to establish connections to other network nodes within the IoT ecosystem, e.g., to request and receive firmware updates or to send data to a cloud API. Hence, it might be required that the device has to provide some kind of authentication credential or secret. These secrets need to be stored on the device in a secure manner to prevent them from being stolen and used to impersonate the device.

### Secrets Stored in Public Storage (IOT-FW-SCRT-001)

**Required Access Levels**

<table width="100%">
	<tr valign="top">
		<th width="1%" align="left">Physical</th>
 <td><i>PA-1</i> - <i>PA-4</i><br>(depending on how the firmware can be accessed, e.g., via an internal/physical debugging interface or remotely via SSH)</td>
	</tr>
	<tr valign="top">
		<th align="left">Authorization</th>
		<td><i>AA-1</i> - <i>AA-4</i><br>(depending on the access model for the given device) </td>
	</tr>
</table>

**Summary**

Generally, there are multiple kinds of storage spaces within a file system, some of which are publicly available and some that can only be accessed with a certain level of privileges. If sensitive data or secrets are stored in publicly accessible storage spaces, users who should not have access to this data but who have access to the file system could read or modify it. In case of a successful attack, it is very likely that secrets, stored in public storage, are disclosed.

**Test Objectives**

- Files and databases within public storage spaces must be checked for the presence of secrets, such as passwords, symmetric or private keys and tokens.

**Remediation**

Access to secrets should only be granted to the accounts or processes with proper privileges. Thus, secrets should be stored in protected storage areas or designated key stores that are only available to certain entities.

**References**

For this test case, data from the following available sources was consolidated:

* OWASP ["Firmware Security Testing Methodology"][owasp_fstm]
* ["IoT Pentesting Guide"][iot_pentesting_guide] by Aditya Gupta
* ["IoT Penetration Testing Cookbook"][iot_penetration_testing_cookbook] by Aaron Guzman and Aditya Gupta
* ["The IoT Hacker's Handbook"][iot_hackers_handbook] by Aditya Gupta
* ["Practical IoT Hacking"][practical_iot_hacking] by Fotios Chantzis, Ioannis Stais, Paulino Calderon, Evangelos Deirmentzoglou, and Beau Woods
* Key aspects of testing of the T-Systems Multimedia Solutions GmbH

### Unencrypted Storage of Secrets (IOT-FW-SCRT-002)

**Required Access Levels**

<table width="100%">
	<tr valign="top">
		<th width="1%" align="left">Physical</th>
 <td><i>PA-1</i> - <i>PA-4</i><br>(depending on how the firmware can be accessed, e.g., via an internal/physical debugging interface or remotely via SSH)</td>
	</tr>
	<tr valign="top">
		<th align="left">Authorization</th>
		<td><i>AA-1</i> - <i>AA-4</i><br>(depending on the access model for the given device) </td>
	</tr>
</table>

**Summary**

Sensitive data and secrets should be stored in an encrypted manner, so that even if an attacker has managed to get access to it, he has no access to the respective plaintext data.

Contrary to [IOT-FW-SCRT-001](#secrets-stored-in-public-storage-iot-fw-scrt-001), it does not matter if the secrets are stored in public or restricted storage spaces, since it is assumed that the attacker has already gotten access to the data, e.g., by circumventing access restrictions or by exploiting a process with access to the restricted storage. Furthermore, the strength of the cryptographic algorithms in use will be covered by [IOT-FW-CRYPT-001](#usage-of-weak-cryptographic-algorithms-iot-fw-crypt-001) and has no relevance for this test case.

**Test Objectives**

- By searching public and restricted storage spaces, it must be determined whether the firmware includes secrets in plaintext form.

**Remediation**

Secrets have to be stored using proper cryptographic algorithms. Only the encrypted form of the secret should be stored.

**References**

For this test case, data from the following sources was consolidated:

* OWASP ["Firmware Security Testing Methodology"][owasp_fstm]
* ["IoT Pentesting Guide"][iot_pentesting_guide] by Aditya Gupta
* ["IoT Penetration Testing Cookbook"][iot_penetration_testing_cookbook] by Aaron Guzman and Aditya Gupta
* ["The IoT Hacker's Handbook"][iot_hackers_handbook] by Aditya Gupta
* ["Practical IoT Hacking"][practical_iot_hacking] by Fotios Chantzis, Ioannis Stais, Paulino Calderon, Evangelos Deirmentzoglou, and Beau Woods
* Key aspects of testing of the T-Systems Multimedia Solutions GmbH

### Usage of Hardcoded Secrets (IOT-FW-SCRT-003)

**Required Access Levels**

<table width="100%">
	<tr valign="top">
		<th width="1%" align="left">Physical</th>
 <td><i>PA-1</i> - <i>PA-4</i><br>(depending on how the firmware can be accessed, e.g., via an internal/physical debugging interface or remotely via SSH)</td>
	</tr>
	<tr valign="top">
		<th align="left">Authorization</th>
		<td><i>AA-1</i> - <i>AA-4</i><br>(depending on the access model for the given device) </td>
	</tr>
</table>

**Summary**

Sometimes, developers tend to incorporate secrets directly into the source code of their software. This can lead to a variety of security issues like:

- the disclosure of secrets via published source code snippets or decompiled source code,

- endangering all devices that are using the given software since it is very likely that the same secret is used on all devices (otherwise, the source code needs to be changed and compiled for every device individually) and

- impeding reactive measures in case of the secret being compromised since changing the secret requires a software update.

**Test Objectives**

- Based on [IOT-FW-INFO-001](#disclosure-of-source-code-iot-fw-info-001), it must be checked if any hard-coded secrets can be identified.

**Remediation**

Secrets should not be hard-coded into the source code. Instead, secrets should be stored in a secure manner (see [IOT-FW-SCRT-001](#secrets-stored-in-public-storage-iot-fw-scrt-001) and [IOT-FW-SCRT-002](#unencrypted-storage-of-secrets-iot-fw-scrt-002)) and the software process should dynamically retrieve the secrets from the secure storage during runtime.

**References**

For this test case, data from the following available sources was consolidated:

* OWASP ["Firmware Security Testing Methodology"][owasp_fstm]
* ["IoT Pentesting Guide"][iot_pentesting_guide] by Aditya Gupta
* ["IoT Penetration Testing Cookbook"][iot_penetration_testing_cookbook] by Aaron Guzman and Aditya Gupta
* ["The IoT Hacker's Handbook"][iot_hackers_handbook] by Aditya Gupta
* ["Practical IoT Hacking"][practical_iot_hacking] by Fotios Chantzis, Ioannis Stais, Paulino Calderon, Evangelos Deirmentzoglou, and Beau Woods
* Key aspects of testing of the T-Systems Multimedia Solutions GmbH



## Cryptography (IOT-FW-CRYPT)

Many IoT devices need to implement cryptographic algorithms, e.g., to securely store sensitive data, for authentication purposes or to receive and verify encrypted data from other network nodes. Failing to implement secure, state of the art cryptography might lead to the exposure of sensitive data, device malfunctions or loss of control over the device.

### Usage of Weak Cryptographic Algorithms (IOT-FW-CRYPT-001)

**Required Access Levels**

<table width="100%">
	<tr valign="top">
		<th width="1%" align="left">Physical</th>
 <td><i>PA-1</i> - <i>PA-4</i><br>(depending on how the firmware can be accessed, e.g., via an internal/physical debugging interface or remotely via SSH)</td>
	</tr>
	<tr valign="top">
		<th align="left">Authorization</th>
		<td><i>AA-1</i> - <i>AA-4</i><br>(depending on the access model for the given device) </td>
	</tr>
</table>

**Summary**

Cryptography can be implemented in various ways. However, due to evolving technologies, new algorithms and more computing power becoming available, many old cryptographic algorithms are nowadays considered weak or insecure. Thus, either new and stronger cryptographic algorithms have to be used or existing algorithms must be adapted, e.g., by increasing the key length or using alternative modes of operation.

The usage of weak cryptographic algorithms might allow an attacker to recover the plaintext from a given ciphertext in a timely manner.

**Test Objectives**

- The data, stored by or within the firmware, must be checked for the presence of encrypted data segments. In case that encrypted data segments are found, it must be checked whether the cryptographic algorithms in use can be identified.

- Furthermore, based on [IOT-FW-INFO-001](#disclosure-of-source-code-iot-fw-info-001) and [IOT-FW-INFO-002](#disclosure-of-implementation-details-iot-fw-info-002), it must be checked whether any source code, configuration files etc. disclose the usage of certain cryptographic algorithms.

- In case that cryptographic algorithms can be identified, it must be determined whether the algorithms in use and their configuration are providing a sufficient level of security at the time of testing, e.g., by consulting cryptography guidelines like the technical guideline [TR-02102-1](https://www.bsi.bund.de/SharedDocs/Downloads/EN/BSI/Publications/TechGuidelines/TG02102/BSI-TR-02102-1.pdf?__blob=publicationFile&v=10) by the BSI.

**Remediation**

Only strong, state of the art cryptographic algorithms should be used. Furthermore, these algorithms must be used in a secure manner by setting proper parameters, such as an appropriate key length or mode of operation.

**References**

For this test case, data from the following sources was consolidated:

* OWASP ["Firmware Security Testing Methodology"][owasp_fstm]
* ["IoT Pentesting Guide"][iot_pentesting_guide] by Aditya Gupta
* ["IoT Penetration Testing Cookbook"][iot_penetration_testing_cookbook] by Aaron Guzman and Aditya Gupta
* ["The IoT Hacker's Handbook"][iot_hackers_handbook] by Aditya Gupta
* Key aspects of testing of the T-Systems Multimedia Solutions GmbH



[owasp_fstm]: https://github.com/scriptingxss/owasp-fstm	"OWASP Firmware Security Testing Methodology"
[iot_pentesting_guide]: https://www.iotpentestingguide.com	"IoT Pentesting Guide"
[iot_penetration_testing_cookbook]: https://www.packtpub.com/product/iot-penetration-testing-cookbook/9781787280571	"IoT Penetration Testing Cookbook"
[iot_hackers_handbook]: https://link.springer.com/book/10.1007/978-1-4842-4300-8	"The IoT Hacker's Handbook"
[practical_iot_hacking]: https://nostarch.com/practical-iot-hacking	"Practical IoT Hacking"