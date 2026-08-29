import urllib.request  # HTTP istekleri için (requests kütüphanesi yerine standart kütüphane)
import json            # GitHub API'den gelen JSON verisini okumak için
import sys             # Hata durumunda programdan çıkmak için


# ──────────────────────────────────────────────
#  SABİTLER
#  GitHub API'ın temel adresi
# ──────────────────────────────────────────────

GITHUB_API = "https://api.github.com"


# ──────────────────────────────────────────────
#  API İSTEĞİ YAPAN FONKSİYON
#  Verilen URL'e istek atar, JSON olarak döndürür.
#  Hata oluşursa None döner.
# ──────────────────────────────────────────────

def api_istegi_yap(url):
    try:
        # GitHub API header gerektiriyor: JSON formatında yanıt istiyoruz.
        istek = urllib.request.Request(
            url,
            headers={"Accept": "application/vnd.github+json"}
        )

        # İsteği gönderir ve yanıtı okur.
        with urllib.request.urlopen(istek) as yanit:
            veri = yanit.read().decode("utf-8")   # Bytes'ı, string'e çevirir.
            return json.loads(veri)               # String'i, Python dict'e çevirir.

    except urllib.error.HTTPError as e:
        # 404 → repo bulunamadı, 403 → API limiti aşıldı gibi hata mesahları.
        print(f"[HATA] HTTP hatası: {e.code} - {e.reason}")
        return None

    except urllib.error.URLError as e:
        # İnternet bağlantısı yoksa bu blok çalışır.
        print(f"[HATA] Bağlantı hatası: {e.reason}")
        return None


# ──────────────────────────────────────────────
#  REPO LİNKİNİ AYRIŞTIRMA FONKSİYONU
#  "https://github.com/kullanici/repo" linkinden
#  kullanıcı adı ve repo adını ayrı ayrı çeker.
# ──────────────────────────────────────────────

def link_ayristir(link):
    try:
        link = link.strip().rstrip("/")   # Baştaki/sondaki boşluk ve slash'ı temizler.

        # Link github.com içeriyorsa URL formatında gelmiş demektir.
        if "github.com" in link:
            parcalar = link.split("github.com/")[-1].split("/")
        else:
            # Doğrudan "kullanici/repo" formatında girilmiş olabilir.
            parcalar = link.split("/")

        if len(parcalar) < 2:
            raise ValueError("Geçersiz format. 'kullanici/repo' veya tam GitHub linki girin.")

        kullanici = parcalar[0]
        repo      = parcalar[1]
        return kullanici, repo

    except ValueError as e:
        print(f"[HATA] {e}")
        return None, None


# ──────────────────────────────────────────────
#  GENEL BİLGİLER FONKSİYONU
#  Repo adı, açıklama, yıldız, fork, izleyici
#  ve oluşturulma/güncellenme tarihleri gösterilir.
# ──────────────────────────────────────────────

def genel_bilgileri_yazdir(veri):
    print("\n========================================")
    print("           GENEL BİLGİLER")
    print("========================================")
    print("Repo Adı     : " + veri["full_name"])

    # Açıklama yoksa "Belirtilmemiş" yazar.
    aciklama = veri["description"] if veri["description"] else "Belirtilmemiş"
    print("Açıklama     : " + aciklama)

    print("Yıldız       : " + str(veri["stargazers_count"]))
    print("Fork         : " + str(veri["forks_count"]))
    print("İzleyici     : " + str(veri["watchers_count"]))
    print("Açık Issue   : " + str(veri["open_issues_count"]))

    # Lisans bilgisi varsa adını gösterir, yoksa "Yok" yazar.
    lisans = veri["license"]["name"] if veri["license"] else "Yok"
    print("Lisans       : " + lisans)

    # Tarihler ISO 8601 formatında geliyor (2024-01-15T10:30:00Z), sadece tarihi al.
    olusturulma = veri["created_at"][:10]
    guncelleme  = veri["updated_at"][:10]
    print("Oluşturulma  : " + olusturulma)
    print("Son Güncell. : " + guncelleme)


# ──────────────────────────────────────────────
#  DİL DAĞILIMI FONKSİYONU
#  Her dilin kaç byte kod içerdiğini gösterir,
#  toplam içindeki yüzdesini hesaplar.
# ──────────────────────────────────────────────

def dil_dagilimini_yazdir(kullanici, repo):
    url  = f"{GITHUB_API}/repos/{kullanici}/{repo}/languages"
    veri = api_istegi_yap(url)

    if not veri:
        print("\n[BİLGİ] Dil bilgisi alınamadı.")
        return

    print("\n========================================")
    print("           DİL DAĞILIMI")
    print("========================================")

    # Toplam byte sayısını hesaplar. (yüzde hesabı için)
    toplam = sum(veri.values())

    # Dilleri byte sayısına göre büyükten küçüğe sıralar.
    sirali = sorted(veri.items(), key=lambda x: x[1], reverse=True)

    for dil, byte in sirali:
        yuzde     = (byte / toplam) * 100           # Yüzde hesaplar
        yuzde_str = str(round(yuzde, 1)) + "%"      # Bir ondalık basamağa yuvarlar
        print(f"  {dil:<20} {yuzde_str:>6}   ({byte:,} byte)")


# ──────────────────────────────────────────────
#  COMMİT GEÇMİŞİ FONKSİYONU
#  Son 10 commit'i listeler: tarih, yazar, mesaj
# ──────────────────────────────────────────────

def commit_gecmisini_yazdir(kullanici, repo):
    # per_page=10 ile sadece son 10 commit'i ister.
    url  = f"{GITHUB_API}/repos/{kullanici}/{repo}/commits?per_page=10"
    veri = api_istegi_yap(url)

    if not veri:
        print("\n[BİLGİ] Commit bilgisi alınamadı.")
        return

    print("\n========================================")
    print("         SON 10 COMMİT")
    print("========================================")

    for i, commit in enumerate(veri, start=1):   # start=1 → sayaç 1'den başlasın
        mesaj = commit["commit"]["message"].split("\n")[0]   # Sadece ilk satırı al
        yazar = commit["commit"]["author"]["name"]
        tarih = commit["commit"]["author"]["date"][:10]      # Sadece tarihi al

        print(f"\n  [{i}] {tarih} - {yazar}")
        print(f"       {mesaj}")


# ──────────────────────────────────────────────
#  REPO LİNKİ ALMA FONKSİYONU
#  Kullanıcıdan geçerli bir link girmesini ister.
# ──────────────────────────────────────────────

def repo_linki_al():
    while True:
        try:
            link = input("\nGitHub repo linki veya 'kullanici/repo': ").strip()

            if not link:
                raise ValueError("Boş giriş yapılamaz.")

            kullanici, repo = link_ayristir(link)

            if not kullanici or not repo:
                raise ValueError("Link ayrıştırılamadı.")

            return kullanici, repo

        except ValueError as e:
            print(f"[HATA] {e} Tekrar deneyin.")


# ──────────────────────────────────────────────
#  ANA PROGRAM
# ──────────────────────────────────────────────

def main():
    print("\n========================================")
    print("       GITHUB REPO ANALİZCİSİ")
    print("========================================")
    print("Örnek giriş: https://github.com/kullanici/repo")
    print("         ya: kullanici/repo")

    while True:
        kullanici, repo = repo_linki_al()

        # Önce repo var mı diye kontrol et.
        url  = f"{GITHUB_API}/repos/{kullanici}/{repo}"
        veri = api_istegi_yap(url)

        if not veri:
            print("[HATA] Repo bulunamadı veya erişilemiyor.")
        else:
            genel_bilgileri_yazdir(veri)
            dil_dagilimini_yazdir(kullanici, repo)
            commit_gecmisini_yazdir(kullanici, repo)

        print("\n----------------------------------------")
        tekrar = input("Başka bir repo analiz etmek ister misiniz? (e/h): ").strip().lower()
        if tekrar != "e":
            print("\nGüvenli günler!")
            sys.exit(0)


if __name__ == "__main__":
    main()
