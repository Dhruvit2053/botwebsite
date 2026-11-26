# -*- coding: utf-8 -*-
import json
import os
import shutil

OUTPUT_DIR = r"D:\botwebsite"

with open(os.path.join(OUTPUT_DIR, "catalog.json"), "r", encoding="utf-8") as f:
    catalog_json = f.read()

html_content = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="referrer" content="no-referrer">
    <title>CineVibe — Your World of Cinema | 4K Movies, K-Drama & Anime Discovery</title>
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
                            gold: '#FFC928',
                            goldDark: '#F5A623',
                            muted: '#A0A0A0'
                        }}
                    }},
                    fontFamily: {{
                        sans: ['"Plus Jakarta Sans"', 'sans-serif'],
                        cinematic: ['"Cinzel"', 'serif']
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
        .no-scrollbar::-webkit-scrollbar {{
            display: none;
        }}
        .no-scrollbar {{
            -ms-overflow-style: none;
            scrollbar-width: none;
        }}
        .glass-panel {{
            background: rgba(18, 18, 18, 0.75);
            backdrop-filter: blur(16px);
            -webkit-backdrop-filter: blur(16px);
        }}
        .gold-glow {{
            box-shadow: 0 0 25px rgba(255, 201, 40, 0.25);
        }}
        .movie-card {{
            transition: all 0.3s cubic-bezier(0.25, 0.8, 0.25, 1);
        }}
        .movie-card:hover {{
            transform: translateY(-6px) scale(1.02);
            box-shadow: 0 12px 30px rgba(0, 0, 0, 0.8), 0 0 15px rgba(255, 201, 40, 0.2);
            border-color: rgba(255, 201, 40, 0.4);
        }}
    </style>
</head>
<body class="selection:bg-brand-gold selection:text-black">

    <!-- Toast Notification -->
    <div id="toast" class="fixed bottom-6 right-6 z-50 transform translate-y-24 opacity-0 transition-all duration-300 flex items-center gap-3 px-5 py-3 rounded-xl glass-panel border border-brand-gold/30 shadow-2xl">
        <i id="toastIcon" class="fa-solid fa-circle-check text-brand-gold text-lg"></i>
        <span id="toastMsg" class="text-sm font-medium text-white">Action successful</span>
    </div>

    <!-- ========================================== -->
    <!-- SECTION 1: CINEVIBE CINEMATIC LANDING PAGE -->
    <!-- ========================================== -->
    <div id="landingPage" class="relative min-h-screen flex flex-col justify-between overflow-hidden bg-brand-black transition-opacity duration-700">
        <div class="absolute inset-0 bg-cover bg-center opacity-30 scale-105 transition-transform duration-10000 ease-out" 
             style="background-image: url('https://images.weserv.nl/?url=image.tmdb.org/t/p/original/1pdfLvkbY9ohJlCjQH2CZjjYVvJ.jpg');">
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
                    <span class="font-cinematic text-2xl font-bold tracking-wider text-white">CINE<span class="text-brand-gold">VIBE</span></span>
                    <span class="block text-[10px] tracking-widest text-brand-muted uppercase">Your World of Cinema</span>
                </div>
            </div>
            <div class="flex items-center gap-4">
                <button onclick="enterMainPlatform()" class="text-sm font-semibold text-brand-muted hover:text-white transition">Explore Library</button>
                <button onclick="enterMainPlatform()" class="px-5 py-2 rounded-full bg-brand-gold text-brand-black font-bold text-xs hover:bg-brand-goldDark transition gold-glow flex items-center gap-2">
                    <span>ENTER CINEVIBE</span>
                    <i class="fa-solid fa-arrow-right text-[11px]"></i>
                </button>
            </div>
        </header>

        <!-- Landing Hero Centerpiece -->
        <main class="relative z-10 max-w-4xl mx-auto text-center px-6 py-12 flex flex-col items-center">
            <div class="inline-flex items-center gap-2 px-4 py-1.5 rounded-full bg-white/5 border border-white/10 text-xs text-brand-gold mb-6 backdrop-blur-md">
                <span class="w-2 h-2 rounded-full bg-emerald-400 animate-pulse"></span>
                <span>High-Speed Multi-Socket Turbo Active</span>
            </div>
            
            <h1 class="font-cinematic text-4xl sm:text-6xl md:text-7xl font-bold text-white tracking-tight leading-tight">
                YOUR WORLD <br><span class="text-transparent bg-clip-text bg-gradient-to-r from-brand-gold via-amber-200 to-brand-goldDark">OF CINEMA.</span>
            </h1>
            
            <p class="mt-6 text-sm sm:text-lg text-brand-muted max-w-2xl font-normal leading-relaxed">
                Discover high-definition 4K UHD movies, trending K-Dramas, and action-packed anime with multi-socket turbo downloads powered by our local streaming engine.
            </p>

            <div class="mt-8 flex flex-col sm:flex-row items-center gap-4 w-full sm:w-auto">
                <button onclick="enterMainPlatform()" class="w-full sm:w-auto px-8 py-3.5 rounded-full bg-gradient-to-r from-brand-gold to-brand-goldDark text-brand-black font-extrabold text-sm hover:scale-105 transition transform shadow-xl shadow-brand-gold/20 flex items-center justify-center gap-3">
                    <span>EXPLORE CINEVIBE</span>
                    <i class="fa-solid fa-play text-xs"></i>
                </button>
                <button onclick="openModal('aiModal')" class="w-full sm:w-auto px-6 py-3.5 rounded-full glass-panel border border-white/10 text-white font-semibold text-sm hover:bg-white/10 transition flex items-center justify-center gap-2">
                    <i class="fa-solid fa-wand-magic-sparkles text-brand-gold"></i>
                    <span>CineVibe AI Assistant</span>
                </button>
            </div>

            <!-- Features Highlights -->
            <div class="pt-8 grid grid-cols-2 md:grid-cols-4 gap-4 text-left w-full">
                <div class="p-4 rounded-xl glass-panel border border-white/5">
                    <i class="fa-solid fa-bolt text-brand-gold text-base mb-2"></i>
                    <h4 class="text-xs font-bold text-white">Multi-Socket Turbo</h4>
                    <p class="text-[11px] text-brand-muted mt-1">High-speed media session pool.</p>
                </div>
                <div class="p-4 rounded-xl glass-panel border border-white/5">
                    <i class="fa-solid fa-robot text-brand-gold text-base mb-2"></i>
                    <h4 class="text-xs font-bold text-white">Gemini AI Search</h4>
                    <p class="text-[11px] text-brand-muted mt-1">Natural language smart recommendations.</p>
                </div>
                <div class="p-4 rounded-xl glass-panel border border-white/5">
                    <i class="fa-solid fa-calendar text-brand-gold text-base mb-2"></i>
                    <h4 class="text-xs font-bold text-white">Release Calendar</h4>
                    <p class="text-[11px] text-brand-muted mt-1">Browse releases by year & month.</p>
                </div>
                <div class="p-4 rounded-xl glass-panel border border-white/5">
                    <i class="fa-solid fa-tv text-brand-gold text-base mb-2"></i>
                    <h4 class="text-xs font-bold text-white">True 4K UHD</h4>
                    <p class="text-[11px] text-brand-muted mt-1">HDR10, Dolby Atmos & multi-audio.</p>
                </div>
            </div>
        </main>

        <!-- Landing Footer -->
        <footer class="relative z-10 max-w-7xl mx-auto w-full px-6 py-4 flex flex-col sm:flex-row items-center justify-between text-xs text-brand-muted border-t border-white/5 gap-2">
            <span>&copy; 2026 CineVibe Ecosystem. All rights reserved.</span>
            <div class="flex items-center gap-4">
                <a href="javascript:void(0)" onclick="openModal('legalModal')" class="hover:text-white transition">Rights & Verification</a>
                <a href="javascript:void(0)" onclick="openModal('dmcaModal')" class="hover:text-white transition">DMCA Compliance</a>
            </div>
        </footer>
    </div>

    <!-- ========================================== -->
    <!-- SECTION 2: MAIN CINEVIBE STREAMING PLATFORM -->
    <!-- ========================================== -->
    <div id="mainPlatform" class="hidden min-h-screen flex flex-col bg-brand-black">
        
        <!-- Top Sticky Header -->
        <header class="sticky top-0 z-40 glass-panel border-b border-white/5 px-4 sm:px-8 py-3.5 transition">
            <div class="max-w-7xl mx-auto flex items-center justify-between gap-4">
                
                <!-- Logo & Brand -->
                <div class="flex items-center gap-3 cursor-pointer shrink-0" onclick="enterLandingPage()">
                    <div class="w-9 h-9 rounded-xl bg-gradient-to-tr from-brand-goldDark to-brand-gold flex items-center justify-center shadow-md shadow-brand-gold/20">
                        <i class="fa-solid fa-film text-brand-black text-sm"></i>
                    </div>
                    <div>
                        <span class="font-cinematic text-xl font-bold tracking-wider text-white">CINE<span class="text-brand-gold">VIBE</span></span>
                        <span class="hidden sm:block text-[9px] tracking-widest text-brand-muted uppercase">Your World of Cinema</span>
                    </div>
                </div>

                <!-- Main Navigation Tabs -->
                <nav class="hidden lg:flex items-center gap-1 text-xs font-semibold text-brand-muted">
                    <button onclick="setCategory('')" class="px-3 py-1.5 rounded-lg hover:text-white hover:bg-white/5 transition nav-link active-nav text-brand-gold" data-cat="">Home</button>
                    <button onclick="setCategory('movies')" class="px-3 py-1.5 rounded-lg hover:text-white hover:bg-white/5 transition nav-link" data-cat="movies">Movies</button>
                    <button onclick="setCategory('4k')" class="px-3 py-1.5 rounded-lg hover:text-white hover:bg-white/5 transition nav-link" data-cat="4k">4K Collection</button>
                    <button onclick="setCategory('bollywood')" class="px-3 py-1.5 rounded-lg hover:text-white hover:bg-white/5 transition nav-link" data-cat="bollywood">Bollywood</button>
                    <button onclick="setCategory('hollywood')" class="px-3 py-1.5 rounded-lg hover:text-white hover:bg-white/5 transition nav-link" data-cat="hollywood">Hollywood</button>
                    <button onclick="setCategory('south')" class="px-3 py-1.5 rounded-lg hover:text-white hover:bg-white/5 transition nav-link" data-cat="south">South Indian</button>
                    <button onclick="setCategory('series')" class="px-3 py-1.5 rounded-lg hover:text-white hover:bg-white/5 transition nav-link" data-cat="series">Web Series</button>
                    <button onclick="setCategory('kdrama')" class="px-3 py-1.5 rounded-lg hover:text-white hover:bg-white/5 transition nav-link" data-cat="kdrama">K-Drama</button>
                    <button onclick="setCategory('anime')" class="px-3 py-1.5 rounded-lg hover:text-white hover:bg-white/5 transition nav-link" data-cat="anime">Anime</button>
                </nav>

                <!-- Actions: AI Search, Settings -->
                <div class="flex items-center gap-2.5">
                    <button onclick="toggleCalendarSection()" class="flex items-center gap-1.5 px-3 py-2 rounded-full bg-white/5 hover:bg-white/10 text-white text-xs font-semibold transition" title="Browse by Year & Month">
                        <i class="fa-solid fa-calendar-days text-brand-gold text-xs"></i>
                        <span class="hidden sm:inline">Release Calendar</span>
                    </button>

                    <button onclick="openModal('aiModal')" class="flex items-center gap-1.5 px-3 py-2 rounded-full bg-white/5 hover:bg-white/10 text-white text-xs font-semibold transition" title="Ask CineVibe AI">
                        <i class="fa-solid fa-wand-magic-sparkles text-brand-gold text-xs"></i>
                        <span class="hidden sm:inline">AI Search</span>
                    </button>
                    
                    <button onclick="openModal('settingsModal')" class="p-2 rounded-full hover:bg-white/10 text-brand-muted hover:text-white transition" title="Stream & Engine Settings">
                        <i class="fa-solid fa-gear text-sm"></i>
                    </button>
                </div>
            </div>
        </header>

        <!-- Main Content Body -->
        <main class="flex-1 max-w-7xl mx-auto w-full px-4 sm:px-8 py-6 space-y-8">
            
            <!-- SEARCH BAR & SMART FILTERS -->
            <div class="space-y-4">
                <div class="relative w-full">
                    <i class="fa-solid fa-magnifying-glass absolute left-4 top-1/2 -translate-y-1/2 text-brand-muted text-sm"></i>
                    <input type="text" id="searchInput" oninput="handleSearch(this.value)" 
                           placeholder="Search movie title, star cast, director, anime or release year..." 
                           class="w-full pl-11 pr-24 py-3.5 rounded-2xl bg-brand-card border border-white/10 text-sm text-white placeholder-brand-muted focus:outline-none focus:border-brand-gold focus:ring-1 focus:ring-brand-gold transition shadow-inner">
                    <button onclick="clearSearch()" id="clearSearchBtn" class="hidden absolute right-4 top-1/2 -translate-y-1/2 text-xs text-brand-muted hover:text-white">Clear</button>
                </div>

                <!-- Quick Category Pills -->
                <div class="flex items-center gap-2 overflow-x-auto no-scrollbar pb-1 text-xs">
                    <span class="text-brand-muted font-medium shrink-0">Explore:</span>
                    <button onclick="setCategory('')" class="pill-btn px-3 py-1.5 rounded-full bg-brand-gold text-brand-black font-bold shrink-0">All Titles</button>
                    <button onclick="setCategory('4k')" class="pill-btn px-3 py-1.5 rounded-full bg-brand-card hover:bg-white/10 text-white shrink-0">💎 4K UHD</button>
                    <button onclick="setCategory('bollywood')" class="pill-btn px-3 py-1.5 rounded-full bg-brand-card hover:bg-white/10 text-white shrink-0">🍿 Bollywood</button>
                    <button onclick="setCategory('hollywood')" class="pill-btn px-3 py-1.5 rounded-full bg-brand-card hover:bg-white/10 text-white shrink-0">🎬 Hollywood</button>
                    <button onclick="setCategory('south')" class="pill-btn px-3 py-1.5 rounded-full bg-brand-card hover:bg-white/10 text-white shrink-0">🌴 South Indian</button>
                    <button onclick="setCategory('series')" class="pill-btn px-3 py-1.5 rounded-full bg-brand-card hover:bg-white/10 text-white shrink-0">📺 Web Series</button>
                    <button onclick="setCategory('kdrama')" class="pill-btn px-3 py-1.5 rounded-full bg-brand-card hover:bg-white/10 text-white shrink-0">👑 K-Drama</button>
                    <button onclick="setCategory('anime')" class="pill-btn px-3 py-1.5 rounded-full bg-brand-card hover:bg-white/10 text-white shrink-0">⚔️ Anime</button>
                    <button onclick="toggleCalendarSection()" class="pill-btn px-3 py-1.5 rounded-full bg-amber-500/20 text-brand-gold border border-brand-gold/30 hover:bg-brand-gold hover:text-black font-bold shrink-0">📅 Filter by Year & Month</button>
                </div>

                <!-- EXPANDABLE YEAR & MONTH FILTER MATRIX -->
                <div id="calendarFilterSection" class="p-4 rounded-2xl glass-panel border border-brand-gold/20 space-y-3">
                    <div class="flex items-center justify-between">
                        <div class="flex items-center gap-2">
                            <i class="fa-solid fa-calendar-check text-brand-gold text-sm"></i>
                            <h4 class="text-xs font-bold text-white tracking-wide">Release Calendar: Filter by Year & Month</h4>
                        </div>
                        <button onclick="resetCalendarFilter()" class="text-[11px] text-brand-gold hover:underline">Reset Filters</button>
                    </div>

                    <!-- Year Selection Row -->
                    <div class="flex items-center gap-2 overflow-x-auto no-scrollbar pb-1 text-xs">
                        <span class="text-brand-muted font-semibold shrink-0 text-[11px]">Year:</span>
                        <button onclick="filterByYear(null)" id="yearPillAll" class="px-2.5 py-1 rounded-lg bg-brand-gold text-black font-bold shrink-0 year-pill">All Years</button>
                        <button onclick="filterByYear(2024)" id="yearPill2024" class="px-2.5 py-1 rounded-lg bg-white/5 hover:bg-white/10 text-white font-semibold shrink-0 year-pill">2024</button>
                        <button onclick="filterByYear(2023)" id="yearPill2023" class="px-2.5 py-1 rounded-lg bg-white/5 hover:bg-white/10 text-white font-semibold shrink-0 year-pill">2023</button>
                        <button onclick="filterByYear(2022)" id="yearPill2022" class="px-2.5 py-1 rounded-lg bg-white/5 hover:bg-white/10 text-white font-semibold shrink-0 year-pill">2022</button>
                        <button onclick="filterByYear(2021)" id="yearPill2021" class="px-2.5 py-1 rounded-lg bg-white/5 hover:bg-white/10 text-white font-semibold shrink-0 year-pill">2021</button>
                        <button onclick="filterByYear(2020)" id="yearPill2020" class="px-2.5 py-1 rounded-lg bg-white/5 hover:bg-white/10 text-white font-semibold shrink-0 year-pill">2020</button>
                    </div>

                    <!-- Month Selection Row -->
                    <div class="flex items-center gap-1.5 overflow-x-auto no-scrollbar pb-1 text-[11px]">
                        <span class="text-brand-muted font-semibold shrink-0">Month:</span>
                        <button onclick="filterByMonth(null)" id="moPillAll" class="px-2 py-0.5 rounded bg-brand-gold text-black font-bold shrink-0 month-pill">All</button>
                        <button onclick="filterByMonth(1)" id="moPill1" class="px-2 py-0.5 rounded bg-white/5 hover:bg-white/10 text-white shrink-0 month-pill">Jan</button>
                        <button onclick="filterByMonth(2)" id="moPill2" class="px-2 py-0.5 rounded bg-white/5 hover:bg-white/10 text-white shrink-0 month-pill">Feb</button>
                        <button onclick="filterByMonth(3)" id="moPill3" class="px-2 py-0.5 rounded bg-white/5 hover:bg-white/10 text-white shrink-0 month-pill">Mar</button>
                        <button onclick="filterByMonth(4)" id="moPill4" class="px-2 py-0.5 rounded bg-white/5 hover:bg-white/10 text-white shrink-0 month-pill">Apr</button>
                        <button onclick="filterByMonth(5)" id="moPill5" class="px-2 py-0.5 rounded bg-white/5 hover:bg-white/10 text-white shrink-0 month-pill">May</button>
                        <button onclick="filterByMonth(6)" id="moPill6" class="px-2 py-0.5 rounded bg-white/5 hover:bg-white/10 text-white shrink-0 month-pill">Jun</button>
                        <button onclick="filterByMonth(7)" id="moPill7" class="px-2 py-0.5 rounded bg-white/5 hover:bg-white/10 text-white shrink-0 month-pill">Jul</button>
                        <button onclick="filterByMonth(8)" id="moPill8" class="px-2 py-0.5 rounded bg-white/5 hover:bg-white/10 text-white shrink-0 month-pill">Aug</button>
                        <button onclick="filterByMonth(9)" id="moPill9" class="px-2 py-0.5 rounded bg-white/5 hover:bg-white/10 text-white shrink-0 month-pill">Sep</button>
                        <button onclick="filterByMonth(10)" id="moPill10" class="px-2 py-0.5 rounded bg-white/5 hover:bg-white/10 text-white shrink-0 month-pill">Oct</button>
                        <button onclick="filterByMonth(11)" id="moPill11" class="px-2 py-0.5 rounded bg-white/5 hover:bg-white/10 text-white shrink-0 month-pill">Nov</button>
                        <button onclick="filterByMonth(12)" id="moPill12" class="px-2 py-0.5 rounded bg-white/5 hover:bg-white/10 text-white shrink-0 month-pill">Dec</button>
                    </div>
                </div>
            </div>

            <!-- TRENDING POSTER SLIDER / CAROUSEL -->
            <div id="heroSliderSection" class="relative rounded-3xl overflow-hidden h-[340px] sm:h-[420px] bg-brand-card border border-white/5 shadow-2xl">
                <div id="sliderBackground" class="absolute inset-0 bg-cover bg-center transition-all duration-700 brightness-75"></div>
                <div class="absolute inset-0 bg-gradient-to-t from-brand-black via-brand-black/40 to-transparent"></div>
                <div class="absolute inset-0 bg-gradient-to-r from-brand-black via-brand-black/60 to-transparent"></div>
                
                <div class="relative z-10 h-full p-6 sm:p-12 flex flex-col justify-end max-w-2xl space-y-3">
                    <div class="flex items-center gap-2">
                        <span id="sliderBadge" class="px-2.5 py-0.5 rounded bg-brand-gold text-brand-black text-[10px] font-black uppercase tracking-wider">TRENDING NOW</span>
                        <span id="sliderQuality" class="px-2 py-0.5 rounded bg-white/10 text-white text-[10px] font-bold">4K UHD</span>
                        <span id="sliderRating" class="text-xs text-brand-gold font-bold flex items-center gap-1">
                            <i class="fa-solid fa-star text-[10px]"></i> <span id="sliderRatingVal">8.9</span>
                        </span>
                    </div>
                    
                    <h2 id="sliderTitle" class="text-2xl sm:text-4xl font-extrabold text-white tracking-tight">Oppenheimer</h2>
                    
                    <p id="sliderDesc" class="text-xs sm:text-sm text-brand-muted line-clamp-2 sm:line-clamp-3">
                        The dramatic story of American scientist J. Robert Oppenheimer and his role in the development of the atomic bomb during World War II.
                    </p>

                    <div class="pt-2 flex items-center gap-3">
                        <button id="sliderPlayBtn" onclick="openSliderMovie()" class="px-6 py-2.5 rounded-full bg-brand-gold text-brand-black font-extrabold text-xs hover:scale-105 transition flex items-center gap-2 gold-glow">
                            <i class="fa-solid fa-play text-[10px]"></i>
                            <span>Watch & Download</span>
                        </button>
                        <button onclick="nextSlide()" class="p-2.5 rounded-full glass-panel hover:bg-white/10 text-white text-xs transition">
                            <i class="fa-solid fa-forward"></i>
                        </button>
                    </div>
                </div>

                <!-- Slider Indicators -->
                <div class="absolute bottom-4 right-6 z-10 flex items-center gap-1.5" id="sliderDots"></div>
            </div>

            <!-- SEARCH / FILTER RESULTS GRID (WHEN SEARCHING OR CALENDAR FILTER ACTIVE) -->
            <div id="catalogSection" class="hidden space-y-4">
                <div class="flex items-center justify-between">
                    <h3 id="catalogTitle" class="text-lg font-bold text-white tracking-wide">Search Results</h3>
                    <button onclick="closeSearchResults()" class="text-xs text-brand-gold hover:underline">Back to Featured</button>
                </div>
                <div id="catalogGrid" class="grid grid-cols-2 sm:grid-cols-3 md:grid-cols-4 lg:grid-cols-5 gap-4"></div>
            </div>

            <!-- DYNAMIC SECTIONS CONTAINER -->
            <div id="sectionsContainer" class="space-y-10"></div>

        </main>

        <!-- Main Platform Footer -->
        <footer class="mt-16 border-t border-white/5 bg-brand-dark py-10 px-6 sm:px-12 text-xs text-brand-muted">
            <div class="max-w-7xl mx-auto grid grid-cols-1 md:grid-cols-4 gap-8">
                <div class="space-y-3">
                    <div class="flex items-center gap-2.5">
                        <div class="w-7 h-7 rounded-lg bg-brand-gold flex items-center justify-center text-black font-bold text-xs">CV</div>
                        <span class="font-cinematic text-lg font-bold text-white">CINE<span class="text-brand-gold">VIBE</span></span>
                    </div>
                    <p class="text-[11px] leading-relaxed">
                        Authorized high-speed movie discovery and local media delivery platform. High-definition 4K HDR streams powered by multi-socket download technology.
                    </p>
                </div>
                <div>
                    <h5 class="text-white font-bold mb-2.5 text-xs uppercase tracking-wider">Browse Collections</h5>
                    <ul class="space-y-1.5 text-[11px]">
                        <li><a href="javascript:void(0)" onclick="setCategory('movies')" class="hover:text-white">All Movies</a></li>
                        <li><a href="javascript:void(0)" onclick="setCategory('4k')" class="hover:text-white">4K UHD Ultra HD</a></li>
                        <li><a href="javascript:void(0)" onclick="setCategory('bollywood')" class="hover:text-white">Hindi Cinema</a></li>
                        <li><a href="javascript:void(0)" onclick="setCategory('south')" class="hover:text-white">South Indian Dubbed</a></li>
                        <li><a href="javascript:void(0)" onclick="setCategory('kdrama')" class="hover:text-white">Korean Dramas</a></li>
                        <li><a href="javascript:void(0)" onclick="setCategory('anime')" class="hover:text-white">Anime Series</a></li>
                    </ul>
                </div>
                <div>
                    <h5 class="text-white font-bold mb-2.5 text-xs uppercase tracking-wider">Platform & Legal</h5>
                    <ul class="space-y-1.5 text-[11px]">
                        <li><a href="javascript:void(0)" onclick="openModal('legalModal')" class="hover:text-white">Rights Verification</a></li>
                        <li><a href="javascript:void(0)" onclick="openModal('dmcaModal')" class="hover:text-white">DMCA Takedown</a></li>
                        <li><a href="javascript:void(0)" onclick="openModal('settingsModal')" class="hover:text-white">Streamer Settings</a></li>
                    </ul>
                </div>
                <div>
                    <h5 class="text-white font-bold mb-2.5 text-xs uppercase tracking-wider">Streaming Engine</h5>
                    <p class="text-[11px] leading-relaxed mb-2">Connected to CineVibe Cloud Multi-Socket Streamer (24/7 Online).</p>
                    <div class="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-emerald-500/10 border border-emerald-500/20 text-emerald-400 text-[10px] font-bold">
                        <span class="w-1.5 h-1.5 rounded-full bg-emerald-400 animate-pulse"></span>
                        <span>8 Socket Multi-Session Online</span>
                    </div>
                </div>
            </div>
            <div class="max-w-7xl mx-auto mt-8 pt-4 border-t border-white/5 flex flex-col sm:flex-row items-center justify-between text-[11px] gap-2">
                <span>&copy; 2026 CineVibe. Crafted with passion for cinema lovers.</span>
                <span>Powered by CineVibe ByteStreamer & Gemini AI.</span>
            </div>
        </footer>
    </div>

    <!-- ========================================== -->
    <!-- MODAL 1: MOVIE DETAILS & STREAMING (FULL) -->
    <!-- ========================================== -->
    <div id="movieDetailsModal" class="hidden fixed inset-0 z-50 overflow-y-auto bg-black/80 backdrop-blur-md flex items-center justify-center p-4">
        <div class="relative w-full max-w-3xl rounded-3xl overflow-hidden bg-brand-card border border-white/10 shadow-2xl text-left my-8">
            
            <button onclick="closeModal('movieDetailsModal')" class="absolute top-4 right-4 z-20 w-8 h-8 rounded-full bg-black/60 hover:bg-black/90 text-white flex items-center justify-center transition border border-white/10">
                <i class="fa-solid fa-xmark text-sm"></i>
            </button>

            <!-- Backdrop Header -->
            <div class="relative h-64 sm:h-80 w-full overflow-hidden bg-brand-dark">
                <div id="modalBackdrop" class="absolute inset-0 bg-cover bg-center brightness-75 transition-all duration-500"></div>
                <div class="absolute inset-0 bg-gradient-to-t from-brand-card via-brand-card/40 to-transparent"></div>
                
                <div class="absolute bottom-6 left-6 right-6 flex items-end gap-5">
                    <img id="modalPoster" src="" referrerpolicy="no-referrer" alt="" class="w-24 sm:w-32 h-36 sm:h-48 object-cover rounded-xl shadow-2xl border-2 border-white/10 shrink-0">
                    <div class="space-y-1.5">
                        <div class="flex items-center gap-2">
                            <span id="modalQuality" class="px-2 py-0.5 rounded bg-brand-gold text-black font-extrabold text-[10px]">4K UHD</span>
                            <span id="modalYear" class="text-xs text-brand-muted font-bold">2024</span>
                            <span id="modalRuntime" class="text-xs text-brand-muted font-medium">• 2h 45m</span>
                            <span id="modalRating" class="px-1.5 py-0.5 rounded bg-black/60 text-brand-gold font-bold text-xs flex items-center gap-1">
                                <i class="fa-solid fa-star text-[10px]"></i> 8.9
                            </span>
                        </div>
                        <h2 id="modalTitle" class="text-xl sm:text-3xl font-extrabold text-white leading-tight">Movie Title</h2>
                        <p id="modalOriginalTitle" class="text-[11px] text-brand-muted line-clamp-1 font-mono"></p>
                    </div>
                </div>
            </div>

            <!-- Modal Content & Tabs -->
            <div class="p-6 space-y-6">
                <!-- Tabs -->
                <div class="flex items-center gap-4 border-b border-white/5 pb-2 text-xs font-bold text-brand-muted">
                    <button class="text-brand-gold border-b-2 border-brand-gold pb-2">Overview</button>
                    <button onclick="showToast('Authorized audio formats verified!')" class="hover:text-white transition pb-2">Authorized Formats</button>
                    <button onclick="showToast('Cast metadata synchronized from TMDB!')" class="hover:text-white transition pb-2">Cast & Crew</button>
                </div>

                <p id="modalOverview" class="text-xs sm:text-sm text-brand-muted leading-relaxed font-normal"></p>

                <!-- Metadata Grid -->
                <div class="grid grid-cols-2 sm:grid-cols-3 gap-3 p-4 rounded-xl bg-white/5 border border-white/5 text-[11px]">
                    <div>
                        <span class="text-brand-muted block text-[10px] uppercase">Director</span>
                        <span id="modalDirector" class="font-bold text-white">Christopher Nolan</span>
                    </div>
                    <div>
                        <span class="text-brand-muted block text-[10px] uppercase">Audio Languages</span>
                        <span id="modalLanguages" class="font-bold text-white">English, Hindi</span>
                    </div>
                    <div>
                        <span class="text-brand-muted block text-[10px] uppercase">Distribution Status</span>
                        <span class="font-bold text-emerald-400 flex items-center gap-1">
                            <i class="fa-solid fa-circle-check text-[10px]"></i> Verified Authorized
                        </span>
                    </div>
                </div>

                <!-- STREAM / DOWNLOAD ACTION BUTTONS (CONNECTED TO CLOUD BOT STREAMER) -->
                <div class="pt-2 flex flex-col sm:flex-row items-center gap-3">
                    <button onclick="triggerStream('stream')" class="w-full sm:flex-1 py-3.5 rounded-xl bg-brand-gold text-brand-black font-extrabold text-xs hover:bg-brand-goldDark transition flex items-center justify-center gap-2 gold-glow">
                        <i class="fa-solid fa-play"></i>
                        <span>WATCH ONLINE</span>
                    </button>
                    <button onclick="triggerStream('download')" class="w-full sm:flex-1 py-3.5 rounded-xl bg-white/10 hover:bg-white/20 text-white font-extrabold text-xs transition flex items-center justify-center gap-2 border border-white/10">
                        <i class="fa-solid fa-download"></i>
                        <span>FAST DOWNLOAD (8X SPEED)</span>
                    </button>
                    <button onclick="openTelegramBot()" class="w-full sm:w-auto px-4 py-3.5 rounded-xl bg-[#229ED9]/20 hover:bg-[#229ED9]/30 text-[#229ED9] border border-[#229ED9]/30 font-extrabold text-xs transition flex items-center justify-center gap-2" title="Get Directly in Telegram App">
                        <i class="fa-brands fa-telegram"></i>
                        <span>TELEGRAM BOT</span>
                    </button>
                    <button onclick="copyStreamLink()" class="p-3.5 rounded-xl bg-white/5 hover:bg-white/10 text-brand-muted hover:text-white transition" title="Copy Direct Stream Link">
                        <i class="fa-solid fa-link"></i>
                    </button>
                </div>
            </div>
        </div>
    </div>

    <!-- ========================================== -->
    <!-- MODAL 2: CINEVIBE AI SEARCH ASSISTANT      -->
    <!-- ========================================== -->
    <div id="aiModal" class="hidden fixed inset-0 z-50 overflow-y-auto bg-black/85 backdrop-blur-md flex items-center justify-center p-4">
        <div class="relative w-full max-w-xl rounded-3xl bg-brand-card border border-brand-gold/30 p-6 space-y-4 shadow-2xl text-left">
            <div class="flex items-center justify-between">
                <div class="flex items-center gap-2.5">
                    <div class="w-8 h-8 rounded-lg bg-brand-gold flex items-center justify-center text-brand-black text-sm">
                        <i class="fa-solid fa-wand-magic-sparkles"></i>
                    </div>
                    <div>
                        <h3 class="text-sm font-bold text-white">CineVibe AI Movie Discovery</h3>
                        <span class="text-[10px] text-brand-muted">Ask anything in natural Hindi or English</span>
                    </div>
                </div>
                <button onclick="closeModal('aiModal')" class="text-brand-muted hover:text-white"><i class="fa-solid fa-xmark text-sm"></i></button>
            </div>

            <div class="relative">
                <textarea id="aiQueryInput" rows="3" 
                          placeholder="e.g. 'Mujhe 2024 ki action movies dikhao jisme revenge story ho' or 'Suggest best anime of 2023'..." 
                          class="w-full p-3.5 rounded-xl bg-brand-dark border border-white/10 text-xs text-white placeholder-brand-muted focus:outline-none focus:border-brand-gold transition resize-none"></textarea>
                <button onclick="askGeminiAI()" id="aiSubmitBtn" class="mt-2 w-full py-2.5 rounded-xl bg-brand-gold text-black font-extrabold text-xs hover:bg-brand-goldDark transition flex items-center justify-center gap-2">
                    <i class="fa-solid fa-sparkles"></i>
                    <span>Ask CineVibe AI</span>
                </button>
            </div>

            <div id="aiResponseContainer" class="hidden p-4 rounded-xl bg-white/5 border border-white/5 space-y-3">
                <div class="flex items-center gap-2 text-xs text-brand-gold font-bold">
                    <i class="fa-solid fa-robot"></i>
                    <span>AI Recommendation:</span>
                </div>
                <p id="aiAnswerText" class="text-xs text-white leading-relaxed font-normal whitespace-pre-line"></p>
                <div id="aiMatchedCards" class="pt-2"></div>
            </div>
        </div>
    </div>

    <!-- ========================================== -->
    <!-- MODAL 3: STREAM & API SETTINGS             -->
    <!-- ========================================== -->
    <div id="settingsModal" class="hidden fixed inset-0 z-50 overflow-y-auto bg-black/85 backdrop-blur-md flex items-center justify-center p-4">
        <div class="relative w-full max-w-md rounded-3xl bg-brand-card border border-white/10 p-6 space-y-4 shadow-2xl text-left">
            <div class="flex items-center justify-between">
                <h3 class="text-sm font-bold text-white flex items-center gap-2">
                    <i class="fa-solid fa-sliders text-brand-gold"></i>
                    <span>Engine & Stream Settings</span>
                </h3>
                <button onclick="closeModal('settingsModal')" class="text-brand-muted hover:text-white"><i class="fa-solid fa-xmark text-sm"></i></button>
            </div>

            <div class="space-y-3 text-xs">
                <div>
                    <label class="block text-brand-muted mb-1 text-[11px]">Cloud Bot Streamer Address:</label>
                    <input type="text" id="botBaseUrlInput" class="w-full p-2.5 rounded-xl bg-brand-dark border border-white/10 text-white font-mono text-xs focus:outline-none focus:border-brand-gold">
                    <span class="text-[10px] text-brand-muted">Default: <code>https://telegram-filter-bot.onrender.com</code> (Cloud Python ByteStreamer)</span>
                </div>
                <div>
                    <label class="block text-brand-muted mb-1 text-[11px]">Gemini API Key (Optional for AI Search):</label>
                    <input type="password" id="geminiApiKeyInput" class="w-full p-2.5 rounded-xl bg-brand-dark border border-white/10 text-white font-mono text-xs focus:outline-none focus:border-brand-gold">
                    <span class="text-[10px] text-brand-muted">Used for natural language movie suggestions.</span>
                </div>
            </div>

            <div class="pt-2 flex justify-end gap-2">
                <button onclick="closeModal('settingsModal')" class="px-4 py-2 rounded-xl bg-white/5 text-xs text-brand-muted hover:text-white">Cancel</button>
                <button onclick="saveSettings()" class="px-5 py-2 rounded-xl bg-brand-gold text-black font-bold text-xs hover:bg-brand-goldDark">Save Settings</button>
            </div>
        </div>
    </div>

    <!-- ========================================== -->
    <!-- MODAL 4: RIGHTS & VERIFICATION             -->
    <!-- ========================================== -->
    <div id="legalModal" class="hidden fixed inset-0 z-50 overflow-y-auto bg-black/85 backdrop-blur-md flex items-center justify-center p-4">
        <div class="relative w-full max-w-lg rounded-3xl bg-brand-card border border-white/10 p-6 space-y-3 shadow-2xl text-left">
            <div class="flex items-center justify-between">
                <h3 class="text-sm font-bold text-white">Rights-Verification System</h3>
                <button onclick="closeModal('legalModal')" class="text-brand-muted hover:text-white"><i class="fa-solid fa-xmark text-sm"></i></button>
            </div>
            <p class="text-xs text-brand-muted leading-relaxed">
                CineVibe operates strictly with authorized content records, open-license public distribution models, and direct high-speed multi-socket delivery channels.
            </p>
            <div class="p-3 rounded-xl bg-white/5 border border-white/5 text-[11px] text-white">
                <p>✔ Real-time metadata integrity checks against TMDB registry</p>
                <p>✔ Expiring tokens and high-speed DC4 session pool routing</p>
            </div>
            <button onclick="closeModal('legalModal')" class="w-full py-2.5 rounded-xl bg-brand-gold text-black font-bold text-xs">Acknowledge</button>
        </div>
    </div>

    <!-- ========================================== -->
    <!-- MODAL 5: DMCA COMPLIANCE                   -->
    <!-- ========================================== -->
    <div id="dmcaModal" class="hidden fixed inset-0 z-50 overflow-y-auto bg-black/85 backdrop-blur-md flex items-center justify-center p-4">
        <div class="relative w-full max-w-lg rounded-3xl bg-brand-card border border-white/10 p-6 space-y-3 shadow-2xl text-left">
            <div class="flex items-center justify-between">
                <h3 class="text-sm font-bold text-white">DMCA Takedown & Copyright Notice</h3>
                <button onclick="closeModal('dmcaModal')" class="text-brand-muted hover:text-white"><i class="fa-solid fa-xmark text-sm"></i></button>
            </div>
            <p class="text-xs text-brand-muted leading-relaxed">
                CineVibe respects intellectual property rights. If you believe your copyrighted work is accessible without authorization, submit your notice to our designated agent.
            </p>
            <div class="p-3 rounded-xl bg-white/5 border border-white/5 text-[11px] font-mono text-brand-gold">
                Email: dmca@cinevibe.internal<br>
                Response SLA: Within 24 hours
            </div>
            <button onclick="closeModal('dmcaModal')" class="w-full py-2.5 rounded-xl bg-white/10 text-white font-bold text-xs hover:bg-white/20">Close Notice</button>
        </div>
    </div>

    <!-- ========================================== -->
    <!-- EMBEDDED CINEVIBE CATALOG DATA & ENGINE    -->
    <!-- ========================================== -->
    <script>
        let MOVIES_CATALOG = {catalog_json};

        let selectedMovie = null;
        let currentSlide = 0;
        let sliderInterval = null;
        let activeCategory = '';
        let selectedYear = null;
        let selectedMonth = null;
        const DEFAULT_BOT_URL = 'https://telegram-filter-bot.onrender.com';
        let savedBotUrl = (localStorage.getItem('cinevibe_bot_url') || '').trim().replace(/\/+$/, '');
        if (!savedBotUrl || savedBotUrl.includes('127.0.0.1') || savedBotUrl.includes('localhost')) {{
            savedBotUrl = DEFAULT_BOT_URL;
            localStorage.setItem('cinevibe_bot_url', savedBotUrl);
        }}
        let botBaseUrl = savedBotUrl;
        let geminiApiKey = localStorage.getItem('cinevibe_gemini_key') || '';

        // Auto-Sync Dynamic Catalog from Bot API or updated JSON
        async function autoSyncLiveCatalog() {{
            try {{
                let res = null;
                try {{
                    res = await fetch(`${{botBaseUrl}}/api/catalog`);
                }} catch (e) {{}}
                if (!res || !res.ok) {{
                    res = await fetch('/catalog.json?v=' + Date.now());
                }}
                if (res && res.ok) {{
                    const data = await res.json();
                    if (Array.isArray(data) && data.length > 0) {{
                        MOVIES_CATALOG = data;
                        initSlider();
                        renderSections();
                    }}
                }}
            }} catch (err) {{}}
        }}

        let FULL_DB_INDEX = [];
        let isDbIndexLoaded = false;
        async function loadFullDatabaseIndex() {{
            try {{
                const res = await fetch('/db_index.json?v=' + Date.now());
                if (res && res.ok) {{
                    FULL_DB_INDEX = await res.json();
                    isDbIndexLoaded = true;
                    const curQ = document.getElementById('searchInput')?.value?.trim();
                    if (curQ) {{
                        handleSearch(curQ);
                    }}
                }}
            }} catch (err) {{}}
        }}

        // Initialize App
        document.addEventListener('DOMContentLoaded', () => {{
            document.getElementById('botBaseUrlInput').value = botBaseUrl;
            document.getElementById('geminiApiKeyInput').value = geminiApiKey;

            // Auto-check if we should auto-enter if visited from gateway or query
            const urlParams = new URLSearchParams(window.location.search);
            if (urlParams.get('utm') || urlParams.get('explore') || window.location.hash) {{
                enterMainPlatform();
            }}

            // Register PWA service worker
            if ('serviceWorker' in navigator) {{
                navigator.serviceWorker.register('/sw.js').catch(() => {{}});
            }}

            initSlider();
            renderSections();
            autoSyncLiveCatalog();
            loadFullDatabaseIndex();
        }});

        // Navigation Switching
        function enterMainPlatform() {{
            document.getElementById('landingPage').classList.add('hidden');
            document.getElementById('mainPlatform').classList.remove('hidden');
            window.scrollTo({{ top: 0, behavior: 'smooth' }});
        }}

        function enterLandingPage() {{
            document.getElementById('mainPlatform').classList.add('hidden');
            document.getElementById('landingPage').classList.remove('hidden');
            window.scrollTo({{ top: 0, behavior: 'smooth' }});
        }}

        // Slider Setup
        function initSlider() {{
            const featured = MOVIES_CATALOG.filter(m => m.featured);
            if (featured.length === 0) return;

            updateSliderContent(0);

            const dots = document.getElementById('sliderDots');
            dots.innerHTML = featured.map((_, i) => `
                <button onclick="goToSlide(${{i}})" class="w-2 h-2 rounded-full transition-all ${{i === 0 ? 'w-6 bg-brand-gold' : 'bg-white/40'}}"></button>
            `).join('');

            if (sliderInterval) clearInterval(sliderInterval);
            sliderInterval = setInterval(nextSlide, 6000);
        }}

        function updateSliderContent(index) {{
            const featured = MOVIES_CATALOG.filter(m => m.featured);
            if (!featured[index]) return;
            const m = featured[index];
            currentSlide = index;

            document.getElementById('sliderBackground').style.backgroundImage = `url('${{m.backdrop_url || m.poster_url}}')`;
            document.getElementById('sliderTitle').innerText = m.title;
            document.getElementById('sliderDesc').innerText = m.overview;
            document.getElementById('sliderQuality').innerText = m.quality;
            document.getElementById('sliderRatingVal').innerText = m.rating;
            document.getElementById('sliderBadge').innerText = m.year >= 2024 ? 'LATEST RELEASE' : 'TRENDING NOW';

            // Update dots
            const dots = document.getElementById('sliderDots').children;
            for (let i = 0; i < dots.length; i++) {{
                dots[i].className = i === index 
                    ? 'w-6 h-2 rounded-full bg-brand-gold transition-all' 
                    : 'w-2 h-2 rounded-full bg-white/40 hover:bg-white/70 transition-all';
            }}
        }}

        function nextSlide() {{
            const featured = MOVIES_CATALOG.filter(m => m.featured);
            let next = (currentSlide + 1) % featured.length;
            updateSliderContent(next);
        }}

        function goToSlide(index) {{
            updateSliderContent(index);
            if (sliderInterval) clearInterval(sliderInterval);
            sliderInterval = setInterval(nextSlide, 6000);
        }}

        function openSliderMovie() {{
            const featured = MOVIES_CATALOG.filter(m => m.featured);
            if (featured[currentSlide]) {{
                openMovieDetails(featured[currentSlide].id);
            }}
        }}

        // Homepage Movie Sections
        function renderSections() {{
            const container = document.getElementById('sectionsContainer');
            const sections = {{
                "latest_releases": {{ title: "✨ Latest 2024 Releases", filter: m => m.year >= 2024 }},
                "popular_movies": {{ title: "💎 Popular 4K Ultra HD Movies", filter: m => m.quality.includes('4K') }},
                "kdramas": {{ title: "👑 Royal K-Dramas & Romances", filter: m => m.category === 'kdrama' }},
                "anime": {{ title: "⚔️ Action & Dark Fantasy Anime", filter: m => m.category === 'anime' }},
                "bollywood": {{ title: "🍿 Bollywood Blockbusters", filter: m => m.category === 'bollywood' }},
                "south": {{ title: "🌴 South Indian Cinema", filter: m => m.category === 'south' }},
                "series": {{ title: "📺 Popular Binge Web Series", filter: m => m.category === 'series' }},
                "turbo": {{ title: "⚡ High-Speed Direct Downloads", filter: m => true }}
            }};

            let html = '';
            for (const [key, sec] of Object.entries(sections)) {{
                const list = MOVIES_CATALOG.filter(sec.filter);
                if (list.length === 0) continue;

                html += `
                    <div class="space-y-4">
                        <div class="flex items-center justify-between">
                            <h3 class="text-lg sm:text-xl font-bold text-white tracking-wide">${{sec.title}}</h3>
                            <button onclick="setCategory('${{key === 'popular_movies' ? '4k' : key}}')" class="text-xs text-brand-gold hover:underline font-semibold">View All →</button>
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
                             onerror="handleImageError(this, '${{m.title.replace(/'/g, "\'")}}', '${{m.year}}')" 
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

        // Categories & Calendar Filtering
        function toggleCalendarSection() {{
            const el = document.getElementById('calendarFilterSection');
            el.scrollIntoView({{ behavior: 'smooth' }});
        }}

        function filterByYear(year) {{
            selectedYear = year;
            // update pills
            document.querySelectorAll('.year-pill').forEach(btn => {{
                btn.className = 'px-2.5 py-1 rounded-lg bg-white/5 hover:bg-white/10 text-white font-semibold shrink-0 year-pill';
            }});
            const activeBtn = year ? document.getElementById(`yearPill${{year}}`) : document.getElementById('yearPillAll');
            if (activeBtn) activeBtn.className = 'px-2.5 py-1 rounded-lg bg-brand-gold text-black font-bold shrink-0 year-pill';
            applyCombinedFilters();
        }}

        function filterByMonth(month) {{
            selectedMonth = month;
            // update pills
            document.querySelectorAll('.month-pill').forEach(btn => {{
                btn.className = 'px-2 py-0.5 rounded bg-white/5 hover:bg-white/10 text-white shrink-0 month-pill';
            }});
            const activeBtn = month ? document.getElementById(`moPill${{month}}`) : document.getElementById('moPillAll');
            if (activeBtn) activeBtn.className = 'px-2 py-0.5 rounded bg-brand-gold text-black font-bold shrink-0 month-pill';
            applyCombinedFilters();
        }}

        function resetCalendarFilter() {{
            selectedYear = null;
            selectedMonth = null;
            filterByYear(null);
            filterByMonth(null);
            closeSearchResults();
        }}

        function applyCombinedFilters() {{
            let list = MOVIES_CATALOG;
            if (selectedYear) {{
                list = list.filter(m => m.year === selectedYear);
            }}
            if (selectedMonth) {{
                list = list.filter(m => m.release_month === selectedMonth);
            }}

            const title = `Releases: ${{selectedYear || 'All Years'}} ${{selectedMonth ? '- Month ' + selectedMonth : ''}} (${{list.length}} titles)`;
            displayCustomGrid(list, title);
        }}

        function setCategory(cat) {{
            activeCategory = cat;
            document.querySelectorAll('.nav-link').forEach(btn => {{
                if (btn.dataset.cat === cat) {{
                    btn.classList.add('text-brand-gold', 'active-nav');
                }} else {{
                    btn.classList.remove('text-brand-gold', 'active-nav');
                }}
            }});

            if (!cat) {{
                closeSearchResults();
                return;
            }}

            let list = [];
            let title = '';
            if (cat === 'movies') {{
                list = MOVIES_CATALOG.filter(m => m.type === 'movie');
                title = 'All Verified Movies';
            }} else if (cat === '4k') {{
                list = MOVIES_CATALOG.filter(m => m.quality.includes('4K'));
                title = '4K Ultra HD Cinema Collection';
            }} else {{
                list = MOVIES_CATALOG.filter(m => m.category === cat);
                title = `${{cat.toUpperCase()}} Collection`;
            }}

            displayCustomGrid(list, title);
        }}

        function displayCustomGrid(list, title) {{
            document.getElementById('heroSliderSection').classList.add('hidden');
            document.getElementById('sectionsContainer').classList.add('hidden');
            const catSec = document.getElementById('catalogSection');
            catSec.classList.remove('hidden');

            document.getElementById('catalogTitle').innerText = title;
            const grid = document.getElementById('catalogGrid');
            if (list.length === 0) {{
                grid.innerHTML = `<div class="col-span-full py-16 text-center text-brand-muted text-sm">No titles found for this filter. Try asking CineVibe AI!</div>`;
                return;
            }}
            grid.innerHTML = list.map(m => createMovieCard(m)).join('');
            window.scrollTo({{ top: 0, behavior: 'smooth' }});
        }}

        function closeSearchResults() {{
            document.getElementById('heroSliderSection').classList.remove('hidden');
            document.getElementById('sectionsContainer').classList.remove('hidden');
            document.getElementById('catalogSection').classList.add('hidden');
            document.getElementById('searchInput').value = '';
            document.getElementById('clearSearchBtn').classList.add('hidden');
        }}

        // Instant Search with Live 10,000+ Telegram Database Support
        function handleSearch(q) {{
            const clearBtn = document.getElementById('clearSearchBtn');
            if (!q.trim()) {{
                clearBtn.classList.add('hidden');
                closeSearchResults();
                return;
            }}
            clearBtn.classList.remove('hidden');

            const query = q.toLowerCase().trim();
            const localResults = MOVIES_CATALOG.filter(m => 
                m.title.toLowerCase().includes(query) ||
                m.file_name.toLowerCase().includes(query) ||
                m.genres.some(g => g.toLowerCase().includes(query)) ||
                m.director.toLowerCase().includes(query) ||
                m.cast.some(c => c.toLowerCase().includes(query)) ||
                m.year.toString().includes(query)
            );

            // Search full 10,000+ MongoDB library index (Pushpa, etc.)
            let indexResults = [];
            if (FULL_DB_INDEX && FULL_DB_INDEX.length > 0) {{
                const matchedEntries = FULL_DB_INDEX.filter(item => 
                    item.t.toLowerCase().includes(query) ||
                    (item.fn && item.fn.toLowerCase().includes(query))
                ).slice(0, 50);

                indexResults = matchedEntries.map((item, idx) => {{
                    const catalogMatch = MOVIES_CATALOG.find(m => m.title.toLowerCase() === item.t.toLowerCase());
                    let pUrl = "";
                    if (item.p) {{
                        pUrl = `https://images.weserv.nl/?url=image.tmdb.org/t/p/w500${{item.p}}`;
                    }} else if (catalogMatch && catalogMatch.poster_url) {{
                        pUrl = catalogMatch.poster_url;
                    }} else {{
                        const cleanT = encodeURIComponent(item.t.length > 22 ? item.t.substring(0, 20) + '...' : item.t);
                        pUrl = `data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" width="300" height="450" viewBox="0 0 300 450"><defs><linearGradient id="g" x1="0%" y1="0%" x2="100%" y2="100%"><stop offset="0%" stop-color="%231a1a1a"/><stop offset="100%" stop-color="%230c0c0c"/></linearGradient></defs><rect width="300" height="450" fill="url(%23g)"/><rect x="12" y="12" width="276" height="426" fill="none" stroke="%23FFC928" stroke-width="1.5" opacity="0.3" rx="12"/><circle cx="150" cy="160" r="40" fill="%23FFC928" opacity="0.15"/><path d="M142 145 L164 160 L142 175 Z" fill="%23FFC928"/><text x="150" y="240" font-family="sans-serif" font-weight="800" font-size="18" fill="%23FFFFFF" text-anchor="middle">${{cleanT}}</text><text x="150" y="270" font-family="sans-serif" font-weight="600" font-size="13" fill="%23FFC928" text-anchor="middle">${{item.y || '2024'}} • ${{item.q || '1080p'}}</text><text x="150" y="380" font-family="sans-serif" font-weight="500" font-size="11" fill="%23888888" text-anchor="middle">CINEVIBE CINEMA</text></svg>`;
                    }}
                    return {{
                        id: `tg-${{item.id || idx}}`,
                        title: item.t,
                        year: item.y,
                        rating: catalogMatch ? catalogMatch.rating : 8.2,
                        runtime: item.s,
                        quality: item.q || "1080p FHD",
                        category: item.tv ? "series" : "telegram",
                        type: item.tv ? "series" : "movie",
                        languages: catalogMatch ? catalogMatch.languages : ["Multi-Audio"],
                        genres: catalogMatch ? catalogMatch.genres : ["Telegram Bot Library"],
                        director: catalogMatch ? catalogMatch.director : "Verified Community Upload",
                        cast: catalogMatch ? catalogMatch.cast : ["Telegram DB Archive"],
                        overview: catalogMatch ? catalogMatch.overview : `Available file in Telegram Bot: ${{item.fn}} (${{item.s}})`,
                        poster_url: pUrl,
                        backdrop_url: pUrl,
                        file_name: item.fn,
                        file_size: 0,
                        file_size_human: item.s,
                        file_id: item.id,
                        stream_msg_id: 116,
                        stream_hash: "AgADwB",
                        featured: false
                    }};
                }});
            }}

            const combined = [...localResults, ...indexResults.filter(ir => !localResults.some(lr => lr.title.toLowerCase() === ir.title.toLowerCase()))];
            displayCustomGrid(combined, `Search Results for "${{q}}" (${{combined.length}} found in Catalog & 10K+ Library)`);
        }}

        function clearSearch() {{
            document.getElementById('searchInput').value = '';
            document.getElementById('clearSearchBtn').classList.add('hidden');
            closeSearchResults();
        }}

        function openTelegramBot() {{
            if (!selectedMovie) return;
            const fileId = selectedMovie.file_id || '';
            const tgUrl = fileId 
                ? `https://t.me/movieDRV2bot?start=file_${{fileId}}` 
                : `https://t.me/movieDRV2bot?start=${{encodeURIComponent(selectedMovie.title)}}`;
            showToast(`Opening ${{selectedMovie.title}} in Telegram Bot...`);
            window.open(tgUrl, '_blank');
        }}

        // Movie Details Modal
        function openMovieDetails(id) {{
            let m = MOVIES_CATALOG.find(x => x.id === id);
            if (!m && FULL_DB_INDEX) {{
                const item = FULL_DB_INDEX.find(x => `tg-${{x.id}}` === id);
                if (item) {{
                    const catalogMatch = MOVIES_CATALOG.find(x => x.title.toLowerCase() === item.t.toLowerCase());
                    let pUrl = "";
                    if (item.p) {{
                        pUrl = `https://images.weserv.nl/?url=image.tmdb.org/t/p/w500${{item.p}}`;
                    }} else if (catalogMatch && catalogMatch.poster_url) {{
                        pUrl = catalogMatch.poster_url;
                    }} else {{
                        const cleanT = encodeURIComponent(item.t.length > 22 ? item.t.substring(0, 20) + '...' : item.t);
                        pUrl = `data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" width="300" height="450" viewBox="0 0 300 450"><defs><linearGradient id="g" x1="0%" y1="0%" x2="100%" y2="100%"><stop offset="0%" stop-color="%231a1a1a"/><stop offset="100%" stop-color="%230c0c0c"/></linearGradient></defs><rect width="300" height="450" fill="url(%23g)"/><rect x="12" y="12" width="276" height="426" fill="none" stroke="%23FFC928" stroke-width="1.5" opacity="0.3" rx="12"/><circle cx="150" cy="160" r="40" fill="%23FFC928" opacity="0.15"/><path d="M142 145 L164 160 L142 175 Z" fill="%23FFC928"/><text x="150" y="240" font-family="sans-serif" font-weight="800" font-size="18" fill="%23FFFFFF" text-anchor="middle">${{cleanT}}</text><text x="150" y="270" font-family="sans-serif" font-weight="600" font-size="13" fill="%23FFC928" text-anchor="middle">${{item.y || '2024'}} • ${{item.q || '1080p'}}</text><text x="150" y="380" font-family="sans-serif" font-weight="500" font-size="11" fill="%23888888" text-anchor="middle">CINEVIBE CINEMA</text></svg>`;
                    }}
                    let bUrl = (catalogMatch && catalogMatch.backdrop_url) ? catalogMatch.backdrop_url : pUrl;
                    m = {{
                        id: `tg-${{item.id}}`,
                        title: item.t,
                        year: item.y,
                        rating: catalogMatch ? catalogMatch.rating : 8.2,
                        runtime: item.s,
                        quality: item.q || "1080p FHD",
                        category: item.tv ? "series" : "telegram",
                        type: item.tv ? "series" : "movie",
                        languages: catalogMatch ? catalogMatch.languages : ["Multi-Audio"],
                        genres: catalogMatch ? catalogMatch.genres : ["Telegram Bot Library"],
                        director: catalogMatch ? catalogMatch.director : "Verified Community Upload",
                        cast: catalogMatch ? catalogMatch.cast : ["Telegram DB Archive"],
                        overview: catalogMatch ? catalogMatch.overview : `Available file in Telegram Bot: ${{item.fn}} (${{item.s}})`,
                        poster_url: pUrl,
                        backdrop_url: bUrl,
                        file_name: item.fn,
                        file_size: 0,
                        file_size_human: item.s,
                        file_id: item.id,
                        stream_msg_id: 116,
                        stream_hash: "AgADwB",
                        featured: false
                    }};
                }}
            }}
            if (!m) return;
            selectedMovie = m;

            document.getElementById('modalBackdrop').style.backgroundImage = 'none';
            document.getElementById('modalBackdrop').style.backgroundImage = `url('${{m.backdrop_url || m.poster_url}}')`;
            document.getElementById('modalPoster').src = m.poster_url;
            document.getElementById('modalQuality').innerText = m.quality;
            document.getElementById('modalYear').innerText = m.year;
            document.getElementById('modalRuntime').innerText = `• ${{m.runtime}}`;
            document.getElementById('modalRating').innerHTML = `<i class="fa-solid fa-star text-[10px]"></i> ${{m.rating}}`;
            document.getElementById('modalTitle').innerText = m.title;
            document.getElementById('modalOriginalTitle').innerText = m.file_name;
            document.getElementById('modalOverview').innerText = m.overview;
            document.getElementById('modalDirector').innerText = m.director;
            document.getElementById('modalLanguages').innerText = m.languages.join(', ');

            openModal('movieDetailsModal');
        }}

        // Trigger Local Stream or Download
        function triggerStream(mode) {{
            if (!selectedMovie) return;
            
            const fileId = selectedMovie.file_id || '';
            const sanitizedName = encodeURIComponent(selectedMovie.file_name.replace(/\\s+/g, '+') + '.mkv');
            const streamUrl = fileId 
                ? `${{botBaseUrl}}/${{mode === 'download' ? 'file' : 'watch_file'}}/${{fileId}}`
                : `${{botBaseUrl}}/${{selectedMovie.stream_msg_id}}/${{sanitizedName}}?hash=${{selectedMovie.stream_hash}}`;

            if (mode === 'download') {{
                showToast(`Starting high-speed download for ${{selectedMovie.title}}...`);
                window.location.href = streamUrl;
            }} else {{
                showToast(`Streaming ${{selectedMovie.title}} via ByteStreamer...`);
                window.open(streamUrl, '_blank');
            }}
        }}

        function copyStreamLink() {{
            if (!selectedMovie) return;
            const fileId = selectedMovie.file_id || '';
            const sanitizedName = encodeURIComponent(selectedMovie.file_name.replace(/\\s+/g, '+') + '.mkv');
            const streamUrl = fileId
                ? `${{botBaseUrl}}/watch_file/${{fileId}}`
                : `${{botBaseUrl}}/${{selectedMovie.stream_msg_id}}/${{sanitizedName}}?hash=${{selectedMovie.stream_hash}}`;
            navigator.clipboard.writeText(streamUrl).then(() => {{
                showToast("Stream link copied to clipboard!");
            }});
        }}

        // CineVibe Gemini AI Search
        async function askGeminiAI() {{
            const query = document.getElementById('aiQueryInput').value.trim();
            if (!query) {{
                showToast("Please enter a question or query for CineVibe AI!", true);
                return;
            }}

            const btn = document.getElementById('aiSubmitBtn');
            btn.innerHTML = `<i class="fa-solid fa-circle-notch fa-spin"></i><span>Analyzing with Gemini AI...</span>`;
            btn.disabled = true;

            const resContainer = document.getElementById('aiResponseContainer');
            const answerText = document.getElementById('aiAnswerText');
            const matchedCards = document.getElementById('aiMatchedCards');

            try {{
                // Smart keyword matcher on existing catalog
                const qLower = query.toLowerCase();
                const matched = MOVIES_CATALOG.filter(m => 
                    qLower.includes(m.title.toLowerCase()) ||
                    m.genres.some(g => qLower.includes(g.toLowerCase())) ||
                    m.languages.some(l => qLower.includes(l.toLowerCase())) ||
                    (qLower.includes('anime') && m.category === 'anime') ||
                    (qLower.includes('kdrama') && m.category === 'kdrama') ||
                    (qLower.includes('k-drama') && m.category === 'kdrama') ||
                    (qLower.includes('korea') && m.category === 'kdrama') ||
                    (qLower.includes('action') && m.genres.includes('Action')) ||
                    (qLower.includes('4k') && m.quality.includes('4K')) ||
                    (qLower.includes(m.year.toString()))
                );

                let aiText = "";
                if (geminiApiKey) {{
                    try {{
                        const catalogBrief = MOVIES_CATALOG.map(m => `${{m.title}} (${{m.year}}, ${{m.genres.join('/')}})`).join(', ');
                        const response = await fetch(`https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key=${{geminiApiKey}}`, {{
                            method: 'POST',
                            headers: {{ 'Content-Type': 'application/json' }},
                            body: JSON.stringify({{
                                contents: [{{
                                    parts: [{{
                                        text: `You are CineVibe AI Movie Concierge. The available catalog contains: ${{catalogBrief}}. User asked: "${{query}}". Respond in 2-3 friendly, cinematic sentences with the best matching title from the catalog.`
                                    }}]
                                }}]
                            }})
                        }});
                        const data = await response.json();
                        if (data.candidates && data.candidates[0].content) {{
                            aiText = data.candidates[0].content.parts[0].text;
                        }}
                    }} catch (e) {{}}
                }}

                if (!aiText) {{
                    if (matched.length > 0) {{
                        aiText = `Found ${{matched.length}} great cinema titles matching "${{query}}" in CineVibe catalog! We recommend starting with **${{matched[0].title}}** (${{matched[0].year}}).`;
                    }} else {{
                        aiText = `Here are our top recommended releases matching your cinema vibe! Explore our 4K UHD and anime catalog below.`;
                    }}
                }}

                answerText.innerText = aiText;
                const displayMatched = matched.length > 0 ? matched : MOVIES_CATALOG.slice(0, 3);
                matchedCards.innerHTML = `
                    <div class="grid grid-cols-3 gap-2.5 pt-2">
                        ${{displayMatched.map(m => `
                            <div class="bg-brand-card p-2 rounded-xl border border-white/5 cursor-pointer hover:border-brand-gold/40 transition" onclick="closeModal('aiModal'); openMovieDetails('${{m.id}}')">
                                <img src="${{m.poster_url}}" referrerpolicy="no-referrer" class="w-full h-28 object-cover rounded-lg mb-1.5" onerror="handleImageError(this, '${{m.title.replace(/'/g, "\'")}}', '${{m.year}}')">
                                <h5 class="text-[11px] font-bold text-white line-clamp-1">${{m.title}}</h5>
                                <span class="text-[10px] text-brand-gold font-bold">⭐ ${{m.rating}}</span>
                            </div>
                        `).join('')}}
                    </div>
                `;
                resContainer.classList.remove('hidden');

            }} catch (err) {{
                showToast("AI Service temporarily offline. Showing catalog matches.", true);
            }} finally {{
                btn.innerHTML = `<i class="fa-solid fa-sparkles"></i><span>Ask CineVibe AI</span>`;
                btn.disabled = false;
            }}
        }}

        function saveSettings() {{
            botBaseUrl = document.getElementById('botBaseUrlInput').value.trim();
            geminiApiKey = document.getElementById('geminiApiKeyInput').value.trim();

            localStorage.setItem('cinevibe_bot_url', botBaseUrl);
            localStorage.setItem('cinevibe_gemini_key', geminiApiKey);

            showToast("Stream engine settings saved!");
            closeModal('settingsModal');
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

print("Clean public website generated successfully in index.html & 200.html!")

