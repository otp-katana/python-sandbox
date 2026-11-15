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

#!düzenlenecek...   
    def bilgileri_goster(self):
        print("-" * 80)
        print(f"Öğrencinin Adı: {self.ad}")
        print(f"Öğrencinin Soyadı: {self.soyad}")
        print("-" * 80)
        print(f"Öğrencinin TC Kimlik Numarası: {self.kimlik_no}")
        print(f"Öğrencinin Doğum Tarihi: {self.dogum_tarihi}")
        print(f"Öğrencinin Bölümü: {self.bolum}")
        print(f"Öğrencinin Okulu: {self.fakulte}")
        print(f"Öğrencinin Öğrenci Numarası: {self.ogrenci_no}")
        print("-" * 80)

    # Yeni ders ve not eklemek için metot
    def not_ekle(self, ders_adi, dersin_notu):
        self.__dersler_ve_notlar[ders_adi] = dersin_notu
        print(f"{ders_adi} dersi notu ({dersin_notu}) başarıyla eklendi.")

    # Eklenen notları görüntülemek için düzeltilen metot
    def not_goruntule(self, ders_adi):
        if ders_adi in self.__dersler_ve_notlar:
            print(f"Öğrenci {self.ad}'nin {ders_adi} dersi notu: {self.__dersler_ve_notlar[ders_adi]}")
        else:
            print(f"Öğrenci {self.ad}, {ders_adi} dersini henüz almamış.")
#!düzenlenecek...


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


    #!düzenlenecek...
    ogrenci_1.bilgileri_goster()

    # Önce nota ekleme yapıyoruz
    ogrenci_1.not_ekle("Matematik", 85)
    ogrenci_1.not_ekle("Programlama", 95)

    print("-" * 80)

    # Sonra eklenen notu sorguluyoruz
    ogrenci_1.not_goruntule("Matematik")
    ogrenci_1.not_goruntule("Fizik")  # Eklenmeyen ders kontrolü
    #!düzenlenecek...


except (TypeError, ValueError) as hata:
    print(f"Başarısız kayıt işlemi!\nSebep: {hata}")