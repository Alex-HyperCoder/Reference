import socket
import os
import time
import sys
from thread import *

'''

    Author: Mipsel / Sprite
    Date: 7/28/17 - July 28th, 2017.
    Fixed Indent Errors - August 14th, 2017
    

    NOTES:
    You will recieve the following Traceback Traces:

    Unhandled exception in thread started by <function clientthread at 0x7fa36457d050>
Traceback (most recent call last):
  File "server.py", line 56, in clientthread
    conn.sendall(reply)
  File "/usr/lib/python2.7/socket.py", line 228, in meth
    return getattr(self._sock,name)(*args)
socket.error: [Errno 32] Broken pipe

----------------------------------------------------

Unhandled exception in thread started by <function clientthread at 0x7f514a7cb050>
Traceback (most recent call last):
  File "server.py", line 71, in clientthread
    conn.sendall(reply)
  File "/usr/lib64/python2.7/socket.py", line 224, in meth
    return getattr(self._sock,name)(*args)
socket.error: [Errno 104] Connection reset by peer

    This is nothing major, But does indeed make it look like ass
    To screen in the background
    screen -dm bash -c 'python server.py SERVER_IP SERVER_PORT'

    BINDING TO SSH PORT:
    If you wish to bind this to the SSH Port,
    Follow as instructed!

    nano /etc/ssh/sshd_config
    Find Port 22
    Change to another port Such as Port 2222
    Then reboot

'''

HOST = sys.argv[1]
PORT = int(sys.argv[2])
 
W  = '\033[0m'  # white (normal)
R  = '\033[31m' # red
G  = '\033[32m' # green

if os.name == 'posix':
	cls = 'clear'
elif os.name == 'nt':
	sys.exit("This is meant for linux machines only!")

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
os.system(cls)
print R+'-'+G * 18
print R+'|'+G+' Socket Started '+R+'|'
print R+'-'+G * 18
time.sleep(1)


def get_banner():
    print R+"-" * 33
    print W+"| Mipsels Honeypot in Python2.7 "+R+"|"
    print R+"-" * 33

try:
    s.bind((HOST, PORT))
except socket.error as msg:
    print 'Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
    sys.exit()

os.system(cls)
get_banner()
print('\n')
print R+'-'+G * 24
print R+'|'+G+' Socket bind complete '+R+'|'
print R+'-'+G * 24
time.sleep(1)

os.system(cls)
s.listen(10)
get_banner()
print('\n')
print R+'-'+G * 24
print R+'|'+G+' Socket now listening '+R+'|'
print R+'-'+G * 24
print G+"Accepting Connections On Port: %d" % PORT
print W+"-" * 35
time.sleep(1)
 
def clientthread(conn):
    try:

        conn.send('Thanks for logging into my honeypot moron!\n')
        
         
        while True:
            
            data = conn.recv(512)
            reply = 'GET LOGGED RETARD \n' + data * 500
            if not data: 
                break
         
            conn.sendall(reply)
         
        conn.close()

    except socket.errno, ex:
        print(R+" ")

try:
    while 1:
        conn, addr = s.accept()
        print 'Host Logged |-| ' + addr[0] + ':' + str(addr[1])
        honeypot = open("honeypot.log","r")
        count = 0
        for line in honeypot:
            count+=1
        honeypot.close()
        honeypot = open("honeypot.log","a")
        honeypot.write("\r\nLogged: " + addr[0] + " Entry : #%d" % count - 1)
        honeypot.truncate()
        honeypot.close()

	    start_new_thread(clientthread ,(conn,))

except socket.errno, ex:
 	print(R+" ")

s.close()
