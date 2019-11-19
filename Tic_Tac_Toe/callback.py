from tkinter import *
from tkinter import ttk

master=Tk()

#create button
btn = ttk.Button(master, text='click')
btn.pack()

btn2 = ttk.Button(master, text='click2')
btn2.pack()

def click(n):
    print('clicked: {}'.format(n))

btn.config(command= lambda : click(1))
btn2.config(command= lambda : click(2))

master.mainloop()
