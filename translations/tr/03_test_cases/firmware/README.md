# 3.3. Bellenim / Firmware (ISTG-FW)

## İçindekiler
* [Genel Bakış](#genel-bakış)
* [Bilgi Toplama (ISTG-FW-INFO)](#bilgi-toplama-istg-fw-info)
  * [Kaynak Kod ve İkiliklerin (Binaries) Açığa Çıkması (ISTG-FW-INFO-001)](#kaynak-kod-ve-ikiliklerin-binaries-açığa-çıkması-istg-fw-info-001)
  * [Uygulama Ayrıntılarının Açığa Çıkması (ISTG-FW-INFO-002)](#uygulama-ayrıntılarının-açığa-çıkması-istg-fw-info-002)
  * [Ekosistem Ayrıntılarının Açığa Çıkması (ISTG-FW-INFO-003)](#ekosistem-ayrıntılarının-açığa-çıkması-istg-fw-info-003)
  * [Güvensiz İkili Derleme Seçenekleri (ISTG-FW-INFO-004)](#güvensiz-ikili-derleme-seçenekleri-istg-fw-info-004)
* [Yapılandırma ve Yama Yönetimi (ISTG-FW-CONF)](#yapılandırma-ve-yama-yönetimi-istg-fw-conf)
  * [Güncel Olmayan Yazılım Kullanımı (ISTG-FW-CONF-001)](#güncel-olmayan-yazılım-kullanımı-istg-fw-conf-001)
  * [Gereksiz Yazılım ve İşlevlerin Varlığı (ISTG-FW-CONF-002)](#gereksiz-yazılım-ve-işlevlerin-varlığı-istg-fw-conf-002)
* [Gizli Bilgiler / Secrets (ISTG-FW-SCRT)](#gizli-bilgiler--secrets-istg-fw-scrt)
  * [Genel Depolama Alanlarında Saklanan Gizli Bilgiler (ISTG-FW-SCRT-001)](#genel-depolama-alanlarında-saklanan-gizli-bilgiler-istg-fw-scrt-001)
  * [Gizli Bilgilerin Şifrelenmemiş Olarak Saklanması (ISTG-FW-SCRT-002)](#gizli-bilgilerin-şifrelenmemiş-olarak-saklanması-istg-fw-scrt-002)
  * [Sabit Kodlanmış (Hard-coded) Gizli Bilgilerin Kullanımı (ISTG-FW-SCRT-003)](#sabit-kodlanmış-hard-coded-gizli-bilgilerin-kullanımı-istg-fw-scrt-003)
* [Kriptografi (ISTG-FW-CRYPT)](#kriptografi-istg-fw-crypt)
  * [Zayıf Kriptografik Algoritmaların Kullanımı (ISTG-FW-CRYPT-001)](#zayıf-kriptografik-algoritmaların-kullanımı-istg-fw-crypt-001)

## Genel Bakış

Bu bölüm; bellenim (firmware) bileşenine ve ilgili bileşen uzmanlaşmaları olan yüklü bellenim ([ISTG-FW[INST]](./installed_firmware.md)) ve bellenim güncelleme mekanizmasına ([ISTG-FW[UPDT]](./firmware_update_mechanism.md)) yönelik test senaryolarını ve kategorilerini içerir. Bu erişimin ayrıntılı olarak nasıl uygulandığına bağlı olarak bellenime tüm fiziksel erişim seviyeleri (*PA-1* - *PA-4*) ile erişilebilir.

Bellenim için geçerli olan aşağıdaki test senaryosu kategorileri belirlenmiştir:

- **Bilgi Toplama (Information Gathering):** Uygun şekilde korunmadığı veya kaldırılmadığı takdirde bellenim içinde saklanan ve potansiyel saldırganlara ifşa olabilecek bilgilere odaklanır.
- **Yapılandırma ve Yama Yönetimi (Configuration & Patch Management):** Bir bellenimin ve yazılım bileşenlerinin yapılandırmasındaki güvenlik açıklarına ve sorunlarına odaklanır.
- **Gizli Bilgiler (Secrets):** Bellenim içinde güvensiz bir şekilde saklanan anahtar ve kimlik bilgilerine odaklanır.
- **Kriptografi (Cryptography):** Kriptografik uygulamadaki güvenlik açıklarına odaklanır.
- **Yetkilendirme (Authorization - Yüklü Bellenim):** Bellenime yetkisiz erişim elde edilmesine veya kısıtlı işlevlere erişmek için yetkilerin yükseltilmesine olanak tanıyan güvenlik açıklarına odaklanır.
- **İş Mantığı (Business Logic - Bellenim Güncelleme Süreci):** Bellenim güncelleme sürecinin tasarım ve uygulamasındaki güvenlik açıklarına odaklanır.

[ISTG-FW](./README.md) bileşenine ait tüm test senaryoları ve kategorileri, bu bileşenin alt uzmanlaşmalarının ayrıntılarına bakılmaksızın genel bellenim analiz yönlerine odaklanır.

## Bilgi Toplama (ISTG-FW-INFO)

Bir IoT cihazının bellenimi; açığa çıkması durumunda cihazın iç işleyişine veya çevre IoT ekosistemine ilişkin ayrıntıları potansiyel saldırganlara ifşa edebilecek çeşitli bilgiler içerebilir. Bu durum daha gelişmiş saldırıların hazırlanmasını ve gerçekleştirilmesini kolaylaştırabilir.

### Kaynak Kod ve İkiliklerin (Binaries) Açığa Çıkması (ISTG-FW-INFO-001)

**Gerekli Erişim Seviyeleri**

<table width="100%">
	<tr valign="top">
		<th width="1%" align="left">Fiziksel</th>
 <td><i>PA-1</i> - <i>PA-4</i><br>(bellenime nasıl erişilebildiğine bağlı olarak; örn. dahili/fiziksel hata ayıklama arayüzü veya uzaktan SSH ile)</td>
	</tr>
	<tr valign="top">
		<th align="left">Yetkilendirme</th>
		<td><i>AA-1</i> - <i>AA-4</i><br>(hangi bileşen uzmanlaşmasının test edileceğine ve ona nasıl erişilebildiğine bağlı olarak)</td>
	</tr>
</table>

**Özet**

Derlenmemiş kaynak kodunun açığa çıkması, deneme-yanılma yöntemine gerek kalmadan doğrudan kod üzerinde güvenlik açıkları tespit edilebileceğinden yazılım uygulamasının istismar edilmesini hızlandırabilir. Ayrıca geride bırakılan kaynak kodları; canlı kullanım için tasarlanmamış dahili geliştirme bilgilerini, geliştirici yorumlarını veya sabit kodlanmış (hard-coded) hassas verileri içerebilir.

Derlenmemiş kaynak koduna benzer şekilde derlenmiş ikilikler (binaries) de ilgili bilgileri açığa çıkarabilir. Ancak yararlı verileri elde etmek için tersine mühendislik (reverse-engineering) gerekebilir ve bu da ciddi zaman alabilir. Bu nedenle test uzmanı, ideal olarak bellenim üreticisiyle koordinasyon halinde hangi ikiliklerin analiz edilmeye değer olduğunu değerlendirmelidir.

**Test Hedefleri**

- Bellenim içinde derlenmemiş kaynak kodunun bulunup bulunmadığı kontrol edilmelidir.
- Derlenmemiş kaynak kodu tespit edilirse, içeriği potansiyel saldırganlar için yararlı olabilecek hassas verilerin varlığı açısından analiz edilmelidir (ayrıca bkz. [ISTG-FW-SCRT-003](#sabit-kodlanmış-hard-coded-gizli-bilgilerin-kullanımı-istg-fw-scrt-003)).
- Bellenim uygulaması ve hassas verilerin işlenmesiyle ilgili yararlı bilgiler elde etmek için seçilen ikilikler üzerinde tersine mühendislik gerçekleştirilmelidir.

**İyileştirme / Çözüm**

Mümkünse, canlı kullanım için tasarlanan bellenimden derlenmemiş kaynak kodları kaldırılmalıdır. Kaynak kodun dahil edilmesi gerekiyorsa, bellenim yayınlanmadan önce tüm dahili geliştirme verilerinin temizlendiği doğrulanmalıdır.

Tersine mühendisliği tamamen engellemek mümkün olmadığından, saldırı yüzeyini azaltmak için genel olarak bellenime erişimi kısıtlayıcı önlemler uygulanmalıdır. Ayrıca kod karartma (obfuscation) gibi yöntemlerle tersine mühendislik süreci zorlaştırılabilir.

**Kaynaklar**

Bu test senaryosu için aşağıdaki kaynaklardan veriler birleştirilmiştir:

* OWASP ["Firmware Security Testing Methodology"][owasp_fstm]
* ["IoT Pentesting Guide"][iot_pentesting_guide] (Aditya Gupta)
* ["IoT Penetration Testing Cookbook"][iot_penetration_testing_cookbook] (Aaron Guzman, Aditya Gupta)
* ["The IoT Hacker's Handbook"][iot_hackers_handbook] (Aditya Gupta)
* ["Practical IoT Hacking"][practical_iot_hacking] (Fotios Chantzis, Ioannis Stais, Paulino Calderon, Evangelos Deirmentzoglou, Beau Woods)
* T-Systems Multimedia Solutions GmbH test standartları

### Uygulama Ayrıntılarının Açığa Çıkması (ISTG-FW-INFO-002)

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

Kullanılan algoritmalar veya kimlik doğrulama prosedürü gibi uygulamaya ilişkin ayrıntıların potansiyel saldırganlar tarafından erişilebilir olması durumunda, başarılı saldırı noktaları ve güvenlik açıkları daha kolay tespit edilir. Bu ayrıntıların tek başına açığa çıkması doğrudan bir zafiyet sayılmasa da potansiyel saldırı vektörlerinin belirlenmesini kolaylaştırarak saldırganların güvensiz uygulamaları daha hızlı istismar etmesini sağlar.

Örneğin, yapılandırma dosyaları, metin dosyaları, sistem ayarları veya veritabanları gibi çeşitli türdeki dosyalarda ilgili bilgiler yer alabilir.

**Test Hedefleri**

- İlerideki testleri hazırlamak amacıyla uygulamaya ilişkin erişilebilir ayrıntılar değerlendirilmelidir. Örneğin şunları içerir:
  - Kullanımdaki kriptografik algoritmalar
  - Kimlik doğrulama ve yetkilendirme mekanizmaları
  - Yerel yollar (local paths) ve ortam ayrıntıları

**İyileştirme / Çözüm**

Yukarıda belirtildiği gibi, bu tür bilgilerin açığa çıkması tek başına bir zafiyet olarak kabul edilmez. Ancak istismar girişimlerini engellemek için yalnızca cihazın çalışması için kesinlikle gerekli olan bilgilere erişilebilmelidir.

**Kaynaklar**

Bu test senaryosu için aşağıdaki kaynaklardan veriler birleştirilmiştir:

* OWASP ["Firmware Security Testing Methodology"][owasp_fstm]
* ["IoT Pentesting Guide"][iot_pentesting_guide] (Aditya Gupta)
* ["IoT Penetration Testing Cookbook"][iot_penetration_testing_cookbook] (Aaron Guzman, Aditya Gupta)
* ["The IoT Hacker's Handbook"][iot_hackers_handbook] (Aditya Gupta)
* ["Practical IoT Hacking"][practical_iot_hacking] (Fotios Chantzis, Ioannis Stais, Paulino Calderon, Evangelos Deirmentzoglou, Beau Woods)
* T-Systems Multimedia Solutions GmbH test standartları

### Ekosistem Ayrıntılarının Açığa Çıkması (ISTG-FW-INFO-003)

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

Cihaz belleniminin içeriği, çevreleyen IoT ekosistemi hakkında hassas URL'ler, IP adresleri, kullanılan yazılımlar vb. bilgileri açığa çıkarabilir. Bir saldırgan bu bilgileri ekosisteme yönelik saldırılar hazırlamak ve yürütmek için kullanabilir.

Örneğin, yapılandırma dosyaları ve metin dosyaları gibi çeşitli türdeki dosyalarda bu tür ilgili bilgiler yer alabilir.

**Test Hedefleri**

- Bellenimin (veya yapılandırma dosyaları gibi parçalarının) çevre ekosistem hakkında ilgili bilgiler içerip içermediği belirlenmelidir.

**İyileştirme / Çözüm**

Bilgilerin açığa çıkması, cihazın çalıştırılması için gereken minimum düzeye indirilmelidir. Açığa çıkan bilgiler değerlendirilmeli ve gereksiz yere dahil edilen tüm veriler kaldırılmalıdır.

**Kaynaklar**

Bu test senaryosu için aşağıdaki kaynaklardan veriler birleştirilmiştir:

* OWASP ["Firmware Security Testing Methodology"][owasp_fstm]
* ["IoT Pentesting Guide"][iot_pentesting_guide] (Aditya Gupta)
* ["IoT Penetration Testing Cookbook"][iot_penetration_testing_cookbook] (Aaron Guzman, Aditya Gupta)
* ["The IoT Hacker's Handbook"][iot_hackers_handbook] (Aditya Gupta)
* ["Practical IoT Hacking"][practical_iot_hacking] (Fotios Chantzis, Ioannis Stais, Paulino Calderon, Evangelos Deirmentzoglou, Beau Woods)
* T-Systems Multimedia Solutions GmbH test standartları

### Güvensiz İkili Derleme Seçenekleri (ISTG-FW-INFO-004)

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

IoT bellenimi içindeki derlenmiş ikilikler (binaries), derleyici ve bağlayıcı güvenlik bayrakları aracılığıyla etkinleştirilen standart istismar önleme özelliklerinden (exploit mitigations) yoksun olabilir. Position Independent Executables (PIE), stack canaries, No-Execute (NX), Relocation Read-Only (RELRO) ve FORTIFY_SOURCE gibi güvenlik sıkılaştırma özellikleri, bellek bozulması (memory corruption) zafiyetlerine karşı kritik derinlemesine savunma (defense-in-depth) sağlar. IoT yönlendirici bellenimleri üzerine yapılan araştırmalar, gömülü ikiliklerin önemli bir kısmının stack canary ve full RELRO gibi temel korumalardan yoksun olduğunu ve cihazları bellek istismarına karşı savunmasız bıraktığını göstermiştir. Bu korumaların bulunmaması, bellenimdeki güvenlik açıklarını istismar etmenin karmaşıklığını azaltır — örneğin bir saldırgan PIE/ASLR'den yoksun ikiliklere karşı Return-Oriented Programming (ROP) tekniklerini kullanabilir ve NX koruması olmayan ikiliklere doğrudan shellcode enjekte edebilir. Milyonlarca gömülü ve IoT cihazını etkileyen BusyBox'taki stack buffer overflow zafiyeti (CVE-2022-48174) gibi gerçek dünya örnekleri, eksik stack canaries ve ASLR korumalarının istismar eşiğini ne kadar düşürdüğünü açıkça ortaya koymaktadır.

**Test Hedefleri**

- Bellenim içindeki derlenmiş ikilikler tanımlanmalı ve yaygın istismar önleme özelliklerinin varlığı veya yokluğu açısından analiz edilmelidir:
  - **PIE (Position Independent Executable):** İkili düzeyde ASLR'yi etkinleştirir, yükleme adreslerini rastgele hale getirir ve ROP saldırılarını karmaşıklaştırır.
  - **NX/W^X (No-Execute):** Yığın (stack) veya öbek (heap) gibi yazılabilir bellek bölgelerine enjekte edilen kodun yürütülmesini engeller.
  - **Stack Canaries (Stack Smashing Protector, SSP):** İşlev dönüşünden önce yığın tabanlı arabellek taşmalarını algılar.
  - **RELRO (Relocation Read-Only):** Dinamik bağlamadan sonra Genel Ofset Tablosunu (GOT) salt okunur olarak işaretleyerek üzerine yazma saldırılarına karşı sıkılaştırır.
  - **FORTIFY_SOURCE:** Derleme zamanında güvensiz C standart kütüphane işlevlerini sınır kontrollü varyantlarla değiştirir.
- İkili sıkılaştırma özelliklerini değerlendirmek için `checksec`, `readelf`, `objdump` ve `rabin2` gibi araçlar kullanılmalıdır.
- Tespit edilen eksik önlemler belgelenmeli ve ikili dosyanın rolü ile potansiyel istismar edilebilirliği bağlamında değerlendirilmelidir.
- Sonuçlar, daha ileri ikili analiz ve istismar testlerini yönlendirmek için kullanılmalıdır (ayrıca bkz. [ISTG-FW-INFO-001](#kaynak-kod-ve-ikiliklerin-binaries-açığa-çıkması-istg-fw-info-001)).

**İyileştirme / Çözüm**

Bellenim derleme süreci, araç zinciri (toolchain) tarafından desteklenen istismar önleme özelliklerini (PIE, stack canaries, full RELRO ve FORTIFY_SOURCE) etkinleştirmeli ve bunları paketlenmiş üçüncü taraf kütüphaneler dahil olmak üzere tüm derlenmiş bileşenlere tutarlı bir şekilde uygulamalıdır. Çapraz derleme (cross-compile) hedefleri için araç zinciri varsayılanlarının masaüstü platformlarından farklı olabileceği ve varsayılmak yerine açıkça doğrulanması gerektiği unutulmamalıdır.

**Kaynaklar**

Bu test senaryosu için aşağıdaki kaynaklardan veriler birleştirilmiştir:

* OWASP ["Firmware Security Testing Methodology"][owasp_fstm]
* ["IoT Penetration Testing Cookbook"][iot_penetration_testing_cookbook] (Aaron Guzman, Aditya Gupta)
* ["Practical IoT Hacking"][practical_iot_hacking] (Fotios Chantzis, Ioannis Stais, Paulino Calderon, Evangelos Deirmentzoglou, Beau Woods)
* [OpenSSF Compiler Options Hardening Guide for C and C++][openssf_compiler_hardening]
* [CWE-119][cwe_119]: Bellek Arabelleği Sınırları İçindeki İşlemlerin Hatalı Kısıtlanması
* [CWE-121][cwe_121]: Yığın Tabanlı Arabellek Taşması
* [CWE-693][cwe_693]: Koruma Mekanizması Başarısızlığı

## Yapılandırma ve Yama Yönetimi (ISTG-FW-CONF)

IoT cihazları uzun bir kullanım ömrüne sahip olabileceğinden, en son güvenlik yamalarını uygulamak için cihazda çalışan yazılımın düzenli olarak güncellendiğinden emin olmak önemlidir. Bellenimin kendi güncelleme süreci [ISTG-FW[UPDT]](../firmware/firmware_update_mechanism.md) kapsamında ele alınacaktır. Ancak bellenimde yer alan yazılım paketlerinin de güncel olduğu doğrulanmalıdır.

### Güncel Olmayan Yazılım Kullanımı (ISTG-FW-CONF-001)

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

Her yazılım parçası saldırılara karşı potansiyel olarak savunmasızdır. Örneğin, kodlama hataları tanımsız program davranışına yol açabilir ve bu da bir saldırgan tarafından uygulama tarafından işlenen verilere erişmek veya çalışma zamanı ortamı bağlamında eylemler gerçekleştirmek için istismar edilebilir. Ayrıca kullanılan çatılardaki (frameworks), kütüphanelerdeki ve diğer teknolojilerdeki güvenlik açıkları da yazılımın güvenlik düzeyini doğrudan etkileyebilir.

Genellikle geliştiriciler yazılımlarında bir zafiyet tespit edildiğinde bir güncelleme yayınlar. Başarılı saldırı olasılığını azaltmak için bu güncellemeler mümkün olan en kısa sürede yüklenmelidir. Aksi takdirde saldırganlar cihaza yönelik saldırılar gerçekleştirmek için bilinen güvenlik açıklarını (known vulnerabilities) kullanabilir.

**Test Hedefleri**

- Yüklü yazılım paketlerinin yanı sıra kullanılan kütüphanelerin ve çatıların sürüm tanımlayıcıları belirlenmelidir.
- Tespit edilen sürüm tanımlayıcılarına dayanarak, kullanılan yazılım sürümünün güncel olup olmadığı (örn. yazılım geliştiricisinin web sitesine veya açık kaynak depolarına başvurularak) belirlenmelidir.
- NIST'in [National Vulnerability Database](https://nvd.nist.gov) (NVD) gibi zafiyet veritabanları kullanılarak tespit edilen yazılım sürümleri için bilinen herhangi bir güvenlik açığı olup olmadığı kontrol edilmelidir.

**İyileştirme / Çözüm**

Bellenim güncel olmayan hiçbir yazılım paketi içermemelidir. Güncellemelerin yayınlanır yayınlanmaz yüklenmesini sağlayan uygun bir yama yönetimi (patch management) süreci uygulanmalıdır.

**Kaynaklar**

Bu test senaryosu için aşağıdaki kaynaklardan veriler birleştirilmiştir:

* OWASP ["Firmware Security Testing Methodology"][owasp_fstm]
* ["IoT Penetration Testing Cookbook"][iot_penetration_testing_cookbook] (Aaron Guzman, Aditya Gupta)
* ["Practical IoT Hacking"][practical_iot_hacking] (Fotios Chantzis, Ioannis Stais, Paulino Calderon, Evangelos Deirmentzoglou, Beau Woods)
* T-Systems Multimedia Solutions GmbH test standartları

### Gereksiz Yazılım ve İşlevlerin Varlığı (ISTG-FW-CONF-002)

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

Bellenime dahil edilen her yazılım parçası, cihaza yönelik saldırılar gerçekleştirmek için kullanılabileceğinden saldırı yüzeyini (attack surface) genişletir. Yüklü yazılım güncel olsa bile henüz yayınlanmamış 0-day güvenlik açıklarından etkilenebilir. Bir yazılım programının zafiyet içermese dahi (örn. belirli dosyalara veya süreçlere erişim sağlayarak) bir saldırıyı kolaylaştırması da mümkündür.

**Test Hedefleri**

- Bellenimde yer alan yazılım paketlerinin tam bir listesi çıkarılmalıdır.
- Cihaz belgelerine, çalışma davranışına ve amaçlanan kullanım senaryolarına dayanarak, yüklü yazılım paketlerinden herhangi birinin cihazın çalışması için zorunlu olup olmadığı belirlenmelidir.

**İyileştirme / Çözüm**

Cihazın çalışması için gerekli olmayan her yazılım kaldırılarak veya devre dışı bırakılarak saldırı yüzeyi mümkün olduğunca en aza indirilmelidir.

Özellikle Windows ve Linux sistemleri gibi genel amaçlı işletim sistemlerinde gereksiz tüm işletim sistemi özelliklerinin ve arka plan servislerinin devre dışı bırakıldığından emin olunmalıdır.

**Kaynaklar**

Bu test senaryosu için aşağıdaki kaynaklardan veriler birleştirilmiştir:

* OWASP ["Firmware Security Testing Methodology"][owasp_fstm]
* ["IoT Penetration Testing Cookbook"][iot_penetration_testing_cookbook] (Aaron Guzman, Aditya Gupta)
* ["Practical IoT Hacking"][practical_iot_hacking] (Fotios Chantzis, Ioannis Stais, Paulino Calderon, Evangelos Deirmentzoglou, Beau Woods)
* T-Systems Multimedia Solutions GmbH test standartları

## Gizli Bilgiler / Secrets (ISTG-FW-SCRT)

IoT cihazları genellikle üreticilerinin kontrol alanının dışında çalıştırılır. Yine de bellenim güncellemelerini istemek/almak veya bir bulut API'sine telemetri/veri göndermek gibi nedenlerle ekosistemdeki diğer ağ düğümleriyle bağlantı kurmaları gerekir. Bu nedenle cihazın bir tür kimlik doğrulama bilgisi veya gizli anahtar sağlaması gerekebilir. Bu gizli bilgilerin çalınmasını ve cihazı taklit etmek için kullanılmasını önlemek amacıyla cihazda güvenli bir şekilde saklanması gerekir.

### Genel Depolama Alanlarında Saklanan Gizli Bilgiler (ISTG-FW-SCRT-001)

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

Genel olarak bir dosya sisteminde bazıları herkese açık olan, bazılarına ise yalnızca belirli bir ayrıcalık düzeyiyle erişilebilen birden fazla depolama alanı türü vardır. Hassas veriler veya gizli bilgiler herkesin erişebileceği depolama alanlarında saklanırsa, bu verilere erişimi olmaması gereken ancak dosya sistemine erişimi olan kullanıcılar bunları okuyabilir veya değiştirebilir. Başarılı bir saldırı durumunda, genel depolama alanında saklanan gizli bilgilerin ifşa olma olasılığı son derece yüksektir.

**Test Hedefleri**

- Genel depolama alanlarındaki dosyalar ve veritabanları; parolalar, simetrik/özel anahtarlar ve oturum belirteçleri (tokens) gibi gizli bilgilerin varlığı açısından kontrol edilmelidir.

**İyileştirme / Çözüm**

Gizli bilgilere erişim yalnızca uygun ayrıcalıklara sahip hesaplara veya süreçlere verilmelidir. Bu nedenle sırlar, yalnızca belirli varlıkların erişebildiği korumalı depolama alanlarında veya özel anahtar depolarında (key stores / secure enclaves) saklanmalıdır.

**Kaynaklar**

Bu test senaryosu için aşağıdaki kaynaklardan veriler birleştirilmiştir:

* OWASP ["Firmware Security Testing Methodology"][owasp_fstm]
* ["IoT Pentesting Guide"][iot_pentesting_guide] (Aditya Gupta)
* ["IoT Penetration Testing Cookbook"][iot_penetration_testing_cookbook] (Aaron Guzman, Aditya Gupta)
* ["The IoT Hacker's Handbook"][iot_hackers_handbook] (Aditya Gupta)
* ["Practical IoT Hacking"][practical_iot_hacking] (Fotios Chantzis, Ioannis Stais, Paulino Calderon, Evangelos Deirmentzoglou, Beau Woods)
* T-Systems Multimedia Solutions GmbH test standartları

### Gizli Bilgilerin Şifrelenmemiş Olarak Saklanması (ISTG-FW-SCRT-002)

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

Hassas veriler ve sırlar şifrelenmiş olarak saklanmalıdır; böylece bir saldırgan bunlara erişmeyi başarsa bile ilgili düz metin (plaintext) verilere erişemez.

[ISTG-FW-SCRT-001](#genel-depolama-alanlarında-saklanan-gizli-bilgiler-istg-fw-scrt-001)'in aksine, saldırganın erişim kısıtlamalarını atlayarak veya kısıtlı depolamaya erişimi olan bir süreci istismar ederek verilere zaten eriştiği varsayıldığından sırların genel mi yoksa kısıtlı depolama alanlarında mı saklandığı bu senaryo için önemsizdir. Ayrıca kullanımdaki kriptografik algoritmaların gücü [ISTG-FW-CRYPT-001](#zayıf-kriptografik-algoritmaların-kullanımı-istg-fw-crypt-001) kapsamında ele alınacaktır.

**Test Hedefleri**

- Genel ve kısıtlı depolama alanları aranarak bellenimin düz metin biçiminde sırlar içerip içermediği belirlenmelidir.

**İyileştirme / Çözüm**

Sırlar uygun kriptografik algoritmalar kullanılarak saklanmalıdır. Yalnızca sırrın şifrelenmiş hali saklanmalıdır.

**Kaynaklar**

Bu test senaryosu için aşağıdaki kaynaklardan veriler birleştirilmiştir:

* OWASP ["Firmware Security Testing Methodology"][owasp_fstm]
* ["IoT Pentesting Guide"][iot_pentesting_guide] (Aditya Gupta)
* ["IoT Penetration Testing Cookbook"][iot_penetration_testing_cookbook] (Aaron Guzman, Aditya Gupta)
* ["The IoT Hacker's Handbook"][iot_hackers_handbook] (Aditya Gupta)
* ["Practical IoT Hacking"][practical_iot_hacking] (Fotios Chantzis, Ioannis Stais, Paulino Calderon, Evangelos Deirmentzoglou, Beau Woods)
* T-Systems Multimedia Solutions GmbH test standartları

### Sabit Kodlanmış (Hard-coded) Gizli Bilgilerin Kullanımı (ISTG-FW-SCRT-003)

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

Geliştiriciler bazen gizli bilgileri doğrudan yazılımlarının kaynak koduna dahil etme eğilimindedir. Bu durum aşağıdakiler gibi çeşitli güvenlik sorunlarına yol açabilir:

- Yayınlanan kaynak kodu parçacıkları veya kaynak kodunun derlemeden geri döndürülmesi (decompilation) yoluyla sırların açığa çıkması,
- Aynı sırrın tüm cihazlarda kullanılma olasılığı çok yüksek olduğundan, ilgili yazılımı kullanan tüm cihazların tehlikeye girmesi (aksi takdirde kaynak kodun her cihaz için ayrı ayrı değiştirilmesi ve derlenmesi gerekir) ve
- Sırrın ele geçirilmesi durumunda sırrı değiştirmenin bir yazılım güncellemesi gerektirmesi nedeniyle reaktif müdahale önlemlerinin engellenmesi.

**Test Hedefleri**

- [ISTG-FW-INFO-001](#kaynak-kod-ve-ikiliklerin-binaries-açığa-çıkması-istg-fw-info-001) temelinde, herhangi bir sabit kodlanmış (hard-coded) sırrın tespit edilip edilemeyeceği kontrol edilmelidir.

**İyileştirme / Çözüm**

Sırlar kaynak koduna sabit kodlanmamalıdır (hard-code edilmemelidir). Bunun yerine sırlar güvenli bir şekilde saklanmalı (bkz. [ISTG-FW-SCRT-001](#genel-depolama-alanlarında-saklanan-gizli-bilgiler-istg-fw-scrt-001) ve [ISTG-FW-SCRT-002](#gizli-bilgilerin-şifrelenmemiş-olarak-saklanması-istg-fw-scrt-002)) ve yazılım süreci çalışma zamanı (runtime) sırasında sırları güvenli depolamadan dinamik olarak almalıdır.

**Kaynaklar**

Bu test senaryosu için aşağıdaki kaynaklardan veriler birleştirilmiştir:

* OWASP ["Firmware Security Testing Methodology"][owasp_fstm]
* ["IoT Pentesting Guide"][iot_pentesting_guide] (Aditya Gupta)
* ["IoT Penetration Testing Cookbook"][iot_penetration_testing_cookbook] (Aaron Guzman, Aditya Gupta)
* ["The IoT Hacker's Handbook"][iot_hackers_handbook] (Aditya Gupta)
* ["Practical IoT Hacking"][practical_iot_hacking] (Fotios Chantzis, Ioannis Stais, Paulino Calderon, Evangelos Deirmentzoglou, Beau Woods)
* T-Systems Multimedia Solutions GmbH test standartları

## Kriptografi (ISTG-FW-CRYPT)

Birçok IoT cihazının hassas verileri güvenli bir şekilde saklamak, kimlik doğrulama amacıyla veya diğer ağ düğümlerinden gelen şifreli verileri alıp doğrulamak için kriptografik algoritmalar uygulaması gerekir. Güvenli ve güncel standartlara uygun kriptografinin uygulanamaması; hassas verilerin ifşasına, cihaz arızalarına veya cihaz üzerindeki kontrolün kaybedilmesine yol açabilir.

### Zayıf Kriptografik Algoritmaların Kullanımı (ISTG-FW-CRYPT-001)

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

Kriptografi çeşitli şekillerde uygulanabilir. Ancak gelişen teknolojiler, yeni algoritmalar ve artan bilgi işlem gücü nedeniyle günümüzde birçok eski kriptografik algoritma zayıf veya güvensiz olarak kabul edilmektedir. Bu nedenle ya daha yeni ve daha güçlü algoritmalar kullanılmalı ya da anahtar uzunluğu artırılarak veya alternatif çalışma modları kullanılarak mevcut algoritmalar uyarlanmalıdır.

Zayıf kriptografik algoritmaların kullanılması, bir saldırganın verilen bir şifreli metinden (ciphertext) düz metni (plaintext) makul bir sürede geri elde etmesine olanak tanıyabilir.

**Test Hedefleri**

- Bellenim tarafından veya bellenim içinde saklanan veriler, şifrelenmiş veri segmentlerinin varlığı açısından kontrol edilmelidir. Şifreli segmentler bulunursa kullanılan algoritmaların tanımlanıp tanımlanamayacağı incelenmelidir.
- [ISTG-FW-INFO-001](#kaynak-kod-ve-ikiliklerin-binaries-açığa-çıkması-istg-fw-info-001) ve [ISTG-FW-INFO-002](#uygulama-ayrıntılarının-açığa-çıkması-istg-fw-info-002) temelinde, herhangi bir kaynak kodun, yapılandırma dosyasının vb. belirli kriptografik algoritmaların kullanımını ifşa edip etmediği kontrol edilmelidir.
- Algoritmaların tespit edilebilmesi durumunda, kullanılan algoritmaların ve yapılandırmalarının test sırasında yeterli bir güvenlik düzeyi sağlayıp sağlamadığı (örn. BSI'ın [TR-02102-1](https://www.bsi.bund.de/SharedDocs/Downloads/EN/BSI/Publications/TechGuidelines/TG02102/BSI-TR-02102-1.pdf?__blob=publicationFile&v=10) teknik kılavuzu gibi rehberlere başvurularak) belirlenmelidir.

**İyileştirme / Çözüm**

Yalnızca güçlü ve güncel standartlara uygun kriptografik algoritmalar kullanılmalıdır. Ayrıca bu algoritmalar, uygun bir anahtar uzunluğu veya çalışma modu gibi doğru parametreler ayarlanarak güvenli bir şekilde kullanılmalıdır.

**Kaynaklar**

Bu test senaryosu için aşağıdaki kaynaklardan veriler birleştirilmiştir:

* OWASP ["Firmware Security Testing Methodology"][owasp_fstm]
* ["IoT Pentesting Guide"][iot_pentesting_guide] (Aditya Gupta)
* ["IoT Penetration Testing Cookbook"][iot_penetration_testing_cookbook] (Aaron Guzman, Aditya Gupta)
* ["The IoT Hacker's Handbook"][iot_hackers_handbook] (Aditya Gupta)
* T-Systems Multimedia Solutions GmbH test standartları

[owasp_fstm]: https://github.com/scriptingxss/owasp-fstm "OWASP Firmware Security Testing Methodology"
[iot_pentesting_guide]: https://www.iotpentestingguide.com "IoT Pentesting Guide"
[iot_penetration_testing_cookbook]: https://www.packtpub.com/product/iot-penetration-testing-cookbook/9781787280571 "IoT Penetration Testing Cookbook"
[iot_hackers_handbook]: https://link.springer.com/book/10.1007/978-1-4842-4300-8 "The IoT Hacker's Handbook"
[practical_iot_hacking]: https://nostarch.com/practical-iot-hacking "Practical IoT Hacking"
[openssf_compiler_hardening]: https://best.openssf.org/Compiler-Hardening-Guides/Compiler-Options-Hardening-Guide-for-C-and-C++.html "OpenSSF Compiler Options Hardening Guide for C and C++"
[cwe_119]: https://cwe.mitre.org/data/definitions/119.html "CWE-119: Improper Restriction of Operations within the Bounds of a Memory Buffer"
[cwe_121]: https://cwe.mitre.org/data/definitions/121.html "CWE-121: Stack-based Buffer Overflow"
[cwe_693]: https://cwe.mitre.org/data/definitions/693.html "CWE-693: Protection Mechanism Failure"
