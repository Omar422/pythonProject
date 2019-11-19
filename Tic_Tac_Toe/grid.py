from tkinter import *
from tkinter import ttk

m = Tk()

ttk.Label(m, background='grey', text='Grey').grid(row=0,column=0, sticky="snew")
ttk.Label(m, background='yellow', text='Black').grid(row=0,column=1, sticky="snew")
ttk.Label(m, background='blue', text='Blue').grid(row=1,column=0, columnspan=2, sticky="snew")
ttk.Label(m, background='orange', text='Orange').grid(row=0,column=2, rowspan=2, sticky="snew")

#ipadx && ipady == padding
#padx && pady == margin

m.rowconfigure(0,weight=1)
m.rowconfigure(1,weight=1)
m.columnconfigure(0,weight=1)
m.columnconfigure(1,weight=1)
m.columnconfigure(2,weight=1)

m.mainloop()
