# 🛠️ utility-hub

**A collection of small Python utilities built while learning the language.**  
*Python öğrenirken geliştirilen küçük Python araçlarının koleksiyonu.*

---

## 📁 Projects / Projeler

### 🔐 Password Generator (`password_generator.py`)

**EN** — A command-line password generator with four strength levels and configurable length. Built to practice functions, error handling, and Python's standard library.

**TR** — Dört farklı güç seviyesi ve ayarlanabilir uzunluk seçeneği sunan bir komut satırı şifre üreticisi. Fonksiyonlar, hata yönetimi ve Python standart kütüphanesi pratiği amacıyla geliştirildi.

**Features / Özellikler:**
- 4 strength levels: Weak → Medium → Strong → Very Strong
- Configurable length between 8–20 characters
- `try/except` error handling for invalid inputs
- Guaranteed character diversity per strength level (at least one char from each required set)
- Uses `random`, `string`, and `sys` from Python's standard library — no external dependencies

---

## 🚀 Getting Started / Başlarken

**Clone the repository / Repoyu klonlayın:**
```bash
git clone https://github.com/YOUR_USERNAME/utility-hub.git
cd utility-hub
```

**Run / Çalıştırın:**
```bash
python password_generator.py
```

> No external libraries required. Python 3.x is sufficient.  
> *Harici kütüphane gerekmez. Python 3.x yeterlidir.*

---

## 🧠 What I Learned / Öğrendiklerim

**EN**  
- Structuring code with `def` functions instead of writing everything in sequence  
- Using `while` loops inside functions for input validation  
- Handling errors gracefully with `try/except/raise`  
- The difference between `random.choice()` (single) and `random.choices()` (multiple)  
- Why `"".join(list)` is preferred over building strings with a `for` loop  
- Using `if __name__ == "__main__"` to separate reusable code from executable code

**TR**  
- Her şeyi sırayla yazmak yerine `def` fonksiyonlarıyla kodu yapılandırma  
- Girdi doğrulaması için fonksiyon içinde `while` döngüsü kullanma  
- `try/except/raise` ile hataları kontrollü şekilde yönetme  
- `random.choice()` (tek) ile `random.choices()` (çoklu) arasındaki fark  
- `for` döngüsüyle string birleştirme yerine neden `"".join(liste)` tercih edildiği  
- Yeniden kullanılabilir kodu çalıştırılabilir koddan ayırmak için `if __name__ == "__main__"` kullanımı

---

## 🔮 Planned / Planlananlar

- Refactor `password_generator.py` using OOP (`class PasswordGenerator`) after completing that chapter  
- Add more utilities as new topics are covered

---

## 📌 Notes / Notlar

**EN** — This repository grows alongside my Python learning journey. Each project reflects the concepts I have studied at that point, not a final production-grade implementation.

**TR** — Bu repo Python öğrenme sürecimle birlikte büyüyor. Her proje o ana kadar çalıştığım konuları yansıtıyor, nihai bir üretim uygulaması değil.
