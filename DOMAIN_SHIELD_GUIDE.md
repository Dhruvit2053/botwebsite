# CineVibe Domain Shield & Safe Redirect Architecture (HDHub4u Pattern)

## Overview: Why Use This Architecture?
Popuar cinema platforms like **HDHub4u**, **Vegamovies**, and **1337x** use a **Two-Tier Domain Architecture**:
1. **Tier 1: Permanent Main Domain (The Shield Gateway)**
   - Example: `https://hdhub4u.kz/` or `https://cinevibe.com/`
   - **Characteristics**: Clean, high-SEO-rank, shared in Telegram channels, bookmarked by users.
   - **Protection**: **NEVER hosts files or content directly.**
2. **Tier 2: Disposable Worker Mirror (Content Nodes)**
   - Example: `https://new16.hdhub4u.cl/?utm=mn1` or `https://cinevibe-cinema.surge.sh`
   - **Characteristics**: Hosts the actual UI, streaming player, and file download links.
   - **Protection**: If an ISP block or copyright complaint hits `new16`, only that $1 domain is replaced by `new17`. The main domain remains 100% safe, clean, and indexed!

---

## How to Set It Up:

### Option A: Cloudflare Worker (Recommended - 0ms Server-Side Redirect)
1. Login to [Cloudflare Dashboard](https://dash.cloudflare.com).
2. Go to **Workers & Pages** -> **Create Worker**.
3. Copy the code from `gateway_worker.js`.
4. Deploy the Worker and bind it to your main domain route (e.g. `hdhub4u.kz/*` or `cinevibe.com/*`).
5. When `new16` needs to be changed to `new17`, edit `ACTIVE_MIRROR` in Cloudflare and save. Done in 5 seconds!

### Option B: Static Gateway File (`gateway.html`)
1. If your main domain is hosted on Surge, GitHub Pages, or cPanel:
   - Copy `gateway.html` as `index.html` on your main domain.
2. Edit the `ACTIVE_MIRRORS` array inside `gateway.html` to specify your active mirror URL:
   ```javascript
   const ACTIVE_MIRRORS = [
       "https://new16.hdhub4u.cl/?utm=mn1"
   ];
   ```
3. Whenever a user opens your main domain, it immediately forwards them to the active mirror with all path and query parameters preserved!

---

## File Deliverables in `botwebsite`:
- `index.html`: The active cinema mirror with genuine TMDB posters, Gemini AI assistant, and multi-socket download links.
- `gateway.html`: Client-side safe gateway for your main domain.
- `gateway_worker.js`: Cloudflare Edge server-side redirector (0ms latency, anti-crawler protection).
