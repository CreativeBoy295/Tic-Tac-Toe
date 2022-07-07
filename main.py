from tkinter import N
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
player1 = '1234567'
player2 = '1234567'
backup_spot = None
def printboard():
    
     print(Back.RESET + " "  + str(spot1) + Back.RESET + " | " + str(spot2) + Back.RESET + " | " +str(spot3) + " ")
     print(" --|---|---")
     print(" " + str(spot4) + Back.RESET + " | " + str(spot5) + Back.RESET + " | " + str(spot6) + " ") 
     print(" --|---|---")
     print(" " + str(spot7) + Back.RESET + " | " + str(spot8) + Back.RESET + " | " + str(spot9) + " ")
def playgame():
    global spot1,spot2,spot3,spot4,spot5,spot6,spot7,spot8,spot9,player,turns,win,user_value,backup_spot
    if(end_game()):
        if(player):
            user_input = input(Back.RED + "Where would X like to play?")
            if (user_input== '1' and spot1 == 1):
                print("\n")
                
                spot1 = player1_value()
                printboard()
            elif (user_input== '2' and spot2 == 2):
                print("\n")
                
                spot2 = player1_value()
                printboard()
            elif (user_input== '3' and spot3 == 3):
                print("\n")
                
                spot3 = player1_value()
                printboard()
            elif (user_input== '4' and spot4 == 4):
                print("\n")
                
                spot4 = player1_value()
                printboard()
            elif (user_input== '5' and spot5 == 5):
                print("\n")
                
                spot5 = player1_value()
                printboard()
            elif (user_input== '6' and spot6 == 6):
                print("\n")
                
                spot6 = player1_value()
                printboard()
            elif (user_input== '7' and spot7 == 7):
                print("\n")
                
                spot7 = player1_value()
                printboard()
            elif (user_input== '8' and spot8 == 8):
                print("\n")
                
                spot8 = player1_value()
                printboard()
            elif (user_input== '9' and spot9 == 9):
                print("\n")
                
                spot9 = player1_value()
                printboard()
            elif (user_input== '1' and Back.BLUE in spot1):
                print("\n")
                backup_spot = spot1
                spot1 = player1_value(spot1)
                if(spot1 is None):
                    spot1 = backup_spot
                printboard()
            elif (user_input== '2' and Back.BLUE in spot2):
                print("\n")
                backup_spot = spot2
                spot2 = player1_value(spot2)
                if(spot2 is None):
                    spot2 = backup_spot
                printboard()
            elif (user_input== '3' and Back.BLUE in spot3):
                print("\n")
                backup_spot = spot3
                spot3 = player1_value(spot3)
                if(spot3 is None):
                    spot3 = backup_spot
                printboard()
            elif (user_input== '4' and Back.BLUE in spot4):
                print("\n")
                backup_spot = spot4
                spot4 = player1_value(spot4)
                if(spot4 is None):
                    spot4 = backup_spot
                printboard()
            elif (user_input== '5' and Back.BLUE in spot5):
                print("\n")
                backup_spot = spot5
                spot5 = player1_value(spot5)
                if(spot5 is None):
                    spot5 = backup_spot
                printboard()
            elif (user_input== '6' and Back.BLUE in spot6):
                print("\n")
                backup_spot = spot6
                spot6 = player1_value(spot6)
                if(spot6 is None):
                    spot6 = backup_spot
                printboard()
            elif (user_input== '7' and Back.BLUE in spot7):
                print("\n")
                backup_spot = spot7
                spot7 = player1_value(spot7)
                if(spot7 is None):
                    spot7 = backup_spot
                printboard()
            elif (user_input== '8' and Back.BLUE in spot8):
                print("\n")
                backup_spot = spot8
                spot8 = player1_value(spot8)
                if(spot8 is None):
                    spot8 = backup_spot
                printboard()
            elif (user_input== '9' and Back.BLUE in spot9):
                print("\n")
                backup_spot = spot9
                spot9 = player1_value(spot9)
                if(spot9 is None):
                    spot9 = backup_spot
                printboard()

            
            else:
                print(Back.RED+"Invalid Input: Please enter a valid number")
                playgame()
            
        else:
            user_input = input(Back.BLUE+"Where would Y like to play?")
            
            if (user_input== '1' and spot1 == 1):
                print("\n")
                
                spot1 = player2_value()
                printboard()
            elif (user_input== '2' and spot2 == 2):
                print("\n")
                
                spot2 = player2_value()
                printboard()
            elif (user_input== '3' and spot3 == 3):
                print("\n")
                
                spot3 = player2_value()
                printboard()
            elif (user_input== '4' and spot4 == 4):
                print("\n")
                
                spot4 = player2_value()
                printboard()
            elif (user_input== '5' and spot5 == 5):
                print("\n")
                
                spot5 = player2_value()
                printboard()
            elif (user_input== '6' and spot6 == 6):
                print("\n")
                
                spot6 =player2_value()
                printboard()
            elif (user_input== '7' and spot7 == 7):
                print("\n")
                
                spot7 = player2_value()
                printboard()
            elif (user_input== '8' and spot8 == 8):
                print("\n")
                
                spot8 =player2_value()
                printboard()
            elif (user_input== '9' and spot9 == 9):
                print("\n")
                
                spot9 =player2_value()
                printboard()
            elif (user_input== '1' and Back.RED in spot1):
                print("\n")
                backup_spot = spot1
                spot1 = player2_value(spot1)
                if(spot1 is None):
                    spot1 = backup_spot
                printboard()
            elif (user_input== '2' and Back.RED in spot2):
                print("\n")
                backup_spot = spot2
                spot2 = player2_value(spot2)
                if(spot2 is None):
                    spot2 = backup_spot
                printboard()
            elif (user_input== '3' and Back.RED in spot3):
                print("\n")
                backup_spot = spot3
                spot3 = player2_value(spot3)
                if(spot3 is None):
                    spot3 = backup_spot
                printboard()
            elif (user_input== '4' and Back.RED in spot4):
                print("\n")
                backup_spot = spot4
                spot4 = player2_value(spot4)
                if(spot4 is None):
                    spot4 = backup_spot
                printboard()
            elif (user_input== '5' and Back.RED in spot5):
                print("\n")
                backup_spot = spot5
                spot5 = player2_value(spot5)
                if(spot5 is None):
                    spot5 = backup_spot
                printboard()
            elif (user_input== '6' and Back.RED in spot6):
                print("\n")
                backup_spot = spot6
                spot6 = player2_value(spot6)
                if(spot6 is None):
                    spot6 = backup_spot
                printboard()
            elif (user_input== '7' and Back.RED in spot7):
                print("\n")
                backup_spot = spot7
                spot7 = player2_value(spot7)
                if(spot7 is None):
                    spot7 = backup_spot
                printboard()
            elif (user_input== '8' and Back.RED in spot8):
                print("\n")
                backup_spot = spot8
                spot8 = player2_value(spot8)
                if(spot8 is None):
                    spot8 = backup_spot
                printboard()
            elif (user_input== '9' and Back.RED in spot9):
                print("\n")
                backup_spot = spot9
                spot9 = player2_value(spot9)
                if(spot9 is None):
                    spot9 = backup_spot
                printboard()

            else:
                print(Back.BLUE + "Invalid Input: Please enter a valid number")
                playgame()
            
    else:
        print(Fore.LIGHTYELLOW_EX+"Game Over")
        turns += 1
def check_winner():
    global spot1,spot2,spot3,spot4,spot5,spot6,spot7,spot8,spot9,player,turns,win
    if(str(spot1).__contains__(Back.RED) and  str(spot2).__contains__(Back.RED) and  str(spot3).__contains__(Back.RED)): 
        print(Back.RED + "X wins ")
        print(Back.RED + "Game over")
        turns = 10
    elif(str(spot4 ).__contains__(Back.RED) and str( spot5).__contains__(Back.RED) and str( spot6).__contains__(Back.RED)  ):
        print(Back.RED + "X wins ")
        print(Back.RED + "Game over")
        turns = 10
    elif(str(spot7 ).__contains__(Back.RED) and str( spot8).__contains__(Back.RED) and str( spot9).__contains__(Back.RED) ):
        print(Back.RED + "X wins ")
        print(Back.RED + "Game over")
        turns = 10
    elif(str(spot1 ).__contains__(Back.RED) and str( spot5).__contains__(Back.RED) and str( spot9).__contains__(Back.RED) ):
        print(Back.RED + "X wins ")
        print(Back.RED + "Game over")
        turns = 10
    elif(str(spot3 ).__contains__(Back.RED) and str( spot5).__contains__(Back.RED) and str( spot7).__contains__(Back.RED) ):
        print(Back.RED + "X wins")
        print(Back.RED + "Game over")
        turns = 10
    elif(str(spot1 ).__contains__(Back.RED) and str( spot4).__contains__(Back.RED) and str( spot7).__contains__(Back.RED) ):
        print(Back.RED + "X wins")
        print(Back.RED + "Game over")
        turns = 10
    elif(str(spot2 ).__contains__(Back.RED) and str( spot5).__contains__(Back.RED) and str( spot8).__contains__(Back.RED) ):
        print(Back.RED + "X wins")
        print(Back.RED + "Game over")
        turns = 10
    elif(str(spot3 ).__contains__(Back.RED) and str( spot6).__contains__(Back.RED) and str( spot9).__contains__(Back.RED) ):
        print(Back.RED + "X wins")
        print(Back.RED + "Game over")
        turns = 10


    elif(str(spot1).__contains__(Back.BLUE) and str( spot2).__contains__(Back.BLUE) and str( spot3).__contains__(Back.BLUE)): 
        print(Back.BLUE + "Y wins")
        print(Back.BLUE + "Game over")
        turns = 10
    elif(str(spot4 ).__contains__(Back.BLUE) and str( spot5).__contains__(Back.BLUE) and str( spot6).__contains__(Back.BLUE) ):
        print(Back.BLUE + "Y wins")
        print(Back.BLUE + "Game over")
        turns = 10
    elif(str(spot7 ).__contains__(Back.BLUE) and str( spot8).__contains__(Back.BLUE) and str( spot9).__contains__(Back.BLUE)):
        print(Back.BLUE + "Y wins")
        print(Back.BLUE + "Game over")
        turns = 10
    elif(str(spot1 ).__contains__(Back.BLUE) and str( spot5).__contains__(Back.BLUE) and str( spot9).__contains__(Back.BLUE)):
        print(Back.BLUE + "Y wins")
        print(Back.BLUE + "Game over")
        turns = 10
    elif(str(spot3 ).__contains__(Back.BLUE) and str( spot5).__contains__(Back.BLUE) and str( spot7).__contains__(Back.BLUE)):
        print(Back.BLUE + "Y wins")
        print(Back.BLUE + "Game over")
        turns = 10
    elif(str(spot1 ).__contains__(Back.BLUE) and str( spot4).__contains__(Back.BLUE) and str( spot7).__contains__(Back.BLUE)):
        print(Back.BLUE + "Y wins")
        print(Back.BLUE + "Game over")
        turns = 10
    elif(str(spot2 ).__contains__(Back.BLUE) and str( spot5).__contains__(Back.BLUE) and str( spot8).__contains__(Back.BLUE)):
        print(Back.BLUE + "Y wins")
        print(Back.BLUE + "Game over")
        turns = 10
    elif(str(spot3 ).__contains__(Back.BLUE) and str( spot6).__contains__(Back.BLUE) and str( spot9).__contains__(Back.BLUE)):
        print(Back.BLUE + "Y wins")
        print(Back.BLUE + "Game over")
        turns = 10
def player1_value(spot_to_check=None):
    global spot1,spot2,spot3,spot4,spot5,spot6,spot7,spot8,spot9,player,turns,win,user_value,player1,player2
    print(player1)
    user_value = input(Back.RED + "What value would you like to play?")
    if(player1.__contains__(user_value) and user_value  != ""):
        if(spot_to_check is None):
            player1 = player1.replace(user_value,'')
            spot = Back.RED + user_value
            player = False
            turns += 1
            return spot
        else:
            #$print(spot_to_check)
            #$spot_to_check = spot3
            #$print(type(spot_to_check))
            #$print(len(spot_to_check))
            #$print(spot_to_check[slice(5,7)])
            if(user_value > spot_to_check[slice(5,7)]):
                player1 = player1.replace(user_value,'')
                spot = Back.RED + user_value
                print(spot_to_check)
                player = False
                turns += 1
                return spot
            else:
                print("Invalid Number")
                return playgame()
    else:
        print("Invalid Number")
        return player1_value()
def player2_value(spot_to_check = None):
    global spot1,spot2,spot3,spot4,spot5,spot6,spot7,spot8,spot9,player,turns,win,user_value,player1,player2
    print(player2)
    user_value = input(Back.BLUE + "What value would you like to play?")
    

    if(player2.__contains__(user_value) and user_value is not None):
        if(spot_to_check is None):
            player2 = player2.replace(user_value,'')
            spot = Back.BLUE + user_value
            player = True
            turns += 1
            
            return spot
        else:
            #print(spot_to_check)
            #spot_to_check = spot3
            #print(type(spot_to_check))
            #print(len(spot_to_check))
            #print(spot_to_check[slice(5,7)])
            if(user_value > spot_to_check[slice(5,7)]):
                player2 = player2.replace(user_value,'')
                spot = Back.BLUE + user_value
                player = True
                turns += 1
                
                return spot
                
            else:
                print("Invalid Number")
                playgame()
            
    else:
        print("Invalid Number")
        return player2_value()
def end_game():
    if(player1 is "" or player2 is ""):
        print(Fore.LIGHTYELLOW_EX+"Game Over!")
        return False
    elif (type(spot1)== str  and type(spot2)== str  and type(spot3)== str  and type(spot4)== str  and type(spot5)== str  and type(spot6)== str  and type(spot7)== str  and type(spot8)== str  and type(spot9) == str):
        return False
    else:
        return True
printboard()
while(end_game()):
    playgame()
    check_winner()
print(Fore.LIGHTYELLOW_EX+"Game Over!")