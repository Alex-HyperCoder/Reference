#!/usr/bin/python

#! Imports !#
import MySQLdb
import os
import sys
import datetime
from datetime import datetime

cmd = 'clear'


db = MySQLdb.connect(host="localhost",
					 user="root",
					 passwd="#mysqlpasswd",
					 db="databasename")


def SearchUsername():
	os.system(cmd)
	if sys.argv[1] == 'ID':
		cur = db.cursor()
		cur.execute("SELECT * FROM membersregistered WHERE memberID = '"+sys.argv[2]+"';")

		t1 = datetime.now()

		for row in cur.fetchall():
			print "-" * 60
			print "ID: %d " % (row[0])
			print "Username: %s " % (row[1])
			print "Password: %s " % (row[2])
			print "Email: %s " % (row[3])
			print "Position: %s " % (row[4])
			print "Division: %s " % (row[5])
			print "Date: %s " % (row[6])
			print "-" * 60

			t2 = datetime.now()
			t3 = t2 - t1
			print "Query Search Took: %s Seconds" % (str(t3))


	elif sys.argv[1] == 'Email':
		cur = db.cursor()
		cur.execute("SELECT * FROM membersregistered WHERE email = '"+sys.argv[2]+"';")

		t1 = datetime.now()

		for row in cur.fetchall():
			print "-" * 60
			print "ID: %d " % (row[0])
			print "Username: %s " % (row[1])
			print "Password: %s " % (row[2])
			print "Email: %s " % (row[3])
			print "Position: %s " % (row[4])
			print "Division: %s " % (row[5])
			print "Date: %s " % (row[6])
			print "-" * 60

			t2 = datetime.now()
			t3 = t2 - t1
			print "Query Search Took: %s Seconds" % (str(t3))


	elif sys.argv[1] == 'Username':
		cur = db.cursor()
		cur.execute("SELECT * FROM membersregistered WHERE username = '"+sys.argv[2]+"';")

		t1 = datetime.now()

		for row in cur.fetchall():
			print "-" * 60
			print "ID: %d " % (row[0])
			print "Username: %s " % (row[1])
			print "Password: %s " % (row[2])
			print "Email: %s " % (row[3])
			print "Position: %s " % (row[4])
			print "Division: %s " % (row[5])
			print "Date: %s " % (row[6])
			print "-" * 60

			t2 = datetime.now()
			t3 = t2 - t1
			print "Query Search Took: %s Seconds" % (str(t3))

	elif sys.argv[1] == 'IP':
		cur = db.cursor()
		cur.execute("SELECT * FROM membersregistered WHERE ip = '"+sys.argv[2]+"';")

		t1 = datetime.now()

		for row in cur.fetchall():
			print "-" * 60
			print "ID: %d " % (row[0])
			print "Username: %s " % (row[1])
			print "Password: %s " % (row[2])
			print "Email: %s " % (row[3])
			print "Position: %s " % (row[4])
			print "Division: %s " % (row[5])
			print "Date: %s " % (row[6])
			print "-" * 60

			t2 = datetime.now()
			t3 = t2 - t1
			print "Query Search Took: %s Seconds" % (str(t3))


	db.close()

SearchUsername()
