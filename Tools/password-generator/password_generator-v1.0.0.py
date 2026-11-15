import random
import string
import sys

# Karakter setleri
KUCUK_HARF = string.ascii_lowercase
BUYUK_HARF = string.ascii_uppercase
RAKAM      = string.digits
SEMBOL     = string.punctuation


# ──────────────────────────────────────────────
#  GÜÇ SEVİYESİ SEÇME FONKSİYONU
# ──────────────────────────────────────────────

def guc_seviyesi_sec():
    print("\n Güç Seviyesi Seçin:")
    print("  1 - Zayıf      (küçük harf + rakam)")
    print("  2 - Orta       (büyük/küçük harf + rakam)")
    print("  3 - Güçlü      (büyük/küçük harf + rakam + sembol)")
    print("  4 - Çok Güçlü  (güçlü + maksimum uzunluk önerisi)")

    while True:
        try:
            secim = input("\nSeçiminiz (1-4): ").strip()

            if not secim:
                raise ValueError("Boş giriş yapılamaz.")

            if secim not in ("1", "2", "3", "4"):
                raise ValueError("Sadece 1, 2, 3 veya 4 girebilirsiniz.")

        except ValueError as e:
            print(f"[HATA] {e} Tekrar deneyin.")
            continue   # Hata varsa döngünün başına dön, aşağıdaki return çalışmaz

        return secim   # Geçerli giriş varsa seviyeyi döndür


# ──────────────────────────────────────────────
#  KARAKTER UZUNLUĞU ALMA FONKSİYONU
# ──────────────────────────────────────────────

def uzunluk_al():
    while True:
        try:
            uzunluk = int(input("Şifre uzunluğu (8-20): "))

            if uzunluk < 8 or uzunluk > 20:
                raise ValueError("Uzunluk 8 ile 20 arasında olmalıdır.")

        except ValueError as e:
            print(f"[HATA] {e} Tekrar deneyin.")
            continue

        return uzunluk


# ──────────────────────────────────────────────
#  ŞİFRE ÜRETME FONKSİYONU
#  if/elif ile seviyeye göre karakter seti belirlenir,
#  zorunlu karakterler önce eklenir, geri kalan rastgele doldurulur.
# ──────────────────────────────────────────────

def sifre_uret(uzunluk, seviye):
    zorunlu_karakterler = []   # Her setten en az 1 karakter tutacak liste
    tum_karakterler = ""       # Rastgele doldurmak için birleşik karakter seti

    if seviye == "1":
        tum_karakterler = KUCUK_HARF + RAKAM
        zorunlu_karakterler.append(random.choice(KUCUK_HARF))
        zorunlu_karakterler.append(random.choice(RAKAM))

    elif seviye == "2":
        tum_karakterler = KUCUK_HARF + BUYUK_HARF + RAKAM
        zorunlu_karakterler.append(random.choice(KUCUK_HARF))
        zorunlu_karakterler.append(random.choice(BUYUK_HARF))
        zorunlu_karakterler.append(random.choice(RAKAM))

    elif seviye == "3" or seviye == "4":
        tum_karakterler = KUCUK_HARF + BUYUK_HARF + RAKAM + SEMBOL
        zorunlu_karakterler.append(random.choice(KUCUK_HARF))
        zorunlu_karakterler.append(random.choice(BUYUK_HARF))
        zorunlu_karakterler.append(random.choice(RAKAM))
        zorunlu_karakterler.append(random.choice(SEMBOL))

    # Zorunlu karakterler eklendikten sonra kalan boşluğu rastgele doldur
    kalan = uzunluk - len(zorunlu_karakterler)
    rastgele_karakterler = random.choices(tum_karakterler, k=kalan)

    # İki listeyi birleştir ve sırayı karıştır
    sifre_listesi = zorunlu_karakterler + rastgele_karakterler
    random.shuffle(sifre_listesi)

    # Listeyi tek bir string'e çevir
    sifre = "".join(sifre_listesi)
    return sifre


# ──────────────────────────────────────────────
#  SEVİYE ADINI DÖNDÜREN FONKSİYON
#  Sözlük yerine if/elif ile seviye adı belirlenir.
# ──────────────────────────────────────────────

def seviye_adi(seviye):
    if seviye == "1":
        return "Zayıf"
    elif seviye == "2":
        return "Orta"
    elif seviye == "3":
        return "Güçlü"
    elif seviye == "4":
        return "Çok Güçlü"


# ──────────────────────────────────────────────
#  SONUCU EKRANA YAZDIRMA FONKSİYONU
# ──────────────────────────────────────────────

def sonuc_yazdir(sifre, seviye):
    print("\n-----------------------------")
    print("       ÜRETİLEN ŞİFRE")
    print("-----------------------------")
    print("Güç Seviyesi : " + seviye_adi(seviye))
    print("Uzunluk      : " + str(len(sifre)))
    print("Şifre        : " + sifre)
    print("-----------------------------")


# ──────────────────────────────────────────────
#  ANA PROGRAM
# ──────────────────────────────────────────────

def main():
    print("\n=== ŞİFRE ÜRETİCİ ===")

    while True:
        seviye  = guc_seviyesi_sec()
        uzunluk = uzunluk_al()
        sifre   = sifre_uret(uzunluk, seviye)
        sonuc_yazdir(sifre, seviye)

        cevap = input("\nYeni şifre üretmek ister misiniz? (e/h): ").strip().lower()
        if cevap != "e":
            print("\nGüvenli günler!")
            sys.exit(0)


if __name__ == "__main__":
    main()
