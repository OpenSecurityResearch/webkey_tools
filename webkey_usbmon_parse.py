#!/usr/bin/env python

# webkey_usbmon_parse.py - Simple script to 
#	parse usbmon data from USB Webkeys 
#	emulating USB HID Keyboards
#
#	Specifically the one labeled WEB-130C
#
# See http://blog.opensecurityresearch.com/2012/10/hacking-usb-webkeys.html
# for more info
#
#	brad.antoniewicz@foundstone.com
#


import sys

# 1 = verbose; 2 = more verbose
verbose=0

# There is definitely a more accurate way to do this, 
# but it gets the job done :)

keycodes = { 	
		'00': '',
		'02': 'Keyboard Left Shift',
		'04': 'Keyboard Left Alt',
		'08': 'Keyboard Left GUI',
		'15': 'Keyboard r and R',
		'28': 'Enter Key',
		'2A': 'Backspace',
		'47': 'Keyboard Scroll Lock',
		'4A': 'Keyboard Home',
		'4D': 'Keyboard End',
		'53': 'Keypad NumLock',
		'59': 'Keypad 1',
		'5A': 'Keypad 2',
		'5B': 'Keypad 3',
		'5C': 'Keypad 4',
		'5D': 'Keypad 5',
		'5E': 'Keypad 6',
		'5F': 'Keypad 7',
		'60': 'Keypad 8',
		'61': 'Keypad 9',
		'62': 'Keypad 0'
		
	}


file = open(sys.argv[1], 'r')

print "[+] Opening file: ",file.name

for line in file:
	line.rstrip()
	if verbose > 1:
		print line
	t = line.split(' ')
	# Only take lines of an appropriate size 
	if len(t) == 9:
		# Match Callbacks (C) and packets with data fields (=)
		if t[2] == 'C' and t[6] == '=':
			print t[7]," =\t",
			v = t[7].upper()
			u = [v[x:x+2] for x in xrange(0,len(t),2)]
			if u[0] in keycodes and u[2] in keycodes:
				print keycodes[u[0]],"+",keycodes[u[2]]
			else:
				print "Unknown!"		
				 
file.close()
