class Karakter:
    def __init__(self, isim, yas, can):
        self.isim = isim
        self._can = can
        self.yas = yas

    #getter method
    def goster_can (self):
        if self._can == 0:
            self._can = 0

        return self._can

    #setter method
    def ayarla_can (self, yeni_can):
        if 0 <= yeni_can <= 100:
            self._can = yeni_can
        else:
            print("Can değeri 0 ile 100 arasında olmalıdır.")

    #getter -> değeri okur
    @property
    def yas (self):
        return self._yas

    #setter -> değere atama yapılırken doğrulama yapar
    @yas.setter
    def yas (self, deger):
        if type(deger) != int:
            raise TypeError("Yaş bir tamsay olmalıdır!")
        elif deger < 0:
            raise ValueError("Yaş negatif olamaz!")

        self._yas = deger



karakter1 = Karakter("Ali", 21, 80)

karakter1.ayarla_can(95)
print(karakter1._can)
karakter1.ayarla_can(185)

#karakter1.yas = -5
#karakter1.yas = "10"
#karakter1.yas = "otuz"
#karakter1.yas = 21.5
karakter1.yas = 23

print(karakter1.yas)
