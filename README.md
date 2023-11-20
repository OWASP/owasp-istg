# OWASP IoT Security Testing Guide

[![CC BY-SA 4.0][cc-by-sa-shield]][cc-by-sa]

The OWASP IoT Security Testing Guide provides a comprehensive methodology for penetration tests in the IoT field offering flexibility to adapt innovations and developments on the IoT market while still ensuring comparability of test results. The guide provides an understanding of communication between manufacturers and operators of IoT devices as well as penetration testing teams that’s facilitated by establishing a common terminology. 

The methodology, the underlying models and the catalog of test cases present tools that can be used separately and in conjunction with each other. Read the latest version of the guide https://owasp.org/owasp-istg/

## Table of Contents

1. [**Introduction**](./src/01_introduction/README.md)

2. [**IoT Security Testing Framework**](./src/02_framework/README.md)

   2.1. [IoT Device Model](./src/02_framework/device_model.md)

   2.2. [Attacker Model](./src/02_framework/attacker_model.md)

   2.3. [Testing Methodology](./src/02_framework/methodology.md)

3. [**Test Case Catalog**](./src/03_test_cases/README.md)

   3.1. [Processing Units (IOT-PROC)](./src/03_test_cases/processing_units/README.md)

   3.2. [Memory (IOT-MEM)](./src/03_test_cases/memory/README.md)

   3.3. [Firmware (IOT-FW)](./src/03_test_cases/firmware/README.md)

      3.3.1. [Installed Firmware (IOT-FW[INST])](./src/03_test_cases/firmware/installed_firmware.md)

      3.3.1. [Firmware Update Mechnanism (IOT-FW[UPDT])](./src/03_test_cases/firmware/firmware_update_mechanism.md)

   3.4. [Data Exchange Services (IOT-DES)](./src/03_test_cases/data_exchange_services/README.md)

   3.5. [Internal Interfaces (IOT-INT)](./src/03_test_cases/internal_interfaces/README.md)

   3.6. [Physical Interfaces (IOT-PHY)](./src/03_test_cases/physical_interfaces/README.md)

   3.7. [Wireless Interfaces (IOT-WRLS)](./src/03_test_cases/wireless_interfaces/README.md)

   3.8. [User Interfaces (IOT-UI)](./src/03_test_cases/user_interfaces/README.md)



## Related Work

The concepts, models and test steps presented in the OWASP IoT Security Testing Guide are based on the master's thesis **"Development of a Methodology for Penetration Tests of Devices in the Field of the Internet of Things"** by Luca Pascal Rotsch.



Test cases were derived from the following public sources:

* OWASP [**"Web Security Testing Guide"**][owasp_wstg]
* OWASP [**"Firmware Security Testing Methodology"**][owasp_fstm]
* OWASP [**"Mobile Security Testing Guide"**][owasp_mstg]
* [**"IoT Pentesting Guide"**][iot_pentesting_guide] by Aditya Gupta
* [**"IoT Penetration Testing Cookbook"**][iot_penetration_testing_cookbook] by Aaron Guzman and Aditya Gupta
* [**"The IoT Hacker's Handbook"**][iot_hackers_handbook] by Aditya Gupta
* [**"Practical IoT Hacking"**][practical_iot_hacking] by Fotios Chantzis, Ioannis Stais, Paulino Calderon, Evangelos Deirmentzoglou, and Beau Woods
* further sources are referenced in the respective test cases



**We also like to thank our collaborators and supporters (see [Project Collaborators and Acknowledgements](./acknowledgements.md))!**



[cc-by-sa]:  http://creativecommons.org/licenses/by-sa/4.0/
[cc-by-sa-shield]: https://img.shields.io/badge/License-CC%20BY--SA%204.0-lightgrey.svg
[owasp_wstg]: https://owasp.org/www-project-web-security-testing-guide/	"OWASP Web Security Testing Guide"
[owasp_fstm]: https://github.com/scriptingxss/owasp-fstm	"OWASP Firmware Security Testing Methodology"
[owasp_mstg]: https://owasp.org/www-project-mobile-security-testing-guide/	"OWASP Mobile Security Testing Guide"
[iot_pentesting_guide]: https://www.iotpentestingguide.com	"IoT Pentesting Guide"
[iot_penetration_testing_cookbook]: https://www.packtpub.com/product/iot-penetration-testing-cookbook/9781787280571	"IoT Penetration Testing Cookbook"
[iot_hackers_handbook]: https://link.springer.com/book/10.1007/978-1-4842-4300-8	"The IoT Hacker's Handbook"
[practical_iot_hacking]: https://nostarch.com/practical-iot-hacking	"Practical IoT Hacking"
