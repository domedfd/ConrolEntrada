#!/usr/bin/python

import MySQLdb

def veriMaster (num):
	# Open database connection
	db = MySQLdb.connect("localhost","pi","","teste" )

	# prepare a cursor object using cursor() method
	cursor = db.cursor()

	sql = """select card_code, card_nome from card """
	sqli =" update card set card_entradas = card_entradas + 0.25 where card_code = %d" % (int(num))

	# TESTE #
#	print("Ver que numero esta pegando: " + num)

	try:
		# Execute the SQL command
		cursor.execute(sql)
		# Fetch all the rows in a list of lists.
		results = cursor.fetchall()
		encontrado = ""
		for row in results:
			card_code   = row[0]
			card_nome   = row[1]
			if str(num) == str(card_code):
				encontrado = "Tarjeta Cadastrada, porfavor pase!"
				cursor.execute(sqli)
				db.commit()
#				porta.abrir()
	except:
		return "Error: unable to fecth data"

	# disconnect from server
	db.close()
	return encontrado
