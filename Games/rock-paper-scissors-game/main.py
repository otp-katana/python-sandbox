
from utils import *
import random
import time

TaşKağıtMakas = ["Taş", "Kağıt", "Makas"]
oyunbitti = True
OyuncuSkorDurumu = 0
BilgisayarSkorDurumu = 0

GirişArayüzü()
GirişYüklenmeAnimasyonu()
Kurallar()
YüklemeAnimasyonu()

while oyunbitti:

    while True:
        BilgisayarınSeçimi = random.choice(TaşKağıtMakas)
        AnaMenü()
        try:
            KullanıcıSeçimi = int(input("> "))
            if 3 >= KullanıcıSeçimi >= 0:
                if KullanıcıSeçimi == 1:
                    print("\nOYUNCU-1'İN HAMLESİ ↴")
                    taş()
                elif KullanıcıSeçimi == 2:
                    print("\nOYUNCU-1'İN HAMLESİ ↴")
                    kağıt()
                else:
                    print("\nOYUNCU-1'İN HAMLESİ ↴")
                    makas()
                if BilgisayarınSeçimi == "Taş":
                    print("\nBİLGİSAYAR'IN HAMLESİ ↴")
                    taş()
                elif BilgisayarınSeçimi == "Kağıt":
                    print("\nBİLGİSAYAR'IN HAMLESİ ↴")
                    kağıt()
                else:
                    print("\nBİLGİSAYAR'IN HAMLESİ ↴")
                    makas()
                break
            else:
                HatalıGiriş()
                YüklemeAnimasyonu()
        except ValueError:
            HatalıGiriş()
            YüklemeAnimasyonu()

    while True:
        if KullanıcıSeçimi != 0:
            if KullanıcıSeçimi == 1 and BilgisayarınSeçimi == "Taş" or\
               KullanıcıSeçimi == 2 and BilgisayarınSeçimi == "Kağıt" or\
               KullanıcıSeçimi == 3 and BilgisayarınSeçimi == "Makas":
                    OyuncuSkorDurumu = OyuncuSkorDurumu
                    BilgisayarSkorDurumu = BilgisayarSkorDurumu
                    YüklemeAnimasyonu()
                    Berabere()
                    YüklemeAnimasyonu()
                    print(f"""
-------------------------------------------------------------------
                        GÜNCEL SKOR [ TUR: 1 ]                     
                        
                          +---------------+                        
                          |    {OyuncuSkorDurumu}  :  {BilgisayarSkorDurumu}    |                        
                          +---------------+                        
                           (SİZ)     (BOT)                           
-------------------------------------------------------------------
    """)
            elif KullanıcıSeçimi == 1 and BilgisayarınSeçimi == "Makas" or\
                 KullanıcıSeçimi == 2 and BilgisayarınSeçimi == "Taş" or\
                 KullanıcıSeçimi == 3 and BilgisayarınSeçimi == "Kağıt":
                    OyuncuSkorDurumu += 1
                    YüklemeAnimasyonu()
                    Kazanma()
                    YüklemeAnimasyonu()
                    print(f"""
-------------------------------------------------------------------
                        GÜNCEL SKOR [ TUR: 1 ]                     
                        
                          +---------------+                        
                          |    {OyuncuSkorDurumu}  :  {BilgisayarSkorDurumu}    |                        
                          +---------------+                        
                           (SİZ)     (BOT)                          
-------------------------------------------------------------------
    """)
            elif KullanıcıSeçimi == 1 and BilgisayarınSeçimi == "Kağıt" or\
                 KullanıcıSeçimi == 2 and BilgisayarınSeçimi == "Makas" or\
                 KullanıcıSeçimi == 3 and BilgisayarınSeçimi == "Taş":
                    BilgisayarSkorDurumu += 1
                    YüklemeAnimasyonu()
                    Kaybetme()
                    YüklemeAnimasyonu()
                    print(f"""
-------------------------------------------------------------------
                        GÜNCEL SKOR [ TUR: 1 ]                     
                        
                          +---------------+                        
                          |    {OyuncuSkorDurumu}  :  {BilgisayarSkorDurumu}    |                        
                          +---------------+                        
                           (SİZ)     (BOT)                                           
-------------------------------------------------------------------
    """)

            if OyuncuSkorDurumu == 3:
                YüklemeAnimasyonu()
                OyunuKazanma()
                YüklemeAnimasyonu()
                oyunbitti = False
            elif BilgisayarSkorDurumu == 3:
                YüklemeAnimasyonu()
                OyunuKaybetme()
                YüklemeAnimasyonu()
                oyunbitti = False

        else:
            YüklemeAnimasyonu()
            ÇıkışAnimasyonu()
            oyunbitti = False
        break
