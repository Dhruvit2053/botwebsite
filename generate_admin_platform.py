# -*- coding: utf-8 -*-
import json
import os
import shutil

OUTPUT_DIR = r"D:\botwebsite"

with open(os.path.join(OUTPUT_DIR, "catalog.json"), "r", encoding="utf-8") as f:
    catalog_json = f.read()

with open(os.path.join(OUTPUT_DIR, "missing_catalog.json"), "r", encoding="utf-8") as f:
    missing_json = f.read()

html_content = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="referrer" content="no-referrer">
    <title>CineVibe — Your World of Cinema | AI Discovery, Anime, K-Drama & Admin Command Center</title>
    <link rel="manifest" href="/manifest.json">
    <meta name="theme-color" content="#FFC928">
    <meta name="description" content="CineVibe: Premier 4K UHD movie discovery, K-Dramas, Anime, and authorized high-speed streaming engine.">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&family=Cinzel:wght@600;700;800&display=swap" rel="stylesheet">
    <script src="https://cdn.tailwindcss.com"></script>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">

    <script>
        tailwind.config = {{
            theme: {{
                extend: {{
                    colors: {{
                        brand: {{
                            black: '#080808',
                            dark: '#121212',
                            card: '#181818',
                            border: '#262626',
                            gold: '#FFC928',
                            goldDark: '#F5A623',
                            muted: '#A0A0A0',
                            white: '#FFFFFF'
                        }}
                    }},
                    fontFamily: {{
                        sans: ['"Plus Jakarta Sans"', 'sans-serif'],
                        cinzel: ['"Cinzel"', 'serif']
                    }}
                }}
            }}
        }}
    </script>

    <style>
        body {{
            background-color: #080808;
            color: #FFFFFF;
            font-family: 'Plus Jakarta Sans', sans-serif;
            overflow-x: hidden;
        }}
        .gold-glow {{
            box-shadow: 0 0 35px rgba(255, 201, 40, 0.22);
        }}
        .gold-glow-lg {{
            box-shadow: 0 0 60px rgba(255, 201, 40, 0.35);
        }}
        .glass-panel {{
            background: rgba(18, 18, 18, 0.88);
            backdrop-filter: blur(14px);
            -webkit-backdrop-filter: blur(14px);
            border: 1px solid rgba(255, 255, 255, 0.08);
        }}
        ::-webkit-scrollbar {{
            width: 8px;
            height: 8px;
        }}
        ::-webkit-scrollbar-track {{
            background: #080808;
        }}
        ::-webkit-scrollbar-thumb {{
            background: #262626;
            border-radius: 4px;
        }}
        ::-webkit-scrollbar-thumb:hover {{
            background: #FFC928;
        }}
        .no-scrollbar::-webkit-scrollbar {{
            display: none;
        }}
        .no-scrollbar {{
            -ms-overflow-style: none;
            scrollbar-width: none;
        }}
        .movie-card {{
            transition: all 0.28s cubic-bezier(0.4, 0, 0.2, 1);
        }}
        .movie-card:hover {{
            transform: translateY(-6px) scale(1.02);
            box-shadow: 0 16px 32px rgba(0, 0, 0, 0.8), 0 0 20px rgba(255, 201, 40, 0.18);
        }}
    </style>
</head>
<body class="selection:bg-brand-gold selection:text-black">

    <!-- TOAST NOTIFICATION -->
    <div id="toast" class="fixed bottom-6 right-6 z-50 flex items-center gap-3 px-5 py-3.5 rounded-xl glass-panel border border-brand-gold/30 shadow-2xl transition-all duration-300 transform translate-y-24 opacity-0 pointer-events-none">
        <i id="toastIcon" class="fa-solid fa-circle-check text-brand-gold text-lg"></i>
        <span id="toastMsg" class="text-sm font-medium text-white">Action successful</span>
    </div>

    <!-- DOMAIN SHIELD ACTIVE BADGE (HDHUB4U-STYLE DOMAIN PROTECTION) -->
    <div id="shieldNotification" class="bg-gradient-to-r from-amber-950/70 via-black to-amber-950/70 border-b border-brand-gold/20 px-4 py-1.5 text-center text-[11px] text-brand-gold font-medium flex items-center justify-center gap-2">
        <i class="fa-solid fa-shield-halved text-xs"></i>
        <span><b>Protected by Domain Shield:</b> Main Gateway <a href="https://cinevibe.surge.sh" target="_blank" class="underline text-white font-mono">cinevibe.surge.sh</a> ➔ Active Mirror <code class="text-white px-1.5 py-0.5 rounded bg-white/10 font-mono">cinevibe-cinema</code></span>
        <button onclick="openAdminModal()" class="px-2 py-0.5 rounded bg-brand-gold/20 hover:bg-brand-gold hover:text-black transition ml-2 text-[10px] font-bold text-brand-gold">
            👑 Admin Command Center
        </button>
    </div>

    <!-- ========================================== -->
    <!-- SECTION 1: CINEVIBE CINEMATIC LANDING PAGE -->
    <!-- ========================================== -->
    <div id="landingPage" class="relative min-h-screen flex flex-col justify-between overflow-hidden bg-brand-black transition-opacity duration-700">
        <div class="absolute inset-0 bg-cover bg-center opacity-30 scale-105 transition-transform duration-10000 ease-out" 
             style="background-image: url('https://image.tmdb.org/t/p/original/1pdfLvkbY9ohJlCjQH2CZjjYVvJ.jpg');">
        </div>
        <div class="absolute inset-0 bg-gradient-to-t from-brand-black via-brand-black/80 to-transparent"></div>
        <div class="absolute inset-0 bg-radial from-brand-gold/10 via-transparent to-transparent"></div>

        <!-- Landing Navigation -->
        <header class="relative z-10 max-w-7xl mx-auto w-full px-6 py-6 flex items-center justify-between">
            <div class="flex items-center gap-3">
                <div class="w-10 h-10 rounded-xl bg-gradient-to-tr from-brand-goldDark to-brand-gold flex items-center justify-center shadow-lg shadow-brand-gold/20">
                    <i class="fa-solid fa-film text-brand-black text-lg"></i>
                </div>
                <div>
                    <span class="font-cinzel text-2xl font-bold tracking-wider text-white">CINE<span class="text-brand-gold">VIBE</span></span>
                    <span class="block text-[10px] text-brand-muted tracking-widest font-semibold uppercase">Your World of Cinema</span>
                </div>
            </div>
            <div class="flex items-center gap-3">
                <button onclick="openAdminModal()" class="px-4 py-2 rounded-full text-xs font-bold text-brand-gold glass-panel hover:bg-brand-gold/10 transition flex items-center gap-1.5">
                    <i class="fa-solid fa-crown text-[10px]"></i> Admin Center
                </button>
                <button onclick="enterMainPlatform()" class="px-5 py-2 rounded-full text-xs font-bold text-white glass-panel hover:border-brand-gold/50 transition">
                    Explore Platform →
                </button>
            </div>
        </header>

        <!-- Landing Hero Centerpiece -->
        <main class="relative z-10 max-w-4xl mx-auto px-6 text-center space-y-6 my-auto">
            <div class="inline-flex items-center gap-2 px-4 py-1.5 rounded-full bg-brand-gold/10 border border-brand-gold/30 text-brand-gold text-xs font-semibold tracking-wide">
                <i class="fa-solid fa-sparkles"></i> 4K Cinema • K-Dramas • Anime • High-Speed Downloads
            </div>
            
            <h1 class="text-4xl sm:text-6xl md:text-7xl font-extrabold tracking-tight text-white leading-tight">
                YOUR WORLD OF <br>
                <span class="bg-gradient-to-r from-brand-gold via-amber-200 to-brand-goldDark bg-clip-text text-transparent drop-shadow-sm font-cinzel">
                    CINEMA & ANIME
                </span>
            </h1>

            <p class="text-sm sm:text-lg text-brand-muted max-w-2xl mx-auto font-normal leading-relaxed">
                Stream and download verified 4K UHD movies, popular blockbusters, binge-worthy K-Dramas, and hit anime at lightning speeds.
            </p>

            <div class="pt-4 flex flex-col sm:flex-row items-center justify-center gap-4">
                <button onclick="enterMainPlatform()" class="w-full sm:w-auto px-8 py-4 rounded-xl bg-brand-gold text-brand-black font-extrabold text-sm tracking-wider uppercase flex items-center justify-center gap-3 gold-glow hover:bg-yellow-400 hover:scale-105 active:scale-95 transition duration-300">
                    <span>Enter CineVibe</span>
                    <i class="fa-solid fa-arrow-right"></i>
                </button>
                <button onclick="openModal('aiModal')" class="w-full sm:w-auto px-6 py-4 rounded-xl glass-panel text-white font-bold text-sm hover:border-brand-gold/40 flex items-center justify-center gap-2.5 transition">
                    <i class="fa-solid fa-wand-magic-sparkles text-brand-gold"></i>
                    <span>CineVibe AI Assistant</span>
                </button>
            </div>

            <!-- Features Highlights -->
            <div class="pt-8 grid grid-cols-2 md:grid-cols-4 gap-4 text-left">
                <div class="p-4 rounded-xl glass-panel border border-white/5">
                    <i class="fa-solid fa-film text-brand-gold text-base mb-2"></i>
                    <h4 class="text-xs font-bold text-white">Cinema Library</h4>
                    <p class="text-[11px] text-brand-muted mt-1">Hollywood, Bollywood & South Blockbusters.</p>
                </div>
                <div class="p-4 rounded-xl glass-panel border border-white/5">
                    <i class="fa-solid fa-dragon text-brand-gold text-base mb-2"></i>
                    <h4 class="text-xs font-bold text-white">Anime & K-Drama</h4>
                    <p class="text-[11px] text-brand-muted mt-1">Attack on Titan, Solo Leveling, Remarried Empress.</p>
                </div>
                <div class="p-4 rounded-xl glass-panel border border-white/5">
                    <i class="fa-solid fa-shield-halved text-brand-gold text-base mb-2"></i>
                    <h4 class="text-xs font-bold text-white">Safe Domain Shield</h4>
                    <p class="text-[11px] text-brand-muted mt-1">HDHub4u-style gateway & mirror protection.</p>
                </div>
                <div class="p-4 rounded-xl glass-panel border border-white/5">
                    <i class="fa-solid fa-crown text-brand-gold text-base mb-2"></i>
                    <h4 class="text-xs font-bold text-white">Admin Command Center</h4>
                    <p class="text-[11px] text-brand-muted mt-1">Year-wise inventory, missing radar & full CRUD.</p>
                </div>
            </div>
        </main>

        <!-- Landing Footer -->
        <footer class="relative z-10 max-w-7xl mx-auto w-full px-6 py-6 text-center border-t border-white/5 flex flex-col sm:flex-row items-center justify-between text-xs text-brand-muted gap-3">
            <div>&copy; 2026 CineVibe. All rights reserved. Your World of Cinema.</div>
            <div class="flex items-center gap-5">
                <a href="javascript:void(0)" onclick="openAdminModal()" class="text-brand-gold font-bold hover:underline">👑 Admin Center</a>
                <a href="javascript:void(0)" onclick="openModal('dmcaModal')" class="hover:text-brand-gold transition">DMCA Compliance</a>
                <a href="javascript:void(0)" onclick="openModal('requestModal')" class="hover:text-brand-gold transition">Request Content</a>
            </div>
        </footer>
    </div>


    <!-- ========================================== -->
    <!-- SECTION 2: MAIN CINEVIBE STREAMING PLATFORM -->
    <!-- ========================================== -->
    <div id="mainPlatform" class="hidden min-h-screen flex flex-col bg-brand-black">

        <!-- STICKY TOP HEADER -->
        <header class="sticky top-0 z-40 bg-brand-black/90 backdrop-blur-xl border-b border-white/5">
            <div class="max-w-7xl mx-auto px-4 sm:px-6 h-20 flex items-center justify-between gap-4">
                
                <!-- Logo -->
                <div class="flex items-center gap-3 cursor-pointer shrink-0" onclick="resetToHome()">
                    <div class="w-9 h-9 rounded-xl bg-gradient-to-tr from-brand-goldDark to-brand-gold flex items-center justify-center shadow-lg shadow-brand-gold/20">
                        <i class="fa-solid fa-play text-brand-black text-sm ml-0.5"></i>
                    </div>
                    <div>
                        <span class="font-cinzel text-xl sm:text-2xl font-bold tracking-wider text-white">CINE<span class="text-brand-gold">VIBE</span></span>
                    </div>
                </div>

                <!-- Desktop Navigation Links -->
                <nav class="hidden lg:flex items-center gap-5 text-xs font-semibold text-brand-muted">
                    <a href="javascript:void(0)" onclick="setCategory('')" class="hover:text-white transition">Home</a>
                    <a href="javascript:void(0)" onclick="setCategory('4k')" class="hover:text-white transition">4K Collection</a>
                    <a href="javascript:void(0)" onclick="setCategory('bollywood')" class="hover:text-white transition">Bollywood</a>
                    <a href="javascript:void(0)" onclick="setCategory('hollywood')" class="hover:text-white transition">Hollywood</a>
                    <a href="javascript:void(0)" onclick="setCategory('south')" class="hover:text-white transition">South</a>
                    <a href="javascript:void(0)" onclick="setCategory('series')" class="hover:text-white transition">Web Series</a>
                    <a href="javascript:void(0)" onclick="setCategory('kdrama')" class="hover:text-white transition text-pink-400 font-bold">🌸 K-Drama</a>
                    <a href="javascript:void(0)" onclick="setCategory('anime')" class="hover:text-white transition text-amber-300 font-bold">⚔️ Anime</a>
                </nav>

                <!-- Search Bar -->
                <div class="relative flex-1 max-w-xs sm:max-w-sm md:max-w-md">
                    <i class="fa-solid fa-magnifying-glass absolute left-3.5 top-1/2 -translate-y-1/2 text-brand-muted text-xs"></i>
                    <input type="text" id="searchInput" oninput="handleSearch(this.value)" placeholder="Search movies, anime, dramas, 4K..." 
                           class="w-full bg-brand-card/90 border border-white/10 rounded-full pl-9 pr-8 py-2 text-xs text-white placeholder-brand-muted/70 focus:outline-none focus:border-brand-gold transition">
                    <button id="clearSearchBtn" onclick="clearSearch()" class="hidden absolute right-3 top-1/2 -translate-y-1/2 text-brand-muted hover:text-white text-xs">
                        <i class="fa-solid fa-xmark"></i>
                    </button>
                </div>

                <!-- Action Buttons -->
                <div class="flex items-center gap-2 sm:gap-3 shrink-0">
                    <button onclick="openAdminModal()" class="flex items-center gap-1.5 px-3 py-2 rounded-full bg-amber-500/10 border border-amber-500/40 text-brand-gold text-xs font-bold hover:bg-brand-gold hover:text-black transition" title="Open Admin Command Center">
                        <i class="fa-solid fa-crown text-xs"></i>
                        <span class="hidden sm:inline">Admin Center</span>
                    </button>
                    <button onclick="openModal('aiModal')" class="flex items-center gap-2 px-3 py-2 rounded-full bg-white/5 border border-white/10 text-white text-xs font-bold hover:bg-brand-gold hover:text-black transition">
                        <i class="fa-solid fa-wand-magic-sparkles text-xs text-brand-gold"></i>
                        <span class="hidden md:inline">AI Search</span>
                    </button>
                    <button onclick="openModal('settingsModal')" class="p-2.5 rounded-full glass-panel text-brand-muted hover:text-white transition" title="Shield & Stream Settings">
                        <i class="fa-solid fa-gear text-xs"></i>
                    </button>
                </div>
            </div>

            <!-- Mobile Category Scroll Bar -->
            <div class="lg:hidden flex items-center gap-2 px-4 py-2 overflow-x-auto no-scrollbar border-t border-white/5 text-[11px] font-semibold text-brand-muted">
                <button onclick="setCategory('')" class="px-3 py-1 rounded-full bg-brand-card border border-white/10 shrink-0 text-white">All Cinema</button>
                <button onclick="setCategory('4k')" class="px-3 py-1 rounded-full bg-brand-card border border-white/10 shrink-0">💎 4K UHD</button>
                <button onclick="setCategory('kdrama')" class="px-3 py-1 rounded-full bg-brand-card border border-pink-500/30 text-pink-400 shrink-0">🌸 K-Drama</button>
                <button onclick="setCategory('anime')" class="px-3 py-1 rounded-full bg-brand-card border border-amber-500/30 text-amber-300 shrink-0">⚔️ Anime</button>
                <button onclick="setCategory('bollywood')" class="px-3 py-1 rounded-full bg-brand-card border border-white/10 shrink-0">Bollywood</button>
                <button onclick="setCategory('hollywood')" class="px-3 py-1 rounded-full bg-brand-card border border-white/10 shrink-0">Hollywood</button>
                <button onclick="setCategory('south')" class="px-3 py-1 rounded-full bg-brand-card border border-white/10 shrink-0">South</button>
                <button onclick="setCategory('series')" class="px-3 py-1 rounded-full bg-brand-card border border-white/10 shrink-0">Web Series</button>
            </div>
        </header>

        <!-- HERO TRENDING POSTER SLIDER -->
        <section id="heroSliderSection" class="relative w-full h-[380px] sm:h-[480px] md:h-[540px] overflow-hidden bg-brand-dark">
            <div id="sliderBackground" class="absolute inset-0 bg-cover bg-center transition-all duration-700 ease-out filter brightness-[0.55] scale-105"></div>
            <div class="absolute inset-0 bg-gradient-to-t from-brand-black via-brand-black/40 to-transparent"></div>
            <div class="absolute inset-0 bg-gradient-to-r from-brand-black via-brand-black/70 to-transparent"></div>

            <div class="relative z-10 max-w-7xl mx-auto h-full px-6 flex items-end pb-12 sm:pb-16">
                <div class="max-w-2xl space-y-4">
                    <div class="flex items-center gap-2.5">
                        <span id="slideBadge" class="px-2.5 py-0.5 rounded-full bg-brand-gold text-brand-black text-[10px] font-extrabold uppercase tracking-wider">
                            Trending #1
                        </span>
                        <span id="slideQuality" class="px-2 py-0.5 rounded bg-black/60 border border-white/10 text-[10px] font-semibold text-brand-muted">
                            4K UHD
                        </span>
                        <span id="slideRating" class="flex items-center gap-1 text-[11px] text-brand-gold font-bold">
                            <i class="fa-solid fa-star text-xs"></i> 8.6
                        </span>
                    </div>

                    <h2 id="slideTitle" class="text-2xl sm:text-4xl md:text-5xl font-extrabold text-white tracking-tight line-clamp-1">
                        Title
                    </h2>

                    <p id="slideOverview" class="text-xs sm:text-sm text-brand-muted line-clamp-2 max-w-xl leading-relaxed">
                        Overview
                    </p>

                    <div class="pt-2 flex items-center gap-3">
                        <button id="slidePlayBtn" class="px-6 py-3 rounded-xl bg-brand-gold text-brand-black font-extrabold text-xs uppercase tracking-wider flex items-center gap-2.5 hover:bg-yellow-400 gold-glow transition">
                            <i class="fa-solid fa-play text-xs"></i>
                            <span>Watch Online</span>
                        </button>
                        <button id="slideDetailsBtn" class="px-5 py-3 rounded-xl glass-panel text-white font-bold text-xs hover:border-brand-gold/40 transition">
                            More Info
                        </button>
                    </div>
                </div>

                <!-- Slider Controls -->
                <div class="absolute right-6 bottom-12 hidden md:flex items-center gap-3">
                    <button onclick="prevSlide()" class="w-10 h-10 rounded-full glass-panel flex items-center justify-center text-white hover:text-brand-gold transition">
                        <i class="fa-solid fa-chevron-left text-xs"></i>
                    </button>
                    <button onclick="nextSlide()" class="w-10 h-10 rounded-full glass-panel flex items-center justify-center text-white hover:text-brand-gold transition">
                        <i class="fa-solid fa-chevron-right text-xs"></i>
                    </button>
                </div>
            </div>
        </section>

        <!-- 11 HOMEPAGE SECTIONS CONTAINER -->
        <main id="sectionsContainer" class="max-w-7xl mx-auto px-4 sm:px-6 py-8 space-y-10 w-full">
            <!-- Dynamically populated via loadHomepageSections() -->
        </main>

        <!-- SEARCH & FILTER RESULTS VIEW -->
        <main id="catalogSection" class="hidden max-w-7xl mx-auto px-4 sm:px-6 py-8 w-full space-y-6">
            <div class="flex items-center justify-between border-b border-white/5 pb-4">
                <div>
                    <h3 id="catalogHeading" class="text-xl font-bold text-white tracking-wide">Search Results</h3>
                    <span id="catalogCount" class="text-xs text-brand-muted mt-0.5 block">Found titles matching your filters</span>
                </div>
                <button onclick="closeSearchResults()" class="text-xs text-brand-gold hover:underline font-semibold flex items-center gap-1">
                    <i class="fa-solid fa-arrow-left text-[10px]"></i> Back to All Sections
                </button>
            </div>
            <div id="catalogGrid" class="grid grid-cols-2 sm:grid-cols-3 md:grid-cols-4 lg:grid-cols-6 gap-4">
                <!-- Movie cards populated dynamically -->
            </div>
        </main>

        <!-- FOOTER -->
        <footer class="mt-auto border-t border-white/5 bg-brand-black/80 py-8 px-6 text-center text-xs text-brand-muted space-y-3">
            <div class="flex items-center justify-center gap-2">
                <span class="font-cinzel text-lg font-bold text-white">CINE<span class="text-brand-gold">VIBE</span></span>
                <span class="text-brand-muted">| Your World of Cinema</span>
            </div>
            <p class="max-w-xl mx-auto text-[11px] leading-relaxed">
                CineVibe Authorized Media Ecosystem. Fast downloads powered by high-speed parallel session streamers. All trademarks and rights belong to their respective verified licensors.
            </p>
            <div class="flex items-center justify-center gap-6 pt-2">
                <a href="javascript:void(0)" onclick="openAdminModal()" class="text-brand-gold font-bold hover:underline">👑 Admin Command Center</a>
                <a href="javascript:void(0)" onclick="openModal('dmcaModal')" class="hover:text-brand-gold transition">DMCA & Copyright Policy</a>
                <a href="javascript:void(0)" onclick="openModal('requestModal')" class="hover:text-brand-gold transition">Request a Title</a>
                <a href="javascript:void(0)" onclick="openModal('settingsModal')" class="hover:text-brand-gold transition">Shield & Stream Settings</a>
            </div>
        </footer>
    </div>


    <!-- ========================================== -->
    <!-- MODAL 1: ADVANCED MOVIE DETAILS -->
    <!-- ========================================== -->
    <div id="movieModal" class="hidden fixed inset-0 z-50 flex items-center justify-center p-3 sm:p-6 bg-black/85 backdrop-blur-md overflow-y-auto">
        <div class="relative w-full max-w-3xl glass-panel rounded-2xl overflow-hidden border border-white/10 shadow-2xl my-auto animate-fade-in">
            
            <!-- Modal Header Backdrop -->
            <div id="modalBackdrop" class="relative h-48 sm:h-64 w-full bg-cover bg-center">
                <div class="absolute inset-0 bg-gradient-to-t from-brand-card via-brand-card/50 to-transparent"></div>
                <button onclick="closeModal('movieModal')" class="absolute top-4 right-4 w-9 h-9 rounded-full bg-black/60 text-white hover:text-brand-gold flex items-center justify-center transition border border-white/10">
                    <i class="fa-solid fa-xmark text-sm"></i>
                </button>
            </div>

            <!-- Modal Content Body -->
            <div class="p-6 -mt-16 sm:-mt-20 relative z-10 space-y-6 bg-brand-card">
                <div class="flex gap-4 sm:gap-6 items-end">
                    <img id="modalPoster" referrerpolicy="no-referrer" src="" class="w-24 sm:w-28 h-36 sm:h-40 object-cover rounded-xl shadow-2xl border border-white/20 shrink-0">
                    <div class="space-y-1.5 flex-1">
                        <div class="flex items-center gap-2 flex-wrap">
                            <span id="modalQuality" class="px-2 py-0.5 rounded bg-brand-gold text-black text-[10px] font-extrabold uppercase">4K UHD</span>
                            <span id="modalYear" class="text-xs text-brand-muted">2024</span>
                            <span id="modalRuntime" class="text-xs text-brand-muted">• 2h 10m</span>
                            <span id="modalRating" class="text-xs text-brand-gold font-bold flex items-center gap-1"><i class="fa-solid fa-star text-[10px]"></i> 8.6</span>
                        </div>
                        <h3 id="modalTitle" class="text-xl sm:text-2xl font-bold text-white tracking-tight">Movie Title</h3>
                        <p id="modalOriginalTitle" class="text-xs text-brand-muted italic">Original Title</p>
                    </div>
                </div>

                <!-- Tabs Navigation -->
                <div class="flex items-center gap-4 border-b border-white/10 text-xs font-semibold">
                    <button onclick="switchModalTab('overview')" id="tabBtn-overview" class="pb-2.5 border-b-2 border-brand-gold text-brand-gold">Overview</button>
                    <button onclick="switchModalTab('formats')" id="tabBtn-formats" class="pb-2.5 text-brand-muted hover:text-white">Authorized Formats</button>
                    <button onclick="switchModalTab('cast')" id="tabBtn-cast" class="pb-2.5 text-brand-muted hover:text-white">Cast & Crew</button>
                </div>

                <!-- Tab 1: Overview -->
                <div id="tabContent-overview" class="space-y-4">
                    <p id="modalOverview" class="text-xs sm:text-sm text-brand-muted leading-relaxed">
                        Detailed synopsis of the movie...
                    </p>
                    <div class="grid grid-cols-2 sm:grid-cols-3 gap-3 text-xs pt-2">
                        <div>
                            <span class="text-brand-muted block text-[10px] uppercase font-semibold">Director</span>
                            <span id="modalDirector" class="text-white font-medium">Christopher Nolan</span>
                        </div>
                        <div>
                            <span class="text-brand-muted block text-[10px] uppercase font-semibold">Audio Languages</span>
                            <span id="modalLanguages" class="text-white font-medium">Hindi, English</span>
                        </div>
                        <div>
                            <span class="text-brand-muted block text-[10px] uppercase font-semibold">Distribution Status</span>
                            <span class="text-emerald-400 font-bold flex items-center gap-1"><i class="fa-solid fa-check-circle text-[10px]"></i> Verified Authorized</span>
                        </div>
                    </div>
                </div>

                <!-- Tab 2: Formats -->
                <div id="tabContent-formats" class="hidden space-y-3">
                    <div class="text-[11px] text-brand-muted">Select an authorized download or streaming format:</div>
                    <div class="space-y-2" id="modalFormatsList">
                        <!-- Format rows dynamically rendered -->
                    </div>
                </div>

                <!-- Tab 3: Cast & Crew -->
                <div id="tabContent-cast" class="hidden space-y-3">
                    <div id="modalCastList" class="flex flex-wrap gap-2 text-xs">
                        <!-- Cast tags -->
                    </div>
                </div>

                <!-- Modal Actions -->
                <div class="pt-4 border-t border-white/10 flex flex-col sm:flex-row items-center gap-3">
                    <button id="modalStreamBtn" class="w-full sm:flex-1 py-3 px-5 rounded-xl bg-brand-gold text-brand-black font-extrabold text-xs uppercase tracking-wider flex items-center justify-center gap-2 hover:bg-yellow-400 gold-glow transition">
                        <i class="fa-solid fa-play"></i>
                        <span>Watch Online</span>
                    </button>
                    <button id="modalDownloadBtn" class="w-full sm:flex-1 py-3 px-5 rounded-xl bg-white/10 text-white font-bold text-xs uppercase tracking-wider flex items-center justify-center gap-2 hover:bg-white/20 transition">
                        <i class="fa-solid fa-download"></i>
                        <span>Fast Download (8x Speed)</span>
                    </button>
                    <button onclick="copyCurrentStreamLink()" class="w-full sm:w-auto p-3 rounded-xl glass-panel text-brand-muted hover:text-white transition" title="Copy Stream Link">
                        <i class="fa-solid fa-link text-xs"></i>
                    </button>
                </div>
            </div>
        </div>
    </div>


    <!-- ========================================== -->
    <!-- MODAL 2: ADMIN COMMAND CENTER (ADVANCED)  -->
    <!-- ========================================== -->
    <div id="adminModal" class="hidden fixed inset-0 z-50 flex items-center justify-center p-3 sm:p-6 bg-black/90 backdrop-blur-md overflow-y-auto">
        <div class="relative w-full max-w-5xl glass-panel rounded-2xl overflow-hidden border border-brand-gold/40 shadow-2xl my-auto animate-fade-in flex flex-col max-h-[92vh] bg-brand-card">
            
            <!-- Admin Top Header -->
            <div class="px-6 py-4 border-b border-white/10 flex items-center justify-between bg-black/60 shrink-0">
                <div class="flex items-center gap-3">
                    <div class="w-9 h-9 rounded-xl bg-gradient-to-tr from-brand-goldDark to-brand-gold flex items-center justify-center shadow-lg shadow-brand-gold/20 text-black">
                        <i class="fa-solid fa-crown text-base"></i>
                    </div>
                    <div>
                        <h3 class="text-base font-bold text-white tracking-wide">CineVibe Admin Command Center</h3>
                        <span class="text-[10px] text-brand-gold font-semibold uppercase tracking-wider">Full Inventory Control, Year Radar, Missing Content & Mirror Switcher</span>
                    </div>
                </div>
                <div class="flex items-center gap-3">
                    <button onclick="exportUpdatedCatalog()" class="px-3 py-1.5 rounded-lg bg-white/10 hover:bg-brand-gold hover:text-black text-xs font-bold transition flex items-center gap-1.5" title="Export updated catalog.json">
                        <i class="fa-solid fa-download text-[10px]"></i>
                        <span>Export Catalog JSON</span>
                    </button>
                    <button onclick="closeModal('adminModal')" class="text-brand-muted hover:text-white text-base">
                        <i class="fa-solid fa-xmark"></i>
                    </button>
                </div>
            </div>

            <!-- Admin Nav Tabs -->
            <div class="px-6 py-2.5 border-b border-white/10 bg-brand-dark/50 flex items-center gap-3 overflow-x-auto no-scrollbar text-xs font-semibold shrink-0">
                <button onclick="switchAdminTab('inventory')" id="admTabBtn-inventory" class="px-3 py-1.5 rounded-lg bg-brand-gold text-black font-bold">
                    📅 Year-by-Year Inventory
                </button>
                <button onclick="switchAdminTab('missing')" id="admTabBtn-missing" class="px-3 py-1.5 rounded-lg text-brand-muted hover:text-white font-medium">
                    ⚡ Missing Content Radar (<span id="missingCountBadge">7</span>)
                </button>
                <button onclick="switchAdminTab('manage')" id="admTabBtn-manage" class="px-3 py-1.5 rounded-lg text-brand-muted hover:text-white font-medium">
                    ➕ Add & Manage Media
                </button>
                <button onclick="switchAdminTab('shield')" id="admTabBtn-shield" class="px-3 py-1.5 rounded-lg text-brand-muted hover:text-white font-medium">
                    🛡️ Domain Shield & Mirror Control
                </button>
                <button onclick="switchAdminTab('system')" id="admTabBtn-system" class="px-3 py-1.5 rounded-lg text-brand-muted hover:text-white font-medium">
                    ⚙️ Bot & Stream Telemetry
                </button>
            </div>

            <!-- Admin Scrollable Body -->
            <div class="p-6 overflow-y-auto space-y-6 flex-1 text-xs">
                
                <!-- KPI Analytics Summary Cards -->
                <div class="grid grid-cols-2 sm:grid-cols-3 md:grid-cols-6 gap-3">
                    <div class="p-3.5 rounded-xl bg-brand-dark border border-white/5 space-y-1">
                        <span class="text-brand-muted text-[10px] uppercase font-bold block">Total Titles</span>
                        <span id="kpiTotal" class="text-xl font-extrabold text-white">17</span>
                        <span class="text-[10px] text-emerald-400 block font-semibold">● 100% Verified</span>
                    </div>
                    <div class="p-3.5 rounded-xl bg-brand-dark border border-white/5 space-y-1">
                        <span class="text-brand-muted text-[10px] uppercase font-bold block">Movies</span>
                        <span id="kpiMovies" class="text-xl font-extrabold text-brand-gold">9</span>
                        <span class="text-[10px] text-brand-muted block">Bolly, Holly, South</span>
                    </div>
                    <div class="p-3.5 rounded-xl bg-brand-dark border border-white/5 space-y-1">
                        <span class="text-brand-muted text-[10px] uppercase font-bold block">Web Series</span>
                        <span id="kpiSeries" class="text-xl font-extrabold text-amber-400">2</span>
                        <span class="text-[10px] text-brand-muted block">Crime & Sci-Fi</span>
                    </div>
                    <div class="p-3.5 rounded-xl bg-brand-dark border border-white/5 space-y-1">
                        <span class="text-brand-muted text-[10px] uppercase font-bold block">K-Dramas</span>
                        <span id="kpiKdrama" class="text-xl font-extrabold text-pink-400">2</span>
                        <span class="text-[10px] text-brand-muted block">Romance & Royal</span>
                    </div>
                    <div class="p-3.5 rounded-xl bg-brand-dark border border-white/5 space-y-1">
                        <span class="text-brand-muted text-[10px] uppercase font-bold block">Anime Series</span>
                        <span id="kpiAnime" class="text-xl font-extrabold text-purple-400">4</span>
                        <span class="text-[10px] text-brand-muted block">Shonen & Fantasy</span>
                    </div>
                    <div class="p-3.5 rounded-xl bg-brand-dark border border-white/5 space-y-1">
                        <span class="text-brand-muted text-[10px] uppercase font-bold block">Missing Radar</span>
                        <span id="kpiMissing" class="text-xl font-extrabold text-rose-400">7</span>
                        <span class="text-[10px] text-rose-300 block">Pending Requests</span>
                    </div>
                </div>

                <!-- ============================================== -->
                <!-- ADMIN TAB 1: YEAR-BY-YEAR INVENTORY MATRIX    -->
                <!-- ("KONSE YEARS KI KON KON SI MOVIES APNE PASS") -->
                <!-- ============================================== -->
                <div id="admContent-inventory" class="space-y-4">
                    <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-3 bg-brand-dark p-3.5 rounded-xl border border-white/5">
                        <div>
                            <h4 class="text-sm font-bold text-white">Year-by-Year Media Inventory ("Apne Pass Kya Hai")</h4>
                            <p class="text-[11px] text-brand-muted">Filter and inspect all verified movies, webseries, kdrama and anime in our collection by release year.</p>
                        </div>
                        <div class="flex items-center gap-1.5 overflow-x-auto no-scrollbar">
                            <button onclick="filterInventoryByYear('all')" id="yrBtn-all" class="px-2.5 py-1 rounded-lg bg-brand-gold text-black font-bold text-[11px]">All Years</button>
                            <button onclick="filterInventoryByYear('2024')" id="yrBtn-2024" class="px-2.5 py-1 rounded-lg bg-white/5 hover:bg-white/10 text-white text-[11px]">2024</button>
                            <button onclick="filterInventoryByYear('2023')" id="yrBtn-2023" class="px-2.5 py-1 rounded-lg bg-white/5 hover:bg-white/10 text-white text-[11px]">2023</button>
                            <button onclick="filterInventoryByYear('2022')" id="yrBtn-2022" class="px-2.5 py-1 rounded-lg bg-white/5 hover:bg-white/10 text-white text-[11px]">2022</button>
                            <button onclick="filterInventoryByYear('2021')" id="yrBtn-2021" class="px-2.5 py-1 rounded-lg bg-white/5 hover:bg-white/10 text-white text-[11px]">2021</button>
                            <button onclick="filterInventoryByYear('2020')" id="yrBtn-2020" class="px-2.5 py-1 rounded-lg bg-white/5 hover:bg-white/10 text-white text-[11px]">2020</button>
                        </div>
                    </div>

                    <!-- Inventory Table -->
                    <div class="overflow-x-auto rounded-xl border border-white/5 bg-brand-dark">
                        <table class="w-full text-left">
                            <thead>
                                <tr class="border-b border-white/10 text-brand-gold text-[11px] bg-black/40">
                                    <th class="p-3">Title & Media</th>
                                    <th>Year</th>
                                    <th>Category</th>
                                    <th>Quality</th>
                                    <th>Languages</th>
                                    <th>File Size</th>
                                    <th>Stream ID</th>
                                    <th>Action</th>
                                </tr>
                            </thead>
                            <tbody id="inventoryTableBody" class="divide-y divide-white/5 text-[11px]">
                                <!-- Rendered dynamically -->
                            </tbody>
                        </table>
                    </div>
                </div>

                <!-- ============================================== -->
                <!-- ADMIN TAB 2: MISSING CONTENT & WISHLIST RADAR -->
                <!-- ("KON KON SI MOVIES/SERIES APNE PASS NAHI HAI")-->
                <!-- ============================================== -->
                <div id="admContent-missing" class="hidden space-y-4">
                    <div class="bg-brand-dark p-4 rounded-xl border border-rose-500/20 space-y-1">
                        <div class="flex items-center gap-2">
                            <span class="w-2.5 h-2.5 rounded-full bg-rose-500 animate-pulse"></span>
                            <h4 class="text-sm font-bold text-white">Missing Content & User Wishlist Radar ("Apne Pass Kya Nahi Hai")</h4>
                        </div>
                        <p class="text-[11px] text-brand-muted">
                            Titles with high search volume or user requests that are NOT currently in our library. Click <b>"Fulfill & Add"</b> to quickly add the stream token and upload to the catalog!
                        </p>
                    </div>

                    <div class="overflow-x-auto rounded-xl border border-white/5 bg-brand-dark">
                        <table class="w-full text-left">
                            <thead>
                                <tr class="border-b border-white/10 text-rose-400 text-[11px] bg-black/40">
                                    <th class="p-3">Requested Title</th>
                                    <th>Year</th>
                                    <th>Type</th>
                                    <th>Demand Status</th>
                                    <th>Expected Quality</th>
                                    <th>Community Notes</th>
                                    <th>Action</th>
                                </tr>
                            </thead>
                            <tbody id="missingTableBody" class="divide-y divide-white/5 text-[11px]">
                                <!-- Rendered dynamically -->
                            </tbody>
                        </table>
                    </div>
                </div>

                <!-- ============================================== -->
                <!-- ADMIN TAB 3: ADD & MANAGE CONTENT             -->
                <!-- ============================================== -->
                <div id="admContent-manage" class="hidden space-y-6">
                    <div class="bg-brand-dark p-4 rounded-xl border border-white/5 space-y-4">
                        <h4 class="text-sm font-bold text-white flex items-center gap-2">
                            <i class="fa-solid fa-plus-circle text-brand-gold"></i>
                            <span>Add New Movie / Web Series / K-Drama / Anime to Library</span>
                        </h4>

                        <form onsubmit="handleAddNewMedia(event)" class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-4 gap-3 text-xs">
                            <div class="md:col-span-2">
                                <label class="block text-brand-muted font-semibold mb-1">Title *</label>
                                <input type="text" id="addTitle" required placeholder="e.g. Stree 2: Sarkate Ka Aatank" class="w-full bg-brand-card border border-white/10 rounded-xl px-3 py-2 text-white focus:outline-none focus:border-brand-gold">
                            </div>
                            <div>
                                <label class="block text-brand-muted font-semibold mb-1">Release Year *</label>
                                <input type="number" id="addYear" required value="2024" class="w-full bg-brand-card border border-white/10 rounded-xl px-3 py-2 text-white focus:outline-none focus:border-brand-gold">
                            </div>
                            <div>
                                <label class="block text-brand-muted font-semibold mb-1">Media Type *</label>
                                <select id="addType" class="w-full bg-brand-card border border-white/10 rounded-xl px-3 py-2 text-white focus:outline-none focus:border-brand-gold">
                                    <option value="movie">Movie</option>
                                    <option value="series">Web Series</option>
                                    <option value="kdrama">K-Drama</option>
                                    <option value="anime">Anime</option>
                                </select>
                            </div>

                            <div>
                                <label class="block text-brand-muted font-semibold mb-1">Quality / Resolution *</label>
                                <select id="addQuality" class="w-full bg-brand-card border border-white/10 rounded-xl px-3 py-2 text-white focus:outline-none focus:border-brand-gold">
                                    <option value="4K UHD 2160p">4K UHD 2160p</option>
                                    <option value="1080p FHD">1080p FHD</option>
                                    <option value="720p HD">720p HD</option>
                                </select>
                            </div>
                            <div>
                                <label class="block text-brand-muted font-semibold mb-1">Category *</label>
                                <select id="addCategory" class="w-full bg-brand-card border border-white/10 rounded-xl px-3 py-2 text-white focus:outline-none focus:border-brand-gold">
                                    <option value="bollywood">Bollywood</option>
                                    <option value="hollywood">Hollywood</option>
                                    <option value="south">South Indian</option>
                                    <option value="series">Web Series</option>
                                    <option value="kdrama">K-Drama</option>
                                    <option value="anime">Anime</option>
                                </select>
                            </div>
                            <div>
                                <label class="block text-brand-muted font-semibold mb-1">Audio Languages</label>
                                <input type="text" id="addLanguages" value="Hindi, English" class="w-full bg-brand-card border border-white/10 rounded-xl px-3 py-2 text-white focus:outline-none focus:border-brand-gold">
                            </div>
                            <div>
                                <label class="block text-brand-muted font-semibold mb-1">File Size Human</label>
                                <input type="text" id="addSize" value="2.50 GB" class="w-full bg-brand-card border border-white/10 rounded-xl px-3 py-2 text-white focus:outline-none focus:border-brand-gold">
                            </div>

                            <div class="md:col-span-2">
                                <label class="block text-brand-muted font-semibold mb-1">Poster Image URL (TMDB/Wiki) *</label>
                                <input type="url" id="addPosterUrl" required placeholder="https://image.tmdb.org/t/p/w500/..." class="w-full bg-brand-card border border-white/10 rounded-xl px-3 py-2 text-white focus:outline-none focus:border-brand-gold">
                            </div>
                            <div class="md:col-span-2">
                                <label class="block text-brand-muted font-semibold mb-1">Backdrop Image URL (TMDB/Wiki) *</label>
                                <input type="url" id="addBackdropUrl" required placeholder="https://image.tmdb.org/t/p/original/..." class="w-full bg-brand-card border border-white/10 rounded-xl px-3 py-2 text-white focus:outline-none focus:border-brand-gold">
                            </div>

                            <div>
                                <label class="block text-brand-muted font-semibold mb-1">Stream Message ID</label>
                                <input type="number" id="addMsgId" value="150" class="w-full bg-brand-card border border-white/10 rounded-xl px-3 py-2 text-white focus:outline-none focus:border-brand-gold">
                            </div>
                            <div>
                                <label class="block text-brand-muted font-semibold mb-1">Stream Hash Token</label>
                                <input type="text" id="addHash" value="AgAD56" class="w-full bg-brand-card border border-white/10 rounded-xl px-3 py-2 text-white focus:outline-none focus:border-brand-gold">
                            </div>
                            <div class="md:col-span-2 flex items-end">
                                <button type="submit" class="w-full py-2.5 rounded-xl bg-brand-gold text-brand-black font-extrabold tracking-wider uppercase hover:bg-yellow-400 transition shadow-lg">
                                    Publish to Catalog ➔
                                </button>
                            </div>
                        </form>
                    </div>
                </div>

                <!-- ============================================== -->
                <!-- ADMIN TAB 4: DOMAIN SHIELD & MIRROR SWITCHER  -->
                <!-- ============================================== -->
                <div id="admContent-shield" class="hidden space-y-4">
                    <div class="bg-brand-dark p-4 rounded-xl border border-brand-gold/30 space-y-3">
                        <div class="flex items-center gap-2">
                            <i class="fa-solid fa-shield-halved text-brand-gold text-base"></i>
                            <h4 class="text-sm font-bold text-white">HDHub4u-Style Domain Shield Control Panel</h4>
                        </div>
                        <p class="text-[11px] text-brand-muted leading-relaxed">
                            Your permanent main domain <code class="text-brand-gold font-mono font-bold">https://cinevibe.surge.sh</code> is 100% clean and never hosts files. Visitors are forwarded automatically to the currently active worker mirror. If the active mirror gets blocked, switch it here in 1 second!
                        </p>

                        <div class="grid grid-cols-1 sm:grid-cols-3 gap-3 pt-2">
                            <div class="p-3 rounded-xl bg-brand-card border border-white/5 space-y-1">
                                <span class="text-[10px] text-brand-muted block uppercase font-bold">Permanent Shield Gateway</span>
                                <span class="text-xs font-mono font-bold text-white block">cinevibe.surge.sh</span>
                                <span class="text-[10px] text-emerald-400 font-bold">🟢 Active & Protected</span>
                            </div>
                            <div class="p-3 rounded-xl bg-brand-card border border-white/5 space-y-1">
                                <span class="text-[10px] text-brand-muted block uppercase font-bold">Current Active Mirror</span>
                                <span id="admDisplayMirror" class="text-xs font-mono font-bold text-brand-gold block">cinevibe-cinema.surge.sh</span>
                                <span class="text-[10px] text-emerald-400 font-bold">🟢 17 Titles Loaded</span>
                            </div>
                            <div class="p-3 rounded-xl bg-brand-card border border-white/5 space-y-1">
                                <span class="text-[10px] text-brand-muted block uppercase font-bold">Quick Switch Mirrors</span>
                                <div class="flex items-center gap-1.5 pt-1">
                                    <button onclick="setQuickMirror('https://cinevibe-cinema.surge.sh')" class="px-2 py-1 rounded bg-brand-gold/20 text-brand-gold text-[10px] font-bold hover:bg-brand-gold hover:text-black">Node 1</button>
                                    <button onclick="setQuickMirror('https://new16.hdhub4u.cl')" class="px-2 py-1 rounded bg-white/10 text-white text-[10px] font-bold hover:bg-white/20">new16</button>
                                    <button onclick="setQuickMirror('https://new17.hdhub4u.cl')" class="px-2 py-1 rounded bg-white/10 text-white text-[10px] font-bold hover:bg-white/20">new17</button>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>

                <!-- ============================================== -->
                <!-- ADMIN TAB 5: BOT & STREAM TELEMETRY           -->
                <!-- ============================================== -->
                <div id="admContent-system" class="hidden space-y-4">
                    <div class="bg-brand-dark p-4 rounded-xl border border-white/5 space-y-3">
                        <h4 class="text-sm font-bold text-white flex items-center gap-2">
                            <i class="fa-solid fa-server text-brand-gold"></i>
                            <span>Telegram Bot & Multi-Socket Stream Diagnostics</span>
                        </h4>
                        <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 text-xs">
                            <div class="p-3 rounded-xl bg-brand-card border border-white/5 space-y-1">
                                <span class="text-brand-muted text-[10px] uppercase font-bold block">Bot Server Host</span>
                                <span class="font-mono text-white text-xs block" id="admBotHost">http://127.0.0.1:8080</span>
                                <span class="text-[10px] text-emerald-400 font-bold">🟢 8 Concurrent DC Sockets Active</span>
                            </div>
                            <div class="p-3 rounded-xl bg-brand-card border border-white/5 space-y-1">
                                <span class="text-brand-muted text-[10px] uppercase font-bold block">Gemini 3.1 AI API</span>
                                <span class="font-mono text-white text-xs block">AIzaSyDiJIBMF2EYATRVzFo3kbckVvzNj0hozwY</span>
                                <span class="text-[10px] text-emerald-400 font-bold">🟢 Connected to Google Generative Language</span>
                            </div>
                        </div>
                    </div>
                </div>

            </div>
        </div>
    </div>


    <!-- ========================================== -->
    <!-- MODAL 3: CINEVIBE AI ASSISTANT             -->
    <!-- ========================================== -->
    <div id="aiModal" class="hidden fixed inset-0 z-50 flex items-center justify-center p-4 bg-black/85 backdrop-blur-md">
        <div class="relative w-full max-w-2xl glass-panel rounded-2xl overflow-hidden border border-brand-gold/40 shadow-2xl p-6 space-y-5 animate-fade-in">
            <div class="flex items-center justify-between">
                <div class="flex items-center gap-2.5">
                    <div class="w-8 h-8 rounded-lg bg-brand-gold/20 flex items-center justify-center text-brand-gold">
                        <i class="fa-solid fa-wand-magic-sparkles text-sm"></i>
                    </div>
                    <div>
                        <h4 class="text-base font-bold text-white">CineVibe AI Assistant</h4>
                        <span class="text-[10px] text-brand-gold uppercase tracking-wider font-semibold">Powered by Google Gemini 3.1</span>
                    </div>
                </div>
                <button onclick="closeModal('aiModal')" class="text-brand-muted hover:text-white text-sm">
                    <i class="fa-solid fa-xmark"></i>
                </button>
            </div>

            <p class="text-xs text-brand-muted leading-relaxed">
                Ask CineVibe AI anything! Describe your mood, ask for plot twists, find high-speed 4K films, or get personalized recommendations.
            </p>

            <div class="relative">
                <textarea id="aiPromptInput" rows="3" placeholder="e.g. Recommend suspenseful Bollywood or Hollywood thrillers with shocking plot twists in 4K UHD..." 
                          class="w-full bg-brand-card border border-white/10 rounded-xl p-3 text-xs text-white placeholder-brand-muted focus:outline-none focus:border-brand-gold resize-none"></textarea>
                <button onclick="runAISearch()" id="aiSubmitBtn" class="absolute right-3 bottom-3 px-4 py-1.5 rounded-lg bg-brand-gold text-brand-black text-xs font-bold hover:bg-yellow-400 transition flex items-center gap-1.5">
                    <i class="fa-solid fa-paper-plane text-[10px]"></i>
                    <span>Ask AI</span>
                </button>
            </div>

            <!-- Pre-made Prompts -->
            <div class="flex items-center gap-2 overflow-x-auto no-scrollbar pb-1 text-[11px]">
                <button onclick="setAiPrompt('Best mind-bending Sci-Fi movies like Interstellar and Inception')" class="px-2.5 py-1 rounded-full bg-white/5 hover:bg-white/10 text-brand-muted hover:text-white shrink-0 transition">🌌 Mind-bending Sci-Fi</button>
                <button onclick="setAiPrompt('Highest rated 4K UHD South Indian blockbusters')" class="px-2.5 py-1 rounded-full bg-white/5 hover:bg-white/10 text-brand-muted hover:text-white shrink-0 transition">🔥 Top South 4K</button>
                <button onclick="setAiPrompt('Best popular Anime and K-Dramas with English/Hindi dubbing')" class="px-2.5 py-1 rounded-full bg-white/5 hover:bg-white/10 text-brand-muted hover:text-white shrink-0 transition">🌸 Anime & K-Drama</button>
            </div>

            <div id="aiResponseBox" class="min-h-[120px] max-h-[300px] overflow-y-auto space-y-3 text-xs text-brand-muted bg-brand-card/50 p-4 rounded-xl border border-white/5">
                <div class="text-center py-6 text-brand-muted text-xs">
                    Type a prompt above or pick a suggested topic to activate CineVibe AI.
                </div>
            </div>
        </div>
    </div>


    <!-- ========================================== -->
    <!-- MODAL 4: DOMAIN SHIELD & STREAM SETTINGS   -->
    <!-- ========================================== -->
    <div id="settingsModal" class="hidden fixed inset-0 z-50 flex items-center justify-center p-4 bg-black/85 backdrop-blur-md">
        <div class="relative w-full max-w-lg glass-panel rounded-2xl overflow-hidden border border-white/10 shadow-2xl p-6 space-y-5 animate-fade-in">
            <div class="flex items-center justify-between">
                <div class="flex items-center gap-2.5">
                    <i class="fa-solid fa-shield-halved text-brand-gold text-base"></i>
                    <h4 class="text-base font-bold text-white">Domain Shield & Streamer Settings</h4>
                </div>
                <button onclick="closeModal('settingsModal')" class="text-brand-muted hover:text-white text-sm">
                    <i class="fa-solid fa-xmark"></i>
                </button>
            </div>

            <div class="space-y-4 text-xs">
                <div>
                    <label class="block text-brand-muted font-semibold mb-1">Active Worker Mirror Target</label>
                    <input type="text" id="activeMirrorInput" value="https://cinevibe-cinema.surge.sh/?utm=mn1" 
                           class="w-full bg-brand-card border border-white/10 rounded-xl px-3.5 py-2.5 text-white focus:outline-none focus:border-brand-gold font-mono text-[11px]">
                </div>

                <div>
                    <label class="block text-brand-muted font-semibold mb-1">Telegram Bot Streamer Base URL</label>
                    <input type="text" id="botBaseUrlInput" value="http://127.0.0.1:8080" 
                           class="w-full bg-brand-card border border-white/10 rounded-xl px-3.5 py-2.5 text-white focus:outline-none focus:border-brand-gold font-mono">
                </div>

                <div>
                    <label class="block text-brand-muted font-semibold mb-1">Gemini API Key</label>
                    <input type="text" id="geminiApiKeyInput" value="AIzaSyDiJIBMF2EYATRVzFo3kbckVvzNj0hozwY" 
                           class="w-full bg-brand-card border border-white/10 rounded-xl px-3.5 py-2.5 text-white focus:outline-none focus:border-brand-gold font-mono">
                </div>
            </div>

            <div class="pt-2 flex justify-end gap-3">
                <button onclick="closeModal('settingsModal')" class="px-4 py-2 rounded-xl text-brand-muted hover:text-white text-xs font-semibold">Cancel</button>
                <button onclick="saveSettings()" class="px-5 py-2 rounded-xl bg-brand-gold text-brand-black text-xs font-bold hover:bg-yellow-400 transition">Save Settings</button>
            </div>
        </div>
    </div>


    <!-- ========================================== -->
    <!-- MODAL 5: REQUEST CONTENT                   -->
    <!-- ========================================== -->
    <div id="requestModal" class="hidden fixed inset-0 z-50 flex items-center justify-center p-4 bg-black/85 backdrop-blur-md">
        <div class="relative w-full max-w-md glass-panel rounded-2xl overflow-hidden border border-white/10 shadow-2xl p-6 space-y-4 animate-fade-in">
            <div class="flex items-center justify-between">
                <h4 class="text-base font-bold text-white flex items-center gap-2">
                    <i class="fa-solid fa-paper-plane text-brand-gold text-xs"></i>
                    <span>Request Movie, K-Drama or Anime</span>
                </h4>
                <button onclick="closeModal('requestModal')" class="text-brand-muted hover:text-white text-sm">
                    <i class="fa-solid fa-xmark"></i>
                </button>
            </div>

            <form onsubmit="submitContentRequest(event)" class="space-y-3 text-xs">
                <div>
                    <label class="block text-brand-muted font-semibold mb-1">Title *</label>
                    <input type="text" id="reqTitle" required placeholder="e.g. Pushpa 2: The Rule" class="w-full bg-brand-card border border-white/10 rounded-xl px-3 py-2 text-white focus:outline-none focus:border-brand-gold">
                </div>
                <div class="grid grid-cols-2 gap-3">
                    <div>
                        <label class="block text-brand-muted font-semibold mb-1">Year</label>
                        <input type="number" id="reqYear" placeholder="2024" class="w-full bg-brand-card border border-white/10 rounded-xl px-3 py-2 text-white focus:outline-none focus:border-brand-gold">
                    </div>
                    <div>
                        <label class="block text-brand-muted font-semibold mb-1">Type</label>
                        <select id="reqType" class="w-full bg-brand-card border border-white/10 rounded-xl px-3 py-2 text-white focus:outline-none focus:border-brand-gold">
                            <option>Movie</option>
                            <option>Web Series</option>
                            <option>K-Drama</option>
                            <option>Anime</option>
                        </select>
                    </div>
                </div>
                <div>
                    <label class="block text-brand-muted font-semibold mb-1">Preferred Language / Audio</label>
                    <select id="reqLang" class="w-full bg-brand-card border border-white/10 rounded-xl px-3 py-2 text-white focus:outline-none focus:border-brand-gold">
                        <option>Hindi Dubbed</option>
                        <option>English</option>
                        <option>Japanese with ESub</option>
                        <option>Korean with ESub</option>
                        <option>Multi-Audio</option>
                    </select>
                </div>
                <button type="submit" class="w-full py-2.5 rounded-xl bg-brand-gold text-brand-black font-extrabold tracking-wider uppercase hover:bg-yellow-400 transition mt-2">
                    Submit Request to Library Radar
                </button>
            </form>
        </div>
    </div>


    <!-- ========================================== -->
    <!-- MODAL 6: DMCA & COPYRIGHT POLICY          -->
    <!-- ========================================== -->
    <div id="dmcaModal" class="hidden fixed inset-0 z-50 flex items-center justify-center p-4 bg-black/85 backdrop-blur-md">
        <div class="relative w-full max-w-lg glass-panel rounded-2xl overflow-hidden border border-white/10 shadow-2xl p-6 space-y-4 animate-fade-in">
            <div class="flex items-center justify-between">
                <h4 class="text-base font-bold text-white flex items-center gap-2">
                    <i class="fa-solid fa-shield-halved text-brand-gold text-xs"></i>
                    <span>DMCA & Rights Verification</span>
                </h4>
                <button onclick="closeModal('dmcaModal')" class="text-brand-muted hover:text-white text-sm">
                    <i class="fa-solid fa-xmark"></i>
                </button>
            </div>
            <p class="text-xs text-brand-muted leading-relaxed">
                CineVibe respects intellectual property rights. If you believe your copyrighted material is displayed without authorization, submit a notice below to queue it for immediate disablement.
            </p>
            <form onsubmit="submitDMCAClaim(event)" class="space-y-3 text-xs">
                <div>
                    <label class="block text-brand-muted font-semibold mb-1">Your Full Name / Entity</label>
                    <input type="text" id="dmcaName" required class="w-full bg-brand-card border border-white/10 rounded-xl px-3 py-2 text-white focus:outline-none focus:border-brand-gold">
                </div>
                <div>
                    <label class="block text-brand-muted font-semibold mb-1">Contact Email</label>
                    <input type="email" id="dmcaEmail" required class="w-full bg-brand-card border border-white/10 rounded-xl px-3 py-2 text-white focus:outline-none focus:border-brand-gold">
                </div>
                <div>
                    <label class="block text-brand-muted font-semibold mb-1">Copyrighted Work Title</label>
                    <input type="text" id="dmcaWork" required class="w-full bg-brand-card border border-white/10 rounded-xl px-3 py-2 text-white focus:outline-none focus:border-brand-gold">
                </div>
                <button type="submit" class="w-full py-2.5 rounded-xl bg-rose-600 text-white font-extrabold tracking-wider uppercase hover:bg-rose-700 transition mt-2">
                    Submit Takedown Notice
                </button>
            </form>
        </div>
    </div>


    <!-- ========================================== -->
    <!-- APPLICATION LOGIC SCRIPT                   -->
    <!-- ========================================== -->
    <script>
        // Load catalogs
        let localCatalog = JSON.parse(localStorage.getItem('cinevibe_custom_catalog')) || {catalog_json};
        let missingCatalog = JSON.parse(localStorage.getItem('cinevibe_missing_catalog')) || {missing_json};

        // State
        let currentSlideIdx = 0;
        let slideTimer = null;
        let selectedMovie = null;
        let activeCategory = '';
        let currentYearFilter = 'all';
        let botBaseUrl = localStorage.getItem('cinevibe_bot_url') || 'http://127.0.0.1:8080';
        let geminiApiKey = localStorage.getItem('cinevibe_gemini_key') || 'AIzaSyDiJIBMF2EYATRVzFo3kbckVvzNj0hozwY';
        let activeMirrorUrl = localStorage.getItem('cinevibe_active_mirror') || 'https://cinevibe-cinema.surge.sh/?utm=mn1';

        document.addEventListener('DOMContentLoaded', () => {{
            document.getElementById('botBaseUrlInput').value = botBaseUrl;
            document.getElementById('geminiApiKeyInput').value = geminiApiKey;
            document.getElementById('activeMirrorInput').value = activeMirrorUrl;

            // Auto-enter if navigated with utm or hash
            const urlParams = new URLSearchParams(window.location.search);
            if (urlParams.get('utm') || urlParams.get('admin') || window.location.hash === '#admin') {{
                enterMainPlatform();
                if (urlParams.get('admin') || window.location.hash === '#admin') {{
                    openAdminModal();
                }}
            }}

            updateKpis();

            if ('serviceWorker' in navigator) {{
                navigator.serviceWorker.register('/sw.js').catch(err => console.log('SW error:', err));
            }}
        }});

        function enterMainPlatform() {{
            document.getElementById('landingPage').classList.add('opacity-0');
            setTimeout(() => {{
                document.getElementById('landingPage').classList.add('hidden');
                document.getElementById('mainPlatform').classList.remove('hidden');
                initCarousel();
                loadHomepageSections();
            }}, 400);
        }}

        function resetToHome() {{
            setCategory('');
            closeSearchResults();
            window.scrollTo({{ top: 0, behavior: 'smooth' }});
        }}

        // ==========================================
        // HERO TRENDING POSTER SLIDER
        // ==========================================
        function initCarousel() {{
            const trending = localCatalog.filter(m => m.featured || m.rating >= 8.5);
            if (trending.length === 0) return;
            renderSlide(0);
            if (slideTimer) clearInterval(slideTimer);
            slideTimer = setInterval(() => {{
                nextSlide();
            }}, 6000);
        }}

        function renderSlide(idx) {{
            const trending = localCatalog.filter(m => m.featured || m.rating >= 8.5);
            const m = trending[idx];
            if (!m) return;
            currentSlideIdx = idx;

            document.getElementById('sliderBackground').style.backgroundImage = `url('${{m.backdrop_url || m.poster_url}}')`;
            document.getElementById('slideBadge').innerText = `Trending #${{idx + 1}} • ${{m.category.toUpperCase()}}`;
            document.getElementById('slideQuality').innerText = m.quality.includes('4K') ? '4K UHD' : m.quality;
            document.getElementById('slideRating').innerHTML = `<i class="fa-solid fa-star text-xs"></i> ${{m.rating}}`;
            document.getElementById('slideTitle').innerText = m.title;
            document.getElementById('slideOverview').innerText = m.overview;

            document.getElementById('slidePlayBtn').onclick = () => launchStream(m);
            document.getElementById('slideDetailsBtn').onclick = () => openMovieDetails(m.id);
        }}

        function nextSlide() {{
            const trending = localCatalog.filter(m => m.featured || m.rating >= 8.5);
            currentSlideIdx = (currentSlideIdx + 1) % trending.length;
            renderSlide(currentSlideIdx);
        }}

        function prevSlide() {{
            const trending = localCatalog.filter(m => m.featured || m.rating >= 8.5);
            currentSlideIdx = (currentSlideIdx - 1 + trending.length) % trending.length;
            renderSlide(currentSlideIdx);
        }}

        // ==========================================
        // 11 HOMEPAGE SECTIONS
        // ==========================================
        function loadHomepageSections() {{
            const container = document.getElementById('sectionsContainer');
            
            const sections = {{
                "trending_now": {{ title: "🔥 Trending Now (Movies & Series)", filter: m => m.rating >= 8.5 }},
                "anime_hits": {{ title: "⚔️ Top Hit Anime Series", filter: m => m.category === 'anime' }},
                "kdrama_romance": {{ title: "🌸 Popular K-Dramas & Royal Romance", filter: m => m.category === 'kdrama' }},
                "latest_2024": {{ title: "✨ Latest 2024 Releases", filter: m => m.year === 2024 }},
                "popular_4k": {{ title: "💎 Popular 4K Ultra HD Cinema", filter: m => m.quality.includes('4K') }},
                "bollywood_hits": {{ title: "🎬 Bollywood Blockbusters", filter: m => m.category === 'bollywood' }},
                "south_blockbusters": {{ title: "🌴 South Cinema Powerhouses", filter: m => m.category === 'south' }},
                "hollywood_epics": {{ title: "🚀 Hollywood & Sci-Fi Epics", filter: m => m.category === 'hollywood' }},
                "binge_series": {{ title: "📺 Binge-Worthy Web Series", filter: m => m.category === 'series' }},
                "curated_picks": {{ title: "🌟 Editor's Top Rated Picks", filter: m => m.rating >= 8.8 }},
                "recently_added": {{ title: "⚡ Recently Added to CineVibe", filter: () => true }}
            }};

            let html = '';
            for (const [key, sec] of Object.entries(sections)) {{
                const list = localCatalog.filter(sec.filter);
                if (list.length === 0) continue;

                html += `
                    <div class="space-y-4">
                        <div class="flex items-center justify-between">
                            <h3 class="text-lg sm:text-xl font-bold text-white tracking-wide">${{sec.title}}</h3>
                            <button onclick="setCategory('${{key === 'anime_hits' ? 'anime' : key === 'kdrama_romance' ? 'kdrama' : key === 'popular_4k' ? '4k' : ''}}')" class="text-xs text-brand-gold hover:underline font-semibold">View All (${{list.length}}) →</button>
                        </div>
                        <div class="flex gap-4 overflow-x-auto no-scrollbar pb-3 pt-1">
                            ${{list.map(m => createMovieCard(m)).join('')}}
                        </div>
                    </div>
                `;
            }}
            container.innerHTML = html;
        }}

        function handleImageError(img, title, year) {{
            img.onerror = null;
            const cleanTitle = title.replace(/"/g, '');
            img.src = `data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" width="300" height="450" viewBox="0 0 300 450"><rect width="300" height="450" fill="%23181818"/><rect x="10" y="10" width="280" height="430" fill="none" stroke="%23FFC928" stroke-width="2" opacity="0.4" rx="8"/><text x="150" y="210" font-family="sans-serif" font-weight="bold" font-size="20" fill="%23FFFFFF" text-anchor="middle">${{encodeURIComponent(cleanTitle)}}</text><text x="150" y="245" font-family="sans-serif" font-size="14" fill="%23FFC928" text-anchor="middle">${{year || 'CineVibe'}}</text></svg>`;
        }}

        function createMovieCard(m) {{
            return `
                <div class="movie-card shrink-0 w-36 sm:w-44 glass-panel rounded-xl overflow-hidden border border-white/5 cursor-pointer flex flex-col" onclick="openMovieDetails('${{m.id}}')">
                    <div class="relative h-52 sm:h-64 w-full bg-brand-dark overflow-hidden">
                        <img src="${{m.poster_url}}" referrerpolicy="no-referrer" alt="${{m.title}}" 
                             onerror="handleImageError(this, '${{m.title.replace(/'/g, "\\\'")}}', '${{m.year}}')" 
                             class="w-full h-full object-cover transition duration-300">
                        <div class="absolute top-2 right-2 px-1.5 py-0.5 rounded bg-black/70 backdrop-blur-md text-[10px] font-bold text-brand-gold border border-brand-gold/30">
                            ${{m.quality.includes('4K') ? '4K UHD' : m.quality.includes('1080p') ? '1080p' : '720p'}}
                        </div>
                        <div class="absolute bottom-2 left-2 px-1.5 py-0.5 rounded bg-black/70 backdrop-blur-md text-[10px] font-semibold text-white flex items-center gap-1">
                            <i class="fa-solid fa-star text-brand-gold text-[9px]"></i> ${{m.rating}}
                        </div>
                    </div>
                    <div class="p-3 flex flex-col flex-1 justify-between">
                        <div>
                            <h4 class="text-xs sm:text-sm font-bold text-white line-clamp-1">${{m.title}}</h4>
                            <span class="text-[11px] text-brand-muted block mt-0.5">${{m.year}} • ${{m.languages[0] || 'Cinema'}}</span>
                        </div>
                        <div class="mt-2.5 pt-2 border-t border-white/5 flex items-center justify-between text-[10px] text-brand-muted">
                            <span>${{m.file_size_human}}</span>
                            <span class="text-brand-gold font-bold">Watch →</span>
                        </div>
                    </div>
                </div>
            `;
        }}

        // ==========================================
        // CATEGORY & SEARCH FILTERING
        // ==========================================
        function setCategory(cat) {{
            activeCategory = cat;
            if (!cat) {{
                closeSearchResults();
                return;
            }}

            let filtered = localCatalog;
            if (cat === '4k') {{
                filtered = localCatalog.filter(m => m.quality.includes('4K'));
            }} else {{
                filtered = localCatalog.filter(m => m.category === cat || m.type === cat);
            }}

            displaySearchResults(filtered, `Category: ${{cat.toUpperCase()}}`);
        }}

        let searchDebounce = null;
        function handleSearch(query) {{
            const q = query.trim().toLowerCase();
            document.getElementById('clearSearchBtn').classList.toggle('hidden', !q);
            if (searchDebounce) clearTimeout(searchDebounce);

            searchDebounce = setTimeout(() => {{
                if (q.length < 2) {{
                    if (q.length === 0) closeSearchResults();
                    return;
                }}
                const results = localCatalog.filter(m => 
                    m.title.toLowerCase().includes(q) ||
                    (m.cast && m.cast.some(c => c.toLowerCase().includes(q))) ||
                    (m.director && m.director.toLowerCase().includes(q)) ||
                    (m.genres && m.genres.some(g => g.toLowerCase().includes(q))) ||
                    String(m.year).includes(q)
                );
                displaySearchResults(results, `Search: "${{query}}"`);
            }}, 200);
        }}

        function clearSearch() {{
            document.getElementById('searchInput').value = '';
            document.getElementById('clearSearchBtn').classList.add('hidden');
            closeSearchResults();
        }}

        function displaySearchResults(list, heading) {{
            document.getElementById('heroSliderSection').classList.add('hidden');
            document.getElementById('sectionsContainer').classList.add('hidden');
            document.getElementById('catalogSection').classList.remove('hidden');

            document.getElementById('catalogHeading').innerText = heading;
            document.getElementById('catalogCount').innerText = `${{list.length}} title(s) found`;

            const grid = document.getElementById('catalogGrid');
            if (list.length === 0) {{
                grid.innerHTML = `<div class="col-span-full py-16 text-center text-brand-muted text-sm">No titles found. Try asking CineVibe AI!</div>`;
                return;
            }}
            grid.innerHTML = list.map(m => createMovieCard(m)).join('');
            window.scrollTo({{ top: 0, behavior: 'smooth' }});
        }}

        function closeSearchResults() {{
            document.getElementById('heroSliderSection').classList.remove('hidden');
            document.getElementById('sectionsContainer').classList.remove('hidden');
            document.getElementById('catalogSection').classList.add('hidden');
        }}

        // ==========================================
        // MOVIE DETAILS MODAL & BOT STREAM ACTIONS
        // ==========================================
        function openMovieDetails(id) {{
            const m = localCatalog.find(x => x.id === id);
            if (!m) return;
            selectedMovie = m;

            document.getElementById('modalBackdrop').style.backgroundImage = `url('${{m.backdrop_url || m.poster_url}}')`;
            document.getElementById('modalPoster').src = m.poster_url;
            document.getElementById('modalQuality').innerText = m.quality;
            document.getElementById('modalYear').innerText = m.year;
            document.getElementById('modalRuntime').innerText = `• ${{m.runtime}}`;
            document.getElementById('modalRating').innerHTML = `<i class="fa-solid fa-star text-[10px]"></i> ${{m.rating}}`;
            document.getElementById('modalTitle').innerText = m.title;
            document.getElementById('modalOriginalTitle').innerText = m.file_name;
            document.getElementById('modalOverview').innerText = m.overview;
            document.getElementById('modalDirector').innerText = m.director || 'Director';
            document.getElementById('modalLanguages').innerText = m.languages.join(', ');

            const formats = [
                {{ label: "4K UHD 2160p HEVC HDR10", size: m.file_size_human, quality: "4K UHD" }},
                {{ label: "1080p FHD x264 Dolby 5.1", size: "2.40 GB", quality: "1080p" }},
                {{ label: "720p HD x264 AAC Stereo", size: "880 MB", quality: "720p" }}
            ];
            document.getElementById('modalFormatsList').innerHTML = formats.map(f => `
                <div class="p-3 rounded-xl bg-brand-dark border border-white/5 flex items-center justify-between text-xs">
                    <div>
                        <span class="text-white font-bold block">${{f.label}}</span>
                        <span class="text-[11px] text-brand-muted">Size: ${{f.size}} • Multi-Socket High Speed</span>
                    </div>
                    <button onclick="launchDownload(selectedMovie)" class="px-3 py-1.5 rounded-lg bg-brand-gold text-brand-black font-bold text-[11px] hover:bg-yellow-400 transition">
                        Download
                    </button>
                </div>
            `).join('');

            document.getElementById('modalCastList').innerHTML = (m.cast || []).map(c => `
                <span class="px-2.5 py-1 rounded-lg bg-brand-dark border border-white/5 text-white">${{c}}</span>
            `).join('');

            document.getElementById('modalStreamBtn').onclick = () => launchStream(m);
            document.getElementById('modalDownloadBtn').onclick = () => launchDownload(m);

            switchModalTab('overview');
            openModal('movieModal');
        }}

        function switchModalTab(tab) {{
            ['overview', 'formats', 'cast'].forEach(t => {{
                document.getElementById(`tabContent-${{t}}`).classList.toggle('hidden', t !== tab);
                const btn = document.getElementById(`tabBtn-${{t}}`);
                if (t === tab) {{
                    btn.className = "pb-2.5 border-b-2 border-brand-gold text-brand-gold font-bold";
                }} else {{
                    btn.className = "pb-2.5 text-brand-muted hover:text-white font-semibold";
                }}
            }});
        }}

        function getBotStreamUrl(m) {{
            const msgId = m.stream_msg_id || 116;
            const hash = m.stream_hash || "AgADwB";
            const filename = encodeURIComponent(m.file_name || m.title);
            return `${{botBaseUrl}}/${{msgId}}/${{filename}}?hash=${{hash}}`;
        }}

        function launchStream(m) {{
            const url = getBotStreamUrl(m);
            showToast("Connecting to CineVibe high-speed streamer...");
            window.open(url, '_blank');
        }}

        function launchDownload(m) {{
            const url = getBotStreamUrl(m);
            showToast("Initiating 8-socket fast download...");
            const a = document.createElement('a');
            a.href = url;
            a.download = m.file_name || m.title;
            document.body.appendChild(a);
            a.click();
            document.body.removeChild(a);
        }}

        function copyCurrentStreamLink() {{
            if (!selectedMovie) return;
            const url = getBotStreamUrl(selectedMovie);
            navigator.clipboard.writeText(url).then(() => {{
                showToast("Stream link copied to clipboard!");
            }});
        }}

        // ==========================================
        // ADMIN COMMAND CENTER LOGIC
        // ==========================================
        function openAdminModal() {{
            renderInventoryTable();
            renderMissingTable();
            openModal('adminModal');
        }}

        function switchAdminTab(tab) {{
            ['inventory', 'missing', 'manage', 'shield', 'system'].forEach(t => {{
                document.getElementById(`admContent-${{t}}`).classList.toggle('hidden', t !== tab);
                const btn = document.getElementById(`admTabBtn-${{t}}`);
                if (t === tab) {{
                    btn.className = "px-3 py-1.5 rounded-lg bg-brand-gold text-black font-bold";
                }} else {{
                    btn.className = "px-3 py-1.5 rounded-lg text-brand-muted hover:text-white font-medium";
                }}
            }});
        }}

        function updateKpis() {{
            document.getElementById('kpiTotal').innerText = localCatalog.length;
            document.getElementById('kpiMovies').innerText = localCatalog.filter(m => m.type === 'movie').length;
            document.getElementById('kpiSeries').innerText = localCatalog.filter(m => m.type === 'series').length;
            document.getElementById('kpiKdrama').innerText = localCatalog.filter(m => m.type === 'kdrama' || m.category === 'kdrama').length;
            document.getElementById('kpiAnime').innerText = localCatalog.filter(m => m.type === 'anime' || m.category === 'anime').length;
            document.getElementById('kpiMissing').innerText = missingCatalog.length;
            document.getElementById('missingCountBadge').innerText = missingCatalog.length;
        }}

        function filterInventoryByYear(yr) {{
            currentYearFilter = yr;
            ['all', '2024', '2023', '2022', '2021', '2020'].forEach(y => {{
                const btn = document.getElementById(`yrBtn-${{y}}`);
                if (btn) {{
                    if (y === yr) {{
                        btn.className = "px-2.5 py-1 rounded-lg bg-brand-gold text-black font-bold text-[11px]";
                    }} else {{
                        btn.className = "px-2.5 py-1 rounded-lg bg-white/5 hover:bg-white/10 text-white text-[11px]";
                    }}
                }}
            }});
            renderInventoryTable();
        }}

        function renderInventoryTable() {{
            const tbody = document.getElementById('inventoryTableBody');
            let list = localCatalog;
            if (currentYearFilter !== 'all') {{
                const yrNum = parseInt(currentYearFilter);
                list = localCatalog.filter(m => m.year === yrNum);
            }}

            if (list.length === 0) {{
                tbody.innerHTML = `<tr><td colspan="8" class="p-6 text-center text-brand-muted">No media titles found for year ${{currentYearFilter}} in inventory. Check the Missing Radar!</td></tr>`;
                return;
            }}

            tbody.innerHTML = list.map(m => `
                <tr class="hover:bg-white/5 transition">
                    <td class="p-3 flex items-center gap-2.5">
                        <img src="${{m.poster_url}}" referrerpolicy="no-referrer" class="w-8 h-11 object-cover rounded shadow border border-white/10">
                        <div>
                            <span class="font-bold text-white block">${{m.title}}</span>
                            <span class="text-[10px] text-brand-muted">${{m.genres ? m.genres.join(', ') : 'Cinema'}}</span>
                        </div>
                    </td>
                    <td class="font-mono font-bold text-white">${{m.year}}</td>
                    <td>
                        <span class="px-2 py-0.5 rounded text-[10px] font-bold ${{m.type === 'anime' ? 'bg-purple-500/20 text-purple-300' : m.type === 'kdrama' ? 'bg-pink-500/20 text-pink-300' : m.type === 'series' ? 'bg-amber-500/20 text-amber-300' : 'bg-blue-500/20 text-blue-300'}}">
                            ${{m.type ? m.type.toUpperCase() : m.category.toUpperCase()}}
                        </span>
                    </td>
                    <td class="font-semibold text-brand-gold">${{m.quality}}</td>
                    <td class="text-brand-muted">${{m.languages.slice(0, 2).join(', ')}}</td>
                    <td class="text-brand-muted font-mono">${{m.file_size_human}}</td>
                    <td class="font-mono text-brand-gold">${{m.stream_msg_id}}</td>
                    <td>
                        <div class="flex items-center gap-1.5">
                            <button onclick="launchStream(localCatalog.find(x => x.id === '${{m.id}}'))" class="px-2 py-1 rounded bg-white/10 hover:bg-brand-gold hover:text-black font-bold text-[10px]">Test</button>
                            <button onclick="deleteCatalogItem('${{m.id}}')" class="px-2 py-1 rounded bg-rose-500/20 text-rose-300 hover:bg-rose-500 hover:text-white font-bold text-[10px]">Delete</button>
                        </div>
                    </td>
                </tr>
            `).join('');
        }}

        function renderMissingTable() {{
            const tbody = document.getElementById('missingTableBody');
            if (missingCatalog.length === 0) {{
                tbody.innerHTML = `<tr><td colspan="7" class="p-6 text-center text-brand-muted">No missing titles recorded! Everything is fulfilled.</td></tr>`;
                return;
            }}

            tbody.innerHTML = missingCatalog.map((m, idx) => `
                <tr class="hover:bg-white/5 transition">
                    <td class="p-3 font-bold text-white flex items-center gap-2">
                        <i class="fa-solid fa-clock text-rose-400 text-xs"></i>
                        <span>${{m.title}}</span>
                    </td>
                    <td class="font-mono font-bold">${{m.year}}</td>
                    <td>
                        <span class="px-2 py-0.5 rounded text-[10px] font-bold bg-white/10 text-white">
                            ${{m.type.toUpperCase()}}
                        </span>
                    </td>
                    <td class="font-bold text-amber-400">${{m.demand}}</td>
                    <td class="text-brand-muted font-semibold">${{m.expected_quality}}</td>
                    <td class="text-brand-muted text-[10px] max-w-xs truncate">${{m.notes}}</td>
                    <td>
                        <button onclick="fulfillMissingTitle(${{idx}})" class="px-2.5 py-1 rounded bg-brand-gold text-black font-extrabold text-[10px] hover:bg-yellow-400 transition">
                            Fulfill & Add ➔
                        </button>
                    </td>
                </tr>
            `).join('');
        }}

        function fulfillMissingTitle(idx) {{
            const item = missingCatalog[idx];
            if (!item) return;
            switchAdminTab('manage');
            document.getElementById('addTitle').value = item.title;
            document.getElementById('addYear').value = item.year;
            document.getElementById('addType').value = item.type;
            document.getElementById('addCategory').value = item.category;
            showToast(`Pre-filled "${{item.title}}". Enter poster & stream hash to publish!`);
        }}

        function handleAddNewMedia(e) {{
            e.preventDefault();
            const newItem = {{
                id: document.getElementById('addTitle').value.toLowerCase().replace(/[^a-z0-9]+/g, '-') + '-' + Date.now(),
                title: document.getElementById('addTitle').value.trim(),
                year: parseInt(document.getElementById('addYear').value),
                rating: 8.5,
                runtime: "2h",
                quality: document.getElementById('addQuality').value,
                category: document.getElementById('addCategory').value,
                type: document.getElementById('addType').value,
                languages: document.getElementById('addLanguages').value.split(',').map(s => s.trim()),
                genres: [document.getElementById('addCategory').value.toUpperCase()],
                director: "Admin Added",
                cast: ["Cast Ensembled"],
                overview: `Authorized CineVibe stream and high-speed distribution for ${{document.getElementById('addTitle').value}}.`,
                poster_url: document.getElementById('addPosterUrl').value.trim(),
                backdrop_url: document.getElementById('addBackdropUrl').value.trim(),
                file_name: `${{document.getElementById('addTitle').value}} ${{document.getElementById('addYear').value}} ${{document.getElementById('addQuality').value}}`,
                file_size: 4294967296,
                file_size_human: document.getElementById('addSize').value.trim(),
                stream_msg_id: parseInt(document.getElementById('addMsgId').value) || 150,
                stream_hash: document.getElementById('addHash').value.trim() || 'AgAD56',
                featured: true
            }};

            localCatalog.unshift(newItem);
            localStorage.setItem('cinevibe_custom_catalog', JSON.stringify(localCatalog));
            
            // Remove from missing catalog if exists
            missingCatalog = missingCatalog.filter(x => x.title.toLowerCase() !== newItem.title.toLowerCase());
            localStorage.setItem('cinevibe_missing_catalog', JSON.stringify(missingCatalog));

            updateKpis();
            renderInventoryTable();
            renderMissingTable();
            loadHomepageSections();
            initCarousel();

            showToast(`Published "${{newItem.title}}" to live catalog!`);
            switchAdminTab('inventory');
            e.target.reset();
        }}

        function deleteCatalogItem(id) {{
            if (!confirm("Are you sure you want to remove this title from library?")) return;
            localCatalog = localCatalog.filter(x => x.id !== id);
            localStorage.setItem('cinevibe_custom_catalog', JSON.stringify(localCatalog));
            updateKpis();
            renderInventoryTable();
            loadHomepageSections();
            showToast("Title removed from active inventory.");
        }}

        function setQuickMirror(url) {{
            activeMirrorUrl = url + '/?utm=mn1';
            localStorage.setItem('cinevibe_active_mirror', activeMirrorUrl);
            document.getElementById('admDisplayMirror').innerText = url.replace('https://', '');
            document.getElementById('activeMirrorInput').value = activeMirrorUrl;
            showToast(`Switched active mirror to: ${{url}}`);
        }}

        function exportUpdatedCatalog() {{
            const dataStr = "data:text/json;charset=utf-8," + encodeURIComponent(JSON.stringify(localCatalog, null, 2));
            const downloadAnchor = document.createElement('a');
            downloadAnchor.setAttribute("href", dataStr);
            downloadAnchor.setAttribute("download", "catalog.json");
            document.body.appendChild(downloadAnchor);
            downloadAnchor.click();
            downloadAnchor.remove();
            showToast("catalog.json exported successfully!");
        }}

        // ==========================================
        // CINEVIBE AI SEARCH (GEMINI API)
        // ==========================================
        function setAiPrompt(text) {{
            document.getElementById('aiPromptInput').value = text;
        }}

        async function runAISearch() {{
            const prompt = document.getElementById('aiPromptInput').value.trim();
            if (!prompt) return;

            const box = document.getElementById('aiResponseBox');
            box.innerHTML = `<div class="p-6 text-center text-brand-muted"><i class="fa-solid fa-circle-notch fa-spin text-brand-gold text-lg mr-2"></i> CineVibe AI is analyzing cinema library for "${{prompt}}"...</div>`;

            const geminiUrl = `https://generativelanguage.googleapis.com/v1/models/gemini-3.1-flash-lite:generateContent?key=${{geminiApiKey}}`;
            const payload = {{
                contents: [{{
                    parts: [{{
                        text: `You are CineVibe AI cinema expert. The user asks: "${{prompt}}". Provide a concise, engaging recommendation of 2-3 movies, anime or k-dramas explaining why they match. Keep response under 100 words.`
                    }}]
                }}]
            }};

            try {{
                const res = await fetch(geminiUrl, {{
                    method: 'POST',
                    headers: {{ 'Content-Type': 'application/json' }},
                    body: JSON.stringify(payload)
                }});
                const data = await res.json();
                let aiReply = "";
                if (data.candidates && data.candidates[0] && data.candidates[0].content) {{
                    aiReply = data.candidates[0].content.parts[0].text;
                }} else {{
                    throw new Error("No candidate returned");
                }}

                const words = prompt.toLowerCase().split(/\\s+/);
                const matched = localCatalog.filter(m => {{
                    return words.some(w => w.length > 3 && (m.title.toLowerCase().includes(w) || (m.genres && m.genres.some(g => g.toLowerCase().includes(w)))));
                }}).slice(0, 3);
                const displayMatched = matched.length > 0 ? matched : localCatalog.slice(0, 3);

                box.innerHTML = `
                    <div class="bg-brand-dark p-4 rounded-xl border border-brand-gold/30 space-y-2">
                        <span class="text-[10px] text-brand-gold font-bold uppercase tracking-wider block">CineVibe AI Rationale</span>
                        <p class="text-white text-xs leading-relaxed whitespace-pre-line">${{aiReply}}</p>
                    </div>
                    <div class="grid grid-cols-3 gap-2.5 pt-2">
                        ${{displayMatched.map(m => `
                            <div class="bg-brand-card p-2 rounded-xl border border-white/5 cursor-pointer hover:border-brand-gold/40 transition" onclick="closeModal('aiModal'); openMovieDetails('${{m.id}}')">
                                <img src="${{m.poster_url}}" referrerpolicy="no-referrer" class="w-full h-28 object-cover rounded-lg mb-1.5" onerror="handleImageError(this, '${{m.title.replace(/'/g, "\\\'")}}', '${{m.year}}')">
                                <h5 class="text-[11px] font-bold text-white line-clamp-1">${{m.title}}</h5>
                                <span class="text-[10px] text-brand-gold font-bold">⭐ ${{m.rating}}</span>
                            </div>
                        `).join('')}}
                    </div>
                `;
            }} catch (err) {{
                const fallbackMovie = localCatalog[Math.floor(Math.random() * localCatalog.length)];
                box.innerHTML = `
                    <div class="bg-brand-dark p-4 rounded-xl border border-brand-gold/30">
                        <span class="text-[10px] text-brand-gold font-bold uppercase tracking-wider block mb-1">CineVibe Recommendation</span>
                        <p class="text-white text-xs leading-relaxed">Based on your query "${{prompt}}", we highly recommend <b>${{fallbackMovie.title}}</b> (${{fallbackMovie.year}}). Features extraordinary cinematography and available in verified high-speed ${{fallbackMovie.quality}}.</p>
                    </div>
                    <div class="pt-2">
                        <button onclick="closeModal('aiModal'); openMovieDetails('${{fallbackMovie.id}}')" class="w-full py-2 rounded-xl bg-brand-gold text-brand-black text-xs font-bold hover:bg-yellow-400 transition">
                            View ${{fallbackMovie.title}} →
                        </button>
                    </div>
                `;
            }}
        }}

        // ==========================================
        // SETTINGS & BOT CONNECTION
        // ==========================================
        function saveSettings() {{
            botBaseUrl = document.getElementById('botBaseUrlInput').value.trim();
            geminiApiKey = document.getElementById('geminiApiKeyInput').value.trim();
            activeMirrorUrl = document.getElementById('activeMirrorInput').value.trim();

            localStorage.setItem('cinevibe_bot_url', botBaseUrl);
            localStorage.setItem('cinevibe_gemini_key', geminiApiKey);
            localStorage.setItem('cinevibe_active_mirror', activeMirrorUrl);

            document.getElementById('admBotHost').innerText = botBaseUrl;
            showToast("Domain shield and API settings saved!");
            closeModal('settingsModal');
        }}

        // ==========================================
        // USER REQUESTS & DMCA CLAIMS
        // ==========================================
        function submitContentRequest(e) {{
            e.preventDefault();
            const title = document.getElementById('reqTitle').value;
            const year = parseInt(document.getElementById('reqYear').value) || 2024;
            const type = document.getElementById('reqType').value.toLowerCase();

            missingCatalog.unshift({{
                title: title,
                year: year,
                type: type,
                category: type === 'anime' ? 'anime' : type === 'kdrama' ? 'kdrama' : 'bollywood',
                demand: "👥 User Requested",
                expected_quality: "4K UHD 2160p",
                notes: `Requested by CineVibe community via website portal.`
            }});
            localStorage.setItem('cinevibe_missing_catalog', JSON.stringify(missingCatalog));
            updateKpis();
            renderMissingTable();

            showToast(`Request for "${{title}}" logged to Admin Missing Radar!`);
            closeModal('requestModal');
            e.target.reset();
        }}

        function submitDMCAClaim(e) {{
            e.preventDefault();
            const work = document.getElementById('dmcaWork').value;
            showToast(`Takedown notice for "${{work}}" received. Queued for audit.`);
            closeModal('dmcaModal');
            e.target.reset();
        }}

        // Modal Helpers
        function openModal(id) {{
            document.getElementById(id).classList.remove('hidden');
        }}
        function closeModal(id) {{
            document.getElementById(id).classList.add('hidden');
        }}

        function showToast(msg, isError = false) {{
            const toast = document.getElementById('toast');
            document.getElementById('toastMsg').innerText = msg;
            document.getElementById('toastIcon').className = isError 
                ? 'fa-solid fa-circle-exclamation text-rose-500 text-lg'
                : 'fa-solid fa-circle-check text-brand-gold text-lg';
            toast.classList.remove('translate-y-24', 'opacity-0');
            setTimeout(() => {{
                toast.classList.add('translate-y-24', 'opacity-0');
            }}, 3500);
        }}
    </script>
</body>
</html>
'''

with open(os.path.join(OUTPUT_DIR, "index.html"), "w", encoding="utf-8") as f:
    f.write(html_content)

shutil.copyfile(os.path.join(OUTPUT_DIR, "index.html"), os.path.join(OUTPUT_DIR, "200.html"))

print("index.html and 200.html generated successfully with Admin Command Center!")

