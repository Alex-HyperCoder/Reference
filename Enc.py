#!/usr/bin/python

#! Imports !#
import os
import sys
import time
try:
    from Crypto.Cipher import AES
except ImportError:
    if os.name == 'nt':
        os.system(cmd)
        print(R+"You do not have pycrypto Installed")
        print(R+"Try installing it by installing this, http://aka.ms/vcpython27")
        print(R+"Then Change your command prompts Directory to C:\Python27\Scripts\ , Then run easy_install pycrypto")

    if os.name == 'posix':
        os.system(cmd)
        print(R+"You do not have pycrypto Installed")
        print(R+"Download pycrypto from https://pypi.python.org/pypi/pycrypto")
        print(R+"Change the your current path to /pycrypto-2.6.1")
        print(R+"Then execute 'python setup.py install'")

import base64

#! Defining Color Codes !#
W  = '\033[0m'  # white (normal)
R  = '\033[31m' # red
C  = '\033[1;36m' # cyan

#! Creating Multi-OS Clear Screen !#
if os.name == 'posix':
    cmd = 'clear'
elif os.name == 'nt':
    cmd = 'cls'

os.system(cmd)


def encode_Message():
    try:

        #! Setting Secret Key !#
        msg = raw_input(C+"Message:"+W).rjust(32)

        print(W+"KEYS MUST BE 16, 24, OR, 32 BYTES LONG")
        secret_key = raw_input(C+"Key: "+W)

        cipher = AES.new(secret_key,AES.MODE_ECB)
        encoded = base64.b64encode(cipher.encrypt(msg))

        file = open("enc.log", "a")
        file.write("""
| CREATED KEY |
Key: """ +secret_key+ """
| Messaged Encoded |
Message: """ +encoded+ """
    """)

    except ValueError:
        os.system(cmd)
        print R+"Key Length: %d " % len(secret_key)
        print(R+"Key: " +secret_key)
        print(R+"Key Must Be 16, 24, or, 32 Characters Long.")

def decode_Message():
    try:
        msg = raw_input(C+"Message:"+W).rjust(32)

        print(W+"KEYS MUST BE 16, 24, OR, 32 BYTES LONG")
        secret_key = raw_input(C+"Key: "+W)

        cipher = AES.new(secret_key,AES.MODE_ECB)
        decoded = cipher.decrypt(base64.b64decode(msg))
        
        file = open("enc.log", "a")
        file.write("""
| KEY USED |
Key: """ +secret_key+ """
| Message Decoded |
Message: """ +decoded+ """     
    """)

    except ValueError:
        os.system(cmd)
        print R+"Key Length: %d " % len(secret_key)
        print(R+"Key: " +secret_key)
        print(R+"Key Must Be 16, 24, or, 32 Characters Long.")

def get_banner():
	print(R+"-" * 41)
	print(R+"|"+C+"     ______ __                       	"+R+"|"+W)
	print(R+"|"+C+"    / ____// /____ _ ____ ___   ___  	"+R+"|"+W)
	print(R+"|"+C+"   / /_   / // __ `// __ `__ \ / _ \ 	"+R+"|"+W)
	print(R+"|"+C+"  / __/  / // /_/ // / / / / //  __/ 	"+R+"|"+W)
	print(R+"|"+C+" /_/    /_/ \__,_//_/ /_/ /_/ \___/  	"+R+"|"+W)
	print(R+"-" * 41)

get_banner()


def get_menu():
    print(C+"[1] Encode Message")
    print(C+"[2] Decode Message")
    enc_Choice = raw_input(C+"1-2: ")

    if enc_Choice == '1':
        encode_Message()

    elif enc_Choice == '2':
        decode_Message()

get_menu()
