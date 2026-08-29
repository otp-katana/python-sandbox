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

# --- İÇE AKTARMALAR (IMPORTS) ---
# UI_functions.py içindeki tüm fonksiyonları (anamenü, zafer, yenilgi, vs.)
# doğrudan bu dosyanın isim uzayına (namespace) çekiyoruz.
# "from X import *" kullanmanın amacı: anamenü(), zafer() gibi fonksiyonları
# UI_functions.anamenü() diye değil, doğrudan anamenü() diye çağırabilmek.
# ALTERNATİF YÖNTEM: "import UI_functions as ui" yazıp ui.anamenü() şeklinde
# çağırmak daha "temiz" kabul edilir çünkü hangi fonksiyonun nereden geldiği
# belli olur ve isim çakışması (aynı isimde iki fonksiyon olması) riski azalır.
# Küçük projelerde "import *" pratik olsa da, büyük projelerde kaçınılması
# önerilen bir yöntemdir.
from UI_functions import *

# random modülü: rastgele sayı üretmek için kullanılıyor (bilgisayarın tuttuğu sayı).
import random

# time modülü: ekrana yazdırma işlemleri arasına gecikme (sleep) koyarak
# oyuna "yükleniyor" hissi / dramatik efekt katmak için kullanılıyor.
# Bu sadece görsel bir efekt, oyunun mantığıyla (kazanma/kaybetme) ilgisi yok.
import time

# --- AÇILIŞ EKRANLARI ---
# Bu bölüm sadece estetik: giriş(), başlık(), kurallar() fonksiyonları
# UI_functions.py içinde tanımlı ve print() ile ASCII sanat / metin basıyor.
# Aralara konan time.sleep() çağrıları, çizgilerin ("━") teker teker,
# hızlanan bir ritimle ekrana gelmesini sağlıyor (1 sn, 0.7 sn, 0.4 sn, 0.2 sn).
# ALTERNATİF: Bu tekrar eden "print + sleep" bloğu bir fonksiyona alınabilirdi,
# örneğin: def yükleniyor_efekti(): for s in [1,0.7,0.4,0.2]: time.sleep(s); print("━")
# Böylece kod tekrarı (DRY - Don't Repeat Yourself ilkesi) önlenirdi.
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

# --- ANA OYUN DÖNGÜSÜ (dış while True) ---
# Bu en dıştaki sonsuz döngü, oyuncunun "tekrar oyna" seçeneğini seçtiği
# sürece tüm oyun akışını (menü -> zorluk seçimi -> oynanış -> sonuç) baştan
# başlatır. Döngüden çıkış, en altta "OyunBitti = True" olduğunda
# "break" ile gerçekleşir. Yani bu yapı GÖREV 4'teki "Yeniden Oyna Seçeneği"
# gereksinimini karşılıyor.
while True:

    # Her yeni oyun turunda hakları ve sayacı sıfırlıyoruz.
    # Bu değişkenler döngü içinde tanımlandığı için her turda "temiz" başlar.
    KalanHak = 0        # GÖREV 2: Can/Hak sistemi -> kaç yanlış tahmine izin var
    TahminSayacı = 0     # GÖREV 2: Kaç kez tahmin yapıldığını sayar

    # --- ANA MENÜ SEÇİM DÖNGÜSÜ ---
    # Kullanıcıdan geçerli bir menü seçimi (1 veya 0) gelene kadar bu döngü
    # tekrar tekrar soruyor. Bu, GÖREV 3'teki "girdi kontrolü" mantığının
    # bir parçası: sonsuz döngü + try/except + koşul kontrolü birlikte
    # kullanılarak kullanıcının HER ZAMAN geçerli bir değer girmesi garanti
    # ediliyor (validasyon deseni).
    while True:
        time.sleep(0.5)
        anamenü()   # UI_functions.py'den menüyü ekrana basan fonksiyon
        try:
            # int(input(...)) -> kullanıcının girdiği metni sayıya çevirmeye çalışır.
            # Harf/özel karakter girilirse ValueError fırlatır (GÖREV 3: harf girişini engelle).
            AnaMenüSeçim = int(input("> "))
            if AnaMenüSeçim == 1 or AnaMenüSeçim == 0:
                # Geçerli bir seçim geldiyse iç döngüden çık ve devam et.
                break
            else:
                # Sayı ama menüde olmayan bir değer (örn. 5) girildiyse uyar.
                time.sleep(0.5)
                print("""
=======================================
            [1] YA DA [0]!
 BİR GÖZ DOKTORUNA GÖRÜNSEN İYİ OLUR...
=======================================
                """)
                time.sleep(0.5)
        except ValueError:
            # int() çevrimi başarısız olduysa (örn. "abc" girildiyse) buraya düşer.
            # Program çökmez, sadece kullanıcıyı uyarıp döngü baştan başlar.
            time.sleep(0.5)
            print("""
=======================================
            [1] YA DA [0]!
 BİR GÖZ DOKTORUNA GÖRÜNSEN İYİ OLUR...
=======================================
            """)
            time.sleep(0.5)  

    # Döngüden çıkıldığında AnaMenüSeçim kesinlikle 1 ya da 0'dır.
    if AnaMenüSeçim == 1:
        # Kullanıcı "Yeni Oyun" seçti -> sadece bilgilendirici/dramatik ekranlar basılıyor.
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
        # Kullanıcı "Çıkış" seçti -> veda mesajları basılıp dış döngü "break" ile sonlandırılıyor.
        # Bu, programın tamamen kapanmasını sağlar (sys.exit() kullanmaya gerek yok,
        # çünkü ana döngüden çıkınca zaten script'in sonuna gelinip program bitiyor).
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
        break   # <-- dış (ana oyun) döngüsünü tamamen sonlandırır

    # --- "YENİ OYUN" ONAY DÖNGÜSÜ ---
    # Burada tek seçenek (1) olduğu için aslında bu döngü biraz gereksiz
    # görünebilir (kullanıcı zaten Ana Menü'de 1'i seçti). Muhtemelen ileride
    # buraya ek seçenekler (örn. skor tablosunu görüntüle) eklenmesi
    # planlanmış olabilir. Şu an sadece "1" dışında bir değer girilirse
    # kullanıcıyı uyarıp tekrar soruyor.
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
    
    # --- ZORLUK SEÇİM DÖNGÜSÜ ---
    # Aynı validasyon deseni (sonsuz döngü + try/except + sınır kontrolü) burada
    # da tekrarlanıyor: kullanıcı 1, 2 veya 3 girene kadar döngü devam eder.
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

    # Zorluk seviyesine göre KalanHak (tahmin hakkı) belirleniyor.
    # NOT: Bu üç if/elif bloğu neredeyse birebir aynı (sadece KalanHak
    # değeri farklı). DAHA TEMİZ BİR ALTERNATİF şu şekilde olurdu:
    #
    #   zorluk_haklari = {1: 10, 2: 7, 3: 4}
    #   KalanHak = zorluk_haklari[ZorlukSeçim]
    #   print("ZORLUK SEVİYESİ ONAYLANDI━━") ... (ortak mesajlar tek yerde)
    #
    # Bu şekilde kod tekrarı üçe bölünmek yerine tek bir yerde yönetilirdi
    # (bir mesajı değiştirmek istediğinde 3 yerine 1 yer güncellenirdi).
    if ZorlukSeçim == 1:
        KalanHak = 10   # Kolay -> en çok hak
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
        KalanHak = 7    # Orta
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
        KalanHak = 4    # Zor -> en az hak
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
        # TEORİK OLARAK buraya asla düşülmez, çünkü yukarıdaki döngü zaten
        # ZorlukSeçim'in 1, 2 ya da 3 olduğunu garanti ediyor. Bu "else"
        # bir güvenlik ağı (defensive programming) niteliğinde; kod ileride
        # değiştirilirse hatayı erken yakalamaya yardımcı olur. Ancak burada
        # "break" kullanılması dış döngüyü tamamen sonlandırıp oyunu
        # tamamen kapatır -- muhtemelen istenen davranış bu değildir,
        # normalde "continue" ile ana menüye dönmek daha mantıklı olurdu.
        time.sleep(0.5)
        print("""
=======================================
           [1] - [2] VEYA [3]!
 BİR GÖZ DOKTORUNA GÖRÜNSEN İYİ OLUR...
=======================================
        """)
        time.sleep(0.5)
        break

    # --- GİZLİ SAYININ ÜRETİLMESİ (GÖREV 1: Rastgele Sayı Üret) ---
    # random.randint(0, 100) -> 0 ile 100 arasında (0 ve 100 dahil) rastgele
    # bir tam sayı üretir. Kurallar ekranında "1 ile 100 arasında" dense de
    # kodda 0'dan başlanıyor; küçük bir tutarsızlık, istenirse
    # random.randint(1, 100) yapılabilir.
    BilgisayarınTuttuğuSayı = random.randint(0, 100)
    #print(BilgisayarınTuttuğuSayı)   # <- hile/debug amaçlı; oyunu test ederken açılabilir


    # --- TAHMİN DÖNGÜSÜ (GÖREV 1 + 2 + 3 birleşimi) ---
    # Bu döngü oyunun kalbi: kullanıcı doğru sayıyı bulana ya da hakları
    # bitene kadar sürekli tahmin almaya devam eder.
    while True:
        time.sleep(0.5)
        try:
            KullanıcıTahmini = int(input("> "))

            # GÖREV 3: Sınır kontrolü -> 1-100 aralığı dışında bir sayı
            # (örn. 0, -5, 150) girilirse geçersiz sayılır.
            if 100 >= KullanıcıTahmini > 0:
                TahminSayacı += 1   # Her geçerli tahminde sayaç bir artar
                #print(TahminSayacı)
                if KullanıcıTahmini != BilgisayarınTuttuğuSayı:
                    KalanHak -= 1   # Yanlış tahmin -> bir hak kaybedilir
                    #print(KalanHak)
                    if KalanHak == 0:
                        # GÖREV 2: Kaybetme şartı -> hak kalmadıysa oyun biter.
                        time.sleep(1)
                        print("━")
                        time.sleep(0.7)
                        print("━")
                        time.sleep(0.4)
                        print("━")
                        time.sleep(0.3)
                        print("━")
                        time.sleep(1)
                        yenilgi()   # Kaybetme ekranı (ASCII sanat)
                        break       # Tahmin döngüsünden çık
                    elif KullanıcıTahmini > BilgisayarınTuttuğuSayı:
                        # GÖREV 1: Sıcak-soğuk mantığı -> girilen sayı büyükse
                        # kullanıcıya daha küçük bir sayı denemesi söylenir.
                        aşağı()
                    else:
                        # Girilen sayı küçükse daha büyük bir sayı denemesi söylenir.
                        yukarı()
                else:
                    # Sayı tutturuldu -> kazanma senaryosu.
                    time.sleep(1)
                    print("━")
                    time.sleep(0.7)
                    print("━")
                    time.sleep(0.4)
                    print("━")
                    time.sleep(0.3)
                    print("━")
                    time.sleep(1)
                    zafer()   # Kazanma ekranı (ASCII sanat)
                    break     # Tahmin döngüsünden çık
            else:
                # 1-100 aralığı dışında bir değer girildi -> uyar, hak/sayaç düşürme.
                time.sleep(0.5)
                print("""
=======================================
               BİRİLERİ,
   KURALLARI GÖRMEZDEN GELMİŞ GİBİ...
=======================================
                """)
                time.sleep(0.5)
        except ValueError:
            # GÖREV 3: Harf girişini engelle -> int() çevrimi başarısız olursa
            # (örn. "elli" yazılırsa) program çökmeden kullanıcıyı uyarır.
            time.sleep(0.5)
            print("""
=======================================
  KİM, SAYI TAHMİN OYUNUNDA BAŞKA BİR
           DEĞER GİRER Kİ?...
=======================================
            """)
            time.sleep(0.5)

    # --- TEKRAR OYNA / ÇIKIŞ DÖNGÜSÜ (GÖREV 4) ---
    # Oyun bittikten (kazanma ya da kaybetme) sonra kullanıcıya iki seçenek
    # sunulur: Ana Menüye dön (1) ya da tamamen çık (0).
    # "OyunBitti" adında bir bayrak (flag) değişkeni kullanılıyor; bu değişken
    # sadece "kullanıcı gerçekten çıkmak mı istedi yoksa yeni bir tura mı
    # geçiyor" bilgisini dış döngüye taşımak için var. Python'da iç içe
    # döngülerde "break" sadece bulunduğu döngüyü kırdığı için (dıştaki
    # döngüyü DEĞİL), bu bayrak yöntemi yaygın bir çözümdür.
    # ALTERNATİF: Bir fonksiyon içine alıp "return" ile çıkmak, ya da
    # Python 3.10+ ile "match" / custom exception fırlatmak da kullanılabilirdi,
    # ama bayrak (flag) yöntemi en basit ve en yaygın olanıdır.
    OyunBitti = False
    while True:
        time.sleep(0.5)
        tekrardene()
        try:
            TekrarDeneSeçim = int(input("> "))
            if TekrarDeneSeçim == 1:
                # Ana menüye dön -> iç döngüden çık, dış "while True" başa sarar,
                # KalanHak ve TahminSayacı sıfırlanarak yeni bir tur başlar.
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
                # Tamamen çık -> OyunBitti bayrağını True yapıp hem bu döngüden
                # hem de en dıştaki döngüden çıkılacak.
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

    # Bayrak True ise (kullanıcı gerçekten çıkmak istediyse) en dış döngüyü de
    # burada kırıyoruz -> program tamamen sona eriyor.
    if OyunBitti:
        break