#──────────────────────────────────────────────────────────────────────────────────────────────────────────
#➥ TEMEL KURALLAR VE ALGORİTMA MANTIĞI
#──────────────────────────────────────────────────────────────────────────────────────────────────────────
#────────────────────────────────────────────────────────────────────────────────────────────────────────── 
#⤷ Uzunluk ve İlk Hane: Toplam 11 hanelidir. İlk hane kesinlikle 0 olamaz.
#⤷ 10. Hane Hesabı:
#	> 1, 3, 5, 7 ve 9. sıradaki rakamların toplamı 7 ile çarpılır.
#	> Bu sonuçtan, 2, 4, 6 ve 8. sıradaki rakamların toplamı çıkarılır.
#	> Çıkan sonucun 10'a bölümünden kalan (yani ... mod 10), 10. haneyi verir.
#	> Formül: [ (1 + 3 + 5 + 7 + 9. basamaklar toplamı) × 7 - (2 + 4 + 6 + 8. basamaklar toplamı) ] mod 10
#⤷ 11. Hane Hesabı:
#	> İlk 10 hanenin tamamının rakamları toplanır.
#	> Bu toplamın 10'a bölümünden kalan (yani ... mod 10), 11. haneyi verir.
#	> Formül: (1'den 10'a kadar olan basamakların toplamı) mod 10
#──────────────────────────────────────────────────────────────────────────────────────────────────────────
import arayuz

def kimlik_no_hesaplama(kimlik_no):
    str_kimlik_no = str(kimlik_no).strip()

    rakamlar = [int(hane) for hane in str_kimlik_no]

    tek_haneler_toplam = sum(rakamlar[0:9:2])
    cift_haneler_toplam = sum(rakamlar[1:8:2])

    hane_10 = ((tek_haneler_toplam * 7) - cift_haneler_toplam) % 10
    hane_11 = sum(rakamlar[:10]) % 10

    gecerli_mi = (hane_10 == rakamlar[9] and hane_11 == rakamlar[10])

    # ASCII doğrulama raporunu ekrana basar
    arayuz.kimlik_dogrulama_raporu_ciz(
        str_kimlik_no, 
        tek_haneler_toplam, 
        cift_haneler_toplam, 
        hane_10, 
        hane_11, 
        gecerli_mi
    )

    return gecerli_mi
