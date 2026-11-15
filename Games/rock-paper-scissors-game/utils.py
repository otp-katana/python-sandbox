def GirişArayüzü ():
    print(r"""
╔══════════════════════════════════════════════════════════════════════════╗
║                                                                          ║
║                                                                          ║
║                                                                          ║
║   ████████╗ █████╗ ███████╗     ██╗  ██╗██████╗ ██████╗  ██╗████████╗    ║
║   ╚══██╔══╝██╔══██╗██╔════╝     ██║ ██╔╝██╔══██╗██╔════╝ ██║╚══██╔══╝    ║                           
║      ██║   ███████║███████╗     █████═╝ ███████║██║  ███╗██║   ██║       ║
║      ██║   ██╔══██║╚════██║     ██╔═██╗ ██╔══██║██║   ██║██║   ██║       ║
║      ██║   ██║  ██║███████║     ██║  ██╗██║  ██║╚██████╔╝██║   ██║       ║                   
║      ╚═╝   ╚═╝  ╚═╝╚══════╝     ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝ ╚═╝   ╚═╝       ║
║                                                                          ║
║                ███╗   ███╗ █████╗ ██╗  ██╗ █████╗ ███████╗               ║
║                ████╗ ████║██╔══██╗██║ ██╔╝██╔══██╗██╔════╝               ║
║                ██╔████╔██║███████║█████═╝ ███████║███████╗               ║
║                ██║╚██╔╝██║██╔══██║██╔═██╗ ██╔══██║╚════██║               ║
║                ██║ ╚═╝ ██║██║  ██║██║  ██╗██║  ██║███████║               ║ 
║                                                                          ║
║        ┌────────────────────────────────────────────────────────┐        ║
║        │               ✦ OYUNUNA HOŞ GELDİNİZ! ✦                │        ║
║        └────────────────────────────────────────────────────────┘        ║
║                                                                          ║
╚══════════════════════════════════════════════════════════════════════════╝
        """)
    
def Kurallar ():
    print(r"""
/=================================================================\
|                      NASIL OYNANIR? / HELP                      |
|=================================================================|
|  KONTROLLER : [1] Taş  |  [2] Kağıt  |  [3] Makas  |  [0] Çıkış  |
|-----------------------------------------------------------------|
|  KURALLAR   :                                                   |
|   • Taş, Makası yener.                                          |
|   • Makas, Kağıdı yener.                                        |
|   • Kağıt, Taşı yener.                                          |
|   • Aynı seçimler beraberlik [0-0] getirir.                     |
|-----------------------------------------------------------------|
|  HEDEF     : 3 tura ulaşan ilk oyuncu oyunu kazanır!             |
\=================================================================/
    """)

def AnaMenü ():
    import time
    time.sleep(0.5)
    print(r"""
=========================================
  TAŞ - KAĞIT - MAKAS, BİR HAMLE SEÇ...
=========================================
[1] 🪨 TAŞ
[2] 📄 KAĞIT
[3] ✂️ MAKAS
[0] ❌ ÇIKIŞ
=========================================
    """)
    time.sleep(0.5)

def taş ():
    print(r"""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
    """)

def kağıt ():
    print(r"""
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
    """)

def makas ():
    print(r"""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
    """)

def YüklemeAnimasyonu ():
    import time
    time.sleep(0.2)
    print("━")
    time.sleep(0.2)
    print("━")
    time.sleep(0.1)
    print("━")
    time.sleep(0.1)
    print("━")
    time.sleep(0.5)

def OyunuKazanma ():
    print(r"""
 ╭─────────╮
╭│🏆 ✨ 🏆│╮
│╰─────────╯│   
│  OYUNU    │    (✿◠‿◠)  EFSANESİN!
│ KAZANDIN! │    Tüm turları darmadağın ettin!
╰───────────╯
    """)

def OyunuKaybetme ():
    print(r"""
 ╭─────────╮
╭│🌧️ 👾 🌧️│╮
│╰─────────╯│   
│   OYUN    │    (｡•́︿•̀｡)  SAĞLIK OLSUN!
│   BİTTİ!  │    Şans bilgisayardan yanaydı...
╰───────────╯
    """)

def Kazanma ():
    print(r"""
    /\\
<--/  \\-->    ( ★ )  BU TURU KAZANDIN!
   \\  /
    \\/
    """)

def Kaybetme ():
    print(r"""
 /\\  /\\
/  \\/  \\    ( 💔 )  BU TURU KAYBETTİN!
\\      /
 \\    /
  \\  /
   \\/
    """)

def Berabere ():
    print(r"""
┌──────┐
│  ==  │    ( 🤝 )  BU TUR BERABERE!
└──────┘
    """)

def ÇıkışAnimasyonu ():
    import time
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
    print("İYİ GÜNLER...")

def HatalıGiriş ():
    print(r"""
     /\_/\
    ( o.o )  <-- "Yanlış tuşa bastın dostum!"
     > ^ <
=====================================================
             [...] Girdi Kabul Edilmedi!
       Seçiminiz sistem tarafından tanınamadı.
=====================================================
    """)

def GirişYüklenmeAnimasyonu ():
    import time
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