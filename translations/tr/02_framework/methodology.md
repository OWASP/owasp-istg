# 2.3. Test Metodolojisi

Bu bölümde, IoT cihazı sızma testlerini gerçekleştirmeye yönelik bir metodoloji açıklanacaktır. [2.1. IoT Cihaz Modeli](./device_model.md) ve [2.2. Saldırgan Modeli](./attacker_model.md) bölümlerinde sunulan kavramlara dayanır ve önceden var olan sızma testi iş akışları ve çerçeveleriyle birlikte kullanılabilecek bir ek görevi görür. Metodoloji, bir IoT cihazı sızma testi sırasında gerçekleştirilmesi gereken temel test hususlarını kapsar. Bu nedenle, her bir münferit cihaz bileşeni için bir test senaryoları kataloğu içerir. Önceki bölümlerde açıklandığı gibi, uygulanabilir test senaryolarının özel seçimi, bu metodoloji bağlamında tasarlanan cihaz ve saldırgan modellerinin uygulanmasının sonuçlarına bağlıdır.

İlk olarak, bu metodolojinin diğer iş akışlarına nasıl entegre edilebileceği ve bu metodolojinin modelleri ve kavramlarının hangi adımlarda kullanılabileceği açıklanacaktır. Ardından, test sırasında uygulanabilecek ve belirli test senaryolarıyla sınırlı olmayan seçilmiş test teknikleri açıklanacaktır. Son olarak, test senaryoları kataloğunun yapısal kavramı izah edilecektir.

Diğer IoT sızma testi çerçeveleriyle karşılaştırıldığında bu metodoloji daha genel ancak kapsamlı bir yaklaşım izler. Belirli teknolojilerin veya standartların ayrıntılarıyla kısıtlanmadan, IoT bağlamında geçerli olan belirli güvenlik sorunları için test senaryoları (temel test hususları) tanımlar. Böylece bu metodoloji diğer çerçevelere göre daha esnektir; bu da IoT alanının değişkenliği göz önüne alındığında önemli bir avantajdır. Bununla birlikte metodoloji çeşitli teknolojilere uygulanabilir ve daha fazla özelleştirme için olanaklar sunar.

Birden fazla bileşen için geçerli olan test senaryolarının bu bölüme dahil edilmediği unutulmamalıdır. Test senaryolarının tam listesi [3. Test Senaryosu Kataloğu](../03_test_cases/README.md) bölümünde bulunabilir.

## Diğer İş Akışlarına ve Çerçevelere Entegrasyon

Verimlilik sağlamak amacıyla, bu metodolojiyi dahil etmek için önceden var olan iş akışlarında büyük ayarlamalar yapılması gerekmemelidir. Aşağıda, BSI sızma testi modeli ([kaynak][bsi_pentest]) örneğine dayalı olarak bu metodolojinin diğer çerçevelere nasıl entegre edilebileceği gösterilecektir. Bu durumda genel test iş akışında herhangi bir değişiklik yapılması gerekmez.

Bu kılavuzda önerilen metodoloji aşağıdaki adımları kolaylaştırmak için kullanılabilir:

- **Test Kapsamının ve Test Perspektifinin Netleştirilmesi:** Metodoloji, cihaz ve saldırgan modelleri biçiminde ortak bir terminoloji oluşturarak iletişimi kolaylaştırır; BSI modelinin 1. ve 3. aşamaları sırasında hizmet alan taraf ile test hedeflerinin ve koşullarının netleştirilmesini destekler ([kaynak][bsi_pentest]). Ayrıca cihaz modeli, potansiyel saldırı vektörlerini belirlemek için belirli bir IoT cihazının mimarisiyle karşılaştırılabilecek genel bir şema sunarak 2. aşama sırasında test ekibini destekler.
- **Test Yürütme ve Dokümantasyon:** Test senaryoları kataloğu, aktif test sırasında (BSI modelinin 4. aşaması ([kaynak][bsi_pentest])) test uzmanları için bir kılavuz görevi görür. Test kapsamına ve test perspektifine bağlı olarak, test sırasında gerçekleştirilmesi gereken uygulanabilir test senaryoları tanımlanır. Böylece test kataloğu, tüm zorunlu testlerin gerçekleştirildiğinden emin olmak için bir kontrol listesi olarak kullanılabilir. Ayrıca, gerçekleştirilen test senaryoları raporda referans gösterilebildiğinden, 5. aşama sırasında test prosedürünün tekrarlanabilir bir şekilde şeffaf olarak belgelenmesine olanak tanır.

## Hiyerarşik Yapının Tanımı

Aşağıda, test senaryosu kataloğunun genel yapısı ve bir test senaryosunun genel düzeni tanımlanacaktır.

### Test Senaryoları Kataloğunun Yapısı

Test senaryoları kataloğu hiyerarşik (ağaç) bir yapı izleyecektir. Tek bir kök düğümden (IOT) başlayarak, cihaz modelinin her bir bileşeni bir alt düğüm (child node) olarak temsil edilecek ve böylece kendi alt ağacını oluşturacaktır. Daha sonra, bileşen düğümlerine alt öğeler olarak başka düğümler eklenecek ve nihayetinde her bir test senaryosu bir yaprak düğüm (leaf node) haline gelecektir. Bu yapıyı içeren benzersiz bir tanımlayıcı (ID) her bir düğüme atanacak ve test raporunda veya diğer belgelerde referans gösterilmesine olanak tanıyacaktır.

Aşağıdaki hiyerarşik seviyeler ve düğüm türleri tanımlanmıştır:

- **Bileşen (Component):** İlk ana hiyerarşi düzeyi bileşendir (bkz. [2.1. IoT Cihaz Modeli](./device_model.md)). Bileşenin türü (cihaz içi öğe/arayüz), basitlik sağlamak amacıyla hiyerarşiye dahil edilmemiştir.
  *Kısa gösterim: 2 - 5 büyük alfabetik karakter*
  *Örnekler: ISTG-PROC, ISTG-MEM, ISTG-FW, ISTG-DES, ISTG-INT, ISTG-PHY, ISTG-WRLS, ISTG-UI*

- **Bileşen Uzmanlaşması / Özelleştirmesi (Component Specialization - İsteğe Bağlı):** İsteğe bağlı bileşen uzmanlaşmaları, bir bileşenin yalnızca belirli parçaları veya somut örnekleri için geçerli olan test senaryolarını tanımlamak için kullanılabilir (örn. bellenim bileşeni - ISTG-FW - için bir uzmanlaşma olarak yüklü bellenim - ISTG-FW[INST] - veya dahili arayüz bileşeni - ISTG-INT - için bir uzmanlaşma olarak SPI - ISTG-INT[SPI]).
  Varsayılan olarak bileşen uzmanlaşmaları, üst düğümleri için tanımlanan tüm kategorileri ve test senaryolarını miras alır.
  Gerekirse uzmanlaşmaların zincirlenmesine izin verilir (örneğin bellenim güncellemesi - ISTG-FW[UPDT] - uzmanlaşması olarak havadan güncelleme - ISTG-FW[UPDT][OTA]).
  *Kısa gösterim: Köşeli parantez içinde 2 - 5 büyük alfabetik karakter*
  *Örnekler: ISTG-FW[INST], ISTG-FW[UPDT]*

- **Kategori (Category):** İkinci ana hiyerarşi düzeyi, test senaryolarını gruplandırmak için kullanılabilen kategoridir (örn. yetkilendirme ile ilgili tüm test senaryoları AUTHZ kategorisinde gruplandırılabilir).
  *Kısa gösterim: 2 - 5 büyük alfabetik karakter*
  *Örnekler: ISTG-\*-AUTHZ, ISTG-\*-INFO, ISTG-\*-CONF*

- **Test Senaryosu (Test Case):** Üçüncü ana hiyerarşi düzeyi test senaryosudur. Ayrıntılar için [3. Test Senaryosu Kataloğu](../03_test_cases/README.md) bölümüne bakınız.
  *Kısa gösterim: Test senaryosunun üç basamaklı artan numarası.*
  *Örnekler: ISTG-FW-INFO-001, ISTG-FW-INFO-002, ISTG-FW-INFO-003*

Bu tür bir yapı, belirli bir cihaz veya test senaryosu için geçerli olmayan düğümlerin (örn. bileşenler, bileşen uzmanlaşmaları ve kategoriler) seçimi kaldırılarak uygulanabilir alt ağaçların verimli bir şekilde belirlenmesine olanak tanır.

<table>
    <thead>
        <tr>
            <th>Hiyerarşi Seviyesi</th>
            <th>ID</th>
            <th>Açıklama</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>0</td>
            <td>IOT</td>
            <td>Kök Düğüm (Root Node)</td>
        </tr>
        <tr>
            <td rowspan="14" valign="top">1</td>
            <td colspan="2"><b>Bileşen (Component)</b></td>
        </tr>
        <tr>
            <td>ISTG-PROC</td>
            <td>İşlem Birimi (Processing Unit)</td>
        </tr>
        <tr>
            <td>ISTG-MEM</td>
            <td>Bellek (Memory)</td>
        </tr>
        <tr>
            <td>ISTG-FW</td>
            <td>Bellenim (Firmware)</td>
        </tr>
        <tr>
            <td>ISTG-DES</td>
            <td>Veri Değişim Hizmeti (Data Exchange Service)</td>
        </tr>
        <tr>
            <td>ISTG-INT</td>
            <td>Dahili Arayüz (Internal Interface)</td>
        </tr>
        <tr>
            <td>ISTG-PHY</td>
            <td>Fiziksel Arayüz (Physical Interface)</td>
        </tr>
        <tr>
            <td>ISTG-WRLS</td>
            <td>Kablosuz Arayüz (Wireless Interface)</td>
        </tr>
        <tr>
            <td>ISTG-UI</td>
            <td>Kullanıcı Arayüzü (User Interface)</td>
        </tr>
        <tr>
            <td>ISTG-*</td>
            <td>Özel Bileşen <i>(gelecekteki uzantılar için yer tutucu)</i></td>
        </tr>
        <tr>
            <td colspan="2"><b>Bileşen Uzmanlaşması (İsteğe Bağlı)</b></td>
        </tr>
        <tr>
            <td>ISTG-FW[INST]</td>
            <td>Yüklü Bellenim (Installed Firmware)</td>
        </tr>
        <tr>
            <td>ISTG-FW[UPDT]</td>
            <td>Bellenim Güncelleme Mekanizması (Firmware Update Mechanism)</td>
        </tr>
        <tr>
            <td>ISTG-*[*]</td>
            <td>Özel Bileşen Uzmanlaşması <i>(gelecekteki uzantılar için yer tutucu)</i></td>
        </tr>
        <tr>
            <td rowspan="10" valign="top">2</td>
            <td colspan="2"><b>Kategori (Category)</b></td>
        </tr>
        <tr>
            <td>ISTG-*-AUTHZ</td>
            <td>Yetkilendirme (Authorization)</td>
        </tr>
        <tr>
            <td>ISTG-*-INFO</td>
            <td>Bilgi Toplama (Information Gathering)</td>
        </tr>
        <tr>
            <td>ISTG-*-CRYPT</td>
            <td>Kriptografi (Cryptography)</td>
        </tr>
        <tr>
            <td>ISTG-*-SCRT</td>
            <td>Gizli Bilgiler / Sırlar (Secrets)</td>
        </tr>
        <tr>
            <td>ISTG-*-CONF</td>
            <td>Yapılandırma ve Yama Yönetimi (Configuration & Patch Management)</td>
        </tr>
        <tr>
            <td>ISTG-*-LOGIC</td>
            <td>İş Mantığı (Business Logic)</td>
        </tr>
        <tr>
            <td>ISTG-*-INPV</td>
            <td>Girdi Doğrulama (Input Validation)</td>
        </tr>
        <tr>
            <td>ISTG-*-SIDEC</td>
            <td>Yan Kanal Saldırıları (Side-Channel Attacks)</td>
        </tr>
        <tr>
            <td>ISTG-*-*</td>
            <td>Özel Kategori <i>(gelecekteki uzantılar için yer tutucu)</i></td>
        </tr>
        <tr>
            <td rowspan="5" valign="top">3</td>
            <td colspan="2"><b>Test Senaryosu (Test Case)</b></td>
        </tr>
        <tr>
            <td>ISTG-*-INFO-001</td>
            <td>Kaynak Kod ve İkili Dosyaların İfşası</td>
        </tr>
        <tr>
            <td>ISTG-*-INFO-002</td>
            <td>Uygulama Ayrıntılarının İfşası</td>
        </tr>
        <tr>
            <td>ISTG-*-INFO-003</td>
            <td>Ekosistem Ayrıntılarının İfşası</td>
        </tr>
        <tr>
            <td>ISTG-*-*-*</td>
            <td>Özel Test Senaryosu <i>(gelecekteki uzantılar için yer tutucu)</i></td>
        </tr>
    </tbody>
</table>

![image](../../src/img/Component_Overview.png)

### Test Senaryolarının Yapısı

Bir yaprak düğümle temsil edilen her bir münferit test senaryosu aşağıdaki bölümlere ayrılmıştır:

- **Gereksinimler (Requirements):** Test senaryosunu yürütmek için hangi fiziksel ve yetkilendirme erişim seviyelerinin gerekli olduğunu tanımlar.
- **Özet (Summary):** Test senaryosunun dayandığı güvenlik sorununun genel bir tanımını içerir.
- **Test Hedefleri (Test Objectives):** Test uzmanının gerçekleştirmesi gereken kontrollerin bir listesini sunar. Test uzmanı bu kontrolleri yaparak cihazın özette açıklanan güvenlik sorunundan etkilenip etkilenmediğini belirleyebilir.
- **İyileştirme / Çözüm (Remediation):** Güvenlik sorununu çözmek için uygulanabilecek potansiyel önlemlere ilişkin önerileri kapsar.

Bu bölümlere ek olarak, bir test senaryosu adlandırdığı araçlar, ilgili zafiyet veya zayıflık kayıtları (CWE/CVE) ve kanıt sağladığı [OWASP IoT Güvenlik Doğrulama Standardı (ISVS)](https://owasp.org/IoT-Security-Verification-Standard-ISVS/) gereksinimleri gibi kendisine özgü kaynakları belirten bir **Kaynaklar (References)** bölümü içerebilir.

[bsi_pentest]: https://www.bsi.bund.de/SharedDocs/Downloads/EN/BSI/Publications/Studies/Penetration/penetration_pdf.pdf?__blob=publicationFile&v=1 "Study: A Penetration Testing Model"
[nvd]: https://nvd.nist.gov "National Vulnerability Database"
[owasp_fuzzing]: https://owasp.org/www-community/Fuzzing "Fuzzing"
