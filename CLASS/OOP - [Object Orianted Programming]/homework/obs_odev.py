#──────────────────────────────────────────────────────────
#                           ÖDEV ✎
#──────────────────────────────────────────────────────────
#──────────────────────────────────────────────────────────
# [1]⥋ "Getter & Setter"
# metotları, @property dekoratörü kullanılarak
# tc_kimlik numarasını doğrulamalı.
#   ˃ Kimlik numarası 11 haneli olmalı ve rakamlardan
#   oluşmalı.
#   ˃ Kimlik numarasına değer atanırken "try" ve "except"
#   blokları kullanılmalı.
# [2]⥋ "dersler" niteliği 'private' hale getirilmeli.
#──────────────────────────────────────────────────────────



#─────────────────────────────────────────────────────────────────
#                   ➤ ÖĞRENCİ BİLGİ SİSTEMİ
#─────────────────────────────────────────────────────────────────



#──────────────────────────────────────────────────
#                   ➥ IMPORT
#──────────────────────────────────────────────────
#──────────────────────────────────────────────────
#⤷ Modülerliği sağlamak ve kod karmaşasını
# önlemek amacıyla arayüz elemanlarına ait "arayüz"
# modülü import edildi.
#──────────────────────────────────────────────────
import arayuz
import algoritma


class OgrenciBilgiSistemi:
    def __init__(self, ogrenci_no, ad, soyad, dogum_tarihi, fakulte, bolum, sinif, kimlik_no):
        #───────────────────────────────────────────────
        #             ➥ TEMEL ÖZELLİKLER
        #───────────────────────────────────────────────
        #───────────────────────────────────────────────
        #⤷ "Ogrenci" olarak tanımlanan sınıf adı
        # "OgrenciBilgiSistemi" şeklinde değiştirildi ve
        # kurucu metotta tanımlanan birçok değişkenin,
        # adları ile sıraları düzenlendi.
        #───────────────────────────────────────────────
        self.ogrenci_no = ogrenci_no
        self.ad = ad
        self.soyad = soyad
        self.dogum_tarihi = dogum_tarihi
        self.fakulte = fakulte
        self.bolum = bolum
        self.sinif = sinif
        self.kimlik_no = kimlik_no

        #────────────────────────────────────────────────
        #       ➥ DİNAMİK ÖZELLİK/NİTELİK(LER) ✎
        #────────────────────────────────────────────────
        #─────────────────────────────────────────────────
        #⤷ self.dersler = {} adındaki dinamik nitelik
        # dersler_ve_notlar olarak düzenlendi. Ayrıca
        # ödev yönergesinde belirtildiği gibi
        # '__' (2 alt çizgi) ile "Private" hale getirildi.
        #─────────────────────────────────────────────────
        self.__dersler_ve_notlar = {}
        self.devamsizlik = {}
        self.aktif_mi = True


    #───────────────────────────────────────────────
    #  ➥ PROPERTY DEKORATÖRÜ (GETTER & SETTER) ✎
    #───────────────────────────────────────────────
    #───────────────────────────────────────────────
    #⤷ Kimlik numarasını tutan nitelik @property
    # dekoratörü ile private hale getirildi. Yapının
    # okunabilirliğini sağlamak için T.C kimlik
    # numarasını hesaplayan algoritma import edildi.
    #───────────────────────────────────────────────

    #───────────────────────────────────────────────
    # ➥ GETTER (ACCESSOR METHOD/ERİŞİMCİ METOT) ✎
    #───────────────────────────────────────────────
    #───────────────────────────────────────────────
    #⤷ Private olarak saklanan niteliğin sınıf 
    # dışından kontrollü bir şekilde okunmasını sağlar.
    # (Ayrıca @property tanımlanmadan ilgili niteliğe
    # ait .setter dekoratörü oluşturulamaz.)
    #───────────────────────────────────────────────
    @property
    def kimlik_no (self):   # Dekoratör metot adının sınıfa ait niteliğin adı olması zorunludur!
        return self.__kimlik_no     # Gizli niteliğin okunduğu satır.

    #───────────────────────────────────────────────
    #➥ SETTER (MUTATOR METHOD/DEĞİŞTİRİCİ METOT) ✎
    #───────────────────────────────────────────────
    #───────────────────────────────────────────────
    #⤷ Dışarıdan gönderilen yeni değerin doğrulama
    # ve tip kontrollerini yaparak private niteliğe
    # güvenli şekilde atanmasını sağlar.
    #───────────────────────────────────────────────
    @kimlik_no.setter   #* Dekoratör adının @property dekoratörünün adıyla aynı olması zorunludur!
    def kimlik_no (self, kimlik_no):    #* Dekoratör metot adının @property dekoratörünün adıyla aynı olması zorunludur!
        if type(kimlik_no) == int and kimlik_no > 0:
            kimlik_no = str(kimlik_no)
            if len(kimlik_no) == 11 and kimlik_no[0] != "0":
                if algoritma.kimlik_no_hesaplama(kimlik_no):
                    self.__kimlik_no = kimlik_no    #* Kontrollerin yapılıp gizli niteliğe atandığı satır.
                else:
                    raise ValueError("Geçersiz kimlik numarası!")
            else:
                raise ValueError("Geçersiz kimlik numarası!")
        else:
            raise TypeError("Geçersiz kimlik numarası!")
        #───────────────────────────────────────────────────
        #                    ➥ UYARI!
        #───────────────────────────────────────────────────
        #───────────────────────────────────────────────────
        #───────────────────────────────────────────────────
        #⤷ Fonksiyonların adı olan "kimlik_no" ile
        # parametre olarak bulunan ve atanana "kimlik_no"
        # aynı şey değildir.
        # Fonksiyon adlarındaki "kimlik_no" doğrudan sınıfa
        # ait niteliktir fakat parametre olarak tutulansa
        # adı üzerinden yerel bir parametredir. İkisi
        # birbirine karışmaz ve farklı amaca hizmet ederler.
        #───────────────────────────────────────────────────
    

    #───────────────────────────────────────────────
    #   ➥ GÖRÜNTÜLEME VE DERS İŞLEMLERİ (ARAYÜZ) ✎
    #───────────────────────────────────────────────
    #───────────────────────────────────────────────
    #⤷ Öğrenci bilgilerinin ve ders notlarının
    # terminal ekranında okunaklı, düzenli bir ASCII
    # çerçeve içinde sunulması amacıyla standart
    # print() ifadeleri yerine 'arayuz' modülündeki
    # görselleştirme fonksiyonları entegre edildi.
    #───────────────────────────────────────────────
    def bilgileri_goster(self):
        arayuz.ogrenci_karti_ciz(self)

    #───────────────────────────────────────────────
    #⤷ Private olarak tanımlanan '__dersler_ve_notlar'
    # sözlüğüne dışarıdan güvenli şekilde yeni ders
    # ve not eklenmesini sağlar. İşlem sonucunda
    # kullanıcıya renkli ASCII onay kutusu gösterilir.
    #───────────────────────────────────────────────
    def not_ekle(self, ders_adi, ders_notu):
        self.__dersler_ve_notlar[ders_adi] = ders_notu
        arayuz.ust_cizgi()
        arayuz.bilgi_mesaji("✔", f"{ders_adi} dersi notu ({ders_notu}) başarıyla eklendi.", "\033[92m")
        arayuz.alt_cizgi()

    #───────────────────────────────────────────────
    #⤷ Sorgulanan dersin '__dersler_ve_notlar' içinde
    # bulunup bulunmadığını kontrol eder ve sonucu
    # duruma göre (bilgi veya hata rengiyle) ASCII
    # çerçevesi içinde ekrana yansıtır.
    #───────────────────────────────────────────────
    def not_goruntule(self, ders_adi):
        arayuz.ust_cizgi()
        if ders_adi in self.__dersler_ve_notlar:
            not_degeri = self.__dersler_ve_notlar[ders_adi]
            arayuz.bilgi_mesaji("➤", f"{self.ad} adlı öğrencinin {ders_adi} notu: {not_degeri}", "\033[96m")
        else:
            arayuz.bilgi_mesaji("✖", f"{self.ad}, {ders_adi} dersini henüz almamış.", "\033[91m")
        arayuz.alt_cizgi()

    #───────────────────────────────────────────────
    #⤷ Öğrencinin aldığı tüm dersleri, notlarını ve
    # geçme/kalma durumlarını tek bir ASCII tablo
    # altında toplu olarak listeler.
    #───────────────────────────────────────────────
    def tum_notlari_listele(self):
        arayuz.ders_tablosu_ciz(self.ad, self.__dersler_ve_notlar)


#────────────────────────────────────────────────────
#                  ➥ TRY/EXCEPT ✎
#────────────────────────────────────────────────────
#────────────────────────────────────────────────────
#⤷ Kimlik numarası atama işlemi için hata kontrolü
# sağlayan 'try & except' blokları eklendi.
#
#⤷ İsimlendirme standardına uygunluk nedeniyle
# "ogrenci1" nesnesi "ogrenci_1" olarak değiştirildi.
#
#⤷ "ogrenci_1" nesnesine ait diğer bloklar hata
# kodlarının karışması sebebiyle 'try' bloğunun içine
# taşındı.
# Kimlik numarasının geçersiz olduğu bir senaryoda
# ilk olarak 'value' veya 'type' Error verdiğinden
# dolayı nesne hiç oluşturulmayacak ama altındaki
# kodlar çalışmaya devam edecek ve bu da
# "NameError: name 'ogrenci_1' is not defined"
# hatasını almaya sebep olacak.
#────────────────────────────────────────────────────
try:
    ogrenci_1 = OgrenciBilgiSistemi(
        "251700001", "Ahmet", "Yılmaz", "01.01.2000", "Uygulamalı Bilimler Yüksekokulu",
        "Yönetim Bilişim Sistemleri", "1", 12345678912
    )

    #───────────────────────────────────────────────
    #      ➥ NESNE METOTLARI VE ARAYÜZ TESTİ
    #───────────────────────────────────────────────
    #───────────────────────────────────────────────
    #⤷ Kimlik doğrulamasını başarıyla geçen 'ogrenci_1'
    # nesnesine ait temel bilgilerin ASCII kartı
    # formatında ekrana yazdırılması sağlanır.
    #───────────────────────────────────────────────
    ogrenci_1.bilgileri_goster()

    #───────────────────────────────────────────────
    #⤷ Private olarak saklanan '__dersler_ve_notlar'
    # niteliğine metot aracılığıyla yeni ders ve not
    # kayıtları eklenir. Her ekleme işlemi sonunda
    # arayüz modülü üzerinden onay kutusu gösterilir.
    #───────────────────────────────────────────────
    ogrenci_1.not_ekle("Matematik", 85)
    ogrenci_1.not_ekle("Programlama", 95)

    #───────────────────────────────────────────────
    #⤷ Eklenen ve eklenmeyen derslerin sorgulanması
    # ile tüm ders listesinin toplu ASCII tablosu
    # halinde görüntülenmesi test edilir.
    #───────────────────────────────────────────────
    ogrenci_1.not_goruntule("Matematik")
    ogrenci_1.not_goruntule("Fizik")    #* Eklenmeyen ders kontrolü (Hata mesajı kutusu tetiklenir).
    ogrenci_1.tum_notlari_listele()    #* Tüm derslerin ve geçme/kalma durumlarının toplu tablosu.

except (TypeError, ValueError) as hata:
    print(f"Başarısız kayıt işlemi!\nSebep: {hata}")