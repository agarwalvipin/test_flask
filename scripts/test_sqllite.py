#!/usr/bin/python

import sqlite3

conn = sqlite3.connect('tbl_entry')

print "Opened database successfully";

#conn.execute('''CREATE TABLE tbl_entry ( id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY, 
 #               amt FLOAT NOT NULL, 
 #               date DATE NOT NULL, 
  #              description VARCHAR(64), 
   #             category VARCHAR(64) NOT NULL,
    #            timestamp DateTime);''')

#print "Table created successfully";

conn.execute('''INSERT INTO tbl_entry (amt, date, description, category, timestamp) 
                VALUES (43.0, '2015-12-04', 'fasdf', 'HOH', '2015-12-05 00:44:38.322000')''')

cur = conn.execute('''select * from tbl_entry''')

for row in cur:
    print row

print "insertion complete!!"
#conn.close()