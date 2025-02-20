import os, sys, io
import M5
from M5 import *
from hardware import I2C
from hardware import Pin
from unit import Encoder8Unit
import time

i2c0 = None
encoder8_0 = None

# Store previous states for comparison
previous_values = {f"v{i}": 0 for i in range(1, 9)}
previous_buttons = {f"b{i}": 0 for i in range(1, 9)}
previous_switch = None
led_timers = {i: 0 for i in range(1, 9)}

def setup():
    global i2c0, encoder8_0, previous_switch

    M5.begin()
    i2c0 = I2C(0, scl=Pin(1), sda=Pin(2), freq=1000000)
    encoder8_0 = Encoder8Unit(i2c0, 0x41)
    
    # Initialize previous switch state
    previous_switch = encoder8_0.get_switch_status()

def light_up_led(index):
    encoder8_0.set_led_rgb(index, 0x6600cc)  # Set LED to purple
    led_timers[index] = time.ticks_ms()  # Store current time

def update_leds():
    current_time = time.ticks_ms()
    for i in range(1, 9):
        if led_timers[i] and time.ticks_diff(current_time, led_timers[i]) > 100:
            encoder8_0.set_led_rgb(i, 0x000000)  # Turn off LED
            led_timers[i] = 0  # Reset timer

def loop():
    global i2c0, encoder8_0, previous_values, previous_buttons, previous_switch

    M5.update()
    update_leds()

    # Check encoder values
    for i in range(1, 9):
        new_value = encoder8_0.get_increment_value(i)
        if new_value != previous_values[f"v{i}"]:
            print(f"v{i}:{new_value}")
            previous_values[f"v{i}"] = new_value
            light_up_led(i)

        new_button = 1 if encoder8_0.get_button_status(i) else 0  # Convert True/False to 1/0
        if new_button != previous_buttons[f"b{i}"]:
            print(f"b{i}:{new_button}")
            previous_buttons[f"b{i}"] = new_button
            light_up_led(i)

    # Check switch status
    new_switch = 1 if encoder8_0.get_switch_status() else 0
    if new_switch != previous_switch:
        print(f"s:{new_switch}")
        previous_switch = new_switch

if __name__ == '__main__':
    try:
        setup()
        while True:
            loop()
    except (Exception, KeyboardInterrupt) as e:
        try:
            from utility import print_error_msg
            print_error_msg(e)
        except ImportError:
            print("please update to latest firmware")
