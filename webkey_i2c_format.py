#!/usr/bin/env python
#
# webkey_i2c_format.py -
# 	simple script to convert an ascii string
#	into hex and prepare it for i2c writing
#	using the bus pirate's commands
#
# 	This was made specific for the EEPROM used
#	with USB Webkeys
#
#	use '+' for enter
#
# See http://blog.opensecurityresearch.com/2012/10/hacking-usb-webkeys.html
# for more info
#
# brad.antoniewicz@foundstone.com
#

import binascii
import sys

if len(sys.argv) != 2:
 print sys.argv[0]," - Simple bus pirate i2c formatting tool"
 print "-------------------------------------------------"
 print "\t+\t-\tEnter"
 print "\t#\t-\tTime waster\n"
 print "usage:"
 print "\t",sys.argv[0]," \"notepad +?????? hello from brad\" \n" 
 sys.exit(1)

text=sys.argv[1]

header="[0xA0 0 0xD3 0xB9"
#trailer=['0xD3', '0xB9', '0xA8', '0x80', '0x80', '0x80', '0xFF', '0xFF']
trailer=['0x80', '0x80', '0x80', '0xFF', '0xFF']
#trailer=['0xFF', '0xFF', '0xFF', '0xFF', '0xFF', '0xFF', '0xFF', '0xFF'] #0xA9 = ESC 0xA7=0 0xA1 = 4 0xB0 = ] 0xB1 = \
count=2 # To make up for the header
print header,
for letter in text:
 count+=1
 if letter == '+': # for enter
  print "0xA8",
 elif letter == "#": # for pause
  print "0xFF",
 else:
  print "0x" + binascii.hexlify(letter),
 if count % 8 == 0 :
  print "][0xA0",count,

endofline=count%8

i=0
while i < len(trailer):
 if endofline == 8:
  print "][0xA0",
  if count % 8 == 0:
   print count+8,
  else:
   print count+8 - (count % 8),
  endofline = 0;
 print trailer[i],
 endofline+=1
 i+=1
 
print "][0xA0 0x00]"

