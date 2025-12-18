# 3.5.1. Inter-Integrated Circuit (ISTG-INT[I2C])

## Table of Contents

- [Overview](#overview)
- [Authorization (ISTG-INT\[I2C\]-AUTHZ)](#authorization-istg-inti2c-authz)
	- [Bus Interaction with Unauthorized Devices (ISTG-INT\[I2C\]-AUTHZ-001)](#bus-interaction-with-unauthorized-devices-istg-inti2c-authz-001)
- [Information Gathering (ISTG-INT\[I2C\]-INFO)](#information-gathering-istg-inti2c-info)
	- [Slave Enumeration (ISTG-INT\[I2C\]-INFO-001)](#slave-enumeration-istg-inti2c-info-001)
	- [Communication Sniffing (ISTG-INT\[I2C\]-INFO-002)](#communication-sniffing-istg-inti2c-info-002)
- [Input Validation (ISTG-INT\[I2C\]-INPV)](#input-validation-istg-inti2c-inpv)
	- [Insufficient Handling of Invalid Data (ISTG-INT\[I2C\]-INPV-001)](#insufficient-handling-of-invalid-data-istg-inti2c-inpv-001)

## Overview

One specialization of the internal interface component is Inter-Integrated Circuit (I2C). I2C is a synchronous serial communication protocol widely used in embedded systems for connecting microcontrollers and peripherals. It has a master-slave architecture and data transmission/reception cannot be done simultaneously. It does not offer security features like authentication, authorization, or encryption by default. Therefore, a higher level protocol should be used on top of I2C to enable secure communication.

This specialization module aims to provide a structured approach for testing the security of I2C interfaces in IoT devices by adding specific test cases relevant to I2C. Some categories from the parent guide, like Business Logic, Cryptography, or Secrets, are not applicable to I2C due to its nature as a low-level communication protocol.

The following categories are not inherited by the specialization [ISTG-INT[I2C]](./inter_integrated_circuit.md):

- **Configuration and Patch Management ([ISTG-INT-CONF](./README.md#configuration-and-patch-management-istg-int-conf))**: This category focuses on the configuration and patch management aspects of internal interfaces. Since this specialization focuses on a the communication protocol I2C rather than high level software/applications, the respective test cases are not applicable.
- **Secrets ([ISTG-INT-SCRT](./README.md#secrets-istg-int-scrt))**: This category focuses on the accessibility of secrets via an internal interface. Since the I2C data bus may be used to transmit secrets, this is already covered by the communication sniffing test case [(ISTG-INT\[I2C\]-INFO-002)](#communication-sniffing-istg-inti2c-info-002).
- **Cryptography ([ISTG-INT-CRYPT](./README.md#cryptography-istg-int-crypt))**: This category focuses on the use of strong encryption algorithms. As I2C is a low level protocol that does not offer encryption by default, these test cases are not applicable.
- **Business Logic ([ISTG-INT-LOGIC](./README.md#business-logic-istg-int-logic))**: This category focuses on the circumvention of the intended business logic that might result in unintended behavior or malfunctions of the device. As I2C is a communication protocol that rather than a high level software/application, traditional business logic test cases are not applicable. However, testing for unintended behavior is covered by the input validation test case [ISTG-INT\[I2C\]-INPV-001](#insufficient-handling-of-invalid-data-istg-inti2c-inpv-001).

## Authorization (ISTG-INT[I2C]-AUTHZ)

Authorization in the context of I2C communication focuses on ensuring that only authorized devices or users can interact via the I2C bus, and unauthorized access is prevented. Since I2C typically lacks an authentication mechanism, it is critical to evaluate how access is controlled.

### Bus Interaction with Unauthorized Devices (ISTG-INT[I2C]-AUTHZ-001)

**Required Access Levels**

<table width="100%">
	<tr valign="top">
		<th width="1%" align="left">Physical</th>
 <td><i>PA-3</i> - <i>PA-4</i><br>(depending on whether an I2C interface is accessible non-invasively somewhere on the device)</td>
	</tr>
	<tr valign="top">
		<th align="left">Authorization</th>
		<td><i>AA-1</i></td>
	</tr>
</table>

**Summary**

The I2C communication bus supports multiple masters and multiple slaves. In IoT hardware, different components on a circuit board (PCB) can communicate with each other over the I2C bus to exchange data and perform tasks. When assessing the system, it's important not only to monitor the communication, but also to actively interact with it. This can be done by acting as an additional master on the bus, for example, to engage with the slaves and control the communication.

To minimize interference with other masters, these can be isolated by cutting the circuit traces. However, this typically requires invasive intervention (access level PA-4).

**Test Objectives**

- The master and slave components on the IoT device must be identified.
- Information about the messages and actions supported by those components must be collected (vendor datasheets).
- In order to interact with the I2C components, devices and tools like a Raspberry Pi with smbus2 or Arduino with Wire.h should be used.
- The reaction/response of the components must be analyzed.

**Remediation**

Proper checks need to be implemented to prevent unauthorized interaction with I2C components. As I2C does not feature authentication/authorization mechanisms by design, the bus and interfaces must be protected physically to be only accessible for authorized individuals.

**References**

- [Python smbus2 Library](https://pypi.org/project/smbus2/)
- [Arduino Wire.h Library](https://docs.arduino.cc/language-reference/en/functions/communication/wire/)

## Information Gathering (ISTG-INT[I2C]-INFO)

The information-gathering section aims to identify the details of the I2C implementation, including device addresses and available resources. This is crucial in understanding the attack surface.

### Slave Enumeration (ISTG-INT[I2C]-INFO-001)

**Required Access Levels**

<table width="100%">
	<tr valign="top">
		<th width="1%" align="left">Physical</th>
 <td><i>PA-3</i> - <i>PA-4</i><br>(depending on whether an I2C interface is accessible non-invasively somewhere on the device)</td>
	</tr>
	<tr valign="top">
		<th align="left">Authorization</th>
		<td><i>AA-1</i></td>
	</tr>
</table>

**Summary**

I2C uses a two wire serial interface. One wire is the Serial Clock (SCL), the other one is the Serial Data (SDA). The master generates the clock signal and starts the communication with the slave. The slave receives the clock signal on the SCL wire and communicates with the master it was addressed by.

Each I2C device has a unique I2C address within the local connection. The I2C reference design has a 7 bit address space, which is sometimes extended up to 10 bits. A 7 bit address space allows a range of 128 distinct addresses. However, 16 of those are reserved for special tasks (0x00-0x07 and 0x78-0x7F), leaving only 112 addresses for the enumeration.

The detection of slaves can also be achieved passively by sniffing the communication (see [(ISTG-INT\[I2C\]-INFO-002)](#communication-sniffing-istg-inti2c-info-002)).

**Test Objectives**

- The SCL and SDA pins/wires on the target device must be identified.
- A separate device (e.g., an Arduino) must be connected to the I2C data bus for scanning.
- A scanning tool should be used to detect I2C components and their addresses.

**Remediation**

While the discoverability of slave components is not considered a vulnerability, it helps understanding the design of the IoT device and preparing more targeted attacks.

**References**

- [I2C Wiring Basics](https://learn.adafruit.com/scanning-i2c-addresses/i2c-basics)
- [I2C Scanning Tool for Arduino](https://learn.adafruit.com/scanning-i2c-addresses/arduino)

### Communication Sniffing (ISTG-INT[I2C]-INFO-002)

**Required Access Levels**

<table width="100%">
	<tr valign="top">
		<th width="1%" align="left">Physical</th>
 <td><i>PA-3</i> - <i>PA-4</i><br>(depending on whether an I2C interface is accessible non-invasively somewhere on the device)</td>
	</tr>
	<tr valign="top">
		<th align="left">Authorization</th>
		<td><i>AA-1</i></td>
	</tr>
</table>

**Summary**

I2C uses a two wire serial interface. One wire is the Serial Clock (SCL), the other one is the Serial Data (SDA). The communication between different components can be sniffed by connecting a data analyzer to the SCL and SDA lines of the data bus. I2C is often used by onboard storage components, such as EEPROMs. It is possible that sensitive information will be exchanged between PCB components on the data bus.

**Test Objectives**

- The SCL and SDA pins/wires on the target device must be identified.
- A logic analyzer must be connected to the I2C data bus and the capture settings (e.g., sampling rate, threshold voltage, etc.) have to be configured accordingly.
- The I2C communication of the target device must be captured and analyzed in different states (e.g., startup, normal operation).

**Remediation**

The transmission of sensitive data should be reduced to the minimum which is required for operating the device. As I2C does not feature protective measures by design, the bus and interfaces must be secured physically to be only accessible for authorized individuals.

**References**

- [Saleae Logic Analyzer](https://saleae.com/logic)
- [sigrok Signal Analysis Software](https://sigrok.org/wiki/Main_Page)

## Input Validation (ISTG-INT[I2C]-INPV)

Input validation is critical to ensure that only valid, expected, and safe data is accepted by the I2C components. Malformed input or invalid commands could potentially compromise the device's security or stability.

### Insufficient Handling of Invalid Data (ISTG-INT[I2C]-INPV-001)

**Required Access Levels**

<table width="100%">
	<tr valign="top">
		<th width="1%" align="left">Physical</th>
 <td><i>PA-3</i> - <i>PA-4</i><br>(depending on whether an I2C interface is accessible non-invasively somewhere on the device)</td>
	</tr>
	<tr valign="top">
		<th align="left">Authorization</th>
		<td><i>AA-1</i></td>
	</tr>
</table>

**Summary**

I2C uses a master-slave architecture where the master generates a clock signal and initializes the communication with slaves. If any of the components does not properly validate the received data or commands, an attacker might be able to manipulate the device's behavior or render it unavailable.

**Test Objectives**

- The SCL and SDA pins/wires on the target device must be identified.
- A separate device (e.g., an Arduino) must be connected to the I2C data bus for sending malformed data.
- An appropriate software library should be used to craft and send malformed data or invalid commands to I2C slave components.

**Remediation**

The I2C components should reject and not further process invalid data or commands, as they could harm the device's integrity and availability. Proper error handling should prevent the system from crashing or behaving unexpectedly.

**References**

- [Understanding the I2C Bus - Texas Instruments](https://www.ti.com/lit/an/slva704/slva704.pdf)
- [Arduino Wire.h Library](https://docs.arduino.cc/language-reference/en/functions/communication/wire/)
