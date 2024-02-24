# 3.2. Memory (ISTG-MEM)

## Table of Contents
* [Overview](#overview)
* [Information Gathering (ISTG-MEM-INFO)](#information-gathering-istg-mem-info)
  * [Disclosure of Source Code and Binaries (ISTG-MEM-INFO-001)](#disclosure-of-source-code-and-binaries-istg-mem-info-001)
  * [Disclosure of Implementation Details (ISTG-MEM-INFO-002)](#disclosure-of-implementation-details-istg-mem-info-002)
  * [Disclosure of Ecosystem Details (ISTG-MEM-INFO-003)](#disclosure-of-ecosystem-details-istg-mem-info-003)
  * [Disclosure of User Data (ISTG-MEM-INFO-004)](#disclosure-of-user-data-istg-mem-info-004)
* [Secrets (ISTG-MEM-SCRT)](#secrets-istg-mem-scrt)
  * [Unencrypted Storage of Secrets (ISTG-MEM-SCRT-001)](#unencrypted-storage-of-secrets-istg-mem-scrt-001)
* [Cryptography (ISTG-MEM-CRYPT)](#cryptography-istg-mem-crypt)
  * [Usage of Weak Cryptographic Algorithms (ISTG-MEM-CRYPT-001)](#usage-of-weak-cryptographic-algorithms-istg-mem-crypt-001)




## Overview

This section includes test cases and categories for the component memory. Similar to the processing unit, the memory is a device-internal element that can only be accessed with *PA-4*. Establishing a direct connection to the memory might require specific hardware equipment (e.g., a debugging board or test probes).

In regards to test case categories that are relevant for memory, the following were identified:

- **Information Gathering:** Focuses on information that is stored on the memory chip and that might be disclosed to potential attackers if not being properly protected or removed.

- **Secrets:** Focuses on secrets that are stored on the memory chip in an insecure manner.

- **Cryptography:** Focuses on vulnerabilities in the cryptographic implementation.



## Information Gathering (ISTG-MEM-INFO)

The memory of an IoT device can include various data, which, if disclosed, could reveal details regarding the inner workings of the device or the underlying IoT ecosystem to potential attackers. This could enable and facilitate further, more advanced attacks.

Tests on the device memory are performed by directly accessing the memory chips. Thus, invasive physical access (*PA-4*) is required while no user accounts are used (*AA-1*).

### Disclosure of Source Code and Binaries (ISTG-MEM-INFO-001)
**Required Access Levels**

<table width="100%">
	<tr valign="top">
		<th width="1%" align="left">Physical</th>
 <td><i>PA-4</i></td>
	</tr>
	<tr valign="top">
		<th align="left">Authorization</th>
		<td><i>AA-1</i></tr>
</table>

**Summary**

The disclosure of uncompiled source code could accelerate the exploitation of the software implementation since vulnerabilities can be directly identified in the code without the need to perform tests in a trial and error manner. Furthermore, left-over source code might include internal development information, developer comments or hard-coded sensitive data, which were not intended for productive use.

Similar to uncompiled source code, compiled binaries might also disclose relevant information. However, reverse-engineering might be required to retrieve useful data, which could take a considerable amount of time. Thus, the tester has to assess which binaries might be worth analyzing, ideally in coordination with the device manufacturer.

**Test Objectives**

- It must be checked if uncompiled source code can be identified within the device memory.

- If uncompiled source code is detected, its content must be analyzed for the presence of sensitive data, which might be useful for potential attackers.

- Reverse-engineering of selected binaries should be performed in order to obtain useful information regarding the device implementation and the processing of sensitive data.

**Remediation**

If possible, uncompiled source code should be removed from devices, intended for productive use. If the source code has to be included, it must be verified that all internal development data is removed before releasing the device.

Since it is not possible to prevent reverse-engineering completely, measures to restrict access to the device memory in general should be implemented to reduce the attack surface. Furthermore, the reverse-engineering process can be impeded, e.g., by obfuscating the code.

**References**

For this test case, data from the following sources was consolidated:

* ["IoT Pentesting Guide"][iot_pentesting_guide] by Aditya Gupta
* ["IoT Penetration Testing Cookbook"][iot_penetration_testing_cookbook] by Aaron Guzman and Aditya Gupta
* ["The IoT Hacker's Handbook"][iot_hackers_handbook] by Aditya Gupta

This test case is based on: [ISTG-FW-INFO-001](../firmware/README.md#disclosure-of-source-code-and-binaries-istg-fw-info-001).

### Disclosure of Implementation Details (ISTG-MEM-INFO-002)
**Required Access Levels**

<table width="100%">
	<tr valign="top">
		<th width="1%" align="left">Physical</th>
 <td><i>PA-4</i></td>
	</tr>
	<tr valign="top">
		<th align="left">Authorization</th>
		<td><i>AA-1</i></tr>
</table>

**Summary**

If details about the implementation, e.g., algorithms in use or the authentication procedure, are available to potential attackers, flaws and entry points for successful attacks are easier to detect. While the disclosure of such details alone is not considered to be a vulnerability, it facilitates the identification of potential attack vectors, thus allowing an attacker to exploit insecure implementations faster.

**Test Objectives**

- Accessible details regarding the implementation must be assessed in order to prepare further tests. For example, this includes:
  - Cryptographic algorithms in use

  - Authentication and authorization mechanism

  - Local paths and environment details


**Remediation**

As mentioned above, the disclosure of such information is not considered a vulnerability. However, in order to impede exploitation attempts, only information necessary for the device operation should be stored on it.

**References**

For this test case, data from the following sources was consolidated:

* ["IoT Pentesting Guide"][iot_pentesting_guide] by Aditya Gupta
* ["IoT Penetration Testing Cookbook"][iot_penetration_testing_cookbook] by Aaron Guzman and Aditya Gupta
* ["The IoT Hacker's Handbook"][iot_hackers_handbook] by Aditya Gupta

This test case is based on: [ISTG-FW-INFO-002](../firmware/README.md#disclosure-of-implementation-details-istg-fw-info-002).

### Disclosure of Ecosystem Details (ISTG-MEM-INFO-003)
**Required Access Levels**

<table width="100%">
	<tr valign="top">
		<th width="1%" align="left">Physical</th>
 <td><i>PA-4</i></td>
	</tr>
	<tr valign="top">
		<th align="left">Authorization</th>
		<td><i>AA-1</i></tr>
</table>

**Summary**

The contents of the device memory might disclose information about the surrounding IoT ecosystem, e.g., sensitive URLs, IP addresses, software in use etc. An attacker might be able to use this information to prepare and execute attacks against the ecosystem.

For example, relevant information might be included in files of various types like configuration files and text files.

**Test Objectives**

- It must be determined if the data stored in the device memory, e.g., configuration files, contain relevant information about the surrounding ecosystem.

**Remediation**

The disclosure of information should be reduced to the minimum, which is required for operating the device. The disclosed information has to be assessed and all unnecessarily included data should be removed.

**References**

For this test case, data from the following sources was consolidated:

* ["IoT Pentesting Guide"][iot_pentesting_guide] by Aditya Gupta
* ["IoT Penetration Testing Cookbook"][iot_penetration_testing_cookbook] by Aaron Guzman and Aditya Gupta
* ["The IoT Hacker's Handbook"][iot_hackers_handbook] by Aditya Gupta

This test case is based on: [ISTG-FW-INFO-003](../firmware/README.md#disclosure-of-ecosystem-details-istg-fw-info-003).

### Disclosure of User Data (ISTG-MEM-INFO-004)
**Required Access Levels**

<table width="100%">
	<tr valign="top">
		<th width="1%" align="left">Physical</th>
 <td><i>PA-4</i></td>
	</tr>
	<tr valign="top">
		<th align="left">Authorization</th>
		<td><i>AA-1</i></tr>
</table>

**Summary**

During runtime, a device is accumulating and processing data of different kinds, such as personal data of its users. If this data is not stored securely, an attacker might be able to recover it from the device.

**Test Objectives**

- It has to be checked whether user data can be accessed by unauthorized individuals.

**Remediation**

Access to user data should only be granted to individuals and processes that need to have access to it. No unauthorized or not properly authorized individual should be able to recover user data.

**References**

For this test case, data from the following sources was consolidated:

* ["IoT Pentesting Guide"][iot_pentesting_guide] by Aditya Gupta
* ["IoT Penetration Testing Cookbook"][iot_penetration_testing_cookbook] by Aaron Guzman and Aditya Gupta
* ["The IoT Hacker's Handbook"][iot_hackers_handbook] by Aditya Gupta

This test case is based on: [ISTG-FW[INST]-INFO-001](../firmware/installed_firmware.md#disclosure-of-user-data-istg-fw[inst]-info-001).



## Secrets (ISTG-MEM-SCRT)

IoT devices are often operated outside of the control space their manufacturer. Still, they need to establish connections to other network nodes within the IoT ecosystem, e.g., to request and receive firmware updates or to send data to a cloud API. Hence, it might be required that the device can provide some kind of authentication credential or secret. These secrets need to be stored on the device in a secure manner to prevent them from being stolen and used to impersonate the device.

### Unencrypted Storage of Secrets (ISTG-MEM-SCRT-001)
**Required Access Levels**

<table width="100%">
	<tr valign="top">
		<th width="1%" align="left">Physical</th>
 <td><i>PA-4</i></td>
	</tr>
	<tr valign="top">
		<th align="left">Authorization</th>
		<td><i>AA-1</i></tr>
</table>

**Summary**

Sensitive data and secrets should be stored in an encrypted manner, so that even if an attacker has managed to get access to the memory, he has no access to the respective plaintext data.

The strength of the cryptographic algorithms in use will be covered by [ISTG-MEM-CRYPT-001](#usage-of-weak-cryptographic-algorithms-istg-mem-crypt-001) and has no relevance for this test case.

**Test Objectives**

- By searching the contents of the device memory, it must be determined whether it includes secrets in plaintext form.

**Remediation**

Secrets have to be stored using proper cryptographic algorithms. Only the encrypted form of the secret should be stored.

**References**

For this test case, data from the following sources was consolidated:

* ["IoT Pentesting Guide"][iot_pentesting_guide] by Aditya Gupta
* ["IoT Penetration Testing Cookbook"][iot_penetration_testing_cookbook] by Aaron Guzman and Aditya Gupta

This test case is based on: [ISTG-FW-SCRT-002](../firmware/README.md#unencrypted-storage-of-secrets-istg-fw-scrt-002).



## Cryptography (ISTG-MEM-CRYPT)

Many IoT devices need to implement cryptographic algorithms, e.g., to securely store sensitive data, for authentication purposes or to receive and verify encrypted data from other network nodes. Failing to implement secure, state of the art cryptography might lead to the exposure of sensitive data, device malfunctions or loss of control over the device.

### Usage of Weak Cryptographic Algorithms (ISTG-MEM-CRYPT-001)
**Required Access Levels**

<table width="100%">
	<tr valign="top">
		<th width="1%" align="left">Physical</th>
 <td><i>PA-4</i></td>
	</tr>
	<tr valign="top">
		<th align="left">Authorization</th>
		<td><i>AA-1</i></tr>
</table>

**Summary**

Cryptography can be implemented in various ways. However, due to evolving technologies, new algorithms and more computing power becoming available, many old cryptographic algorithms are nowadays considered weak or insecure. Thus, either new and stronger cryptographic algorithms have to be used or existing algorithms must be adapted, e.g., by increasing the key length or using alternative modes of operation.

The usage of weak cryptographic algorithms might allow an attacker to recover the plaintext from a given ciphertext in a timely manner.

**Test Objectives**

- The data, stored on the device, must be checked for the presence of encrypted data segments. In case that encrypted data segments are found, it must be checked whether the cryptographic algorithms in use can be identified.

- Furthermore, based on [ISTG-MEM-INFO-001](#disclosure-of-source-code-and-binaries-istg-mem-info-001) and [ISTG-MEM-INFO-002](#disclosure-of-implementation-details-istg-mem-info-002), it must be checked whether any source code, configuration files etc. disclose the usage of certain cryptographic algorithms.

- In case that cryptographic algorithms can be identified, it must be determined whether the algorithms in use and their configuration are providing a sufficient level of security at the time of testing, e.g., by consulting cryptography guidelines like the technical guideline [TR-02102-1](https://www.bsi.bund.de/SharedDocs/Downloads/EN/BSI/Publications/TechGuidelines/TG02102/BSI-TR-02102-1.pdf?__blob=publicationFile&v=10) by the BSI.

**Remediation**

Only strong, state of the art cryptographic algorithms should be used. Furthermore, these algorithms must be used in a secure manner by setting proper parameters, such as an appropriate key length or mode ofoperation.

**References**

For this test case, data from the following sources was consolidated:

* ["IoT Pentesting Guide"][iot_pentesting_guide] by Aditya Gupta
* ["IoT Penetration Testing Cookbook"][iot_penetration_testing_cookbook] by Aaron Guzman and Aditya Gupta

This test case is based on: [ISTG-FW-CRYPT-001](../firmware/README.md#usage-of-weak-cryptographic-algorithms-istg-fw-crypt-001).



[iot_pentesting_guide]: https://www.iotpentestingguide.com	"IoT Pentesting Guide"
[iot_penetration_testing_cookbook]: https://www.packtpub.com/product/iot-penetration-testing-cookbook/9781787280571	"IoT Penetration Testing Cookbook"
[iot_hackers_handbook]: https://link.springer.com/book/10.1007/978-1-4842-4300-8	"The IoT Hacker's Handbook"