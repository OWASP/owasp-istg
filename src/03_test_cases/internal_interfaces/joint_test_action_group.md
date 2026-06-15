# 3.5.1. Joint Test Action Group and Serial Wire Debug Interfaces (ISTG-INT[JTAG])

## Table of Contents

* [Overview](#overview)
* [Authorization (ISTG-INT[JTAG]-AUTHZ)](#authorization-istg-intjtag-authz)

  * [Unauthorized Debug Access in Production State (ISTG-INT[JTAG]-AUTHZ-001)](#unauthorized-debug-access-in-production-state-istg-intjtag-authz-001)
  * [Early-Boot Debug-State Exposure (ISTG-INT[JTAG]-AUTHZ-002)](#early-boot-debug-state-exposure-istg-intjtag-authz-002)
* [Information Gathering (ISTG-INT[JTAG]-INFO)](#information-gathering-istg-intjtag-info)

  * [Interface Presence, Physical Accessibility, and Transport Identification (ISTG-INT[JTAG]-INFO-001)](#interface-presence-physical-accessibility-and-transport-identification-istg-intjtag-info-001)
  * [Accessible Asset Boundary Review (ISTG-INT[JTAG]-INFO-002)](#accessible-asset-boundary-review-istg-intjtag-info-002)
* [Configuration and Patch Management (ISTG-INT[JTAG]-CONF)](#configuration-and-patch-management-istg-intjtag-conf)

  * [Lifecycle and Security-Configuration Review (ISTG-INT[JTAG]-CONF-001)](#lifecycle-and-security-configuration-review-istg-intjtag-conf-001)

## Overview

Joint Test Action Group (JTAG), Serial Wire Debug (SWD), and related device-internal debug-access paths may be present on IoT devices for development, manufacturing, diagnostics, service, or failure analysis.

The security impact of such interfaces depends on the specific implementation and production configuration. Relevant factors include whether the interface is present, whether it is physically reachable, which transport is exposed, whether access is disabled or restricted in the intended production state, whether authenticated debug is implemented, and which asset classes are reachable through the interface.

This specialization focuses on authorized, laboratory-based testing of JTAG, SWD, and related debug-access paths on IoT devices. The baseline methodology is intended to be read-only and non-destructive by default.

Fault injection, invasive or destructive analysis, irreversible lifecycle-state changes, firmware modification, secure-boot validation, and platform-isolation assessment are outside the baseline scope unless separately authorized and covered by a dedicated methodology.

Documented hardware-interface threat models and vulnerability disclosures show that insufficiently restricted debug interfaces can support firmware or data extraction, runtime asset exposure, and deeper platform analysis when physical access is available. This specialization focuses on testable device properties rather than threat-actor attribution.

JTAG, SWD, Boundary Scan, internal scan chains, debug locking, debug authentication, readout protection, lifecycle states, eFuse-based controls, and option-byte style configuration are related but distinct concepts. The presence of a physical interface does not automatically imply unrestricted processor debug access or full memory access. Actual capabilities depend on the device architecture, vendor implementation, lifecycle state, and configured protections.

Input Validation, Secrets, Cryptography, and Business Logic are not inherited as separate categories in this specialization: unsafe write, breakpoint, or execution-control operations are outside the baseline unless separately authorized; secret, firmware, memory, or cryptographic-material exposure is covered as an observable asset-boundary concern; and business-logic testing is not applicable to a low-level debug-access transport.

## Authorization (ISTG-INT[JTAG]-AUTHZ)

Authorization testing for JTAG, SWD, and related debug-access paths focuses on whether the assessed device rejects unauthorized debug access in its intended production state.

### Unauthorized Debug Access in Production State (ISTG-INT[JTAG]-AUTHZ-001)

**Required Access Levels**

<table width="100%">
	<tr valign="top">
		<th width="1%" align="left">Physical</th>
		<td><i>PA-3</i> - <i>PA-4</i><br>(depending on whether the debug interface is accessible without opening the device)</td>
	</tr>
	<tr valign="top">
		<th align="left">Authorization</th>
		<td><i>AA-1</i></td>
	</tr>
</table>

**Summary**

In the intended production state, debug-access paths should not allow unauthorized access to the device. Depending on the device design, debug access may be disabled, restricted, authenticated, or intentionally retained for service purposes. If the device does not correctly enforce the intended access policy, an unauthorized individual with physical access may be able to interact with the debug interface.

**Test Objectives**

* It must be determined whether JTAG, SWD, or a related debug-access path is accessible in the intended production state.

* It must be determined whether debug access is unrestricted, disabled, restricted, authenticated, or conditionally available.

* If debug access is intentionally retained, it must be determined whether access is controlled according to the documented production or service policy.

* It must be determined whether the implementation relies only on physical obscurity, such as hidden pads, missing headers, or enclosure placement, instead of an enforced access-control mechanism.

**Remediation**

Production devices should disable or restrict unused debug access using vendor-supported debug-lock, readout-protection, or authenticated-debug controls, and retained service access should expose only the minimum required capability.

**References**

- [MITRE CWE-1191: On-Chip Debug and Test Interface With Improper Access Control][mitre_cwe_1191]
- [NVD CVE-2024-7726 — Kioxia CM6 / PM6 / PM7 JTAG Debug Port][nvd_cve_2024_7726]
- [NVD CVE-2025-26408 — Wattsense Bridge JTAG Interface][nvd_cve_2025_26408]

### Early-Boot Debug-State Exposure (ISTG-INT[JTAG]-AUTHZ-002)

**Required Access Levels**

<table width="100%">
	<tr valign="top">
		<th width="1%" align="left">Physical</th>
		<td><i>PA-3</i> - <i>PA-4</i><br>(depending on whether the debug interface is accessible without opening the device)</td>
	</tr>
	<tr valign="top">
		<th align="left">Authorization</th>
		<td><i>AA-1</i></td>
	</tr>
</table>

**Summary**

Some devices may apply debug restrictions only after a certain boot stage, reset transition, or lifecycle-state transition. If debug policy is not enforced consistently during the earliest relevant boot stages, a temporary debug-access window may exist before the intended production restrictions are active.

**Test Objectives**

* Vendor documentation and device behavior must be reviewed to determine whether debug restrictions are expected to apply before, during, and after boot.

* Where explicitly authorized and feasible in a non-destructive test scope, it must be determined whether the intended debug restrictions remain consistent across reset and startup states.

* Any uncertainty about early-boot behavior must be documented conservatively.

**Remediation**

Debug restrictions should be enforced from the earliest relevant boot, reset, and lifecycle states rather than relying solely on later software initialization.

**References**

- [NVD CVE-2019-18827 — Barco ClickShare Button JTAG Access][nvd_cve_2019_18827]
- [NVD CVE-2017-18347 — STM32F0 RDP Level 1 SWD Race Condition][nvd_cve_2017_18347]

## Information Gathering (ISTG-INT[JTAG]-INFO)

Information gathering for JTAG, SWD, and related debug-access paths focuses on identifying the presence, accessibility, transport type, and observable asset boundaries of the interface without performing destructive or unauthorized actions.

### Interface Presence, Physical Accessibility, and Transport Identification (ISTG-INT[JTAG]-INFO-001)

**Required Access Levels**

<table width="100%">
	<tr valign="top">
		<th width="1%" align="left">Physical</th>
		<td><i>PA-3</i> - <i>PA-4</i><br>(depending on whether the debug interface is accessible without opening the device)</td>
	</tr>
	<tr valign="top">
		<th align="left">Authorization</th>
		<td><i>AA-1</i></td>
	</tr>
</table>

**Summary**

JTAG, SWD, and related debug-access paths may be exposed through headers, pads, test points, board-to-board connectors, service areas, or documented manufacturing and diagnostic paths. Physical reachability and transport identification affect the risk and the required follow-up testing, but the presence of a physical interface alone does not prove unrestricted debug capability.

**Test Objectives**

* It must be determined whether JTAG, SWD, or a related debug-access path is present on the assessed device.

* It must be determined whether the interface is physically reachable in the tested configuration.

* It must be determined whether the identified path is JTAG, SWD, Boundary Scan, another documented transport, or an unknown internal interface.

* If a JTAG chain is present, it must be determined whether the chain exposes one or more components.

* Vendor documentation should be reviewed for alternate documented debug paths that may not be obvious from visual inspection alone.

* Standard tooling such as JTAGulator or JTAGenum may support authorized pin discovery, and OpenOCD may support authorized interaction with identified debug targets.

**Remediation**

Production devices should disable or restrict unnecessary debug paths instead of relying on hidden pads, missing headers, or mechanical concealment as the primary control.

**References**

- [NVD CVE-2024-7726 — Kioxia CM6 / PM6 / PM7 JTAG Debug Port][nvd_cve_2024_7726]
- [NVD CVE-2025-26408 — Wattsense Bridge JTAG Interface][nvd_cve_2025_26408]

### Accessible Asset Boundary Review (ISTG-INT[JTAG]-INFO-002)

**Required Access Levels**

<table width="100%">
	<tr valign="top">
		<th width="1%" align="left">Physical</th>
		<td><i>PA-3</i> - <i>PA-4</i><br>(depending on whether the debug interface is accessible without opening the device)</td>
	</tr>
	<tr valign="top">
		<th align="left">Authorization</th>
		<td><i>AA-1</i></td>
	</tr>
</table>

**Summary**

If a debug-access path is available within the authorized test scope, it is important to determine which asset classes are observable through that path. Relevant asset classes may include firmware, memory regions, registers, device identifiers, configuration state, or runtime information. This review should remain read-only in the baseline methodology.

**Test Objectives**

* It must be determined which asset classes, if any, are observable through the authorized debug-access path.

* Static firmware or memory exposure must be distinguished from runtime inspection.

* The tested access scope and any observed limitations must be documented.

* Write, erase, firmware modification, breakpoint, execution-control, lifecycle-change, or unlock operations must not be performed unless they are separately authorized.

**Remediation**

Debug-access policy should limit observable assets to the minimum required scope and prevent unauthorized exposure of firmware, memory, secrets, user data, or configuration state.

**References**

- [MITRE EMB3D TID-115: Firmware/Data Extraction via Hardware Interface][mitre_emb3d_tid_115]
- [MITRE EMB3D TID-119: Latent Hardware Debug Port Allows Memory/Code Manipulation][mitre_emb3d_tid_119]
- [MITRE CWE-1244: Internal Asset Exposed to Unsafe Debug Access Level or State][mitre_cwe_1244]
- [AMD CVE-2025-0040 — AMD Graphics Vulnerabilities, May 2026][amd_cve_2025_0040]

## Configuration and Patch Management (ISTG-INT[JTAG]-CONF)

Configuration review for JTAG, SWD, and related debug-access paths focuses on whether the observed debug policy is consistent with the documented production lifecycle and vendor security model.

### Lifecycle and Security-Configuration Review (ISTG-INT[JTAG]-CONF-001)

**Required Access Levels**

<table width="100%">
	<tr valign="top">
		<th width="1%" align="left">Physical</th>
		<td><i>PA-3</i> - <i>PA-4</i><br>(depending on whether the debug interface is accessible without opening the device)</td>
	</tr>
	<tr valign="top">
		<th align="left">Authorization</th>
		<td><i>AA-1</i></td>
	</tr>
</table>

**Summary**

Debug-access policy is often affected by lifecycle state, readout protection, debug locking, authenticated debug, eFuse-based controls, option-byte style configuration, or vendor-specific production settings. These mechanisms are not interchangeable, and their behavior varies by vendor and product family.

**Test Objectives**

* The intended lifecycle state of the assessed device must be identified where possible.

* Vendor documentation must be reviewed to determine which debug-security controls apply to the assessed device and lifecycle state.

* It must be determined whether the observed debug-access behavior is consistent with the documented production policy.

* It must be determined whether all documented debug paths are covered by the intended security configuration.

* Persistent or irreversible configuration mechanisms must be documented without changing them unless separate written authorization exists.

**Remediation**

Production devices should apply and verify the vendor-supported debug-security configuration for the intended lifecycle state, including readout protection, debug locks, or eFuse/option-byte settings where applicable.

**References**

- [MITRE CWE-1191: On-Chip Debug and Test Interface With Improper Access Control][mitre_cwe_1191]
- [MITRE CWE-1244: Internal Asset Exposed to Unsafe Debug Access Level or State][mitre_cwe_1244]
- [NVD CVE-2017-18347 — STM32F0 RDP Level 1 SWD Race Condition][nvd_cve_2017_18347]


[nvd_cve_2019_18827]: https://nvd.nist.gov/vuln/detail/CVE-2019-18827
[nvd_cve_2024_7726]: https://nvd.nist.gov/vuln/detail/CVE-2024-7726
[nvd_cve_2017_18347]: https://nvd.nist.gov/vuln/detail/CVE-2017-18347
[amd_cve_2025_0040]: https://www.amd.com/en/resources/product-security/bulletin/amd-sb-6027.html
[mitre_emb3d_tid_115]: https://emb3d.mitre.org/threats/TID-115.html
[mitre_emb3d_tid_119]: https://emb3d.mitre.org/threats/TID-119.html
[mitre_cwe_1191]: https://cwe.mitre.org/data/definitions/1191.html
[mitre_cwe_1244]: https://cwe.mitre.org/data/definitions/1244.html
[nvd_cve_2025_26408]: https://nvd.nist.gov/vuln/detail/CVE-2025-26408
