# 3.1. Processing Units (IOT-PROC)

## Table of Contents
* [Overview](#overview)
* [Authorization (IOT-PROC-AUTHZ)](#authorization-iot-proc-authz)
  * [Unauthorized Access to the Processing Unit (IOT-PROC-AUTHZ-001)](#unauthorized-access-to-the-processing-unit-iot-proc-authz-001)
  * [Privilege Escalation (IOT-PROC-AUTHZ-002)](#privilege-escalation-iot-proc-authz-002)
* [Business Logic (IOT-PROC-LOGIC)](#business-logic-iot-proc-logic)
  * [Insecure Implementation of Instructions (IOT-PROC-LOGIC-001)](#insecure-implementation-of-instructions-iot-proc-logic-001)
* [Side-Channel Attacks (IOT-PROC-SIDEC)](#side-channel-attacks-iot-proc-sidec)
  * [Insufficient Protection Against Side-Channel Attacks (IOT-PROC-SIDEC-001)](#insufficient-protection-against-side-channel-attacks-iot-proc-sidec-001)




## Overview

This section includes test cases and categories for the component processing unit. A processing unit is a device-internal element that can only be accessed with *PA-4*. Establishing a direct connection to the processing unit might require specific hardware equipment (e.g., a debugging board, an oscilloscope or test probes). 

The following test case categories, relevant for processing units, were identified:

- **Authorization:** Focuses on vulnerabilities that allow to get unauthorized access to the processing unit or to elevate privileges in order to access restricted functionalities.

- **Business Logic:** Focuses on vulnerabilities in the design and implementation of instructions as well as the presence of undocumented, potentially vulnerable, instructions.

- **Side-channel Attacks:** Focuses on the resilience against side-channel attacks like timing and glitching attacks.



## Authorization (IOT-PROC-AUTHZ)

Depending on the access model for a given device, only certain individuals might be allowed to access a processing unit directly. Thus, proper authentication and authorization procedures need to be in place, which ensure that only authorized entities can get access.

### Unauthorized Access to the Processing Unit (IOT-PROC-AUTHZ-001)

**Required Access Levels**

<table width="100%">
	<tr valign="top">
		<th width="1%" align="left">Physical</th>
 <td><i>PA-4</i></td>
	</tr>
	<tr valign="top">
		<th align="left">Logical</th>
		<td><i>LA-1</i></td>
	</tr>
</table>

**Summary**

Depending on the specific implementation of a given device, access to a processing unit might be restricted to entities with a certain logical access level, e.g., *LA-2*, *LA-3* or *LA-4*. If the device fails to correctly verify access permissions, any attacker (*LA-1*) might be able to get access.

**Test Objectives**

- It must be checked if authorization checks for access to the processing unit are implemented.

- In case that authorization checks are in place, it must be determined whether there is a way to bypass them.

**Remediation**

Proper authorization checks need to be implemented, which ensure that access to the processing unit is only possible for authorized entities.

**References**

This test case is based on: [IOT-DES-AUTHZ-001](../data_exchange_services/README.md#unauthorized-access-to-the-data-exchange-service-iot-des-authz-001).

### Privilege Escalation (IOT-PROC-AUTHZ-002)

**Required Access Levels**

<table width="100%">
	<tr valign="top">
		<th width="1%" align="left">Physical</th>
		<td><i>PA-4</i></td>
	</tr>
	<tr valign="top">
		<th align="left">Logical</th>
		<td><i>LA-2</i> - <i>LA-3</i><br>(depending on the access model for the given device)</td>
	</tr>
</table>

**Summary**

Depending on the specific implementation of a given device, access to some functionalities of a processing unit might be restricted to individuals with a certain logical access level, e.g., *LA-3* or *LA-4*. If the processing unit fails to correctly verify access permissions, an attacker with a lower logical access level than intended might be able to get access to the restricted functionalities.

**Test Objectives**

- Based on [IOT-PROC-AUTHZ-001](#unauthorized-access-to-the-processing-unit-iot-proc-authz-001), it must be determined whether there is a way to elevate the given access privileges and thus to access restricted functionalities.

**Remediation**

Proper authorization checks need to be implemented, which ensure that access to restricted functionalities is only possible for individuals with the required logical access levels.

**References**

This test case is based on: [IOT-DES-AUTHZ-002](../data_exchange_services/README.md#privilege-escalation-iot-des-authz-002).



## Business Logic (IOT-PROC-LOGIC)

Issues in the underlying logic of a processing unit might render the device vulnerable to attacks. Thus, it must be verified if the processing unit and its functionalities are working as intended and if exceptions are detected and properly handled.

### Insecure Implementation of Instructions (IOT-PROC-LOGIC-001)

**Required Access Levels**

<table width="100%">
	<tr valign="top">
		<th width="1%" align="left">Physical</th>
		<td><i>PA-4</i></td>
	</tr>
	<tr valign="top">
		<th align="left">Logical</th>
		<td><i>LA-1</i> - <i>LA-4</i><br>(depending on what level of privileges is required to successfully submit instructions to the processing unit)</td>
	</tr>
</table>
**Summary**

Flaws in the implementation of the business logic might result in unintended behavior or malfunctions of the device. For example, if an attacker intentionally tries to skip or change important instructions in the processing workflow, the device might end up in an unknown, potentially insecure state.

**Test Objectives**

- Based on the specific implementation, it has to be determined whether instructions can be misused to manipulate the behavior of the device.

- It must be checked if the processing unit in use supports undocumented, potentially vulnerable instructions. For example, this can be done by fuzzing instructions or performing research regarding the processing unit model.

**Remediation**

The device should not end up in an unknown state. Anomalies in the workflow must be detected and exceptions have to be handled properly.

**References**

This test case is based on: [IOT-DES-LOGIC-001](../data_exchange_services/README.md#circumvention-of-the-intended-business-logic-iot-des-logic-001).



## Side-Channel Attacks (IOT-PROC-SIDEC)

Side-channel attacks, such as timing and glitching attacks, are usually targeted against the physical implementation of a device or more specifically a processing unit instead of the device firmware or its interfaces. The goal of such attacks is to gather information about cryptographic algorithms and operations, performed by a processing unit, in order to retrieve key material, manipulate the cryptographic calculations or gain access to protected information.

### Insufficient Protection Against Side-Channel Attacks (IOT-PROC-SIDEC-001)

**Required Access Levels**

<table width="100%">
	<tr valign="top">
		<th width="1%" align="left">Physical</th>
		<td><i>PA-4</i></td>
	</tr>
	<tr valign="top">
		<th align="left">Logical</th>
		<td><i>LA-1</i> - <i>LA-4</i><br>(depending on how the attack is being performed; see summary for more details)</td>
	</tr>
</table>
**Summary**

As mentioned above, side-channel attacks can be used by an attacker to get access to sensitive data or to manipulate the device operation. Usually, side-channel attacks are customized attacks tailored to a specific hardware implementation.

Depending on how the attack is being performed, different levels of logical access might be required. Some side-channel attacks, such as glitching attacks, do not require logical access at all since the attack is performed on a physical level by manipulating the power supply. Other side-channel attack vectors, such as the Meltdown vulnerability, require the execution of code by an attacker. Thus, some kind of logical access is necessary.

**Test Objectives**

- It has to be determined whether the processing unit is affected by known vulnerabilities, such as Meltdown and Spectre.

- During the testing period, the behavior of the processing unit has to be analyzed in order to assess the probability of successful side-channel attacks like timing or glitching attacks.

**Remediation**

Based on the results of the analysis, the hardware design should be adjusted to be resilient against side-channel attacks. Furthermore, if publicly known vulnerabilities exist, the latest patches should be installed.

**References**

For this test case, data from the following sources was consolidated:

* ["A practical implementation of the timing attack"][timing_attack] by Jean-François Dhem, François Koeune, Philippe-Alexandre Leroux, Patrick Mestré, Jean-Jacques Quisquater, and Jean-Louis Willems *(In Jean-Jacques Quisquater and Bruce Schneier, editors, Smart Card Research and Applications, pages 167 - 182, Berlin, Heidelberg, 2000. Springer Berlin Heidelberg.)*
* ["Injecting Power Attacks with Voltage Glitching and Generation of Clock Attacks for Testing Fault Injection Attacks"][power_glitching_attack] by Shaminder Kaur, Balwinder Singh, Harsimranjit Kaur, and Lipika Gupta *(In Pradeep Kumar Singh, Arti Noor, Maheshkumar H. Kolekar, Sudeep Tanwar, Raj K. Bhatnagar, and Shaweta Khanna, editors, Evolving Technologies for Computing, Communication and Smart World, pages 23 - 37, Singapore, 2021. Springer Singapore.)*
* ["Spectre attacks: Exploiting speculative execution"][spectre_attack] by Paul Kocher, Jann Horn, Anders Fogh, Daniel Genkin, Daniel Gruss, Werner Haas, Mike Hamburg, Moritz Lipp, Stefan Mangard, Thomas Prescher, Michael Schwarz, and Yuval Yarom *(In 40th IEEE Symposium on Security and Privacy (S&P'19), 2019.)*
* ["Meltdown: Reading kernel memory from user space"][meltdown_attack] Moritz Lipp, Michael Schwarz, Daniel Gruss, Thomas Prescher, Werner Haas, Anders Fogh, Jann Horn, Stefan Mangard, Paul Kocher, Daniel Genkin, Yuval Yarom, and Mike Hamburg *(In 27th USENIX Security Symposium (USENIX Security 18), 2018.)*



[timing_attack]: https://link.springer.com/chapter/10.1007/10721064_15	"A practical implementation of the timing attack"
[power_glitching_attack]: https://link.springer.com/chapter/10.1007/978-981-15-7804-5_3	"Injecting Power Attacks with Voltage Glitching and Generation of Clock Attacks for Testing Fault Injection Attacks"
[spectre_attack]: https://ieeexplore.ieee.org/document/8835233	"Spectre attacks: Exploiting speculative execution"
[meltdown_attack]: https://www.usenix.org/conference/usenixsecurity18/presentation/lipp	"Meltdown: Reading kernel memory from user"
