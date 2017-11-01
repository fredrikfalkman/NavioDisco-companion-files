#!/usr/bin/env python3

from goprocam import GoProCamera
from goprocam import constants

gopro = GoProCamera.GoPro(constants.gpcontrol)
gopro.stream('udp://94.234.203.109:5000')

#gopro.shutter(constants.start)
