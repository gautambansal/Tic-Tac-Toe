import tkinter.messagebox
from tkinter import*


root = Tk()
root.geometry("1350x750")
root.title("Tic Tac Toe")
root.configure(background ='cadet blue')

Tops = Frame(root, bg = 'cadet blue', pady =2, width =1350, height =100,relief = RIDGE)
Tops.grid(row =0,column=0)

lblTitle =Label(Tops, font=('arial',50,'bold'), text='Tic Tac Toe Game',bd =21,bg='cadet blue',fg ='cornsilk',justify = CENTER)
lblTitle.grid(row = 0, column =0)

# FRAMES

MainFrame = Frame(root, bg = 'powder blue', pady =2, width =1350, height =600,relief = RIDGE)
MainFrame.grid(row =1,column=0)

LeftFrame = Frame(MainFrame,bg ='cadet blue', bd = 10 , padx=10 ,pady =2, width =750, height =500,relief = RIDGE)
LeftFrame.pack(side=LEFT)

RightFrame = Frame(MainFrame,bg ='cadet blue', bd = 10 , padx=10 ,pady =2, width =560, height =500,relief = RIDGE)
RightFrame.pack(side=RIGHT)

RightFrame1 = Frame(RightFrame,bg ='cadet blue', bd = 10 , padx=10 ,pady =2, width =560, height =200,relief = RIDGE)
RightFrame1.grid(row=0 , column=0)

RightFrame2 = Frame(RightFrame,bg ='cadet blue', bd = 10 , padx=10 ,pady =2, width =560, height =200,relief = RIDGE)
RightFrame2.grid(row=1 , column=0)

# VARS

PlayerX = IntVar()
PlayerO = IntVar()

TurnX = StringVar()
TurnO = StringVar()

PlayerX.set(0)
PlayerO.set(0)

buttons = StringVar()
click = True

flag = 0

TurnX.set('Your Turn')
TurnO.set('Wait.....')

    #GAME BUTTON FEATURE 

def checker(buttons):
    global click
    global flag
    if buttons["text"] == " " and click == True:
        buttons["text"] = "X"
        click = False
        flag += 1
        scorekeeper()
    elif buttons["text"] == " " and click == False:
        buttons["text"] = "O"
        click = True
        flag += 1
        scorekeeper()

    if click == True:
        TurnX.set('Your Turn')
        TurnO.set('Wait.....')
    else:
        TurnX.set('Wait.....')
        TurnO.set('Your Turn')
    # CHECK FOR VICTORY
def scorekeeper():
    global flag
    for i in range(3):
        if btn[i][0]['text']==btn[i][1]['text']==btn[i][2]['text']!=" ":
            if btn[i][0]['text']=="X":
                n = float(PlayerX.get())
                score = (n+1)
                PlayerX.set(score)
                tkinter.messagebox.showinfo("X wins","Congrats X!!")
                reset()      
            elif btn[i][0]['text']=="O":
                n = float(PlayerO.get())
                score = (n+1)
                PlayerO.set(score)
                tkinter.messagebox.showinfo("O wins","Congrats O!!")
                reset()
            break
        if btn[0][i]['text']==btn[1][i]['text']==btn[2][i]['text']!=" ":
            if btn[0][i]['text']=="X":
                n = float(PlayerX.get())
                score = (n+1)
                PlayerX.set(score)
                tkinter.messagebox.showinfo("X wins","Congrats X!!")
                reset()
                      
            elif btn[0][i]['text']=="O":
                n = float(PlayerO.get())
                score = (n+1)
                PlayerO.set(score)
                tkinter.messagebox.showinfo("O wins","Congrats O!!")
                reset()
            break
        if btn[0][0]['text']==btn[1][1]['text']==btn[2][2]['text']!=" ":
            if btn[0][0]['text']=="X":
                n = float(PlayerX.get())
                score = (n+1)
                PlayerX.set(score)
                tkinter.messagebox.showinfo("X wins","Congrats X!!")
                reset()
                break      
            elif btn[0][0]['text']=="O":
                n = float(PlayerO.get())
                score = (n+1)
                PlayerO.set(score)
                tkinter.messagebox.showinfo("O wins","Congrats O!!")
                reset()
                break
        if btn[0][2]['text']==btn[1][1]['text']==btn[2][0]['text']!=" ":
            if btn[0][2]['text']=="X":
                n = float(PlayerX.get())
                score = (n+1)
                PlayerX.set(score)
                tkinter.messagebox.showinfo("X wins","Congrats X!!")
                reset()
                break      
            elif btn[0][2]['text']=="O":
                n = float(PlayerO.get())
                score = (n+1)
                PlayerO.set(score)
                tkinter.messagebox.showinfo("O wins","Congrats O!!")
                reset()
                break
    if flag == 9:
        tkinter.messagebox.showinfo("Tie","It's a tie!!")
        reset()
        return

     
    # RESET & NEW GAME BUTTON FEATURE

def reset():
    global flag
    flag = 0
    for i in range(3):
        for j in range(3):
            btn[i][j]['text']=" "
            btn[i][j].configure(background = 'gainsboro')

def NewGame():
    global flag
    flag = 0
    reset()
    PlayerX.set(0)
    PlayerO.set(0)

    # SOME LABELS

lblPlayerX =Label(RightFrame1, font=('arial',40,'bold'), text='Player X:',padx=2,pady=2,bg='cadet blue')
lblPlayerX.grid(row = 0, column =0 ,sticky = W)

txtPlayerX =Entry(RightFrame1, font=('arial',40,'bold'),bd = 2,fg='black',textvariable =PlayerX,width =4,justify=LEFT).grid(row=0,column=1)
Entry(RightFrame1, font=('arial',40,'bold'),bd = 2,fg='black',textvariable =TurnX,width =10,justify=LEFT).grid(row=0,column=2)


lblPlayerO =Label(RightFrame1, font=('arial',40,'bold'), text='Player O:',padx=2,pady=2,bg='cadet blue')
lblPlayerO.grid(row = 1, column =0,sticky = W)

txtPlayerO =Entry(RightFrame1, font=('arial',40,'bold'),bd = 2,fg='black',textvariable =PlayerO,width =4,justify=LEFT).grid(row=1,column=1)
Entry(RightFrame1, font=('arial',40,'bold'),bd = 2,fg='black',textvariable =TurnO,width =10,justify=LEFT).grid(row=1,column=2)

    #GAME BUTTONS

btn = [[0,0,0],
       [0,0,0],
       [0,0,0]]

for i in range(3):
    for j in range(3):
        btn[i][j] = Button(LeftFrame, text=" ",font =('Times 26 bold'),height =3 ,width =8 ,bg='gainsboro',command = lambda r=i, c=j:checker(btn[r][c]) )
        btn[i][j].grid(row=i+1,column=j, sticky=S+N+E+W)

    #RESET AND NEWGAME BUTTONS

btnReset = Button(RightFrame2, text="Reset",font =('arial',40, 'bold'),height =1 ,width =20 ,bg='gainsboro',command = reset )
btnReset.grid(row=0,column=0,padx = 6,pady=10)

btnNewGame = Button(RightFrame2, text="New Game",font =('arial',40, 'bold'),height =1 ,width =20 ,bg='gainsboro',command = NewGame)
btnNewGame.grid(row=1,column=0,padx=6,pady=10)

root.mainloop()
