# 🧮 Basit Hesap Makinesi (Python)

Bu proje, Python kullanılarak geliştirilmiş terminal tabanlı basit bir hesap makinesi uygulamasıdır.
Kullanıcı dostu bir arayüz ile dört temel matematik işlemini gerçekleştirebilir.

---

## 🚀 Özellikler

* ➕ Toplama işlemi
* ➖ Çıkarma işlemi
* ✖️ Çarpma işlemi
* ➗ Bölme işlemi
* ❌ Sıfıra bölme hatası kontrolü
* 🎨 Unicode karakterler ile tasarlanmış arayüz
* 🟥 ANSI escape kodları ile renklendirilmiş terminal çıktısı
* 🔁 Sonsuz döngü ile sürekli kullanım
* ⏳ `time.sleep()` ile daha okunabilir çıktı akışı

---

## 📸 Arayüz

Program, terminal üzerinde aşağıdaki gibi bir menü ile çalışır:

```
┌────────────────────┐
║ 4-) Bölme İşlemi   ║
║                    ║
║ 3-) Çarpma İşlemi  ║
║                    ║
║ 2-) Çıkarma İşlemi ║
║                    ║
║ 1-) Toplama İşlemi ║
└────────────────────┘
```

---

## 🛠️ Kullanım

1. Python yüklü olduğundan emin olun.
2. Projeyi klonlayın:

```
git clone https://github.com/kullanici_adin/proje_adi.git
```

3. Proje klasörüne girin:

```
cd proje_adi
```

4. Programı çalıştırın:

```
python hesap_makinesi.py
```

---

## ⚙️ Nasıl Çalışır?

* Kullanıcıdan işlem seçimi alınır.
* Seçilen işleme göre iki sayı girilmesi istenir.
* Sonuç hesaplanır ve ekrana yazdırılır.
* Bölme işleminde:

  * Sıfıra bölme kontrol edilir.
  * Sonuç tam sayı ise `int`, değilse `float` olarak gösterilir.

---

## 🧠 Öğrenim Amaçları

Bu proje aşağıdaki Python konularını pekiştirmek için geliştirilmiştir:

* `while` döngüsü
* `if-elif-else` yapıları
* Kullanıcıdan veri alma (`input`)
* Veri tipleri (`int`, `float`)
* Hata kontrolü
* Basit arayüz tasarımı
* Modül kullanımı

---

## 📌 Geliştirme Fikirleri

Projeyi daha ileri taşımak için:

* Fonksiyon (`def`) yapısı eklenebilir
* Daha fazla matematik işlemi eklenebilir
* Liste ile çoklu sayı işlemleri yapılabilir
* GUI (Tkinter, PyQt) arayüz eklenebilir
* Hata yönetimi (`try-except`) geliştirilebilir

---

## 📄 Lisans

Bu proje eğitim amaçlı geliştirilmiştir. İstediğiniz gibi kullanabilir ve geliştirebilirsiniz.

---

## 👨‍💻 Geliştirici

Bu proje, Python öğrenme sürecinde pratik yapmak amacıyla geliştirilmiştir.
