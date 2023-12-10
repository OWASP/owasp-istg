# 1. Introduction

## Motivation

The networking of a multitude of different devices towards the Internet of Things (IoT) poses new challenges for manufacturers and operators of respective solutions. Due to the interconnection of many different technologies, standards and protocols, a considerable amount of effort is necessary to build up and maintain a homogeneous level of network security, data security and IT security in general. Additionally, since the IoT field is changing and developing quickly, manufacturers and operators must continuously monitor potential threats to their devices and networks.

While conventionally networked computer systems can be secured with established methods, e.g., restricting physical and authorization access to networks and important systems, these methods can be difficult to apply to IoT devices and ecosystems due to the above-mentioned heterogeneity and new network layouts. Compared to conventional computer networks, IoT infrastructures can be very wide-spread. Even though the back end infrastructure might be similar to conventional computer networks, IoT devices could be located at an arbitrary location, possibly even outside of a secure zone of the operator. In some cases, the devices are even physically accessible to third parties and potential attackers, e.g., connected cars, smart home devices or package stations. Hence, every IoT device represents a potential threat to user data and the entire infrastructure since a single manipulated device is sufficient to endanger the entire ecosystem.

In order to reduce the risk of successful attacks, manufacturers and operators should periodically assess the security level of their IoT solutions. An instrument for this purpose is penetration testing. The goal of a penetration test is to identify security vulnerabilities within IoT solutions. The results can be used to address the detected vulnerabilities and thus strengthen the security level.



## Challenges

Within the context of penetration tests, it is important that the test procedure is transparent. Otherwise, the manufacturer or operator might not be able to understand the meaning of the test results to the full extent and could draw wrong conclusions. Furthermore, test results have to be reproducible, so that on the one hand the developers can replicate how a vulnerability was exploited in order to craft a sufficient fix and on the other hand to enable a proper retest once the fix has been applied.

Testing methodologies have been developed in order to make test procedures and results comparable and to ensure that the results of two or more testers, who perform the same test of the same target, do not differ. These well-known methodologies define a common approach for performing tests, including key aspects of testing and test cases, which have to be considered during a test. Unfortunately, only a few, not yet complete test methodologies for IoT penetration tests exist at the moment of writing this guide. Furthermore, these methodologies only focus on a specific technological area or are currently in an early development phase.



## Goals

In order to solve the above-mentioned challenges, the aim of this guide is to develop a methodology for penetration tests of end devices in the IoT field, including general key aspects of testing.

The methodology should:

-   be flexibly expandable so that more detailed test cases for certain technologies can be added later on (*expandability*).
    
-   enable the comparison of test procedure (test steps/cases) and results regardless of specific technologies or device types (*comparability*).
    
-   serve the purpose of a common language between manufacturers/operators and penetration testing service providers, meaning that it should facilitate the communication between both parties by establishing a comprehensible terminology (*comprehensibility*).

-   be efficient, so that it can be used as a supporting instrument by penetration testing teams without requiring major changes to any established workflows or additions of any new steps or testing phases (*efficiency*).



## Intended Audience

As the name suggests, the OWASP IoT Security Testing Guide is mainly intended to be used by penetration testers and security analysts in the IoT, hardware and embedded fields. However, others might benefit from the concepts and test cases introduced in this guide as well:

### **Builder**

- **Manufacturers of IoT devices** (e.g., architects, engineers, developers and managers) can use the contents of this guide to get an understanding of potential issues and vulnerabilities that might affect their products. Since vulnerable products can lead to various kinds of damages for the manufacturer (financial loss, loss of reputation, etc.), there should be an interest in understanding how a certain product could be vulnerable in any given context or operational environment. By increasing the awareness and understanding early on in the design and development process, it is possible to improve product security in the long term while keeping the respective costs as low as possible.
### **Breaker**

- **Penetration testers and bug bounty researchers** can use the concepts introduced in [2. IoT Security Testing Framework](../02_framework/README.md) to plan their tests and define the test scope, test conditions and test approach. While performing the test, the test cases in [3. Test Case Catalog](../03_test_cases/README.md) and the respective [Checklists](../../checklists) can be used:
  - a) as a guide that shows which aspects should be tested, why they should be tested, how they should be tested and how potential issues could be mitigated as well as
  - b) to  keep track of the test completion status, making sure that all relevant aspects have been examined.
- **Security consultants and security managers** can use this guide and its contents as a common foundation for working with their teams and clients as well as communicating with any of the stakeholders mentioned above. Especially the terminology and structure defined in this guide should help to facilitate collaboration across different teams and organizations.
### **Defender**

- **Operators of IoT devices** (e.g., users) can use this guide in a similar fashion as manufacturers. However, the operators who run IoT devices usually have no or very little influence on the design and development process. Hence, their focus is more directed towards understanding how a device might be vulnerable in a particular operational environment and how this environment could be affected in case that the device is compromised or insecure.



## Modularity as a Key Concept

This guide is not a monolithic, all-encompassing instruction manual for IoT device penetration testing. Instead, it should be seen as a dynamic and growing collection of test cases for various technologies related to IoT devices.

In its current state, this guide comprises test cases on a very high and generic level. This is intentional since the base version of this guide should be applicable to as many different IoT devices as possible (*comparability*). However, the long-term goal is that this guide will be expanded over time by adding modules with more detailed test cases for specific technologies (*expandability*). Thereby, the guide will evolve and become more and more detailed over time.



## Solution Approach

During the preparation of a penetration test, a series of important decisions need to be made, which have a major impact on the test procedure and consequently the test results. Part of these decisions is to clarify what should be tested (*scope of the test*) and how the test should be performed (*test perspective*).

In order to achieve the proposed solution, the following approach was chosen:

1. **Creation of an IoT device model, which represents an abstract, generalized IoT device:** 

   Before the test scope for an IoT device penetration test can be identified, it must first be defined what an IoT device is and which parts it consists of. In order to support the test scope definition, the device model should include device components that can either be included in or excluded from the test scope. This guide will only focus on components, directly belonging to the device itself. All device-external elements, such as web applications, mobile applications and back end servers, will not be part of this guide although sister OWASP testing guides cover these areas. The device model will serve as a generalized scheme, depicting the common structure of IoT devices, thereby enhancing the comprehensibility and comparability of the methodology presented in this guide. As all further parts of the guide will rely on this basis, the creation of the device model is a mandatory and important first step.

2. **Creation of an attacker model, which represents and categorizes potential attackers:** 

   The guide will comprise key aspects of testing for each component of the device model. Therefore, it will include a catalog of potential test cases for all device components. Since it might not be required to perform all of these test cases for any given kind of IoT device, a systematic approach is required, which yields a selection of applicable test cases based on the requirements and the intended operational environment of a specific device. The attacker model will support the definition of the test perspective, providing comprehensibility and comparability by defining common groups/types of attackers. In order to maintain efficiency, the attacker model will not incorporate extensive threat and risk analysis models. This also  benefits the comparability across different device implementations.

3. **Creation of a test methodology, which includes general key aspects of testing:** 

   Based on the IoT device model, a testing methodology including general key aspects of testing will be developed. These general key aspects represent security issues that are relevant for the device components and will be derived from more detailed test cases for specific exemplars of a given component or technology. This derivation should decouple the key aspects from specifics of the exemplar in order to enable the methodology to be used for as many different IoT device implementations as possible (*comparability*). However, the structure of the methodology will allow to add more detailed key aspects of testing for specific exemplars of a device component later on, thus providing expandability.
   

