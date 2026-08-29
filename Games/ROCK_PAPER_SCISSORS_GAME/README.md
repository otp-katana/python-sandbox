# 🪨📄✂️ Taş Kağıt Makas — Terminal Oyunu

Python ile geliştirilmiş, ASCII sanatlı ve mini animasyonlarla desteklenmiş bir terminal Taş-Kağıt-Makas oyunu. Proje `main.py` (oyun döngüsü ve mantık) ve `utils.py` (arayüz, animasyon ve yardımcı fonksiyonlar) olmak üzere iki dosyaya ayrılmış durumda.

---

## ✅ Görevler (Faz Bazlı)

### Faz 1 — Temel Mantık ve Kurulum
- [x] `random` modülünü projeye dahil et.
- [x] Taş, Kağıt, Makas seçeneklerini bir listede tanımla.
- [x] Kullanıcıdan hamlesini girdi olarak al.
- [x] Bilgisayara listeden rastgele bir hamle seçtir ve ekrana yazdır.

### Faz 2 — Karşılaştırma ve Sonuç
- [x] Aynı hamle seçildiğinde "Berabere" durumunu tespit et ve bildir.
- [x] `if-elif-else` ile oyuncunun kazandığı tüm ihtimalleri (Taş-Makas, Kağıt-Taş, Makas-Kağıt) kodla.
- [x] Kalan tüm durumlarda bilgisayarın kazandığını belirle.

### Faz 3 — Oyun Döngüsü ve Skor
- [x] Oyunu bir döngüye alarak sürekli tekrar etmesini sağla.
- [x] Döngü dışında `oyuncu_skoru` ve `bilgisayar_skoru` değişkenlerini tanımla, her el kazananın skorunu 1 artır.
- [x] Kullanıcı çıkış seçeneğini (`0`) girdiğinde döngüyü sonlandır.

### Faz 4 — Geliştirme (Bonus)
- [x] Kullanıcı geçersiz bir değer girerse uyarı ver ve tekrar girdi iste.
- [ ] ~~Büyük/Küçük harf duyarlılığı (`.lower()`/`.capitalize()`)~~ — girdi sayısal (`0-3`) olduğu için bu madde artık uygulanabilir değil; proje metin girdisinden sayısal menü girdisine evrildi.

### Faz 5 — Sıradaki Adımlar (Öneri)
- [ ] `int(input()).strip()` hatasını düzelt (bkz. Eleştiri #1).
- [ ] Skor/hamle mantığını sözlük tabanlı yapıya taşı (bkz. Eleştiri #3, #4).
- [ ] Tekrarlanan skor kutusu kodunu tek bir fonksiyona çıkar (bkz. Eleştiri #6).
- [ ] Gerçek tur sayacı ekle (bkz. Eleştiri #5).
- [ ] Oyun durumunu global değişkenler yerine bir `class` içinde topla (bkz. Eleştiri #2).

---

## 📦 Proje Neler Yapıyor?

### 1. Giriş Deneyimi
`GirişArayüzü()`, ASCII-art bir logo bastırarak oyuncuyu karşılıyor. Ardından `GirişYüklenmeAnimasyonu()` sahte bir "sistem başlatma" animasyonu oynatarak terminale retro/hacker havası katıyor. `Kurallar()` fonksiyonu kontrol tuşlarını ve kazanma koşullarını özetleyen bir kutu yazdırıyor.

### 2. Ana Oyun Döngüsü (`main.py`)
Dış `while oyunbitti:` döngüsü, oyuncu 3 skora ulaşana ya da çıkış yapana kadar sürekli tur oynatıyor. Her tur şu adımlardan oluşuyor:
- **Bilgisayarın hamlesi** `random.choice()` ile üç seçenekten rastgele belirleniyor.
- **Oyuncu girdisi** `AnaMenü()` ile gösterilen menüden `int(input())` şeklinde alınıyor; 0-3 aralığı dışına çıkan ya da sayı olmayan girdilerde `HatalıGiriş()` uyarısı basılıp döngü tekrar başa dönüyor.
- Her iki tarafın seçimi de `taş()`, `kağıt()`, `makas()` fonksiyonlarıyla ASCII olarak ekrana basılıyor.

### 3. Karşılaştırma ve Skor Mantığı
İkinci `while True` bloğu, seçilen iki hamleyi karşılaştırıp üç duruma ayırıyor:
- **Beraberlik** → `Berabere()` animasyonu, skor değişmiyor.
- **Oyuncu kazanır** → `OyuncuSkorDurumu += 1`, `Kazanma()` animasyonu.
- **Bilgisayar kazanır** → `BilgisayarSkorDurumu += 1`, `Kaybetme()` animasyonu.

Her sonuçtan sonra güncel skor kutu içinde ekrana basılıyor. Skorlardan biri 3'e ulaştığında `OyunuKazanma()` ya da `OyunuKaybetme()` tetiklenip `oyunbitti = False` ile dış döngü sonlandırılıyor.

### 4. Çıkış Akışı
Oyuncu `0` girerse `ÇıkışAnimasyonu()` çalışıyor ve "sistem kapanıyor" temalı bir seri mesaj gecikmeli olarak basılıyor.

### 5. Hatalı Girdi Koruması
`try/except ValueError` bloğu sayısal olmayan girdileri yakalıyor; `HatalıGiriş()` ASCII kedi karakteriyle kullanıcıyı uyarıyor ve tekrar deneme şansı veriyor.

### 6. Görsel/Animasyon Katmanı (`utils.py`)
Tüm ekran çıktıları (`GirişArayüzü`, `Kurallar`, `AnaMenü`, hamle çizimleri, kazanma/kaybetme kutuları, yükleme animasyonu) `utils.py` içinde toplanıp ana belgeye çağrılmış.

---

## 🔎 ELEŞTİRİ VE GELİŞTİRME ÖNERİLERİ

Bu bölüm "yanlış" demek için değil; kodun mevcut haliyle nasıl çalıştığını ve bir sonraki mini projede/geliştirmede nelerin daha sağlam olabileceğini göstermek için.

### 1. Global değişkenlere bağımlılık
`OyuncuSkorDurumu`, `BilgisayarSkorDurumu`, `KullanıcıSeçimi`, `BilgisayarınSeçimi` gibi değişkenler fonksiyonlar arasında global olarak paylaşılıyor. Küçük bir script için çalışır, ama proje büyüdükçe hangi fonksiyonun neyi değiştirdiğini takip etmek zorlaşır. 
**Daha iyisi:** Oyun durumunu bir `sözlük` ya da küçük bir `class Oyun:` içinde tutup, fonksiyonlara parametre olarak geçirmek (ya da `self.` üzerinden erişmek). Bu hem test edilebilirliği hem okunabilirliği artırır.

### 2. Tekrarlanan if-elif zincirleri
Kazanma/kaybetme/beraberlik mantığı üç büyük `or`'lu koşul zinciriyle yazılmış. Okunması zor ve yeni bir hamle eklemek (örneğin "Taş-Kağıt-Makas-Kertenkele-Spock") kâbusa dönüşür. 
**Daha iyisi:** Yenme ilişkilerini bir sözlükte tanımlamak:
```python
YENER = {"Taş": "Makas", "Makas": "Kağıt", "Kağıt": "Taş"}

if OyuncuHamlesi == BilgisayarHamlesi:
    sonuc = "berabere"
elif YENER[OyuncuHamlesi] == BilgisayarHamlesi:
    sonuc = "kazandın"
else:
    sonuc = "kaybettin"
```
Bu tek bir sözlük satırıyla tüm `elif` bloklarının yerini alır.

### 3. `taş()`, `kağıt()`, `makas()` fonksiyonları üç kez tekrar çağrılıyor
Aynı üç fonksiyon hem oyuncu hem bilgisayar için ayrı ayrı if-elif ile çağrılıyor. 
**Daha iyisi:** Yine fonksiyonları bir sözlükte tutup çağırmak:
```python
HAMLE_ÇİZİMLERİ = {"Taş": taş, "Kağıt": kağıt, "Makas": makas}
HAMLE_ÇİZİMLERİ[BilgisayarınSeçimi]()
```

### 4. Skor tablosunda sabit "TUR: 1" yazısı
Skor kutusundaki `[ TUR: 1 ]` metni her turda aynı kalıyor, gerçek tur sayısını takip eden bir sayaç yok. Küçük ama fark edilir bir görsel tutarsızlık. 
**Daha iyisi:** Bir `tur_sayaci` değişkeni tanımlayıp her turda `+= 1` yapmak.

### 5. Aynı skor kutusu üç kez neredeyse birebir kopyalanmış
Beraberlik, kazanma ve kaybetme bloklarının her birinde neredeyse aynı `print(f"""...""")` bloğu tekrar ediliyor. 
**Daha iyisi:** Bunu `SkorGoster(oyuncu, bilgisayar, tur)` adında tek bir fonksiyona çıkarmak, kodu ~30 satır kısaltır.

### 6. `import time` fonksiyon içlerinde tekrar tekrar yapılıyor
`utils.py` içindeki her animasyon fonksiyonu kendi içinde `import time` satırı içeriyor. Python bunu sorunsuz çalıştırır (modül cache'lenir) ama gereksizdir. 
**Daha iyisi:** Dosyanın en üstüne tek bir `import time` koymak yeterli.

### 7. Girdi doğrulama ile oyun mantığının iç içe geçmesi
`main.py` içindeki dış döngüde hem girdi alma hem hamle çizme hem "geçersiz girdi" kontrolü aynı bloğa sıkıştırılmış. 
**Daha iyisi:** `hamle_al()` gibi ayrı bir fonksiyon yazıp sadece geçerli bir `1-3` değeri döndürene kadar döngüde tutmak — `main.py`'deki ana akışı çok daha okunur hale getirir.

### 8. İsimlendirme tutarlılığı
`TaşKağıtMakas`, `oyunbitti`, `OyuncuSkorDurumu` gibi değişkenler PascalCase/camelCase/snake_case karışımı kullanıyor. Fonksiyonel olarak sorun yaratmıyor ama PEP8 açısından `snake_case` (örn. `oyuncu_skoru`) daha standarttır.

---