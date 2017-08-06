#!/usr/bin/python

# Date Created - 04/24/17

'''
    Author: Mipsel - Sprite
    Credits: Help from ~Entity~
```

# -*- encoding: utf-8 -*-

# imports
import os, sys, time
import dns.resolver
import requests
import socket
from urllib2 import urlopen, URLError, HTTPError

# colors
class color:
  class fg:   
    blue = '\033[94m'
    green = '\033[92m'
    yellow = '\033[93m'
    red = '\033[91m'
  class ex:
  	end = '\033[0m'

if os.name=='posix':
	cmd = 'clear'
else:
	cmd = 'cls'


if len(sys.argv)==1:
	sys.exit(color.fg.red +'ERROR : Retry using the correct usage.\r\nExample: python grep.py pastebin.com/raw/fD8yDmEf')

domain = sys.argv[1]

print(color.fg.red +" ")
os.system(cmd)

print ("Making sure Domain is online!")
socket.setdefaulttimeout( 10 )  # timeout in second
try :
    response = urlopen( domain )
except HTTPError, e:
    print 'The server couldn\'t fulfill the request. Reason:', str(e.code)
except URLError, e:
    print 'Failed to Connect Via Socket in 10 second Intervals. Reason:', str(e.reason)
else :
    html = response.read()
print (color.fg.green +'Got Response\r\nCode 200')
time.sleep(5)
os.system(cmd)
response = requests.get(domain)
print (color.ex.end + response.content)






