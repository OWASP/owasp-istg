# 3.5.1. Inter-Integrated Circuit (ISTG-INT[I2C])

## Table of Contents

- [Overview](#overview)
- [Authorization (ISTG-INT\[I2C\]-AUTHZ)](#authorization-istg-inti2c-authz)
	- [Bus Interaction with Unauthorized Devices (ISTG-INT\[I2C\]-AUTHZ-001)](#bus-interaction-with-unauthorized-devices-istg-inti2c-authz-001)
- [Information Gathering (ISTG-INT\[I2C\]-INFO)](#information-gathering-istg-inti2c-info)
	- [Slave Enumeration (ISTG-INT\[I2C\]-INFO-001)](#slave-enumeration-istg-inti2c-info-001)
	- [Communication Sniffing (ISTG-INT\[I2C\]-INFO-002)](#communication-sniffing-istg-inti2c-info-002)
	- [EEPROM/Memory Extraction (ISTG-INT\[I2C\]-INFO-003)](#eeprommemory-extraction-istg-inti2c-info-003)
- [Input Validation (ISTG-INT\[I2C\]-INPV)](#input-validation-istg-inti2c-inpv)
	- [Insufficient Handling of Invalid Data (ISTG-INT\[I2C\]-INPV-001)](#insufficient-handling-of-invalid-data-istg-inti2c-inpv-001)

## Overview

One specialization of the internal interface component is Inter-Integrated Circuit (I2C). I2C is a synchronous serial communication protocol widely used in embedded systems for connecting microcontrollers and peripherals. It has a master-slave architecture and data transmission/reception cannot be done simultaneously. It does not offer security features like authentication, authorization, or encryption by default. Therefore, a higher level protocol should be used on top of I2C to enable secure communication.

This specialization module aims to provide a structured approach for testing the security of I2C interfaces in IoT devices by adding specific test cases relevant to I2C. Some categories from the parent guide, like Business Logic, Cryptography, or Secrets, are not applicable to I2C due to its nature as a low-level communication protocol.

The following categories are not inherited by the specialization [ISTG-INT[I2C]](./inter_integrated_circuit.md):

- **Configuration and Patch Management ([ISTG-INT-CONF](./README.md#configuration-and-patch-management-istg-int-conf))**: This category focuses on the configuration and patch management aspects of internal interfaces. Since this specialization focuses on the communication protocol I2C rather than high level software/applications, the respective test cases are not applicable.
- **Secrets ([ISTG-INT-SCRT](./README.md#secrets-istg-int-scrt))**: This category focuses on the accessibility of secrets via an internal interface. Since the I2C data bus may be used to transmit secrets and secrets may be stored in I2C-attached memory, this is already covered by the communication sniffing test case [(ISTG-INT\[I2C\]-INFO-002)](#communication-sniffing-istg-inti2c-info-002) and the EEPROM/memory extraction test case [(ISTG-INT\[I2C\]-INFO-003)](#eeprommemory-extraction-istg-inti2c-info-003).
- **Cryptography ([ISTG-INT-CRYPT](./README.md#cryptography-istg-int-crypt))**: This category focuses on the use of strong encryption algorithms. As I2C is a low level protocol that does not offer encryption by default, these test cases are not applicable.
- **Business Logic ([ISTG-INT-LOGIC](./README.md#business-logic-istg-int-logic))**: This category focuses on the circumvention of the intended business logic that might result in unintended behavior or malfunctions of the device. As I2C is a communication protocol rather than a high level software/application, traditional business logic test cases are not applicable. However, testing for unintended behavior is covered by the input validation test case [ISTG-INT\[I2C\]-INPV-001](#insufficient-handling-of-invalid-data-istg-inti2c-inpv-001).

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
- In order to interact with the I2C components, a dedicated hardware tool (e.g., Bus Pirate, HydraBus) or a microcontroller (e.g., Raspberry Pi with smbus2, Arduino with Wire.h) should be used.
- The reaction/response of the components must be analyzed.

**Remediation**

Proper checks need to be implemented to prevent unauthorized interaction with I2C components. As I2C does not feature authentication/authorization mechanisms by design, the bus and interfaces must be protected physically to be only accessible for authorized individuals.

**References**

For this test case, data from the following sources was consolidated:

* ["IoT Pentesting Guide"][iot_pentesting_guide] by Aditya Gupta
* ["IoT Penetration Testing Cookbook"][iot_penetration_testing_cookbook] by Aaron Guzman and Aditya Gupta
* ["The IoT Hacker's Handbook"][iot_hackers_handbook] by Aditya Gupta
* ["Practical IoT Hacking"][practical_iot_hacking] by Fotios Chantzis, Ioannis Stais, Paulino Calderon, Evangelos Deirmentzoglou, and Beau Woods
* Key aspects of testing of the T-Systems Multimedia Solutions GmbH

- [Python smbus2 Library](https://pypi.org/project/smbus2/)
- [Arduino Wire.h Library](https://docs.arduino.cc/language-reference/en/functions/communication/wire/)
- [Bus Pirate I2C Guide](http://dangerousprototypes.com/docs/I2C)
- [HydraBus Open-Source Hardware Tool](https://hydrabus.com)

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
- A separate device (e.g., an Arduino, Bus Pirate, or HydraBus) or a Linux host with i2c-tools must be connected to the I2C data bus for scanning.
- A scanning tool (e.g., `i2cdetect -r` from the i2c-tools package) should be used to probe all 112 non-reserved addresses using read probes, which avoids accidental write transactions that could disturb or corrupt sensitive devices (e.g., EEPROMs, DACs) on the bus. The default write-probe mode (`i2cdetect` without `-r`) must only be used when the device types present on the bus are already known.
- The general call address (0x00) should also be probed, as it broadcasts to all slaves and may expose devices that do not respond to normal address enumeration.
- Identified device addresses should be cross-referenced against datasheets to determine the component type and supported register map.

**Remediation**

While the discoverability of slave components is not considered a vulnerability, it helps understanding the design of the IoT device and preparing more targeted attacks.

**References**

For this test case, data from the following sources was consolidated:

* ["IoT Pentesting Guide"][iot_pentesting_guide] by Aditya Gupta
* ["IoT Penetration Testing Cookbook"][iot_penetration_testing_cookbook] by Aaron Guzman and Aditya Gupta
* ["The IoT Hacker's Handbook"][iot_hackers_handbook] by Aditya Gupta
* ["Practical IoT Hacking"][practical_iot_hacking] by Fotios Chantzis, Ioannis Stais, Paulino Calderon, Evangelos Deirmentzoglou, and Beau Woods
* Key aspects of testing of the T-Systems Multimedia Solutions GmbH

- [I2C Wiring Basics](https://learn.adafruit.com/scanning-i2c-addresses/i2c-basics)
- [I2C Scanning Tool for Arduino](https://learn.adafruit.com/scanning-i2c-addresses/arduino)
- [i2c-tools Package](https://i2c.wiki.kernel.org/index.php/I2C_Tools)

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
- A logic analyzer or dedicated hardware tool (e.g., Bus Pirate in I2C sniffer mode, HydraBus, Saleae) must be connected to the I2C data bus and the capture settings (e.g., sampling rate, threshold voltage) have to be configured accordingly.
- The I2C communication of the target device must be captured and analyzed in different states (e.g., startup, normal operation, firmware update).
- Captured traffic must be inspected for sensitive data, including keys, credentials, or configuration parameters.

**Remediation**

The transmission of sensitive data should be reduced to the minimum which is required for operating the device. As I2C does not feature protective measures by design, the bus and interfaces must be secured physically to be only accessible for authorized individuals.

**References**

For this test case, data from the following sources was consolidated:

* ["IoT Pentesting Guide"][iot_pentesting_guide] by Aditya Gupta
* ["IoT Penetration Testing Cookbook"][iot_penetration_testing_cookbook] by Aaron Guzman and Aditya Gupta
* ["The IoT Hacker's Handbook"][iot_hackers_handbook] by Aditya Gupta
* ["Practical IoT Hacking"][practical_iot_hacking] by Fotios Chantzis, Ioannis Stais, Paulino Calderon, Evangelos Deirmentzoglou, and Beau Woods
* Key aspects of testing of the T-Systems Multimedia Solutions GmbH

- [Saleae Logic Analyzer](https://www.saleae.com)
- [sigrok Signal Analysis Software](https://sigrok.org/wiki/Main_Page)
- [Bus Pirate I2C Documentation](http://dangerousprototypes.com/docs/Bus_Pirate_I2C)

### EEPROM/Memory Extraction (ISTG-INT[I2C]-INFO-003)

**Required Access Levels**

<table width="100%">
	<tr valign="top">
		<th width="1%" align="left">Physical</th>
 <td><i>PA-3</i> - <i>PA-4</i><br>(depending on whether an I2C interface is accessible non-invasively somewhere on the device)</td>
	</tr>
	<tr valign="top">
		<th align="left">Authorization</th>
		<td><i>AA-1</i></td>
	</tr>
</table>

**Summary**

I2C is frequently used to connect EEPROMs and other non-volatile memory devices to a microcontroller. These memory chips often store sensitive data such as firmware, configuration parameters, cryptographic keys, or device credentials. Since the I2C bus provides no authentication or encryption by default, an attacker with physical access to the bus can directly read the contents of attached memory devices using standard tooling.

**Test Objectives**

- Based on [ISTG-INT\[I2C\]-INFO-001](#slave-enumeration-istg-inti2c-info-001), I2C devices at known EEPROM address ranges (e.g., 0x50-0x57 for 24Cxx series EEPROMs) must be identified.
- The contents of identified memory devices must be extracted using tools such as `i2cdump` (from the i2c-tools package) or a hardware tool (e.g., Bus Pirate, HydraBus). Note: `i2cdump` uses 8-bit internal addressing by default and will wrap at 256 bytes; for EEPROMs with 16-bit internal addressing (e.g., 24C256, 24C512), word-addressed mode (`i2cdump -y <bus> <addr> w`) or a scripted multi-page read must be used to obtain a complete dump.
- Extracted data must be analyzed for sensitive information, including firmware images, configuration files, cryptographic keys, and credentials.
- It must be determined whether the extracted data is stored in plaintext or is protected by encryption.
- If write access to the EEPROM is possible, the state of the write-protect (WP) pin must be verified. An improperly grounded WP pin allows an attacker to overwrite EEPROM contents, which may enable persistent compromise of device configuration or credentials.

**Remediation**

Sensitive data stored in EEPROM or other I2C-attached memory must be encrypted. Cryptographic keys and credentials should not be stored on devices accessible via an unprotected bus. Where possible, cryptographic memory modules with built-in access control (e.g., Microchip ATECC608) should be used instead of general-purpose EEPROMs.

**References**

For this test case, data from the following sources was consolidated:

* ["IoT Pentesting Guide"][iot_pentesting_guide] by Aditya Gupta
* ["IoT Penetration Testing Cookbook"][iot_penetration_testing_cookbook] by Aaron Guzman and Aditya Gupta
* ["The IoT Hacker's Handbook"][iot_hackers_handbook] by Aditya Gupta
* ["Practical IoT Hacking"][practical_iot_hacking] by Fotios Chantzis, Ioannis Stais, Paulino Calderon, Evangelos Deirmentzoglou, and Beau Woods
* Key aspects of testing of the T-Systems Multimedia Solutions GmbH

- [i2c-tools Package](https://i2c.wiki.kernel.org/index.php/I2C_Tools)
- [Bus Pirate I2C Documentation](http://dangerousprototypes.com/docs/Bus_Pirate_I2C)
- [HydraBus Open-Source Hardware Tool](https://hydrabus.com)



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
- A separate device (e.g., an Arduino, Bus Pirate, or HydraBus) must be connected to the I2C data bus for sending malformed data.
- An appropriate software library should be used to craft and send malformed data or invalid commands to I2C slave components. Examples of conditions to test include:
  - Out-of-range register addresses or command bytes not defined in the device datasheet.
  - Payloads that exceed the expected data length for a given register write.
  - NAK flooding: repeatedly sending START conditions without completing transactions.
  - Repeated START (Sr) condition abuse: chaining transactions without releasing the bus to detect improper bus state handling.
- Clock stretching behavior must be tested where applicable: a slave that holds SCL low indefinitely can stall the master and cause a denial-of-service condition. The master's timeout handling for clock stretching must be verified.
- The general call address (0x00) must be used to broadcast commands to all slaves simultaneously to test whether slaves respond unexpectedly to global resets or other general call commands.
- The reaction and recovery behavior of target components after receiving malformed input must be documented and assessed.

**Remediation**

The I2C components should reject and not further process invalid data or commands, as they could harm the device's integrity and availability. Proper error handling should prevent the system from crashing or behaving unexpectedly.

**References**

For this test case, data from the following sources was consolidated:

* ["IoT Pentesting Guide"][iot_pentesting_guide] by Aditya Gupta
* ["IoT Penetration Testing Cookbook"][iot_penetration_testing_cookbook] by Aaron Guzman and Aditya Gupta
* ["The IoT Hacker's Handbook"][iot_hackers_handbook] by Aditya Gupta
* ["Practical IoT Hacking"][practical_iot_hacking] by Fotios Chantzis, Ioannis Stais, Paulino Calderon, Evangelos Deirmentzoglou, and Beau Woods
* Key aspects of testing of the T-Systems Multimedia Solutions GmbH

- [Understanding the I2C Bus - Texas Instruments](https://www.ti.com/lit/an/slva704/slva704.pdf)
- [Arduino Wire.h Library](https://docs.arduino.cc/language-reference/en/functions/communication/wire/)



[iot_pentesting_guide]: https://www.iotpentestingguide.com	"IoT Pentesting Guide"
[iot_penetration_testing_cookbook]: https://www.packtpub.com/product/iot-penetration-testing-cookbook/9781787280571	"IoT Penetration Testing Cookbook"
[iot_hackers_handbook]: https://link.springer.com/book/10.1007/978-1-4842-4300-8	"The IoT Hacker's Handbook"
[practical_iot_hacking]: https://nostarch.com/practical-iot-hacking	"Practical IoT Hacking"
