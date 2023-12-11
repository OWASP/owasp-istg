# 3.3.2. Firmware Update Mechanism (IOT-FW[UPDT])

## Table of Contents
* [Overview](#overview)
* [Authorization (IOT-FW-AUTHZ)](#authorization-iot-fw[updt]-authz)
  * [Unauthorized Firmware Update (IOT-FW-AUTHZ-001)](#unauthorized-firmware-update-iot-fw[updt]-authz-001)
* [Cryptography (IOT-FW-CRYPT)](#cryptography-iot-fw[updt]-crypt)
  * [Insufficient Firmware Update Signature (IOT-FW-CRYPT-001)](#insufficient-firmware-update-signature-iot-fw[updt]-crypt-001)
  * [Insufficient Firmware Update Encryption (IOT-FW-CRYPT-002)](#insufficient-firmware-update-encryption-iot-fw[updt]-crypt-002)
  * [Insecure Transmission of the Firmware Update (IOT-FW-CRYPT-003)](#insecure-transmission-of-the-firmware-update-iot-fw[updt]-crypt-003)
  * [Insufficient Verification of the Firmware Update Signature (IOT-FW-CRYPT-004)](#insufficient-verification-of-the-firmware-update-signature-iot-fw[updt]-crypt-004)
* [Business Logic (IOT-FW-LOGIC)](#business-logic-iot-fw[updt]-logic)
  * [Insufficient Rollback Protection (IOT-FW-LOGIC-001)](#insufficient-rollback-protection-iot-fw[updt]-logic-001)



## Overview

Another important aspect of the device firmware is the firmware update mechanism. Failing to implement a secure update mechanism might enable attackers to install a custom, manipulated firmware on the device, thus gaining complete control over it.

The following categories are not inherited by the specialization [IOT-FW[UPDT]](./firmware_update_mechanism.md):

- **Configuration and Patch Management ([IOT-FW-CONF](./README.md#configuration-and-patch-management-iot-fw-conf))**: This category focuses on the configuration and patch management aspects of a firmware file. Since [IOT-FW[UPDT]](./firmware_update_mechanism.md) focuses on the firmware update mechanism rather than a specific firmware file, the respective test cases are not applicable.

- **Secrets ([IOT-FW-SCRT](./README.md#secrets-iot-fw-scrt))**: This category focuses on the handling of secrets within a firmware file. Since [IOT-FW[UPDT]](./firmware_update_mechanism.md) focuses on the firmware update mechanism rather than a specific firmware file, the respective test cases are not applicable.



## Authorization (IOT-FW[UPDT]-AUTHZ)

Since the test of the firmware update mechanism is also a dynamic analysis, it is possible to check if only authorized individuals can initialize and perform an update.

### Unauthorized Firmware Update (IOT-FW[UPDT]-AUTHZ-001)

**Required Access Levels**

<table width="100%">
	<tr valign="top">
		<th width="1%" align="left">Physical</th>
 <td><i>PA-1</i> - <i>PA-4</i><br>(depending on how the firmware can be accessed, e.g., via an internal/physical debugging interface or remotely via SSH)</td>
	</tr>
	<tr valign="top">
		<th align="left">Authorization</th>
		<td><i>AA-1</i> - <i>AA-3</i><br>(depending on the access model for the given device) </td>
	</tr>
</table>

**Summary**

Depending on the specific implementation of a given device, the permission to perform firmware updates might be restricted to individuals with a certain authorization access level, e.g., *AA-2*, *AA-3* or *AA-4*. If the device firmware fails to correctly verify these permissions, any attacker (*AA-1*) or an attacker with a lower authorization access level than intended might be able to perform unintended firmware updates.

**Test Objectives**

- It must be checked if authorization checks for performing a firmware update are implemented.

- In case that authorization checks are in place, it must be determined whether there is a way to bypass them.

**Remediation**

Proper authorization checks need to be implemented, which ensure that a firmware update can only be performed by individuals with certain authorization access levels.

**References**

For this test case, data from the following sources was consolidated:

* OWASP ["Firmware Security Testing Methodology"][owasp_fstm]
* Key aspects of testing of the T-Systems Multimedia Solutions GmbH



## Cryptography (IOT-FW[UPDT]-CRYPT)

During the firmware update process, cryptographic algorithms are used to verify the integrity of the new firmware and to ensure that no sensitive data is disclosed in transit.

### Insufficient Firmware Update Signature (IOT-FW[UPDT]-CRYPT-001)

**Required Access Levels**

<table width="100%">
	<tr valign="top">
		<th width="1%" align="left">Physical</th>
 <td><i>PA-1</i> - <i>PA-4</i><br>(depending on how the firmware can be accessed, e.g., via an internal/physical debugging interface or remotely via SSH)</td>
	</tr>
	<tr valign="top">
		<th align="left">Authorization</th>
		<td><i>AA-1</i> - <i>AA-4</i><br>(depending on the access model for the given device) </td>
	</tr>
</table>

**Summary**

One way to manipulate a device would be to install a manipulated firmware package. In order to enable the detection of modifications, the firmware update package needs to be digitally signed. This way, the validity of the package can be verified during the installation or update process.

**Test Objectives**

- It must be determined if a digital signature for the firmware update package is available.

- If a digital signature is available, it must be checked whether the validity of the signature can be verified.

- Based on [IOT-FW-CRYPT-001](./README.md#usage-of-weak-cryptographic-algorithms-iot-fw-crypt-001), the cryptographic algorithm, used for generating the digital signature, has to be assessed in order to determine whether a weak our outdated algorithm was used.

**Remediation**

A valid digital signature must be available for the firmware update package. Furthermore, it must be possible to verify the validity of the digital signature.

**References**

For this test case, data from the following sources was consolidated:

* OWASP ["Firmware Security Testing Methodology"][owasp_fstm]
* ["IoT Penetration Testing Cookbook"][iot_penetration_testing_cookbook] by Aaron Guzman and Aditya Gupta
* ["Practical IoT Hacking"][practical_iot_hacking] by Fotios Chantzis, Ioannis Stais, Paulino Calderon, Evangelos Deirmentzoglou, and Beau Woods
* Key aspects of testing of the T-Systems Multimedia Solutions GmbH

### Insufficient Firmware Update Encryption (IOT-FW[UPDT]-CRYPT-002)

**Required Access Levels**

<table width="100%">
	<tr valign="top">
		<th width="1%" align="left">Physical</th>
 <td><i>PA-1</i> - <i>PA-4</i><br>(depending on how the firmware can be accessed, e.g., via an internal/physical debugging interface or remotely via SSH)</td>
	</tr>
	<tr valign="top">
		<th align="left">Authorization</th>
		<td><i>AA-1</i> - <i>AA-4</i><br>(depending on the access model for the given device) </td>
	</tr>
</table>

**Summary**

Firmware update packages might include confidential data of the soft- and hardware developer, e.g., intellectual property. Hence, it might be required to encrypt the package itself.

**Test Objectives**

- It has to be clarified with the firmware developer whether the firmware update package needs to be encrypted.

- If encryption is required, it must be determined whether the package is encrypted.

- Based on [IOT-FW-CRYPT-001](./README.md#usage-of-weak-cryptographic-algorithms-iot-fw-crypt-001), it has to be determined whether proper algorithms were used for encryption.

**Remediation**

The firmware update package should be encrypted using state of the art cryptographic algorithms.

**References**

For this test case, data from the following sources was consolidated:

* OWASP ["Firmware Security Testing Methodology"][owasp_fstm]
* ["IoT Pentesting Guide"][iot_pentesting_guide] by Aditya Gupta
* ["IoT Penetration Testing Cookbook"][iot_penetration_testing_cookbook] by Aaron Guzman and Aditya Gupta
* ["The IoT Hacker's Handbook"][iot_hackers_handbook] by Aditya Gupta
* ["Practical IoT Hacking"][practical_iot_hacking] by Fotios Chantzis, Ioannis Stais, Paulino Calderon, Evangelos Deirmentzoglou, and Beau Woods
* Key aspects of testing of the T-Systems Multimedia Solutions GmbH

### Insecure Transmission of the Firmware Update (IOT-FW[UPDT]-CRYPT-003)

**Required Access Levels**

<table width="100%">
	<tr valign="top">
		<th width="1%" align="left">Physical</th>
 <td><i>PA-1</i> - <i>PA-4</i><br>(depending on how the firmware can be accessed, e.g., via an internal/physical debugging interface or remotely via SSH)</td>
	</tr>
	<tr valign="top">
		<th align="left">Authorization</th>
		<td><i>AA-1</i> - <i>AA-4</i><br>(depending on the access model for the given device) </td>
	</tr>
</table>

**Summary**

If the firmware update process is not performed via a secure channel or if no further measures are in place to ensure the confidentiality and to detect modifications of the transmitted data, an attacker with access to the communication channel might be able to interfere with the update process.

**Test Objectives**

- It has to be determined whether the firmware update is performed over a secure channel.

- If the firmware update is performed over an insecure channel, like the internet, it must be checked whether proper measures in regards of confidentiality and integrity are in place.

- If, for example, the communication channel is secured using TLS, it must be checked which cipher suites are supported and if the server certificate is validated by the client.

**Remediation**

If feasible, the firmware update should be performed via a secure channel. Otherwise, proper measures need to be implemented in order to prevent or detect interferences with potential attackers.

**References**

For this test case, data from the following sources was consolidated:

* OWASP ["Firmware Security Testing Methodology"][owasp_fstm]
* ["IoT Penetration Testing Cookbook"][iot_penetration_testing_cookbook] by Aaron Guzman and Aditya Gupta
* ["Practical IoT Hacking"][practical_iot_hacking] by Fotios Chantzis, Ioannis Stais, Paulino Calderon, Evangelos Deirmentzoglou, and Beau Woods
* Key aspects of testing of the T-Systems Multimedia Solutions GmbH

### Insufficient Verification of the Firmware Update Signature (IOT-FW[UPDT]-CRYPT-004)

**Required Access Levels**

<table width="100%">
	<tr valign="top">
		<th width="1%" align="left">Physical</th>
 <td><i>PA-1</i> - <i>PA-4</i><br>(depending on how the firmware can be accessed, e.g., via an internal/physical debugging interface or remotely via SSH)</td>
	</tr>
	<tr valign="top">
		<th align="left">Authorization</th>
		<td><i>AA-1</i> - <i>AA-4</i><br>(depending on the access model for the given device) </td>
	</tr>
</table>

**Summary**

Even if the firmware update package is digitally signed, an attacker could install a manipulated firmware package on the device in case that the digital signature is not properly validated. For example, the device might not reject the update if no signature is provided.

**Test Objectives**

- Based on [IOT-FW-CRYPT-001](./README.md#usage-of-weak-cryptographic-algorithms-iot-fw-crypt-001), it must be checked if the signature of the firmware update package is properly verified by the device during the update process.

**Remediation**

The device must properly verify the digital signature of an update package before the installation process is started. Any update package without a valid signature or with no signature at all should be rejected.

**References**

For this test case, data from the following sources was consolidated:

* OWASP ["Firmware Security Testing Methodology"][owasp_fstm]
* ["IoT Penetration Testing Cookbook"][iot_penetration_testing_cookbook] by Aaron Guzman and Aditya Gupta
* ["Practical IoT Hacking"][practical_iot_hacking] by Fotios Chantzis, Ioannis Stais, Paulino Calderon, Evangelos Deirmentzoglou, and Beau Woods
* Key aspects of testing of the T-Systems Multimedia Solutions GmbH



## Business Logic (IOT-FW[UPDT]-LOGIC)

Even if all other aspects of the firmware update are securely implemented, issues in the underlying logic of the update process itself might render the device vulnerable to attacks. Thus, it must be verified if the process is working as intended and if exceptions are detected and properly handled.

### Insufficient Rollback Protection (IOT-FW[UPDT]-LOGIC-001)

**Required Access Levels**

<table width="100%">
	<tr valign="top">
		<th width="1%" align="left">Physical</th>
 <td><i>PA-1</i> - <i>PA-4</i><br>(depending on how the firmware can be accessed, e.g., via an internal/physical debugging interface or remotely via SSH)</td>
	</tr>
	<tr valign="top">
		<th align="left">Authorization</th>
		<td><i>AA-1</i> - <i>AA-4</i><br>(depending on the access model for the given device) </td>
	</tr>
</table>

**Summary**

Some manufacturers implement a rollback protection for their devices. This rollback protection prevents updating a device firmware to an older version than the currently installed one. This way, an attacker can not install a valid but outdated firmware in order to exploit known vulnerabilities of that version.

**Test Objectives**

- It must has to be assessed whether it is possible to install older versions of the firmware.

**Remediation**

A proper rollback protection mechanism verifying that the firmware version to be installed is newer than the currently installed version should be implemented.

**References**

For this test case, data from the following sources was consolidated:

* ["IoT Penetration Testing Cookbook"][iot_penetration_testing_cookbook] by Aaron Guzman and Aditya Gupta
* Key aspects of testing of the T-Systems Multimedia Solutions GmbH



[owasp_fstm]: https://github.com/scriptingxss/owasp-fstm	"OWASP Firmware Security Testing Methodology"
[iot_pentesting_guide]: https://www.iotpentestingguide.com	"IoT Pentesting Guide"
[iot_penetration_testing_cookbook]: https://www.packtpub.com/product/iot-penetration-testing-cookbook/9781787280571	"IoT Penetration Testing Cookbook"
[iot_hackers_handbook]: https://link.springer.com/book/10.1007/978-1-4842-4300-8	"The IoT Hacker's Handbook"
[practical_iot_hacking]: https://nostarch.com/practical-iot-hacking	"Practical IoT Hacking"
