#!/usr/bin/python

#! Internal Imports !#
import os
import sys

'''

    Author: Mipsel / Sprite
    Date: 7/28/17 - July 28th, 2017.

'''

#! Color Codes !#
W  = '\033[0m'  # white (normal)
R  = '\033[31m' # red
G  = '\033[32m' # green
O  = '\033[33m' # orange
B  = '\033[34m' # blue
P  = '\033[35m' # purple
C  = '\033[1;36m' # cyan
GR = '\033[37m' # gray
T  = '\033[93m' # tan
Y = '\e[1;33m' # yellow

if os.name == 'posix':
	cs = 'clear'
else:
	cs = 'cls'

readFile = sys.argv[1]
writeFile = sys.argv[1]

def get_banner():
	os.system(cs)
	print(R+"-" * 41)
	print(R+"|"+C+"     ______ __                       	"+R+"|"+W)
	print(R+"|"+C+"    / ____// /____ _ ____ ___   ___  	"+R+"|"+W)
	print(R+"|"+C+"   / /_   / // __ `// __ `__ \ / _ \ 	"+R+"|"+W)
	print(R+"|"+C+"  / __/  / // /_/ // / / / / //  __/ 	"+R+"|"+W)
	print(R+"|"+C+" /_/    /_/ \__,_//_/ /_/ /_/ \___/  	"+R+"|"+W)
	print(R+"-" * 41)


def read_file():
	get_banner()
	fileName = raw_input("File: ")
	file = open(fileName, "r")
	for line in file:
		print (line)


def write_file():
	get_banner()
	fileName = raw_input("File: ")
	while True:
		file = open(fileName, "a")
		fileWrite = raw_input(": ")
		file.write(fileWrite+"\r\n")
		file.close()


if sys.argv[1] == 'read':
	read_file()

if sys.argv[1] == 'write':
	write_file()
