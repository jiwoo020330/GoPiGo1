#!/usr/bin/env python
from __future__ import print_function
from __future__ import division
from builtins import input

'''
## License
 GoPiGo for the Raspberry Pi: an open source robotics platform for the Raspberry Pi.
 Copyright (C) 2015  Dexter Industries
This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.
This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.
You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/gpl-3.0.txt>.
'''

from gopigo import *
import sys

import atexit
atexit.register(stop)

def print_menu():
	print( "  f	:	Move the GoPiGo forward")
	print( "  l	:	Turn the GoPiGo left")
	print( "  b	:	Move the GoPiGo back")
	print( "  r	:	Turn the GoPiGo right")
	print( "  rl:	Rotate the GoPiGo left in place")
	print( "  rr:	Rotate the GoPiGo right in place")
	print( "  s:	Stop the GoPiGo")
	print( "  sp10:	Increase the speed by 10 (default 200, min:0 max 255)")
	print( "  re10:	Reduce the speed by 10")
	print( "  print volt:	Print the voltage of the batteries (should be greater than 10)")
	print( "  serpos:	Set servo position")
	print( "  ser180:	Run a servo 180 degree sweep")
	print( "  d:	Get the distance from the ultrasonic ranger")
	print( "  led:	Turn the LED's on and off")
	print( "  printfirm	:	Print the firmware version on the GoPiGo")
	print( "  tr:	Read the trim value on the GoPiGo")
	print( "  tw:	Write the trim value to the GoPiGo")
	print( "  tt:	Test the trim value to the GoPiGo")
	print( "  printmenu:	Print the menu again")
	print( "  e:	Exit")
	print( "Please type a command and press ENTER: ")

print( "  ____       ____  _  ____       ")
print( " / ___| ___ |  _ \(_)/ ___| ___  ")
print( "| |  _ / _ \| |_) | | |  _ / _ \ ")
print( "| |_| | (_) |  __/| | |_| | (_) |")
print( " \____|\___/|_|   |_|\____|\___/ ")
print( "")
print( "Welcome to GoPiGo Basic test program\nYou can use this to try out the various features of your GoPiGo\n")
print_menu()
while True:
	print( "\nCmd:",end="")
	a=input()
	if a=='f':
		fwd()
	elif a=='l':
		left()
	elif a=='r':
		right()
	elif a=='b':
		bwd()
	elif a=='s':
		stop()
	elif a=='sp10':
		increase_speed()
	elif a=='re10':
		decrease_speed()
	elif a=='print volt':
		print( "{}V".format(volt()))
	elif a=='ser180': #servo test
		for i in range(180):
			servo(i)
			print( i)
			time.sleep(.02)
	elif a=='e':
		sys.exit()
	elif a=='d':
		print( '{}cm'.format(us_dist(15)))
	elif a=='led':
		led_on(0)
		led_on(1)
		time.sleep(1)
		led_off(0)
		led_off(1)
	elif a=='i':
		motor_fwd()
	elif a=='k':
		motor_bwd()
	elif a=='rl':
		left_rot()
	elif a=='rr':
		right_rot()
	elif a=='y':
		enc_tgt(1,1,18)
	elif a=='printfirm':
		print( "v{}".format(fw_ver()))
	elif a=='tr':
		val=trim_read()
		if val==-3:
			print( "-3, Trim Value Not set")
		else:
			print( val-100)
	elif a=='tw':
		print( "Enter trim value to write to EEPROM(-100 to 100):",end="")
		val=int(input())
		trim_write(val)
		time.sleep(.1)
		print( "Value in EEPROM: {}".format(trim_read()-100))
	elif a=='tt':
		print( "Enter trim value to test(-100 to 100):",end="")
		val=int(input())
		trim_test(val)
		time.sleep(.1)
		print( "Value in EEPROM: {}".format(trim_read()-100))
	elif a=='st':
		print( "Enter Servo position:",end="")
		val=int(input())
		servo(val)
	elif a=='?':
		print_menu()
	time.sleep(.1)
