class OyunKarakteri:
    def __init__(self, isim, can = 100, max_can = 200, boy = 2.00):
        self.isim = isim
        self.can = can
        self.max_can = max_can
        self.boy = boy
        self.hayatta_mi = True
        self.hasar_gucu = 15


    def can_dusur (self, miktar):
        if not self.hayatta_mi:
            print(f"{self.isim} zaten öldü daha fazla hasar alamaz!")
            return

        self.can -= miktar
        print(f"{self.isim} {miktar} hasar aldı! Kalan Can: {self.can}")

        if self.can <= 0:
            self.can = 0
            self.hayatta_mi = False
        print(f"{self.isim} öldü... OYUN BİTTİ.")

    def can_yukselt (self, miktar):
        if not self.hayatta_mi:
            print(f"{self.isim} öldüğü için canı yükseltilemez!")
            return
        
        self.can += miktar
        print(f"{self.isim} {miktar} can yeniledi! Güncel Can: {self.can}")

        if self.can > self.max_can:
            self.can = self.max_can

    def ekrana_durum_yazdir (self):
        if self.hayatta_mi == True:
            self.hayatta_mi = "Evet"
        else:
            self.hayatta_mi = "Hayır"
        print(f"İsim: {self.isim} | Can: {self.can} | Max. can: {self.max_can} | Boy: {self.boy} | Hayatta mı: {self.hayatta_mi} | Hasar: {self.hasar_gucu} |")

    def saldir (self, dusman):
        self.can -= self.hasar_gucu
        self.dusman = dusman


#?Karakterimizi oluşturuyoruz (İsim: Savaşçı, Boy: 1.85)
kahraman = OyunKarakteri(isim="Savaşçı", boy=1.85)
print(f"Karakter Oluşturuldu: {kahraman.isim} | Can: {kahraman.can} | Boy: {kahraman.boy}m\n")

#?Karakter bir tuzağa basıyor ve hasar alıyor
print("Kahraman zindanda yürürken bir ok tuzağına yakalandı!")
kahraman.can_dusur(30)
print("-" * 40)

#?Kahraman bir sağlık iksiri buluyor ve içiyor
print("Kahraman yerde kırmızı bir iksir buldu ve içti!")
kahraman.can_yukselt(15)
print("-" * 40)

#?Kahraman büyük bir canavarla (Boss) karşılaşıyor ve ölümcül darbe alıyor
print("DEV EJDERHA BELİRDİ! Alev püskürtüyor!")
kahraman.can_dusur(90)
print("-" * 40)

#?Ölmüş karaktere tekrar iksir vermeyi deniyoruz
print("Çantadaki son iksiri kullanmaya çalışıyorsun...")
kahraman.can_yukselt(20)

kahraman.ekrana_durum_yazdir()