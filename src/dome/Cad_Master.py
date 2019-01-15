#!/usr/bin/env python

import RPi.GPIO as GPIO
import SimpleMFRC522
import MySQLdb
import time

import display as d

def cadastroMaster ():
        # Open database connection
        db = MySQLdb.connect("localhost","pi","","teste" )

        # prepare a cursor object using cursor() method
        cursor = db.cursor()

	reader = SimpleMFRC522.SimpleMFRC522()

	try:
		text = 'Master'
		print("Pase ahora tu tarjeta para configurala como Master")
		reader.write(text)

		id, text = reader.read()
                print("ID: " + str(id))
                print("Dato: " + text)
                sql = "INSERT INTO card(card_code, card_nome, card_data, card_master) VALUES ( %d, 'Master', '2099-01-01', 1 )" % (id)
                cursor.execute(sql)
                db.commit()
		print("Grabado con exito")
		d.printi("Grabado con","   Exito!")
		time.sleep(2)

	finally:
	        GPIO.cleanup()
