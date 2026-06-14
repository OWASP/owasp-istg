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
* [Reporting Guidance](#reporting-guidance)
* [Security and Remediation Considerations](#security-and-remediation-considerations)
* [Out-of-Scope Activities](#out-of-scope-activities)
* [References](#references)

## Overview

Joint Test Action Group (JTAG), Serial Wire Debug (SWD), and related device-internal debug-access paths may be present on IoT devices for development, manufacturing, diagnostics, service, or failure analysis.

The security impact of such interfaces depends on the specific implementation and production configuration. Relevant factors include whether the interface is present, whether it is physically reachable, which transport is exposed, whether access is disabled or restricted in the intended production state, whether authenticated debug is implemented, and which asset classes are reachable through the interface.

This specialization focuses on authorized, laboratory-based testing of JTAG, SWD, and related debug-access paths on IoT devices. The baseline methodology is intended to be read-only and non-destructive by default.

Documented hardware-interface threat models and vulnerability disclosures show that insufficiently restricted debug interfaces can support firmware or data extraction, runtime asset exposure, and deeper platform analysis when physical access is available. This specialization focuses on testable device properties rather than threat-actor attribution.

JTAG, SWD, Boundary Scan, internal scan chains, debug locking, debug authentication, readout protection, lifecycle states, eFuse-based controls, and option-byte style configuration are related but distinct concepts. The presence of a physical interface does not automatically imply unrestricted processor debug access or full memory access. Actual capabilities depend on the device architecture, vendor implementation, lifecycle state, and configured protections.

## Authorization (ISTG-INT[JTAG]-AUTHZ)

Authorization testing for JTAG, SWD, and related debug-access paths focuses on whether the assessed device rejects unauthorized debug access in its intended production state.

### Unauthorized Debug Access in Production State (ISTG-INT[JTAG]-AUTHZ-001)

**Required Access Levels**

<table width="100%">
	<tr valign="top">
		<th width="1%" align="left">Physical</th>
		<td><i>PA-4</i></td>
	</tr>
	<tr valign="top">
		<th align="left">Authorization</th>
		<td><i>AA-1</i> - <i>AA-4</i><br>(depending on the intended debug-access model for the assessed device)</td>
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

Production devices should enforce the intended debug-access policy using documented hardware-backed or vendor-supported controls where available. Debug access that is not required in production should be disabled or restricted. If service debug access is intentionally retained, it should require documented authentication and should expose only the capabilities required for the service use case.

### Early-Boot Debug-State Exposure (ISTG-INT[JTAG]-AUTHZ-002)

**Required Access Levels**

<table width="100%">
	<tr valign="top">
		<th width="1%" align="left">Physical</th>
		<td><i>PA-4</i></td>
	</tr>
	<tr valign="top">
		<th align="left">Authorization</th>
		<td><i>AA-1</i> - <i>AA-4</i><br>(depending on the intended debug-access model for the assessed device)</td>
	</tr>
</table>

**Summary**

Some devices may apply debug restrictions only after a certain boot stage, reset transition, or lifecycle-state transition. If debug policy is not enforced consistently during the earliest relevant boot stages, a temporary debug-access window may exist before the intended production restrictions are active.

**Test Objectives**

* Vendor documentation and device behavior must be reviewed to determine whether debug restrictions are expected to apply before, during, and after boot.

* Where explicitly authorized and feasible in a non-destructive test scope, it must be determined whether the intended debug restrictions remain consistent across reset and startup states.

* Any uncertainty about early-boot behavior must be documented conservatively.

**Remediation**

Debug restrictions should be enforced consistently across the relevant boot, reset, and lifecycle states. Production debug policy should not depend solely on software initialization that occurs after an unauthorized debug-access window is already available.

## Information Gathering (ISTG-INT[JTAG]-INFO)

Information gathering for JTAG, SWD, and related debug-access paths focuses on identifying the presence, accessibility, transport type, and observable asset boundaries of the interface without performing destructive or unauthorized actions.

### Interface Presence, Physical Accessibility, and Transport Identification (ISTG-INT[JTAG]-INFO-001)

**Required Access Levels**

<table width="100%">
	<tr valign="top">
		<th width="1%" align="left">Physical</th>
		<td><i>PA-4</i></td>
	</tr>
	<tr valign="top">
		<th align="left">Authorization</th>
		<td><i>AA-1</i> - <i>AA-4</i><br>(depending on the assessment scope and device access model)</td>
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

**Remediation**

Unnecessary debug-access paths should be removed, disabled, or restricted in the intended production state. Mechanical concealment or removal of headers should not be treated as a substitute for an enforced debug-access policy.

### Accessible Asset Boundary Review (ISTG-INT[JTAG]-INFO-002)

**Required Access Levels**

<table width="100%">
	<tr valign="top">
		<th width="1%" align="left">Physical</th>
		<td><i>PA-4</i></td>
	</tr>
	<tr valign="top">
		<th align="left">Authorization</th>
		<td><i>AA-1</i> - <i>AA-4</i><br>(depending on the assessment scope and device access model)</td>
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

Debug-access permissions should be limited to the minimum asset scope required for the documented production, service, or diagnostic use case. Production devices should not expose sensitive firmware, memory, secrets, user data, or configuration state through unauthorized debug access.

## Configuration and Patch Management (ISTG-INT[JTAG]-CONF)

Configuration review for JTAG, SWD, and related debug-access paths focuses on whether the observed debug policy is consistent with the documented production lifecycle and vendor security model.

### Lifecycle and Security-Configuration Review (ISTG-INT[JTAG]-CONF-001)

**Required Access Levels**

<table width="100%">
	<tr valign="top">
		<th width="1%" align="left">Physical</th>
		<td><i>PA-4</i></td>
	</tr>
	<tr valign="top">
		<th align="left">Authorization</th>
		<td><i>AA-1</i> - <i>AA-4</i><br>(depending on the assessment scope and device access model)</td>
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

Production devices should use the vendor-supported debug-security configuration appropriate for the intended lifecycle state. Configuration should be applied consistently across documented debug paths. Persistent or irreversible security controls should be managed through a controlled manufacturing and quality-assurance process.

## Reporting Guidance

A finding related to JTAG, SWD, or a related debug-access path should record the relevant device and testing context. At minimum, the report should include:

- Device model and hardware revision where available
- Firmware version where available
- Intended lifecycle state, such as development, manufacturing, production, service, RMA, or decommissioned
- Identified transport, such as JTAG, SWD, Boundary Scan, USB-JTAG, another documented debug path, or unknown
- Physical accessibility of the interface in the tested configuration
- Observed debug-access state, such as unrestricted, disabled, restricted, authenticated, or conditionally available
- Asset classes observed through the interface, if any
- Whether testing remained read-only and non-destructive
- Any assumptions, limitations, or uncertainties
- Remediation principle appropriate to the assessed device and lifecycle state

## Security and Remediation Considerations

The following controls may reduce the risk of unintentionally exposed JTAG, SWD, or related debug-access paths:

- Define the intended debug-access policy for each lifecycle state.
- Disable or restrict debug access that is not required in production.
- Use vendor-supported hardware-backed controls where available.
- Require documented authentication for retained service or RMA debug access.
- Apply least privilege to authenticated debug capabilities.
- Ensure that all documented debug paths are covered by the same production security policy.
- Verify debug-security configuration during manufacturing quality assurance.
- Treat irreversible controls, such as OTP, eFuse, option-byte, readout-protection, or lifecycle-state changes, as controlled production operations.
- Use physical protections such as locked enclosures, tamper-evident seals, and access control as supporting controls, not as a replacement for enforced debug-access policy.
- Document service procedures so that debug access is not left enabled unintentionally after repair or diagnostics.

## Out-of-Scope Activities

The following activities are outside the baseline scope of this specialization unless they are separately authorized and covered by a dedicated methodology:

* Voltage fault injection
* Electromagnetic fault injection
* Clock glitching
* Invasive board modification
* Destructive package analysis
* Permanent lifecycle-state changes
* OTP, eFuse, option-byte, readout-protection, or unlock-state modification
* Firmware modification or reflashing
* ROM parser fuzzing
* Secure-boot validation
* TrustZone or platform-isolation validation
* Anti-tamper architecture assessment

These topics may be relevant in advanced hardware-security assessments, but they should not be treated as baseline JTAG or SWD test steps.

## References

For this specialization, data from the following sources was consolidated:

* Arm Developer Documentation, [CoreSight SoC-400 Technical Reference Manual — JTAG and SWD Interface][arm_coresight_swjdp]
* Espressif Systems, [JTAG Debugging for ESP32-C3][espressif_esp32c3_jtag]
* Espressif Systems, [Configure Built-in JTAG Interface for ESP32-C3][espressif_esp32c3_builtin_jtag]
* Espressif Systems, [Configure Other JTAG Interfaces for ESP32-C3][espressif_esp32c3_other_jtag]
* NVD, [CVE-2019-18827 — Barco ClickShare Button JTAG Access][nvd_cve_2019_18827]
* SEC Consult, [Unlocked JTAG Interface and Buffer Overflow in Siemens SM-2558 Protocol Element][sec_consult_siemens_sm2558]
* NVD, [CVE-2024-7726 — Kioxia CM6 / PM6 / PM7 JTAG Debug Port][nvd_cve_2024_7726]
* NVD, [CVE-2017-18347 — STM32F0 RDP Level 1 SWD Race Condition][nvd_cve_2017_18347]
* AMD, [AMD Graphics Vulnerabilities — May 2026, CVE-2025-0040][amd_cve_2025_0040]
* MITRE EMB3D, [TID-115: Firmware/Data Extraction via Hardware Interface][mitre_emb3d_tid_115]
* MITRE EMB3D, [TID-119: Latent Hardware Debug Port Allows Memory/Code Manipulation][mitre_emb3d_tid_119]
* MITRE CWE, [CWE-1191: On-Chip Debug and Test Interface With Improper Access Control][mitre_cwe_1191]
* MITRE CWE, [CWE-1244: Internal Asset Exposed to Unsafe Debug Access Level or State][mitre_cwe_1244]
* NVD, [CVE-2025-26408 — Wattsense Bridge JTAG Interface][nvd_cve_2025_26408]
* SEC Consult, [Multiple Vulnerabilities in Wattsense Bridge][sec_consult_wattsense]

[arm_coresight_swjdp]: https://developer.arm.com/documentation/ddi0480/e/Debug-Access-Port/SWJ-DP/JTAG-and-SWD-interface
[espressif_esp32c3_jtag]: https://docs.espressif.com/projects/esp-idf/en/stable/esp32c3/api-guides/jtag-debugging/index.html
[espressif_esp32c3_builtin_jtag]: https://docs.espressif.com/projects/esp-idf/en/stable/esp32c3/api-guides/jtag-debugging/configure-builtin-jtag.html
[espressif_esp32c3_other_jtag]: https://docs.espressif.com/projects/esp-idf/en/stable/esp32c3/api-guides/jtag-debugging/configure-other-jtag.html
[nvd_cve_2019_18827]: https://nvd.nist.gov/vuln/detail/CVE-2019-18827
[sec_consult_siemens_sm2558]: https://sec-consult.com/vulnerability-lab/advisory/unlocked-jtag-interface-and-buffer-overflow-in-siemens-sm-2558-protocol-element/
[nvd_cve_2024_7726]: https://nvd.nist.gov/vuln/detail/CVE-2024-7726
[nvd_cve_2017_18347]: https://nvd.nist.gov/vuln/detail/CVE-2017-18347
[amd_cve_2025_0040]: https://www.amd.com/en/resources/product-security/bulletin/amd-sb-6027.html
[mitre_emb3d_tid_115]: https://emb3d.mitre.org/threats/TID-115.html
[mitre_emb3d_tid_119]: https://emb3d.mitre.org/threats/TID-119.html
[mitre_cwe_1191]: https://cwe.mitre.org/data/definitions/1191.html
[mitre_cwe_1244]: https://cwe.mitre.org/data/definitions/1244.html
[nvd_cve_2025_26408]: https://nvd.nist.gov/vuln/detail/CVE-2025-26408
[sec_consult_wattsense]: https://sec-consult.com/vulnerability-lab/advisory/multiple-vulnerabilities-in-wattsense-bridge/
