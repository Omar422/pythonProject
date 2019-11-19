# 41. Classes And Objectss

"""
# Create Class using the keyword (class)
# Create object with assign it to the className(), cannot create object without class
# Note: The __init__() function is called automatically every time the class is being used to
create a new object.
"""

class Game:
    def __init__(self, name, r, c, id):
        self.name = ttk.Button(master, text=' ')
        self.name.grid(row=self.r,column=self.c, sticky='snew', ipadx=30, ipady=30)
        self.name.config(command = lambda : click(id))
