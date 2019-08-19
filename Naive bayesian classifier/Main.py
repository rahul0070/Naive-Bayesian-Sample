from tkinter import *
from tkinter.ttk import *
import os
import sys
import time

def main_app():
    print('Creating database...')
    import Create_training_table
    print('inserting sample data...')
    import Insert_data


def rn():
    import Naive_Bayesian

def tx():
    import Display_table

def ex():
    sys.exit()	

fr = Frame(width=500, height=200)
try:
	main_app()
except:
    print('Database exists')

l1 = Label(fr, text = 'WELCOME')
l2 = Label(fr, text = 'NAIVE BAYES CLASSIFIER')
b1 = Button(fr, text = 'Run', command = rn, width=20)
b2 = Button(fr, text = 'View sample data', command = tx, width=20)
b3 = Button(fr, text = 'Exit', command = ex, width=20)

l1.pack()
l2.pack()
b1.pack()
b2.pack()
b3.pack()
fr.pack()

fr.mainloop()
