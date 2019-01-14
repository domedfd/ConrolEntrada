#!/usr/bin/python

import MySQLdb
def veriMaster ():
	# Open database connection
	db = MySQLdb.connect("localhost","pi","","teste" )

	# prepare a cursor object using cursor() method
	cursor = db.cursor()

	sql = """select card_code, card_nome from card where card_nome='master' limit 1"""

	sqld = """delete from card where card_data<current_date()-INTERVAL 30 day"""

	try:
		# Execute the SQL command
		cursor.execute(sql)
		# Fetch all the rows in a list of lists.
		results = cursor.fetchall()
		if results:
			for row in results:
				card_code   = row[0]
				card_nome   = row[1]
				# Now print fetched result
				cursor.execute(sqld)
				db.commit()
				return "%s" % \
					( card_code), \
					"%s" % (card_nome)
		else:
			return "nada","nada"
	except:
		return "Error: unable to fecth data"

	# disconnect from server
	db.close()
