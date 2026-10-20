class Futbolcu:
    def __init__(self, isim, yas, mevki, guc= 120):
        self.isim = isim
        self.yas = yas
        self.mevki = mevki
        self.guc = guc

    def kos (self):
        print(f"{self.isim} koşuyor.")

    def sut_cek (self, guc):
        print(f"{self.isim} {guc} güçle şut çekti.")

futbolcu1 = Futbolcu(isim= "Ali", yas= 21, mevki= "Santrafor")

print(f"Futbolcu {futbolcu1.isim} {futbolcu1.guc} şiddetinde şut çekti.")