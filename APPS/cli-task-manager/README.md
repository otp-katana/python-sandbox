# Todo CLI — Mini Proje #1: Kas Haritası ve Ders Notları

> **Seviye:** Başlangıç
> **Ana Tema:** Dosya I/O, argparse, hata yönetimi, fonksiyonel ayrıştırma
> **Kariyer Bağlantısı:** Veri mühendisliğinde her gün yapılacak şey budur —
> bir kaynaktan veri okumak, üzerinde işlem yapmak, başka bir yere yazmak.
> Bu proje o döngünün en yalın halidir.

---

## 1. Bu Proje Neden Var?

Bir görev yöneticisi yazmak "sıradan" görünebilir ama aslında şu soruyu
cevaplıyor: **"Python'da kalıcı veri (persistent state) nasıl yönetilir?"**

Programın her çalıştırıldığında hafızası sıfırlanmaz — çünkü veriyi diske
yazıyoruz. Bu, tüm yazılımların temel sorunudur: *state'i nerede ve nasıl
tutuyorsun?* Bugün JSON dosyasıyla çözdüğün bu problemi, ileride veri
mühendisliği kariyerinde PostgreSQL, S3, Parquet dosyaları veya bir mesaj
kuyruğuyla (Kafka) çözeceksin. Mantık aynı, araç değişiyor.

---

## 2. Mimari Kararlar ve "Neden"leri

### 2.1. Neden tek dosyada (`todo.py`) ama katmanlı yazdık?

Kodun içinde üç görünmez katman var, yorum satırlarıyla işaretlenmiş halde:

```
┌─────────────────────────────┐
│   CLI Katmanı (argparse)     │  ← Kullanıcıdan girdi alır
├─────────────────────────────┤
│   İş Mantığı Katmanı         │  ← "Ne yapılacağını" bilir (ekle, sil, listele)
├─────────────────────────────┤
│   Veri Katmanı (JSON I/O)    │  ← "Nasıl saklanacağını" bilir
└─────────────────────────────┘
```

Bu proje küçük olduğu için hepsi tek dosyada, ama **kavramsal olarak
ayrılmış durumda**. Bunu neden önemsiyoruz?

Çünkü yarın "JSON yerine SQLite kullanmak istiyorum" dersen, sadece
`gorevleri_yukle()` ve `gorevleri_kaydet()` fonksiyonlarını değiştirmen
yeterli olur. `gorev_ekle()`, `gorev_tamamla()` gibi iş mantığı fonksiyonları
**hiç değişmez** çünkü onlar "veri nasıl saklanıyor" bilgisine bağımlı değil.

Bu prensibin ismi **Separation of Concerns** (İlgi Alanlarının Ayrılması).
Büyük projelerde bu ayrım genellikle farklı dosyalara/modüllere bölünür
(örn. `storage.py`, `logic.py`, `cli.py`) — 7 numaralı ileri seviye
projende (paketlenebilir ETL) bunu fiilen ayrı dosyalarda yapacaksın.

### 2.2. Neden JSON, CSV değil?

| | JSON | CSV |
|---|---|---|
| İç içe veri (nested) | ✅ Doğal destekler | ❌ Zorlama gerekir |
| Tip bilgisi (bool, int, str) | ✅ Korur | ❌ Her şey string olur |
| Python dict/list ile eşleşme | ✅ Bire bir | ❌ Manuel dönüşüm gerekir |
| İnsan tarafından okunabilirlik | ✅ (indent ile) | ✅ |

`tamamlandi` alanının `true`/`false` (bool) olarak kalması örneğin CSV'de
imkansız olurdu — her şey string'e dönerdi ve `"false"` string'i Python'da
**truthy** (yani `if "false":` her zaman `True` döner!) olduğu için sinsi
bir bug kaynağı olurdu. Bu, veri tipi seçiminin neden önemli olduğuna dair
küçük ama gerçek bir örnek.

### 2.3. Neden `next()` + generator expression, neden `list comprehension`?

Kodda iki farklı Python idiomunu bilinçli olarak kullandık:

```python
# Filtreleme -> list comprehension (TÜM eşleşenleri istiyoruz)
gorevler = [g for g in gorevler if not g["tamamlandi"]]

# Arama -> next() + generator (SADECE İLK eşleşeni istiyoruz)
hedef = next((g for g in gorevler if g["id"] == gorev_id), None)
```

Fark önemli: `list comprehension` **tüm listeyi hemen belleğe** üretir.
`next()` ile generator expression ise **tembel (lazy)** çalışır — eşleşen
ilk elemanı bulur bulmaz durur, listenin geri kalanını hiç işlemez. 10
elemanlı bir listede fark hissedilmez, ama 10 milyon satırlık bir veri
setinde (veri mühendisliğinde sık karşılaşacağın ölçek) bu fark **saniyeler
ile dakikalar arasındaki** farka dönüşebilir. Bu projede küçük ölçekte
görmen, ileri seviye projede (generator'lar konusunu derinleştireceğimiz
Proje 7'de) neden önemli olduğunu tam kavramana zemin hazırlıyor.

### 2.4. Neden hata yönetiminde `sys.exit(1)` ve `file=sys.stderr`?

Unix/Linux dünyasının temel bir sözleşmesi var:

- **stdout** (`print(...)`) → *programın normal çıktısı*. Başka bir programa
  pipe'lanabilir (`python todo.py list | grep "yaz"` gibi).
- **stderr** (`print(..., file=sys.stderr)`) → *hata ve teşhis mesajları*.
  Normal çıktıyı kirletmemesi gerekir.
- **Çıkış kodu** (`sys.exit(1)`) → Programı çağıran başka bir script veya
  CI/CD pipeline'ı, işlemin başarılı olup olmadığını bu kodla anlar.
  `0` = başarı, `0` dışı = hata (kodun kendisi genelde hata türünü de
  ifade edebilir, ama basit araçlarda `1` yeterlidir).

Bu üç kural, komut satırı araçlarının **birbirleriyle konuşabilmesinin**
temelidir (Unix felsefesi: "her araç bir işi iyi yapsın, çıktıları
birleştirilebilsin"). Bunu şimdi öğrenmek, ileride bir ETL pipeline'ının
neden loglama ve exit code'lara bu kadar önem verdiğini anlamanı sağlayacak.

### 2.5. Neden `id` hesaplamasında `max(...) + 1`, `len(liste) + 1` değil?

Bu, kodun içinde en "sinsi bug" potansiyeli taşıyan kısımdı, bilerek
seçtik çünkü öğretici:

```python
yeni_id = max((g["id"] for g in gorevler), default=0) + 1
```

Senaryo: 3 görevin var (id: 1, 2, 3). id=2'yi silersin, elinde (1, 3) kalır.
Yeni görev eklersin:

- `len(gorevler) + 1` → `2 + 1 = 3` → **ÇAKIŞMA!** (id=3 zaten var)
- `max(id'ler) + 1` → `3 + 1 = 4` → doğru, çakışma yok

Bu, gerçek veritabanlarındaki `AUTO_INCREMENT` / `SERIAL` mantığının
minyatür bir simülasyonu. Veritabanları da id'leri asla "yeniden
kullanmaz" — hep bir üst sınırdan devam eder. Şimdi bunu elle yaşaman,
ileride bir veritabanı şemasında `PRIMARY KEY AUTOINCREMENT` gördüğünde
"bu neden böyle" sorusuna zaten cevabın olacak demektir.

---

## 3. Kullanılan Python Özelliklerinin Sözlüğü

| Özellik | Bu Projede Nerede | Neden Öğrenmen Gerekiyor |
|---|---|---|
| `pathlib.Path` | `TASKS_FILE` tanımı | Modern dosya yolu yönetimi; `os.path`'ten üstün |
| `with` (context manager) | Dosya okuma/yazma | Kaynak sızıntısını (resource leak) önler |
| `try/except` (spesifik hata sınıfları) | `gorevleri_yukle()` | "Her hatayı aynı torbaya atma" disiplini |
| `f-string` | Tüm `print()` çağrıları | Okunabilir, hızlı string formatlama |
| List comprehension | `gorevleri_listele()` | Fonksiyonel filtreleme idiomu |
| Generator expression + `next()` | `gorev_tamamla()`, `gorev_sil()` | Tembel değerlendirme (lazy evaluation) |
| Type hints (`list[dict]`, `-> None`) | Tüm fonksiyon imzaları | Kodun "sözleşmesini" netleştirir, IDE desteği sağlar |
| `argparse` + subparsers | `parser_olustur()` | Profesyonel CLI tasarımı |
| `datetime.isoformat()` | `gorev_ekle()` | Standart, sıralanabilir tarih formatı |
| `__name__ == "__main__"` | Dosya sonu | Modülün hem script hem kütüphane olabilmesi |

Bilmediğin bir terim varsa, bana sor — her birini tek tek, örneklerle
derinleştirebiliriz.

---

## 4. Kurulum ve Çalıştırma

```bash
# python-sandbox reposunun kökündeki .venv'i aktive et
source .venv/bin/activate  # (Windows: .venv\Scripts\activate)

# Bu projenin klasörüne gir
cd apps/todo-cli  # kendi klasör yapına göre ayarla

# Görev ekle
python3 todo.py add "Asyncio konusunu çalış"

# Tüm görevleri listele
python3 todo.py list

# Sadece tamamlanmamışları listele
python3 todo.py list --bekleyen

# Görevi tamamlandı işaretle (id ile)
python3 todo.py done 1

# Görevi sil
python3 todo.py delete 2

# Yardım
python3 todo.py --help
python3 todo.py add --help
```

---

## 5. Bilinçli Bırakılan Eksikler (Sıradaki Katmanda Kapatılacak)

Bu proje **başlangıç seviyesi** olduğu için bazı şeyleri kasıtlı basit
bıraktık. Bunları bilmen, "bu kod eksik mi?" diye kafanı karıştırmasın:

- **Özel exception sınıfları yok** (`class GorevBulunamadi(Exception)` gibi)
  → Orta/ileri seviye projelerde işleyeceğiz.
- **Test dosyası yok** (`pytest`) → Derinleştirme fazında bu projeye de
  eklenecek (senden onay alınca).
- **Logging modülü yok**, düz `print` kullanıyoruz → İleri seviyede
  `logging` modülüyle değiştireceğiz.
- **Girdi validasyonu sınırlı** (örn. boş başlık `""` eklenebilir) →
  Bilerek bıraktık, "bonus görev" olarak sana bırakabiliriz istersen.

---

## 6. Önerilen Bonus Görevler (Derinleştirme Fazı İçin)

Konuştuğumuz "derinleştirme" stratejisine uygun olarak, bu projeye şu
kasları enjekte edebiliriz (onayını bekliyorum):

1. **Custom Exception**: `GorevBulunamadiHatasi(Exception)` sınıfı yaz,
   `sys.exit(1)` yerine bu exception'ı fırlat ve `main()` içinde yakala.
2. **Context Manager**: Kendi `TasksDosyasi` context manager sınıfını
   yaz (`__enter__`/`__exit__`), dosya açma/kapamayı `with` ile daha
   şık hale getir.
3. **pytest ile test**: `test_todo.py` yazarak `gorev_ekle`,
   `gorev_tamamla` fonksiyonlarını test et (geçici/mock dosya ile).
4. **Boş başlık validasyonu**: `gorev_ekle("")` çağrıldığında anlamlı
   bir hata ver.
5. **`ruff`/`black` entegrasyonu**: Kod formatlama ve linting aracını
   projeye tanıt.

Hangisini/hangilerini şimdi ekleyelim istersen söyle, yoksa önce
sıradaki mini projeye (Proje 2: Şifre Üretici) geçip bonus görevleri
daha sonra toplu halde mi işleyelim — sana kalmış.