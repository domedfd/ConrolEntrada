#!/usr/bin/env python

import RPi.GPIO as GPIO
import SimpleMFRC522
import MySQLdb
import time

import verificar as veri
import verificar_master as verMaster

def cadastrar ():
        # Open database connection
        db = MySQLdb.connect("localhost","pi","","teste" )

        # prepare a cursor object using cursor() method
        cursor = db.cursor()

	reader = SimpleMFRC522.SimpleMFRC522()

	try:
		while True:
			print("- Pase la nueva tarjeta para cadastrar.\n- Pase la tarjeta Master para salir del modo configuracion.\n")
			id, text = reader.read()
        	        print("ID:" + str(id))
        	        print("Texto:" + text)
			idm, master = verMaster.veriMaster()
			if str(id) == idm:
				print("Tarjeta Master detectada, saliendo de modo configuracion...\n\n")
				return
			elif veri.veriMaster(id):
				print("Tarjeta ya cadastrada\nsera eliminada")
				sqld = "DELETE FROM card WHERE card_code = '%d'" % (id)
				cursor.execute(sqld)
				db.commit()
                        	print("Tarjeta eliminada com exito\n\n")
				time.sleep(2)
			else:
	                	sqla = "INSERT INTO card(card_code, card_nome, card_data, card_master, card_entradas) VALUES ( '%s', ' Nueva Tarjeta', current_date(), 0, 0 )" % (str(id))
	                	cursor.execute(sqla)
	                	db.commit()
				reader.write("Nueva")
				print("Tarjeta nueva\nsera agregada")
				print("Grabado con exito\n\n")
				time.sleep(2)

	finally:
	        GPIO.cleanup()
