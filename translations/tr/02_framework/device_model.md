# 2.1. IoT Cihaz Modeli

Bu bölüm, IoT cihazlarının genel yapısını temsil eden IoT cihaz modeline odaklanmaktadır. Cihaz modelinin oluşturulması, çözüm yaklaşımında tanımlanan hedeflere ulaşmak için ilk adımdır (bkz. [1. Giriş](../01_introduction/README.md)). [2.2. Saldırgan Modeli](./attacker_model.md), [2.3. Metodoloji](./methodology.md) ve [3. Test Senaryosu Kataloğu](../03_test_cases/README.md) bölümlerinde açıklanacak olan sonraki tüm adımlar bu cihaz modeline dayanacaktır.

## İlgili Çalışmalar

Cihaz modeli, IoT platformlarına yönelik bir referans mimari üzerine inşa edilmiştir. Ayrıca, cihaz modeli bir güvenlik bağlamında kullanılacağından, saldırı yüzeyi alanları (attack surface areas) biçimindeki potansiyel saldırı vektörleri de dikkate alınmıştır. Bunlar aşağıdaki ilgili çalışmalarla özetlenmiştir:

- **["Comparison of IoT Platform Architectures: A Field Study based on a Reference Architecture"][reference_architecture]:** Bu makalenin amacı, IoT ekosistemleri için bir referans mimari önermektir. Bu referans mimari "farklı platformların karşılaştırılmasını kolaylaştıran tek tip, soyut bir terminoloji olarak hizmet etmesi amacıyla özellikle soyut tutulmuştur" ([kaynak][reference_architecture]). Bu kılavuzda geliştirilen cihaz modelinin de belirli uygulama ve tasarımlardan bağımsız olarak farklı IoT cihazları için tek tip bir model işlevi görmesi gerektiğinden, Guth ve arkadaşlarının ([kaynak][reference_architecture]) referans modeli temel alınmıştır. Bununla birlikte, Guth ve arkadaşlarının modeli IoT cihazının kendisi açısından yüzeyseldir; cihazı (sürücüler dışında) parçalarını daha fazla ayrıştırmadan tek bir bileşen olarak tasvir eder. Bu nedenle, test kapsamının ayrıntılı olarak tanımlanmasına (belirli cihaz parçalarının dahil edilmesi ve hariç tutulması) izin vermediğinden bu kılavuz için yeterli değildir. Bu kılavuzda sunulan modelde, IoT cihazlarının münferit parçalarını daha fazla ayrıştırmak için bazı ayarlamalar yapılmıştır.

- **["IoT Attack Surface Areas Project"][owasp_iot_attack_surface_areas]:** OWASP; web ve mobil uygulama güvenliği gibi çeşitli teknik alanlarda düzenli olarak sızma testi metodolojileri ve popüler güvenlik riskleri koleksiyonları ("OWASP Top 10" olarak adlandırılır) yayınlamaktadır. Popülaritesi nedeniyle sızma testleriyle ilgili bilgiler için ana kaynaklardan biri haline gelmiştir. 2014 ve 2018 yıllarında OWASP, IoT alanına ilişkin bir güvenlik riskleri ilk 10 listesi de yayınlamıştır. "IoT Attack Surface Areas Project" kapsamında bahsedilen saldırı yüzeyi alanları, potansiyel saldırganlar tarafından hedeflenebilecek bir IoT çözümünün parçalarını temsil eder. Bu listenin IoT cihazları ve genel olarak IoT ekosistemleriyle ilgili birçok potansiyel saldırı vektörünü kapsaması nedeniyle, bu kılavuzda önerilen cihaz modeli için de bir temel olarak kullanılmıştır. Ancak, özellikle donanım tarafında IoT cihazı uygulamalarının ayrıntılarını daha iyi ayrıştırmak için bazı ayarlamalar yapılmıştır. Ayrıca, "IoT Attack Surface Areas Project" yalnızca cihaz parçalarının birbirleriyle nasıl etkileşime girdiğini belirtmeyen basit bir listeden oluşur; her bir cihaz parçasının (veya saldırı yüzeyinin) özelliklerini tanımlamada yetersiz kalır ve bu durum "Cihaz Belleği" ile "Yerel Veri Depolama" gibi unsurları ayırt etmeyi zorlaştırır. ([kaynak][owasp_iot_attack_surface_areas])

## Cihaz Sınırları

Bir IoT cihazına ait bileşenler ile çevreleyen IoT ekosisteminin bileşenleri arasında ayrım yapabilmek için öncelikle bir IoT cihazının sınırlarını tanımlamak gerekir. Bir IoT cihazı genel olarak, cihaz içi öğeleri cihaz dışı öğelerden (fiziksel olarak) ayıran bir tür kasa/muhafaza (enclosure) ile çevrilidir.

Dahili ve harici unsurlar arasındaki etkileşimler yalnızca arayüzler (interfaces) aracılığıyla mümkündür. Bu kılavuz kapsamında söz konusu arayüzler kasanın bir parçası olarak kabul edilmez; bunun yerine ayrı olarak kategorize edilir (bkz. [Arayüzler](#arayüzler)).

Bir sonraki bölümde açıklanacağı üzere "bileşen" terimi, bir sızma testinin konusu olabilecek bir öğeyi ifade eder. Bu nedenle, cihaz içi öğeler ve arayüzler bu kılavuz kapsamında birer bileşen olarak değerlendirilir.

## Bileşenler

Önceki bölümlerde tanıtıldığı gibi, önerilen cihaz modeli IoT cihazlarının oluştuğu parçaların genelleştirilmiş bir seçkisini sunmalıdır. Bu parçalar **bileşenler** olarak anılacaktır. Her bileşen, teorik olarak ayrı ayrı test edilebilen bir yazılım ve/veya donanım parçasıdır. Bir IoT cihazı için sızma testi kapsamı bu nedenle bir bileşenler listesi olarak tanımlanabilir.

### Cihaz İçi Öğeler

Her cihaz içi öğe, cihaz kasasının içinde yer alan bir bileşendir. Dolayısıyla IoT cihazının bir parçasıdır. IoT cihazları genellikle OWASP tarafından oluşturulan saldırı yüzeyleri listesinde de belirtilen aşağıdaki dahili öğelerden oluşur ([kaynak][owasp_iot_attack_surface_areas]):

- **İşlem birimi (Processing unit):** İşlemci olarak da adlandırılan işlem birimi, veri işleme görevlerinin yönetilmesinden ve yürütülmesinden sorumludur. Bu görevler, bellekten yüklenen bir komut dizisi olarak tanımlanır. Bir cihaz, temel işlevlerini (bellenim tarafından tanımlanan) yerine getiren en az bir merkezi işlem birimine (CPU) sahiptir. Bununla birlikte, daha karmaşık cihazlar belirli alt görevlere atanmış ek işlem birimleriyle de donatılmış olabilir. Tek bir devre üzerine inşa edilmiş mikroişlemciler özel bir işlemci türüdür. Mikrodenetleyiciler (microcontrollers) ise analog ve dijital giriş/çıkışlara da sahip mikroişlemcilerdir. Genellikle bir cihazın davranışını kontrol etmek için kullanılırlar ve gömülü sistemler alanında sıklıkla tercih edilirler. ([kaynak][ekomp_processor])

  *Örnekler: x86 işlemci, ARM işlemci, AVR işlemci*

- **Bellek (Memory):** Bellek; programlar (işlem birimi için komutlar) ve bilgiler gibi verileri ikili (binary) formatta depolamak için kullanılır. Bellek türüne bağlı olarak, bir işlem birimi tarafından işlenirken verileri geçici olarak depolamak (birincil bellek veya önbellek) ya da cihaz kapalıyken bile verileri kalıcı olarak saklamak (ikincil bellek) için kullanılır. Flash bellek özel bir ikincil bellek türüdür. Enerji tasarruflu olması, daha az ısı üretmesi ve hareketli parçaların bulunmaması nedeniyle titreşime ve manyetik alanlara karşı daha az duyarlı olması sebebiyle birçok cihazda yaygın olarak kullanılır. Flash bellek yarı iletken teknolojisine dayanır ve verilere hızlı ve kalıcı erişim (okuma, yazma, silme) sağlayabilir. ([kaynak][ekomp_flash_memory], [kaynak][ekomp_memory])

  *Örnekler: EEPROM, flash bellek, NAND/NOR Flash*

- **Bellenim (Firmware):** "Bellenim, bir donanım cihazı üzerinde programlanmış bir yazılım programı veya komutlar kümesidir" ([kaynak][tech_terms_firmware]). Cihazı ve cihaz içi ile cihaz dışı unsurlar arasındaki iletişimi (veri değişim hizmetleri aracılığıyla veri girişi ve çıkışı) kontrol etmek için kullanılır. Bellenim bir bellekte saklanır ve bir işlem birimi tarafından yürütülür. Cihaz bellenimi açısından aşağıdaki bileşenler bir sızma testi için potansiyel hedefler olabilir:

  - **Yüklü bellenim (Installed firmware):** Bir cihaza halihazırda yüklenmiş olan bellenimi ifade eder. Dinamik analizlerin hedefi olabilir ve genellikle hassas kullanıcı verilerinin depolanmasını ve işlenmesini yönetir.
  - **Bellenim güncelleme mekanizması (Firmware update mechanism):** Bellenimin bir parçasıdır ve bellenim güncellemelerinin (bellenim paketleri şeklinde) bir cihaza nasıl yüklenebileceğini tanımlar. Bellenim güncelleme sürecinin kritik bir sorumluluğu, yalnızca uygun ve güvenilir bellenim paketlerinin yüklenip çalıştırılabilmesini sağlamaktır.[^1]

  *Örnekler: İşletim sistemi (OS), Gerçek Zamanlı İşletim Sistemi (RTOS), bare-metal gömülü bellenim*

- **Veri değişim hizmeti (Data exchange service):** Bir arayüz (örn. ağ, veri yolu) aracılığıyla iki veya daha fazla bileşen arasında veri aktarmak için kullanılan programları veya program parçalarını ifade eder. Bu hizmetler bellenimin bir parçasıdır ve veri iletmek, veri almak veya her ikisi için kullanılabilir.

  *Örnekler: Ağ servisi, hata ayıklama (debug) servisi, veri yolu dinleyicisi (bus listener)*

[^1]: Bir bellenim güncelleme mekanizmasının testini gerçekleştirmek için bir bellenim paketi gereklidir. Bir bellenim paketi ayrı olarak da incelenebileceğinden, bu paket de bir bileşen olarak kabul edilebilir. Ancak, bu kılavuz yalnızca cihaz içi öğelere ve cihaz arayüzlerine odaklandığından bellenim paketleri kapsam dışındadır. Yüklü bellenimin aksine, bir güncelleme paketi önemli veriler içerebilecek bellenim başlığını (header) da içerir.

### Arayüzler

İki veya daha fazla bileşeni birbirine bağlamak için arayüzler gereklidir. Cihaz içi öğeler arasındaki veya cihaz içi ile cihaz dışı öğeler arasındaki etkileşimler yalnızca arayüzler aracılığıyla mümkündür. Bir arayüzün hangi bileşenleri birbirine bağladığına bağlı olarak makineden makineye (M2M) veya insandan makineye (H2M) arayüz olarak kategorize edilebilir. Bağlanan bileşenlerden en az biri cihaz içi bir öğe olduğu sürece arayüzün kendisi de cihazın bir parçasıdır.

Bu kılavuz kapsamında, tümü doğrudan veya dolaylı olarak OWASP tarafından oluşturulan saldırı yüzeyleri listesinde belirtilen aşağıdaki arayüz türleri ayırt edilecektir ([kaynak][owasp_iot_attack_surface_areas]):

- **Dahili arayüzler (Internal interfaces - makineden makineye):** Bu arayüzler cihaz içi öğeler arasında bağlantı kurmak için kullanılır ve cihaz kasasının dışından doğrudan erişilemez.

  *Örnekler: JTAG, UART, SPI, I2C*

- **Fiziksel arayüzler (Physical interfaces - makineden makineye):** Fiziksel arayüzler, bileşenler veya bu bileşenlerin ilgili arayüzleri arasındaki fiziksel bir bağlantıya dayalı olarak cihaz içi ve cihaz dışı öğeler arasında bir bağlantı kurmak için kullanılır. Bu nedenle fiziksel arayüzler, cihaz kasasına yerleştirilmiş bir soket veya bağlantı noktası (port) gerektirir ve böylece cihazın dışından erişilebilir durumdadır.

  *Örnekler: USB, Ethernet*

- **Kablosuz arayüzler (Wireless interfaces - makineden makineye):** Fiziksel arayüzlere benzer şekilde kablosuz arayüzler de cihaz içi ve cihaz dışı öğeler arasında bir bağlantı kurmak için kullanılır. Ancak kablosuz arayüzler arasındaki bağlantı fiziksel bir bağlantıya değil; radyo dalgalarına, optik sinyallere veya diğer kablosuz teknolojilere dayanır. Kablosuz arayüzlere cihazın dışından, genellikle fiziksel arayüzlere kıyasla daha uzak mesafelerden erişilebilir.

  *Örnekler: Wi-Fi, Bluetooth, BLE (Bluetooth Low Energy), ZigBee, LoRaWAN*

- **Kullanıcı arayüzleri (User interfaces - insandan makineye):** Yukarıda belirtilen diğer tüm arayüzlerin aksine, kullanıcı arayüzleri iki makine arasında bağlantı kurmak için kullanılmaz. Bunun yerine amaçları, cihaz içi öğeler ile bir kullanıcı arasındaki etkileşime izin vermektir. Bu etkileşimler dokunmatik ekran örneğinde olduğu gibi fiziksel bir bağlantıya ya da kamera veya mikrofon örneğinde olduğu gibi kablosuz bağlantılara dayanabilir.

  *Örnekler: Dokunmatik ekran, kamera, mikrofon, yerel web arayüzü (cihaz üzerinde barındırılan web paneli)*

## Cihaz Modeli Şeması

Cihaz modeli, yukarıda belirtilen tüm bileşenlerin birleşimidir ve aşağıdaki şekilde görülebilir. Daha iyi okunabilirlik açısından çokluklar (cardinalities) dahil edilmemiş olsa da, bir IoT cihazına her bileşenden birden fazla örneğin yerleştirilebileceği unutulmamalıdır.

![IoT Cihaz Modeli](../../src/img/IoT_Device_Model.jpg)

Diğer modeller (örneğin [İlgili Çalışmalar](#i̇lgili-çalışmalar) bölümünde belirtilenler), sensörleri ve eyleyicileri (aktüatörleri) bir cihazın bileşenleri olarak dahil eder. Bu kılavuz kapsamında sensörler ve aktüatörler; fiziksel bağlantılar (örn. dokunmatik sensör, kapı kilidi kontrolü) veya kablosuz bağlantılar (örn. mikrofon, sıcaklık sensörü) aracılığıyla cihaz içi ve cihaz dışı öğeler ya da kullanıcılar arasında etkileşim sağladıkları için sırasıyla fiziksel, kablosuz veya kullanıcı arayüzleri olarak kabul edilir.

Bazı durumlarda, cihazların kendileri de cihaz sayılabilecek parçalar içermesi mümkündür (yani iç içe geçmiş cihazlar / nested devices). Bu durumda hangi arayüzlerin dahili ve harici olarak sınıflandırılacağı gözlemcinin bakış açısına bağlıdır. Belirleyici faktör, gözlemci ile arayüz arasındaki sınırlardır (bkz. [Cihaz Sınırları](#cihaz-sınırları), [Cihaz İçi Öğeler](#cihaz-i̇çi-öğeler) ve [Arayüzler](#arayüzler)).

Genel olarak, bu kılavuz bağlamında özel olarak geliştirilen cihaz modeli, çok çeşitli IoT cihazlarının soyut temsillerini oluşturmak ve paylaşmak için kullanılabilir. Diğer modellerin aksine bu model yalnızca IoT cihazına ve inşa edildiği bileşenlere odaklanır. Bu nedenle model, cihaz uygulamalarını daha ayrıntılı bir şekilde tanımlamaya olanak tanır. Sonraki bölümlerde geliştirilen modeller ve kavramlarla birlikte, uygulanan belirli teknolojilerden veya standartlardan bağımsız olarak herhangi bir cihaz için geçerli test senaryolarının bir listesini derlemek mümkündür.

[reference_architecture]: https://ieeexplore.ieee.org/document/7872918 "Comparison of IoT platform architectures: A field study based on a reference architecture"
[owasp_iot_attack_surface_areas]: https://wiki.owasp.org/index.php/OWASP_Internet_of_Things_Project#tab=IoT_Attack_Surface_Areas "OWASP IoT Attack Surface Areas Project"
[tech_terms_firmware]: https://techterms.com/definition/firmware "TechTerms.com"
[ekomp_processor]: https://www.elektronik-kompendium.de/sites/com/0309161.htm "CPU - Central Processing Unit / Hauptprozessor"
[ekomp_flash_memory]: https://www.elektronik-kompendium.de/sites/com/0312261.htm "Flash-Speicher / Flash-Memory"
[ekomp_memory]: https://www.elektronik-kompendium.de/sites/com/1812051.htm "Speicherarchitektur"
