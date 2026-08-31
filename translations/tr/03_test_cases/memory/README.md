# 3.2. Bellek (ISTG-MEM)

## İçindekiler
* [Genel Bakış](#genel-bakış)
* [Bilgi Toplama (ISTG-MEM-INFO)](#bilgi-toplama-istg-mem-info)
  * [Kaynak Kod ve İkiliklerin (Binaries) Açığa Çıkması (ISTG-MEM-INFO-001)](#kaynak-kod-ve-ikiliklerin-binaries-açığa-çıkması-istg-mem-info-001)
  * [Uygulama Ayrıntılarının Açığa Çıkması (ISTG-MEM-INFO-002)](#uygulama-ayrıntılarının-açığa-çıkması-istg-mem-info-002)
  * [Ekosistem Ayrıntılarının Açığa Çıkması (ISTG-MEM-INFO-003)](#ekosistem-ayrıntılarının-açığa-çıkması-istg-mem-info-003)
  * [Kullanıcı Verilerinin Açığa Çıkması (ISTG-MEM-INFO-004)](#kullanıcı-verilerinin-açığa-çıkması-istg-mem-info-004)
  * [Güvensiz İkili Derleme Seçenekleri (ISTG-MEM-INFO-005)](#güvensiz-ikili-derleme-seçenekleri-istg-mem-info-005)
* [Gizli Bilgiler / Secrets (ISTG-MEM-SCRT)](#gizli-bilgiler--secrets-istg-mem-scrt)
  * [Gizli Bilgilerin Şifrelenmemiş Olarak Saklanması (ISTG-MEM-SCRT-001)](#gizli-bilgilerin-şifrelenmemiş-olarak-saklanması-istg-mem-scrt-001)
* [Kriptografi (ISTG-MEM-CRYPT)](#kriptografi-istg-mem-crypt)
  * [Zayıf Kriptografik Algoritmaların Kullanımı (ISTG-MEM-CRYPT-001)](#zayıf-kriptografik-algoritmaların-kullanımı-istg-mem-crypt-001)

## Genel Bakış

Bu bölüm, bellek (memory) bileşenine yönelik test senaryolarını ve kategorilerini içerir. İşlem birimine benzer şekilde bellek, yalnızca *PA-4* (invaziv fiziksel erişim) ile erişilebilen bir cihaz içi öğedir. Belleğe doğrudan bağlantı kurmak özel donanım ekipmanları (örn. bir hata ayıklama kartı veya test probları) gerektirebilir.

Bellek için geçerli olan aşağıdaki test senaryosu kategorileri belirlenmiştir:

- **Bilgi Toplama (Information Gathering):** Uygun şekilde korunmadığı veya kaldırılmadığı takdirde bellek yongasında saklanan ve potansiyel saldırganlara açığa çıkabilecek bilgilere odaklanır.
- **Gizli Bilgiler (Secrets):** Bellek yongasında güvensiz bir şekilde saklanan gizli anahtar ve kimlik bilgilerine odaklanır.
- **Kriptografi (Cryptography):** Kriptografik uygulamadaki güvenlik açıklarına odaklanır.

## Bilgi Toplama (ISTG-MEM-INFO)

Bir IoT cihazının belleği, açığa çıkması durumunda cihazın iç işleyişine veya temel IoT ekosistemine ilişkin ayrıntıları potansiyel saldırganlara ifşa edebilecek çeşitli veriler içerebilir. Bu durum, daha gelişmiş saldırıların hazırlanmasını ve yürütülmesini kolaylaştırabilir.

Cihaz belleği üzerindeki testler doğrudan bellek yongalarına erişilerek gerçekleştirilir. Bu nedenle, kullanıcı hesabı kullanılmazken (*AA-1*) invaziv fiziksel erişim (*PA-4*) gereklidir.

### Kaynak Kod ve İkiliklerin (Binaries) Açığa Çıkması (ISTG-MEM-INFO-001)

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

Derlenmemiş kaynak kodunun açığa çıkması, deneme-yanılma yöntemine gerek kalmadan doğrudan kod üzerinde güvenlik açıkları tespit edilebileceğinden yazılım uygulamasının istismar edilmesini hızlandırabilir. Ayrıca geride bırakılan kaynak kodları; canlı kullanım için tasarlanmamış dahili geliştirme bilgilerini, geliştirici yorumlarını veya sabit kodlanmış (hard-coded) hassas verileri içerebilir.

Derlenmemiş kaynak koduna benzer şekilde derlenmiş ikilikler (binaries) de ilgili bilgileri açığa çıkarabilir. Ancak yararlı verileri elde etmek için tersine mühendislik (reverse-engineering) gerekebilir ve bu da ciddi zaman alabilir. Bu nedenle test uzmanı, ideal olarak cihaz üreticisiyle koordinasyon halinde hangi ikiliklerin analiz edilmeye değer olduğunu değerlendirmelidir.

**Test Hedefleri**

- Cihaz belleğinde derlenmemiş kaynak kodunun bulunup bulunmadığı kontrol edilmelidir.
- Derlenmemiş kaynak kodu tespit edilirse, içeriği potansiyel saldırganlar için yararlı olabilecek hassas verilerin varlığı açısından analiz edilmelidir.
- Cihaz uygulaması ve hassas verilerin işlenmesiyle ilgili yararlı bilgiler elde etmek için seçilen ikilikler üzerinde tersine mühendislik gerçekleştirilmelidir.

**İyileştirme / Çözüm**

Mümkünse, canlı kullanım için tasarlanan cihazlardan derlenmemiş kaynak kodları kaldırılmalıdır. Kaynak kodun dahil edilmesi gerekiyorsa, cihaz piyasaya sürülmeden önce tüm dahili geliştirme verilerinin temizlendiği doğrulanmalıdır.

Tersine mühendisliği tamamen engellemek mümkün olmadığından, saldırı yüzeyini azaltmak için genel olarak cihaz belleğine erişimi kısıtlayıcı önlemler uygulanmalıdır. Ayrıca kod karartma (obfuscation) gibi yöntemlerle tersine mühendislik süreci zorlaştırılabilir.

**Kaynaklar**

Bu test senaryosu için aşağıdaki kaynaklardan veriler birleştirilmiştir:

* ["IoT Pentesting Guide"][iot_pentesting_guide] (Aditya Gupta)
* ["IoT Penetration Testing Cookbook"][iot_penetration_testing_cookbook] (Aaron Guzman, Aditya Gupta)
* ["The IoT Hacker's Handbook"][iot_hackers_handbook] (Aditya Gupta)

Bu test senaryosu şuna dayanmaktadır: [ISTG-FW-INFO-001](../firmware/README.md#disclosure-of-source-code-and-binaries-istg-fw-info-001).

### Uygulama Ayrıntılarının Açığa Çıkması (ISTG-MEM-INFO-002)

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

Kullanılan algoritmalar veya kimlik doğrulama prosedürü gibi uygulamaya ilişkin ayrıntıların potansiyel saldırganlar tarafından erişilebilir olması durumunda, başarılı saldırı noktaları ve güvenlik açıkları daha kolay tespit edilir. Bu ayrıntıların tek başına açığa çıkması doğrudan bir zafiyet sayılmasa da potansiyel saldırı vektörlerinin belirlenmesini kolaylaştırarak saldırganların güvensiz uygulamaları daha hızlı istismar etmesini sağlar.

**Test Hedefleri**

- İlerideki testleri hazırlamak amacıyla uygulamaya ilişkin erişilebilir ayrıntılar değerlendirilmelidir. Örneğin şunları içerir:
  - Kullanımdaki kriptografik algoritmalar
  - Kimlik doğrulama ve yetkilendirme mekanizmaları
  - Yerel yollar (local paths) ve ortam ayrıntıları

**İyileştirme / Çözüm**

Yukarıda belirtildiği gibi, bu tür bilgilerin açığa çıkması tek başına bir zafiyet olarak kabul edilmez. Ancak istismar girişimlerini engellemek için cihazda yalnızca cihazın çalışması için kesinlikle gerekli olan bilgiler saklanmalıdır.

**Kaynaklar**

Bu test senaryosu için aşağıdaki kaynaklardan veriler birleştirilmiştir:

* ["IoT Pentesting Guide"][iot_pentesting_guide] (Aditya Gupta)
* ["IoT Penetration Testing Cookbook"][iot_penetration_testing_cookbook] (Aaron Guzman, Aditya Gupta)
* ["The IoT Hacker's Handbook"][iot_hackers_handbook] (Aditya Gupta)

Bu test senaryosu şuna dayanmaktadır: [ISTG-FW-INFO-002](../firmware/README.md#disclosure-of-implementation-details-istg-fw-info-002).

### Ekosistem Ayrıntılarının Açığa Çıkması (ISTG-MEM-INFO-003)

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

Cihaz belleğinin içeriği, çevreleyen IoT ekosistemi hakkında hassas URL'ler, IP adresleri, kullanılan yazılımlar vb. bilgileri açığa çıkarabilir. Bir saldırgan bu bilgileri ekosisteme yönelik saldırılar hazırlamak ve yürütmek için kullanabilir.

Örneğin, yapılandırma dosyaları ve metin dosyaları gibi çeşitli türdeki dosyalarda bu tür ilgili bilgiler yer alabilir.

**Test Hedefleri**

- Cihaz belleğinde saklanan yapılandırma dosyaları gibi verilerin çevre ekosistem hakkında ilgili bilgiler içerip içermediği belirlenmelidir.

**İyileştirme / Çözüm**

Bilgilerin açığa çıkması, cihazın çalıştırılması için gereken minimum düzeye indirilmelidir. Açığa çıkan bilgiler değerlendirilmeli ve gereksiz yere dahil edilen tüm veriler kaldırılmalıdır.

**Kaynaklar**

Bu test senaryosu için aşağıdaki kaynaklardan veriler birleştirilmiştir:

* ["IoT Pentesting Guide"][iot_pentesting_guide] (Aditya Gupta)
* ["IoT Penetration Testing Cookbook"][iot_penetration_testing_cookbook] (Aaron Guzman, Aditya Gupta)
* ["The IoT Hacker's Handbook"][iot_hackers_handbook] (Aditya Gupta)

Bu test senaryosu şuna dayanmaktadır: [ISTG-FW-INFO-003](../firmware/README.md#disclosure-of-ecosystem-details-istg-fw-info-003).

### Kullanıcı Verilerinin Açığa Çıkması (ISTG-MEM-INFO-004)

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

Çalışma zamanı (runtime) boyunca bir cihaz, kullanıcılarının kişisel verileri gibi farklı türlerde veriler toplar ve işler. Bu veriler güvenli bir şekilde saklanmazsa, bir saldırgan bunları cihazdan kurtarabilir.

**Test Hedefleri**

- Kullanıcı verilerine yetkisiz kişilerce erişilip erişilemeyeceği kontrol edilmelidir.

**İyileştirme / Çözüm**

Kullanıcı verilerine erişim yalnızca erişmesi gereken bireylere ve süreçlere verilmelidir. Yetkisiz veya düzgün yetkilendirilmemiş hiçbir birey kullanıcı verilerini geri getirememelidir.

**Kaynaklar**

Bu test senaryosu için aşağıdaki kaynaklardan veriler birleştirilmiştir:

* ["IoT Pentesting Guide"][iot_pentesting_guide] (Aditya Gupta)
* ["IoT Penetration Testing Cookbook"][iot_penetration_testing_cookbook] (Aaron Guzman, Aditya Gupta)
* ["The IoT Hacker's Handbook"][iot_hackers_handbook] (Aditya Gupta)

Bu test senaryosu şuna dayanmaktadır: [ISTG-FW[INST]-INFO-001](../firmware/installed_firmware.md#disclosure-of-user-data-istg-fw[inst]-info-001).

### Güvensiz İkili Derleme Seçenekleri (ISTG-MEM-INFO-005)

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

Cihaz belleğinden çıkarılan ikilikler (binaries), derleyici ve bağlayıcı (linker) güvenlik bayrakları aracılığıyla etkinleştirilen standart istismar önleme özelliklerinden (exploit mitigations) yoksun olabilir. İkilikler doğrudan bellek yongalarından çıkarıldığında, cihazın istismar edilebilirlik durumunu anlamak için derleme güvenlik özellikleri değerlendirilebilir. PIE, stack canaries, NX, RELRO ve FORTIFY_SOURCE gibi korumaların bulunmaması; çıkarılan ikiliklerdeki zafiyetler için istismar geliştirme karmaşıklığını azaltarak Return-Oriented Programming (ROP) veya doğrudan kabuk kodu (shellcode) enjeksiyonu gibi tekniklere olanak tanır. Milyonlarca gömülü ve IoT cihazını etkileyen BusyBox'taki yığın arabellek taşması (stack buffer overflow) zafiyeti olan CVE-2022-48174 gibi gerçek dünya örnekleri, eksik stack canary ve ASLR korumalarının istismar eşiğini ne kadar düşürdüğünü kanıtlamaktadır.

**Test Hedefleri**

- Cihaz belleğinde tanımlanan ikilikler, aşağıdakiler dahil olmak üzere yaygın istismar önleme özelliklerinin varlığı veya yokluğu açısından analiz edilmelidir:
  - **PIE (Position Independent Executable):** İkili düzeyde ASLR'yi etkinleştirir, yükleme adreslerini rastgele hale getirir ve ROP saldırılarını karmaşıklaştırır.
  - **NX/W^X (No-Execute):** Yığın (stack) veya öbek (heap) gibi yazılabilir bellek bölgelerine enjekte edilen kodun yürütülmesini engeller.
  - **Stack Canaries (Stack Smashing Protector, SSP):** İşlev dönüşünden önce yığın tabanlı arabellek taşmalarını algılar.
  - **RELRO (Relocation Read-Only):** Dinamik bağlamadan sonra Genel Ofset Tablosunu (GOT) salt okunur olarak işaretleyerek üzerine yazma saldırılarına karşı sıkılaştırır.
  - **FORTIFY_SOURCE:** Derleme zamanında güvensiz C standart kütüphane işlevlerini sınır kontrollü varyantlarla değiştirir.
- İkili sıkılaştırma özelliklerini değerlendirmek için `checksec`, `readelf`, `objdump` ve `rabin2` gibi araçlar kullanılmalıdır.
- Tespit edilen eksik önlemler belgelenmeli ve ikili dosyanın rolü ile potansiyel istismar edilebilirliği bağlamında değerlendirilmelidir.

**İyileştirme / Çözüm**

Bellenim derleme süreçleri, derleyici ve bağlayıcı düzeyinde güvenlik sıkılaştırma özelliklerini etkinleştirmelidir. Ayrıntılı iyileştirme rehberliği için [ISTG-FW-INFO-004](../firmware/README.md#insecure-binary-compilation-options-istg-fw-info-004) bölümüne bakınız.

**Kaynaklar**

Bu test senaryosu için aşağıdaki kaynaklardan veriler birleştirilmiştir:

* ["IoT Pentesting Guide"][iot_pentesting_guide] (Aditya Gupta)
* ["IoT Penetration Testing Cookbook"][iot_penetration_testing_cookbook] (Aaron Guzman, Aditya Gupta)
* ["The IoT Hacker's Handbook"][iot_hackers_handbook] (Aditya Gupta)
* [OpenSSF Compiler Options Hardening Guide for C and C++][openssf_compiler_hardening]
* [CWE-119][cwe_119]: Bellek Arabelleği Sınırları İçindeki İşlemlerin Hatalı Kısıtlanması
* [CWE-121][cwe_121]: Yığın Tabanlı Arabellek Taşması (Stack-based Buffer Overflow)
* [CWE-693][cwe_693]: Koruma Mekanizması Başarısızlığı

Bu test senaryosu şuna dayanmaktadır: [ISTG-FW-INFO-004](../firmware/README.md#insecure-binary-compilation-options-istg-fw-info-004).

## Gizli Bilgiler / Secrets (ISTG-MEM-SCRT)

IoT cihazları genellikle üreticilerinin kontrol alanının dışında çalıştırılır. Yine de bellenim güncellemelerini istemek/almak veya bir bulut API'sine veri göndermek gibi nedenlerle ekosistemdeki diğer ağ düğümleriyle bağlantı kurmaları gerekir. Bu nedenle cihazın bir tür kimlik doğrulama bilgisi veya gizli anahtar sağlaması gerekebilir. Bu gizli bilgilerin çalınmasını ve cihazı taklit etmek için kullanılmasını önlemek amacıyla cihazda güvenli bir şekilde saklanması gerekir.

### Gizli Bilgilerin Şifrelenmemiş Olarak Saklanması (ISTG-MEM-SCRT-001)

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

Hassas veriler ve gizli bilgiler şifrelenmiş olarak saklanmalıdır; böylece bir saldırgan belleğe erişmeyi başarsa bile ilgili düz metin (plaintext) verilere erişemez.

Kullanımdaki kriptografik algoritmaların gücü [ISTG-MEM-CRYPT-001](#zayıf-kriptografik-algoritmaların-kullanımı-istg-mem-crypt-001) kapsamında ele alınacak olup bu test senaryosu için doğrudan geçerli değildir.

**Test Hedefleri**

- Cihaz belleğinin içeriği taranarak düz metin biçiminde gizli bilgiler içerip içermediği belirlenmelidir.

**İyileştirme / Çözüm**

Gizli bilgiler uygun kriptografik algoritmalar kullanılarak saklanmalıdır. Yalnızca gizli bilginin şifrelenmiş hali saklanmalıdır.

**Kaynaklar**

Bu test senaryosu için aşağıdaki kaynaklardan veriler birleştirilmiştir:

* ["IoT Pentesting Guide"][iot_pentesting_guide] (Aditya Gupta)
* ["IoT Penetration Testing Cookbook"][iot_penetration_testing_cookbook] (Aaron Guzman, Aditya Gupta)

Bu test senaryosu şuna dayanmaktadır: [ISTG-FW-SCRT-002](../firmware/README.md#unencrypted-storage-of-secrets-istg-fw-scrt-002).

## Kriptografi (ISTG-MEM-CRYPT)

Birçok IoT cihazının hassas verileri güvenli bir şekilde saklamak, kimlik doğrulama amacıyla veya diğer ağ düğümlerinden gelen şifreli verileri alıp doğrulamak için kriptografik algoritmalar uygulaması gerekir. Güvenli ve güncel standartlara uygun kriptografinin uygulanamaması; hassas verilerin ifşasına, cihaz arızalarına veya cihaz üzerindeki kontrolün kaybedilmesine yol açabilir.

### Zayıf Kriptografik Algoritmaların Kullanımı (ISTG-MEM-CRYPT-001)

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

Kriptografi çeşitli şekillerde uygulanabilir. Ancak gelişen teknolojiler, yeni algoritmalar ve artan bilgi işlem gücü nedeniyle günümüzde birçok eski kriptografik algoritma zayıf veya güvensiz olarak kabul edilmektedir. Bu nedenle ya daha yeni ve daha güçlü algoritmalar kullanılmalı ya da anahtar uzunluğu artırılarak veya alternatif çalışma modları kullanılarak mevcut algoritmalar uyarlanmalıdır.

Zayıf kriptografik algoritmaların kullanılması, bir saldırganın verilen bir şifreli metinden (ciphertext) düz metni (plaintext) makul bir sürede geri elde etmesine olanak tanıyabilir.

**Test Hedefleri**

- Cihazda saklanan veriler, şifrelenmiş veri segmentlerinin varlığı açısından kontrol edilmelidir. Şifreli segmentler bulunursa kullanılan algoritmaların tanımlanıp tanımlanamayacağı incelenmelidir.
- [ISTG-MEM-INFO-001](#kaynak-kod-ve-ikiliklerin-binaries-açığa-çıkması-istg-mem-info-001) ve [ISTG-MEM-INFO-002](#uygulama-ayrıntılarının-açığa-çıkması-istg-mem-info-002) temelinde, herhangi bir kaynak kodun, yapılandırma dosyasının vb. belirli kriptografik algoritmaların kullanımını ifşa edip etmediği kontrol edilmelidir.
- Algoritmaların tespit edilebilmesi durumunda, kullanılan algoritmaların ve yapılandırmalarının test sırasında yeterli bir güvenlik düzeyi sağlayıp sağlamadığı (örn. BSI'ın [TR-02102-1](https://www.bsi.bund.de/SharedDocs/Downloads/EN/BSI/Publications/TechGuidelines/TG02102/BSI-TR-02102-1.pdf?__blob=publicationFile&v=10) teknik kılavuzu gibi rehberlere başvurularak) belirlenmelidir.

**İyileştirme / Çözüm**

Yalnızca güçlü ve güncel standartlara uygun kriptografik algoritmalar kullanılmalıdır. Ayrıca bu algoritmalar, uygun bir anahtar uzunluğu veya çalışma modu gibi doğru parametreler ayarlanarak güvenli bir şekilde kullanılmalıdır.

**Kaynaklar**

Bu test senaryosu için aşağıdaki kaynaklardan veriler birleştirilmiştir:

* ["IoT Pentesting Guide"][iot_pentesting_guide] (Aditya Gupta)
* ["IoT Penetration Testing Cookbook"][iot_penetration_testing_cookbook] (Aaron Guzman, Aditya Gupta)

Bu test senaryosu şuna dayanmaktadır: [ISTG-FW-CRYPT-001](../firmware/README.md#usage-of-weak-cryptographic-algorithms-istg-fw-crypt-001).

[iot_pentesting_guide]: https://www.iotpentestingguide.com "IoT Pentesting Guide"
[iot_penetration_testing_cookbook]: https://www.packtpub.com/product/iot-penetration-testing-cookbook/9781787280571 "IoT Penetration Testing Cookbook"
[iot_hackers_handbook]: https://link.springer.com/book/10.1007/978-1-4842-4300-8 "The IoT Hacker's Handbook"
[openssf_compiler_hardening]: https://best.openssf.org/Compiler-Hardening-Guides/Compiler-Options-Hardening-Guide-for-C-and-C++.html "OpenSSF Compiler Options Hardening Guide for C and C++"
[cwe_119]: https://cwe.mitre.org/data/definitions/119.html "CWE-119: Improper Restriction of Operations within the Bounds of a Memory Buffer"
[cwe_121]: https://cwe.mitre.org/data/definitions/121.html "CWE-121: Stack-based Buffer Overflow"
[cwe_693]: https://cwe.mitre.org/data/definitions/693.html "CWE-693: Protection Mechanism Failure"
