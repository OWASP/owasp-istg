# 3.3.2. Bellenim Güncelleme Mekanizması (ISTG-FW[UPDT])

## İçindekiler
* [Genel Bakış](#genel-bakış)
* [Yetkilendirme (ISTG-FW[UPDT]-AUTHZ)](#yetkilendirme-istg-fwupdt-authz)
  * [Yetkisiz Bellenim Güncellemesi (ISTG-FW[UPDT]-AUTHZ-001)](#yetkisiz-bellenim-güncellemesi-istg-fwupdt-authz-001)
* [Kriptografi (ISTG-FW[UPDT]-CRYPT)](#kriptografi-istg-fwupdt-crypt)
  * [Yetersiz Bellenim Güncelleme İmzası (ISTG-FW[UPDT]-CRYPT-001)](#yetersiz-bellenim-güncelleme-imzası-istg-fwupdt-crypt-001)
  * [Yetersiz Bellenim Güncelleme Şifrelemesi (ISTG-FW[UPDT]-CRYPT-002)](#yetersiz-bellenim-güncelleme-şifrelemesi-istg-fwupdt-crypt-002)
  * [Bellenim Güncellemesinin Güvensiz İletimi (ISTG-FW[UPDT]-CRYPT-003)](#bellenim-güncellemesinin-güvensiz-iletimi-istg-fwupdt-crypt-003)
  * [Bellenim Güncelleme İmzasının Yetersiz Doğrulanması (ISTG-FW[UPDT]-CRYPT-004)](#bellenim-güncelleme-imzasının-yetersiz-doğrulanması-istg-fwupdt-crypt-004)
* [İş Mantığı (ISTG-FW[UPDT]-LOGIC)](#iş-mantığı-istg-fwupdt-logic)
  * [Yetersiz Geri Alma / Sürüm Düşürme Koruması (Anti-Rollback) (ISTG-FW[UPDT]-LOGIC-001)](#yetersiz-geri-alma--sürüm-düşürme-koruması-anti-rollback-istg-fwupdt-logic-001)

## Genel Bakış

Cihaz belleniminin bir diğer kritik yönü, bellenim güncelleme mekanizmasıdır (firmware update mechanism / OTA). Güvenli bir güncelleme mekanizmasının uygulanamaması; saldırganların cihaza özel, manipüle edilmiş bir bellenim yüklemesine ve böylece cihaz üzerinde tam kontrol elde etmesine olanak tanıyabilir.

Aşağıdaki kategoriler [ISTG-FW[UPDT]](./firmware_update_mechanism.md) uzmanlaşması tarafından miras alınmaz:

- **Yapılandırma ve Yama Yönetimi ([ISTG-FW-CONF](./README.md#yapılandırma-ve-yama-yönetimi-istg-fw-conf))**: Bu kategori, bir bellenim dosyasının yapılandırma ve yama yönetimi yönlerine odaklanır. [ISTG-FW[UPDT]](./firmware_update_mechanism.md) belirli bir bellenim dosyasından ziyade bellenim güncelleme mekanizmasına odaklandığından, ilgili test senaryoları burada geçerli değildir.
- **Gizli Bilgiler ([ISTG-FW-SCRT](./README.md#gizli-bilgiler--secrets-istg-fw-scrt))**: Bu kategori, bir bellenim dosyası içindeki sırların işlenmesine odaklanır. [ISTG-FW[UPDT]](./firmware_update_mechanism.md) belirli bir bellenim dosyasından ziyade bellenim güncelleme mekanizmasına odaklandığından, ilgili test senaryoları burada geçerli değildir.

## Yetkilendirme (ISTG-FW[UPDT]-AUTHZ)

Bellenim güncelleme mekanizmasının testi de dinamik bir analiz olduğundan, yalnızca yetkili bireylerin bir güncellemeyi başlatıp gerçekleştirebildiğini kontrol etmek mümkündür.

### Yetkisiz Bellenim Güncellemesi (ISTG-FW[UPDT]-AUTHZ-001)

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

Belirli bir cihazın özel uygulamasına bağlı olarak, bellenim güncellemelerini gerçekleştirme izni belirli bir yetkilendirme erişim seviyesine (örn. *AA-2*, *AA-3* veya *AA-4*) sahip bireylerle sınırlandırılmış olabilir. Cihaz bellenimi bu izinleri doğru bir şekilde doğrulayamazsa, herhangi bir saldırgan (*AA-1*) veya hedeflenenden daha düşük yetkilendirme erişim seviyesine sahip bir saldırgan istenmeyen bellenim güncellemeleri gerçekleştirebilir.

**Test Hedefleri**

- Bellenim güncellemesi gerçekleştirmek için yetkilendirme kontrollerinin uygulanıp uygulanmadığı kontrol edilmelidir.
- Yetkilendirme kontrollerinin mevcut olması durumunda, bunları atlatmanın bir yolu olup olmadığı belirlenmelidir.

**İyileştirme / Çözüm**

Bellenim güncellemesinin yalnızca belirli yetkilendirme erişim seviyelerine sahip bireyler tarafından gerçekleştirilebilmesini sağlayan uygun yetkilendirme kontrolleri uygulanmalıdır.

**Kaynaklar**

Bu test senaryosu için aşağıdaki kaynaklardan veriler birleştirilmiştir:

* OWASP ["Firmware Security Testing Methodology"][owasp_fstm]
* T-Systems Multimedia Solutions GmbH test standartları
* OWASP [IoT Security Verification Standard (ISVS)](https://owasp.org/IoT-Security-Verification-Standard-ISVS/) — İlgili gereksinimler: V3.4.10 (cihaz bir güncellemeyi indirmeden önce güncelleme sunucusuna kimlik doğrulaması yapar)

## Kriptografi (ISTG-FW[UPDT]-CRYPT)

Bellenim güncelleme süreci sırasında, yeni bellenimin bütünlüğünü doğrulamak ve iletim sırasında hiçbir hassas verinin açığa çıkmamasını sağlamak için kriptografik algoritmalar kullanılır.

### Yetersiz Bellenim Güncelleme İmzası (ISTG-FW[UPDT]-CRYPT-001)

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

Bir cihazı manipüle etmenin yollarından biri manipüle edilmiş bir bellenim paketi yüklemektir. Değişikliklerin tespit edilmesini sağlamak için bellenim güncelleme paketinin dijital olarak imzalanması gerekir. Bu sayede kurulum veya güncelleme işlemi sırasında paketin geçerliliği doğrulanabilir.

**Test Hedefleri**

- Bellenim güncelleme paketi için bir dijital imzanın mevcut olup olmadığı belirlenmelidir.
- Bir dijital imza mevcutsa, imzanın geçerliliğinin doğrulanıp doğrulanamayacağı kontrol edilmelidir.
- [ISTG-FW-CRYPT-001](./README.md#zayıf-kriptografik-algoritmaların-kullanımı-istg-fw-crypt-001) temelinde, dijital imzayı oluşturmak için kullanılan kriptografik algoritma değerlendirilmeli ve zayıf ya da güncel olmayan bir algoritmanın kullanılıp kullanılmadığı belirlenmelidir.

**İyileştirme / Çözüm**

Bellenim güncelleme paketi için geçerli bir dijital imza mevcut olmalıdır. Ayrıca dijital imzanın geçerliliğini doğrulamak teknik olarak mümkün olmalıdır.

**Kaynaklar**

Bu test senaryosu için aşağıdaki kaynaklardan veriler birleştirilmiştir:

* OWASP ["Firmware Security Testing Methodology"][owasp_fstm]
* ["IoT Penetration Testing Cookbook"][iot_penetration_testing_cookbook] (Aaron Guzman, Aditya Gupta)
* ["Practical IoT Hacking"][practical_iot_hacking] (Fotios Chantzis, Ioannis Stais, Paulino Calderon, Evangelos Deirmentzoglou, Beau Woods)
* T-Systems Multimedia Solutions GmbH test standartları
* OWASP [IoT Security Verification Standard (ISVS)](https://owasp.org/IoT-Security-Verification-Standard-ISVS/) — İlgili gereksinimler: V2.4.2 (yeterli anahtar boyutlarına sahip güçlü, standart kriptografik algoritmaların doğru kullanımı); V3.4.13 (2030 sonrasında çalışan cihazlar için kuantum sonrası veya hibrit güncelleme imzaları)

### Yetersiz Bellenim Güncelleme Şifrelemesi (ISTG-FW[UPDT]-CRYPT-002)

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

Bellenim güncelleme paketleri, yazılım ve donanım geliştiricisinin fikri mülkiyet (intellectual property) gibi gizli verilerini içerebilir. Bu nedenle paketin kendisinin şifrelenmesi gerekebilir.

**Test Hedefleri**

- Bellenim güncelleme paketinin şifrelenmesi gerekip gerekmediği bellenim geliştiricisiyle netleştirilmelidir.
- Şifreleme gerekiyorsa paketin şifrelenip şifrelenmediği belirlenmelidir.
- [ISTG-FW-CRYPT-001](./README.md#zayıf-kriptografik-algoritmaların-kullanımı-istg-fw-crypt-001) temelinde, şifreleme için uygun algoritmaların kullanılıp kullanılmadığı belirlenmelidir.

**İyileştirme / Çözüm**

Bellenim güncelleme paketi, güncel standartlara uygun kriptografik algoritmalar kullanılarak şifrelenmelidir.

**Kaynaklar**

Bu test senaryosu için aşağıdaki kaynaklardan veriler birleştirilmiştir:

* OWASP ["Firmware Security Testing Methodology"][owasp_fstm]
* ["IoT Pentesting Guide"][iot_pentesting_guide] (Aditya Gupta)
* ["IoT Penetration Testing Cookbook"][iot_penetration_testing_cookbook] (Aaron Guzman, Aditya Gupta)
* ["The IoT Hacker's Handbook"][iot_hackers_handbook] (Aditya Gupta)
* ["Practical IoT Hacking"][practical_iot_hacking] (Fotios Chantzis, Ioannis Stais, Paulino Calderon, Evangelos Deirmentzoglou, Beau Woods)
* T-Systems Multimedia Solutions GmbH test standartları

### Bellenim Güncellemesinin Güvensiz İletimi (ISTG-FW[UPDT]-CRYPT-003)

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

Bellenim güncelleme süreci güvenli bir kanal (secure channel) üzerinden gerçekleştirilmezse veya iletilen verilerin gizliliğini sağlamak ve değişiklikleri tespit etmek için ek önlemler alınmazsa, iletişim kanalına erişimi olan bir saldırgan güncelleme sürecine müdahale edebilir (MitM).

**Test Hedefleri**

- Bellenim güncellemesinin güvenli bir kanal üzerinden gerçekleştirilip gerçekleştirilmediği belirlenmelidir.
- Bellenim güncellemesi internet gibi güvensiz bir kanal üzerinden gerçekleştiriliyorsa gizlilik ve bütünlük açısından uygun önlemlerin alınıp alınmadığı kontrol edilmelidir.
- Örneğin iletişim kanalı TLS kullanılarak güvenceye alınmışsa hangi şifre paketlerinin (cipher suites) desteklendiği ve sunucu sertifikasının istemci tarafından doğrulanıp doğrulanmadığı kontrol edilmelidir.

**İyileştirme / Çözüm**

Mümkünse bellenim güncellemesi güvenli bir kanal üzerinden gerçekleştirilmelidir. Aksi takdirde, potansiyel saldırganların müdahalelerini önlemek veya tespit etmek için uygun koruma önlemleri uygulanmalıdır.

**Kaynaklar**

Bu test senaryosu için aşağıdaki kaynaklardan veriler birleştirilmiştir:

* OWASP ["Firmware Security Testing Methodology"][owasp_fstm]
* ["IoT Penetration Testing Cookbook"][iot_penetration_testing_cookbook] (Aaron Guzman, Aditya Gupta)
* ["Practical IoT Hacking"][practical_iot_hacking] (Fotios Chantzis, Ioannis Stais, Paulino Calderon, Evangelos Deirmentzoglou, Beau Woods)
* T-Systems Multimedia Solutions GmbH test standartları
* OWASP [IoT Security Verification Standard (ISVS)](https://owasp.org/IoT-Security-Verification-Standard-ISVS/) — İlgili gereksinimler: V3.4.12 (güncellemeler şifreli bir kanal üzerinden iletilir); V4.1.2 (yalnızca güçlü TLS cipher suite'leri etkindir); V4.1.3 (cihaz X.509 sertifikasını kriptografik olarak doğrular)

### Bellenim Güncelleme İmzasının Yetersiz Doğrulanması (ISTG-FW[UPDT]-CRYPT-004)

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

Bellenim güncelleme paketi dijital olarak imzalanmış olsa bile, dijital imzanın düzgün bir şekilde doğrulanmaması durumunda bir saldırgan cihaza manipüle edilmiş bir bellenim paketi yükleyebilir. Örneğin, imza sağlanmadığında cihaz güncellemeyi reddetmeyebilir.

**Test Hedefleri**

- [ISTG-FW-CRYPT-001](./README.md#zayıf-kriptografik-algoritmaların-kullanımı-istg-fw-crypt-001) temelinde, güncelleme işlemi sırasında bellenim güncelleme paketinin imzasının cihaz tarafından düzgün bir şekilde doğrulanıp doğrulanmadığı kontrol edilmelidir.

**İyileştirme / Çözüm**

Cihaz, kurulum süreci başlatılmadan önce bir güncelleme paketinin dijital imzasını düzgün bir şekilde doğrulamalıdır. Geçerli bir imzası olmayan veya hiç imzası bulunmayan tüm güncelleme paketleri doğrudan reddedilmelidir.

**Kaynaklar**

Bu test senaryosu için aşağıdaki kaynaklardan veriler birleştirilmiştir:

* OWASP ["Firmware Security Testing Methodology"][owasp_fstm]
* ["IoT Penetration Testing Cookbook"][iot_penetration_testing_cookbook] (Aaron Guzman, Aditya Gupta)
* ["Practical IoT Hacking"][practical_iot_hacking] (Fotios Chantzis, Ioannis Stais, Paulino Calderon, Evangelos Deirmentzoglou, Beau Woods)
* T-Systems Multimedia Solutions GmbH test standartları
* OWASP [IoT Security Verification Standard (ISVS)](https://owasp.org/IoT-Security-Verification-Standard-ISVS/) — İlgili gereksinimler: V3.4.3 (güncellemeler güvenilir bir kaynak tarafından imzalanır ve yürütülmeden önce doğrulanır)

## İş Mantığı (ISTG-FW[UPDT]-LOGIC)

Bellenim güncellemesinin diğer tüm yönleri güvenli bir şekilde uygulanmış olsa bile güncelleme sürecinin temel mantığındaki sorunlar cihazı saldırılara karşı savunmasız hale getirebilir. Bu nedenle sürecin amaçlandığı gibi çalışıp çalışmadığı ve istisnaların tespit edilip düzgün bir şekilde yönetilip yönetilmediği doğrulanmalıdır.

### Yetersiz Geri Alma / Sürüm Düşürme Koruması (Anti-Rollback) (ISTG-FW[UPDT]-LOGIC-001)

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

Bazı üreticiler cihazları için geri alma/sürüm düşürme koruması (anti-rollback protection) uygular. Bu koruma, bir cihaz belleniminin halihazırda yüklü olan sürümden daha eski bir sürüme güncellenmesini (downgrade) engeller. Bu sayede bir saldırgan, o sürümün bilinen güvenlik açıklarını istismar etmek amacıyla geçerli ancak güncel olmayan eski bir bellenimi cihaza yükleyemez.

**Test Hedefleri**

- Bellenimin eski sürümlerinin yüklenmesinin mümkün olup olmadığı değerlendirilmelidir.

**İyileştirme / Çözüm**

Yüklenecek bellenim sürümünün halihazırda yüklü olan sürümden daha yeni olduğunu doğrulayan uygun bir geri alma/sürüm düşürme koruma mekanizması (anti-rollback mechanism) uygulanmalıdır.

**Kaynaklar**

Bu test senaryosu için aşağıdaki kaynaklardan veriler birleştirilmiştir:

* ["IoT Penetration Testing Cookbook"][iot_penetration_testing_cookbook] (Aaron Guzman, Aditya Gupta)
* T-Systems Multimedia Solutions GmbH test standartları
* OWASP [IoT Security Verification Standard (ISVS)](https://owasp.org/IoT-Security-Verification-Standard-ISVS/) — İlgili gereksinimler: V3.4.6 (cihazın bilinen güvenlik açıklarına sahip eski sürümlere düşürülmesinin engellenmesi — anti-rollback)

[owasp_fstm]: https://github.com/scriptingxss/owasp-fstm "OWASP Firmware Security Testing Methodology"
[iot_pentesting_guide]: https://www.iotpentestingguide.com "IoT Pentesting Guide"
[iot_penetration_testing_cookbook]: https://www.packtpub.com/product/iot-penetration-testing-cookbook/9781787280571 "IoT Penetration Testing Cookbook"
[iot_hackers_handbook]: https://link.springer.com/book/10.1007/978-1-4842-4300-8 "The IoT Hacker's Handbook"
[practical_iot_hacking]: https://nostarch.com/practical-iot-hacking "Practical IoT Hacking"
