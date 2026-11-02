class Kitap:
    def __init__(self, ad, sayfa):
        self.ad = ad
        self.sayfa = sayfa

    def __str__(self):
        # __str__ özel bir metottur ve nesnenin string temsilini döndürmek için kullanılır.
        # Bu sayede print() fonksiyonu kullanıldığında nesne hakkında anlamlı bir bilgi verir.
        return f"{self.ad} ({self.sayfa} sayfa)"

    def yazdir(self):
        # aşağıda __str__ kullanılmadan, bir nesnenin metodunu çağırarak nesne hakkında
        # bilgi vermek için yazdırma işlemi yapılır.
        print(f"{self.ad} kitabı {self.sayfa} sayfadan oluşuyor.")



k = Kitap("Python Temelleri", 250)
print(k)  # __str__ sayesinde: Python Temelleri (250 sayfa)
k.yazdir()  # yazdir metodu sayesinde: Python Temelleri kitabı 250 sayfadan oluşuyor.
