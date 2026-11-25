# CineVibe — Security Architecture & Policy
**Classification:** Public Security Specification  
**Platform:** CineVibe — Your World of Cinema  
**Version:** 1.0.0  

---

## 1. Authentication & Session Security
- **Password Storage:** Passwords hashed with PBKDF2-HMAC-SHA256 (100,000 rounds) using a cryptographically random 16-byte salt per user.
- **Tokens:** JWT access tokens signed with HMAC-SHA256 and configurable expiration.
- **Session Protection:** Tokens are stored in client memory or secure HTTP storage; no credentials stored in cleartext.

---

## 2. Download Token & Storage Protection
- **No Direct Storage Exposure:** Direct MTProto credentials, bot tokens, and internal channel IDs are strictly withheld from the browser.
- **Expiring Download Tokens:** Generated through `DownloadTokenManager` (`secrets.token_urlsafe(32)`). Each token is valid for 1800 seconds and permits a maximum of 10 downloads.
- **IP Rate Limiting:** Enforced via `utils_download.ip_rate_limiter` to prevent denial-of-service or scraping attacks.

---

## 3. Injection, CSRF & XSS Prevention
- **Parameterized Queries:** All SQLite interactions use parameterized queries (`?`) to prevent SQL injection.
- **Regex Sanitization:** User-submitted search keywords are escaped with `re.escape()` to prevent regex injection or catastrophic backtracking.
- **Filename Sanitization:** Downloads use `sanitize_filename()` to eliminate path traversal characters (`..`, `/`, `\`, null bytes).

---

## 4. Rights Management & DMCA Compliance
- Every title is indexed with a formal rights verification state (`is_authorized: true`).
- The public DMCA form allows rights holders to submit formal infringement notices.
- Immediate suspension workflow available in `/admin` to disable access to disputed files within minutes.

