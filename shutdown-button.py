#!/usr/bin/env python3
from gpiozero import Button
from signal import pause
import os, sys

offGPIO = 17
holdTime = 1

# the function called to shut down the RPI
def shutdown():
     print('Shutdown button pressed - shutting down')
     os.system("sudo poweroff")


btn = Button(offGPIO, hold_time=holdTime)
btn.when_held = shutdown
print('Shutdown-button.py script is running - started from etc/rc.local and etc/profile')
pause()     # handle the button presses in the background
