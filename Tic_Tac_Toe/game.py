from tkinter import *
from tkinter import ttk
from tkinter import messagebox

# defined here to be global
Active = 1
player1 = []
player2 = []

def game():

    master = Tk()

    master.title("Tic Tac Toe : Player 1")

    # when choose to restart the game , empty the lists to start again
    player1.clear()
    player2.clear()

# create the nine buttons
    btn1 = ttk.Button(master, text=' ')
    btn1.grid(row=0,column=0, sticky='snew', ipadx=30, ipady=30)
    btn1.config(command = lambda : click(1) )

    btn2 = ttk.Button(master, text=' ')
    btn2.grid(row=0,column=1, sticky='snew', ipadx=30, ipady=30)
    btn2.config(command = lambda : click(2) )

    btn3 = ttk.Button(master, text=' ')
    btn3.grid(row=0,column=2, sticky='snew', ipadx=30, ipady=30)
    btn3.config(command = lambda : click(3) )

    btn4 = ttk.Button(master, text=' ')
    btn4.grid(row=1,column=0, sticky='snew', ipadx=30, ipady=30)
    btn4.config(command = lambda : click(4) )

    btn5 = ttk.Button(master, text=' ')
    btn5.grid(row=1,column=1, sticky='snew', ipadx=30, ipady=30)
    btn5.config(command = lambda : click(5) )

    btn6 = ttk.Button(master, text=' ')
    btn6.grid(row=1,column=2, sticky='snew', ipadx=30, ipady=30)
    btn6.config(command = lambda : click(6) )

    btn7 = ttk.Button(master, text=' ')
    btn7.grid(row=2,column=0, sticky='snew', ipadx=30, ipady=30)
    btn7.config(command = lambda : click(7) )

    btn8 = ttk.Button(master, text=' ')
    btn8.grid(row=2,column=1, sticky='snew', ipadx=30, ipady=30)
    btn8.config(command = lambda : click(8) )

    btn9 = ttk.Button(master, text=' ')
    btn9.grid(row=2,column=2, sticky='snew', ipadx=30, ipady=30)
    btn9.config(command = lambda : click(9) )

# flexable buttons ...
    master.rowconfigure(0,weight=1)
    master.rowconfigure(1,weight=1)
    master.rowconfigure(2,weight=1)
    master.columnconfigure(0,weight=1)
    master.columnconfigure(1,weight=1)
    master.columnconfigure(2,weight=1)

    # when user click the button
    def click(id):
        global Active
        global player1
        global player2

        # to play first even if player1 won the last game
        if len(player1)==0:
            Active=1
        # if a player clicked the button change it text 'call play()', state & Active value, also add the position of it in the players array
        if (Active==1):
            play(id, 'X')
            player1.append(id)
            master.title("Tic Tac Toe : Player 2")
            Active = 2
            #print('player1: {}'.format(player1))
        elif(Active==2):
            play(id, 'O')
            player2.append(id)
            master.title("Tic Tac Toe : Player 1")
            Active = 1
            #print('player2: {}'.format(player2))

        # call the winner function after every move in the game
        winner()

# function to change the button content to (x||O) and disable it.
    def play(id, text):
        if(id==1):
            btn1.config(text=text)
            btn1.state(['disabled'])
        elif(id==2):
            btn2.config(text=text)
            btn2.state(['disabled'])
        elif(id==3):
            btn3.config(text=text)
            btn3.state(['disabled'])
        elif(id==4):
            btn4.config(text=text)
            btn4.state(['disabled'])
        elif(id==5):
            btn5.config(text=text)
            btn5.state(['disabled'])
        elif(id==6):
            btn6.config(text=text)
            btn6.state(['disabled'])
        elif(id==7):
            btn7.config(text=text)
            btn7.state(['disabled'])
        elif(id==8):
            btn8.config(text=text)
            btn8.state(['disabled'])
        elif(id==9):
            btn9.config(text=text)
            btn9.state(['disabled'])

# to win the game there're eight conditions to that
    def winner():
        winner = -1
        if( ( (1 in player1) and (2 in player1) and (3 in player1) ) or
            ( (4 in player1) and (5 in player1) and (6 in player1) ) or
            ( (7 in player1) and (8 in player1) and (9 in player1) ) or
            ( (1 in player1) and (4 in player1) and (7 in player1) ) or
            ( (2 in player1) and (5 in player1) and (8 in player1) ) or
            ( (3 in player1) and (6 in player1) and (9 in player1) ) or
            ( (1 in player1) and (5 in player1) and (9 in player1) ) or
            ( (3 in player1) and (5 in player1) and (7 in player1) )
        ):
            winner = 1

        if( ( (1 in player2) and (2 in player2) and (3 in player2) ) or
            ( (4 in player2) and (5 in player2) and (6 in player2) ) or
            ( (7 in player2) and (8 in player2) and (9 in player2) ) or
            ( (1 in player2) and (4 in player2) and (7 in player2) ) or
            ( (2 in player2) and (5 in player2) and (8 in player2) ) or
            ( (3 in player2) and (6 in player2) and (9 in player2) ) or
            ( (1 in player2) and (5 in player2) and (9 in player2) ) or
            ( (3 in player2) and (5 in player2) and (7 in player2) )
        ):
            winner = 2


# show a message after end the game
        if winner==1 :
            messagebox.showinfo(title='Congratulations', message='Player 1 is winner')
            d() # call it to destroy this game.
        elif winner==2:
            messagebox.showinfo(title='Congratulations', message='Player 2 is winner')
            d() # call it to destroy this game.
        else:
            # this condition to make sure that all button have been clicked and winner still == -1 which means no winner
            if len(player1)==5 and len(player2)==4:
                messagebox.showinfo(title='No Winner', message='Players are tied')
                d() # call it to destroy this game.

    def d():
        master.destroy()
        restart() # call it to choose (Play Again || Exit)


    master.mainloop()

#call after finish a game, start another match or exit
def restart():
    root=Tk()
    root.title('Choose to play again or exit:')

    again = ttk.Button(root, text='Play Again')
    again.grid(row=0,column=0, sticky='snew', ipadx=50, ipady=15)

    close = ttk.Button(root, text='Exit')
    close.grid(row=0,column=1, sticky='snew', ipadx=50, ipady=15)

# flexable buttons ...
    root.rowconfigure(0,weight=1)
    root.columnconfigure(0,weight=1)
    root.columnconfigure(1,weight=1)

# Play Again || Exit
    def setting(id):
        if (id==1):
            root.destroy()
            game()
        else:
            root.destroy()

    again.config(command = lambda : setting(1) )
    close.config(command = lambda : setting(2) )

    root.mainloop()

game()
