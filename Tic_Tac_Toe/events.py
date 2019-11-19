from tkinter import *
from tkinter import ttk

master=Tk()

def key_press(event):
    print("type:{}".format(event.type))
    print('Ctrl+C')

#root.bind(event,function)
master.bind('<Control-c>', key_press)

def button_press(event):
    print('Pressed')

btn = ttk.Button(master, text = 'click')
btn.pack()
btn.bind('<ButtonPress>', button_press)

master.mainloop()
