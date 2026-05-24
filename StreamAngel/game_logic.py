# This file handles all the game logic like tracking player stats,
# saving and loading the game, and picking which event shows up next.
# all follower and money values stored in k units. 

import json
import os
import random
import copy
from game_text import EVENTS, ENDINGS, DANMAKU_POOL, DIARY_LINES

# Use absolute paths so files are always created next to game_logic.py,
# regardless of which directory the user runs python from.
_HERE = os.path.dirname(os.path.abspath(__file__))
SAVE_FILE  = os.path.join(_HERE, "save.json")
DIARY_FILE = os.path.join(_HERE, "diary.txt")
MAX_TURNS = 30
RENT_EVERY = 3      # rent is charged every 3 turns
RENT_COST = 20      # how much rent costs each time (in k units, so 20k)
NEG_CHANCE = 0.70   # 70% chance the next event will be a negative one
AD_DIVISOR = 20     # every 20k followers = 1k ad revenue
RECOVERY = 3        # stress and edge decrease by this amount every day (every 3 turns)

# Dream ending conditions
DREAM_FOLLOWERS = 1000
DREAM_STRESS_MAX = 70
DREAM_EDGE_MAX = 70

class GameState:
    """This class holds all variables for a player's playthrough."""
    
    def __init__(self):
        self.day = 1
        self.stress = 5        # from 0 to 100
        self.edge = 5          # from 0 to 100
        self.followers = 100    # stored in k units (100 = 100k followers)
        self.money = 40         # stored in k units (40 = $40k)
        self.turn = 0          
        self.log = []          

    def apply_choice(self, effect):
        """Changes stats based on user selection and clamps numbers."""
        self.stress += effect.get("stress", 0)
        self.edge += effect.get("edge", 0)
        self.followers += effect.get("followers", 0)
        self.money += effect.get("money", 0)
        
        # Make sure none of the stats go outside their allowed range
        self.stress = max(0, min(100, self.stress))
        self.edge = max(0, min(100, self.edge))
        self.followers = max(0, self.followers)

    def next_turn(self):
        """Moves game turn forward. Calculates rent and Ad revenue every 3 turns."""
        self.turn += 1
        if self.turn % RENT_EVERY == 0:
            self.day += 1
            
            # calculate ad money based on follower count
            ad_revenue = self.followers // AD_DIVISOR
            self.money += ad_revenue - RENT_COST

            # Resting on day update slightly recovers your stress and edge
            self.stress = max(0, self.stress - RECOVERY)
            self.edge = max(0, self.edge - RECOVERY)

            # Write Angel-chan's private diary entry — includes real stat data + inner thought
            diary_line = write_diary_entry(self.day, self.stress, self.edge, self.followers, self.money, ad_revenue)
            
            notice = f"Day {self.day} Update | Internet Bill: -{RENT_COST}k | Ad Revenue: +{ad_revenue}k | Rest: Stress/Edge -{RECOVERY}"
            # Return both the system notice and the diary line as a tuple
            return notice, diary_line
        return None, None

    def check_ending(self):
        """Checks if stats triggered any special game over or win condition."""
        # Bad endings trigger immediately during the game
        if self.stress >= 100:
            return "stress"
        if self.edge >= 100:
            return "edge"
        if self.money <= 0:
            return "money"
        # Check all endings once 30 turns are complete
        if self.turn >= MAX_TURNS:
            # Dream end: 1 million fans AND both stress and edge under 80
            if self.followers >= DREAM_FOLLOWERS and self.stress < DREAM_STRESS_MAX and self.edge < DREAM_EDGE_MAX:
                return "dream"
            # Dark lord: fame but lost your mind
            elif (self.stress >= 80 or self.edge >= 80) and self.followers >= 500:
                return "dark_lord"
            # Mid crisis: unwell AND stuck in obscurity
            elif (self.stress >= 80 or self.edge >= 80) and self.followers < 500:
                return "mid_crisis"
            # Normal streamer: sane but not famous enough for dream end
            else:
                return "normal_streamer"
        return None

    def get_stats(self):
        """Pack stats into python dictionary for json storage."""
        data_dict = {
            "day": self.day, 
            "stress": self.stress, 
            "edge": self.edge,
            "followers": self.followers, 
            "money": self.money,
            "turn": self.turn, 
            "log": self.log
        }
        return data_dict

    def load_stats(self, data):
        """Unpack data from dictionary back into the object."""
        self.day = data.get("day", 1)
        self.stress = data.get("stress", 5)
        self.edge = data.get("edge", 5)
        self.followers = data.get("followers", 100)
        self.money = data.get("money", 50)
        self.turn = data.get("turn", 0)
        self.log = data.get("log", [])


# Diary system

def write_diary_entry(day, stress, edge, followers, money, ad_revenue):
    """Picks a mood-appropriate diary line and appends it to diary.txt.

    Each entry has two parts:
      Line 1 — the real stat snapshot (stress, fans, cash, ad income)
      Line 2 — Angel-chan's inner monologue, picked by mood
    """
    # Choose which pool to draw from based on current stress and edge
    if stress >= 70 and edge >= 70:
        mood = "breaking"
    elif edge >= 60:
        mood = "edgy"
    elif stress >= 60:
        mood = "stressed"
    else:
        mood = "calm"

    inner_thought = random.choice(DIARY_LINES[mood])

    # Build the data header — this is the stats record for the day
    data_header = (
        f"Day {day} | Stress {stress} | Edge {edge} | "
        f"Fans {followers}k | Cash ${money}k | Ad Revenue +{ad_revenue}k"
    )
    # Full diary entry: stats on line 1, inner thought on line 2
    entry = f"[{data_header}]\n  {inner_thought}\n\n"

    try:
        # 'a' mode appends each day without overwriting older entries
        with open(DIARY_FILE, "a", encoding="utf-8") as f:
            f.write(entry)
    except Exception as e:
        print(f"Diary write error: {e}")

    # Return only the inner thought for the sidebar peek display
    return inner_thought


def read_diary_entries():
    """Reads diary.txt and returns the last 5 entries as a list of strings.

    Each entry is a two-line block separated by a blank line, so we split
    on double-newline to get one complete entry string per day.
    """
    if not os.path.exists(DIARY_FILE):
        return []
    try:
        with open(DIARY_FILE, "r", encoding="utf-8") as f:
            raw = f.read()
        # Split on blank lines — each chunk is one day's entry
        entries = [block.strip() for block in raw.split("\n\n") if block.strip()]
        return entries[-5:]   # only return the most recent 5
    except Exception as e:
        print(f"Diary read error: {e}")
        return []


# Functions to save and load the game using a JSON file

def save_game(state, current_event):
    """Saves player stats and the current pending event to save.json."""
    try:
        save_data = {
            "state": state.get_stats(),
            "current_event": current_event
        }
        with open(SAVE_FILE, "w", encoding="utf-8") as f:
            json.dump(save_data, f, indent=2, ensure_ascii=False)
        return True
    except Exception as e:
        print(f"Save error occurred: {e}")
        return False

def load_game():
    """Reads save.json and returns (state, current_event), or (None, None) on failure."""
    if not os.path.exists(SAVE_FILE):
        return None, None
    try:
        with open(SAVE_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
        # Support old save format that only stored stats directly
        if "state" not in data:
            return None, None
        state = GameState()
        state.load_stats(data["state"])
        current_event = data.get("current_event", None)
        return state, current_event
    except Exception as e:
        print(f"Load error occurred: {e}")
        return None, None


# This function picks a random event and adjusts the money rewards based on followers

def get_current_event(state):
    """
    Picks a random event and scales the money rewards dynamically 
    based on how many followers the player has.
    """
    if random.random() < NEG_CHANCE:
        category = "negative"
    else:
        category = "positive"
        
    event_template = random.choice(EVENTS[category])
    
    current_event = copy.deepcopy(event_template)
    current_event["category"] = category
    
    # pick 20 random chat messages to show in the background
    current_event["bg_chat"] = random.sample(DANMAKU_POOL, 20)
    
    # the more followers you have, the more money/followers positive choices give you
    import math
    bonus_multiplier = 1.0 + math.sqrt(state.followers / 100) * 0.5
    
    for option in current_event["options"]:
        # apply the bonus to options that actually reward money or followers
        if option["effect"]["money"] > 0:
            base_money = option["effect"]["money"]
            option["effect"]["money"] = int(base_money * bonus_multiplier)
        if option["effect"]["followers"] > 0:
            base_followers = option["effect"]["followers"]
            option["effect"]["followers"] = int(base_followers * bonus_multiplier)
            
    return current_event

def get_ending(key):
    """Looks up full text block for a specific ending code."""
    return ENDINGS.get(key, {"title": "Error", "text": "The timeline fractured."})
