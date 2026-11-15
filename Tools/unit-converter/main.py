from UI import *


programı_sonlandır = True
while programı_sonlandır:
    ana_menü()

    while True:
        try:
            kullanıcı_girişi = int(input("> "))

            if kullanıcı_girişi == 1:
                uzunluk_dönüştürücü_from()
                giriş_from = int(input("> "))
                if giriş_from == 1:
                    birim_giriş_from = float(input("Birim> "))
                    uzunluk_dönüştürücü_to()
                    giriş_to = int(input("> "))
                    if giriş_to == 2:
                        print(birim_giriş_from / 10)
                    elif giriş_to == 3:
                        print(birim_giriş_from / 1000)
                    elif giriş_to == 4:
                        print(birim_giriş_from / 1000000)
                    elif giriş_to == 5:
                        print(birim_giriş_from / 25.4)
                    elif giriş_to == 6:
                        print(birim_giriş_from / 304.8)
                    elif giriş_to == 7:
                        print(birim_giriş_from / 914.4)
                    elif giriş_to == 8:
                        print(birim_giriş_from / 0.0254)

                elif giriş_from == 2:
                    birim_giriş_from = float(input("Birim> "))
                    uzunluk_dönüştürücü_to()
                    giriş_to = int(input("> "))
                    if giriş_to == 1:
                        print(birim_giriş_from * 10)
                    elif giriş_to == 3:
                        print(birim_giriş_from / 1000)
                    elif giriş_to == 4:
                        print(birim_giriş_from / 1000000)
                    elif giriş_to == 5:
                        print(birim_giriş_from / 25.4)
                    elif giriş_to == 6:
                        print(birim_giriş_from / 304.8)
                    elif giriş_to == 7:
                        print(birim_giriş_from / 914.4)
                    elif giriş_to == 8:
                        print(birim_giriş_from / 0.0254)                    







        
