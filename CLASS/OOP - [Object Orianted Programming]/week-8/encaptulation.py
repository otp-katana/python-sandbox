"""
Kapsülleme yöntemi (encapculation)
"""

class Karakter:
    def __init__(self, isim, can, seviye = 1):
        self.isim = isim
        self._can = can
        self.__seviye = seviye

    def can_eksilt (self, miktar):
        if self._can < 0:
            self._can = 0

        self._can -= miktar

karakter1 = Karakter("Ali", 100)



#Korumalı değişken (önerilmez). Sınıf dışından erişme uyarısı verir.
print(karakter1.isim)
print(karakter1._can)

karakter1.can_eksilt(30)
print(karakter1._can)

print(karakter1._Karakter__seviye)
#print(karakter1.__seviye) #-> Doğrudan erişimi engeller.
