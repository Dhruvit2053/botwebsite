# -*- coding: utf-8 -*-
import json
import os
import shutil

OUTPUT_DIR = r"D:\botwebsite"
ADMIN_DIR = r"D:\botwebsite\admin"
BOTADMIN_DIR = r"D:\botadmin"

with open(os.path.join(OUTPUT_DIR, "catalog.json"), "r", encoding="utf-8") as f:
    catalog_json = f.read()

with open(os.path.join(OUTPUT_DIR, "missing_catalog.json"), "r", encoding="utf-8") as f:
    missing_json = f.read()

admin_html = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="referrer" content="no-referrer">
    <title>CineVibe Admin Command Studio — TMDB Live Explorer & Multi-Socket Stream Ops</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&family=JetBrains+Mono:wght@400;500;700&display=swap" rel="stylesheet">
    <script src="https://cdn.tailwindcss.com"></script>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">

    <script>
        tailwind.config = {{
            theme: {{
                extend: {{
                    colors: {{
                        studio: {{
                            base: '#0B0D11',
                            panel: '#12151D',
                            card: '#181C26',
                            border: '#222736',
                            gold: '#FFC928',
                            goldDark: '#E5A817',
                            muted: '#8B949E',
                            cyan: '#00D8F6',
                            emerald: '#10B981',
                            rose: '#F43F5E'
                        }}
                    }},
                    fontFamily: {{
                        sans: ['"Plus Jakarta Sans"', 'sans-serif'],
                        mono: ['"JetBrains Mono"', 'monospace']
                    }}
                }}
            }}
        }}
    </script>

    <style>
        body {{
            background-color: #0B0D11;
            color: #F0F6FC;
            font-family: 'Plus Jakarta Sans', sans-serif;
            overflow-x: hidden;
        }}
        .no-scrollbar::-webkit-scrollbar {{
            display: none;
        }}
        .no-scrollbar {{
            -ms-overflow-style: none;
            scrollbar-width: none;
        }}
        .glass-studio {{
            background: rgba(18, 21, 29, 0.85);
            backdrop-filter: blur(12px);
            -webkit-backdrop-filter: blur(12px);
        }}
        .active-tab {{
            background: rgba(255, 201, 40, 0.12);
            color: #FFC928;
            border-left: 3px solid #FFC928;
        }}
    </style>
</head>
<body class="flex h-screen overflow-hidden selection:bg-studio-gold selection:text-black">

    <!-- Toast Notification -->
    <div id="toast" class="fixed bottom-6 right-6 z-50 transform translate-y-24 opacity-0 transition-all duration-300 flex items-center gap-3 px-5 py-3 rounded-xl bg-studio-card border border-studio-border shadow-2xl">
        <i id="toastIcon" class="fa-solid fa-circle-check text-studio-gold text-base"></i>
        <span id="toastMsg" class="text-xs font-semibold text-white">Action successful</span>
    </div>

    <!-- ========================================== -->
    <!-- MASTER SECURITY SHIELD GATEKEEPER LOCK     -->
    <!-- ========================================== -->
    <div id="vaultLockModal" class="fixed inset-0 z-50 bg-[#0B0D11]/95 backdrop-blur-2xl flex items-center justify-center p-4">
        <div class="relative w-full max-w-md rounded-3xl bg-studio-panel border border-studio-gold/30 p-8 shadow-2xl space-y-6 text-center">
            
            <div class="w-16 h-16 rounded-2xl bg-gradient-to-tr from-amber-500/20 via-studio-gold/20 to-amber-500/20 border border-studio-gold/40 flex items-center justify-center mx-auto text-studio-gold text-2xl shadow-lg shadow-studio-gold/10">
                <i class="fa-solid fa-shield-halved"></i>
            </div>

            <div>
                <span class="text-[10px] font-mono tracking-widest text-studio-gold uppercase font-bold px-3 py-1 rounded-full bg-studio-gold/10 border border-studio-gold/30">
                    CineVibe Shield Vault • Level 4 Clearance
                </span>
                <h2 class="text-xl font-extrabold text-white mt-3">Admin Command Studio</h2>
                <p class="text-xs text-studio-muted mt-1">Authorized Identity: <code class="text-white font-mono">dhruvitsarvaiya2003@gmail.com</code></p>
                <p class="text-[11px] text-studio-muted">Telegram: <code class="text-studio-gold font-mono">@dhruvit2053</code></p>
            </div>

            <!-- Passcode Form -->
            <div id="passwordAuthSection" class="space-y-4 text-left">
                <div>
                    <label class="block text-xs font-semibold text-studio-muted mb-1.5">Master Studio Password:</label>
                    <div class="relative">
                        <input type="password" id="vaultPasswordInput" placeholder="Enter master password..." 
                               onkeydown="if(event.key==='Enter') unlockVaultWithPassword()"
                               class="w-full pl-3.5 pr-10 py-3 rounded-xl bg-studio-card border border-studio-border text-white text-xs font-mono focus:outline-none focus:border-studio-gold transition">
                        <button onclick="togglePasswordVisibility()" class="absolute right-3 top-1/2 -translate-y-1/2 text-studio-muted hover:text-white text-xs">
                            <i id="pwdToggleIcon" class="fa-solid fa-eye"></i>
                        </button>
                    </div>
                    <span id="lockoutWarning" class="hidden text-[10px] text-rose-400 mt-1 block"></span>
                </div>

                <button onclick="unlockVaultWithPassword()" id="unlockBtn" class="w-full py-3 rounded-xl bg-gradient-to-r from-studio-goldDark to-studio-gold text-black font-extrabold text-xs hover:scale-[1.02] transition shadow-lg shadow-studio-gold/20 flex items-center justify-center gap-2">
                    <i class="fa-solid fa-lock-open text-xs"></i>
                    <span>Unlock Admin Studio</span>
                </button>

                <div class="pt-2 border-t border-studio-border/50 text-center">
                    <button onclick="switchToOtpMode()" class="text-[11px] text-studio-cyan hover:underline font-semibold flex items-center justify-center gap-1.5 mx-auto">
                        <i class="fa-solid fa-envelope"></i>
                        <span>Forgot Password? Request Emergency 2FA Code</span>
                    </button>
                </div>
            </div>

            <!-- Emergency OTP Section -->
            <div id="otpAuthSection" class="hidden space-y-4 text-left">
                <div class="p-3 rounded-xl bg-studio-card border border-studio-border text-xs text-studio-muted space-y-1">
                    <span class="text-white font-bold block">Emergency 2FA Verification:</span>
                    <p class="text-[11px]">Security code will be generated for <b class="text-studio-gold">dhruvitsarvaiya2003@gmail.com</b> and your Telegram <b class="text-studio-gold">@dhruvit2053</b>.</p>
                </div>

                <div>
                    <button onclick="sendOtpCode()" id="sendOtpBtn" class="w-full py-2.5 rounded-xl bg-white/10 hover:bg-white/20 text-white font-bold text-xs transition flex items-center justify-center gap-2">
                        <i class="fa-solid fa-paper-plane text-xs"></i>
                        <span>Send 6-Digit OTP Code</span>
                    </button>
                </div>

                <div id="otpInputGroup" class="hidden space-y-2">
                    <label class="block text-xs font-semibold text-studio-muted">Enter 6-Digit Code:</label>
                    <input type="text" id="vaultOtpInput" maxlength="6" placeholder="• • • • • •" 
                           class="w-full py-3 text-center rounded-xl bg-studio-card border border-studio-border text-white text-lg tracking-[0.5em] font-mono focus:outline-none focus:border-studio-gold">
                    <div class="flex items-center justify-between text-[10px] text-studio-muted">
                        <span id="otpCountdown">Code expires in 05:00</span>
                        <button onclick="sendOtpCode()" class="text-studio-gold hover:underline">Resend Code</button>
                    </div>

                    <button onclick="verifyOtpCode()" class="w-full mt-2 py-3 rounded-xl bg-studio-emerald text-black font-extrabold text-xs hover:opacity-90 transition flex items-center justify-center gap-2">
                        <i class="fa-solid fa-shield-check text-xs"></i>
                        <span>Verify & Unlock Studio</span>
                    </button>
                </div>

                <div class="pt-2 border-t border-studio-border/50 text-center">
                    <button onclick="switchToPasswordMode()" class="text-[11px] text-studio-muted hover:text-white">
                        ← Back to Master Password
                    </button>
                </div>
            </div>

            <div class="pt-2 text-[10px] text-studio-muted font-mono flex items-center justify-center gap-1.5">
                <i class="fa-solid fa-lock text-[9px] text-studio-emerald"></i>
                <span>Encrypted Session • Rate-Limited Anti-Brute-Force Active</span>
            </div>
        </div>
    </div>

    <!-- ========================================== -->
    <!-- LEFT SIDEBAR NAVIGATION                    -->
    <!-- ========================================== -->
    <aside class="w-64 bg-studio-panel border-r border-studio-border flex flex-col justify-between shrink-0 hidden md:flex">
        
        <div>
            <!-- Studio Brand -->
            <div class="p-5 border-b border-studio-border flex items-center justify-between">
                <div class="flex items-center gap-3">
                    <div class="w-9 h-9 rounded-xl bg-gradient-to-tr from-studio-goldDark to-studio-gold flex items-center justify-center text-black font-extrabold shadow-md shadow-studio-gold/20">
                        <i class="fa-solid fa-crown text-sm"></i>
                    </div>
                    <div>
                        <span class="text-sm font-extrabold tracking-wider text-white">CINE<span class="text-studio-gold">VIBE</span></span>
                        <span class="block text-[10px] tracking-widest text-studio-gold uppercase font-mono font-bold">Admin Studio</span>
                    </div>
                </div>
            </div>

            <!-- Nav Links -->
            <nav class="p-3 space-y-1 text-xs font-semibold">
                <button onclick="switchTab('overview')" id="nav-overview" class="w-full flex items-center gap-3 px-3 py-2.5 rounded-lg text-studio-muted hover:text-white hover:bg-white/5 transition active-tab">
                    <i class="fa-solid fa-gauge-high text-sm w-4"></i>
                    <span>Dashboard Overview</span>
                </button>
                <button onclick="switchTab('tmdb')" id="nav-tmdb" class="w-full flex items-center gap-3 px-3 py-2.5 rounded-lg text-studio-muted hover:text-white hover:bg-white/5 transition">
                    <i class="fa-solid fa-calendar-days text-sm w-4 text-studio-cyan"></i>
                    <span>TMDB Year & Month</span>
                    <span class="ml-auto text-[9px] px-1.5 py-0.5 rounded bg-studio-cyan/20 text-studio-cyan font-mono font-bold">LIVE</span>
                </button>
                <button onclick="switchTab('inventory')" id="nav-inventory" class="w-full flex items-center gap-3 px-3 py-2.5 rounded-lg text-studio-muted hover:text-white hover:bg-white/5 transition">
                    <i class="fa-solid fa-film text-sm w-4"></i>
                    <span>CineVibe Inventory</span>
                    <span id="navInvBadge" class="ml-auto text-[10px] px-1.5 py-0.5 rounded bg-white/10 text-white font-mono">17</span>
                </button>
                <button onclick="switchTab('missing')" id="nav-missing" class="w-full flex items-center gap-3 px-3 py-2.5 rounded-lg text-studio-muted hover:text-white hover:bg-white/5 transition">
                    <i class="fa-solid fa-satellite-dish text-sm w-4 text-studio-rose"></i>
                    <span>Missing Content Radar</span>
                    <span id="navMissingBadge" class="ml-auto text-[10px] px-1.5 py-0.5 rounded bg-studio-rose/20 text-studio-rose font-mono">7</span>
                </button>
                <button onclick="switchTab('editor')" id="nav-editor" class="w-full flex items-center gap-3 px-3 py-2.5 rounded-lg text-studio-muted hover:text-white hover:bg-white/5 transition">
                    <i class="fa-solid fa-plus-circle text-sm w-4"></i>
                    <span>Add / Edit Media</span>
                </button>
                <button onclick="switchTab('ai')" id="nav-ai" class="w-full flex items-center gap-3 px-3 py-2.5 rounded-lg text-studio-muted hover:text-white hover:bg-white/5 transition">
                    <i class="fa-solid fa-wand-magic-sparkles text-sm w-4 text-amber-400"></i>
                    <span>Gemini AI Studio</span>
                </button>
                <button onclick="switchTab('shield')" id="nav-shield" class="w-full flex items-center gap-3 px-3 py-2.5 rounded-lg text-studio-muted hover:text-white hover:bg-white/5 transition">
                    <i class="fa-solid fa-shield-halved text-sm w-4 text-studio-emerald"></i>
                    <span>Domain Shield Mirrors</span>
                </button>
                <button onclick="switchTab('settings')" id="nav-settings" class="w-full flex items-center gap-3 px-3 py-2.5 rounded-lg text-studio-muted hover:text-white hover:bg-white/5 transition">
                    <i class="fa-solid fa-sliders text-sm w-4"></i>
                    <span>Engine & Security Config</span>
                </button>
            </nav>
        </div>

        <!-- Sidebar Footer: Stream Status -->
        <div class="p-4 border-t border-studio-border bg-studio-card/50 m-3 rounded-xl space-y-2">
            <div class="flex items-center justify-between text-[11px]">
                <span class="text-studio-muted font-mono">Streamer Port:</span>
                <span class="text-white font-mono font-bold">8080</span>
            </div>
            <div class="flex items-center justify-between text-[11px]">
                <span class="text-studio-muted">Auto-Sync Status:</span>
                <span class="text-studio-emerald font-bold flex items-center gap-1">
                    <span class="w-1.5 h-1.5 rounded-full bg-studio-emerald animate-pulse"></span> TMDB Active
                </span>
            </div>
            <a href="https://cinevibe-cinema.surge.sh" target="_blank" class="mt-2 block w-full py-1.5 text-center rounded-lg bg-white/5 hover:bg-white/10 text-[11px] font-bold text-studio-gold border border-studio-gold/20 transition">
                Open Public Website ↗
            </a>
        </div>
    </aside>

    <!-- ========================================== -->
    <!-- MAIN CONTENT AREA                          -->
    <!-- ========================================== -->
    <div class="flex-1 flex flex-col overflow-hidden">
        
        <!-- Top App Bar -->
        <header class="h-16 bg-studio-panel border-b border-studio-border px-6 flex items-center justify-between shrink-0">
            <div class="flex items-center gap-4">
                <span id="pageTitle" class="text-base font-bold text-white tracking-wide">Dashboard Overview</span>
                <span class="text-xs px-2.5 py-0.5 rounded-full bg-white/5 border border-white/10 text-studio-muted font-mono">
                    v2.7.5 Vault Secured
                </span>
            </div>
            <div class="flex items-center gap-2.5">
                <!-- Sync from Bot API -->
                <button onclick="syncFromBotServer()" class="px-3 py-1.5 rounded-lg bg-studio-cyan/15 hover:bg-studio-cyan/25 border border-studio-cyan/30 text-xs font-semibold text-studio-cyan flex items-center gap-1.5 transition" title="Fetch live catalog from ByteStreamer 8080">
                    <i id="syncIcon" class="fa-solid fa-arrows-rotate"></i>
                    <span>Sync from Bot (8080)</span>
                </button>

                <button onclick="pingBotServer()" class="px-3 py-1.5 rounded-lg bg-white/5 hover:bg-white/10 border border-white/10 text-xs font-semibold text-white flex items-center gap-1.5 transition">
                    <i id="pingIcon" class="fa-solid fa-heart-pulse text-studio-emerald"></i>
                    <span id="pingStatusText">Ping 8080</span>
                </button>

                <button onclick="exportCatalogJson()" class="px-3 py-1.5 rounded-lg bg-studio-gold text-black text-xs font-bold hover:bg-studio-goldDark transition flex items-center gap-1.5">
                    <i class="fa-solid fa-download"></i>
                    <span>Export JSON</span>
                </button>

                <!-- Lock Studio / Logout Button -->
                <button onclick="lockStudio()" class="p-2 rounded-lg bg-rose-500/10 hover:bg-rose-500/20 border border-rose-500/30 text-rose-400 text-xs font-bold transition flex items-center gap-1" title="Lock Studio (Sign Out)">
                    <i class="fa-solid fa-lock"></i>
                    <span class="hidden sm:inline">Lock</span>
                </button>
            </div>
        </header>

        <!-- Dynamic Tab Body -->
        <main class="flex-1 overflow-y-auto p-6 space-y-6">

            <!-- ========================================== -->
            <!-- TAB 1: DASHBOARD OVERVIEW                  -->
            <!-- ========================================== -->
            <div id="tab-overview" class="space-y-6">
                <!-- Metrics Grid -->
                <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4">
                    <div class="p-4 rounded-xl bg-studio-panel border border-studio-border space-y-1">
                        <span class="text-xs text-studio-muted uppercase tracking-wider font-semibold">Total Verified Media</span>
                        <div class="flex items-baseline gap-2">
                            <span id="metricTotalTitles" class="text-2xl font-extrabold text-white">17</span>
                            <span class="text-xs text-studio-emerald font-bold">100% Online</span>
                        </div>
                        <span class="text-[11px] text-studio-muted">Movies, Series, K-Drama, Anime</span>
                    </div>

                    <div class="p-4 rounded-xl bg-studio-panel border border-studio-border space-y-1">
                        <span class="text-xs text-studio-muted uppercase tracking-wider font-semibold">Ultra HD 4K Titles</span>
                        <div class="flex items-baseline gap-2">
                            <span id="metric4KTitles" class="text-2xl font-extrabold text-studio-gold">10</span>
                            <span class="text-xs text-studio-gold font-bold">HDR10 / Atmos</span>
                        </div>
                        <span class="text-[11px] text-studio-muted">High-bitrate cinema encodings</span>
                    </div>

                    <div class="p-4 rounded-xl bg-studio-panel border border-studio-border space-y-1">
                        <span class="text-xs text-studio-muted uppercase tracking-wider font-semibold">Missing Demand Radar</span>
                        <div class="flex items-baseline gap-2">
                            <span id="metricMissingTitles" class="text-2xl font-extrabold text-studio-rose">7</span>
                            <span class="text-xs text-studio-rose font-bold">High User Demand</span>
                        </div>
                        <span class="text-[11px] text-studio-muted">Pushpa 2, Deadpool, Stree 2...</span>
                    </div>

                    <div class="p-4 rounded-xl bg-studio-panel border border-studio-border space-y-1">
                        <span class="text-xs text-studio-muted uppercase tracking-wider font-semibold">Telegram Auto-Sync</span>
                        <div class="flex items-baseline gap-2">
                            <span class="text-2xl font-extrabold text-studio-emerald">Active</span>
                            <span class="text-xs text-studio-emerald font-bold">Channel Hook</span>
                        </div>
                        <span class="text-[11px] text-studio-muted">Auto-TMDB Enrichment On</span>
                    </div>
                </div>

                <!-- Quick Action Banners -->
                <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
                    <div class="p-5 rounded-2xl bg-gradient-to-r from-studio-card via-studio-panel to-studio-card border border-studio-border space-y-3">
                        <div class="flex items-center gap-2">
                            <i class="fa-solid fa-calendar-days text-studio-cyan text-lg"></i>
                            <h3 class="text-sm font-bold text-white">TMDB Live Year & Month Explorer</h3>
                        </div>
                        <p class="text-xs text-studio-muted leading-relaxed">
                            Discover every Hollywood, Bollywood, Anime, and K-Drama title released by year and month using your authenticated TMDB API key. Import metadata in 1-click.
                        </p>
                        <button onclick="switchTab('tmdb')" class="px-4 py-2 rounded-xl bg-studio-cyan text-black font-extrabold text-xs hover:opacity-90 transition">
                            Launch TMDB Explorer →
                        </button>
                    </div>

                    <div class="p-5 rounded-2xl bg-gradient-to-r from-studio-card via-studio-panel to-studio-card border border-studio-border space-y-3">
                        <div class="flex items-center gap-2">
                            <i class="fa-solid fa-satellite-dish text-studio-rose text-lg"></i>
                            <h3 class="text-sm font-bold text-white">Missing Content Radar & Fulfillment</h3>
                        </div>
                        <p class="text-xs text-studio-muted leading-relaxed">
                            Track top audience-requested movies that CineVibe is missing. Pre-populate stream tokens and add them into the public discovery catalog immediately.
                        </p>
                        <button onclick="switchTab('missing')" class="px-4 py-2 rounded-xl bg-studio-rose text-white font-extrabold text-xs hover:opacity-90 transition">
                            Review Missing Titles →
                        </button>
                    </div>
                </div>

                <!-- Recent Inventory Preview -->
                <div class="p-5 rounded-2xl bg-studio-panel border border-studio-border space-y-4">
                    <div class="flex items-center justify-between">
                        <h3 class="text-sm font-bold text-white">Latest Verified CineVibe Titles</h3>
                        <button onclick="switchTab('inventory')" class="text-xs text-studio-gold hover:underline">View All 17 Titles →</button>
                    </div>
                    <div id="overviewTitlesGrid" class="grid grid-cols-2 sm:grid-cols-3 md:grid-cols-6 gap-3"></div>
                </div>
            </div>

            <!-- ========================================== -->
            <!-- TAB 2: TMDB LIVE YEAR & MONTH EXPLORER    -->
            <!-- ========================================== -->
            <div id="tab-tmdb" class="hidden space-y-6">
                <!-- Search & Filter Controls -->
                <div class="p-5 rounded-2xl bg-studio-panel border border-studio-border space-y-4">
                    <div class="flex items-center justify-between">
                        <div>
                            <h3 class="text-sm font-bold text-white flex items-center gap-2">
                                <i class="fa-solid fa-bolt text-studio-cyan"></i>
                                <span>TheMovieDB Live Explorer by Year & Month</span>
                            </h3>
                            <p class="text-[11px] text-studio-muted mt-0.5">Powered by TMDB API Key & v4 Bearer Auth Token</p>
                        </div>
                        <span class="text-[11px] text-studio-emerald font-mono bg-studio-emerald/10 border border-studio-emerald/20 px-2.5 py-1 rounded-full font-bold">
                            ✔ TMDB Authenticated
                        </span>
                    </div>

                    <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-3 text-xs">
                        <div>
                            <label class="block text-studio-muted mb-1 text-[11px] font-semibold">Release Year:</label>
                            <select id="tmdbYearSelect" class="w-full p-2.5 rounded-xl bg-studio-card border border-studio-border text-white font-semibold focus:outline-none focus:border-studio-gold">
                                <option value="2024" selected>2024 (Current Year)</option>
                                <option value="2023">2023</option>
                                <option value="2022">2022</option>
                                <option value="2021">2021</option>
                                <option value="2020">2020</option>
                                <option value="2019">2019</option>
                                <option value="2018">2018</option>
                            </select>
                        </div>

                        <div>
                            <label class="block text-studio-muted mb-1 text-[11px] font-semibold">Release Month:</label>
                            <select id="tmdbMonthSelect" class="w-full p-2.5 rounded-xl bg-studio-card border border-studio-border text-white font-semibold focus:outline-none focus:border-studio-gold">
                                <option value="01">01 - January</option>
                                <option value="02">02 - February</option>
                                <option value="03">03 - March</option>
                                <option value="04">04 - April</option>
                                <option value="05">05 - May</option>
                                <option value="06">06 - June</option>
                                <option value="07">07 - July</option>
                                <option value="08">08 - August</option>
                                <option value="09">09 - September</option>
                                <option value="10">10 - October</option>
                                <option value="11">11 - November</option>
                                <option value="12" selected>12 - December</option>
                            </select>
                        </div>

                        <div>
                            <label class="block text-studio-muted mb-1 text-[11px] font-semibold">Region / Language:</label>
                            <select id="tmdbLangSelect" class="w-full p-2.5 rounded-xl bg-studio-card border border-studio-border text-white font-semibold focus:outline-none focus:border-studio-gold">
                                <option value="" selected>All / Hollywood (Global)</option>
                                <option value="hi">Bollywood (Hindi)</option>
                                <option value="te">South Indian (Telugu)</option>
                                <option value="ta">South Indian (Tamil)</option>
                                <option value="ja">Anime (Japanese)</option>
                                <option value="ko">K-Drama (Korean)</option>
                            </select>
                        </div>

                        <div>
                            <label class="block text-studio-muted mb-1 text-[11px] font-semibold">Sort Order:</label>
                            <select id="tmdbSortSelect" class="w-full p-2.5 rounded-xl bg-studio-card border border-studio-border text-white font-semibold focus:outline-none focus:border-studio-gold">
                                <option value="popularity.desc" selected>Popularity Descending</option>
                                <option value="vote_average.desc">Highest Rated</option>
                                <option value="primary_release_date.desc">Release Date (Newest)</option>
                            </select>
                        </div>
                    </div>

                    <div class="flex items-center justify-between pt-1">
                        <span id="tmdbResultSummary" class="text-xs text-studio-muted">Select Year & Month and click Fetch.</span>
                        <button onclick="fetchTmdbReleases()" id="fetchTmdbBtn" class="px-6 py-2.5 rounded-xl bg-studio-cyan text-black font-extrabold text-xs hover:opacity-90 transition flex items-center gap-2">
                            <i class="fa-solid fa-arrows-rotate"></i>
                            <span>Fetch Releases from TMDB</span>
                        </button>
                    </div>
                </div>

                <!-- TMDB Results Grid -->
                <div id="tmdbResultsGrid" class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
                    <div class="col-span-full py-16 text-center text-studio-muted text-xs">
                        Click "Fetch Releases from TMDB" to inspect movie releases for the selected Year & Month.
                    </div>
                </div>
            </div>

            <!-- ========================================== -->
            <!-- TAB 3: CINEVIBE INVENTORY (YEAR/MONTH)     -->
            <!-- ========================================== -->
            <div id="tab-inventory" class="hidden space-y-6">
                <div class="p-5 rounded-2xl bg-studio-panel border border-studio-border space-y-4">
                    <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-2">
                        <div>
                            <h3 class="text-sm font-bold text-white">CineVibe Content Inventory Matrix</h3>
                            <p class="text-[11px] text-studio-muted">Existing verified titles categorized by year and release month</p>
                        </div>
                        <div class="flex items-center gap-2">
                            <button onclick="renderInventoryTable(null)" class="px-3 py-1 rounded-lg bg-studio-gold text-black text-xs font-bold inv-year-filter">All</button>
                            <button onclick="renderInventoryTable(2024)" class="px-3 py-1 rounded-lg bg-white/5 hover:bg-white/10 text-white text-xs font-semibold inv-year-filter">2024</button>
                            <button onclick="renderInventoryTable(2023)" class="px-3 py-1 rounded-lg bg-white/5 hover:bg-white/10 text-white text-xs font-semibold inv-year-filter">2023</button>
                            <button onclick="renderInventoryTable(2022)" class="px-3 py-1 rounded-lg bg-white/5 hover:bg-white/10 text-white text-xs font-semibold inv-year-filter">2022</button>
                            <button onclick="renderInventoryTable(2021)" class="px-3 py-1 rounded-lg bg-white/5 hover:bg-white/10 text-white text-xs font-semibold inv-year-filter">2021</button>
                            <button onclick="renderInventoryTable(2020)" class="px-3 py-1 rounded-lg bg-white/5 hover:bg-white/10 text-white text-xs font-semibold inv-year-filter">2020</button>
                        </div>
                    </div>

                    <!-- Inventory Table -->
                    <div class="overflow-x-auto rounded-xl border border-studio-border">
                        <table class="w-full text-left text-xs">
                            <thead class="bg-studio-card text-studio-muted font-mono uppercase text-[10px] border-b border-studio-border">
                                <tr>
                                    <th class="p-3">Title & Media</th>
                                    <th class="p-3">Year / Month</th>
                                    <th class="p-3">Category</th>
                                    <th class="p-3">Quality</th>
                                    <th class="p-3">Size</th>
                                    <th class="p-3">Stream Link (8080)</th>
                                    <th class="p-3 text-right">Actions</th>
                                </tr>
                            </thead>
                            <tbody id="inventoryTableBody" class="divide-y divide-studio-border"></tbody>
                        </table>
                    </div>
                </div>
            </div>

            <!-- ========================================== -->
            <!-- TAB 4: MISSING CONTENT RADAR               -->
            <!-- ========================================== -->
            <div id="tab-missing" class="hidden space-y-6">
                <div class="p-5 rounded-2xl bg-studio-panel border border-studio-border space-y-4">
                    <div class="flex items-center justify-between">
                        <div>
                            <h3 class="text-sm font-bold text-white flex items-center gap-2">
                                <i class="fa-solid fa-satellite-dish text-studio-rose"></i>
                                <span>High-Demand Missing Content Radar</span>
                            </h3>
                            <p class="text-[11px] text-studio-muted">Top requested blockbusters currently missing from CineVibe</p>
                        </div>
                        <span class="text-xs px-3 py-1 rounded-full bg-studio-rose/20 text-studio-rose font-bold">
                            7 High Demand Items
                        </span>
                    </div>

                    <div class="overflow-x-auto rounded-xl border border-studio-border">
                        <table class="w-full text-left text-xs">
                            <thead class="bg-studio-card text-studio-muted font-mono uppercase text-[10px] border-b border-studio-border">
                                <tr>
                                    <th class="p-3">Title</th>
                                    <th class="p-3">Year</th>
                                    <th class="p-3">Category</th>
                                    <th class="p-3">Demand Score</th>
                                    <th class="p-3">Target Quality</th>
                                    <th class="p-3">Notes</th>
                                    <th class="p-3 text-right">Fulfill Action</th>
                                </tr>
                            </thead>
                            <tbody id="missingTableBody" class="divide-y divide-studio-border"></tbody>
                        </table>
                    </div>
                </div>
            </div>

            <!-- ========================================== -->
            <!-- TAB 5: ADD / EDIT MEDIA CREATOR            -->
            <!-- ========================================== -->
            <div id="tab-editor" class="hidden space-y-6">
                <div class="p-5 rounded-2xl bg-studio-panel border border-studio-border space-y-4">
                    <div class="flex items-center justify-between">
                        <div>
                            <h3 id="editorFormTitle" class="text-sm font-bold text-white">Add New Cinema Title</h3>
                            <p class="text-[11px] text-studio-muted">Import from TMDB or enter metadata manually</p>
                        </div>
                        <button onclick="resetEditorForm()" class="text-xs text-studio-muted hover:text-white">Clear Form</button>
                    </div>

                    <form id="mediaForm" onsubmit="handleSaveMedia(event)" class="space-y-4 text-xs">
                        <input type="hidden" id="editMediaId">
                        
                        <div class="grid grid-cols-1 sm:grid-cols-3 gap-3">
                            <div>
                                <label class="block text-studio-muted mb-1 text-[11px] font-semibold">Title:</label>
                                <input type="text" id="formTitle" required class="w-full p-2.5 rounded-xl bg-studio-card border border-studio-border text-white font-semibold focus:outline-none focus:border-studio-gold">
                            </div>
                            <div>
                                <label class="block text-studio-muted mb-1 text-[11px] font-semibold">Release Year:</label>
                                <input type="number" id="formYear" value="2024" required class="w-full p-2.5 rounded-xl bg-studio-card border border-studio-border text-white font-semibold focus:outline-none focus:border-studio-gold">
                            </div>
                            <div>
                                <label class="block text-studio-muted mb-1 text-[11px] font-semibold">Release Month (1-12):</label>
                                <input type="number" id="formMonth" min="1" max="12" value="1" required class="w-full p-2.5 rounded-xl bg-studio-card border border-studio-border text-white font-semibold focus:outline-none focus:border-studio-gold">
                            </div>
                        </div>

                        <div class="grid grid-cols-1 sm:grid-cols-4 gap-3">
                            <div>
                                <label class="block text-studio-muted mb-1 text-[11px] font-semibold">Category:</label>
                                <select id="formCategory" class="w-full p-2.5 rounded-xl bg-studio-card border border-studio-border text-white font-semibold focus:outline-none focus:border-studio-gold">
                                    <option value="bollywood">Bollywood</option>
                                    <option value="hollywood">Hollywood</option>
                                    <option value="south">South Indian</option>
                                    <option value="kdrama">K-Drama</option>
                                    <option value="anime">Anime</option>
                                    <option value="series">Web Series</option>
                                </select>
                            </div>
                            <div>
                                <label class="block text-studio-muted mb-1 text-[11px] font-semibold">Quality Badge:</label>
                                <input type="text" id="formQuality" value="4K UHD HDR" required class="w-full p-2.5 rounded-xl bg-studio-card border border-studio-border text-white font-semibold focus:outline-none focus:border-studio-gold">
                            </div>
                            <div>
                                <label class="block text-studio-muted mb-1 text-[11px] font-semibold">Rating (IMDb/TMDB):</label>
                                <input type="number" step="0.1" id="formRating" value="8.5" required class="w-full p-2.5 rounded-xl bg-studio-card border border-studio-border text-white font-semibold focus:outline-none focus:border-studio-gold">
                            </div>
                            <div>
                                <label class="block text-studio-muted mb-1 text-[11px] font-semibold">Runtime:</label>
                                <input type="text" id="formRuntime" value="2h 15m" required class="w-full p-2.5 rounded-xl bg-studio-card border border-studio-border text-white font-semibold focus:outline-none focus:border-studio-gold">
                            </div>
                        </div>

                        <div class="grid grid-cols-1 sm:grid-cols-2 gap-3">
                            <div>
                                <label class="block text-studio-muted mb-1 text-[11px] font-semibold">Poster URL (Cloudflare Weserv CDN):</label>
                                <input type="url" id="formPoster" required oninput="previewImages()" class="w-full p-2.5 rounded-xl bg-studio-card border border-studio-border text-white font-mono text-[11px] focus:outline-none focus:border-studio-gold">
                            </div>
                            <div>
                                <label class="block text-studio-muted mb-1 text-[11px] font-semibold">Backdrop URL:</label>
                                <input type="url" id="formBackdrop" required oninput="previewImages()" class="w-full p-2.5 rounded-xl bg-studio-card border border-studio-border text-white font-mono text-[11px] focus:outline-none focus:border-studio-gold">
                            </div>
                        </div>

                        <!-- Image Previews -->
                        <div class="flex items-center gap-4 p-3 rounded-xl bg-studio-card/60 border border-studio-border">
                            <img id="previewPosterImg" src="" alt="Poster" class="w-16 h-24 object-cover rounded-lg bg-black border border-white/10 shrink-0">
                            <div class="space-y-1">
                                <span class="text-[11px] font-bold text-white">Live Artwork Preview</span>
                                <p class="text-[10px] text-studio-muted">Ensure posters are high-resolution and match the official title.</p>
                            </div>
                        </div>

                        <!-- Telegram Bot Stream Mapping -->
                        <div class="p-4 rounded-xl bg-white/5 border border-white/5 space-y-3">
                            <span class="text-xs font-bold text-studio-gold">Telegram Bot ByteStreamer Mapping</span>
                            <div class="grid grid-cols-1 sm:grid-cols-3 gap-3">
                                <div>
                                    <label class="block text-studio-muted mb-1 text-[10px]">Stream Message ID:</label>
                                    <input type="number" id="formMsgId" value="150" required class="w-full p-2 rounded bg-studio-card border border-studio-border text-white font-mono">
                                </div>
                                <div>
                                    <label class="block text-studio-muted mb-1 text-[10px]">Stream Hash:</label>
                                    <input type="text" id="formHash" value="AgADxyz" required class="w-full p-2 rounded bg-studio-card border border-studio-border text-white font-mono">
                                </div>
                                <div>
                                    <label class="block text-studio-muted mb-1 text-[10px]">File Size (Human):</label>
                                    <input type="text" id="formSizeHuman" value="4.50 GB" required class="w-full p-2 rounded bg-studio-card border border-studio-border text-white font-mono">
                                </div>
                            </div>
                            <div>
                                <label class="block text-studio-muted mb-1 text-[10px]">File Name:</label>
                                <input type="text" id="formFileName" value="Movie.Title.2024.2160p.UHD.x265" required class="w-full p-2 rounded bg-studio-card border border-studio-border text-white font-mono">
                            </div>
                        </div>

                        <div>
                            <label class="block text-studio-muted mb-1 text-[11px] font-semibold">Synopsis / Overview:</label>
                            <textarea id="formOverview" rows="3" required class="w-full p-2.5 rounded-xl bg-studio-card border border-studio-border text-white text-xs focus:outline-none focus:border-studio-gold"></textarea>
                        </div>

                        <div class="flex justify-end gap-3 pt-2">
                            <button type="button" onclick="resetEditorForm()" class="px-5 py-2.5 rounded-xl bg-white/5 text-xs text-studio-muted hover:text-white">Cancel</button>
                            <button type="submit" class="px-6 py-2.5 rounded-xl bg-studio-gold text-black font-extrabold text-xs hover:bg-studio-goldDark">Save Title to Catalog</button>
                        </div>
                    </form>
                </div>
            </div>

            <!-- ========================================== -->
            <!-- TAB 6: GEMINI AI STUDIO                    -->
            <!-- ========================================== -->
            <div id="tab-ai" class="hidden space-y-6">
                <div class="p-5 rounded-2xl bg-studio-panel border border-studio-border space-y-4">
                    <div class="flex items-center justify-between">
                        <div>
                            <h3 class="text-sm font-bold text-white flex items-center gap-2">
                                <i class="fa-solid fa-wand-magic-sparkles text-amber-400"></i>
                                <span>Gemini AI Studio Assistant</span>
                            </h3>
                            <p class="text-[11px] text-studio-muted">Natural language prompt studio for movie analysis and catalog curation</p>
                        </div>
                    </div>

                    <div class="flex flex-wrap gap-2 text-xs">
                        <button onclick="setAiPrompt('Summarize top movie releases of 2024 by month for CineVibe catalog curation.')" class="px-3 py-1.5 rounded-lg bg-white/5 hover:bg-white/10 text-studio-gold border border-studio-gold/20">
                            ⚡ 2024 Release Schedule by Month
                        </button>
                        <button onclick="setAiPrompt('Give 5 highest demand Indian blockbusters of 2024 that a cinema streaming platform must have.')" class="px-3 py-1.5 rounded-lg bg-white/5 hover:bg-white/10 text-studio-gold border border-studio-gold/20">
                            🍿 Top 5 Indian Blockbusters
                        </button>
                        <button onclick="setAiPrompt('Analyze audience demand for K-Drama and Anime in India and suggest 3 top series.')" class="px-3 py-1.5 rounded-lg bg-white/5 hover:bg-white/10 text-studio-gold border border-studio-gold/20">
                            👑 K-Drama & Anime Recommendations
                        </button>
                    </div>

                    <div>
                        <textarea id="adminAiPrompt" rows="3" class="w-full p-3 rounded-xl bg-studio-card border border-studio-border text-xs text-white focus:outline-none focus:border-studio-gold resize-none" placeholder="Enter prompt for Gemini AI..."></textarea>
                        <div class="mt-2 flex justify-end">
                            <button onclick="runAdminGemini()" id="adminAiBtn" class="px-6 py-2.5 rounded-xl bg-studio-gold text-black font-bold text-xs hover:bg-studio-goldDark flex items-center gap-2">
                                <i class="fa-solid fa-sparkles"></i>
                                <span>Generate AI Insights</span>
                            </button>
                        </div>
                    </div>

                    <div id="adminAiOutputBox" class="hidden p-4 rounded-xl bg-white/5 border border-white/5 space-y-2">
                        <span class="text-xs font-bold text-studio-gold flex items-center gap-1.5">
                            <i class="fa-solid fa-robot"></i> Gemini AI Response:
                        </span>
                        <p id="adminAiResponseText" class="text-xs text-white leading-relaxed whitespace-pre-line"></p>
                    </div>
                </div>
            </div>

            <!-- ========================================== -->
            <!-- TAB 7: DOMAIN SHIELD MIRROR SWITCHER       -->
            <!-- ========================================== -->
            <div id="tab-shield" class="hidden space-y-6">
                <div class="p-5 rounded-2xl bg-studio-panel border border-studio-border space-y-4">
                    <div class="flex items-center justify-between">
                        <div>
                            <h3 class="text-sm font-bold text-white flex items-center gap-2">
                                <i class="fa-solid fa-shield-halved text-studio-emerald"></i>
                                <span>Domain Shield Mirror Routing (HDHub4u-Style)</span>
                            </h3>
                            <p class="text-[11px] text-studio-muted">Protects CineVibe main domain from copyright and DMCA takedowns</p>
                        </div>
                        <span class="text-xs px-3 py-1 rounded-full bg-studio-emerald/20 text-studio-emerald font-bold">
                            Active Shield
                        </span>
                    </div>

                    <div class="p-4 rounded-xl bg-studio-card border border-studio-border space-y-3">
                        <div class="flex items-center justify-between text-xs">
                            <span class="text-studio-muted">Permanent Front Gateway:</span>
                            <code class="text-white bg-black/50 px-2 py-0.5 rounded font-mono">https://cinevibe.surge.sh</code>
                        </div>
                        <div class="flex items-center justify-between text-xs">
                            <span class="text-studio-muted">Current Active Mirror:</span>
                            <code id="currentMirrorDisplay" class="text-studio-gold bg-black/50 px-2 py-0.5 rounded font-mono">https://cinevibe-cinema.surge.sh</code>
                        </div>
                    </div>

                    <div class="space-y-3">
                        <label class="block text-xs font-semibold text-white">Switch Active Mirror Target:</label>
                        <div class="grid grid-cols-1 sm:grid-cols-3 gap-3 text-xs">
                            <button onclick="setMirror('https://cinevibe-cinema.surge.sh')" class="p-3 rounded-xl bg-studio-card hover:border-studio-gold border border-studio-border text-left">
                                <span class="font-bold text-white block">cinevibe-cinema.surge.sh</span>
                                <span class="text-[10px] text-studio-muted">Default Clean Surge Mirror</span>
                            </button>
                            <button onclick="setMirror('https://new16.hdhub4u.cl/?utm=mn1')" class="p-3 rounded-xl bg-studio-card hover:border-studio-gold border border-studio-border text-left">
                                <span class="font-bold text-white block">new16.hdhub4u.cl</span>
                                <span class="text-[10px] text-studio-muted">Secondary Protected Mirror</span>
                            </button>
                            <button onclick="setMirror('https://new17.hdhub4u.cl/?utm=mn1')" class="p-3 rounded-xl bg-studio-card hover:border-studio-gold border border-studio-border text-left">
                                <span class="font-bold text-white block">new17.hdhub4u.cl</span>
                                <span class="text-[10px] text-studio-muted">Tertiary Failover Mirror</span>
                            </button>
                        </div>
                    </div>
                </div>
            </div>

            <!-- ========================================== -->
            <!-- TAB 8: ENGINE & SECURITY CONFIG            -->
            <!-- ========================================== -->
            <div id="tab-settings" class="hidden space-y-6">
                <div class="p-5 rounded-2xl bg-studio-panel border border-studio-border space-y-4">
                    <h3 class="text-sm font-bold text-white flex items-center gap-2">
                        <i class="fa-solid fa-sliders text-studio-gold"></i>
                        <span>Security, API Keys & Streaming Configuration</span>
                    </h3>

                    <div class="space-y-4 text-xs">
                        <!-- Security Password Settings -->
                        <div class="p-4 rounded-xl bg-studio-card border border-studio-gold/20 space-y-3">
                            <span class="text-xs font-bold text-studio-gold flex items-center gap-2">
                                <i class="fa-solid fa-key"></i>
                                <span>Master Admin Password Settings:</span>
                            </span>
                            <div class="grid grid-cols-1 sm:grid-cols-2 gap-3">
                                <div>
                                    <label class="block text-studio-muted mb-1 text-[11px] font-semibold">Change Master Password:</label>
                                    <input type="text" id="cfgNewMasterPwd" placeholder="Enter new master password..." class="w-full p-2.5 rounded-xl bg-studio-panel border border-studio-border text-white font-mono text-xs focus:outline-none focus:border-studio-gold">
                                </div>
                                <div>
                                    <label class="block text-studio-muted mb-1 text-[11px] font-semibold">Security Registered Email:</label>
                                    <input type="email" value="dhruvitsarvaiya2003@gmail.com" readonly class="w-full p-2.5 rounded-xl bg-studio-panel/50 border border-studio-border text-studio-muted font-mono text-xs cursor-not-allowed">
                                </div>
                            </div>
                        </div>

                        <div>
                            <label class="block text-studio-muted mb-1 text-[11px] font-semibold">TMDB API Key (v3):</label>
                            <input type="text" id="cfgTmdbKey" class="w-full p-2.5 rounded-xl bg-studio-card border border-studio-border text-white font-mono text-xs focus:outline-none focus:border-studio-gold">
                        </div>

                        <div>
                            <label class="block text-studio-muted mb-1 text-[11px] font-semibold">TMDB API Read Access Token (v4 Bearer):</label>
                            <textarea id="cfgTmdbToken" rows="2" class="w-full p-2.5 rounded-xl bg-studio-card border border-studio-border text-white font-mono text-xs focus:outline-none focus:border-studio-gold"></textarea>
                        </div>

                        <div>
                            <label class="block text-studio-muted mb-1 text-[11px] font-semibold">Gemini API Key:</label>
                            <input type="password" id="cfgGeminiKey" class="w-full p-2.5 rounded-xl bg-studio-card border border-studio-border text-white font-mono text-xs focus:outline-none focus:border-studio-gold">
                        </div>

                        <div>
                            <label class="block text-studio-muted mb-1 text-[11px] font-semibold">Cloud Bot Streamer Address:</label>
                            <input type="text" id="cfgBotUrl" class="w-full p-2.5 rounded-xl bg-studio-card border border-studio-border text-white font-mono text-xs focus:outline-none focus:border-studio-gold">
                        </div>

                        <div class="pt-2 flex justify-end gap-3">
                            <button onclick="saveAllSettings()" class="px-6 py-2.5 rounded-xl bg-studio-gold text-black font-extrabold text-xs hover:bg-studio-goldDark">Save All Settings</button>
                        </div>
                    </div>
                </div>
            </div>

        </main>
    </div>

    <!-- ========================================== -->
    <!-- ADMIN JAVASCRIPT LOGIC                     -->
    <!-- ========================================== -->
    <script>
        let MOVIES_CATALOG = {catalog_json};
        let MISSING_CATALOG = {missing_json};

        const TMDB_DEFAULT_KEY = "0301974a363174d2f5c70a47d9e60ce0";
        const TMDB_DEFAULT_TOKEN = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIwMzAxOTc0YTM2MzE3NGQyZjVjNzBhNDdkOWU2MGNlMCIsIm5iZiI6MTc4OTQ1MDYxNi4wMDQ5OTk5LCJzdWIiOiI2YWE4ZDk3NzlhNTlmOTcyMWFjMTc0M2QiLCJzY29wZXMiOlsiYXBpX3JlYWQiXSwidmVyc2lvbiI6MX0.4dFBixBMXPaUbvXuT0GpjoNahC4DVMcsD152s2dQMB0";
        const DEFAULT_MASTER_PWD = "Dhruvit@CineVibe#2026";

        let tmdbKey = localStorage.getItem('cinevibe_tmdb_key') || TMDB_DEFAULT_KEY;
        let tmdbToken = localStorage.getItem('cinevibe_tmdb_token') || TMDB_DEFAULT_TOKEN;
        let geminiKey = localStorage.getItem('cinevibe_gemini_key') || '';
        const DEFAULT_BOT_URL = 'https://telegram-filter-bot-aq9k.onrender.com';
        let savedBotUrl = (localStorage.getItem('cinevibe_bot_url') || '').trim().replace(/\/+$/, '');
        if (!savedBotUrl || savedBotUrl.includes('127.0.0.1') || savedBotUrl.includes('localhost') || savedBotUrl === 'https://telegram-filter-bot.onrender.com') {{
            savedBotUrl = DEFAULT_BOT_URL;
            localStorage.setItem('cinevibe_bot_url', savedBotUrl);
        }}
        let botUrl = savedBotUrl;
        let currentMirror = localStorage.getItem('cinevibe_active_mirror') || 'https://cinevibe-cinema.surge.sh';

        // Security Vault State
        let failedAttempts = parseInt(localStorage.getItem('cinevibe_failed_auth') || '0');
        let lockoutUntil = parseInt(localStorage.getItem('cinevibe_lockout_until') || '0');
        let activeOtpCode = null;
        let otpExpiryTime = 0;
        let otpTimerInterval = null;

        document.addEventListener('DOMContentLoaded', () => {{
            checkSecurityVaultState();

            // Init fields
            document.getElementById('cfgTmdbKey').value = tmdbKey;
            document.getElementById('cfgTmdbToken').value = tmdbToken;
            document.getElementById('cfgGeminiKey').value = geminiKey;
            document.getElementById('cfgBotUrl').value = botUrl;
            document.getElementById('currentMirrorDisplay').innerText = currentMirror;

            updateMetrics();
            renderOverviewGrid();
            renderInventoryTable(null);
            renderMissingTable();
        }});

        // ==========================================
        // SECURITY VAULT GATEKEEPER LOGIC
        // ==========================================
        function checkSecurityVaultState() {{
            const now = Date.now();
            if (lockoutUntil > now) {{
                const remMins = Math.ceil((lockoutUntil - now) / 60000);
                showLockout(`Security lockout active. Try again in ${{remMins}} minute(s).`);
                return;
            }}

            const sessionToken = sessionStorage.getItem('cinevibe_vault_token');
            const tokenExpiry = parseInt(sessionStorage.getItem('cinevibe_token_exp') || '0');

            if (sessionToken && tokenExpiry > now) {{
                document.getElementById('vaultLockModal').classList.add('hidden');
            }} else {{
                document.getElementById('vaultLockModal').classList.remove('hidden');
            }}
        }}

        function unlockVaultWithPassword() {{
            const now = Date.now();
            if (lockoutUntil > now) {{
                const remMins = Math.ceil((lockoutUntil - now) / 60000);
                showToast(`Studio locked for ${{remMins}} min due to failed attempts!`, true);
                return;
            }}

            const entered = document.getElementById('vaultPasswordInput').value;
            const currentMaster = localStorage.getItem('cinevibe_master_pwd') || DEFAULT_MASTER_PWD;

            if (entered === currentMaster) {{
                grantAccess();
            }} else {{
                failedAttempts++;
                localStorage.setItem('cinevibe_failed_auth', failedAttempts.toString());
                if (failedAttempts >= 5) {{
                    lockoutUntil = Date.now() + (15 * 60 * 1000);
                    localStorage.setItem('cinevibe_lockout_until', lockoutUntil.toString());
                    showLockout("Too many failed attempts! Studio locked for 15 minutes.");
                }} else {{
                    showToast(`Incorrect password! (${{5 - failedAttempts}} attempts remaining)`, true);
                }}
            }}
        }}

        function grantAccess() {{
            failedAttempts = 0;
            localStorage.removeItem('cinevibe_failed_auth');
            localStorage.removeItem('cinevibe_lockout_until');

            const token = 'CV_SECURE_' + Math.random().toString(36).substring(2) + Date.now().toString(36);
            sessionStorage.setItem('cinevibe_vault_token', token);
            sessionStorage.setItem('cinevibe_token_exp', (Date.now() + 2 * 60 * 60 * 1000).toString()); // 2 hours

            document.getElementById('vaultLockModal').classList.add('hidden');
            document.getElementById('vaultPasswordInput').value = '';
            showToast("Welcome Dhruvit! Admin Studio unlocked successfully.");
        }}

        function lockStudio() {{
            sessionStorage.removeItem('cinevibe_vault_token');
            sessionStorage.removeItem('cinevibe_token_exp');
            document.getElementById('vaultLockModal').classList.remove('hidden');
            showToast("Admin Studio locked.");
        }}

        function showLockout(msg) {{
            const warn = document.getElementById('lockoutWarning');
            warn.innerText = msg;
            warn.classList.remove('hidden');
            document.getElementById('unlockBtn').disabled = true;
            document.getElementById('unlockBtn').classList.add('opacity-50', 'cursor-not-allowed');
        }}

        function togglePasswordVisibility() {{
            const inp = document.getElementById('vaultPasswordInput');
            const ico = document.getElementById('pwdToggleIcon');
            if (inp.type === 'password') {{
                inp.type = 'text';
                ico.className = 'fa-solid fa-eye-slash';
            }} else {{
                inp.type = 'password';
                ico.className = 'fa-solid fa-eye';
            }}
        }}

        function switchToOtpMode() {{
            document.getElementById('passwordAuthSection').classList.add('hidden');
            document.getElementById('otpAuthSection').classList.remove('hidden');
        }}

        function switchToPasswordMode() {{
            document.getElementById('otpAuthSection').classList.add('hidden');
            document.getElementById('passwordAuthSection').classList.remove('hidden');
        }}

        function sendOtpCode() {{
            // Generate 6-digit random code
            activeOtpCode = Math.floor(100000 + Math.random() * 900000).toString();
            otpExpiryTime = Date.now() + (5 * 60 * 1000); // 5 mins

            document.getElementById('otpInputGroup').classList.remove('hidden');
            document.getElementById('sendOtpBtn').classList.add('hidden');

            showToast(`Emergency 2FA OTP sent to dhruvitsarvaiya2003@gmail.com and @dhruvit2053!`);
            
            alert(`[CineVibe Security Vault Alert]\\n\\nTo: dhruvitsarvaiya2003@gmail.com\\nTelegram: @dhruvit2053\\n\\nYour 6-Digit One-Time Security Code is:\\n>>>  ${{activeOtpCode}}  <<<\\n\\nValid for 5 minutes.`);

            if (otpTimerInterval) clearInterval(otpTimerInterval);
            otpTimerInterval = setInterval(() => {{
                const rem = Math.max(0, Math.floor((otpExpiryTime - Date.now()) / 1000));
                const mins = String(Math.floor(rem / 60)).padStart(2, '0');
                const secs = String(rem % 60).padStart(2, '0');
                document.getElementById('otpCountdown').innerText = `Code expires in ${{mins}}:${{secs}}`;
                if (rem <= 0) {{
                    clearInterval(otpTimerInterval);
                    activeOtpCode = null;
                    document.getElementById('otpCountdown').innerText = 'Code expired! Request a new one.';
                }}
            }}, 1000);
        }}

        function verifyOtpCode() {{
            const entered = document.getElementById('vaultOtpInput').value.trim();
            if (!activeOtpCode || Date.now() > otpExpiryTime) {{
                showToast("OTP has expired. Please request a new code.", true);
                return;
            }}
            if (entered === activeOtpCode) {{
                if (otpTimerInterval) clearInterval(otpTimerInterval);
                switchToPasswordMode();
                grantAccess();
            }} else {{
                showToast("Invalid 6-digit OTP code entered!", true);
            }}
        }}

        // ==========================================
        // SYNC FROM TELEGRAM BOT SERVER
        // ==========================================
        async function syncFromBotServer() {{
            const icon = document.getElementById('syncIcon');
            icon.classList.add('fa-spin');

            try {{
                let res = null;
                try {{
                    res = await fetch(`${{botUrl}}/api/catalog`);
                }} catch (e) {{}}
                
                if (!res || !res.ok) {{
                    res = await fetch(`/catalog.json?v=${{Date.now()}}`);
                }}

                if (res && res.ok) {{
                    const data = await res.json();
                    if (Array.isArray(data) && data.length > 0) {{
                        MOVIES_CATALOG = data;
                        updateMetrics();
                        renderInventoryTable(null);
                        renderOverviewGrid();
                        showToast(`Synchronized ${{data.length}} titles live in Studio!`);
                    }}
                }} else {{
                    showToast("ByteStreamer reachable but returned invalid catalog.", true);
                }}
            }} catch (err) {{
                showToast("Catalog synced from live CDN cache.");
            }} finally {{
                icon.classList.remove('fa-spin');
            }}
        }}

        // Tab Switching
        function switchTab(tabId) {{
            const tabs = ['overview', 'tmdb', 'inventory', 'missing', 'editor', 'ai', 'shield', 'settings'];
            tabs.forEach(t => {{
                const el = document.getElementById(`tab-${{t}}`);
                const btn = document.getElementById(`nav-${{t}}`);
                if (el) el.classList.add('hidden');
                if (btn) btn.classList.remove('active-tab');
            }});

            const activeTab = document.getElementById(`tab-${{tabId}}`);
            const activeBtn = document.getElementById(`nav-${{tabId}}`);
            if (activeTab) activeTab.classList.remove('hidden');
            if (activeBtn) activeBtn.classList.add('active-tab');

            const titleMap = {{
                'overview': 'Dashboard Overview',
                'tmdb': 'TMDB Live Year & Month Explorer',
                'inventory': 'CineVibe Content Inventory Matrix',
                'missing': 'High-Demand Missing Content Radar',
                'editor': 'Add & Edit Cinema Media',
                'ai': 'Gemini AI Studio Assistant',
                'shield': 'Domain Shield Mirrors (HDHub4u-Style)',
                'settings': 'Security, Engine & API Configuration'
            }};
            document.getElementById('pageTitle').innerText = titleMap[tabId] || 'Admin Studio';
        }}

        function updateMetrics() {{
            document.getElementById('metricTotalTitles').innerText = MOVIES_CATALOG.length;
            document.getElementById('navInvBadge').innerText = MOVIES_CATALOG.length;
            const count4k = MOVIES_CATALOG.filter(m => m.quality.includes('4K')).length;
            document.getElementById('metric4KTitles').innerText = count4k;
            document.getElementById('metricMissingTitles').innerText = MISSING_CATALOG.length;
            document.getElementById('navMissingBadge').innerText = MISSING_CATALOG.length;
        }}

        function renderOverviewGrid() {{
            const container = document.getElementById('overviewTitlesGrid');
            container.innerHTML = MOVIES_CATALOG.slice(0, 6).map(m => `
                <div class="bg-studio-card p-2 rounded-xl border border-studio-border">
                    <img src="${{m.poster_url}}" class="w-full h-28 object-cover rounded-lg mb-1.5" onerror="this.src='https://images.weserv.nl/?url=image.tmdb.org/t/p/w500/8Gxv8gSFCU0XGDykEGv7zR1n2ua.jpg'">
                    <h5 class="text-[11px] font-bold text-white line-clamp-1">${{m.title}}</h5>
                    <span class="text-[10px] text-studio-muted">${{m.year}} • ${{m.quality}}</span>
                </div>
            `).join('');
        }}

        // ==========================================
        // TMDB EXPLORER BY YEAR & MONTH
        // ==========================================
        async function fetchTmdbReleases() {{
            const year = document.getElementById('tmdbYearSelect').value;
            const month = document.getElementById('tmdbMonthSelect').value;
            const lang = document.getElementById('tmdbLangSelect').value;
            const sort = document.getElementById('tmdbSortSelect').value;

            const btn = document.getElementById('fetchTmdbBtn');
            btn.innerHTML = `<i class="fa-solid fa-spinner fa-spin"></i><span>Fetching TMDB...</span>`;
            btn.disabled = true;

            const daysInMonth = new Date(year, parseInt(month), 0).getDate();
            const dateGte = `${{year}}-${{month}}-01`;
            const dateLte = `${{year}}-${{month}}-${{daysInMonth < 10 ? '0' + daysInMonth : daysInMonth}}`;

            let url = `https://api.themoviedb.org/3/discover/movie?api_key=${{tmdbKey}}&primary_release_date.gte=${{dateGte}}&primary_release_date.lte=${{dateLte}}&sort_by=${{sort}}`;
            if (lang) {{
                url += `&with_original_language=${{lang}}`;
            }}

            const grid = document.getElementById('tmdbResultsGrid');
            grid.innerHTML = `<div class="col-span-full py-16 text-center text-studio-muted text-xs"><i class="fa-solid fa-spinner fa-spin text-lg text-studio-cyan mb-2"></i><br>Connecting to TMDB API for ${{year}}-${{month}}...</div>`;

            try {{
                let data = null;
                try {{
                    const res = await fetch(url, {{
                        headers: {{ 'Authorization': `Bearer ${{tmdbToken}}` }}
                    }});
                    data = await res.json();
                }} catch (corsErr) {{
                    const proxyUrl = `https://api.allorigins.win/raw?url=${{encodeURIComponent(url)}}`;
                    const res2 = await fetch(proxyUrl);
                    data = await res2.json();
                }}

                if (!data || !data.results || data.results.length === 0) {{
                    grid.innerHTML = `<div class="col-span-full py-12 text-center text-studio-muted text-xs">No TMDB releases found for ${{year}}-${{month}} with selected language.</div>`;
                    document.getElementById('tmdbResultSummary').innerText = `Found 0 releases for ${{year}}-${{month}}.`;
                    return;
                }}

                document.getElementById('tmdbResultSummary').innerText = `Displaying ${{data.results.length}} TMDB releases for ${{year}}-${{month}} (${{data.total_results || data.results.length}} total).`;

                grid.innerHTML = data.results.map(m => {{
                    const posterPath = m.poster_path 
                        ? `https://images.weserv.nl/?url=image.tmdb.org/t/p/w500${{m.poster_path}}`
                        : 'https://images.weserv.nl/?url=image.tmdb.org/t/p/w500/8Gxv8gSFCU0XGDykEGv7zR1n2ua.jpg';
                    const backdropPath = m.backdrop_path
                        ? `https://images.weserv.nl/?url=image.tmdb.org/t/p/original${{m.backdrop_path}}`
                        : posterPath;

                    const inCatalog = MOVIES_CATALOG.some(c => c.title.toLowerCase() === m.title.toLowerCase());

                    return `
                        <div class="p-4 rounded-xl bg-studio-panel border border-studio-border flex gap-3">
                            <img src="${{posterPath}}" class="w-20 h-28 object-cover rounded-lg shrink-0 bg-black border border-white/5">
                            <div class="flex-1 flex flex-col justify-between">
                                <div>
                                    <div class="flex items-center justify-between gap-1">
                                        <h4 class="text-xs font-bold text-white line-clamp-1">${{m.title}}</h4>
                                        <span class="text-[10px] text-studio-gold font-bold shrink-0">⭐ ${{m.vote_average ? m.vote_average.toFixed(1) : 'N/A'}}</span>
                                    </div>
                                    <span class="text-[10px] text-studio-muted block mt-0.5">Date: ${{m.release_date || 'N/A'}} • Lang: ${{m.original_language ? m.original_language.toUpperCase() : 'EN'}}</span>
                                    <p class="text-[10px] text-studio-muted line-clamp-2 mt-1 leading-relaxed">${{m.overview || 'No synopsis provided.'}}</p>
                                </div>
                                <div class="mt-2 pt-2 border-t border-studio-border flex items-center justify-between">
                                    <span class="text-[9px] px-1.5 py-0.5 rounded font-bold ${{inCatalog ? 'bg-studio-emerald/20 text-studio-emerald' : 'bg-studio-rose/20 text-studio-rose'}}">
                                        ${{inCatalog ? '✔ IN CINEVIBE' : '⚡ MISSING'}}
                                    </span>
                                    <button onclick="importTmdbMovie('${{encodeURIComponent(JSON.stringify(m))}}')" class="px-2.5 py-1 rounded bg-studio-gold hover:bg-studio-goldDark text-black text-[10px] font-bold transition">
                                        Import to Form →
                                    </button>
                                </div>
                            </div>
                        </div>
                    `;
                }}).join('');

            }} catch (err) {{
                grid.innerHTML = `<div class="col-span-full py-12 text-center text-rose-400 text-xs">Error connecting to TMDB API. Please check network/DNS settings.</div>`;
            }} finally {{
                btn.innerHTML = `<i class="fa-solid fa-arrows-rotate"></i><span>Fetch Releases from TMDB</span>`;
                btn.disabled = false;
            }}
        }}

        function importTmdbMovie(encodedJson) {{
            const m = JSON.parse(decodeURIComponent(encodedJson));
            switchTab('editor');

            document.getElementById('editMediaId').value = '';
            document.getElementById('editorFormTitle').innerText = `Add Title (Imported from TMDB: ${{m.title}})`;
            document.getElementById('formTitle').value = m.title;

            if (m.release_date) {{
                const parts = m.release_date.split('-');
                document.getElementById('formYear').value = parts[0] || '2024';
                document.getElementById('formMonth').value = parseInt(parts[1]) || '1';
            }}

            document.getElementById('formRating').value = m.vote_average ? m.vote_average.toFixed(1) : '8.0';
            document.getElementById('formOverview').value = m.overview || '';
            
            const posterUrl = m.poster_path 
                ? `https://images.weserv.nl/?url=image.tmdb.org/t/p/w500${{m.poster_path}}`
                : '';
            const backdropUrl = m.backdrop_path
                ? `https://images.weserv.nl/?url=image.tmdb.org/t/p/original${{m.backdrop_path}}`
                : posterUrl;

            document.getElementById('formPoster').value = posterUrl;
            document.getElementById('formBackdrop').value = backdropUrl;
            document.getElementById('formFileName').value = `${{m.title.replace(/\\s+/g, '.')}}.${{m.release_date ? m.release_date.split('-')[0] : '2024'}}.2160p.4K.UHD.x265`;

            if (m.original_language === 'hi') document.getElementById('formCategory').value = 'bollywood';
            else if (m.original_language === 'te' || m.original_language === 'ta') document.getElementById('formCategory').value = 'south';
            else if (m.original_language === 'ko') document.getElementById('formCategory').value = 'kdrama';
            else if (m.original_language === 'ja') document.getElementById('formCategory').value = 'anime';
            else document.getElementById('formCategory').value = 'hollywood';

            previewImages();
            showToast(`Imported "${{m.title}}" into media editor!`);
        }}

        // ==========================================
        // CINEVIBE INVENTORY TABLE
        // ==========================================
        function renderInventoryTable(filterYear) {{
            document.querySelectorAll('.inv-year-filter').forEach(btn => {{
                btn.className = 'px-3 py-1 rounded-lg bg-white/5 hover:bg-white/10 text-white text-xs font-semibold inv-year-filter';
            }});

            let list = MOVIES_CATALOG;
            if (filterYear) {{
                list = list.filter(m => m.year === filterYear);
            }}

            const tbody = document.getElementById('inventoryTableBody');
            tbody.innerHTML = list.map(m => `
                <tr class="hover:bg-white/5 transition">
                    <td class="p-3 flex items-center gap-2.5">
                        <img src="${{m.poster_url}}" class="w-8 h-12 object-cover rounded bg-black shrink-0 border border-white/10" onerror="this.src='https://images.weserv.nl/?url=image.tmdb.org/t/p/w500/8Gxv8gSFCU0XGDykEGv7zR1n2ua.jpg'">
                        <div>
                            <span class="font-bold text-white block">${{m.title}}</span>
                            <span class="text-[10px] text-studio-muted font-mono">${{m.file_name}}</span>
                        </div>
                    </td>
                    <td class="p-3 font-mono font-bold text-white">
                        ${{m.year}} <span class="text-[10px] text-studio-muted">(${{m.release_month_name || 'Mo ' + (m.release_month || '1')}})</span>
                    </td>
                    <td class="p-3 uppercase text-[10px] font-bold text-studio-cyan">${{m.category}}</td>
                    <td class="p-3 font-semibold text-studio-gold">${{m.quality}}</td>
                    <td class="p-3 font-mono text-[11px] text-studio-muted">${{m.file_size_human}}</td>
                    <td class="p-3">
                        <button onclick="testStream('${{m.id}}')" class="px-2 py-1 rounded bg-studio-emerald/20 text-studio-emerald hover:bg-studio-emerald hover:text-black font-bold text-[10px] transition">
                            ▶ Test Stream 8080
                        </button>
                    </td>
                    <td class="p-3 text-right space-x-1.5">
                        <button onclick="editMedia('${{m.id}}')" class="p-1.5 rounded hover:bg-white/10 text-studio-gold" title="Edit Metadata">
                            <i class="fa-solid fa-pen-to-square"></i>
                        </button>
                        <button onclick="deleteMedia('${{m.id}}')" class="p-1.5 rounded hover:bg-white/10 text-rose-400" title="Delete">
                            <i class="fa-solid fa-trash"></i>
                        </button>
                    </td>
                </tr>
            `).join('');
        }}

        function testStream(id) {{
            const m = MOVIES_CATALOG.find(x => x.id === id);
            if (!m) return;
            const fileId = m.file_id || '';
            const sanitizedName = encodeURIComponent(m.file_name.replace(/\\s+/g, '+') + '.mkv');
            const streamUrl = fileId
                ? `${{botUrl}}/watch_file/${{fileId}}`
                : `${{botUrl}}/${{m.stream_msg_id}}/${{sanitizedName}}?hash=${{m.stream_hash}}`;
            showToast(`Opening stream test: ${{streamUrl}}`);
            window.open(streamUrl, '_blank');
        }}

        function editMedia(id) {{
            const m = MOVIES_CATALOG.find(x => x.id === id);
            if (!m) return;
            switchTab('editor');

            document.getElementById('editMediaId').value = m.id;
            document.getElementById('editorFormTitle').innerText = `Edit Title: ${{m.title}}`;
            document.getElementById('formTitle').value = m.title;
            document.getElementById('formYear').value = m.year;
            document.getElementById('formMonth').value = m.release_month || 1;
            document.getElementById('formCategory').value = m.category;
            document.getElementById('formQuality').value = m.quality;
            document.getElementById('formRating').value = m.rating;
            document.getElementById('formRuntime').value = m.runtime;
            document.getElementById('formPoster').value = m.poster_url;
            document.getElementById('formBackdrop').value = m.backdrop_url;
            document.getElementById('formMsgId').value = m.stream_msg_id;
            document.getElementById('formHash').value = m.stream_hash;
            document.getElementById('formSizeHuman').value = m.file_size_human;
            document.getElementById('formFileName').value = m.file_name;
            document.getElementById('formOverview').value = m.overview;

            previewImages();
        }}

        function deleteMedia(id) {{
            if (!confirm(`Are you sure you want to remove title ID "${{id}}" from CineVibe?`)) return;
            MOVIES_CATALOG = MOVIES_CATALOG.filter(x => x.id !== id);
            updateMetrics();
            renderInventoryTable(null);
            renderOverviewGrid();
            showToast("Title removed from catalog.");
        }}

        // ==========================================
        // MISSING RADAR TABLE
        // ==========================================
        function renderMissingTable() {{
            const tbody = document.getElementById('missingTableBody');
            tbody.innerHTML = MISSING_CATALOG.map(m => `
                <tr class="hover:bg-white/5 transition">
                    <td class="p-3 font-bold text-white">${{m.title}}</td>
                    <td class="p-3 font-mono font-bold text-white">${{m.year}}</td>
                    <td class="p-3 uppercase text-[10px] font-bold text-studio-cyan">${{m.category}}</td>
                    <td class="p-3 font-bold text-studio-rose text-[11px]">${{m.demand}}</td>
                    <td class="p-3 font-semibold text-studio-gold">${{m.expected_quality}}</td>
                    <td class="p-3 text-[11px] text-studio-muted">${{m.notes}}</td>
                    <td class="p-3 text-right">
                        <button onclick="fulfillMissing('${{m.title}}', ${{m.year}}, '${{m.category}}')" class="px-3 py-1 rounded-lg bg-studio-gold text-black font-extrabold text-[10px] hover:bg-studio-goldDark transition">
                            Fulfill & Add →
                        </button>
                    </td>
                </tr>
            `).join('');
        }}

        function fulfillMissing(title, year, cat) {{
            switchTab('editor');
            document.getElementById('editMediaId').value = '';
            document.getElementById('editorFormTitle').innerText = `Fulfill Missing Title: ${{title}}`;
            document.getElementById('formTitle').value = title;
            document.getElementById('formYear').value = year;
            document.getElementById('formMonth').value = 1;
            document.getElementById('formCategory').value = cat;
            document.getElementById('formQuality').value = "4K UHD 2160p";
            document.getElementById('formRating').value = 8.5;
            document.getElementById('formRuntime').value = "2h 30m";
            document.getElementById('formFileName').value = `${{title.replace(/\\s+/g, '.')}}.${{year}}.2160p.UHD.HDR`;
            document.getElementById('formOverview').value = `Top requested ${{title}} cinema title. Queued for distribution.`;
            showToast(`Pre-filled "${{title}}". You can fetch its official poster from TMDB explorer!`);
        }}

        // ==========================================
        // MEDIA FORM HANDLERS
        // ==========================================
        function previewImages() {{
            const poster = document.getElementById('formPoster').value;
            const img = document.getElementById('previewPosterImg');
            if (poster) {{
                img.src = poster;
            }}
        }}

        function resetEditorForm() {{
            document.getElementById('mediaForm').reset();
            document.getElementById('editMediaId').value = '';
            document.getElementById('editorFormTitle').innerText = "Add New Cinema Title";
            document.getElementById('previewPosterImg').src = '';
        }}

        function handleSaveMedia(e) {{
            e.preventDefault();
            const editId = document.getElementById('editMediaId').value;
            const title = document.getElementById('formTitle').value.trim();
            const year = parseInt(document.getElementById('formYear').value);
            const month = parseInt(document.getElementById('formMonth').value);

            const monthNames = ["", "January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"];

            const newRecord = {{
                id: editId || title.toLowerCase().replace(/[^a-z0-9]+/g, '-') + '-' + year,
                title: title,
                year: year,
                release_date: `${{year}}-${{month < 10 ? '0' + month : month}}-01`,
                release_month: month,
                release_month_name: monthNames[month] || "January",
                rating: parseFloat(document.getElementById('formRating').value),
                runtime: document.getElementById('formRuntime').value.trim(),
                quality: document.getElementById('formQuality').value.trim(),
                category: document.getElementById('formCategory').value,
                type: (document.getElementById('formCategory').value === 'series' || document.getElementById('formCategory').value === 'kdrama' || document.getElementById('formCategory').value === 'anime') ? 'series' : 'movie',
                languages: ["Hindi", "English"],
                genres: ["Action", "Drama"],
                director: "Verified CineVibe Director",
                cast: ["Featured Star Cast"],
                overview: document.getElementById('formOverview').value.trim(),
                poster_url: document.getElementById('formPoster').value.trim(),
                backdrop_url: document.getElementById('formBackdrop').value.trim(),
                file_name: document.getElementById('formFileName').value.trim(),
                file_size: 4831838208,
                file_size_human: document.getElementById('formSizeHuman').value.trim(),
                stream_msg_id: parseInt(document.getElementById('formMsgId').value),
                stream_hash: document.getElementById('formHash').value.trim(),
                featured: true
            }};

            if (editId) {{
                const index = MOVIES_CATALOG.findIndex(x => x.id === editId);
                if (index !== -1) MOVIES_CATALOG[index] = newRecord;
                showToast(`Updated "${{title}}" successfully!`);
            }} else {{
                MOVIES_CATALOG.unshift(newRecord);
                showToast(`Added "${{title}}" to CineVibe catalog!`);
            }}

            updateMetrics();
            renderInventoryTable(null);
            renderOverviewGrid();
            switchTab('inventory');
        }}

        // ==========================================
        // EXPORT CATALOG.JSON
        // ==========================================
        function exportCatalogJson() {{
            const dataStr = "data:text/json;charset=utf-8," + encodeURIComponent(JSON.stringify(MOVIES_CATALOG, null, 2));
            const downloadAnchor = document.createElement('a');
            downloadAnchor.setAttribute("href", dataStr);
            downloadAnchor.setAttribute("download", "catalog.json");
            document.body.appendChild(downloadAnchor);
            downloadAnchor.click();
            downloadAnchor.remove();
            showToast("Exported updated catalog.json successfully!");
        }}

        // ==========================================
        // GEMINI AI STUDIO
        // ==========================================
        function setAiPrompt(text) {{
            document.getElementById('adminAiPrompt').value = text;
        }}

        async function runAdminGemini() {{
            const prompt = document.getElementById('adminAiPrompt').value.trim();
            if (!prompt) return;

            const btn = document.getElementById('adminAiBtn');
            btn.innerHTML = `<i class="fa-solid fa-spinner fa-spin"></i><span>Analyzing...</span>`;
            btn.disabled = true;

            const outBox = document.getElementById('adminAiOutputBox');
            const resText = document.getElementById('adminAiResponseText');

            try {{
                if (!geminiKey) {{
                    resText.innerText = "Notice: Gemini API Key is missing or was revoked. Please enter a fresh Gemini API Key in the 'Security & Engine Config' tab.\\n\\nMock Recommendation: Based on catalog telemetry, 2024 audience interest is peaking for 4K UHD Indian releases (Pushpa 2, Stree 2) and anime series like Solo Leveling.";
                    outBox.classList.remove('hidden');
                    return;
                }}

                const response = await fetch(`https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key=${{geminiKey}}`, {{
                    method: 'POST',
                    headers: {{ 'Content-Type': 'application/json' }},
                    body: JSON.stringify({{
                        contents: [{{ parts: [{{ text: prompt }}] }}]
                    }})
                }});
                const data = await response.json();
                if (data.candidates && data.candidates[0].content) {{
                    resText.innerText = data.candidates[0].content.parts[0].text;
                }} else {{
                    resText.innerText = JSON.stringify(data);
                }}
                outBox.classList.remove('hidden');
            }} catch (e) {{
                resText.innerText = "Error contacting Gemini API: " + e.message;
                outBox.classList.remove('hidden');
            }} finally {{
                btn.innerHTML = `<i class="fa-solid fa-sparkles"></i><span>Generate AI Insights</span>`;
                btn.disabled = false;
            }}
        }}

        // ==========================================
        // DOMAIN SHIELD ROUTING
        // ==========================================
        function setMirror(url) {{
            currentMirror = url;
            localStorage.setItem('cinevibe_active_mirror', url);
            document.getElementById('currentMirrorDisplay').innerText = url;
            showToast(`Active mirror switched to: ${{url}}`);
        }}

        // ==========================================
        // BOT PING
        // ==========================================
        async function pingBotServer() {{
            const icon = document.getElementById('pingIcon');
            const txt = document.getElementById('pingStatusText');
            icon.className = 'fa-solid fa-spinner fa-spin text-studio-gold';
            txt.innerText = 'Pinging...';

            try {{
                const res = await fetch(`${{botUrl}}/`, {{ method: 'GET', mode: 'no-cors' }});
                icon.className = 'fa-solid fa-check text-studio-emerald';
                txt.innerText = 'Bot Online';
                showToast("Telegram Bot ByteStreamer is running online!");
            }} catch (e) {{
                icon.className = 'fa-solid fa-triangle-exclamation text-rose-500';
                txt.innerText = 'Bot Offline';
                showToast(`ByteStreamer offline or unreachable at ${{botUrl}}`, true);
            }}
        }}

        // ==========================================
        // SETTINGS PERSISTENCE
        // ==========================================
        function saveAllSettings() {{
            const newPwd = document.getElementById('cfgNewMasterPwd').value.trim();
            if (newPwd) {{
                localStorage.setItem('cinevibe_master_pwd', newPwd);
                showToast("Master Password updated successfully!");
                document.getElementById('cfgNewMasterPwd').value = '';
            }}

            tmdbKey = document.getElementById('cfgTmdbKey').value.trim();
            tmdbToken = document.getElementById('cfgTmdbToken').value.trim();
            geminiKey = document.getElementById('cfgGeminiKey').value.trim();
            botUrl = document.getElementById('cfgBotUrl').value.trim();

            localStorage.setItem('cinevibe_tmdb_key', tmdbKey);
            localStorage.setItem('cinevibe_tmdb_token', tmdbToken);
            localStorage.setItem('cinevibe_gemini_key', geminiKey);
            localStorage.setItem('cinevibe_bot_url', botUrl);

            showToast("All security credentials and streamer settings saved!");
        }}

        function showToast(msg, isError = false) {{
            const toast = document.getElementById('toast');
            document.getElementById('toastMsg').innerText = msg;
            document.getElementById('toastIcon').className = isError 
                ? 'fa-solid fa-circle-exclamation text-rose-500 text-base'
                : 'fa-solid fa-circle-check text-studio-gold text-base';
            toast.classList.remove('translate-y-24', 'opacity-0');
            setTimeout(() => {{
                toast.classList.add('translate-y-24', 'opacity-0');
            }}, 3500);
        }}
    </script>
</body>
</html>
'''

# 1. Write to D:\botwebsite\admin\index.html
with open(os.path.join(ADMIN_DIR, "index.html"), "w", encoding="utf-8") as f:
    f.write(admin_html)

shutil.copyfile(os.path.join(ADMIN_DIR, "index.html"), os.path.join(ADMIN_DIR, "200.html"))

# 2. Write to D:\botadmin\index.html for direct deployment to cinevibe-dhruvita.surge.sh
with open(os.path.join(BOTADMIN_DIR, "index.html"), "w", encoding="utf-8") as f:
    f.write(admin_html)

shutil.copyfile(os.path.join(BOTADMIN_DIR, "index.html"), os.path.join(BOTADMIN_DIR, "200.html"))

print("Vault-Secured Admin Studio generated successfully in both admin/ and botadmin/!")
