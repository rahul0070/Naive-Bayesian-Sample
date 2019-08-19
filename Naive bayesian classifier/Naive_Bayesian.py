import sqlite3
from tkinter import *


# from tkinter.ttk import *
px=0
py=0

def naive(a, b, c, d):
    conn = sqlite3.connect("Training_data.db")
    print("Calculating Probability...")
    pr_yes = 1
    pr_no = 1
    li=[a, b, c, d]
    for i in li:
        cur = conn.execute("select p_yes, p_no from prob where attribute=?", (i,))
        tu = cur.fetchone()
        print("Probability of "+i+" --> YES: "+str(tu[0])+",  NO: "+str(tu[1]))
        pr_yes = pr_yes * tu[0]
        pr_no = pr_no * tu[1]
    cur.close()
    #print(pr_yes)
    #print(pr_no)
    if(pr_yes>pr_no):
    	print("Result of ");print(li);print("is YES")
    elif(pr_no>pr_yes):
    	print("Result of ");print(li);print("is NO")
         	

def nb_main(a, b, c, d):
    list1 = []
    list2 = []
    list3 = []
    list4 = []
    print("Calculating Outcome...")
    conn = sqlite3.connect("Training_data.db")
    cur = conn.execute("select distinct outlook from Data;")
    for row in cur:
        list1.append(row[0])
    cur.close()
    cur = conn.execute("select distinct temperature from Data;")
    for row in cur:
        list2.append(row[0])
    cur.close()
    cur = conn.execute("select distinct humidity from Data;")
    for row in cur:
        list3.append(row[0])
    cur.close()
    cur = conn.execute("select distinct wind from Data;")
    for row in cur:
        list4.append(row[0])
    cur.close()
    list5=['Yes','No']

    conn.execute("delete from prob")
    curx = conn.execute("select count(*) from Data where result='Yes';")
    cury = conn.execute("select count(*) from Data;")
    px1 = curx.fetchone()
    pt1 = cury.fetchone()
    py = pt1[0] - px1[0]
    px = px1[0]
    pt = pt1[0]


    for x in list1:
        cur1 = conn.execute("select count(*) from Data where outlook=? and result=?;", (x, "Yes"))
        cur2 = conn.execute("select count(*) from Data where outlook=? and result=?;", (x, "No"))
        q1 = cur1.fetchone()
        w1 = cur2.fetchone()
        q = q1[0]
        w = w1[0]
        p_x = q / px
        p_y = w / py
        conn.execute("insert into prob(attribute, p_yes, p_no) values(?,?,?);", (x, p_x, p_y))
        conn.commit()
    for x in list2:
        cur1 = conn.execute("select count(*) from Data where temperature=? and result=?;", (x, "Yes"))
        cur2 = conn.execute("select count(*) from Data where temperature=? and result=?;", (x, "No"))
        q1 = cur1.fetchone()
        w1 = cur2.fetchone()
        q = q1[0]
        w = w1[0]
        p_x = q / px
        p_y = w / py
        conn.execute("insert into prob(attribute, p_yes, p_no) values(?,?,?);", (x, p_x, p_y))
        conn.commit()

    for x in list3:
        cur1 = conn.execute("select count(*) from Data where humidity=? and result=?;", (x, "Yes"))
        cur2 = conn.execute("select count(*) from Data where humidity=? and result=?;", (x, "No"))
        q1 = cur1.fetchone()
        w1 = cur2.fetchone()
        q = q1[0]
        w = w1[0]
        p_x = q / px
        p_y = w / py
        conn.execute("insert into prob(attribute, p_yes, p_no) values(?,?,?);", (x, p_x, p_y))
        conn.commit()
    for x in list4:
        cur1 = conn.execute("select count(*) from Data where wind=? and result=?;", (x, "Yes"))
        cur2 = conn.execute("select count(*) from Data where wind=? and result=?;", (x, "No"))
        q1 = cur1.fetchone()
        w1 = cur2.fetchone()
        q = q1[0]
        w = w1[0]
        p_x = q / px
        p_y = w / py
        conn.execute("insert into prob(attribute, p_yes, p_no) values(?,?,?);", (x, p_x, p_y))
        conn.commit()

    px=px/pt
    py=py/pt
    conn.execute("insert into prob(attribute, p_yes, p_no) values(?,?,?);", ("Total", px, py))
    conn.commit()
    naive(a, b, c, d)


def run_nb():
    a = var1.get()
    b = var2.get()
    c = var3.get()
    d = var4.get()
    nb_main(a, b, c, d)


# main
o1 = ['Sunny', 'Rainy', 'Overcast']
o2 = ['Hot', 'Mild', 'Cool']
o3 = ['High', 'Normal']
o4 = ['Weak', 'Strong']

fr = Frame(width="100")
fr.pack()

var1 = StringVar(fr)
var1.set(o1[0])
var2 = StringVar(fr)
var2.set(o2[0])
var3 = StringVar(fr)
var3.set(o3[0])
var4 = StringVar(fr)
var4.set(o4[0])

l1 = Label(fr, text="SELECT THE ATTRIBUTE VALUES:")
l1.pack()
l2=Label(fr, text="Outlook")
l2.pack()
op1 = OptionMenu(fr, var1, *o1)
op1.pack()
l3=Label(fr, text="Temperature")
l3.pack()
op2 = OptionMenu(fr, var2, *o2)
op2.pack()
l4=Label(fr, text="humidity")
l4.pack()
op3 = OptionMenu(fr, var3, *o3)
op3.pack()
l5=Label(fr, text="Wind")
l5.pack()
op4 = OptionMenu(fr, var4, *o4)
op4.pack()
l6=Label(fr, text="    ")
l6.pack()
b1 = Button(text="SUBMIT", command=run_nb)
b1.pack()
fr.mainloop()
