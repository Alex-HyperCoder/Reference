#! Internal Imports !#
import os
import sys

#! External Imports !#
import subprocess

#! Color Codes !#
W  = '\033[0m'  # white (normal)
R  = '\033[31m' # red
C  = '\033[1;36m' # cyan


if os.name == 'posix':
	cs = 'clear'
else:
	cs = 'cls'

def get_banner():
	os.system(cs)
	print(R+"-" * 41)
	print(R+"|"+C+"     ______ __                       	"+R+"|"+W)
	print(R+"|"+C+"    / ____// /____ _ ____ ___   ___  	"+R+"|"+W)
	print(R+"|"+C+"   / /_   / // __ `// __ `__ \ / _ \ 	"+R+"|"+W)
	print(R+"|"+C+"  / __/  / // /_/ // / / / / //  __/ 	"+R+"|"+W)
	print(R+"|"+C+" /_/    /_/ \__,_//_/ /_/ /_/ \___/  	"+R+"|"+W)
	print(R+"-" * 41)


def get_cpu_kernal():
	get_banner()

	def run(cmd):
		subprocess.call(cmd, shell=True)

	print(R+"Detecting Processing Emulator"+W)
	run('lscpu | grep "Architecture:"'+R)

get_cpu_kernal()
