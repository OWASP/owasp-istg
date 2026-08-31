# 3.1. İşlem Birimleri (ISTG-PROC)

## İçindekiler
* [Genel Bakış](#genel-bakış)
* [Yetkilendirme (ISTG-PROC-AUTHZ)](#yetkilendirme-istg-proc-authz)
  * [İşlem Birimine Yetkisiz Erişim (ISTG-PROC-AUTHZ-001)](#işlem-birimine-yetkisiz-erişim-istg-proc-authz-001)
  * [Yetki Yükseltme (ISTG-PROC-AUTHZ-002)](#yetki-yükseltme-istg-proc-authz-002)
* [İş Mantığı (ISTG-PROC-LOGIC)](#iş-mantığı-istg-proc-logic)
  * [Komutların Güvensiz Uygulanması (ISTG-PROC-LOGIC-001)](#komutların-güvensiz-uygulanması-istg-proc-logic-001)
* [Yan Kanal Saldırıları (ISTG-PROC-SIDEC)](#yan-kanal-saldırıları-istg-proc-sidec)
  * [Yan Kanal Saldırılarına Karşı Yetersiz Koruma (ISTG-PROC-SIDEC-001)](#yan-kanal-saldırılarına-karşı-yetersiz-koruma-istg-proc-sidec-001)

## Genel Bakış

Bu bölüm, işlem birimi (processing unit) bileşenine yönelik test senaryolarını ve kategorilerini içerir. İşlem birimi, yalnızca *PA-4* (invaziv fiziksel erişim) ile erişilebilen bir cihaz içi öğedir. İşlem birimi ile doğrudan bağlantı kurmak özel donanım ekipmanları (örn. bir hata ayıklama kartı, osiloskop veya test probları) gerektirebilir.

İşlem birimleri için geçerli olan aşağıdaki test senaryosu kategorileri belirlenmiştir:

- **Yetkilendirme (Authorization):** İşlem birimine yetkisiz erişim elde edilmesine veya kısıtlı işlevlere erişmek için yetkilerin yükseltilmesine olanak tanıyan güvenlik açıklarına odaklanır.
- **İş Mantığı (Business Logic):** Komutların tasarımı ve uygulanmasındaki zafiyetlerin yanı sıra belgelenmemiş, potansiyel olarak savunmasız komutların varlığına odaklanır.
- **Yan Kanal Saldırıları (Side-channel Attacks):** Zamanlama (timing) ve voltaj/saat sıçraması (glitching) gibi yan kanal saldırılarına karşı dirence odaklanır.

## Yetkilendirme (ISTG-PROC-AUTHZ)

Belirli bir cihazın erişim modeline bağlı olarak, yalnızca belirli bireylerin bir işlem birimine doğrudan erişmesine izin verilebilir. Bu nedenle, yalnızca yetkili varlıkların erişim elde edebilmesini sağlayan uygun kimlik doğrulama ve yetkilendirme prosedürlerinin mevcut olması gerekir.

### İşlem Birimine Yetkisiz Erişim (ISTG-PROC-AUTHZ-001)

**Gerekli Erişim Seviyeleri**

<table width="100%">
	<tr valign="top">
		<th width="1%" align="left">Fiziksel</th>
		<td><i>PA-4</i></td>
	</tr>
	<tr valign="top">
		<th align="left">Yetkilendirme</th>
		<td><i>AA-1</i></td>
	</tr>
</table>

**Özet**

Belirli bir cihazın özel uygulamasına bağlı olarak, bir işlem birimine erişim belirli bir yetkilendirme erişim seviyesine (örn. *AA-2*, *AA-3* veya *AA-4*) sahip varlıklarla sınırlandırılmış olabilir. Cihaz erişim izinlerini doğru bir şekilde doğrulayamazsa, herhangi bir saldırgan (*AA-1*) erişim elde edebilir.

**Test Hedefleri**

- İşlem birimine erişim için yetkilendirme kontrollerinin uygulanıp uygulanmadığı kontrol edilmelidir.
- Yetkilendirme kontrollerinin mevcut olması durumunda, bunları atlatmanın bir yolu olup olmadığı belirlenmelidir.

**İyileştirme / Çözüm**

İşlem birimine erişimin yalnızca yetkili varlıklar için mümkün olmasını sağlayan uygun yetkilendirme kontrolleri uygulanmalıdır.

**Kaynaklar**

Bu test senaryosu şuna dayanmaktadır: [ISTG-DES-AUTHZ-001](../data_exchange_services/README.md#unauthorized-access-to-the-data-exchange-service-istg-des-authz-001).

### Yetki Yükseltme (ISTG-PROC-AUTHZ-002)

**Gerekli Erişim Seviyeleri**

<table width="100%">
	<tr valign="top">
		<th width="1%" align="left">Fiziksel</th>
		<td><i>PA-4</i></td>
	</tr>
	<tr valign="top">
		<th align="left">Yetkilendirme</th>
		<td><i>AA-2</i> - <i>AA-3</i><br>(belirli cihazın erişim modeline bağlı olarak)</td>
	</tr>
</table>

**Özet**

Belirli bir cihazın özel uygulamasına bağlı olarak, bir işlem biriminin bazı işlevlerine erişim belirli bir yetkilendirme erişim seviyesine (örn. *AA-3* veya *AA-4*) sahip bireylerle sınırlandırılmış olabilir. İşlem birimi erişim izinlerini doğru bir şekilde doğrulayamazsa, hedeflenenden daha düşük bir yetkilendirme erişim seviyesine sahip bir saldırgan kısıtlı işlevlere erişim elde edebilir.

**Test Hedefleri**

- [ISTG-PROC-AUTHZ-001](#işlem-birimine-yetkisiz-erişim-istg-proc-authz-001) temelinde, verilen erişim ayrıcalıklarını yükseltmenin ve böylece kısıtlı işlevlere erişmenin bir yolu olup olmadığı belirlenmelidir.

**İyileştirme / Çözüm**

Kısıtlı işlevlere erişimin yalnızca gerekli yetkilendirme erişim seviyelerine sahip bireyler için mümkün olmasını sağlayan uygun yetkilendirme kontrolleri uygulanmalıdır.

**Kaynaklar**

Bu test senaryosu şuna dayanmaktadır: [ISTG-DES-AUTHZ-002](../data_exchange_services/README.md#privilege-escalation-istg-des-authz-002).

## İş Mantığı (ISTG-PROC-LOGIC)

Bir işlem biriminin temel mantığındaki sorunlar cihazı saldırılara karşı savunmasız hale getirebilir. Bu nedenle, işlem biriminin ve işlevlerinin amaçlandığı gibi çalışıp çalışmadığı ve istisnaların (exceptions) tespit edilip uygun şekilde ele alınıp alınmadığı doğrulanmalıdır.

### Komutların Güvensiz Uygulanması (ISTG-PROC-LOGIC-001)

**Gerekli Erişim Seviyeleri**

<table width="100%">
	<tr valign="top">
		<th width="1%" align="left">Fiziksel</th>
		<td><i>PA-4</i></td>
	</tr>
	<tr valign="top">
		<th align="left">Yetkilendirme</th>
		<td><i>AA-1</i> - <i>AA-4</i><br>(işlem birimine komutları başarıyla göndermek için hangi düzeyde ayrıcalık gerektiğine bağlı olarak)</td>
	</tr>
</table>

**Özet**

İş mantığının uygulanmasındaki kusurlar, cihazın istenmeyen davranışlarına veya arızalanmasına neden olabilir. Örneğin, bir saldırgan işlem iş akışındaki önemli komutları kasıtlı olarak atlamaya veya değiştirmeye çalışırsa, cihaz bilinmeyen ve potansiyel olarak güvensiz bir durumda kalabilir.

**Test Hedefleri**

- Özel uygulamaya bağlı olarak, komutların cihazın davranışını manipüle etmek için kötüye kullanılıp kullanılamayacağı belirlenmelidir.
- Kullanımdaki işlem biriminin belgelenmemiş, potansiyel olarak savunmasız komutları destekleyip desteklemediği kontrol edilmelidir. Örneğin bu kontrol, komut fuzzing'i (fuzzing instructions) yapılarak veya işlem birimi modeliyle ilgili araştırmalar gerçekleştirilerek yapılabilir.

**İyileştirme / Çözüm**

Cihaz bilinmeyen bir durumda kalmamalıdır. İş akışındaki anomaliler tespit edilmeli ve istisnalar (exceptions) uygun şekilde yönetilmelidir.

**Kaynaklar**

Bu test senaryosu şuna dayanmaktadır: [ISTG-DES-LOGIC-001](../data_exchange_services/README.md#circumvention-of-the-intended-business-logic-istg-des-logic-001).

## Yan Kanal Saldırıları (ISTG-PROC-SIDEC)

Zamanlama (timing) ve voltaj/saat sıçraması (glitching) gibi yan kanal saldırıları, genellikle cihaz bellenimi veya arayüzleri yerine cihazın fiziksel uygulamasına (daha spesifik olarak bir işlem birimine) yöneliktir. Bu tür saldırıların amacı; anahtar malzemesini ele geçirmek, kriptografik hesaplamaları manipüle etmek veya korunan bilgilere erişim elde etmek için işlem birimi tarafından gerçekleştirilen kriptografik algoritmalar ve işlemler hakkında bilgi toplamaktır.

### Yan Kanal Saldırılarına Karşı Yetersiz Koruma (ISTG-PROC-SIDEC-001)

**Gerekli Erişim Seviyeleri**

<table width="100%">
	<tr valign="top">
		<th width="1%" align="left">Fiziksel</th>
		<td><i>PA-4</i></td>
	</tr>
	<tr valign="top">
		<th align="left">Yetkilendirme</th>
		<td><i>AA-1</i> - <i>AA-4</i><br>(saldırının nasıl gerçekleştirildiğine bağlı olarak; daha fazla ayrıntı için özete bakınız)</td>
	</tr>
</table>

**Özet**

Yukarıda belirtildiği gibi, yan kanal saldırıları bir saldırgan tarafından hassas verilere erişmek veya cihazın çalışmasını manipüle etmek için kullanılabilir. Genellikle yan kanal saldırıları, belirli bir donanım uygulamasına göre uyarlanmış özel saldırılardır.

Saldırının nasıl gerçekleştirildiğine bağlı olarak farklı yetkilendirme erişim seviyeleri gerekebilir. Voltaj/saat sıçraması (glitching) gibi bazı yan kanal saldırıları, saldırı güç kaynağını veya saat sinyalini manipüle ederek fiziksel düzeyde gerçekleştirildiğinden hiçbir yetkilendirme erişimi gerektirmez. Meltdown zafiyeti gibi diğer yan kanal saldırı vektörleri ise saldırgan tarafından kod yürütülmesini gerektirir; bu nedenle bir tür yetkilendirme erişimi zorunludur.

**Test Hedefleri**

- İşlem biriminin Meltdown ve Spectre gibi bilinen güvenlik açıklarından etkilenip etkilenmediği belirlenmelidir.
- Test süresi boyunca, zamanlama veya sıçrama (glitching) gibi yan kanal saldırılarının başarı olasılığını değerlendirmek için işlem biriminin davranışı analiz edilmelidir.

**İyileştirme / Çözüm**

Analiz sonuçlarına bağlı olarak, donanım tasarımı yan kanal saldırılarına karşı dirençli olacak şekilde ayarlanmalıdır. Ayrıca, kamuya açık bilinen güvenlik açıkları mevcutsa en son yamalar yüklenmelidir.

**Kaynaklar**

Bu test senaryosu için aşağıdaki kaynaklardan veriler birleştirilmiştir:

* ["A practical implementation of the timing attack"][timing_attack] (Jean-François Dhem, François Koeune, Philippe-Alexandre Leroux, Patrick Mestré, Jean-Jacques Quisquater, Jean-Louis Willems)
* ["Injecting Power Attacks with Voltage Glitching and Generation of Clock Attacks for Testing Fault Injection Attacks"][power_glitching_attack] (Shaminder Kaur, Balwinder Singh, Harsimranjit Kaur, Lipika Gupta)
* ["Spectre attacks: Exploiting speculative execution"][spectre_attack] (Paul Kocher, Jann Horn, Anders Fogh, Daniel Genkin, Daniel Gruss, Werner Haas, Mike Hamburg, Moritz Lipp, Stefan Mangard, Thomas Prescher, Michael Schwarz, Yuval Yarom)
* ["Meltdown: Reading kernel memory from user space"][meltdown_attack] (Moritz Lipp, Michael Schwarz, Daniel Gruss, Thomas Prescher, Werner Haas, Anders Fogh, Jann Horn, Stefan Mangard, Paul Kocher, Daniel Genkin, Yuval Yarom, Mike Hamburg)

[timing_attack]: https://link.springer.com/chapter/10.1007/10721064_15 "A practical implementation of the timing attack"
[power_glitching_attack]: https://link.springer.com/chapter/10.1007/978-981-15-7804-5_3 "Injecting Power Attacks with Voltage Glitching and Generation of Clock Attacks for Testing Fault Injection Attacks"
[spectre_attack]: https://ieeexplore.ieee.org/document/8835233 "Spectre attacks: Exploiting speculative execution"
[meltdown_attack]: https://www.usenix.org/conference/usenixsecurity18/presentation/lipp "Meltdown: Reading kernel memory from user"
