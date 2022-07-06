from this import d


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
  print(" "  + str(spot1) + " | " + str(spot2) + " | " +str(spot3) + " ")
  print(" --|---|---")
  print(" " + str(spot4) + " | " + str(spot5) + " | " + str(spot6) + " ") 
  print(" --|---|---")
  print(" " + str(spot7) + " | " + str(spot8) + " | " + str(spot9) + " ")


def playgame():
    global spot1,spot2,spot3,spot4,spot5,spot6,spot7,spot8,spot9,player,turns,win
    if(turns != 9):
        if(player):
            user_input = input("Where would X like to play?")
            if (user_input== '1' and spot1 == 1):
                spot1 = 'X'
                printboard()
                player = False
                turns += 1
            elif (user_input== '2' and spot2 == 2):
                spot2 = 'X'
                printboard()
                player = False
                turns += 1
            elif (user_input== '3' and spot3 == 3):
                spot3 = 'X'
                printboard()
                player = False
                turns += 1
            elif (user_input== '4' and spot4 == 4):
                spot4 = 'X'
                printboard()
                player = False
                turns += 1
            elif (user_input== '5' and spot5 == 5):
                spot5 = 'X'
                printboard()
                player = False
                turns += 1
            elif (user_input== '6' and spot6 == 6):
                spot6 = 'X'
                printboard()
                player = False
                turns += 1
            elif (user_input== '7' and spot7 == 7):
                spot7 = 'X'
                printboard()
                player = False
                turns += 1
            elif (user_input== '8' and spot8 == 8):
                spot8 = 'X'
                printboard()
                player = False
                turns += 1
            elif (user_input== '9' and spot9 == 9):
                spot9 = 'X'
                printboard()
                player = False
                turns += 1
            else:
                print("Invalid Input: Please enter a valid number")
                playgame()
            
        else:
            user_input = input("Where would Y like to play?")
            
            if (user_input== '1' and spot1 == 1):
                spot1 = 'Y'
                printboard()
                player = True
                turns += 1
            elif (user_input== '2' and spot2 == 2):
                spot2 = 'Y'
                printboard()
                player = True
                turns += 1
            elif (user_input== '3' and spot3 == 3):
                spot3 = 'Y'
                printboard()
                player = True
                turns += 1
            elif (user_input== '4' and spot4 == 4):
                spot4 = 'Y'
                printboard()
                player = True
                turns += 1
            elif (user_input== '5' and spot5 == 5):
                spot5 = 'Y'
                printboard()
                player = True
                turns += 1
            elif (user_input== '6' and spot6 == 6):
                spot6 = 'Y'
                printboard()
                player = True
                turns += 1
            elif (user_input== '7' and spot7 == 7):
                spot7 = 'Y'
                printboard()
                player = True
                turns += 1
            elif (user_input== '8' and spot8 == 8):
                spot8 = 'Y'
                printboard()
                player = True
                turns += 1
            elif (user_input== '9' and spot9 == 9):
                spot9 = 'Y'
                printboard()
                player = True
                turns += 1
            else:
                print("Invalid Input: Please enter a valid number")
                playgame()
            
    else:
        print("Game Over")
        turns += 1

    

def check_winner():
    global spot1,spot2,spot3,spot4,spot5,spot6,spot7,spot8,spot9,player,turns,win
    if(spot1 == 'X' and spot2 == 'X' and spot3 == 'X'): 
        print("X wins 1")
        print("Game over")
        turns = 10
    elif(spot4 == 'X' and spot5 == 'X' and spot6 == 'X' ):
        print("X wins 2")
        print("Game over")
        turns = 10
    elif(spot7 == 'X' and spot8 == 'X' and spot9 == 'X'):
        print("X wins 3")
        print("Game over")
        turns = 10
    elif(spot1 == 'X' and spot5 == 'X' and spot9 == 'X'):
        print("X wins 4")
        print("Game over")
        turns = 10
    elif(spot3 == 'X' and spot5 == 'X' and spot7 == 'X'):
        print("X wins5")
        print("Game over")
        turns = 10
    elif(spot1 == 'X' and spot4 == 'X' and spot7 == 'X'):
        print("X wins6")
        print("Game over")
        turns = 10
    elif(spot2 == 'X' and spot5 == 'X' and spot8 == 'X'):
        print("X wins7")
        print("Game over")
        turns = 10
    elif(spot3 == 'X' and spot6 == 'X' and spot9 == 'X'):
        print("X wins8")
        print("Game over")
        turns = 10


    elif(spot1 == 'Y' and spot2 == 'Y' and spot3 == 'Y'): 
        print("Y wins1")
        print("Game over")
        turns = 10
    elif(spot4 == 'Y' and spot5 == 'Y' and spot6 == 'Y' ):
        print("Y wins2")
        print("Game over")
        turns = 10
    elif(spot7 == 'Y' and spot8 == 'Y' and spot9 == 'Y'):
        print("Y wins3")
        print("Game over")
        turns = 10
    elif(spot1 == 'Y' and spot5 == 'Y' and spot9 == 'Y'):
        print("Y wins4")
        print("Game over")
        turns = 10
    elif(spot3 == 'Y' and spot5 == 'Y' and spot7 == 'Y'):
        print("Y wins5")
        print("Game over")
        turns = 10
    elif(spot1 == 'Y' and spot4 == 'Y' and spot7 == 'Y'):
        print("Y wins6")
        print("Game over")
        turns = 10
    elif(spot2 == 'Y' and spot5 == 'Y' and spot8 == 'Y'):
        print("Y wins7")
        print("Game over")
        turns = 10
    elif(spot3 == 'Y' and spot6 == 'Y' and spot9 == 'Y'):
        print("Y wins8")
        print("Game over")
        turns = 10
        

        


printboard()

while(turns < 10):
    playgame()
    check_winner()
    print(turns)
