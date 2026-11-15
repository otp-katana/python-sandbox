#GÖREVLER

"""
? 1- TEMEL MEKANİK
    *Rastgele Sayı Üret
    *Kullanıcıdan Girdi Al
    *Sonsuz Döngü Başlat
    *Karşılaştırma Yap (Sıcak-Soğuk mantığı)

? 2- SAYAÇ VE HAK SINIRI
    *Tahmin Sayacı Tut
    *Can/Hak Sistemi Kur
    *Kaybetme Şartı Ekle

? 3- HATA YÖNETİMİ VE GİRDİ KONTROLÜ
    *Harf Girişini Engelle
    *Sınır Kontrolü Yap

? 4- TEKRAR OYNAMA VE SKOR TABLOSU
    *Yeniden Oyna Seçeneği
"""
from UI_functions import *
import random
import time

giriş()
time.sleep(1)
print("━")
time.sleep(0.7)
print("━")
time.sleep(0.4)
print("━")
time.sleep(0.2)
print("━")
time.sleep(1)
başlık()
time.sleep(1)
print("━")
time.sleep(0.7)
print("━")
time.sleep(0.4)
print("━")
time.sleep(0.2)
print("━")
time.sleep(1)
kurallar()
time.sleep(1)
print("━")
time.sleep(0.7)
print("━")
time.sleep(0.4)
print("━")
time.sleep(0.2)
print("━")
time.sleep(1)

while True:
    
    KalanHak = 0
    TahminSayacı = 0

    while True:
        time.sleep(0.5)
        anamenü()
        try:
            AnaMenüSeçim = int(input("> "))
            if AnaMenüSeçim == 1 or AnaMenüSeçim == 0:
                break
            else:
                time.sleep(0.5)
                print("""
=======================================
            [1] YA DA [0]!
 BİR GÖZ DOKTORUNA GÖRÜNSEN İYİ OLUR...
=======================================
                """)
                time.sleep(0.5)
        except ValueError:
            time.sleep(0.5)
            print("""
=======================================
            [1] YA DA [0]!
 BİR GÖZ DOKTORUNA GÖRÜNSEN İYİ OLUR...
=======================================
            """)
            time.sleep(0.5)  
    if AnaMenüSeçim == 1:
        print("🎮 YENİ OYUN ONAYLANDI━━")
        time.sleep(1)
        print("Sistem Bileşenleri Aktif Hale Getiriliyor...")
        time.sleep(1)
        print("━")
        time.sleep(0.6)
        print("━")
        time.sleep(0.3)
        print("━")
        time.sleep(1)
        print("Oyun Ortamı Oluşturuldu!")
        time.sleep(1)
    elif AnaMenüSeçim == 0:
        print("     ❌ SİSTEMDEN ÇIKILIYOR━━")
        time.sleep(1)
        print("Sistem Bileşenleri Parçalanıyor...")
        time.sleep(1)
        print("━")
        time.sleep(0.6)
        print("━")
        time.sleep(0.3)
        print("━")
        time.sleep(1)
        print("Oyun Ortamı Sonlandırıldı!")
        time.sleep(1)
        print("İYİ GÜNLER...")
        break
    
    while True:
        time.sleep(0.5)
        yenioyun()
            
        try:
            YeniOyunSeçim = int(input("> "))
            if YeniOyunSeçim == 1:
                break
            else:
                time.sleep(0.5)
                print("""
=======================================
              CİDDEN Mİ?...
      SADECE TEK SEÇENEĞİN VARDI.
=======================================
                """)
                time.sleep(0.5)
        except ValueError:
            time.sleep(0.5)
            print("""
=======================================
              CİDDEN Mİ?...
      SADECE TEK SEÇENEĞİN VARDI.
=======================================
                        """)
            time.sleep(0.5)
    
    while True:
        time.sleep(0.5)
        zorluk()

        try:
            ZorlukSeçim = int(input("> "))
            if ZorlukSeçim == 1 or ZorlukSeçim == 2 or ZorlukSeçim == 3:
                break
            else:
                time.sleep(0.5)
                print("""
=======================================
     DOSTUM BİR 3 TANE ZORLUK VAR.
=======================================
                """)
                time.sleep(0.5)
        except ValueError:
            time.sleep(0.5)
            print("""
=======================================
              CİDDEN Mİ?...
      SADECE TEK SEÇENEĞİN VARDI.
=======================================
            """)
            time.sleep(0.5)
    if ZorlukSeçim == 1:
        KalanHak = 10
        print("ZORLUK SEVİYESİ ONAYLANDI━━")
        time.sleep(1)
        print("Sistem Bileşenleri Düzenleniyor...")
        time.sleep(1)
        print("━")
        time.sleep(0.6)
        print("━")
        time.sleep(0.3)
        print("━")
        time.sleep(1)
        print(f"Tahmin Hakkınız → {KalanHak} Olarak Ayarlandı...")
        time.sleep(1)
        print("BOL ŞANS...")
    elif ZorlukSeçim == 2:
        KalanHak = 7
        print("ZORLUK SEVİYESİ ONAYLANDI━━")
        time.sleep(1)
        print("Sistem Bileşenleri Düzenleniyor...")
        time.sleep(1)
        print("━")
        time.sleep(0.6)
        print("━")
        time.sleep(0.3)
        print("━")
        time.sleep(1)
        print(f"Tahmin Hakkınız → {KalanHak} Olarak Ayarlandı...")
        time.sleep(1)
        print("BOL ŞANS...")
    elif ZorlukSeçim == 3:
        KalanHak = 4
        print("ZORLUK SEVİYESİ ONAYLANDI━━")
        time.sleep(1)
        print("Sistem Bileşenleri Düzenleniyor...")
        time.sleep(1)
        print("━")
        time.sleep(0.6)
        print("━")
        time.sleep(0.3)
        print("━")
        time.sleep(1)
        print(f"Tahmin Hakkınız → {KalanHak} Olarak Ayarlandı...")
        time.sleep(1)
        print("BOL ŞANS...")
    else:
        time.sleep(0.5)
        print("""
=======================================
           [1] - [2] VEYA [3]!
 BİR GÖZ DOKTORUNA GÖRÜNSEN İYİ OLUR...
=======================================
        """)
        time.sleep(0.5)
        break

    BilgisayarınTuttuğuSayı = random.randint(0, 100)
    #print(BilgisayarınTuttuğuSayı)


    while True:
        time.sleep(0.5)
        try:
            KullanıcıTahmini = int(input("> "))

            if 100 >= KullanıcıTahmini > 0:
                TahminSayacı += 1
                #print(TahminSayacı)
                if KullanıcıTahmini != BilgisayarınTuttuğuSayı:
                    KalanHak -= 1
                    #print(KalanHak)
                    if KalanHak == 0:
                        time.sleep(1)
                        print("━")
                        time.sleep(0.7)
                        print("━")
                        time.sleep(0.4)
                        print("━")
                        time.sleep(0.3)
                        print("━")
                        time.sleep(1)
                        yenilgi()
                        break
                    elif KullanıcıTahmini > BilgisayarınTuttuğuSayı:
                        aşağı()
                    else:
                        yukarı()
                else:
                    time.sleep(1)
                    print("━")
                    time.sleep(0.7)
                    print("━")
                    time.sleep(0.4)
                    print("━")
                    time.sleep(0.3)
                    print("━")
                    time.sleep(1)
                    zafer()
                    break
            else:
                time.sleep(0.5)
                print("""
=======================================
               BİRİLERİ,
   KURALLARI GÖRMEZDEN GELMİŞ GİBİ...
=======================================
                """)
                time.sleep(0.5)
        except ValueError:
            time.sleep(0.5)
            print("""
=======================================
  KİM, SAYI TAHMİN OYUNUNDA BAŞKA BİR
           DEĞER GİRER Kİ?...
=======================================
            """)
            time.sleep(0.5)
    OyunBitti = False
    while True:
        time.sleep(0.5)
        tekrardene()
        try:
            TekrarDeneSeçim = int(input("> "))
            if TekrarDeneSeçim == 1:
                print("Ana Menüye Aktarılıyorsunuz...")
                time.sleep(1)
                print("━")
                time.sleep(0.6)
                print("━")
                time.sleep(0.3)
                print("━")
                time.sleep(1)
                break
            elif TekrarDeneSeçim == 0:
                print("❌ SİSTEMDEN ÇIKILIYOR━━")
                time.sleep(1)
                print("Sistem Bileşenleri Parçalanıyor...")
                time.sleep(1)
                print("━")
                time.sleep(0.6)
                print("━")
                time.sleep(0.3)
                print("━")
                time.sleep(1)
                print("Oyun Ortamı Sonlandırıldı!")
                time.sleep(1)
                çıkış()
                OyunBitti = True
                break
            else:
                time.sleep(0.5)
                print("""
=======================================
            [1] YA DA [0]!
 BİR GÖZ DOKTORUNA GÖRÜNSEN İYİ OLUR...
=======================================
                """)
                time.sleep(0.5)

        except ValueError:
            time.sleep(0.5)
            print("""
=======================================
            [1] YA DA [0]!
 BİR GÖZ DOKTORUNA GÖRÜNSEN İYİ OLUR...
=======================================
                """)
            time.sleep(0.5)
    if OyunBitti:
        break