#BASİT HESAP MAKİNESİ PROGRAMI

"""
#BEKLENTİLER:
1-) BASİT BİR KULLANICI ARA YÜZÜ
2-) 4 TEMEL İŞLEMİ GERÇEKLEŞTİRME
3-) HATASIZ ÇALIŞMA
4-) TÜM İŞLEMLERİN KENDİLİĞİNDEN TEKRAR ETMESİ
5-) KONFOR
"""



#ARAYÜZ
""" 
print("┌────────────────────┐")
print("║ 4-) Bölme İşlemi   ║")
print("║                    ║")
print("║ 3-) Çarpma İşlemi  ║")
print("║                    ║")
print("║ 2-) Çıkarma İşlemi ║")
print("║                    ║")
print("║ 1-) Toplama İşlemi ║")
print("└────────────────────┘")
print("┌────────────────────┐")
print("║ 0-) \033[31m\033[4mÇIKIŞ\033[0m          ║")
print("└────────────────────┘")
"""
"""
UNICODE KARAKTERLER VE ANSI ESCAPE KODLARI İLE ARA YÜZ TASARIMI YAPILMIŞTIR. DEĞİŞKENLERİ VE ÇEŞİTLİ İSİMLERİ
TÜRKÇE KARAKTERLER İLE ADLANDIRMAMIN SEBEBİ KENDİ KONFORUM İÇİNDİR. ÖĞRENME VE PRATİK YAPMIYORSANIZ
BU TÜR TERCİHLER YAPMAMANIZ DAHA İYİ OLUR.
BEN EN BAŞTA ARA YÜZÜ TASARLASAM DA SİZ BÖYLE YAPMAK SORUNDA DEĞİLSİNİZ. KEYFİNİZ NASIL İSTERSE ÖYLE TASARLAYABİLİRSİNİZ.
FAKAT BUNU BAŞTAN YAPARSANIZ NEYİ NEREYE KOYACAĞINIZI VEYA NE İÇİN ÇALIŞTIRACAĞINIZI DAHA RAHAT GÖRÜRSÜNÜZ.
SİSTEMİ PARÇALARA AYIRMAK VE GÖREV BELİRLEMEK, ADIM ADIM VE TEMİZ GELİŞTİRMEYİ SAĞLAR. BÖYLECE MANTIK KURUP
PARÇALARI BİRLEŞTİREREK BÜTÜNE GİDEBİLİRSİNİZ.
"""

#ANA SİSTEM BLOĞU

import time

while True:
    print("┌────────────────────┐")
    print("║ 4-) Bölme İşlemi   ║")
    print("║                    ║")
    print("║ 3-) Çarpma İşlemi  ║")
    print("║                    ║")
    print("║ 2-) Çıkarma İşlemi ║")
    print("║                    ║")
    print("║ 1-) Toplama İşlemi ║")
    print("└────────────────────┘")
    print("┌────────────────────┐")
    print("║ 0-) \033[31m\033[4mÇIKIŞ\033[0m          ║")
    print("└────────────────────┘")

    print("┌───────────────────────────────────────────────────┐")
    print("║ Yapmak İstediğiniz İşlem Numarasını Girin. [1, 4] ║")
    print("└───────────────────────────────────────────────────┘")

    İşlem_Seçimi = int(input("> "))
    """
    KULLANICININ İŞLEM SEÇİMİNİ DAHA KONFORLU YAPABİLMESİ İÇİN ANA MENÜ TASARLANDI. İŞLEM SEÇİMİ İÇİN KULLANICIDAN GİRDİ İSTENDİ.
    """
    if İşlem_Seçimi == 1:
        print("┌───────────────────────────┐")
        print("║ TOPLAMA İŞLEMİNİ SEÇTİNİZ ║")
        print("└───────────────────────────┘")

        Sayı_1 = int(input("\n> "))
        Sayı_2 = int(input("> "))
        """
        KULLANICININ İŞLEMİ GERÇEKLEŞTİRMESİ İÇİN BASİT BİR SAYI GİRDİSİ EKLENDİ. FARKLI YÖNTEMLERLE İKİDEN FAZLA
        SAYI GİRDİSİ ALINABİLİR.
        """
        Toplama = (Sayı_1 + Sayı_2)
        """
        İŞLEMİN UYGULANMASI ADIMI. SONUCUN AYRI BİR DEĞİŞKENDE TUTULMASI ÖNEMLİ DEĞİLDİR FAKAT OKUNURLUK İÇİN ÖNEMLİ.
        """
        print(f"\033[4m\nSONUÇ\033[0m> {Toplama}\n")
        time.sleep(1)
        """
        SONUÇ ADIMLARINDAN SONRA BİR DELAY YANİ 'time.sleep()' KOYMANIN AMACI, SONRASINDA ÇIKAN ARAYÜZÜ GECİKTİRMEK
        VE SONUCU DAHA RAHAT GÖREBİLMEK İÇİN. BUNU EKSTRA BİR 'input' İLE ERTELEMEK DE BİR SEÇENEK FAKAT BEN BURADA
        KONTROLÜ KULLANICIDA HİSSETTİRMEK İÇİN EKLEDİM. TERMİNALİ SÜREKLİ AŞAĞI YUKARI KAYDIRMAK BENİM BİLE CANIMI SIKTI.
        BUNU ÇÖZMENİN BİRÇOK YOLU VAR FAKAT BASİT BİR UYGULAMA İÇİN YETERLİ.
        """
        print("┌────────────────────────────────┐")
        print("║ DEVAM ETMEK İÇİN \033[31m'ENTER'\033[0m BASIN ║")
        print("└────────────────────────────────┘")
        input(">")
        """
        KONTROL HİSSİ İÇİN EKLENEN 'input'. ARA YÜZ İLE BİRLİKTE.
        """

    elif İşlem_Seçimi == 2:
        """
        SAYI GİRDİSİ İSTERKEN 'int' KULLANMAMIN SEBEBİ 'IF' BLOĞUNDA EŞİTLENEN SAYININ BİR 'str' KARAKTERE
        ÇEVRİLME ZORUNLULUĞUNU ENGELLEMEKTİ. PYTHON DEFAULT OLARAK 'str' ALGILADIĞI İÇİN KARIŞIKLIĞI ÖNLEMEK İSTEDİM.
        KODA YAPILAN EKLEMELERDE ÇIKABİLECEK HATALARI DA BÖYLECE EN BAŞTAN ENGELLEMİŞ OLDUM.
        """
        print("┌───────────────────────────┐")
        print("║ ÇIKARMA İŞLEMİNİ SEÇTİNİZ ║")
        print("└───────────────────────────┘")

        Sayı_1 = int(input("\n> "))
        Sayı_2 = int(input("> "))

        Çıkarma = (Sayı_1 - Sayı_2)

        print(f"\033[4m\nSONUÇ\033[0m> {Çıkarma}\n")
        time.sleep(1)

        print("┌────────────────────────────────┐")
        print("║ DEVAM ETMEK İÇİN \033[31m'ENTER'\033[0m BASIN ║")
        print("└────────────────────────────────┘")
        input(">")
        

    elif İşlem_Seçimi == 3:
        print("┌──────────────────────────┐")
        print("║ ÇARPMA İŞLEMİNİ SEÇTİNİZ ║")
        print("└──────────────────────────┘")

        Sayı_1 = int(input("\n> "))
        Sayı_2 = int(input("> "))

        Çarpma = (Sayı_1 * Sayı_2)

        print(f"\033[4m\nSONUÇ\033[0m> {Çarpma}\n")
        time.sleep(1)

        print("┌────────────────────────────────┐")
        print("║ DEVAM ETMEK İÇİN \033[31m'ENTER'\033[0m BASIN ║")
        print("└────────────────────────────────┘")
        input(">")


    elif İşlem_Seçimi == 4:
        print("┌─────────────────────────┐")
        print("║ BÖLME İŞLEMİNİ SEÇTİNİZ ║")
        print("└─────────────────────────┘")

        Sayı_1 = int(input("\n> "))
        Sayı_2 = int(input("> "))

        if Sayı_2 == 0:
            print(f"\033[4m\nSONUÇ\033[0m> \033[31mHATA\033[0m\n")

            print("┌──────────────────────────────────────────────┐")
            print("║ HERHANGİ BİR SAYININ BÖLENİ SIFIR (0) OLAMAZ ║")
            print("└──────────────────────────────────────────────┘")
            time.sleep(1)

            print("┌────────────────────────────────┐")
            print("║ DEVAM ETMEK İÇİN \033[31m'ENTER'\033[0m BASIN ║")
            print("└────────────────────────────────┘")
            input("> ")
            """
            BU IF BLOĞUNUN AMACI, BÖLME İŞLEMİNDE HATAYA SEBEP OLAN 'division by zero' YANİ SIFIRA BÖLÜNEMEMEYİ KONTROL ETMEKTİR.
            İKİNCİ SAYI YANİ BÖLENİN SIFIR OLMASI DURUMUNDA SONUCU BİR HATA VEYA TANIMSIZLIK OLARAK GÖSTERİP İŞLEMİ ATLAMAKTIR.
            BİR GİRDİ ALMADAN DA İŞLEMİ ATLAMAK MÜMKÜNDÜR. 'continue' KOMUTU RAHATLIKLA KULLANILABİLİR.
            GİRDİYİ YALNIZCA ARA YÜZ İÇİN KULLANDIM.
            """

        elif Sayı_2 != 0 and (Sayı_1 % Sayı_2) == 0:
            Bölme = int(Sayı_1 / Sayı_2)

            print(f"\033[4m\nSONUÇ\033[0m> {Bölme}\n")
            time.sleep(1)

            print("┌────────────────────────────────┐")
            print("║ DEVAM ETMEK İÇİN \033[31m'ENTER'\033[0m BASIN ║")
            print("└────────────────────────────────┘")
            input(">")
            """
            BU KOD BLOĞUNUN AMACI, BÖLME İŞLEMİNDE PYTHON'IN KENDİLİĞİNDEN 'float' TYPE GÖSTERMESİNİ ENGELLEMEK. TAMAMEN KEYTFİ TERCİHTİR.
            BELİRLENEN SAYILARIN BİRBİRİNE TAM BÖLÜNMESİ MÜMKÜNSE TAM SAYI TİPİNDE YAZILMASINI KONTROL EDER.
            """

        elif Sayı_2 != 0 and (Sayı_1 % Sayı_2) != 0:
            Bölme = float(Sayı_1 / Sayı_2)


            print(f"\033[4m\nSONUÇ\033[0m> {Bölme}\n")
            time.sleep(1)

            print("┌────────────────────────────────┐")
            print("║ DEVAM ETMEK İÇİN \033[31m'ENTER'\033[0m BASIN ║")
            print("└────────────────────────────────┘")
            input("> ")
            """
            BELİRLENEN SAYILARIN BİRBİRİNE TAM BÖLÜNMESİ MÜMKÜN DEĞİLSE ONDALIK SAYI TİPİNDE YAZILMASINI KONTROL EDER.
            BU KEYFİ TERCİHİ YAPACAKSANIZ 'Sayı_2' DEĞİŞKENİN and OPERATÖRÜ İLE SIFIRA EŞİT OLMAMASI DURUMU KULLANILMAK ZORUNDADIR.
            KALAN KONTROLÜ İÇİN KULLANILAN İŞLEMDE 'Sayı_2' SIFIRA EŞİTLENİRSE 'division by zero' HATASI MEYDANA GELİR VE PROGRAM DURUR.
            """

    elif İşlem_Seçimi == 0:
        print("┌────────────────────────┐")
        print("║ \033[31mÇIKIŞ\033[0m YAPMAYI SEÇTİNİZ ║")
        print("└────────────────────────┘")
        time.sleep(1)

        print("┌─────────────────────────────────┐")
        print("║ ÇIKIŞ YAPMAK İÇİN \033[31m'ENTER'\033[0m BASIN ║")
        print("└─────────────────────────────────┘")

        Çıkış = input("> ")

        if Çıkış == "":
            print("┌────────────────────────────────┐")
            print("║ UYGULAMADAN ÇIKIŞ YAPILIYOR... ║")
            print("└────────────────────────────────┘")
            break

        else:
            print("┌───────────────────────────────────────────────────────────┐")
            print("║ \033[31m\033[4mHATALI GİRİŞ YAPTINIZ\033[0m, ANA MENÜYE YÖNLENDİRİLİYORSUNUZ... ║")
            print("└───────────────────────────────────────────────────────────┘")
            time.sleep(2)
            """
            SON ADIM OLARAK ÇIKIŞ İŞLEMİNİN YAPILMASI VE RASTGELE TUŞ BASIMI KONTROLÜ.
            """


    else:
        print("┌───────────────────────────────────────────────────────────┐")
        print("║ \033[31m\033[4mHATALI GİRİŞ YAPTINIZ\033[0m, ANA MENÜYE YÖNLENDİRİLİYORSUNUZ... ║")
        print("└───────────────────────────────────────────────────────────┘")
        time.sleep(2)
        """
        GİRİŞTEKİ VAR OLMAYAN İŞLEM SEÇİMİ KONTROLÜ.
        """
        """
        NOT: SADECE TEMEL BİLGİLERLE GELİŞTİRİLMİŞTİR. 'def' FONKSİYONLARI, ARGÜMANLAR, PARAMETRELER, DICT, LIST GİBİ ÇEŞİTLİ
        METHODLARLA ÇOK DAHA KOMPLEKS VE GELİŞMİŞ BİR YAPIYA EVRİLEBİLİR.
        """
