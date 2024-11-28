import board
import digitalio
from time import sleep, monotonic
import busio

# HID Keyboard
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from adafruit_hid.keycode import Keycode

debug_enabled = False 
if debug_enabled:
        print("Debug Enabled: ", debug_enabled)
        print("Running and ready to debug.")

def debug_messages(enabled: bool, key):
    if enabled:
        print("Key Pressed: ", key)

# Define UART connection
uart = busio.UART(board.TX, board.RX, baudrate=9600)

# Initialize variables for debounce mechanism
last_key = None
last_key_time = 0
debounce_delay = 0.1  # Adjust this value as needed

def debounce(key):
    global last_key
    global last_key_time

    # Check if the received key is the same as the last key
    if key == last_key:
        # Check if enough time has passed since the last keypress
        if (monotonic() - last_key_time) >= debounce_delay:
            last_key_time = monotonic()
            return key
        else:
            return None  # Ignore the keypress
    else:
        last_key = key
        last_key_time = monotonic()
        return key

while True:
    try:
        # Check if there's any data available on UART
        if uart.in_waiting > 0:
            # Read and print the received data
            received_data = uart.read(uart.in_waiting).decode("utf-8")
            key = debounce(received_data)

            # Initialize keyboard and keyboard layout
            keyboard = Keyboard(usb_hid.devices)
            keyboard_layout = KeyboardLayoutUS(keyboard)  # US Layout

            # Handle keypress
            if isinstance(key, str):  # If it's a string...
                # Handle Enter Key Press
                if key == '\r':
                    keyboard.press(Keycode.ENTER)
                    keyboard.release_all()  # ..."Release"!

                else:
                    keyboard_layout.write(key)  # ...Print the string
                    keyboard.release_all()  # ..."Release"!

    except Exception as e:
        # Print any exception that occurs
        print("Error:", e)
