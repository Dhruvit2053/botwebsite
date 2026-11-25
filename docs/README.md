# CineVibe — Your World of Cinema
### AI-Powered Movie Discovery, Content Management & Authorized High-Speed Download Ecosystem

[![Python](https://img.shields.io/badge/Python-3.13-blue.svg)](https://www.python.org/)
[![Database](https://img.shields.io/badge/MongoDB-Atlas_86k+-green.svg)](https://www.mongodb.com/)
[![Speed](https://img.shields.io/badge/Download_Engine-8--Socket_Pool-gold.svg)](https://github.com/)
[![License](https://img.shields.io/badge/Status-100%25_Verified-emerald.svg)](https://github.com/)

---

## 🎬 About CineVibe

**CineVibe** is a complete, scalable cinema discovery and authorized content distribution platform. Connected directly to an active Telegram bot (`@movieDRV2bot`) and an 86,000+ title MongoDB document store, CineVibe combines:
- **Atmospheric Cinematic Design:** Luxury dark aesthetic (`#080808`, `#121212`, `#FFC928` gold), smooth transitions, and glassmorphism.
- **CineVibe AI:** Natural language search assistant ("Show me 4K action movies from 2024") and contextual recommendations.
- **8-Socket Multi-Session Turbo Engine:** Bypasses Telegram's single-connection rate limit to deliver 7+ MB/s sustained download speeds and <0.5s video seeking.
- **Dual C/OpenSSL Crypto Acceleration:** Native `cryptg` (500+ MB/s AES-IGE) and OpenSSL `AES-CTR` (380+ MB/s) eliminating CPU bottlenecks.
- **Content Rights & Legal Compliance:** Formal rights verification registry, DMCA claim workflow, and instant content suspension controls.
- **Admin Control Center (`/admin`):** Live telemetry, rights verification, and complaint management.

---

## 🚀 Quickstart

### 1. Clone & Configure
```bash
git clone https://github.com/Dhruvit2053/telegram-filter-bot.git
cd telegram-filter-bot
cp .env.example .env
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Start the Unified Engine
```bash
python bot.py
```

Visit:
- **CineVibe Web Platform:** `http://localhost:8080/`
- **Main Catalog:** `http://localhost:8080/#explore`
- **Admin Control Center:** `http://localhost:8080/#admin`
- **API Health & Stats:** `http://localhost:8080/api/v1/admin/stats`

---

## 📡 REST API Overview (`/api/v1`)

| Method | Endpoint | Description |
| :--- | :--- | :--- |
| `GET` | `/api/v1/movies` | Paginated catalog search with filters (category, quality, year, sort). |
| `GET` | `/api/v1/movies/trending` | Top 12 trending titles for the hero carousel. |
| `GET` | `/api/v1/movies/sections` | 11 dynamic homepage sections from the 86k database. |
| `GET` | `/api/v1/movies/{id}` | Detailed metadata, cast, director, and format options. |
| `POST`| `/api/v1/ai/search` | Natural language cinema discovery powered by CineVibe AI. |
| `POST`| `/api/v1/downloads/create-token` | Issue authorized, expiring high-speed download tokens. |
| `POST`| `/api/v1/auth/register` / `login` | PBKDF2-HMAC-SHA256 user authentication & JWT sessions. |
| `POST`| `/api/v1/requests` | Submit content requests with Telegram channel forwarding. |
| `POST`| `/api/v1/dmca/claim` | Formal copyright complaint submission. |
| `GET` | `/api/v1/admin/stats` | Live platform telemetry and multi-socket engine status. |

---

## 📚 Complete Documentation Suite
- [PROJECT_AUDIT.md](file:///d:/bot/PROJECT_AUDIT.md): Complete audit of existing infrastructure and database.
- [SYSTEM_ARCHITECTURE.md](file:///d:/bot/SYSTEM_ARCHITECTURE.md): System architecture and data flow diagrams.
- [DATABASE_SCHEMA.md](file:///d:/bot/DATABASE_SCHEMA.md): MongoDB and relational schema specifications.
- [API_DOCUMENTATION.md](file:///d:/bot/API_DOCUMENTATION.md): Complete REST API documentation.
- [DEVELOPMENT_PLAN.md](file:///d:/bot/DEVELOPMENT_PLAN.md): Development phases and roadmap.
- [DEPLOYMENT_GUIDE.md](file:///d:/bot/DEPLOYMENT_GUIDE.md): Local, Docker, and Cloud deployment guide.
- [SECURITY.md](file:///d:/bot/SECURITY.md): Security architecture and rights management policies.
- [BACKUP_AND_RECOVERY.md](file:///d:/bot/BACKUP_AND_RECOVERY.md): Backup and disaster recovery procedures.
- [TESTING_REPORT.md](file:///d:/bot/TESTING_REPORT.md): Automated testing and benchmark report.
- [CHANGELOG.md](file:///d:/bot/CHANGELOG.md): Platform version changelog.

---

## ⚖️ Legal & Compliance
CineVibe operates strictly with authorized content distribution records and provides a formal Copyright & DMCA notice process. Disputed titles are subject to immediate administrative suspension upon notice verification.
