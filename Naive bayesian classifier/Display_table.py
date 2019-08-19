import sqlite3
conn=sqlite3.connect("Training_data.db")
cur=conn.execute("select * from Data")
i=0
for row in cur:
	print(str(i+1)+" "+str(row[0])+" "+str(row[1])+" "+str(row[2])+" "+str(row[3])+"---"+str(row[4]))
	i=i+1
    
x=input("Table displayed.")	