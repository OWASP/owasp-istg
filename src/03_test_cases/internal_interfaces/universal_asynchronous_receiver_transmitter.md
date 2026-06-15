# 3.5.3. Universal Asynchronous Receiver-Transmitter (ISTG-INT[UART])

## Table of Contents

- [Overview](#overview)
- [Authorization (ISTG-INT\[UART\]-AUTHZ)](#authorization-istg-intuart-authz)
	- [Unauthenticated Access to Serial Console (ISTG-INT\[UART\]-AUTHZ-001)](#unauthenticated-access-to-serial-console-istg-intuart-authz-001)
	- [Bootloader Interrupt via Serial Console (ISTG-INT\[UART\]-AUTHZ-002)](#bootloader-interrupt-via-serial-console-istg-intuart-authz-002)
- [Information Gathering (ISTG-INT\[UART\]-INFO)](#information-gathering-istg-intuart-info)
	- [UART Interface and Baud Rate Identification (ISTG-INT\[UART\]-INFO-001)](#uart-interface-and-baud-rate-identification-istg-intuart-info-001)
	- [Disclosure of Sensitive Data in Serial Output (ISTG-INT\[UART\]-INFO-002)](#disclosure-of-sensitive-data-in-serial-output-istg-intuart-info-002)
- [Input Validation (ISTG-INT\[UART\]-INPV)](#input-validation-istg-intuart-inpv)
	- [Command Injection via Serial Interface (ISTG-INT\[UART\]-INPV-001)](#command-injection-via-serial-interface-istg-intuart-inpv-001)

## Overview

One specialization of the internal interface component is Universal Asynchronous Receiver-Transmitter (UART). UART is a serial communication protocol widely used in IoT devices for debug consoles, bootloader interaction, and inter-component communication. Unlike synchronous protocols such as I2C or SPI, UART operates asynchronously without a shared clock signal, using two lines — TX (transmit) and RX (receive) — along with a common GND reference.

UART interfaces are among the most commonly exposed debug surfaces on IoT hardware. They frequently provide direct access to a device's serial console or bootloader, often without any authentication. UART does not offer security features such as authentication, authorization, or encryption by design. Protections must therefore be implemented at the firmware or physical level.

Where UART test points or connector headers are externally accessible on the device enclosure without disassembly, physical access level *PA-3* may be sufficient. In most cases, however, access to internal UART pads requires opening the device, corresponding to *PA-4*. The applicable access level is noted per test case and must be assessed for each specific device under test.

This specialization module provides a structured approach for testing the security of UART interfaces in IoT devices. Some categories from the parent guide are not applicable to UART due to its nature as a low-level asynchronous communication protocol.

The following categories are not inherited by the specialization [ISTG-INT[UART]](./universal_asynchronous_receiver_transmitter.md):

- **Configuration and Patch Management ([ISTG-INT-CONF](./README.md#configuration-and-patch-management-istg-int-conf))**: This category focuses on the configuration and patch management of internal interface software. Since this specialization focuses on the UART communication protocol rather than high-level software or applications, the respective test cases are not applicable.
- **Secrets ([ISTG-INT-SCRT](./README.md#secrets-istg-int-scrt))**: This category focuses on the accessibility of secrets via an internal interface. Since sensitive data such as credentials, keys, and configuration parameters may be disclosed via UART serial output, this is already covered by the disclosure test case [(ISTG-INT\[UART\]-INFO-002)](#disclosure-of-sensitive-data-in-serial-output-istg-intuart-info-002).
- **Cryptography ([ISTG-INT-CRYPT](./README.md#cryptography-istg-int-crypt))**: This category focuses on the use of strong cryptographic algorithms. As UART is a low-level transport protocol that does not offer encryption by design, these test cases are not applicable.
- **Business Logic ([ISTG-INT-LOGIC](./README.md#business-logic-istg-int-logic))**: This category focuses on the circumvention of the intended business logic that might result in unintended behavior or malfunctions of the device. As UART is a communication protocol rather than a high-level application, traditional business logic test cases are not applicable. However, testing for unintended behavior resulting from malformed input is covered by [(ISTG-INT\[UART\]-INPV-001)](#command-injection-via-serial-interface-istg-intuart-inpv-001).

## Authorization (ISTG-INT[UART]-AUTHZ)

Authorization in the context of UART communication focuses on ensuring that access to the serial console and bootloader is restricted to authorized individuals. Since UART interfaces frequently expose privileged shells or bootloader prompts without any authentication, evaluating access controls is critical.

### Unauthenticated Access to Serial Console (ISTG-INT[UART]-AUTHZ-001)

**Required Access Levels**

<table width="100%">
	<tr valign="top">
		<th width="1%" align="left">Physical</th>
		<td><i>PA-3</i> - <i>PA-4</i><br>(depending on whether UART test points or headers are accessible without opening the device)</td>
	</tr>
	<tr valign="top">
		<th align="left">Authorization</th>
		<td><i>AA-1</i></td>
	</tr>
</table>

**Summary**

Many IoT devices expose a UART serial console that drops directly to a privileged shell — often root — without requiring any authentication. This allows any individual with physical access to the UART interface to gain full control of the operating system, read and modify the filesystem, extract credentials and keys, and install persistent backdoors. This is one of the most frequently encountered vulnerabilities in IoT hardware security assessments and continues to affect devices across consumer, industrial, and carrier-grade product categories. Recent examples include CVE-2025-53914 (unauthenticated root access via UART on Calix GigaCenter ONT devices) and CVE-2024-28326 (unauthenticated UART root access on the ASUS RT-N12 D1 router).

**Test Objectives**

- The UART TX, RX, and GND pins must be identified on the target device (see [ISTG-INT\[UART\]-INFO-001](#uart-interface-and-baud-rate-identification-istg-intuart-info-001)).
- A USB-UART adapter (e.g., based on FT232RL, CP2102, or CH340G) must be connected to the device at the identified baud rate. The adapter voltage must match the device's logic level (typically 3.3V for modern IoT devices).
- A serial terminal (e.g., minicom, screen, picocom) must be opened at the correct baud rate and settings (typically 8N1: 8 data bits, no parity, 1 stop bit).
- It must be determined whether the serial console provides a shell or login prompt upon device boot and during normal operation.
- Where relevant to the device boot flow, repeated interrupt inputs such as Ctrl+C or Ctrl+D during kernel initialization or early userspace startup must be assessed to determine whether they expose an unintended fallback shell, recovery console, debug prompt, or other unauthenticated state.
- If a login prompt is present, it must be assessed whether it can be bypassed (e.g., via bootloader access, single-user mode, or kernel parameter modification).
- The privilege level of any accessible shell must be documented.

**Remediation**

Serial console access must require authentication in production firmware. If a console is required for manufacturing or support purposes, strong authentication must be enforced and access must be logged. Where no operational requirement exists, the UART console should be disabled in production firmware (e.g., by redirecting the kernel console to `/dev/null` and removing interactive shell spawning from init). Physical removal or depopulation of UART headers and test point pads prior to shipping provides the strongest protection.

**References**

- [minicom Serial Terminal](https://salsa.debian.org/minicom-team/minicom)
- [picocom Minimal Serial Terminal](https://github.com/npat-efault/picocom)
- [FT232RL USB-UART Adapter - FTDI](https://ftdichip.com/products/ft232rl/)
- [CP2102 USB-UART Bridge - Silicon Labs](https://www.silabs.com/interface/usb-bridges/classic/device.cp2102)
- [CVE-2025-53914 - Calix GigaCenter ONT Unauthenticated UART Root Access](https://www.cve.org/CVERecord?id=CVE-2025-53914)
- [CVE-2024-28326 - ASUS RT-N12 D1 Unauthenticated UART Root Access](https://www.cvedetails.com/cve/CVE-2024-28326/)
- OWASP [IoT Security Verification Standard (ISVS)](https://owasp.org/IoT-Security-Verification-Standard-ISVS/) — Related requirements: V2.2.4: "Verify that device debug capabilities can only be accessed by approved staff (e.g. support and engineering teams) and verify that access is monitored or logged"

### Bootloader Interrupt via Serial Console (ISTG-INT[UART]-AUTHZ-002)

**Required Access Levels**

<table width="100%">
	<tr valign="top">
		<th width="1%" align="left">Physical</th>
		<td><i>PA-3</i> - <i>PA-4</i><br>(depending on whether UART test points or headers are accessible without opening the device)</td>
	</tr>
	<tr valign="top">
		<th align="left">Authorization</th>
		<td><i>AA-1</i></td>
	</tr>
</table>

**Summary**

Many IoT devices use bootloaders such as U-Boot that can be interrupted via the UART serial console during the boot sequence. If no interrupt protection is in place, an attacker can halt the boot process and access the bootloader prompt within the first few seconds of power-on. From the bootloader prompt, an attacker can enumerate flash layout and environment variables, modify kernel boot arguments, load and execute arbitrary code, and dump or overwrite flash memory — effectively bypassing all operating system-level access controls. Recent examples include CVE-2023-48426 (U-Boot shell accessible via UART interrupt on Chromecast devices, CVSS 10.0), CVE-2024-22013 (U-Boot environment read from an unauthenticated partition), and CVE-2023-39902 (unauthenticated code execution via a crafted FIT image in the U-Boot Secondary Program Loader).

**Test Objectives**

- Based on [ISTG-INT\[UART\]-AUTHZ-001](#unauthenticated-access-to-serial-console-istg-intuart-authz-001), a serial terminal must be connected and monitoring output before device power-on.
- During the boot sequence, interrupt signals must be sent (commonly Ctrl+C, spacebar, or a device-specific key combination) within the bootloader's autoboot window to attempt to halt the boot process.
- If a bootloader prompt is obtained, the following must be assessed:
  - Environment variables must be inspected (e.g., `printenv` in U-Boot) for sensitive data including credentials, boot commands, and partition layouts.
  - Whether boot arguments can be modified to alter the operating system's security posture (e.g., appending `init=/bin/sh` to the kernel command line).
  - Whether arbitrary code can be loaded and executed (e.g., via `fatload` and `go` commands in U-Boot).
  - Whether flash memory can be read or written directly (e.g., via `md`, `mw`, `nand read`, or `sf read` commands).
  - Whether UART-based firmware loading commands are available (e.g., `loady` for Y-Modem or `loadx` for X-Modem in U-Boot), which would allow an attacker to load and execute arbitrary firmware images over the serial interface.
- It must be determined whether the bootloader requires authentication to access its prompt or execute privileged commands.

**Remediation**

The bootloader autoboot delay should be set to zero (`CONFIG_BOOTDELAY=0` in U-Boot) to eliminate the interrupt window in production builds. If bootloader access is required for manufacturing, password authentication should be enforced using `CONFIG_AUTOBOOT_KEYED_CTRLC` or HMAC-based protection via `CONFIG_AUTOBOOT_ENCRYPTION` (U-Boot v2023+). Dangerous commands such as `md`, `mw`, `go`, `loady`, and `loadx` should be removed from production bootloader builds to prevent arbitrary code and firmware loading. Verified boot must be enabled using `CONFIG_FIT_SIGNATURE` to cryptographically verify FIT images before execution, preventing unsigned firmware from being loaded via the bootloader. Secure boot should additionally be implemented at the SoC level to verify the bootloader itself before execution.

**References**

- [U-Boot Documentation](https://docs.u-boot.org/en/latest/)
- [U-Boot CONFIG_BOOTDELAY and Autoboot Security](https://docs.u-boot.org/en/latest/usage/cmd/autoboot.html)
- [CVE-2023-48426 - U-Boot Shell Accessible via UART Interrupt (CVSS 10.0)](https://www.tenable.com/cve/CVE-2023-48426)
- [CVE-2024-22013 - U-Boot Environment Read from Unauthenticated Partition](https://github.com/advisories/GHSA-7j8v-7qw4-w29q)
- [CVE-2023-39902 - U-Boot SPL Unauthenticated Code Execution via FIT Image](https://community.nxp.com/t5/i-MX-Security/U-Boot-Secondary-Program-Loader-Authentication-Vulnerability-CVE/ta-p/1736196)
- OWASP [IoT Security Verification Standard (ISVS)](https://owasp.org/IoT-Security-Verification-Standard-ISVS/) — Related requirements: V2.2.4: "Verify that device debug capabilities can only be accessed by approved staff and verify that access is monitored or logged"; V3.1.3: "Verify that communication interfaces such as USB, UART, and other variants are disabled or adequately protected during every stage of the device's boot process"; V5.1.1: "Verify that the platform supports disabling or protecting access to debugging interfaces (e.g. JTAG, SWD, UART etc.)"

## Information Gathering (ISTG-INT[UART]-INFO)

The information-gathering section aims to identify the UART interface parameters and assess what data is disclosed via the serial interface. This is a prerequisite for all subsequent UART test cases and provides critical intelligence about the device's software stack and potential attack surface.

### UART Interface and Baud Rate Identification (ISTG-INT[UART]-INFO-001)

**Required Access Levels**

<table width="100%">
	<tr valign="top">
		<th width="1%" align="left">Physical</th>
		<td><i>PA-3</i> - <i>PA-4</i><br>(depending on whether UART test points or headers are accessible without opening the device)</td>
	</tr>
	<tr valign="top">
		<th align="left">Authorization</th>
		<td><i>AA-1</i></td>
	</tr>
</table>

**Summary**

Before interacting with a UART interface, the physical pin locations and communication parameters must be identified. UART interfaces on IoT devices are commonly exposed as through-hole headers, surface-mount test points, or unpopulated pads on the PCB. The TX line can be identified by its idle-high state (held at VCC — typically 3.3V on modern IoT devices — when no data is being transmitted). The baud rate must be determined to decode serial output correctly; connecting at the wrong baud rate produces garbled output.

**Test Objectives**

- The PCB must be inspected for UART indicators including silkscreen labels (TX, RX, GND, UART, J1, CON1), unpopulated header pads, or test points near the main SoC or processor.
- A multimeter must be used to identify the GND pin (continuity to device ground plane) and any VCC pin (static DC voltage). The TX pin can be identified by its idle-high voltage (approximately 3.3V or 5V) relative to GND.
- An oscilloscope or logic analyzer should be used to confirm UART activity on suspected TX pins by observing digital transitions during device boot.
- The baud rate must be determined using one of the following methods:
  - **Automated**: JTAGulator or a logic analyzer with protocol auto-detection (e.g., sigrok/Pulseview).
  - **Semi-automated**: baudrate.py connected to a logic capture device.
  - **Manual**: Measuring the duration of the shortest pulse on the TX line with an oscilloscope; the baud rate equals the reciprocal of the bit period (e.g., 8.68 µs per bit = 115200 baud).
- Common baud rates to test if automated detection is unavailable: 115200, 57600, 38400, 19200, 9600.
- The logic voltage level of the UART interface must be confirmed (3.3V or 5V) before connecting a USB-UART adapter to avoid damaging the device.

**Remediation**

While the identification of UART interface parameters is not a vulnerability in itself, it is a prerequisite for further attacks. Manufacturers should depopulate UART headers and test point pads in production hardware and avoid silkscreen labeling that identifies debug interfaces. These measures increase the effort required for an attacker to locate and connect to the interface.

**References**

- [JTAGulator - Automated UART and JTAG Detection](https://www.grandideastudio.com/portfolio/jtagulator/)
- [baudrate.py - Baud Rate Detection Tool](https://github.com/devttys0/baudrate)
- [sigrok/PulseView Logic Analyzer Software](https://sigrok.org/wiki/PulseView)
- [HydraBus UART Mode](https://github.com/hydrabus/hydrafw/wiki/HydraFW-UART-guide)
- [Bus Pirate UART Documentation](https://buspirate.com/bus-pirate-uart/)
- OWASP [IoT Security Verification Standard (ISVS)](https://owasp.org/IoT-Security-Verification-Standard-ISVS/) — Related requirements: V5.1.1: "Verify that the platform supports disabling or protecting access to debugging interfaces (e.g. JTAG, SWD, UART etc.)"

### Disclosure of Sensitive Data in Serial Output (ISTG-INT[UART]-INFO-002)

**Required Access Levels**

<table width="100%">
	<tr valign="top">
		<th width="1%" align="left">Physical</th>
		<td><i>PA-3</i> - <i>PA-4</i><br>(depending on whether UART test points or headers are accessible without opening the device)</td>
	</tr>
	<tr valign="top">
		<th align="left">Authorization</th>
		<td><i>AA-1</i></td>
	</tr>
</table>

**Summary**

IoT devices commonly output diagnostic and debug information over the UART serial interface during boot and normal operation. This output frequently contains sensitive data that should not be accessible in production devices, including firmware version strings and build timestamps (enabling targeted exploitation of known vulnerabilities), credentials and API keys, cryptographic key material, MAC addresses and internal network configuration, memory addresses and kernel symbols (facilitating memory corruption exploitation), and filesystem paths.

**Test Objectives**

- Based on [ISTG-INT\[UART\]-INFO-001](#uart-interface-and-baud-rate-identification-istg-intuart-info-001), a serial terminal must be connected and capturing output before device power-on.
- The full boot sequence output must be captured and inspected for sensitive data including:
  - Firmware version strings, build dates, and compiler information.
  - Bootloader environment variables printed during boot.
  - Kernel messages referencing memory addresses, loaded modules, or mount points.
  - Credentials, API tokens, or cryptographic key material printed in plaintext.
  - MAC addresses, IP addresses, or network interface configuration.
  - WiFi SSIDs, passwords, or provisioning data.
- Serial output must also be captured during normal device operation and across different device states (e.g., during network activity, firmware update, error conditions) to identify runtime data disclosure.
- The sensitivity and exploitability of any disclosed data must be assessed.

**Remediation**

Serial output in production firmware must be reduced to the minimum required for device operation. Debug and verbose logging levels must be disabled at compile time for production builds. Credentials, keys, and sensitive configuration data must never be printed to any interface including the serial console. Firmware version information, if required for diagnostics, should not be printed in a format that directly maps to known vulnerability databases.

**References**

- [minicom Serial Terminal](https://salsa.debian.org/minicom-team/minicom)
- [picocom Minimal Serial Terminal](https://github.com/npat-efault/picocom)
- OWASP [IoT Security Verification Standard (ISVS)](https://owasp.org/IoT-Security-Verification-Standard-ISVS/) — Related requirements: V2.1.9: "Verify that authentication credentials for users, devices, or services are not hardcoded in firmware or ecosystem applications"; V3.1.6: "Verify that bootloader stages do not contain sensitive information (e.g. private keys or passwords logged to the console) as part of device start-up"

## Input Validation (ISTG-INT[UART]-INPV)

Input validation testing via the UART interface focuses on whether commands or data submitted through the serial console are properly validated and handled. A serial console that accepts commands without sufficient validation may allow an attacker to execute unintended operations, escalate privileges, or destabilize the device.

### Command Injection via Serial Interface (ISTG-INT[UART]-INPV-001)

**Required Access Levels**

<table width="100%">
	<tr valign="top">
		<th width="1%" align="left">Physical</th>
		<td><i>PA-3</i> - <i>PA-4</i><br>(depending on whether UART test points or headers are accessible without opening the device)</td>
	</tr>
	<tr valign="top">
		<th align="left">Authorization</th>
		<td><i>AA-1</i> - <i>AA-2</i><br>(depending on whether the serial console requires authentication)</td>
	</tr>
</table>

**Summary**

If a UART serial console accepts commands without proper input validation, an attacker may be able to inject operating system commands, manipulate bootloader environment variables, or trigger unintended device behavior. This is particularly relevant in restricted shell environments or custom command interfaces where filtering is implemented but may be bypassable, as well as in bootloader environments where environment variable expansion may lead to unintended command execution.

**Test Objectives**

- Based on [ISTG-INT\[UART\]-AUTHZ-001](#unauthenticated-access-to-serial-console-istg-intuart-authz-001), access to the serial console must be established.
- If a full shell is accessible, standard OS command injection techniques must be tested including shell metacharacters (`;`, `|`, `&&`, `` ` ``, `$()`), path traversal, and environment variable manipulation.
- If a restricted shell or custom command interface is accessible, alternate line-termination and delimiter handling must be assessed, including CR/LF variants (`\r`, `\n`) and raw byte values (`0x0D`, `0x0A`) where the serial parser handles raw input.
- If a restricted shell or custom command interface is accessible, it must be assessed whether the command set can be escaped or bypassed to execute arbitrary commands.
- In bootloader environments (see [ISTG-INT\[UART\]-AUTHZ-002](#bootloader-interrupt-via-serial-console-istg-intuart-authz-002)), environment variable injection must be tested by setting variables such as `bootcmd` or `bootargs` to include malicious commands that execute during the boot process.
- The stability and recovery behavior of the device following malformed or unexpected input must be documented.

**Remediation**

Serial console command interfaces must validate and sanitize all input before processing. Restricted shell environments must be hardened against escape techniques. Bootloader environment variables that influence the boot process must be set as read-only in production builds. Where a serial console is not required in production, it must be disabled entirely in firmware rather than relying on input filtering as the sole protection.

**References**

- [U-Boot Environment Variable Security](https://docs.u-boot.org/en/latest/usage/environment.html)
- [GNU Screen Terminal Multiplexer](https://www.gnu.org/software/screen/)
- OWASP [IoT Security Verification Standard (ISVS)](https://owasp.org/IoT-Security-Verification-Standard-ISVS/) — Related requirements: V3.1.3: "Verify that communication interfaces such as USB, UART, and other variants are disabled or adequately protected during every stage of the device's boot process"
