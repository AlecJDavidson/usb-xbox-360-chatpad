import board
import busio
from time import sleep, monotonic

debug_enabled = True
if debug_enabled:
    print("Debug Enabled:", debug_enabled)
    print("Running and ready to debug.")

# Define UART connection
uart = busio.UART(board.TX, board.RX, baudrate=9600)

# Initialize variables for debounce mechanism
last_key = None
last_key_time = 0
debounce_delay = 0.1 # Adjust this value as needed

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
            return None # Ignore the keypress
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

            # Print to serial console
            if isinstance(key, str): # If it's a string...
                print("Key Pressed:", key)
    except Exception as e:
        # Print any exception that occurs
        print("Error:", e)
