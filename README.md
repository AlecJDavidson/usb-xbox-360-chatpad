# Raspberry Pi Pico Xbox 360 Chatpad Interpreter

This project allows you to interpret serial commands from a modified Xbox 360 chatpad using a Raspberry Pi Pico. To get started, follow the instructions below:

## Prerequisites
- A Raspberry Pi Pico board
- A modified Xbox 360 chatpad with a 6 pin female dupont header soldered on (instructions provided)
- Pickit3 HAS TO BE A PICKit3!
- CircuitPython CLI installed

## Steps
1. **Flash the chatpad**: Connect the chatpad to the Pickit3 and use it to flash the included hex file onto the chatpad. The stock chatpad hex file dump is also included for reversing changes if needed.
2. **Connect the chatpad to the Pico**: Wire up the chatpad to the Raspberry Pi Pico as follows:
   - TX of the chatpad (pin 2) to RX pin on the pico (Pin 0)
   - RX of the chatpad (pin 3) to TX (pin 1) on the pico.
   - Pin 4 on the chatpad to ground on the pico.
   - Pin 1 on the chatpad to 3.3v on the pico.
   **Important**: Do not wire the chatpad to the pico before flashing! The pico should be turned off during this process, as a serial connection between the two can interfere with flashing.

3. **Program the Pico**: Use the Adafruit CircuitPython .uf2 file included in this project. Then copy the code.py file onto the Raspberry Pi Pico replacing the one that is already there.

**Note**: Detailed instructions and pictures will be added as soon as possible.

## Usage
Once the pico is programmed, it should interpret the serial commands coming from the modified chatpad and convert those into HID keypresses.

If you have any questions or issues, feel free to reach out!
