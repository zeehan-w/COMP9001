[README.txt](https://github.com/user-attachments/files/28196240/README.txt)
# COMP9001
StreamAngel game
COMP9001
--------------------------------------------------------------------------------
SPECIAL NOTES
--------------------------------------------------------------------------------

  - This program uses a web-based UI (index.html rendered in the browser).
  - The backend is 100% Python using only the built-in http.server.
    Please run 'python3 main.py' and interact through your web browser.
  - If port 8888 is in use, the program will fail to start.
    Close any other running instances or change the PORT variable in main.py.
  - save.json and diary.txt are dynamically generated data files. 
    They are completely safe to overwrite or delete at any time.

--------------------------------------------------------------------------------
HOW TO RUN
--------------------------------------------------------------------------------

  python3 main.py

  The program will automatically:
    1. Start a local lightweight web server on port 8888.
    2. Open your default web browser directly to http://127.0.0.1:8888.
    3. Load the interactive game UI — just start clicking!

  To quit: press Ctrl+C in your terminal window.

  NOTE: If the browser does not open automatically, open it manually and
  navigate to: http://127.0.0.1:8888

--------------------------------------------------------------------------------
REQUIREMENTS & DEPENDENCIES
--------------------------------------------------------------------------------

  Python 3.10

    http.server   — runs the local lightweight web server 
    json          — saves/loads game data + handles frontend-backend API 
    threading     — auto-launches the browser without blocking the server 
    webbrowser    — opens the local game URL in your default browser 
    random        — handles event selection, chat pools, and diary thoughts 
    os            — manages pathing and file verification safely 
    copy          — performs deep-copies on event templates safely 
    math          — scales choices dynamically using sqrt() based on popularity 
    urllib.parse  — parses incoming HTTP request paths 

  The frontend UI (index.html) runs entirely in the browser.
  No Node.js, no npm, and no external CSS/JS dependencies required.

--------------------------------------------------------------------------------
PROJECT FILES STRUCTURE
--------------------------------------------------------------------------------

  main.py        ← START HERE. Contains the HTTP server & API endpoint handlers.
  game_logic.py  ← GameState manager, data progression mechanics, and event handlers.
  game_text.py   ← All database pools: story events, chat overlay (danmaku), and endings.
  index.html     ← Browser-based responsive UI (HTML + CSS layout + JavaScript network client).
  save.json      ← Automatically created/updated when you click Save in-game.
  diary.txt      ← Private diary file written by Angel-chan every 3 turns. Append-only.
  README.txt     ← This file.

--------------------------------------------------------------------------------
CORE GAMEPLAY & MECHANICS
--------------------------------------------------------------------------------

  You play as an aspiring small streamer starting with 100k followers. 
  Your goal is to scale your channel to 1 million fans (1000k) without burning out 
  or going bankrupt over a tight timeline of 30 turns.

  Each turn, your live chat sends messages. You must select one of 3 
  response styles, directly shifting your core stats and shaping your future.

  REWARD SCALING SYSTEM
  ---------------------------
  The game features a dynamic multiplier system ($1.0 + \sqrt{\text{followers}/100} \times 0.5$). 
  As your channel grows, positive outcomes scale up significantly, giving you larger 
  sums of money and wider audience boosts for your successful streams!

  CORE STATS
  ----------
    STRESS   (0–100)  High-intensity or successful performance raises stress.
                      Hits 100 → Triggers an instant Burnt Out ending.
    EDGE     (0–100)  Toxic, edgy, or chaotic replies raise your edge meter.
                      Hits 100 → Triggers an instant Toxic Royalty ending.
    MONEY    ($k)     Your operating capital. Stored in k units.
                      Drops to or below 0 → Triggers an instant Connection Lost ending.
    FANS     (k)      Your subscriber base. Start at 100k. Reach 1000k (1 million) 
                      while keeping sanity balanced to unlock the best ending.

  AUTOMATIC CALENDAR EVENTS (Occurs every 3 turns = 1 Day Update)
  -----------------------------------------------------------------------
    - Internet Bill:  -20k deducted automatically for stream bandwidth.
    - Ad Revenue:     Passive income based on growth (+followers ÷ 20).
    - Rest Recovery:  Stress and Edge meters naturally decrease by 3 points.
    - Private Diary: Angel-chan records a snapshot of her stats along with 
                     an inner monologue based entirely on her current mental mood 
                     (Calm, Stressed, Edgy, or Breaking) into diary.txt.

--------------------------------------------------------------------------------
ENDINGS (6 TOTAL)
--------------------------------------------------------------------------------

  ✦ Dream End       — Reach 1,000k fans with both Stress & Edge strictly under 70. 
                       The ultimate, wholesome angel streamer.
  ✦ Dark Lord       — Reach 500k+ fans but let your Stress or Edge climb to 80+. 
                       You won immense fame, but lost your soul along the way.
  ✦ Mid Crisis      — Trapped under 500k fans with high Stress or Edge (80+). 
                       Unwell, unstable, and stuck in mid-tier streaming limbo forever.
  ✦ Normal Streamer — Survive all 30 turns with stable mental meters, but fail 
                       to hit the massive fan milestones.
  ✦ Burnt Out       — [Instant GameOver] Stress hits 100.
  ✦ Toxic Royalty   — [Instant GameOver] Edge hits 100.
  ✦ Connection Lost — [Instant GameOver] Money falls to $0k or below.

--------------------------------------------------------------------------------
DATA PERSISTENCE (SAVE / LOAD / DIARY)
--------------------------------------------------------------------------------

  - Click the SAVE button in-game to write your status, logs, and current pending 
    event into save.json.
  - Click the LOAD button to instantly resume from your exact point in time.
  - Starting a "New Game" completely clears out old diary entries to prevent timeline 
    clutter, giving you a fresh start!
