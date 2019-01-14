#!/usr/bin/env python

import RPi.GPIO as GPIO
import SimpleMFRC522
import MySQLdb
def lectura ():
        # Open database connection
        db = MySQLdb.connect("localhost","pi","","teste" )

        # prepare a cursor object using cursor() method
        cursor = db.cursor()


        reader = SimpleMFRC522.SimpleMFRC522()

        try:
                id, text = reader.read()
                print(id)
                print(text)
                sql = "INSERT INTO card(id, nome) VALUES ( '%s', '%s' )" % (id, text)
                cursor.execute(sql)
                db.commit()
        except:
                db.rollback()
        finally:
                GPIO.cleanup()
                db.close()
lectura()
