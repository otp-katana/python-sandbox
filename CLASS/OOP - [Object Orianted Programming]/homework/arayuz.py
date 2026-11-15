#─────────────────────────────────────────────────────────────────
#                   ➤ ARAYÜZ MODÜLÜ (ASCII)
#─────────────────────────────────────────────────────────────────

GENISLIK = 72  # Kutu genişliği

def ust_cizgi():
    print("╔" + "═" * (GENISLIK - 2) + "╗")

def orta_cizgi():
    print("╠" + "═" * (GENISLIK - 2) + "╣")

def ince_cizgi():
    print("╟" + "─" * (GENISLIK - 2) + "╢")

def alt_cizgi():
    print("╚" + "═" * (GENISLIK - 2) + "╝")

def baslik_yazdir(baslik):
    ust_cizgi()
    print("║" + baslik.center(GENISLIK - 2) + "║")
    orta_cizgi()

def satir_yazdir(etiket, deger):
    icerik = f"  {etiket:<22}: {deger}"
    print("║" + icerik.ljust(GENISLIK - 2) + "║")

def bilgi_mesaji(ikon, mesaj, renk_kodu=""):
    # opsiyonel renk kodu
    sıfırla = "\033[0m" if renk_kodu else ""
    metin = f"  {ikon} {mesaj}"
    # Görünür karakter uzunluğuna göre boşluk hesaplama
    bosluk = (GENISLIK - 2) - len(metin)
    print(f"║{renk_kodu}{metin}{sıfırla}{' ' * bosluk}║")

def ogrenci_karti_ciz(ogrenci):
    baslik_yazdir("🎓 ÖĞRENCİ BİLGİ KARTI")
    satir_yazdir("Adı Soyadı", f"{ogrenci.ad} {ogrenci.soyad}")
    satir_yazdir("Öğrenci No", ogrenci.ogrenci_no)
    satir_yazdir("T.C. Kimlik No", ogrenci.kimlik_no)
    satir_yazdir("Doğum Tarihi", ogrenci.dogum_tarihi)
    ince_cizgi()
    satir_yazdir("Fakülte / Y.O.", ogrenci.fakulte)
    satir_yazdir("Bölüm", ogrenci.bolum)
    satir_yazdir("Sınıf", f"{ogrenci.sinif}. Sınıf")
    durum = "Aktif Öğrenci ✔" if ogrenci.aktif_mi else "Pasif ✖"
    satir_yazdir("Kayıt Durumu", durum)
    alt_cizgi()

def ders_tablosu_ciz(ogrenci_adi, dersler_sozlugu):
    ust_cizgi()
    baslik = f"📚 {ogrenci_adi.upper()} - DERS VE NOT LİSTESİ"
    print("║" + baslik.center(GENISLIK - 2) + "║")
    orta_cizgi()
    
    # Tablo Sütun Başlıkları
    sutun_baslik = f"  {'DERS ADI':<40} │ {'NOT':^10} │ {'DURUM':^10}"
    print("║" + sutun_baslik.ljust(GENISLIK - 2) + "║")
    ince_cizgi()

    if not dersler_sozlugu:
        bos_mesaj = "Henüz kayıtlı ders bulunmamaktadır."
        print("║" + bos_mesaj.center(GENISLIK - 2) + "║")
    else:
        for ders, notu in dersler_sozlugu.items():
            durum = "GEÇTİ" if notu >= 50 else "KALDI"
            satir = f"  {ders:<40} │ {str(notu):^10} │ {durum:^10}"
            print("║" + satir.ljust(GENISLIK - 2) + "║")
            
    alt_cizgi()



def kimlik_dogrulama_raporu_ciz(kimlik_no, tek_toplam, cift_toplam, hane_10, hane_11, gecerli_mi):
    ust_cizgi()
    baslik = "🔐 T.C. KİMLİK NUMARASI ALGORİTMA DOĞRULAMA"
    print("║" + baslik.center(GENISLIK - 2) + "║")
    orta_cizgi()

    # Kimlik numarasını basamaklarına ayırarak gösterme
    basamaklar_str = " ".join(list(str(kimlik_no)))
    satir_yazdir("Girilen Kimlik No", basamaklar_str)
    ince_cizgi()

    # Hesaplama Detayları
    satir_yazdir("Tek Haneler Toplamı", f"{tek_toplam} (1, 3, 5, 7, 9. haneler)")
    satir_yazdir("Çift Haneler Toplamı", f"{cift_toplam} (2, 4, 6, 8. haneler)")
    ince_cizgi()

    # 10. ve 11. Hane Karşılaştırması
    girilen_10 = str(kimlik_no)[9]
    girilen_11 = str(kimlik_no)[10]
    
    satir_yazdir("10. Hane Kontrolü", f"Hesaplanan: {hane_10}  |  Girilen: {girilen_10}")
    satir_yazdir("11. Hane Kontrolü", f"Hesaplanan: {hane_11}  |  Girilen: {girilen_11}")
    orta_cizgi()

    # Sonuç Mesajı
    if gecerli_mi:
        bilgi_mesaji("✔", "DOĞRULAMA BAŞARILI: Kimlik numarası geçerlidir.", "\033[92m")
    else:
        bilgi_mesaji("✖", "DOĞRULAMA BAŞARISIZ: Kontrol basamakları uyuşmuyor!", "\033[91m")
        
    alt_cizgi()