# Write your code here :-)
# core: circuitPython-8.2.9
# dependency: adafruit-circuitpython-bundle-8.x-mpy-20231224
#                     __
#               GP0--|  |--VBUS
#               GP1        VSYS
#               GND        GND
#     Z |---/ --GP2        3V3EN
#     X |---/ --GP3        3V3OUT
# ENTER |---/ --GP4        VREF
#  DOWN |---/ --GP5        GP28 --/ ---| SPACE
#               GND  ____  GND
# RIGHT |---/ --GP6 | RP | GP27
#               GP7 |2040| GP26
#  LEFT |---/ --GP8  ----  RUN
#    UP |---/ --GP9        GP22

import board
import digitalio

import time
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode

kbd = Keyboard(usb_hid.devices)



keycodes = [Keycode.UP_ARROW, Keycode.DOWN_ARROW, Keycode.LEFT_ARROW, Keycode.RIGHT_ARROW,
            Keycode.X, Keycode.Z, Keycode.SPACE, Keycode.ENTER]

btn_up = digitalio.DigitalInOut(board.GP9)
btn_up.switch_to_input(pull=digitalio.Pull.UP)
btn_dn = digitalio.DigitalInOut(board.GP5)
btn_dn.switch_to_input(pull=digitalio.Pull.UP)
btn_lt = digitalio.DigitalInOut(board.GP8)
btn_lt.switch_to_input(pull=digitalio.Pull.UP)
btn_rt = digitalio.DigitalInOut(board.GP6)
btn_rt.switch_to_input(pull=digitalio.Pull.UP)
btn_bb = digitalio.DigitalInOut(board.GP2)
btn_bb.switch_to_input(pull=digitalio.Pull.UP)
btn_aa = digitalio.DigitalInOut(board.GP3)
btn_aa.switch_to_input(pull=digitalio.Pull.UP)
btn_se = digitalio.DigitalInOut(board.GP28)
btn_se.switch_to_input(pull=digitalio.Pull.UP)
btn_st = digitalio.DigitalInOut(board.GP4)
btn_st.switch_to_input(pull=digitalio.Pull.UP)

last_pressed = 255



while True:
    
    k_up = 0 if btn_up.value == True else 1
    k_dn = 0 if btn_dn.value == True else 1
    k_lt = 0 if btn_lt.value == True else 1
    k_rt = 0 if btn_rt.value == True else 1
    k_aa = 0 if btn_aa.value == True else 1
    k_bb = 0 if btn_bb.value == True else 1
    k_se = 0 if btn_se.value == True else 1
    k_st = 0 if btn_st.value == True else 1
    
    this_pressed = \
                 k_up << 0 | \
                 k_dn << 1 | \
                 k_lt << 2 | \
                 k_rt << 3 | \
                 k_aa << 4 | \
                 k_bb << 5 | \
                 k_se << 6 | \
                 k_st << 7 
    
    if (this_pressed != last_pressed):
        #new keypresses
        for i in range(8):
            if (this_pressed & 1<<i) and not (last_pressed & 1<<i):
                kbd.press(keycodes[i])
            if (last_pressed & 1<<i) and not (this_pressed & 1<<i):
                kbd.release(keycodes[i])
        last_pressed = this_pressed
    time.sleep(0.01)