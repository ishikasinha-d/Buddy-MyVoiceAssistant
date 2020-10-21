import random
def hangg():
    word=random.choice(["starwars","batman","avengers","ironman","supernaturals","sunshine","titanic","thor","interstellar"])
    valid="abcdefghijklmnopqrstuvwxyz"
    turns=10
    guessing=""
    while len(word)>0:
        main=""
        for i in word:
            if i in guessing:
                main = main + i
            else:
                main = main + "_" + " "
        print(main)
        guess=input("Make your guess")

        if guess in guessing:
            print ("Already entered by you....make another guess")
            guess=input()

        if guess in valid:
            guessing=guessing+guess
        else:
            print("Enter a valid character")
            guess=input()


        if guess not in word:
            turns=turns-1
            turnp(turns)
            if(turns==0):
                break
        if main==word:
            print("Yes.. the word is %s ",main)
            print("You won!")
            break

def turnp(n):
    print("turns left:",n)
    if n==9:
        print("_________")
    elif n==8:
        print("_________")
        print("    O    ")
    elif n==7:
        print("_________")
        print("    O    ")
        print("    |    ")
    elif n==6:
        print("_________")
        print("    O    ")
        print("    |    ")
        print("   /     ")
    elif n==5:
        print("_________")
        print("    O    ")
        print("    |    ")
        print("   / \   ")
    elif n==4:
        print("_________")
        print("   \O    ")
        print("    |    ")
        print("   / \   ")
    elif n==3:
        print("_________")
        print("   \O/   ")
        print("    |    ")
        print("   / \   ")
    elif n==2:
        print("The man is gonna die! Make wise guess")
        print("_________")
        print("   \O/|  ")
        print("    |    ")
        print("   / \   ")

    elif n==1:
        print("The rope has been tied!!!")
        print("You have last chance")
        print("_________")
        print("   \O_|  ")
        print("    |\   ")
        print("   / \   ")
    elif n==0:
        print("Oops! the innocent man died...")
        print("_________")
        print("    O_|  ")
        print("   /|\   ")
        print("   / \   ")



def hang():

    i=input("Do you want to play hangman (y/n) ? ")
    if(i=="Y" or i=="y"):
        name = input("Who are you??")
        print("Welcome to the game ", name)

        print("____________________________")
        print("You have to guess the word within 10 attempts to save the innocent man from getting hanged")
        hangg()
    else:
        print("okay not playing")


