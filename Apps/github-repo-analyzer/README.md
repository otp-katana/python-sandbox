# 🔍 GitHub Repo Analyzer

**EN** — A command-line tool that analyzes any public GitHub repository using the GitHub API. Fetches general information, language breakdown, and recent commit history.

**TR** — GitHub API kullanarak herhangi bir public repoyu analiz eden komut satırı aracı. Genel bilgiler, dil dağılımı ve son commit geçmişini çeker.

---

## 📌 Features / Özellikler

- General repo info: stars, forks, watchers, open issues, license, dates
- Language breakdown with percentage and byte count
- Last 10 commits: date, author, message
- Supports both full URL and `username/repo` format
- No external dependencies — uses Python's standard library only
- `try/except` error handling for invalid input and connection errors

---

## 🚀 Getting Started / Başlarken

**Clone / Klonla:**
```bash
git clone https://github.com/YOUR_USERNAME/utility-hub.git
cd utility-hub
```

**Run / Çalıştır:**
```bash
python github_repo_analyzer.py
```

> No pip install required. Python 3.x is sufficient.  
> *Herhangi bir kurulum gerekmez. Python 3.x yeterlidir.*

---

## 💡 Usage / Kullanım

Program çalışınca aşağıdaki formatlarda giriş yapabilirsin:

```
https://github.com/psf/requests
github.com/psf/requests
psf/requests
```

**Example output / Örnek çıktı:**
```
========================================
           GENEL BİLGİLER
========================================
Repo Adı     : psf/requests
Açıklama     : A simple, yet elegant, HTTP library.
Yıldız       : 52000
Fork         : 9500
...

========================================
           DİL DAĞILIMI
========================================
  Python               98.5%   (320000 byte)
  Makefile              1.0%   (3200 byte)
...

========================================
         SON 10 COMMİT
========================================
  [1] 2024-11-10 - kennethreitz
       Initial commit
...
```

---

## 🧠 What I Learned / Öğrendiklerim

**EN**
- Making HTTP requests with `urllib.request` from the standard library (no `requests` needed)
- Parsing JSON responses with `json.loads()` and accessing data via dictionary keys
- Handling HTTP errors (`404`, `403`) and connection errors with separate `except` blocks
- Sorting a list of tuples with `sorted()` and `lambda`
- Using f-string format specifiers (`:<20`, `:>6`) for aligned terminal output
- Parsing and slicing ISO 8601 date strings (`"2024-01-15T10:30:00Z"[:10]`)

**TR**
- Standart kütüphaneden `urllib.request` ile HTTP isteği atmak (pip gerekmez)
- `json.loads()` ile JSON verisini okumak ve dict key'leriyle bilgiye ulaşmak
- HTTP hatalarını (`404`, `403`) ve bağlantı hatalarını ayrı `except` bloklarıyla yönetmek
- `sorted()` ve `lambda` ile tuple listesi sıralamak
- F-string format belirteçleriyle (`:<20`, `:>6`) hizalı terminal çıktısı üretmek
- ISO 8601 tarih string'ini dilimleme (`"2024-01-15T10:30:00Z"[:10]`)

---

## ⚠️ Notes / Notlar

**EN** — GitHub API has a rate limit of 60 requests/hour for unauthenticated users. If you hit the limit, the tool will show a `403` error. You can add a [Personal Access Token](https://github.com/settings/tokens) to the request headers to raise the limit to 5000/hour.

**TR** — GitHub API, kimlik doğrulaması yapılmamış kullanıcılar için saatte 60 istek sınırı uygular. Sınıra ulaşırsanız `403` hatası alırsınız. [Personal Access Token](https://github.com/settings/tokens) ekleyerek bu limiti saatte 5000'e çıkarabilirsiniz.

---

## 🔮 Planned / Planlananlar

- Add Personal Access Token support for higher API rate limits
- Refactor using OOP (`class RepoAnalyzer`) after completing that chapter
