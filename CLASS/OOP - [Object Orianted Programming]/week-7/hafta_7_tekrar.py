"""
------- Değişkenler -------
adi
soyadi
tc_kimlik
dogum_tarihi
bolum
okul
ogrenci_no
"""

class Ogrenci:
    def __init__(self, adi, soyadi, tc_kimlik, dogum_tarihi, bolum, okul, ogrenci_no):
        self.adi = adi
        self.soyadi = soyadi
        self.tc_kimlik = tc_kimlik
        self.dogum_tarihi = dogum_tarihi
        self.bolum = bolum
        self.okul = okul
        self.ogrenci_no = ogrenci_no
        # Dersleri ve notları key-value (Ders: Not) olarak tutmak için boş bir sözlük
        self.dersler = {} 

    def bilgileri_goster(self):
        print("-" * 80)
        print(f"Öğrencinin Adı: {self.adi}")
        print(f"Öğrencinin Soyadı: {self.soyadi}")
        print("-" * 80)
        print(f"Öğrencinin TC Kimlik Numarası: {self.tc_kimlik}")
        print(f"Öğrencinin Doğum Tarihi: {self.dogum_tarihi}")
        print(f"Öğrencinin Bölümü: {self.bolum}")
        print(f"Öğrencinin Okulu: {self.okul}")
        print(f"Öğrencinin Öğrenci Numarası: {self.ogrenci_no}")
        print("-" * 80)

    # Yeni ders ve not eklemek için metot
    def not_ekle(self, ders_adi, dersin_notu):
        self.dersler[ders_adi] = dersin_notu
        print(f"{ders_adi} dersi notu ({dersin_notu}) başarıyla eklendi.")

    # Eklenen notları görüntülemek için düzeltilen metot
    def not_goruntule(self, ders_adi):
        if ders_adi in self.dersler:
            print(f"Öğrenci {self.adi}'nin {ders_adi} dersi notu: {self.dersler[ders_adi]}")
        else:
            print(f"Öğrenci {self.adi}, {ders_adi} dersini henüz almamış.")


# Öğrenci oluşturulurken sadece kişisel bilgileri verilir
ogrenci1 = Ogrenci("Ahmet", "Yılmaz", "11111111111", "01.01.2000", 
                   "Yönetim Bilişim Sistemleri", 
                   "Uygulamalı Bilimler Yüksekokulu", "251700001")

ogrenci1.bilgileri_goster()

# Önce nota ekleme yapıyoruz
ogrenci1.not_ekle("Matematik", 85)
ogrenci1.not_ekle("Programlama", 95)

print("-" * 80)

# Sonra eklenen notu sorguluyoruz
ogrenci1.not_goruntule("Matematik")
ogrenci1.not_goruntule("Fizik")  # Eklenmeyen ders kontrolü