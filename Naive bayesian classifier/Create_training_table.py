import sqlite3
import os
#os.remove("Training_data.db")
conn=sqlite3.connect("Training_data.db")
conn.execute("create table Data(outlook varchar(50), temperature varchar(50), humidity varchar(50), wind varchar(50), result varchar(20))")
conn.execute("create table prob(attribute varchar(50), p_yes float(10,3), p_no float(10,3));")
conn.commit()
conn.close()
print("Table created")
