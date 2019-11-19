#Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 19:29:22) [MSC v.1916 32 bit (Intel)] on win32
#Type "help", "copyright", "credits" or "license()" for more information.
from tkinter import *
from tkinter import ttk
master=Tk()
btn=ttk.Button(master, text='btn1')
btn.pack()
btn2=ttk.Button(master, text='btn2')
btn2.pack()
btn3=ttk.Button(master, text='btn3')
btn3.pack()
style=ttk.Style()
style.theme_use()
'vista'
style.theme_names()
('winnative', 'clam', 'alt', 'default', 'classic', 'vista', 'xpnative')
style.theme_use('alt')
style.configure('TButton', foreground='blue')
style.theme_use('classic')
style.configure('TButton', foreground='white', background='blue')
style.configure('TButton', foreground='grey')
style.configure('a.TButton', background='green')
b3.style('a.TButton
b3.style('a.TButton')
b3.configure('a.TButton
b3.configure('a.TButton')
btn3.configure('a.TButton
btn3.configure('a.TButton')
btn3.configure(style='a.TButton')
