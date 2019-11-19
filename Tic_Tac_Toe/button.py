from tkinter import *
from tkinter import ttk

master=Tk()
master.title('Test')
# input field
val = ttk.Entry(master, width=40)
val.pack()

# function to print the input value
def bc():
    print(val.get())
    val.delete(0, END)

# button to click
btn1 = ttk.Button(master, text='get text', width=20)
btn1.pack()


# call the function after click the button
btn1.config(command=bc)


master.mainloop()
