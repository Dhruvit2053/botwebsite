# Backup & Restoration Guide - Telegram Movie Bot (`d:\bot`)

This directory contains your complete, working Pyrogram Telegram Movie Bot.

## Active Configuration Backup
- **`.env.backup`**: Complete copy of active environment variables (Bot Tokens, MongoDB URIs, Channels, Log Channel).

## Key Settings
- **LOG_CHANNEL**: `-1002671004694`
- **CHANNELS**: `-1002349178640 -1003949211781 -1004352306044 -1004477610369`
- **AUTH_CHANNEL**: `-1002523490157`
- **DATABASE_NAME**: `Dhruvitnew`

## How to Restore / Run your Pyrogram Bot at any time
1. Open PowerShell in `d:\bot`.
2. Run development auto-reloader:
   ```powershell
   python dev.py
   ```
3. Or run directly:
   ```powershell
   python bot.py
   ```
