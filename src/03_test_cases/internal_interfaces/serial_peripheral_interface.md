# 3.5.2. Serial Peripheral Interface (ISTG-INT[SPI])

## Table of Contents

- [Overview](#overview)
- [Authorization (ISTG-INT[SPI]-AUTHZ)](#authorization-istg-intspi-authz)
	- [Bus Interaction with Unauthorized Devices (ISTG-INT[SPI]-AUTHZ-001)](#bus-interaction-with-unauthorized-devicesintspi-authz-001)
- [Information Gathering (ISTG-INT[SPI]-INFO)](#information-gathering-istg-intspi-info)
	- [Packet Sniffing (ISTG-INT[SPI]-INFO-001)](#packet-sniffing-intspi-info-001)
- [Input Validation (ISTG-INT[SPI]-INPV)](#input-validation-intspi-inpv)
	- [Insufficient Handling of Invalid Data (ISTG-INT[SPI]-INPV-001)](#insufficient-handling-of-invalid-data-intspi-inpv-001)

## Overview

The Serial Peripheral Interface (SPI) is a serial communication bus primarily designed for the short-wire data transfer between integrated circuits. SPI has a master-slave architecture and operates with four logic signals. One for the serial clock (SCLK), one as chip select (CS) for the target receiver chip, and the last two for receiving and transmitting data. Especially, the two separated lines transmitting and receiving data enable the SPI bus to operate in full duplex mode.

SPI does not offer security features like authentication or encryption by default. Therefore, a higher-level protocol should be used on top to enable secure communication.

This specialization module aims to provide a structured approach for testing the security of SPI interfaces in IoT devices by adding specific test cases relevant to SPI. Some categories from the parent guide, like Business Logic, Cryptography, or Secrets, are not applicable to SPI due to its nature as a low-level communication protocol.

The following categories are not inherited by the specialization ISTG-INT[SPI]:

- **Configuration and Patch Management ([ISTG-INT-CONF](./README.md#configuration-and-patch-management-istg-int-conf))**: This category focuses on the configuration and patch management aspects of internal interfaces. Since this specialization focuses on a the communication protocol SPI rather than high level software/applications, the respective test cases are not applicable.
- **Secrets ([ISTG-INT-SCRT](./README.md#secrets-istg-int-scrt))**: This category focuses on the accessibility of secrets via an internal interface. Since the SPI data bus may be used to transmit secrets, this is already covered by the communication sniffing test case (ISTG-INT[SPI]-INFO-002).
- **Cryptography ([ISTG-INT-CRYPT](./README.md#cryptography-istg-int-crypt))**: This category focuses on the use of strong encryption algorithms. As SPI is a low level protocol that does not offer encryption by default, these test cases are not applicable.
- **Business Logic ([ISTG-INT-LOGIC](./README.md#business-logic-istg-int-logic))**: This category focuses on the circumvention of the intended business logic that might result in unintended behavior or malfunctions of the device. As SPI is a communication protocol rather than a high level software/application, traditional business logic test cases are not applicable. However, testing for unintended behavior is covered by the input validation test case [ISTG-INT[SPI]-INPV-001](#insufficient-handling-of-invalid-data-istg-intspi-inpv-001).

## Authorization (ISTG-INT[SPI]-AUTHZ)

Authorization in the context of SPI communication focuses on ensuring that only authorized devices or users can interact via the SPI bus, and unauthorized access is prevented. Since SPI typically lacks an authentication mechanism, it is critical to evaluate how Access is controlled.  

### Bus Interaction with Unauthorized Devices (ISTG-INT[SPI]-AUTHZ-001)  

**Required Access Levels**

<table width="100%">
	<tr valign="top">
		<th width="1%" align="left">Physical</th>
 <td><i>PA-3 - PA-4</i>
(depending on whether an SPI interface is accessible non-invasively somewhere on the device)</td>
	</tr>
	<tr valign="top">
		<th align="left">Authorization</th>
		<td><i>AA-1</i></td>
	</tr>
</table>

**Summary**

The SPI communication bus usually supports only one master and multiple slaves. However, there are systems that also support multiple masters via SPI, where one master acts as the active, primary master and the other as the inactive secondary master. In IoT hardware, different components on a circuit board (PCB) can communicate with each other over the SPI bus to exchange data and perform tasks. When assessing the system, it's important not only to monitor the communication, but also to actively interact with it. This can be done by acting as an additional master on the bus, for example, to engage with the slaves and control the communication.  

To minimize interference with other masters, these can be isolated by cutting the circuit traces. However, this typically requires invasive intervention (access level PA-4).

**Test Objectives**  

- The master and slave components on the IoT device must be identified.  
- Information about the messages and actions supported by those components must be collected (vendor datasheets).  
- In order to interact with the SPI components, devices and tools like a Raspberry Pi with spidev or Arduino with SPI.h should be used.  
- The reaction/response of the components must be analyzed. 

**Remediation**  

Proper checks need to be implemented to prevent unauthorized interaction with SPI components. As SPI does not feature authentication/authorization mechanisms by design, the bus and interfaces must be protected physically to be only accessible for authorized individuals.

## Information Gathering (ISTG-INT[SPI]-INFO)

The information-gathering section aims to identify the details of the SPI implementation, including available resources and the sniffing of data packets. This is crucial in understanding the attack surface.

### Packet Sniffing (ISTG-INT[SPI]-INFO-001)

**Required Access Levels**

<table width="100%">
	<tr valign="top">
		<th width="1%" align="left">Physical</th>
 <td><i>PA-3 - PA-4</i><br>(depending on whether an SPI interface is accessible non-invasively somewhere on the device)</td>
	</tr>
	<tr valign="top">
		<th align="left">Authorization</th>
		<td><i>AA-1</i></td>
	</tr>
</table>

**Summary**

SPI uses a four wire serial interface. One wire is the Serial Clock (SCLK), one is the Chip Selection (CS). The other two wires are for the data transfer from the master to the slave (MOSI) and vice versa (MISO). The communication between different components can be sniffed by connecting a data analyzer to the SCLK, MISO and MOSI lines. SPI is often used by onboard storage components, such as EEPROMs. It is possible that sensitive information will be exchanged between PCB components on the data bus.

**Test Objectives**

- The SCLK, CS, MOSI and MISO pins/wires on the target device must be identified.
- A logic analyzer must be connected to the SPI pins and the capture settings (e.g., sampling rate, threshold voltage, etc.) have to be configured accordingly.
- The SPI communication of the target device must be captured and analyzed in different states (e.g., startup, normal operation).

**Remediation**

The transmission of sensitive data should be reduced to the minimum which is required for operating the device. As SPI does not feature protective measures by design, the bus and interfaces must be secured physically to be only accessible for authorized individuals.

**References**

- [Saleae Logic Analyzer](https://saleae.com/logic)
- [sigrok Signal Analysis Software](https://sigrok.org/wiki/Main_Page)
- [Understanding the SPI Bus - Texas Instruments](https://www.ti.com/lit/ab/sboa621/sboa621.pdf?ts=1773992941308&ref_url=https%253A%252F%252Fwww.ti.com%252Fsitesearch%252Fen-us%252Fdocs%252Funiversalsearch.tsp%253FlangPref%253Den-US%2526nr%253D104250%2526searchTerm%253DSPI)
- [Arduino & Serial Peripheral Interface (SPI) - Arduino Documentation](https://docs.arduino.cc/learn/communication/spi/) 
- [PyFtdi — PyFtdi documentation](https://eblot.github.io/pyftdi/) 
## Input Validation (ISTG-INT[SPI]-INPV)

Input validation is critical to ensure that only valid, expected, and safe data is accepted by the SPI components. Malformed input or invalid commands could potentially compromise the device's security or stability.

### Insufficient Handling of Invalid Data (ISTG-INT[SPI]-INPV-001)

**Required Access Levels**

<table width="100%">
	<tr valign="top">
		<th width="1%" align="left">Physical</th>
 <td><i>PA-3 - PA-4</i>
(depending on whether an SPI interface is accessible non-invasively somewhere on the device)</td>
	</tr>
	<tr valign="top">
		<th align="left">Authorization</th>
		<td><i>AA-1</i></td>
	</tr>
</table>

**Summary**

SPI uses a master-slave architecture where the master generates a clock signal and initializes the communication with slaves via the chip select line. If any of the components does not properly validate the received data or commands, an attacker might be able to manipulate the device's behavior or render it unavailable.

**Test Objectives**

- The SCLK, CS, MOSI and MISO pins/wires on the target device must be identified.
- A separate device (e.g., an Arduino or an FTDI chip) must be connected to the SPI bus for sending malformed data.
- An appropriate software library should be used to craft and send malformed data or invalid commands to SPI slave components.

**Remediation**

The SPI components should reject and not further process invalid data or commands, as they could harm the device's integrity and availability. Proper error handling should prevent the system from crashing or behaving unexpectedly.

**References**

- [Understanding the SPI Bus - Texas Instruments](https://www.ti.com/lit/ab/sboa621/sboa621.pdf?ts=1773992941308&ref_url=https%253A%252F%252Fwww.ti.com%252Fsitesearch%252Fen-us%252Fdocs%252Funiversalsearch.tsp%253FlangPref%253Den-US%2526nr%253D104250%2526searchTerm%253DSPI)
- [Arduino & Serial Peripheral Interface (SPI) - Arduino Documentation](https://docs.arduino.cc/learn/communication/spi/) 
- [PyFtdi — PyFtdi documentation](https://eblot.github.io/pyftdi/)
