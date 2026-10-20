#!/usr/bin/env python3
"""
Todo CLI - Komut satırından çalışan basit bir görev yöneticisi.

Bu proje şu "kasları" hedefler:
  1. argparse ile komut satırı arayüzü tasarımı
  2. Dosya I/O (JSON okuma/yazma)
  3. Context manager kullanımı (with ifadesi)
  4. Hata yönetimi (try/except ile öngörülebilir hataları yakalamak)
  5. Fonksiyonel ayrıştırma (her işi tek bir fonksiyona vermek - Single Responsibility)

NEDEN JSON kullanıyoruz?
  Veri mühendisliğinde en sık karşılaşılacak format budur. CSV'den farklı olarak
  iç içe (nested) yapı taşıyabilir ve Python'un dict/list yapılarıyla bire bir
  eşleşir - bu yüzden serileştirme/deserileştirme mantığını öğrenmek için ideal.
"""

import argparse
import json
import sys
from pathlib import Path
from datetime import datetime

# NEDEN Path kullanıyoruz, os.path değil?
# Path nesnesi, dosya yollarını string yerine bir "nesne" gibi ele almamızı
# sağlar. Path("a") / "b" gibi okunaklı birleştirme yapabiliriz ve işletim
# sistemi farkını (Windows'ta \, Linux'ta /) otomatik hallederiz.
# Modern Python'da os.path yerine pathlib tercih edilir.
TASKS_FILE = Path(__file__).parent / "tasks" / "tasks.json"


# ----------------------------------------------------------------------------
# VERİ KATMANI (Data Layer)
# NEDEN bu fonksiyonları ayırdık?
#   "Veriyi okumak/yazmak" ile "iş mantığı" (görev ekleme, tamamlama) birbirinden
#   bağımsız olmalı. Bu ayrım ileride veri kaynağını (JSON -> SQLite -> API)
#   değiştirmek istediğinde sadece bu iki fonksiyonu değiştirmen yeterli olur.
#   Bu prensibin adı: "Separation of Concerns" (İlgi Alanlarının Ayrılması).
# ----------------------------------------------------------------------------

def gorevleri_yukle() -> list[dict]:
    """
    tasks.json dosyasından görev listesini okur.

    NEDEN try/except FileNotFoundError kullanıyoruz?
      Programın ilk çalıştırılışında dosya henüz yoktur. Bu durumu bir "hata"
      olarak değil, "beklenen bir senaryo" olarak ele almalıyız. Bu yüzden
      hatayı yakalayıp boş bir liste döndürüyoruz - programı çökertmiyoruz.

    NEDEN json.JSONDecodeError'ı ayrıca yakalıyoruz?
      Dosya var ama içeriği bozuksa (örneğin elle düzenlerken sözdizimi
      hatası yapıldıysa), bu farklı bir hata sınıfıdır. Kullanıcıya net bir
      mesaj vermek, "sessizce boş liste dönüp veri kaybını gizlemekten"
      çok daha güvenlidir.
    """
    if not TASKS_FILE.exists():
        return []

    try:
        # NEDEN "with" kullanıyoruz?
        # Context manager, dosyayı işimiz bitince otomatik kapatmamızı
        # garanti eder - hata oluşsa bile. Manuel f.close() yazsaydık,
        # exception fırlarsa dosya açık kalabilirdi (resource leak).
        with open(TASKS_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except json.JSONDecodeError:
        print(
            f"HATA: {TASKS_FILE} dosyası bozuk (geçersiz JSON). "
            "Dosyayı manuel kontrol et veya sil.",
            file=sys.stderr,  # NEDEN stderr? Hata mesajları normal çıktıdan
            # (stdout) ayrı bir kanala gitmeli ki, programın çıktısını başka
            # bir yere yönlendirirken (örn. "python todo.py list > liste.txt")
            # hata mesajları o dosyaya karışmasın.
        )
        sys.exit(1)  # NEDEN çıkış kodu 1? Unix konvansiyonu: 0 = başarı,
        # 0 dışı her şey = hata. Script'ler ve CI/CD pipeline'ları bu kodu
        # okuyarak "işlem başarılı mıydı?" kararını verir.


def gorevleri_kaydet(gorevler: list[dict]) -> None:
    """
    Görev listesini tasks.json dosyasına yazar.

    NEDEN parent klasörü kontrol edip oluşturuyoruz?
      İlk çalıştırmada "tasks/" klasörü olmayabilir. mkdir(parents=True,
      exist_ok=True) hem eksik ara klasörleri oluşturur hem de klasör zaten
      varsa hata fırlatmaz (exist_ok=True olmasaydı FileExistsError alırdık).
    """
    TASKS_FILE.parent.mkdir(parents=True, exist_ok=True)

    with open(TASKS_FILE, "w", encoding="utf-8") as f:
        # NEDEN ensure_ascii=False?
        # Varsayılan olarak json.dump Türkçe karakterleri (ğ, ş, ı, ö, ü, ç)
        # \u00e7 gibi unicode escape kodlarına çevirir. ensure_ascii=False
        # ile dosyada okunabilir Türkçe metin görürüz.
        # NEDEN indent=2?
        # JSON dosyasını insan gözüyle okunabilir/diff'lenebilir yapar -
        # git diff'te değişikliği net görebilmek için önemlidir.
        json.dump(gorevler, f, ensure_ascii=False, indent=2)


# ----------------------------------------------------------------------------
# İŞ MANTIĞI KATMANI (Business Logic Layer)
# ----------------------------------------------------------------------------

def gorev_ekle(baslik: str) -> None:
    """Yeni bir görev ekler ve dosyaya kaydeder."""
    gorevler = gorevleri_yukle()

    # NEDEN id'yi "mevcut en büyük id + 1" olarak hesaplıyoruz,
    # len(gorevler) + 1 değil?
    # Bir görevi sildiğimizde id'ler boşluk bırakır (1, 2, 3 sil-2 -> 1, 3).
    # len() kullansaydık yeni eklenen görev eski silinmiş bir id'yle
    # çakışabilirdi (1, 3 varken len=2, +1=3 -> ÇAKIŞMA). Bu, gerçek
    # veritabanlarında "auto-increment" mantığının neden id'yi asla
    # yeniden kullanmadığını anlamak için iyi bir örnektir.
    yeni_id = max((g["id"] for g in gorevler), default=0) + 1

    gorevler.append({
        "id": yeni_id,
        "baslik": baslik,
        "tamamlandi": False,
        # NEDEN ISO 8601 formatı (datetime.now().isoformat())?
        # Bu format hem insan tarafından okunabilir hem de string olarak
        # sıralanabilir (lexicographic sort = kronolojik sort ile aynı
        # sonucu verir) hem de neredeyse tüm dillerde/sistemlerde standarttır.
        "olusturma_tarihi": datetime.now().isoformat(timespec="seconds"),
    })

    gorevleri_kaydet(gorevler)
    print(f"✓ Görev eklendi: [{yeni_id}] {baslik}")


def gorevleri_listele(sadece_bekleyen: bool = False) -> None:
    """Görevleri ekrana yazdırır."""
    gorevler = gorevleri_yukle()

    if sadece_bekleyen:
        # NEDEN list comprehension kullanıyoruz, for döngüsü yerine?
        # Filtreleme işlemi için list comprehension hem daha kısa hem de
        # Python'da "bu işi biliyorum" sinyali veren idiomatic bir yapıdır.
        # Performans olarak da genellikle eşdeğer for döngüsünden hafif
        # daha hızlıdır (CPython'da özel bir bytecode ile optimize edilir).
        gorevler = [g for g in gorevler if not g["tamamlandi"]]

    if not gorevler:
        print("Hiç görev yok." if not sadece_bekleyen else "Bekleyen görev yok. 🎉")
        return

    for g in gorevler:
        durum = "✓" if g["tamamlandi"] else " "
        # NEDEN f-string kullanıyoruz, .format() ya da % yerine?
        # f-string Python 3.6+'da tanıtıldı, okunabilirlik ve performans
        # açısından diğer yöntemlerden üstün - modern Python kod tabanlarının
        # standardı budur.
        print(f"[{durum}] {g['id']:>3} | {g['baslik']}")


def gorev_tamamla(gorev_id: int) -> None:
    """Belirtilen id'ye sahip görevi tamamlandı olarak işaretler."""
    gorevler = gorevleri_yukle()

    # NEDEN next() + generator expression kullanıyoruz, for döngüsü yerine?
    # "Listede belirli bir koşulu sağlayan ilk elemanı bul" işlemi için
    # next(generator, default) idiomu, döngü + break + flag değişkeni
    # yazmaktan çok daha temiz. default=None sayesinde bulunamama durumunu
    # da güvenle ele alırız (IndexError riski yok).
    hedef = next((g for g in gorevler if g["id"] == gorev_id), None)

    if hedef is None:
        # NEDEN burada exception fırlatmak yerine print + return kullandık?
        # Bu bir CLI aracı - kullanıcıya "hata" göstermek istiyoruz ama
        # programın tamamen çökmesini (traceback ile) istemiyoruz. Bu,
        # "kullanıcı hatası" (beklenen, ele alınabilir) ile "programcı hatası"
        # (beklenmeyen, bug) arasındaki farkı ayırt etmenin bir örneğidir.
        print(f"HATA: {gorev_id} numaralı görev bulunamadı.", file=sys.stderr)
        sys.exit(1)

    hedef["tamamlandi"] = True
    gorevleri_kaydet(gorevler)
    print(f"✓ Tamamlandı: [{gorev_id}] {hedef['baslik']}")


def gorev_sil(gorev_id: int) -> None:
    """Belirtilen id'ye sahip görevi listeden kaldırır."""
    gorevler = gorevleri_yukle()
    yeni_liste = [g for g in gorevler if g["id"] != gorev_id]

    # NEDEN uzunlukları karşılaştırıyoruz?
    # Silme işlemi gerçekten gerçekleşti mi kontrol etmenin basit bir yolu.
    # Eğer uzunluk değişmediyse, o id zaten yoktu demektir.
    if len(yeni_liste) == len(gorevler):
        print(f"HATA: {gorev_id} numaralı görev bulunamadı.", file=sys.stderr)
        sys.exit(1)

    gorevleri_kaydet(yeni_liste)
    print(f"🗑 Silindi: [{gorev_id}]")


# ----------------------------------------------------------------------------
# CLI KATMANI (Arayüz Katmanı)
# NEDEN argparse kullanıyoruz, sys.argv'yi manuel parse etmek yerine?
#   argparse otomatik olarak: --help mesajı üretir, tip dönüşümü yapar
#   (int, str vb.), eksik/yanlış argüman durumunda anlamlı hata verir.
#   Bunları elle yazmak hem zaman kaybı hem de hataya açık.
# ----------------------------------------------------------------------------

def parser_olustur() -> argparse.ArgumentParser:
    """Argparse yapılandırmasını ayrı bir fonksiyonda topluyoruz.

    NEDEN ayrı fonksiyon? main() fonksiyonunu şişirmemek ve bu parser'ı
    ileride test etmek istersek (örn. pytest ile) bağımsız çağırabilmek için.
    """
    parser = argparse.ArgumentParser(
        prog="todo",
        description="Basit bir komut satırı görev yöneticisi.",
    )

    # NEDEN subparsers kullanıyoruz?
    # "todo add ...", "todo list", "todo done 3" gibi git/docker tarzı
    # alt-komut yapısı, tek bir komutta onlarca --flag biriktirmekten çok
    # daha okunabilir ve ölçeklenebilir bir CLI tasarımıdır.
    subparsers = parser.add_subparsers(dest="komut", required=True)

    # --- add komutu ---
    add_parser = subparsers.add_parser("add", help="Yeni görev ekle")
    add_parser.add_argument("baslik", type=str, help="Görev başlığı")

    # --- list komutu ---
    list_parser = subparsers.add_parser("list", help="Görevleri listele")
    list_parser.add_argument(
        "--bekleyen",
        action="store_true",  # NEDEN store_true? Bu bir "flag" - değer
        # almaz, sadece var/yok bilgisini taşır (--bekleyen yazılırsa True).
        help="Sadece tamamlanmamış görevleri göster",
    )

    # --- done komutu ---
    done_parser = subparsers.add_parser("done", help="Görevi tamamlandı işaretle")
    done_parser.add_argument("id", type=int, help="Görev ID'si")

    # --- delete komutu ---
    delete_parser = subparsers.add_parser("delete", help="Görevi sil")
    delete_parser.add_argument("id", type=int, help="Görev ID'si")

    return parser


def main() -> None:
    parser = parser_olustur()
    args = parser.parse_args()

    # NEDEN if/elif zinciri kullanıyoruz, match-case (Python 3.10+) yerine?
    # match-case burada da kullanılabilirdi ve daha modern görünürdü, ancak
    # 4 dallı basit bir yönlendirme için if/elif hem daha geniş Python sürüm
    # uyumluluğu sağlar hem de okunurluk açısından fark yaratmaz. Bu, "her
    # yeni özelliği kullanmak zorunda değilsin, iş göreni seç" prensibinin
    # bir örneğidir.
    if args.komut == "add":
        gorev_ekle(args.baslik)
    elif args.komut == "list":
        gorevleri_listele(sadece_bekleyen=args.bekleyen)
    elif args.komut == "done":
        gorev_tamamla(args.id)
    elif args.komut == "delete":
        gorev_sil(args.id)


# NEDEN bu blok en altta?
# __name__ == "__main__" kontrolü, bu dosya doğrudan çalıştırıldığında
# (python todo.py ...) main()'i tetikler, ama başka bir dosya bu modülü
# import ederse (örn. "from todo import gorev_ekle") main() otomatik
# çalışmaz. Bu, modülün hem "script" hem de "kütüphane" olarak
# kullanılabilmesini sağlayan standart Python idiomudur.
if __name__ == "__main__":
    main()