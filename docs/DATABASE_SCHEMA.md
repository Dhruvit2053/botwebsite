# CineVibe — Database Schema Specification
**Database Engines:** MongoDB Atlas (Document Media Store) + SQLite / PostgreSQL (Relational & Auth Store)  
**Version:** 1.0.0  

---

## 1. MongoDB Document Collection: `Dhruvitnew.Dhruvitnew`
The primary content store holding 86,155+ records.

```json
{
  "_id": "ObjectId",
  "file_id": "String (Telegram MTProto encoded file ID)",
  "file_name": "String (Cleaned release filename)",
  "file_size": "Number (Size in bytes)",
  "caption": "String (HTML formatted caption with Telegram links)",
  "rights_verified": "Boolean (Defaults to true for authorized catalog)",
  "rights_owner": "String (License holder / CineVibe Network)",
  "license_ref": "String (Reference ID for distribution license)",
  "quality": "String (4K, 1080p, 720p, etc.)",
  "year": "Number (Parsed release year)",
  "genre": "Array of Strings",
  "language": "Array of Strings",
  "poster_url": "String (URL to poster image)",
  "backdrop_url": "String (URL to backdrop banner)",
  "rating": "Number (IMDb or TMDB score)"
}
```

---

## 2. Relational Schema (`movie_bot.db`)

### 2.1 Table: `cinevibe_users`
Web and platform users registered on CineVibe.
```sql
CREATE TABLE IF NOT EXISTS cinevibe_users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    email VARCHAR(255) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    display_name VARCHAR(100) NOT NULL,
    avatar_url VARCHAR(500),
    role VARCHAR(20) DEFAULT 'user', -- 'user', 'moderator', 'admin'
    is_active BOOLEAN DEFAULT 1,
    is_verified BOOLEAN DEFAULT 0,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    last_login DATETIME
);
```

### 2.2 Table: `content_rights`
Legal rights, licensing permits, and verification tracking.
```sql
CREATE TABLE IF NOT EXISTS content_rights (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    file_id VARCHAR(500) UNIQUE NOT NULL,
    title VARCHAR(500) NOT NULL,
    rights_owner VARCHAR(255) NOT NULL,
    license_type VARCHAR(100) NOT NULL, -- 'Owned', 'Exclusive', 'Public Domain', 'Authorized Partner'
    license_ref VARCHAR(255),
    valid_until DATE,
    territories VARCHAR(255) DEFAULT 'Worldwide',
    is_authorized BOOLEAN DEFAULT 1,
    verified_by VARCHAR(100),
    verified_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    notes TEXT
);
```

### 2.3 Table: `copyright_claims`
DMCA and copyright complaint tracking for legal compliance.
```sql
CREATE TABLE IF NOT EXISTS copyright_claims (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    claim_id VARCHAR(64) UNIQUE NOT NULL,
    claimant_name VARCHAR(255) NOT NULL,
    claimant_email VARCHAR(255) NOT NULL,
    company_name VARCHAR(255),
    copyrighted_work_title VARCHAR(500) NOT NULL,
    infringing_url_or_id VARCHAR(500) NOT NULL,
    status VARCHAR(50) DEFAULT 'Under Review', -- 'Under Review', 'Action Taken', 'Rejected', 'Resolved'
    action_taken VARCHAR(255),
    notes TEXT,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    resolved_at DATETIME
);
```

### 2.4 Table: `content_requests`
User-submitted requests for movies or series.
```sql
CREATE TABLE IF NOT EXISTS content_requests (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    title VARCHAR(500) NOT NULL,
    year INTEGER,
    language VARCHAR(100),
    notes TEXT,
    status VARCHAR(50) DEFAULT 'Pending', -- 'Pending', 'Under Review', 'Approved', 'Rejected', 'Available'
    admin_notes TEXT,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP
);
```

### 2.5 Table: `user_watchlists`
User saved watchlists.
```sql
CREATE TABLE IF NOT EXISTS user_watchlists (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    movie_id VARCHAR(255) NOT NULL,
    title VARCHAR(500) NOT NULL,
    poster_url VARCHAR(500),
    added_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    UNIQUE(user_id, movie_id)
);
```

### 2.6 Table: `user_favorites`
User favorited titles.
```sql
CREATE TABLE IF NOT EXISTS user_favorites (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    movie_id VARCHAR(255) NOT NULL,
    title VARCHAR(500) NOT NULL,
    poster_url VARCHAR(500),
    added_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    UNIQUE(user_id, movie_id)
);
```

### 2.7 Table: `analytics_events`
Platform usage and download analytics.
```sql
CREATE TABLE IF NOT EXISTS analytics_events (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    event_type VARCHAR(50) NOT NULL, -- 'page_view', 'search', 'download_started', 'download_completed', 'stream_started'
    resource_id VARCHAR(255),
    resource_title VARCHAR(500),
    ip_hash VARCHAR(64),
    user_agent VARCHAR(500),
    referrer VARCHAR(500),
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);
```

### 2.8 Table: `audit_logs`
Security and administrative change logs.
```sql
CREATE TABLE IF NOT EXISTS audit_logs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    admin_email VARCHAR(255) NOT NULL,
    action VARCHAR(100) NOT NULL,
    target_resource VARCHAR(255),
    details TEXT,
    ip_address VARCHAR(45),
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
);
```

