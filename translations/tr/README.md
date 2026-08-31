<a href="https://owasp.org/owasp-istg/"><img width="180px" align="right" style="float: right;" src="../../src/img/istg_cover.png"></a>

# OWASP IoT Güvenlik Test Rehberi (ISTG)

[![CC BY-SA 4.0](https://img.shields.io/badge/License-CC%20BY--SA%204.0-lightgrey.svg)](http://creativecommons.org/licenses/by-sa/4.0/) [![OpenSSF Best Practices](https://www.bestpractices.dev/projects/8419/badge)](https://www.bestpractices.dev/projects/8419)

OWASP IoT Güvenlik Test Rehberi (ISTG), test sonuçlarının karşılaştırılabilirliğini sağlarken IoT pazarındaki yeniliklere ve gelişmelere uyum sağlama esnekliği sunan, IoT alanındaki sızma testleri için kapsamlı bir metodoloji sunar. Kılavuz, ortak bir terminoloji oluşturarak IoT cihazlarının üreticileri ve operatörleri ile sızma testi ekipleri arasındaki iletişimin kolaylaştırılmasını sağlar.

Güvenlik güvencesi ve test kapsamı, aşağıdaki IoT bileşenlerine ve her biri için geçerli test senaryosu kategorilerine genel bakış ile gösterilebilir. Metodoloji, temel modeller ve test senaryoları kataloğu; hem ayrı ayrı hem de birbiriyle bağlantılı olarak kullanılabilecek araçlar sunar.

![Component Overview](../../src/img/Component_Overview.png)

- 🔔 [OWASP ISTG'yi Okumak İçin Buraya Tıklayın 📖📚](https://owasp.org/owasp-istg/) 🔔
- ✅ [En Güncel ISTG Kontrol Listelerini Alın](https://github.com/OWASP/owasp-istg/tree/main/checklists) ✅
- 📝 🔍 [ISTG'ye Katkıda Bulunun](https://owasp.org/www-project-iot-security-testing-guide/#div-contributing) — bu depoda kullanılan kurallar için [katkı kılavuzuna](https://github.com/OWASP/owasp-istg/blob/main/CONTRIBUTING.md) da bakabilirsiniz.

## İçindekiler

1. [**Giriş**](./01_introduction/README.md)
2. [**IoT Güvenlik Test Çerçevesi**](./02_framework/README.md)
   * 2.1. [IoT Cihaz Modeli](./02_framework/device_model.md)
   * 2.2. [Saldırgan Modeli](./02_framework/attacker_model.md)
   * 2.3. [Test Metodolojisi](./02_framework/methodology.md)
3. [**Test Senaryosu Kataloğu**](./03_test_cases/README.md)
   * 3.1. [İşlem Birimleri (ISTG-PROC)](./03_test_cases/processing_units/README.md)
   * 3.2. [Bellek (ISTG-MEM)](./03_test_cases/memory/README.md)
   * 3.3. [Bellenim (ISTG-FW)](./03_test_cases/firmware/README.md)
     * 3.3.1. [Yüklü Bellenim (ISTG-FW[INST])](./03_test_cases/firmware/installed_firmware.md)
     * 3.3.2. [Bellenim Güncelleme Mekanizması (ISTG-FW[UPDT])](./03_test_cases/firmware/firmware_update_mechanism.md)
   * 3.4. [Veri Değişim Hizmetleri (ISTG-DES)](./03_test_cases/data_exchange_services/README.md)
   * 3.5. [Dahili Arayüzler (ISTG-INT)](./03_test_cases/internal_interfaces/README.md)
     * 3.5.1. [Inter-Integrated Circuit (ISTG-INT[I2C])](./03_test_cases/internal_interfaces/inter_integrated_circuit.md)
     * 3.5.2. [Universal Asynchronous Receiver-Transmitter (ISTG-INT[UART])](./03_test_cases/internal_interfaces/universal_asynchronous_receiver_transmitter.md)
   * 3.6. [Fiziksel Arayüzler (ISTG-PHY)](./03_test_cases/physical_interfaces/README.md)
   * 3.7. [Kablosuz Arayüzler (ISTG-WRLS)](./03_test_cases/wireless_interfaces/README.md)
   * 3.8. [Kullanıcı Arayüzleri (ISTG-UI)](./03_test_cases/user_interfaces/README.md)

## İlgili Çalışmalar

OWASP IoT Güvenlik Test Rehberi'nde sunulan kavramlar, modeller ve test adımları Luca Pascal Rotsch tarafından hazırlanan **"Development of a Methodology for Penetration Tests of Devices in the Field of the Internet of Things"** başlıklı yüksek lisans tezine dayanmaktadır.

Test senaryoları aşağıdaki kamuya açık kaynaklardan türetilmiştir:

* OWASP [**"Web Security Testing Guide"**](https://owasp.org/www-project-web-security-testing-guide/)
* OWASP [**"Firmware Security Testing Methodology"**](https://github.com/scriptingxss/owasp-fstm)
* OWASP [**"Mobile Security Testing Guide"**](https://owasp.org/www-project-mobile-security-testing-guide/)
* [**"IoT Pentesting Guide"**](https://www.iotpentestingguide.com) (Aditya Gupta)
* [**"IoT Penetration Testing Cookbook"**](https://www.packtpub.com/product/iot-penetration-testing-cookbook/9781787280571) (Aaron Guzman ve Aditya Gupta)
* [**"The IoT Hacker's Handbook"**](https://link.springer.com/book/10.1007/978-1-4842-4300-8) (Aditya Gupta)
* [**"Practical IoT Hacking"**](https://nostarch.com/practical-iot-hacking) (Fotios Chantzis, Ioannis Stais, Paulino Calderon, Evangelos Deirmentzoglou ve Beau Woods)
* Diğer kaynaklar ilgili test senaryolarında belirtilmiştir.
