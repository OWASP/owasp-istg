# 2.2. Attacker Model

In this chapter, a selection scheme for test cases will be described, which is based on potential attackers that are assumed to be a threat to a given IoT device. Contrary to a full threat and risk modeling approach, like the STRIDE model, the attacker model used in this guide presents a more streamlined procedure for defining and selecting threats to IoT devices.

The reasons for not using a formal threat and risk modeling approach are:

-   Threat and risk modeling is usually focused on one specific implementation design. Thus, the identified threats and risks are based on certain conditions of a given solution or device, which makes it difficult to compare different solutions with each other.

-   Performing a formal threat and risk analysis requires a significant amount of time, which further increases with the complexity of the subject. Making a formal threat and risk analysis a mandatory requirement for penetration tests would result in longer testing periods and consequently higher expenses per test.

The spectrum of potential attackers reaches from anonymous global attackers to privileged individuals and users of the device. As will be explained in following sections, the list of attackers can be narrowed down by defining minimum and maximum access requirements, representing the test perspective. Every device component and test case will be tagged with the access level, which is required to perform the respective tests. Hence, the list of device components in scope of the test as well as the list of applicable test cases will be a result of applying the attacker model on the results, yielded by the device model.

It must be noted that, within this chapter, the term "IoT device" refers to a single device or device type whereas, in the other chapters of this guide, it refers to IoT devices in general.




## Conceptual Basis for the Attacker Model

This attacker model will characterize groups of potential attackers based on their access capabilities[^1]. The metrics that are used for this attacker model are based on the metrics of the [CVSS][cvss]. Even though the CVSS is primarily used to rate the severity of vulnerabilities in the web application and computer networking field, it implements a straightforward approach to assess the capabilities of attackers and the conditions that are required to exploit certain security issues. Another benefit of using a model that is similar to the CVSS is that many security professionals are already working with the CVSS. Hence, many testers and manufacturers/operators are familiar with this system, which also contributes to the acceptance of this attacker model.

The CVSS defines the following exploitability metrics:

-   **Attack vector:** "This metric reflects the context by which vulnerability exploitation is possible" ([source][cvss]). Values for this metric are ranging from network access (e.g., via the internet) to physical access. Within the attacker model, this metric will be reflected by the physical access level.

-   **Attack complexity:** "This metric describes the conditions beyond the attacker's control that must exist in order to exploit the vulnerability" ([source][cvss]). The attack complexity is not used in the attacker model since it refers to "conditions beyond the attacker's control" ([source][cvss]) and thus is not relevant for categorizing potential attackers.

-   **Privileges required:** "This metric describes the level of privileges an attacker must possess before successfully exploiting the vulnerability" ([source][cvss]). Values for this metric are ranging from none (no privileges) to high. The required privileges are represented in the attacker model by the authorization access level.

-   **User interaction:** "This metric captures the requirement for a human user, other than the attacker, to participate in the successful compromise of the vulnerable component" ([source][cvss]). The necessity of interactions by legitimate users will not be considered in the attacker model since, while being relevant for the exploitability of a vulnerability, it is not relevant for the selection of applicable test cases.

[^1]: In regards of IT security, attackers are usually characterized based on further factors, e.g., their aggressiveness and their resources (processing power, time, money). However, these factors do not have or only have a minor impact for the selection of applicable test cases.



## Access Levels

Within this attacker model, access levels are a measure for the relation between a certain group of individuals (access group) and the IoT device. They describe how individuals of the access group are intended to be able to interact with the device. These can either be physical interactions or logical authorization interactions.

The degree of how close individuals can get to the device is measured by the physical access level. The physical access level is an adaption of the CVSS metric "attack vector" and it reflects the physical context that is required to perform attacks against a target device. Therefore, some of the original values from the CVSS were used (network, local, physical). However, the description of local access was adjusted in regards of the focus on the physical context. Additionally, the physical access as defined in the CVSS was split into two levels: non-invasive and invasive physical access. The reason for this is that some IoT devices are protected with special measures that restrict access to device-internal elements, e.g., locked or sealed enclosures. In this case, attackers might not be able to access device-internals in a reasonable amount of time, thus they only have non-invasive physical access. Other devices have enclosures that can be opened in a short time, e.g., by removing screws. Thus, attackers could access device-internals, therefore gaining invasive physical access. Overall, the physical access level can be affected by factors like geographical location, building security or the device enclosure.

The following physical access levels are defined:

1.  **Remote access (*PA-1*):** There is an arbitrary physical distance between an individual and the device. An attacker with remote access can be located anywhere in the world, which usually means that the device is directly accessible via a Global Area Network (GAN).

2.  **Local access (*PA-2*):** There is a limited physical distance[^2] between an individual and the device, but direct physical interactions are not possible. An attacker with local access can use the device from close proximity, which usually means that the device is directly accessible via a Local Area Network (LAN) or Wireless Local Area Network (WLAN).

3.  **Non-invasive access (*PA-3*):** There is no physical distance between an individual and the device, but the individual cannot directly access device-internal elements in a physical manner (i.e., cannot easily open the device enclosure).

4.  **Invasive access (*PA-4*):** There is no physical distance between an individual and the device and the individual can directly access device-internal elements in a physical manner (i.e., open the device enclosure).

The digital privileges of individuals are measured by the authorization access level. The authorization access level is an adaption of the CVSS metric "privileges required". In addition to the values, defined in the CVSS, another level of privileges, called manufacturer-level access, was added on top of the high privileges. Contrary to web applications and computer networks, which are usually operated from within the control zone of the operator (e.g., within a data center), IoT devices are often operated outside that control zone. Established methods for securing maintenance and debugging access (e.g., restricting maintenance access to pre-defined subnets, IP addresses or physical ports in the data center) can not always be applied. Hence, attacks against a device with manufacturer-level access might be possible. Overall, the authorization access level can be affected by factors like policies or role-based access models.

The following authorization access levels are defined:

1.  **Unauthorized access (*AA-1*):** An individual can get anonymous access to the device component. Attackers with anonymous access can be any unregistered user.

2.  **Low-privileged access (*AA-2*):** An individual can only get access to the device component, if it is authenticated and in possession of standard authorization privileges. Attackers with low-privileged access can be any registered user.

3.  **High-privileged access (*AA-3*):** An individual can only get access to the device component, if it is authenticated and in possession of extensive privileges. The term "extensive privileges" means that individuals have access to restricted functionalities that are not available to all registered users of the device component (e.g., configuration settings).

4.  **Manufacturer-level access (*AA-4*):** An individual can only get access to the device component, if it is authenticated and in possession of manufacturer-level authorization privileges. Contrary to high-privileged access, manufacturer-level access is not restricted in any way and includes, e.g., debugging access for developers of the device, access to the source code or root-level access to the firmware.

[^2]: Limited physical distance is not restricted to a specic maximum value per se. Depending on the technologies in use, the maximum distance might range from a few meters (e.g., in case of Bluetooth) to a few kilometers (e.g., in case of LTE).



## Mapping of Device Components and Access Levels

The perspective of the testers during the test will be determined by minimal and maximal access levels, chosen as a baseline for the test. Physical and authorization access levels have different impacts on the penetration test and its scope.

**Physical access level:**

-   The physical access level refers to the device as a whole. Thus, some physical access levels directly define that certain device components can not be tested with the given level since an attacker could not interact with these components at all. The relation between physical access levels and device components is shown in the table below.

-   Based on the specific requirements of a manufacturer or operator, the minimal and/or maximal physical access levels might be hard boundaries for the test execution since the contractee might want to specifically exclude certain tests, e.g., those which require invasive physical access.

**Authorization access level:**

-   Since authorization access might be handled differently across multiple device components, the authorization access level rather refers to access to an individual component than to the device as a whole. Thus, the impact of authorization access levels on the test scope always depends on the specific implementation of the business logic and the AuthZ/permission scheme per component.

-   There is no reason for selecting a minimal authorization access level for the test perspective since evaluating whether it is possible to get access to (parts of) the device with lower privileges than intended should be part of the test.

All in all, the attacker model can be used to create an abstract representation of potential attackers. It can be used to describe which kind of attackers is considered a threat to a given device in its operation environment. Contrary to other methodologies and models, this one can be used in a more streamlined manner, thus being more efficient, e.g., compared to full threat and risk analysis approaches. It is also takes the specifics of the IoT context more into account than the CVSS, which it is based on. In combination with the device model, it is possible to define the test scope and test perspective, thereby determining which test cases can and shall be performed.

| Component                 | PA-4  |   PA-3    |   PA-2    |   PA-1    |
| ------------------------- | :---: | :-------: | :-------: | :-------: |
| Processing Unit           | **✓** |           |           |           |
| Memory                    | **✓** |           |           |           |
| Installed Firmware        | **✓** | **?**[^3] | **?**[^3] | **?**[^3] |
| Firmware Update Mechanism | **✓** | **?**[^3] | **?**[^3] | **?**[^3] |
| Data Exchange Service     | **✓** | **?**[^4] | **?**[^4] | **?**[^4] |
| Internal Interface        | **✓** |           |           |           |
| Physical Interface        | **✓** |   **✓**   | **?**[^5] |           |
| Wireless Interface        | **✓** |   **✓**   |   **✓**   |           |
| User Interface            | **✓** |   **✓**   | **?**[^6] | **?**[^6] |

[^3]: Installed firmware and the firmware update mechanism might be testable with non-invasive (*PA-3*), local (*PA-2*) or remote physical access (*PA-1*), depending on how direct access to the firmware can be accomplished (e.g., via SSH).

[^4]: Data exchange services might be testable with non-invasive (*PA-3*), local (*PA-2*) or remote physical access (*PA-1*), depending on if they were designed for that kind of access, e.g., for remote control or monitoring purposes.

[^5]: Physical interfaces might be testable with local physical access (*PA-2*) under certain circumstances, e.g., if the physical interface is connected to a local network.

[^6]: User interfaces might be testable with local (*PA-2*) or remote physical access (*PA-1*), depending on if they were designed for that kind of access, e.g., for remote control or monitoring purposes.



[cvss]: https://www.first.org/cvss/	"Common Vulnerability Scoring System"

