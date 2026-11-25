# CineVibe — Backup & Disaster Recovery Plan
**Platform:** CineVibe — Your World of Cinema  
**Recovery Time Objective (RTO):** < 15 Minutes  
**Recovery Point Objective (RPO):** < 1 Hour  

---

## 1. Data Classification

| Asset | Storage Engine | Criticality | Backup Frequency |
| :--- | :--- | :--- | :--- |
| **Media Documents** | MongoDB Atlas | Mission-Critical | Continuous Continuous Cloud Snapshots (Atlas M0/M10) |
| **Relational Data** | SQLite (`movie_bot.db`) | High | Daily automated file copy |
| **Telegram Session** | `Dhruvit.session` (SQLite) | Critical | Backed up securely off-repository |
| **Environment Config** | `.env` | Confidential | Secure offline secret vault |

---

## 2. Backup Procedures

### SQLite Database Backup:
```bash
# Safely snapshot movie_bot.db while application is running
python -c "
import sqlite3, shutil, datetime
src = 'movie_bot.db'
dst = f'backups/movie_bot_{datetime.datetime.now().strftime(\"%Y%m%d_%H%M%S\")}.db'
conn = sqlite3.connect(src)
bck = sqlite3.connect(dst)
conn.backup(bck)
bck.close()
conn.close()
print('Backup created:', dst)
"
```

### MongoDB Atlas Export:
```bash
# Dump collection to JSON archive
mongoexport --uri="mongodb+srv://..." --collection=Dhruvitnew --out=cinevibe_media_backup.json
```

---

## 3. Recovery Procedure
1. Provision host or container running Python 3.13.
2. Restore `.env` from secure secret store.
3. Restore `movie_bot.db` from latest snapshot.
4. Restore `Dhruvit.session` to retain MTProto authentication.
5. Execute `python bot.py`.
6. Run `GET /api/v1/admin/stats` to verify 100% operational restoration.

