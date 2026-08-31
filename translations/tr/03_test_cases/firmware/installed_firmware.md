# 3.3.1. Yüklü Bellenim (ISTG-FW[INST])

## İçindekiler
* [Genel Bakış](#genel-bakış)
* [Yetkilendirme (ISTG-FW[INST]-AUTHZ)](#yetkilendirme-istg-fwinst-authz)
  * [Bellenime Yetkisiz Erişim (ISTG-FW[INST]-AUTHZ-001)](#bellenime-yetkisiz-erişim-istg-fwinst-authz-001)
  * [Yetki Yükseltme (ISTG-FW[INST]-AUTHZ-002)](#yetki-yükseltme-istg-fwinst-authz-002)
* [Bilgi Toplama (ISTG-FW[INST]-INFO)](#bilgi-toplama-istg-fwinst-info)
  * [Kullanıcı Verilerinin Açığa Çıkması (ISTG-FW[INST]-INFO-001)](#kullanıcı-verilerinin-açığa-çıkması-istg-fwinst-info-001)
* [Kriptografi (ISTG-FW[INST]-CRYPT)](#kriptografi-istg-fwinst-crypt)
  * [Bootloader İmzasının Yetersiz Doğrulanması (ISTG-FW[INST]-CRYPT-001)](#bootloader-imzasının-yetersiz-doğrulanması-istg-fwinst-crypt-001)

## Genel Bakış

Bellenim bileşeninin uzmanlaşmalarından biri, dinamik analizin konusu olabilen yüklü bellenim (installed firmware) formudur. Dinamik analiz, çalışma zamanı (runtime) sırasında verilerin nasıl işlendiğinin test edilmesine olanak tanır. Bu sayede kullanıcı verilerinin işlenmesi ve saklanması da analiz edilebilir. Dinamik analizin bir ön koşulu olarak, hedef bellenim sürümünü çalıştıran bir cihaz sağlanmalıdır.

## Yetkilendirme (ISTG-FW[INST]-AUTHZ)

Genellikle çalışma zamanı sırasında cihaz bellenimine yalnızca yöneticiler gibi belirli bireylerin erişmesine izin verilmelidir. Bu nedenle, yalnızca yetkili kullanıcıların bellenime erişebilmesini sağlayan uygun kimlik doğrulama (authentication) ve yetkilendirme (authorization) prosedürlerinin mevcut olması gerekir.

### Bellenime Yetkisiz Erişim (ISTG-FW[INST]-AUTHZ-001)

**Gerekli Erişim Seviyeleri**

<table width="100%">
	<tr valign="top">
		<th width="1%" align="left">Fiziksel</th>
 <td><i>PA-1</i> - <i>PA-4</i><br>(bellenime nasıl erişilebildiğine bağlı olarak; örn. dahili/fiziksel hata ayıklama arayüzü veya uzaktan SSH ile)</td>
	</tr>
	<tr valign="top">
		<th align="left">Yetkilendirme</th>
		<td><i>AA-1</i></td>
	</tr>
</table>

**Özet**

Belirli bir cihazın özel uygulamasına bağlı olarak, bellenime veya işlevlerine erişim belirli bir yetkilendirme erişim seviyesine (örn. *AA-2*, *AA-3* veya *AA-4*) sahip bireylerle sınırlandırılmış olabilir. Cihaz bellenimi erişim izinlerini doğru bir şekilde doğrulayamazsa, herhangi bir saldırgan (*AA-1*) bellenime erişim elde edebilir.

**Test Hedefleri**

- Bellenime erişim için yetkilendirme kontrollerinin uygulanıp uygulanmadığı kontrol edilmelidir.
- Yetkilendirme kontrollerinin mevcut olması durumunda, bunları atlatmanın bir yolu olup olmadığı belirlenmelidir.

**İyileştirme / Çözüm**

Bellenime erişimin yalnızca yetkili bireyler için mümkün olmasını sağlayan uygun yetkilendirme kontrolleri uygulanmalıdır.

**Kaynaklar**

Bu test senaryosu için aşağıdaki kaynaklardan veriler birleştirilmiştir:

* OWASP ["Firmware Security Testing Methodology"][owasp_fstm]
* ["IoT Penetration Testing Cookbook"][iot_penetration_testing_cookbook] (Aaron Guzman, Aditya Gupta)
* ["The IoT Hacker's Handbook"][iot_hackers_handbook] (Aditya Gupta)
* ["Practical IoT Hacking"][practical_iot_hacking] (Fotios Chantzis, Ioannis Stais, Paulino Calderon, Evangelos Deirmentzoglou, Beau Woods)
* T-Systems Multimedia Solutions GmbH test standartları

Bu test senaryosu şuna dayanmaktadır: [ISTG-DES-AUTHZ-001](../data_exchange_services/README.md#unauthorized-access-to-the-data-exchange-service-istg-des-authz-001).

### Yetki Yükseltme (ISTG-FW[INST]-AUTHZ-002)

**Gerekli Erişim Seviyeleri**

<table width="100%">
	<tr valign="top">
		<th width="1%" align="left">Fiziksel</th>
 <td><i>PA-1</i> - <i>PA-4</i><br>(bellenime nasıl erişilebildiğine bağlı olarak; örn. dahili/fiziksel hata ayıklama arayüzü veya uzaktan SSH ile)</td>
	</tr>
	<tr valign="top">
		<th align="left">Yetkilendirme</th>
		<td><i>AA-1</i> - <i>AA-3</i><br>(belirli cihazın erişim modeline bağlı olarak)</td>
	</tr>
</table>

**Özet**

Belirli bir cihazın özel uygulamasına bağlı olarak, bellenimin bazı bölümlerine veya işlevlerine erişim belirli bir yetkilendirme erişim seviyesine (örn. *AA-3* veya *AA-4*) sahip bireylerle sınırlandırılmış olabilir. Cihaz bellenimi erişim izinlerini doğru bir şekilde doğrulayamazsa, hedeflenenden daha düşük bir yetkilendirme erişim seviyesine sahip bir saldırgan kısıtlı bellenim bölümlerine erişim elde edebilir.

**Test Hedefleri**

- *ISTG-FW-AUTHZ-001* temelinde, verilen erişim ayrıcalıklarını yükseltmenin ve böylece bellenimin kısıtlı işlevlerine veya bölümlerine erişmenin bir yolu olup olmadığı belirlenmelidir.

**İyileştirme / Çözüm**

Bellenimin kısıtlı bölümlerine erişimin yalnızca gerekli yetkilendirme erişim seviyelerine sahip bireyler için mümkün olmasını sağlayan uygun yetkilendirme kontrolleri uygulanmalıdır.

**Kaynaklar**

Bu test senaryosu şuna dayanmaktadır: [ISTG-DES-AUTHZ-002](../data_exchange_services/README.md#privilege-escalation-istg-des-authz-002).

* OWASP [IoT Security Verification Standard (ISVS)](https://owasp.org/IoT-Security-Verification-Standard-ISVS/) — İlgili gereksinimler: V2.2.2 (en az ayrıcalık / least privilege — root olarak çalışan uygulama ve servisleri sınırlandırın); V3.3.3 (yükseltilmiş erişime ihtiyaç duyan süreçler için minimal çekirdek yetenekleri)

## Bilgi Toplama (ISTG-FW[INST]-INFO)

Yukarıda belirtildiği gibi, dinamik analiz sırasında çalışma zamanı (runtime) boyunca kullanıcı verilerinin cihazda güvenli bir şekilde saklanıp saklanmadığını test etmek de mümkündür.

### Kullanıcı Verilerinin Açığa Çıkması (ISTG-FW[INST]-INFO-001)

**Gerekli Erişim Seviyeleri**

<table width="100%">
	<tr valign="top">
		<th width="1%" align="left">Fiziksel</th>
 <td><i>PA-1</i> - <i>PA-4</i><br>(bellenime nasıl erişilebildiğine bağlı olarak; örn. dahili/fiziksel hata ayıklama arayüzü veya uzaktan SSH ile)</td>
	</tr>
	<tr valign="top">
		<th align="left">Yetkilendirme</th>
		<td><i>AA-1</i> - <i>AA-4</i><br>(belirli cihazın erişim modeline bağlı olarak)</td>
	</tr>
</table>

**Özet**

Çalışma zamanı boyunca bir cihaz, kullanıcılarının kişisel verileri gibi farklı türlerde veriler toplar ve işler. Bu veriler güvenli bir şekilde saklanmazsa, bir saldırgan bunları cihazdan kurtarabilir.

**Test Hedefleri**

- Kullanıcı verilerine yetkisiz kişilerce erişilip erişilemeyeceği kontrol edilmelidir.

**İyileştirme / Çözüm**

Kullanıcı verilerine erişim yalnızca erişmesi gereken bireylere ve süreçlere verilmelidir. Yetkisiz veya düzgün yetkilendirilmemiş hiçbir birey kullanıcı verilerini geri getirememelidir.

**Kaynaklar**

Bu test senaryosu için aşağıdaki kaynaklardan veriler birleştirilmiştir:

* OWASP ["Firmware Security Testing Methodology"][owasp_fstm]
* ["IoT Penetration Testing Cookbook"][iot_penetration_testing_cookbook] (Aaron Guzman, Aditya Gupta)
* ["The IoT Hacker's Handbook"][iot_hackers_handbook] (Aditya Gupta)
* ["Practical IoT Hacking"][practical_iot_hacking] (Fotios Chantzis, Ioannis Stais, Paulino Calderon, Evangelos Deirmentzoglou, Beau Woods)
* T-Systems Multimedia Solutions GmbH test standartları

## Kriptografi (ISTG-FW[INST]-CRYPT)

Birçok IoT cihazının hassas verileri güvenli bir şekilde saklamak, kimlik doğrulama amacıyla veya diğer ağ düğümlerinden gelen şifreli verileri alıp doğrulamak için kriptografik algoritmalar uygulaması gerekir. Güvenli ve güncel standartlara uygun kriptografinin uygulanamaması; hassas verilerin ifşasına, cihaz arızalarına veya cihaz üzerindeki kontrolün kaybedilmesine yol açabilir.

### Bootloader İmzasının Yetersiz Doğrulanması (ISTG-FW[INST]-CRYPT-001)

**Gerekli Erişim Seviyeleri**

<table width="100%">
	<tr valign="top">
		<th width="1%" align="left">Fiziksel</th>
 <td><i>PA-1</i> - <i>PA-4</i><br>(bellenime nasıl erişilebildiğine bağlı olarak; örn. dahili/fiziksel hata ayıklama arayüzü veya uzaktan SSH ile)</td>
	</tr>
	<tr valign="top">
		<th align="left">Yetkilendirme</th>
		<td><i>AA-1</i> - <i>AA-4</i><br>(belirli cihazın erişim modeline bağlı olarak)</td>
	</tr>
</table>

**Özet**

Bootloader'ın (ön yükleyici) dijital imzasının doğrulanması; bootloader üzerindeki manipülasyonları tespit etmek ve böylece cihazda manipüle edilmiş bir bellenimin yürütülmesini engellemek (Secure Boot) için kritik bir önlemdir.

**Test Hedefleri**

- Önyükleme (boot) işlemi sırasında bootloader imzasının cihaz tarafından düzgün bir şekilde doğrulanıp doğrulanmadığı kontrol edilmelidir.

**İyileştirme / Çözüm**

Cihaz, bir bootloader'ı yürütmeden önce dijital imzasını düzgün bir şekilde doğrulamalıdır. Geçerli bir imzası olmayan bir bootloader asla çalıştırılmamalıdır.

**Kaynaklar**

* OWASP [IoT Security Verification Standard (ISVS)](https://owasp.org/IoT-Security-Verification-Standard-ISVS/) — İlgili gereksinimler: V3.1.4 (ilk aşama bootloader orijinalliği, değiştirilemez bir ROM tabanlı Root of Trust / Güven Kökü tarafından doğrulanır); V3.1.5 (önyükleme aşamaları yürütülmeden önce kriptografik olarak doğrulanır)

[owasp_fstm]: https://github.com/scriptingxss/owasp-fstm "OWASP Firmware Security Testing Methodology"
[iot_penetration_testing_cookbook]: https://www.packtpub.com/product/iot-penetration-testing-cookbook/9781787280571 "IoT Penetration Testing Cookbook"
[iot_hackers_handbook]: https://link.springer.com/book/10.1007/978-1-4842-4300-8 "The IoT Hacker's Handbook"
[practical_iot_hacking]: https://nostarch.com/practical-iot-hacking "Practical IoT Hacking"
