import os
import sys
import time

number = 0

W  = '\033[0m'  # white (normal)
R  = '\033[31m' # red
C  = '\033[1;36m' # cyan

if os.name == 'posix':
    cs = 'clear'
elif os.name == 'nt':
    cs = 'cls'

def get_banner():
	os.system(cs)
	print(R+"-" * 41)
	print(R+"|"+C+"     ______ __                       	"+R+"|"+W)
	print(R+"|"+C+"    / ____// /____ _ ____ ___   ___  	"+R+"|"+W)
	print(R+"|"+C+"   / /_   / // __ `// __ `__ \ / _ \ 	"+R+"|"+W)
	print(R+"|"+C+"  / __/  / // /_/ // / / / / //  __/ 	"+R+"|"+W)
	print(R+"|"+C+" /_/    /_/ \__,_//_/ /_/ /_/ \___/  	"+R+"|"+W)
	print(R+"-" * 41 +W)

get_banner()

while True:
    time.sleep(1)
    number+=1
    print number


