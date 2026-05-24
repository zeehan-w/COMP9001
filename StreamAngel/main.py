# This file runs the game by starting a local web server on port 8888.
# It also opens the browser automatically so the user doesn't have to do it manually.

import json
import threading
import webbrowser
import os
import time
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse

from game_logic import GameState, save_game, load_game, get_current_event, get_ending, read_diary_entries

PORT = 8888

# These two variables store the current game state and event for the whole session
state = GameState()
current_event = None

class GameHandler(BaseHTTPRequestHandler):
    """Custom request handler that receives browser inputs and sends responses."""

    def log_message(self, format, *args):
        # This stops the terminal from printing a new line every time the browser sends a request
        pass

    def do_GET(self):
        """Delivers index.html page when user connects to the web browser."""
        path = urlparse(self.path).path

        if path == "/" or path == "/index.html":
            self.serve_file("index.html", "text/html")
        else:
            self.send_data(404, "text/plain", b"Not found")

    def do_POST(self):
        """Processes API endpoints for choice picking, saving and loading."""
        path = urlparse(self.path).path
        body = self.read_body()

        if path == "/new_game":
            self.handle_new_game()
        elif path == "/choose":
            chosen_index = body.get("index", 0)
            self.handle_choice(chosen_index)
        elif path == "/save":
            self.handle_save()
        elif path == "/load":
            self.handle_load()
        elif path == "/diary":
            self.handle_diary()
        else:
            self.send_data(404, "text/plain", b"Not found")

    # These functions handle what happens when the player does something in the game

    def handle_new_game(self):
        global state, current_event
        state = GameState()
        current_event = get_current_event(state)
        # Clear the diary file so a fresh run starts with no old entries
        try:
            diary_path = os.path.join(os.path.dirname(__file__), "diary.txt")
            if os.path.exists(diary_path):
                os.remove(diary_path)
        except Exception as e:
            print(f"Could not clear diary on new game: {e}")
        response_data = {
            "status": "ok", 
            "state": state.get_stats(), 
            "event": current_event
        }
        self.send_json(response_data)

    def handle_choice(self, index):
        global state, current_event

        # Make sure the index is valid before doing anything
        if current_event is None:
            self.send_json({
                "status": "error",
                "message": "No event found"
            })
            return
            
        if index < 0 or index >= len(current_event["options"]):
            self.send_json({
                "status": "error",
                "message": "Invalid index selection"
            })
            return

        chosen_option = current_event["options"][index]
        state.apply_choice(chosen_option["effect"])
        state.log.append(chosen_option["desc"])
        state.log = state.log[-6:]  # only keep the last 6 entries so the log doesn't get too long

        # Move to the next turn; next_turn returns (notice_message, diary_line)
        notice_message, diary_line = state.next_turn()
        ending_found = state.check_ending()

        if ending_found:
            self.send_json({
                "status": "ending",
                "ending": get_ending(ending_found),
                "state": state.get_stats(),
                "desc": chosen_option["desc"],
                "sfx": chosen_option.get("sfx", "click"),
                "notice": notice_message,
                "diary_line": diary_line
            })
            return

        # Get the next event based on the player's updated follower count
        current_event = get_current_event(state)
        self.send_json({
            "status": "ok",
            "state": state.get_stats(),
            "event": current_event,
            "desc": chosen_option["desc"],
            "sfx": chosen_option.get("sfx", "click"),
            "notice": notice_message,
            "diary_line": diary_line
        })

    def handle_diary(self):
        """Returns the last few diary entries so the frontend can display them."""
        entries = read_diary_entries()
        self.send_json({
            "status": "ok",
            "entries": entries
        })

    def handle_save(self):
        success = save_game(state, current_event)
        if success:
            self.send_json({
                "status": "ok",
                "message": "Progress saved successfully!"
            })
        else:
            self.send_json({
                "status": "error",
                "message": "Failed to write save file to disk."
            })

    def handle_load(self):
        global state, current_event
        loaded_state, loaded_event = load_game()

        if loaded_state is None:
            self.send_json({
                "status": "error",
                "message": "No valid save data was found on disk."
            })
            return

        state = loaded_state
        # Restore the exact event the player was looking at when they saved
        if loaded_event is not None:
            current_event = loaded_event
        else:
            current_event = get_current_event(state)
        self.send_json({
            "status": "ok",
            "message": "Save loaded successfully! Welcome back to streaming.",
            "state": state.get_stats(),
            "event": current_event
        })

    # These are helper functions for reading and sending data over the network

    def read_body(self):
        """Helper to safely read incoming JSON request bodies."""
        length = int(self.headers.get("Content-Length", 0))
        if length == 0:
            return {}
        try:
            return json.loads(self.rfile.read(length))
        except Exception:
            return {}

    def send_json(self, data):
        """Helper to send JSON payloads back to the frontend browser."""
        json_string = json.dumps(data, ensure_ascii=False)
        payload = json_string.encode("utf-8")
        self.send_data(200, "application/json", payload)

    def serve_file(self, filename, content_type):
        """Helper to fetch files locally off the drive folder with error prevention."""
        filepath = os.path.join(os.path.dirname(__file__), filename)
        try:
            with open(filepath, "rb") as f:
                self.send_data(200, content_type, f.read())
        except FileNotFoundError:
            self.send_data(404, "text/plain", b"File not found")

    def send_data(self, code, content_type, body):
        """Sends raw low-level HTTP network headers."""
        self.send_response(code)
        self.send_header("Content-Type", f"{content_type}; charset=utf-8")
        self.send_header("Content-Length", len(body))
        self.send_header("Access-Control-Allow-Origin", "*")
        self.end_headers()
        self.wfile.write(body)


def open_browser():
    time.sleep(0.8)
    webbrowser.open(f"http://127.0.0.1:{PORT}")

if __name__ == "__main__":
    server = HTTPServer(("127.0.0.1", PORT), GameHandler)
    print("=" * 50)
    print("       † DREAM ★ ANGEL ONLINE †")
    print(f"    Running local backend server at port: {PORT}")
    print("    Open your browser to start the simulation!")
    print("    Use Ctrl+C to close down the system safely.")
    print("=" * 50)

    # Set background thread to open the tab automatically
    browser_thread = threading.Thread(target=open_browser)
    browser_thread.daemon = True
    browser_thread.start()

    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nStream closed down safely.")