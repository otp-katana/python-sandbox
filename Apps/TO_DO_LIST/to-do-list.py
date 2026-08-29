"""
========================================
  GÖREV LİSTESİ (TO-DO LIST) UYGULAMASI
========================================

Bu program; görev ekleme, silme, tamamlama ve listeleme
işlemlerini gerçekleştiren basit bir komut satırı uygulamasıdır.

Kullanılan temel Python kavramları:
  - Listeler (list) ve sözlükler (dict)
  - Fonksiyonlar (def)
  - Döngüler (for, while)
  - Koşullu ifadeler (if / elif / else)
  - Dosya okuma/yazma (open, json)
  - f-string ile metin biçimlendirme
  - enumerate() ile indeks takibi
"""

import json  # Görevleri dosyaya kaydetmek ve okumak için kullanılır
import os    # Dosyanın var olup olmadığını kontrol etmek için kullanılır

# Görevlerin kaydedileceği dosyanın adı
DOSYA_ADI = "gorevler.json"


# ──────────────────────────────────────────────────────────────
# YARDIMCI FONKSİYONLAR (Dosya okuma/yazma)
# ──────────────────────────────────────────────────────────────

def gorevleri_yukle():
    """
    Kaydedilmiş görevleri JSON dosyasından okur ve bir liste olarak döndürür.
    Dosya yoksa boş bir liste döndürür.

    Döndürülen liste şu yapıda sözlükler içerir:
        {"id": 1, "baslik": "Görev adı", "tamamlandi": False}
    """
    if os.path.exists(DOSYA_ADI):          # Dosya daha önce oluşturulduysa
        with open(DOSYA_ADI, "r", encoding="utf-8") as dosya:
            return json.load(dosya)        # JSON içeriğini Python listesine çevir
    return []                              # Dosya yoksa boş liste döndür


def gorevleri_kaydet(gorevler):
    """
    Görev listesini JSON formatında dosyaya yazar.
    'indent=2' parametresi dosyayı okunabilir hale getirir.
    """
    with open(DOSYA_ADI, "w", encoding="utf-8") as dosya:
        json.dump(gorevler, dosya, ensure_ascii=False, indent=2)
        # ensure_ascii=False → Türkçe karakterlerin bozulmamasını sağlar


# ──────────────────────────────────────────────────────────────
# ANA İŞLEM FONKSİYONLARI
# ──────────────────────────────────────────────────────────────

def gorev_ekle(gorevler, baslik):
    """
    Listeye yeni bir görev ekler.

    Her görev bir sözlük (dict) olarak tutulur:
      - id        : Göreve atanan benzersiz numara
      - baslik    : Görevin açıklaması
      - tamamlandi: Görevin bitip bitmediğini gösteren True/False değeri
    """
    # Mevcut en yüksek id'yi bularak yeni görevin id'sini belirle
    # Liste boşsa id'yi 1'den başlat
    yeni_id = max((g["id"] for g in gorevler), default=0) + 1

    yeni_gorev = {
        "id": yeni_id,
        "baslik": baslik.strip(),   # Kullanıcının girdiği baştaki/sondaki boşlukları temizle
        "tamamlandi": False          # Yeni görev varsayılan olarak tamamlanmamış
    }

    gorevler.append(yeni_gorev)     # Görevi listeye ekle
    gorevleri_kaydet(gorevler)      # Güncellenen listeyi dosyaya yaz
    print(f"\n✅ '{baslik}' görevi eklendi. (ID: {yeni_id})")


def gorev_sil(gorevler, gorev_id):
    """
    Belirtilen ID'ye sahip görevi listeden kaldırır.
    ID bulunamazsa kullanıcıya bilgi verir.
    """
    # List comprehension ile eşleşen görevi hariç tut (filtreleme yöntemi)
    yeni_liste = [g for g in gorevler if g["id"] != gorev_id]

    if len(yeni_liste) == len(gorevler):
        # Uzunluk değişmediyse silinecek görev bulunamadı demektir
        print(f"\n⚠️  ID {gorev_id} numaralı görev bulunamadı.")
    else:
        gorevler.clear()            # Orijinal listeyi temizle
        gorevler.extend(yeni_liste) # Filtrelenmiş listeyi geri yükle
        gorevleri_kaydet(gorevler)
        print(f"\n🗑️  ID {gorev_id} numaralı görev silindi.")


def gorev_tamamla(gorevler, gorev_id):
    """
    Belirtilen ID'ye sahip görevi tamamlandı olarak işaretler.
    Zaten tamamlandıysa kullanıcıyı bilgilendirir.
    """
    for gorev in gorevler:                    # Tüm görevleri teker teker gez
        if gorev["id"] == gorev_id:           # Eşleşen ID'yi bul
            if gorev["tamamlandi"]:
                print(f"\nℹ️  Bu görev zaten tamamlanmış.")
            else:
                gorev["tamamlandi"] = True    # Durumu güncelle
                gorevleri_kaydet(gorevler)
                print(f"\n🎉 '{gorev['baslik']}' görevi tamamlandı olarak işaretlendi.")
            return                            # Görev bulundu, döngüyü bitir

    print(f"\n⚠️  ID {gorev_id} numaralı görev bulunamadı.")


def gorevleri_listele(gorevler):
    """
    Tüm görevleri ekrana düzenli biçimde yazdırır.
    Tamamlanan görevler [✓], tamamlanmayanlar [ ] ile gösterilir.
    """
    print("\n" + "=" * 40)
    print("        GÖREV LİSTESİ")
    print("=" * 40)

    if not gorevler:                          # Liste tamamen boşsa
        print("  Henüz hiç görev eklenmedi.")
        print("=" * 40)
        return

    # enumerate() → hem indeks (sıra numarası) hem de öğeye aynı anda erişir
    for i, gorev in enumerate(gorevler, start=1):
        durum = "✓" if gorev["tamamlandi"] else " "   # Tamamlanma durumu simgesi
        print(f"  [{durum}] ID:{gorev['id']:>2}  {gorev['baslik']}")

    # Özet bilgi
    toplam      = len(gorevler)
    tamamlanan  = sum(1 for g in gorevler if g["tamamlandi"])
    bekleyen    = toplam - tamamlanan

    print("=" * 40)
    print(f"  Toplam: {toplam}  |  Tamamlanan: {tamamlanan}  |  Bekleyen: {bekleyen}")
    print("=" * 40)


# ──────────────────────────────────────────────────────────────
# MENÜ VE ANA DÖNGÜ
# ──────────────────────────────────────────────────────────────

def menuyu_goster():
    """Kullanıcıya seçenekleri gösterir."""
    print("\n┌─────────────────────────┐")
    print("│        ANA MENÜ         │")
    print("├─────────────────────────┤")
    print("│  1. Görevleri listele   │")
    print("│  2. Görev ekle          │")
    print("│  3. Görev tamamla       │")
    print("│  4. Görev sil           │")
    print("│  5. Çıkış               │")
    print("└─────────────────────────┘")


def tam_sayi_al(mesaj):
    """
    Kullanıcıdan tam sayı alır; geçersiz giriş yapılırsa tekrar sorar.
    Bu yaklaşım 'girdi doğrulama' (input validation) örneğidir.
    """
    while True:                               # Geçerli giriş alana kadar tekrarla
        try:
            return int(input(mesaj))          # Girdiyi tam sayıya çevirmeye çalış
        except ValueError:
            # int() dönüşümü başarısız olursa bu blok çalışır
            print("⚠️  Lütfen geçerli bir sayı girin.")


def main():
    """
    Programın ana fonksiyonu.
    Uygulama bu fonksiyondan başlar ve burada döngü kurulur.
    """
    print("\n🗒️  Görev Listesi Uygulamasına Hoş Geldiniz!")
    gorevler = gorevleri_yukle()              # Kayıtlı görevleri dosyadan yükle

    while True:                               # Kullanıcı çıkış seçene kadar döngü devam eder
        menuyu_goster()
        secim = input("\nSeçiminizi yapın (1-5): ").strip()

        if secim == "1":
            gorevleri_listele(gorevler)

        elif secim == "2":
            baslik = input("Yeni görevin adı: ").strip()
            if baslik:                        # Boş giriş kontrolü
                gorev_ekle(gorevler, baslik)
            else:
                print("⚠️  Görev adı boş olamaz.")

        elif secim == "3":
            gorevleri_listele(gorevler)
            gorev_id = tam_sayi_al("Tamamlanacak görevin ID numarası: ")
            gorev_tamamla(gorevler, gorev_id)

        elif secim == "4":
            gorevleri_listele(gorevler)
            gorev_id = tam_sayi_al("Silinecek görevin ID numarası: ")
            gorev_sil(gorevler, gorev_id)

        elif secim == "5":
            print("\n👋 Görüşmek üzere!\n")
            break                             # Döngüyü kır ve programı bitir

        else:
            print("⚠️  Geçersiz seçim. Lütfen 1 ile 5 arasında bir değer girin.")


# ──────────────────────────────────────────────────────────────
# PROGRAMIN BAŞLANGIÇ NOKTASI
# ──────────────────────────────────────────────────────────────

# Bu blok yalnızca dosya doğrudan çalıştırıldığında tetiklenir.
# Başka bir .py dosyasına import edilirse çalışmaz — bu standart bir Python alışkanlığıdır.
if __name__ == "__main__":
    main()