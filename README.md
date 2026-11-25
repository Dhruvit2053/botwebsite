# CineVibe — Your World of Cinema

AI-Powered Movie Discovery, Content Management & Authorized High-Speed Download Ecosystem.

## Features
- **Visual Streaming Interface**: Deep Black (#080808) and Golden Yellow (#FFC928) aesthetic with glassmorphism and ambient glow.
- **Hero Trending Poster Slider**: Auto-sliding cinematic showcase with real backdrops.
- **11 Curated Homepage Sections**: Trending Now, Latest Releases, 4K UHD, Editor's Picks, Recommended, South Cinema, Web Series, and more.
- **Real Movie Posters**: Authentic official posters (IMDb / Amazon / Wikimedia) for all titles.
- **High-Speed Download & Stream Integration**: Directly connected to the Telegram Bot multi-socket stream server (`http://127.0.0.1:8080`).
- **Gemini AI Cinema Assistant**: Integrated with Google Gemini 3.1 Flash Lite API for real-time recommendations and film insights.
- **PWA & Offline Ready**: Web App Manifest and Service Worker for mobile and desktop app experience.
- **Surge.sh Deployment Ready**: Complete with `200.html` for clean SPA routing.

## Deployment on Surge
```bash
npx surge . cinevibe-cinema.surge.sh
```

## Configuration
In the top right header, click the **Settings** icon to configure:
1. **Bot Streamer Base URL**: Set your local or remote Telegram bot streamer (default: `http://127.0.0.1:8080`).
2. **Gemini API Key**: Set your Google Gemini API key.

