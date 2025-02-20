# m5stack
UIFlow2 Projects


# Encoder8Unit

## Overview
This script is designed to interface with an M5Stack device and an Encoder8Unit module via I2C. It continuously monitors encoder values and button presses and provides visual feedback by briefly lighting up the corresponding LED when a change is detected.
Test it with https://webserial.io/

## Serial Output
```
v6:-2␍␊
v6:-1␍␊
v6:-2␍␊
v6:-1␍␊
v6:-2␍␊
v6:0␍␊
v6:1␍␊
v6:0␍␊
v6:1␍␊
v6:2␍␊
v6:0␍␊
v6:1␍␊
v6:0␍␊
v8:-1␍␊
v8:0␍␊
v8:-2␍␊
v8:0␍␊
s:1␍␊
s:0␍␊
```

## Features
- Reads incremental values from 8 rotary encoders.
- Detects button presses on each encoder.
- Detects the status of a switch.
- Provides LED feedback when an encoder value changes or a button is pressed.
- Uses a non-blocking method to turn off LEDs after a short delay.

## How It Works
1. **Setup Phase:**
   - Initializes the M5Stack device and the I2C communication.
   - Sets up the Encoder8Unit module.
   - Stores the initial state of the switch.

2. **Loop Execution:**
   - Continuously updates the M5 system.
   - Checks encoder values and button statuses.
   - If a value change or button press is detected, the corresponding LED is lit up momentarily.
   - Uses a timer-based approach to turn off LEDs after 100ms.
   - Prints encoder values and button states to the console.

## Function Descriptions
- `setup()`: Initializes the system and prepares the Encoder8Unit.
- `light_up_led(index)`: Lights up the LED at the given index and stores the activation time.
- `update_leds()`: Checks if the LEDs should be turned off based on elapsed time.
- `loop()`: Main execution loop that updates encoder values, button presses, and LEDs.

## Exception Handling
The script includes error handling for exceptions and keyboard interrupts. If an error occurs, it attempts to print an error message, suggesting a firmware update if necessary.

## Dependencies
- `M5` library
- `hardware` module
- `unit` module
- `time` module (for non-blocking LED timing)

