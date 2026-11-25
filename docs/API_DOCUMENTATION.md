# CineVibe — REST API Documentation
**Base URL:** `/api/v1`  
**Protocol:** HTTPS  
**Authentication:** Bearer JWT Token (or Session Cookie)  
**Content-Type:** `application/json`  

---

## 1. Movies & Content Discovery

### `GET /api/v1/movies`
Retrieve a paginated, filterable list of movies from the 86,155+ catalog.
- **Query Parameters:**
  - `query` (string, optional): Search keyword.
  - `genre` (string, optional): Action, Thriller, Drama, Comedy, Sci-Fi, Romance, Horror, Animation.
  - `language` (string, optional): Hindi, English, Tamil, Telugu, Malayalam, Korean, Japanese.
  - `year` (integer, optional): Release year (e.g. 2024).
  - `quality` (string, optional): 2160p, 1080p, 720p, 480p.
  - `category` (string, optional): bollywood, hollywood, south, anime, series.
  - `sort` (string, optional): `latest` (default), `oldest`, `size_desc`, `size_asc`.
  - `page` (integer, optional, default: 1): Page index.
  - `limit` (integer, optional, default: 24): Items per page.
- **Response `200 OK`:**
  ```json
  {
    "status": "success",
    "total": 86155,
    "page": 1,
    "limit": 24,
    "total_pages": 3590,
    "data": [
      {
        "id": "6aa6dffdd558e3a6ed9a77cd",
        "file_id": "BAADBAADcRUAArVVeFA78d57cJ0PSBYE",
        "title": "Farrey",
        "clean_title": "Farrey 2024 2160p ZEE5 WEB DL Hindi DDP5 1 H 265 Archie mkv",
        "year": 2024,
        "quality": "2160p 4K",
        "file_size": 2256934057,
        "file_size_human": "2.10 GB",
        "languages": ["Hindi"],
        "poster_url": "https://image.tmdb.org/t/p/w500/...",
        "backdrop_url": "https://image.tmdb.org/t/p/w1280/...",
        "rating": 7.4,
        "is_authorized": true
      }
    ]
  }
  ```

### `GET /api/v1/movies/trending`
Retrieve curated trending movies for the hero carousel.
- **Response `200 OK`:** Returns top 12 trending titles with full backdrop art, ratings, and loglines.

### `GET /api/v1/movies/{id}`
Retrieve complete metadata for a specific movie.
- **Response `200 OK`:**
  ```json
  {
    "status": "success",
    "data": {
      "id": "6aa6dffdd558e3a6ed9a77cd",
      "title": "Farrey",
      "year": 2024,
      "tagline": "The ultimate exam thriller.",
      "overview": "An orphan genius scholarship student gets enticed into an elite high school cheating syndicate...",
      "runtime": "130 min",
      "genres": ["Thriller", "Drama"],
      "languages": ["Hindi"],
      "cast": ["Alizeh Agnihotri", "Ronit Roy", "Sahil Mehta"],
      "director": "Soumendra Padhi",
      "rating": 7.4,
      "poster_url": "...",
      "backdrop_url": "...",
      "trailer_url": "https://youtube.com/watch?v=...",
      "available_formats": [
        {
          "resolution": "2160p 4K HDR",
          "file_size": "2.10 GB",
          "format": "MKV (H.265 / HEVC)",
          "audio": "Hindi DDP 5.1",
          "subtitles": ["English"],
          "verified_rights": "CineVibe Authorized Distribution",
          "can_download": true,
          "can_stream": true
        }
      ]
    }
  }
  ```

---

## 2. CineVibe AI Discovery

### `POST /api/v1/ai/search`
Process a natural language search query through CineVibe AI.
- **Request Body:**
  ```json
  {
    "prompt": "Show me 4K action movies from 2024 with high rating"
  }
  ```
- **Response `200 OK`:**
  ```json
  {
    "status": "success",
    "intent": {
      "query": "",
      "genre": "Action",
      "year": 2024,
      "quality": "2160p",
      "min_rating": 7.0
    },
    "ai_reply": "Here are top-rated 2024 Action movies available in ultra-crisp 4K UHD.",
    "results": [...]
  }
  ```

---

## 3. Downloads & Streaming

### `POST /api/v1/downloads/create-token`
Issue an authorized, expiring download token for a movie format.
- **Request Body:**
  ```json
  {
    "file_id": "BAADBAADcRUAArVVeFA78d57cJ0PSBYE",
    "format_id": "2160p"
  }
  ```
- **Response `200 OK`:**
  ```json
  {
    "status": "success",
    "token": "71WAfd5_4O8CmVd...3zeNWnbYp08TQ",
    "download_url": "/download/71WAfd5_4O8CmVd...3zeNWnbYp08TQ",
    "stream_url": "/watch/116/Farrey.mkv?hash=AgADwB",
    "expires_in_seconds": 1800,
    "max_downloads": 10
  }
  ```

---

## 4. User Accounts & Preferences

- `POST /api/v1/auth/register`: Register new account with email & password.
- `POST /api/v1/auth/login`: Authenticate and receive JWT session.
- `GET /api/v1/auth/me`: Get current user profile and preferences.
- `GET /api/v1/user/watchlist`: Get user's saved watchlist.
- `POST /api/v1/user/watchlist`: Add or remove title from watchlist.
- `GET /api/v1/user/favorites`: Get user favorites.
- `POST /api/v1/user/favorites`: Toggle favorite status.

---

## 5. Content Requests & Copyright Compliance

### `POST /api/v1/requests`
Submit a movie request.
- **Request Body:**
  ```json
  {
    "title": "Kalki 2898 AD",
    "year": 2024,
    "language": "Hindi",
    "notes": "Looking for the 4K Hindi dubbed release."
  }
  ```

### `POST /api/v1/dmca/claim`
Submit a formal copyright infringement notice.
- **Request Body:**
  ```json
  {
    "claimant_name": "Studio Legal Representative",
    "claimant_email": "legal@studio.com",
    "company_name": "Cinema Rights Worldwide LLC",
    "copyrighted_work_title": "Example Film Title",
    "infringing_url_or_id": "https://cinevibe.tv/movie/6aa6dffdd558e3a6ed9a77cd",
    "statement": "I have a good faith belief that use of the material is not authorized by the copyright owner."
  }
  ```

---

## 6. Admin Control Center (`/api/v1/admin`)

- `GET /api/v1/admin/stats`: Total catalog records, users, downloads, server uptime, bot status.
- `GET /api/v1/admin/rights`: List and filter all content rights records.
- `POST /api/v1/admin/rights/verify`: Set rights status (Authorized, Suspended, Under Review).
- `GET /api/v1/admin/claims`: Review DMCA/Copyright complaint queue.
- `POST /api/v1/admin/claims/{id}/resolve`: Take action on copyright complaint (Disable file, Reject claim).
- `GET /api/v1/admin/bot-status`: Check Telegram bot connectivity, ping, and pre-warmed session pools.

