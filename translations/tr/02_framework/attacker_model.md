# 2.2. Saldırgan Modeli

Bu bölümde, belirli bir IoT cihazı için tehdit oluşturduğu varsayılan potansiyel saldırganlara dayalı test senaryoları seçim şeması açıklanacaktır. STRIDE modeli gibi tam kapsamlı bir tehdit ve risk modelleme yaklaşımının aksine, bu kılavuzda kullanılan saldırgan modeli, IoT cihazlarına yönelik tehditleri tanımlamak ve seçmek için daha sadeleştirilmiş ve verimli bir prosedür sunar.

Resmi bir tehdit ve risk modelleme yaklaşımının tercih edilmeme nedenleri şunlardır:

- **Tehdit ve risk modellemesi genellikle belirli bir uygulama tasarımına odaklanır.** Dolayısıyla, tanımlanan tehditler ve riskler belirli bir çözümün veya cihazın özel koşullarına dayanır; bu da farklı çözümleri birbiriyle karşılaştırmayı zorlaştırır.
- **Resmi bir tehdit ve risk analizi gerçekleştirmek, konunun karmaşıklığıyla birlikte artan önemli miktarda zaman gerektirir.** Resmi bir tehdit ve risk analizini sızma testleri için zorunlu bir gereklilik haline getirmek, daha uzun test sürelerine ve dolayısıyla test başına daha yüksek maliyetlere yol açacaktır.

Potansiyel saldırgan yelpazesi, anonim küresel saldırganlardan ayrıcalıklı bireylere ve cihazın son kullanıcılarına kadar uzanır. Sonraki bölümlerde açıklanacağı üzere saldırganlar listesi, test perspektifini temsil eden minimum ve maksimum erişim gereksinimleri tanımlanarak daraltılabilir. Her cihaz bileşeni ve test senaryosu, ilgili testleri gerçekleştirmek için gereken erişim seviyesiyle etiketlenecektir. Böylece, test kapsamında yer alan cihaz bileşenlerinin listesi ve uygulanabilir test senaryoları listesi, saldırgan modelinin cihaz modelinden elde edilen sonuçlara uygulanmasıyla ortaya çıkacaktır.

Bu bölüm kapsamında "IoT cihazı" teriminin tek bir cihazı veya cihaz türünü ifade ettiği, kılavuzun diğer bölümlerinde ise genel olarak IoT cihazlarını ifade ettiği unutulmamalıdır.

## Saldırgan Modelinin Kavramsal Temeli

Bu saldırgan modeli, potansiyel saldırgan gruplarını erişim yeteneklerine[^1] göre karakterize edecektir. Bu saldırgan modeli için kullanılan metrikler [CVSS][cvss] (Ortak Zafiyet Puanlama Sistemi) metriklerine dayanmaktadır. CVSS temel olarak web uygulamaları ve bilgisayar ağları alanındaki zafiyetlerin ciddiyetini derecelendirmek için kullanılsa da, saldırganların yeteneklerini ve belirli güvenlik sorunlarını istismar etmek için gereken koşulları değerlendirmek için anlaşılır ve doğrudan bir yaklaşım uygular. CVSS'e benzer bir model kullanmanın bir diğer faydası da birçok güvenlik uzmanının halihazırda CVSS ile çalışıyor olmasıdır. Dolayısıyla birçok test uzmanı ve üretici/operatör bu sisteme aşinadır; bu da saldırgan modelinin kabul edilebilirliğine katkıda bulunur.

CVSS aşağıdaki istismar edilebilirlik (exploitability) metriklerini tanımlar:

- **Saldırı vektörü (Attack vector):** "Bu metrik, güvenlik açığının istismar edilmesinin mümkün olduğu bağlamı yansıtır" ([kaynak][cvss]). Bu metriğin değerleri ağ erişiminden (örn. internet üzerinden) fiziksel erişime kadar uzanır. Saldırgan modelinde bu metrik **fiziksel erişim seviyesi** ile yansıtılacaktır.
- **Saldırı karmaşıklığı (Attack complexity):** "Bu metrik, güvenlik açığını istismar etmek için saldırganın kontrolü dışında var olması gereken koşulları tanımlar" ([kaynak][cvss]). Saldırı karmaşıklığı, "saldırganın kontrolü dışındaki koşulları" ifade ettiğinden ve dolayısıyla potansiyel saldırganları kategorize etmek için doğrudan birincil olmadığından saldırgan modelinde kullanılmaz.
- **Gerekli ayrıcalıklar (Privileges required):** "Bu metrik, bir saldırganın güvenlik açığını başarıyla istismar etmeden önce sahip olması gereken ayrıcalıkların düzeyini tanımlar" ([kaynak][cvss]). Bu metriğin değerleri yoktan (yetkisiz) yükseğe kadar değişir. Gerekli ayrıcalıklar saldırgan modelinde **yetkilendirme erişim seviyesi** ile temsil edilir.
- **Kullanıcı etkileşimi (User interaction):** "Bu metrik, savunmasız bileşenin başarılı bir şekilde ele geçirilmesine saldırgan dışındaki bir insan kullanıcının katılma gereksinimini yakalar" ([kaynak][cvss]). Meşru kullanıcıların etkileşim zorunluluğu, bir güvenlik açığının istismar edilebilirliği için geçerli olmakla birlikte, uygulanabilir test senaryolarının seçimi için doğrudan belirleyici olmadığından saldırgan modelinde dikkate alınmayacaktır.

[^1]: BT güvenliği açısından saldırganlar genellikle saldırganlık düzeyleri ve kaynakları (işlem gücü, zaman, para) gibi ek faktörlere göre de karakterize edilir. Ancak bu faktörlerin uygulanabilir test senaryolarının seçimi üzerinde etkisi yoktur veya çok azdır.

## Erişim Seviyeleri

Bu saldırgan modeli kapsamında erişim seviyeleri, belirli bir birey grubu (erişim grubu) ile IoT cihazı arasındaki ilişkinin bir ölçüsüdür. Erişim grubundaki bireylerin cihazla nasıl etkileşime girebilmelerinin hedeflendiğini tanımlar. Bunlar fiziksel etkileşimler veya mantıksal yetkilendirme etkileşimleri olabilir.

Bireylerin cihaza ne kadar yaklaşabileceğinin derecesi **fiziksel erişim seviyesi** ile ölçülür. Fiziksel erişim seviyesi, CVSS "saldırı vektörü" metriğinin bir uyarlamasıdır ve hedef cihaza yönelik saldırıları gerçekleştirmek için gereken fiziksel bağlamı yansıtır. Bu nedenle CVSS'deki orijinal değerlerden bazıları kullanılmıştır (ağ, yerel, fiziksel). Ancak, yerel erişimin açıklaması fiziksel bağlama odaklanacak şekilde ayarlanmıştır. Ek olarak, CVSS'de tanımlanan fiziksel erişim iki seviyeye ayrılmıştır: **invaziv olmayan (non-invasive)** ve **invaziv (invasive) fiziksel erişim**. Bunun nedeni, bazı IoT cihazlarının kilitli veya mühürlü kasalar gibi cihaz içi öğelere erişimi kısıtlayan özel önlemlerle korunmasıdır. Bu durumda, saldırganlar makul bir süre içinde cihazın iç donanımına erişemeyebilir; bu nedenle yalnızca invaziv olmayan fiziksel erişime sahiptirler. Diğer cihazlar ise örneğin vidaları sökülerek kısa sürede açılabilen muhafazalara sahiptir. Dolayısıyla saldırganlar cihazın dahili donanımına erişebilir ve bu sayede invaziv fiziksel erişim elde edebilir. Genel olarak fiziksel erişim seviyesi; coğrafi konum, bina güvenliği veya cihaz muhafazası gibi faktörlerden etkilenebilir.

Aşağıdaki fiziksel erişim seviyeleri tanımlanmıştır:

1. **Uzak erişim (*PA-1 - Remote access*):** Birey ile cihaz arasında rastgele bir fiziksel mesafe vardır. Uzaktan erişime sahip bir saldırgan dünyanın herhangi bir yerinde bulunabilir; bu da genellikle cihazın bir Geniş Alan Ağı (GAN/Internet) üzerinden doğrudan erişilebilir olduğu anlamına gelir.
2. **Yerel erişim (*PA-2 - Local access*):** Birey ile cihaz arasında sınırlı bir fiziksel mesafe[^2] vardır, ancak doğrudan fiziksel temas mümkün değildir. Yerel erişime sahip bir saldırgan cihazı yakın mesafeden kullanabilir; bu da genellikle cihazın bir Yerel Alan Ağı (LAN) veya Kablosuz Yerel Alan Ağı (WLAN) üzerinden doğrudan erişilebilir olduğu anlamına gelir.
3. **İnvaziv olmayan erişim (*PA-3 - Non-invasive access*):** Birey ile cihaz arasında fiziksel mesafe yoktur, ancak birey cihaz içi öğelere doğrudan fiziksel olarak erişemez (yani cihaz muhafazasını/kasasını kolayca açamaz).
4. **İnvaziv erişim (*PA-4 - Invasive access*):** Birey ile cihaz arasında fiziksel bir mesafe yoktur ve birey cihaz içi donanım öğelerine doğrudan fiziksel olarak erişebilir (yani cihaz kasasını açabilir).

Bireylerin dijital yetki ve ayrıcalıkları **yetkilendirme erişim seviyesi** ile ölçülür. Yetkilendirme erişim seviyesi, CVSS "gerekli ayrıcalıklar" metriğinin bir uyarlamasıdır. CVSS'de tanımlanan değerlere ek olarak, yüksek ayrıcalıkların üzerine **üretici düzeyinde erişim** adı verilen başka bir ayrıcalık seviyesi eklenmiştir. Genellikle operatörün kontrol bölgesi içinden (örn. bir veri merkezinde) çalıştırılan web uygulamaları ve bilgisayar ağlarının aksine, IoT cihazları genellikle bu kontrol bölgesinin dışında çalıştırılır. Bakım ve hata ayıklama erişimini güvence altına almak için kullanılan yerleşik yöntemler (örn. bakım erişimini veri merkezindeki önceden tanımlanmış alt ağlar, IP adresleri veya fiziksel bağlantı noktalarıyla sınırlamak) her zaman uygulanamaz. Bu nedenle, üretici düzeyinde erişime sahip bir cihaza yönelik saldırılar mümkün olabilir. Genel olarak yetkilendirme erişim seviyesi, güvenlik politikaları veya rol tabanlı erişim modelleri gibi faktörlerden etkilenebilir.

Aşağıdaki yetkilendirme erişim seviyeleri tanımlanmıştır:

1. **Yetkisiz erişim (*AA-1 - Unauthorized access*):** Bir birey cihaz bileşenine anonim olarak erişebilir. Anonim erişime sahip saldırganlar kayıtlı olmayan herhangi bir kullanıcı olabilir.
2. **Düşük ayrıcalıklı erişim (*AA-2 - Low-privileged access*):** Bir birey cihaz bileşenine yalnızca kimliği doğrulanmışsa ve standart yetkilendirme ayrıcalıklarına sahipse erişebilir. Düşük ayrıcalıklı erişime sahip saldırganlar herhangi bir kayıtlı kullanıcı olabilir.
3. **Yüksek ayrıcalıklı erişim (*AA-3 - High-privileged access*):** Bir birey cihaz bileşenine yalnızca kimliği doğrulanmışsa ve kapsamlı ayrıcalıklara sahipse erişebilir. "Kapsamlı ayrıcalıklar" terimi, bireylerin cihaz bileşeninin tüm kayıtlı kullanıcılarına açık olmayan kısıtlı işlevlere (örn. yapılandırma ayarları, yönetim paneli) erişebildiği anlamına gelir.
4. **Üretici düzeyinde erişim (*AA-4 - Manufacturer-level access*):** Bir birey cihaz bileşenine yalnızca kimliği doğrulanmışsa ve üretici düzeyinde yetkilendirme ayrıcalıklarına sahipse erişebilir. Yüksek ayrıcalıklı erişimin aksine, üretici düzeyinde erişim hiçbir şekilde kısıtlanmamıştır ve örneğin cihazın geliştiricileri için hata ayıklama (debugging) erişimini, kaynak koduna erişimi veya bellenime kök (root) düzeyinde erişimi içerir.

[^2]: Sınırlı fiziksel mesafe tek başına belirli bir maksimum değerle sınırlı değildir. Kullanılan teknolojilere bağlı olarak maksimum mesafe birkaç metreden (örn. Bluetooth durumunda) birkaç kilometreye kadar (örn. LTE/LoRa durumunda) değişebilir.

## Cihaz Bileşenlerinin ve Erişim Seviyelerinin Eşleştirilmesi

Test sırasında test uzmanlarının bakış açısı, test için bir temel olarak seçilen minimum ve maksimum erişim seviyelerine göre belirlenecektir. Fiziksel ve yetkilendirme erişim seviyelerinin sızma testi ve kapsamı üzerinde farklı etkileri vardır.

**Fiziksel erişim seviyesi:**
- Fiziksel erişim seviyesi bir bütün olarak cihazı ifade eder. Dolayısıyla, bazı fiziksel erişim seviyeleri belirli cihaz bileşenlerinin verilen seviyede test edilemeyeceğini doğrudan tanımlar; çünkü saldırgan bu bileşenlerle hiçbir şekilde etkileşime giremez. Fiziksel erişim seviyeleri ile cihaz bileşenleri arasındaki ilişki aşağıdaki tabloda gösterilmiştir.
- Bir üreticinin veya operatörün özel gereksinimlerine bağlı olarak, minimum ve/veya maksimum fiziksel erişim seviyeleri test yürütmesi için katı sınırlar olabilir; çünkü hizmeti alan taraf örneğin invaziv fiziksel erişim gerektiren belirli testleri özellikle kapsam dışı bırakmak isteyebilir.

**Yetkilendirme erişim seviyesi:**
- Yetkilendirme erişimi birden fazla cihaz bileşeni arasında farklı şekilde ele alınabileceğinden, yetkilendirme erişim seviyesi bir bütün olarak cihazdan ziyade münferit bir bileşene erişimi ifade eder. Dolayısıyla, yetkilendirme erişim seviyelerinin test kapsamı üzerindeki etkisi her zaman iş mantığının ve bileşen başına yetkilendirme/izin şemasının özel uygulamasına bağlıdır.
- Test perspektifi için minimum bir yetkilendirme erişim seviyesi seçmenin bir anlamı yoktur; çünkü cihazın (veya parçalarının) hedeflenenden daha düşük ayrıcalıklarla erişilip erişilemeyeceğini değerlendirmek zaten testin temel bir parçası olmalıdır.

Özetle saldırgan modeli, potansiyel saldırganların soyut bir temsilini oluşturmak için kullanılabilir. Belirli bir cihaz için operasyonel ortamında ne tür saldırganların tehdit olarak kabul edildiğini açıklamak için kullanılır. Diğer metodoloji ve modellerin aksine bu model daha akıcı bir şekilde kullanılabilir, dolayısıyla tam tehdit ve risk analizi yaklaşımlarına kıyasla daha verimlidir. Ayrıca, temel aldığı CVSS'e kıyasla IoT bağlamının özelliklerini daha fazla dikkate alır. Cihaz modeli ile birlikte test kapsamını ve test perspektifini tanımlamayı mümkün kılar; böylece hangi test senaryolarının gerçekleştirilebileceğini ve gerçekleştirilmesi gerektiğini belirler.

| Bileşen                   | PA-4  |   PA-3    |   PA-2    |   PA-1    |
| ------------------------- | :---: | :-------: | :-------: | :-------: |
| İşlem Birimi              | **✓** |           |           |           |
| Bellek                    | **✓** |           |           |           |
| Yüklü Bellenim            | **✓** | **?**[^3] | **?**[^3] | **?**[^3] |
| Bellenim Güncelleme Mekanizması | **✓** | **?**[^3] | **?**[^3] | **?**[^3] |
| Veri Değişim Hizmeti      | **✓** | **?**[^4] | **?**[^4] | **?**[^4] |
| Dahili Arayüz             | **✓** |           |           |           |
| Fiziksel Arayüz           | **✓** |   **✓**   | **?**[^5] |           |
| Kablosuz Arayüz           | **✓** |   **✓**   |   **✓**   |           |
| Kullanıcı Arayüzü         | **✓** |   **✓**   | **?**[^6] | **?**[^6] |

[^3]: Yüklü bellenim ve bellenim güncelleme mekanizması, bellenime doğrudan erişimin nasıl sağlanabildiğine bağlı olarak (örn. SSH üzerinden) invaziv olmayan (*PA-3*), yerel (*PA-2*) veya uzaktan fiziksel erişim (*PA-1*) ile test edilebilir.
[^4]: Veri değişim hizmetleri, uzaktan kontrol veya izleme amacıyla bu tür bir erişim için tasarlanıp tasarlanmadıklarına bağlı olarak invaziv olmayan (*PA-3*), yerel (*PA-2*) veya uzaktan fiziksel erişim (*PA-1*) ile test edilebilir.
[^5]: Fiziksel arayüzler, belirli koşullar altında (örn. fiziksel arayüz yerel bir ağa bağlıysa) yerel fiziksel erişim (*PA-2*) ile test edilebilir.
[^6]: Kullanıcı arayüzleri, uzaktan kontrol veya izleme amacıyla bu tür bir erişim için tasarlanıp tasarlanmadıklarına bağlı olarak yerel (*PA-2*) veya uzaktan fiziksel erişim (*PA-1*) ile test edilebilir.

[cvss]: https://www.first.org/cvss/ "Common Vulnerability Scoring System"
