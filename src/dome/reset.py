#!/usr/bin/python

import MySQLdb

# Open database connection
db = MySQLdb.connect("localhost","pi","","teste" )

# prepare a cursor object using cursor() method
cursor = db.cursor()

# Drop table if it already exist using execute() method.
cursor.execute("DROP TABLE IF EXISTS card")

# Create table as per requirement
sql = """CREATE TABLE `card` (
  `id` int NOT NULL AUTO_INCREMENT,
  `card_code` char(20) NOT NULL,
  `card_nome` char(20),
  `card_data` date,
  `card_master` int(20),
  `card_entradas` decimal(12,2),
  PRIMARY KEY (id)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;"""

cursor.execute(sql)

# disconnect from server
db.close()
