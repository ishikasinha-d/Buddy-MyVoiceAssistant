import tkinter as tki
import random

def play(move):
    ch=random.choice(['scissors','rock','paper'])
    if((ch=='scissors' and move=='rock') or (ch=='rock' and move=='paper') or (ch=='paper' and move=='scissors')):
        r="You won"
    elif(ch==move):
        r="It's a draw"
    else:
        r="You lost"
    dis.config(text="Computer's move is "+ch+"\n"+r)
def click_s():
    play("scissors")
def click_p():
    play("paper")
def click_r():
    play("rock")


i = input("Do you want to play rock paper scissors? (y/n) ? ")
if (i == "Y" or i == "y"):
    w = tki.Tk()
    scissors = tki.Button(w, text="Scissors", bg='light salmon', padx=10, pady=5, command=click_s, width=20)
    scissors.pack(side="left")
    rock = tki.Button(w, text="rock", bg='light pink', padx=10, pady=5, command=click_r, width=20)
    rock.pack(side="left")
    paper = tki.Button(w, text="paper", bg='PaleTurquoise1', padx=10, pady=5, command=click_p, width=20)
    paper.pack(side="left")
    dis = tki.Button(w, text="What's your move???", fg='tomato', padx=10, pady=5, width=20)
    dis.pack(side="right")
    w.mainloop()
else:
    print("okay..not playing")





