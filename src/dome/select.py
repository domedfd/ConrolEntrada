#!/usr/bin/python

import MySQLdb

# Open database connection
db = MySQLdb.connect("localhost","pi","","teste" )

# prepare a cursor object using cursor() method
cursor = db.cursor()

sql = "SELECT * FROM card \
       WHERE card_nome= '%s'" % ("domenico")
try:
   # Execute the SQL command
   cursor.execute(sql)
   # Fetch all the rows in a list of lists.
   results = cursor.fetchall()
   for row in results:
      id = row[0]
      nome = row[1]
      # Now print fetched result
      print "ID=%s,Nombre=%s" % \
             (id, nome )
except:
   print "Error: unable to fecth data"

# disconnect from server
db.close()
