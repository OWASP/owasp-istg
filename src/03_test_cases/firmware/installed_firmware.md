# 3.3.1. Installed Firmware (ISTG-FW[INST])

## Table of Contents
* [Overview](#overview)
* [Authorization (ISTG-FW-AUTHZ)](#authorization-istg-fw[inst]-authz)
  * [Unauthorized Access to the Firmware (ISTG-FW-AUTHZ-001)](#unauthorized-access-to-the-firmware-istg-fw[inst]-authz-001)
  * [Privilege Escalation (ISTG-FW-AUTHZ-002)](#privilege-escalation-istg-fw[inst]-authz-002)
* [Information Gathering (ISTG-FW-INFO)](#information-gathering-istg-fw[inst]-info)
  * [Disclosure of User Data (ISTG-FW-INFO-001)](#disclosure-of-user-data-istg-fw[inst]-info-001)
* [Cryptography (ISTG-FW-CRYPT)](#cryptography-istg-fw[inst]-crypt)
  * [Insufficient Verification of the Bootloader Signature (ISTG-FW-CRYPT-001)](#insufficient-verification-of-the-bootloader-signature-istg-fw[inst]-crypt-001)




## Overview

One specialization of the component firmware is the installed form of a firmware, which might be the subject of a dynamic analysis. The dynamic analysis allows to test the handling of data during runtime. This way, the processing and storing of user data can also be analyzed. As a pre-requisite for the dynamic analysis, a device, which is running the target firmware version, must be provided.



## Authorization (ISTG-FW[INST]-AUTHZ)

Usually, only certain individuals, e.g., administrators, should be allowed to access the device firmware during runtime. Thus, proper authentication and authorization procedures need to be in place, which ensure that only authorized users can get access to the firmware.

### Unauthorized Access to the Firmware (ISTG-FW[INST]-AUTHZ-001)

**Required Access Levels**

<table width="100%">
	<tr valign="top">
		<th width="1%" align="left">Physical</th>
 <td><i>PA-1</i> - <i>PA-4</i><br>(depending on how the firmware can be accessed, e.g., via an internal/physical debugging interface or remotely via SSH)</td>
	</tr>
	<tr valign="top">
		<th align="left">Authorization</th>
		<td><i>AA-1</i></td>
	</tr>
</table>

**Summary**

Depending on the specific implementation of a given device, access to the firmware or its functions might be restricted to individuals with a certain authorization access level, e.g., *AA-2*, *AA-3* or *AA-4*. If the device firmware fails to correctly verify access permissions, any attacker (*AA-1*) might be able to get access to the firmware.

**Test Objectives**

- It must be checked if authorization checks for access to the firmware are implemented.

- In case that authorization checks are in place, it must be determined whether there is a way to bypass them.

**Remediation**

Proper authorization checks need to be implemented, which ensure that access to the firmware is only possible for authorized individuals.

**References**

For this test case, data from the following sources was consolidated:

* OWASP ["Firmware Security Testing Methodology"][owasp_fstm]
* ["IoT Penetration Testing Cookbook"][iot_penetration_testing_cookbook] by Aaron Guzman and Aditya Gupta
* ["The IoT Hacker's Handbook"][iot_hackers_handbook] by Aditya Gupta
* ["Practical IoT Hacking"][practical_iot_hacking] by Fotios Chantzis, Ioannis Stais, Paulino Calderon, Evangelos Deirmentzoglou, and Beau Woods
* Key aspects of testing of the T-Systems Multimedia Solutions GmbH

This test case is based on: [ISTG-DES-AUTHZ-001](../data_exchange_services/README.md#unauthorized-access-to-the-data-exchange-service-istg-des-authz-001).

### Privilege Escalation (ISTG-FW[INST]-AUTHZ-002)

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

Depending on the specific implementation of a given device, access to parts of the firmware or its functions might be restricted to individuals with a certain authorization access level, e.g., *AA-3* or *AA-4*. If the device firmware fails to correctly verify access permissions, an attacker with a lower authorization access level than intended might be able to get access to the restricted firmware parts.

**Test Objectives**

- Based on *ISTG-FW-AUTHZ-001*, it must be determined whether there is a way to elevate the given access privileges and thus to access restricted functions or parts of the firmware.

**Remediation**

Proper authorization checks need to be implemented, which ensure that access to restricted parts of the firmware is only possible for individuals with the required authorization access levels.

**References**

This test case is based on: [ISTG-DES-AUTHZ-002](../data_exchange_services/README.md#privilege-escalation-istg-des-authz-002).



## Information Gathering (ISTG-FW[INST]-INFO)

As mentioned above, during the dynamic analysis, it is also possible to test whether user data is securely stored on the device during runtime.

### Disclosure of User Data (ISTG-FW[INST]-INFO-001)

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

During runtime, a device is accumulating and processing data of different kinds, such as personal data of its users. If this data is not stored securely, an attacker might be able to recover it from the device.

**Test Objectives**

- It has to be checked whether user data can be accessed by unauthorized individuals.

**Remediation**

Access to user data should only be granted to individuals and processes that need to have access to it. No unauthorized or not properly authorized individual should be able to recover user data.

**References**

For this test case, data from the following sources was consolidated:

* OWASP ["Firmware Security Testing Methodology"][owasp_fstm]
* ["IoT Penetration Testing Cookbook"][iot_penetration_testing_cookbook] by Aaron Guzman and Aditya Gupta
* ["The IoT Hacker's Handbook"][iot_hackers_handbook] by Aditya Gupta
* ["Practical IoT Hacking"][practical_iot_hacking] by Fotios Chantzis, Ioannis Stais, Paulino Calderon, Evangelos Deirmentzoglou, and Beau Woods
* Key aspects of testing of the T-Systems Multimedia Solutions GmbH



## Cryptography (ISTG-FW[INST]-CRYPT)

Many IoT devices need to implement cryptographic algorithms, e.g., to securely store sensitive data, for authentication purposes or to receive and verify encrypted data from other network nodes. Failing to implement secure, state of the art cryptography might lead to the exposure of sensitive data, device malfunctions or loss of control over the device.

### Insufficient Verification of the Bootloader Signature (ISTG-FW[INST]-CRYPT-001)

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

Verifying the digital signature of the bootloader is an important measure to detect manipulations of the bootloader, thus preventing the execution of manipulated firmware on a device.

**Test Objectives**

- It must be checked if the signature of the bootloader is properly verified by the device during the boot process.

**Remediation**

The device must properly verify the digital signature of a bootloader before it is executed. A bootloader without a valid signature should not be executed.



[owasp_fstm]: https://github.com/scriptingxss/owasp-fstm	"OWASP Firmware Security Testing Methodology"
[iot_penetration_testing_cookbook]: https://www.packtpub.com/product/iot-penetration-testing-cookbook/9781787280571	"IoT Penetration Testing Cookbook"
[iot_hackers_handbook]: https://link.springer.com/book/10.1007/978-1-4842-4300-8	"The IoT Hacker's Handbook"
[practical_iot_hacking]: https://nostarch.com/practical-iot-hacking	"Practical IoT Hacking"