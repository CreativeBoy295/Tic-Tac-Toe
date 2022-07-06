from this import d
import colorama
from colorama import Back, Fore, Style
colorama.init(autoreset=True)


spot1 = 1
spot2 = 2
spot3 = 3
spot4 = 4
spot5 = 5
spot6 = 6
spot7 = 7
spot8 = 8
spot9 = 9
player = True
turns = 0
win = False

def printboard():
    
     print(Back.RESET + " "  + str(spot1) + Back.RESET + " | " + str(spot2) + Back.RESET + " | " +str(spot3) + " ")
     print(" --|---|---")
     print(" " + str(spot4) + Back.RESET + " | " + str(spot5) + Back.RESET + " | " + str(spot6) + " ") 
     print(" --|---|---")
     print(" " + str(spot7) + Back.RESET + " | " + str(spot8) + Back.RESET + " | " + str(spot9) + " ")


def playgame():
    global spot1,spot2,spot3,spot4,spot5,spot6,spot7,spot8,spot9,player,turns,win
    if(turns != 9):
        if(player):
            user_input = input(Back.RED + "Where would X like to play?")
            if (user_input== '1' and spot1 == 1):
                print("\n")
                spot1 = Back.RED + 'X'
                printboard()
                player = False
                turns += 1
            elif (user_input== '2' and spot2 == 2):
                print("\n")
                spot2 = Back.RED + 'X'
                printboard()
                player = False
                turns += 1
            elif (user_input== '3' and spot3 == 3):
                print("\n")
                spot3 = Back.RED + 'X'
                printboard()
                player = False
                turns += 1
            elif (user_input== '4' and spot4 == 4):
                print("\n")
                spot4 = Back.RED + 'X'
                printboard()
                player = False
                turns += 1
            elif (user_input== '5' and spot5 == 5):
                print("\n")
                spot5 = Back.RED + 'X'
                printboard()
                player = False
                turns += 1
            elif (user_input== '6' and spot6 == 6):
                print("\n")
                spot6 = Back.RED + 'X'
                printboard()
                player = False
                turns += 1
            elif (user_input== '7' and spot7 == 7):
                print("\n")
                spot7 = Back.RED + 'X'
                printboard()
                player = False
                turns += 1
            elif (user_input== '8' and spot8 == 8):
                print("\n")
                spot8 = Back.RED + 'X'
                printboard()
                player = False
                turns += 1
            elif (user_input== '9' and spot9 == 9):
                print("\n")
                spot9 = Back.RED + 'X'
                printboard()
                player = False
                turns += 1
            else:
                print(Back.RED+"Invalid Input: Please enter a valid number")
                playgame()
            
        else:
            user_input = input(Back.BLUE+"Where would Y like to play?")
            
            if (user_input== '1' and spot1 == 1):
                print("\n")
                spot1 = Back.BLUE + 'Y'
                printboard()
                player = True
                turns += 1
            elif (user_input== '2' and spot2 == 2):
                print("\n")
                spot2 = Back.BLUE + 'Y'
                printboard()
                player = True
                turns += 1
            elif (user_input== '3' and spot3 == 3):
                print("\n")
                spot3 = Back.BLUE + 'Y'
                printboard()
                player = True
                turns += 1
            elif (user_input== '4' and spot4 == 4):
                print("\n")
                spot4 = Back.BLUE + 'Y'
                printboard()
                player = True
                turns += 1
            elif (user_input== '5' and spot5 == 5):
                print("\n")
                spot5 = Back.BLUE + 'Y'
                printboard()
                player = True
                turns += 1
            elif (user_input== '6' and spot6 == 6):
                print("\n")
                spot6 = Back.BLUE + 'Y'
                printboard()
                player = True
                turns += 1
            elif (user_input== '7' and spot7 == 7):
                print("\n")
                spot7 = Back.BLUE + 'Y'
                printboard()
                player = True
                turns += 1
            elif (user_input== '8' and spot8 == 8):
                print("\n")
                spot8 = Back.BLUE + 'Y'
                printboard()
                player = True
                turns += 1
            elif (user_input== '9' and spot9 == 9):
                print("\n")
                spot9 = Back.BLUE + 'Y'
                printboard()
                player = True
                turns += 1
            else:
                print(Back.BLUE + "Invalid Input: Please enter a valid number")
                playgame()
            
    else:
        print(Fore.LIGHTYELLOW_EX+"Game Over")
        turns += 1

    

def check_winner():
    global spot1,spot2,spot3,spot4,spot5,spot6,spot7,spot8,spot9,player,turns,win
    if(spot1 == Back.RED + 'X' and spot2 == Back.RED + 'X' and spot3 == Back.RED + 'X'): 
        print(Back.RED + "X wins ")
        print(Back.RED + "Game over")
        turns = 10
    elif(spot4  == Back.RED + 'X' and spot5 == Back.RED + 'X' and spot6 == Back.RED + 'X' ):
        print(Back.RED + "X wins ")
        print(Back.RED + "Game over")
        turns = 10
    elif(spot7  == Back.RED + 'X' and spot8 == Back.RED + 'X' and spot9 == Back.RED + 'X'):
        print(Back.RED + "X wins ")
        print(Back.RED + "Game over")
        turns = 10
    elif(spot1  == Back.RED + 'X' and spot5 == Back.RED + 'X' and spot9 == Back.RED + 'X'):
        print(Back.RED + "X wins ")
        print(Back.RED + "Game over")
        turns = 10
    elif(spot3  == Back.RED + 'X' and spot5 == Back.RED + 'X' and spot7 == Back.RED + 'X'):
        print(Back.RED + "X wins")
        print(Back.RED + "Game over")
        turns = 10
    elif(spot1  == Back.RED + 'X' and spot4 == Back.RED + 'X' and spot7 == Back.RED + 'X'):
        print(Back.RED + "X wins")
        print(Back.RED + "Game over")
        turns = 10
    elif(spot2  == Back.RED + 'X' and spot5 == Back.RED + 'X' and spot8 == Back.RED + 'X'):
        print(Back.RED + "X wins")
        print(Back.RED + "Game over")
        turns = 10
    elif(spot3  == Back.RED + 'X' and spot6 == Back.RED + 'X' and spot9 == Back.RED + 'X'):
        print(Back.RED + "X wins")
        print(Back.RED + "Game over")
        turns = 10


    elif(spot1 == Back.BLUE + 'Y' and spot2 == Back.BLUE + 'Y' and spot3 == Back.BLUE + 'Y'): 
        print(Back.BLUE + "Y wins")
        print(Back.BLUE + "Game over")
        turns = 10
    elif(spot4  == Back.BLUE + 'Y' and spot5 == Back.BLUE + 'Y' and spot6 == Back.BLUE + 'Y' ):
        print(Back.BLUE + "Y wins")
        print(Back.BLUE + "Game over")
        turns = 10
    elif(spot7  == Back.BLUE + 'Y' and spot8 == Back.BLUE + 'Y' and spot9 == Back.BLUE + 'Y'):
        print(Back.BLUE + "Y wins")
        print(Back.BLUE + "Game over")
        turns = 10
    elif(spot1  == Back.BLUE + 'Y' and spot5 == Back.BLUE + 'Y' and spot9 == Back.BLUE + 'Y'):
        print(Back.BLUE + "Y wins")
        print(Back.BLUE + "Game over")
        turns = 10
    elif(spot3  == Back.BLUE + 'Y' and spot5 == Back.BLUE + 'Y' and spot7 == Back.BLUE + 'Y'):
        print(Back.BLUE + "Y wins")
        print(Back.BLUE + "Game over")
        turns = 10
    elif(spot1  == Back.BLUE + 'Y' and spot4 == Back.BLUE + 'Y' and spot7 == Back.BLUE + 'Y'):
        print(Back.BLUE + "Y wins")
        print(Back.BLUE + "Game over")
        turns = 10
    elif(spot2  == Back.BLUE + 'Y' and spot5 == Back.BLUE + 'Y' and spot8 == Back.BLUE + 'Y'):
        print(Back.BLUE + "Y wins")
        print(Back.BLUE + "Game over")
        turns = 10
    elif(spot3  == Back.BLUE + 'Y' and spot6 == Back.BLUE + 'Y' and spot9 == Back.BLUE + 'Y'):
        print(Back.BLUE + "Y wins")
        print(Back.BLUE + "Game over")
        turns = 10
    
    
printboard()

while(turns < 10):
    playgame()
    check_winner()
