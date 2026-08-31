# 1. Giriş

## Motivasyon

Çok çeşitli cihazların Nesnelerin İnterneti (IoT) ekosistemine dahil edilmesi, ilgili çözümleri geliştiren üreticiler ve işleten kurumlar için yeni güvenlik zorluklarını beraberinde getirmektedir. Birçok farklı teknoloji, standart ve protokolün birbirine bağlanması nedeniyle; ağ güvenliği, veri güvenliği ve genel olarak BT güvenliği alanında homojen bir güvenlik seviyesi oluşturmak ve bunu sürdürmek ciddi bir çaba gerektirir. Buna ek olarak, IoT alanı hızla değişip geliştiğinden, üreticiler ve operatörler cihazlarına ve ağlarına yönelik olası tehditleri sürekli olarak izlemelidir.

Geleneksel olarak ağa bağlı bilgisayar sistemleri, ağlara ve kritik sistemlere yönelik fiziksel ve yetkilendirme erişimini kısıtlamak gibi yerleşik yöntemlerle korunabilirken; yukarıda belirtilen heterojenlik ve yeni ağ mimarileri nedeniyle bu yöntemlerin IoT cihazlarına ve ekosistemlerine uygulanması zor olabilir. Geleneksel bilgisayar ağlarıyla karşılaştırıldığında, IoT altyapıları coğrafi olarak son derece geniş bir alana yayılmış olabilir. Arka uç (backend) altyapısı geleneksel bilgisayar ağlarına benzer olsa bile, IoT cihazları rastgele bir konumda, hatta işleticinin güvenli bölgesinin tamamen dışında bulunabilir. Hatta bazı durumlarda (örneğin akıllı araçlar, akıllı ev cihazları veya paket teslimat istasyonları) bu cihazlar üçüncü tarafların ve potansiyel saldırganların fiziksel erişimine tamamen açıktır. Dolayısıyla, tek bir manipüle edilmiş cihaz bile tüm ekosistemi tehlikeye atmaya yeteceğinden, her bir IoT cihazı kullanıcı verileri ve tüm altyapı için potansiyel bir tehdit oluşturur.

Başarılı saldırı riskini azaltmak için üreticiler ve işleticiler, IoT çözümlerinin güvenlik seviyesini periyodik olarak değerlendirmelidir. Bu amaca yönelik en temel araçlardan biri sızma testidir (penetration testing). Sızma testinin amacı, IoT çözümleri içindeki güvenlik açıklarını tespit etmektir. Elde edilen sonuçlar, tespit edilen zafiyetlerin giderilmesi ve böylece güvenlik seviyesinin güçlendirilmesi için kullanılır.

## Zorluklar

Sızma testleri bağlamında, test prosedürünün şeffaf olması kritik öneme sahiptir. Aksi takdirde, üretici veya operatör test sonuçlarının anlamını tam olarak kavrayamayabilir ve yanlış çıkarımlarda bulunabilir. Ayrıca, test sonuçları tekrarlanabilir (reproducible) olmalıdır; böylece geliştiriciler bir zafiyetin nasıl istismar edildiğini tam olarak canlandırıp uygun bir yama hazırlayabilir ve yama uygulandıktan sonra doğrulama testi (retest) sağlıklı şekilde gerçekleştirilebilir.

Test prosedürlerini ve sonuçlarını karşılaştırılabilir kılmak ve aynı hedef üzerinde aynı testi gerçekleştiren iki veya daha fazla test uzmanının sonuçlarının farklılaşmamasını sağlamak amacıyla test metodolojileri geliştirilmiştir. Bu köklü metodolojiler; test sırasında dikkate alınması gereken temel hususları ve test senaryolarını kapsayan ortak bir yaklaşım tanımlar. Ne yazık ki, bu kılavuzun yazıldığı sırada IoT sızma testlerine yönelik yalnızca birkaç ve henüz tamamlanmamış test metodolojisi bulunmaktadır. Üstelik bu metodolojiler ya yalnızca belirli bir teknolojik alana odaklanmakta ya da henüz erken geliştirme aşamasında yer almaktadır.

## Amaçlar

Yukarıda belirtilen zorlukları çözmek amacıyla bu kılavuzun hedefi, genel temel test hususlarını içerecek şekilde IoT alanındaki uç cihazların sızma testlerine yönelik kapsamlı bir metodoloji geliştirmektir.

Metodoloji:

-   Belirli teknolojiler için daha ayrıntılı test senaryolarının sonradan eklenebilmesi amacıyla esnek biçimde genişletilebilir olmalıdır (*genişletilebilirlik / expandability*).
-   Belirli teknolojilerden veya cihaz türlerinden bağımsız olarak test prosedürlerinin (test adımları/senaryoları) ve sonuçlarının karşılaştırılmasına olanak tanımalıdır (*karşılaştırılabilirlik / comparability*).
-   Üreticiler/operatörler ile sızma testi hizmeti sağlayıcıları arasında ortak bir dil işlevi görmeli, anlaşılır bir terminoloji oluşturarak her iki taraf arasındaki iletişimi kolaylaştırmalıdır (*anlaşılırlık / comprehensibility*).
-   Sızma testi ekipleri tarafından yerleşik iş akışlarında büyük değişiklikler yapılmasına veya yeni aşamalar eklenmesine gerek kalmadan destekleyici bir araç olarak kullanılabilecek kadar verimli olmalıdır (*verimlilik / efficiency*).

## Hedef Kitle

Adından da anlaşılacağı gibi, OWASP IoT Güvenlik Test Rehberi (ISTG) temel olarak IoT, donanım ve gömülü sistemler alanlarındaki sızma testi uzmanları (penetration testers) ve güvenlik analistleri tarafından kullanılmak üzere tasarlanmıştır. Bununla birlikte, bu kılavuzda sunulan kavram ve test senaryolarından diğer paydaşlar da faydalanabilir:

### **Üretici (Builder)**

- **IoT Cihazı Üreticileri** (örn. mimarlar, mühendisler, geliştiriciler ve yöneticiler), ürünlerini etkileyebilecek potansiyel sorunlar ve zafiyetler hakkında fikir edinmek için bu kılavuzun içeriğinden yararlanabilir. Güvenlik açığı barındıran ürünler üretici için çeşitli zararlara (finansal kayıp, itibar kaybı vb.) yol açabileceğinden, belirli bir ürünün herhangi bir bağlamda veya operasyonel ortamda nasıl savunmasız olabileceğini anlamak kritik önem taşır. Tasarım ve geliştirme sürecinin erken aşamalarında farkındalığı ve anlayışı artırarak, ilgili maliyetleri mümkün olduğunca düşük tutarken uzun vadede ürün güvenliğini artırmak mümkündür.

### **Kırıcı / Test Uzmanı (Breaker)**

- **Sızma Testi Uzmanları ve Hata Avcıları (Bug Bounty Researchers)**, testlerini planlamak, test kapsamını, koşullarını ve yaklaşımını belirlemek için [2. IoT Güvenlik Test Çerçevesi](../02_framework/README.md) bölümünde sunulan kavramları kullanabilir. Testi gerçekleştirirken, [3. Test Senaryosu Kataloğu](../03_test_cases/README.md) içindeki test senaryoları ve ilgili [Kontrol Listeleri](../../checklists):
  - a) Hangi hususların neden, nasıl test edilmesi gerektiğini ve olası sorunların nasıl giderilebileceğini gösteren bir rehber olarak,
  - b) Tüm ilgili hususların incelendiğinden emin olmak ve testin tamamlanma durumunu takip etmek amacıyla kullanılabilir.
- **Güvenlik Danışmanları ve Güvenlik Yöneticileri**, bu kılavuzu ve içeriğini ekipleriyle ve müşterileriyle çalışmak ve yukarıda belirtilen paydaşlarla iletişim kurmak için ortak bir temel olarak kullanabilir. Özellikle bu kılavuzda tanımlanan terminoloji ve yapı, farklı ekipler ve kuruluşlar arasındaki iş birliğini kolaylaştırmaya yardımcı olacaktır.

### **Savunucu (Defender)**

- **IoT Cihazı Operatörleri** (örn. son kullanıcılar ve kurumlar), bu kılavuzdan üreticilere benzer şekilde yararlanabilir. Ancak, IoT cihazlarını çalıştıran operatörlerin genellikle tasarım ve geliştirme süreci üzerinde hiçbir etkisi veya çok az etkisi vardır. Bu nedenle odak noktaları, bir cihazın belirli bir operasyonel ortamda nasıl savunmasız olabileceğini ve cihazın güvenliğinin ihlal edilmesi durumunda bu ortamın nasıl etkilenebileceğini anlamaya yöneliktir.

## Temel Bir Kavram Olarak Modülerlik

Bu kılavuz, IoT cihazı sızma testleri için monolitik ve değişmez tek bir talimat kılavuzu değildir. Bunun yerine, IoT cihazlarıyla ilgili çeşitli teknolojiler için dinamik ve sürekli büyüyen bir test senaryoları koleksiyonu olarak görülmelidir.

Mevcut durumunda bu kılavuz, oldukça üst ve genel bir düzeydeki test senaryolarını içerir. Bu durum kasıtlıdır; çünkü kılavuzun temel versiyonunun mümkün olduğunca çok sayıda farklı IoT cihazına uygulanabilir olması hedeflenmiştir (*karşılaştırılabilirlik*). Bununla birlikte uzun vadeli hedef, belirli teknolojiler için daha ayrıntılı test senaryolarına sahip modüller eklenerek bu kılavuzun zaman içinde genişletilmesidir (*genişletilebilirlik*). Böylece kılavuz zamanla gelişecek ve çok daha ayrıntılı hale gelecektir.

## Çözüm Yaklaşımı

Bir sızma testinin hazırlığı sırasında, test prosedürü ve dolayısıyla test sonuçları üzerinde büyük etkisi olan bir dizi önemli kararın verilmesi gerekir. Bu kararların bir parçası da neyin test edilmesi gerektiğini (*testin kapsamı*) ve testin nasıl gerçekleştirilmesi gerektiğini (*test perspektifi*) netleştirmektir.

Önerilen çözüme ulaşmak için aşağıdaki yaklaşım seçilmiştir:

1. **Soyut, genelleştirilmiş bir IoT cihazını temsil eden IoT cihaz modelinin oluşturulması:**
   Bir IoT cihazı sızma testinin kapsamı belirlenmeden önce, ilk olarak bir IoT cihazının ne olduğu ve hangi parçalardan oluştuğu tanımlanmalıdır. Test kapsamı tanımını desteklemek için cihaz modeli, test kapsamına dahil edilebilecek veya kapsam dışı bırakılabilecek cihaz bileşenlerini içermelidir. Bu kılavuz, kardeş OWASP test kılavuzları diğer alanları kapsasa da, yalnızca doğrudan cihazın kendisine ait bileşenlere odaklanacaktır. Web uygulamaları, mobil uygulamalar ve arka uç sunucuları gibi cihaz harici tüm unsurlar bu kılavuzun bir parçası olmayacaktır. Cihaz modeli, IoT cihazlarının genel yapısını tasvir eden genelleştirilmiş bir şema görevi görecek ve böylece bu kılavuzda sunulan metodolojinin anlaşılırlığını ve karşılaştırılabilirliğini artıracaktır. Kılavuzun sonraki tüm bölümleri bu temele dayanacağından, cihaz modelinin oluşturulması zorunlu ve önemli bir ilk adımdır.

2. **Potansiyel saldırganları temsil eden ve kategorize eden bir saldırgan modelinin oluşturulması:**
   Kılavuz, cihaz modelinin her bir bileşeni için temel test hususlarını içerecektir. Bu nedenle, tüm cihaz bileşenleri için potansiyel test senaryolarından oluşan bir katalog barındıracaktır. Belirli bir IoT cihazı türü için bu test senaryolarının tümünün gerçekleştirilmesi gerekmeyebileceğinden, belirli bir cihazın gereksinimlerine ve hedeflenen operasyonel ortamına dayalı olarak uygulanabilir test senaryolarının seçilmesini sağlayan sistematik bir yaklaşım gereklidir. Saldırgan modeli, yaygın saldırgan gruplarını/türlerini tanımlayarak anlaşılırlık ve karşılaştırılabilirlik sağlayarak test perspektifinin tanımlanmasını destekleyecektir. Verimliliği korumak için saldırgan modeli kapsamlı tehdit ve risk analizi modellerini içermeyecektir. Bu aynı zamanda farklı cihaz uygulamaları arasındaki karşılaştırılabilirliğe de fayda sağlar.

3. **Genel temel test hususlarını içeren bir test metodolojisinin oluşturulması:**
   IoT cihaz modeline dayalı olarak, genel temel test hususlarını içeren bir test metodolojisi geliştirilecektir. Bu genel temel hususlar, cihaz bileşenleri için geçerli olan güvenlik sorunlarını temsil eder ve belirli bir bileşenin veya teknolojinin somut örneklerine yönelik daha ayrıntılı test senaryolarından türetilecektir. Bu türetme, metodolojinin mümkün olduğunca çok sayıda farklı IoT cihazı uygulamasında kullanılmasına olanak sağlamak amacıyla temel hususları ilgili örneğin ayrıntılarından ayırmalıdır (*karşılaştırılabilirlik*). Bununla birlikte, metodolojinin yapısı ilerleyen zamanlarda bir cihaz bileşeninin belirli örnekleri için daha ayrıntılı temel test hususlarının eklenmesine izin vererek genişletilebilirlik sağlayacaktır.
