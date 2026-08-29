import random
from utils import *

kelime_havuzu = ["çilek", "çiçek", "mantal", "ız"]

kelime = random.choice(kelime_havuzu).replace("i", "İ").replace("ı", "I").upper()

gizli_kelime = ["_" for _ in kelime]

tahmin_edilenler = set()

arayüz_liste = [step_1(), step_2(), step_3(), step_4(), step_5(), step_6()]

step_0()
can = 6
while can > 0 and "_" in gizli_kelime:

    tahmin = input("> ").replace("i", "İ").replace("ı", "I").upper()
    tahmin_edilenler.add(tahmin)



    if tahmin in kelime:
        for indeks, harf in enumerate(kelime):
            if harf == tahmin:
                gizli_kelime[indeks] = tahmin
    else:
        can -= 1
 


    print(" ".join(gizli_kelime))

