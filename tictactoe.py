import random
board = [' ' for _ in range(9)]
def isspace(pos):
    return board[pos]==' '
def insert(move,pos):
    board[pos]=move
def printBoard(board):
    print("   |   |   ")
    print(" "+board[0]+" | "+board[1]+" | "+board[2] )
    print("   |   |   ")
    print("-----------")
    print("   |   |   ")
    print(" "+board[3]+" | "+board[4]+" | "+board[5] )
    print("   |   |   ")
    print("-----------")
    print("   |   |   ")
    print(" " + board[6] + " | " + board[7] + " | " + board[8])
    print("   |   |   ")
    print()
def isfull(board):
    return board.count(' ')==0
def iswinner(l,b):
    return (b[0]==l and b[1]==l and b[2]==l) or (b[3]==l and b[4]==l and b[5]==l) or (b[6]==l and b[7]==l and b[8]==l)or(b[0]==l and b[3]==l and b[6]==l)or(b[1] == l and b[4] == l and b[7] == l) or (b[2] == l and b[5] == l and b[8] == l) or (b[0] == l and b[4] == l and b[8] == l)or (b[2] == l and b[4] == l and b[6] == l)
def playermove(board):
    run=True
    while run:
        try:
            move=int(input("Enter a position in range 1 to 9"))-1

            if move in range(0,9):
                if isspace(move):
                    run = False
                    board[move]="X"
                else: print("The space is pre-occupied")
            else:
                print("You entered value out of specified range")
        except:
            print("Enter a valid move position")
def computermove(board):
    possiblemoves=[x for x,letter in enumerate(board) if letter==' ']

    move=0
    for let in ['O','X']:
        for i in possiblemoves:
            bcopy=board[:]
            bcopy[i]=let
            if(iswinner(let,bcopy)):
                move=i
                return move
    cornersopen=[]
    for x in possiblemoves:
        if x in [0,2,6,8]:
            cornersopen.append(x)

    if len(cornersopen)>0:
        move=random.choice(cornersopen)
        return move
    if 4 in possiblemoves:
        move=4
        return move
    edgesopen = [x for x in possiblemoves if x in [1, 3, 5, 7]]
    if len(edgesopen)>0:
        move=random.choice(edgesopen)
        return move
def main(board):
    print("Let's play tic-tac-toe :) ")
    print("Your move=X and Computer's move=O")
    printBoard(board)

    while not(isfull(board)):
        if not(iswinner("O",board)):
            playermove(board)
            printBoard(board)

        else:
            print("You Lost!")
            break


        if not (iswinner("X", board)) :
            if (not(isfull(board))):
                m=computermove(board)
                board[m]="O"
                print("Computer's move at pos: ",(m+1))
                printBoard(board)

        else:
            print("You Win!")
            break
    else:
        if isfull(board):
            print("It's a Tie")




def playttt():
    while True:
        choice = input("Do you want to play? (y/n)")
        if (choice.lower() == "y"):
            board = [' ' for _ in range(9)]
            print("---------------------------------")
            main(board)
        else:
            break
