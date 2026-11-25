# CineVibe — Production Deployment & Operations Guide
**Platform:** CineVibe — Your World of Cinema  
**Target Environments:** Linux / Docker / Render / Heroku / Windows Server  
**Version:** 1.0.0  

---

## 1. Prerequisites
- Python 3.10+ (Python 3.13 recommended)
- MongoDB Atlas cluster URI (minimum M0 free tier or higher)
- Telegram Bot Token & API credentials (from https://my.telegram.org)
- Port 8080 exposed for HTTP/HTTPS streaming

---

## 2. Environment Configuration
Copy `.env.example` to `.env` and populate your secrets:
```bash
cp .env.example .env
```

Key environment variables:
```env
BOT_TOKEN=8920814193:AAHarDsF2eeBvupzLmym0fAPedO0ZEKsGvI
API_ID=21267502
API_HASH=ff0d341105cf6ea8d645ee555e33088a
DATABASE_URI=mongodb+srv://...
DATABASE_NAME=Dhruvitnew
COLLECTION_NAME=Dhruvitnew
LOG_CHANNEL=-1002671004694
PORT=8080
URL=https://cinevibe.onrender.com
CINEVIBE_JWT_SECRET=super_secret_cryptographic_key_here
```

---

## 3. Local & Development Execution

### Standard Python Run:
```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Run with background auto-reloader
python dev.py

# Or run directly:
python bot.py
```

Visit:
- **CineVibe Platform:** `http://localhost:8080/`
- **Main Catalog:** `http://localhost:8080/#explore`
- **Admin Control Center:** `http://localhost:8080/#admin`
- **API Health:** `http://localhost:8080/api/v1/admin/stats`

---

## 4. Docker Production Deployment

Build and run using the optimized Docker container:
```bash
# Build the Docker image
docker build -t cinevibe:latest .

# Run container with environment file
docker run -d \
  --name cinevibe-app \
  -p 8080:8080 \
  --env-file .env \
  --restart always \
  cinevibe:latest
```

---

## 5. Cloud Hosting (Render / Heroku)

### Render Deployment:
CineVibe includes `render.yaml` pre-configured as a Web Service:
- Runtime: Python / Docker
- Build Command: `pip install -r requirements.txt`
- Start Command: `python bot.py`
- Environment Variables are detected automatically from `render.yaml`.
- CineVibe's internal keepalive mechanism (`TechDRV/util/keepalive.py`) automatically self-pings `RENDER_EXTERNAL_URL` every 10 minutes to prevent the free tier from sleeping.

---

## 6. Service Verification Checklist
1. Verify HTTP 200 on `http://<host>:8080/`.
2. Verify catalog search on `http://<host>:8080/api/v1/movies?query=Farrey`.
3. Verify bot status log in Telegram `LOG_CHANNEL` (`#SYSTEM_LOGS`).
4. Verify multi-session pool: check console output for `[ByteStreamer] Multi-Session Pool active: 8 concurrent sockets on DC 4`.

