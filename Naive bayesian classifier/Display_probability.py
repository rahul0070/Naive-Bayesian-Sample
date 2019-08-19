import sqlite3
conn=sqlite3.connect("Training_data.db")
cur=conn.execute("select * from prob")
for row in cur:
	print(row[0]+" "+str(row[1])+" "+str(row[2]))

x=input("Done")


