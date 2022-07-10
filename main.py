from tkinter import *
import colorama
from colorama import Back, Fore
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
playerx = 'X'
playero = 'O'
user_input = None
user_value = None


mainWindow = Tk()
mainWindow.geometry("1100x600")

place = None
value = None
def place_click(number):
    place_entry.insert(0,number)
    place_entry.config(state=DISABLED)

def value_click(number):
    value_entry.insert(0,number)
    value_entry.config(state=DISABLED)

def submit():
    user_i = place_entry.get()
    user_v = value_entry.get()
    value_entry.config(state="normal")
    place_entry.config(state="normal")
    #value_entry.grid(row=8,column = 1 , columnspan = 3)
    place_entry.delete(0,END)
    value_entry.delete(0,END)
    #place_entry.grid(row=7,column = 1 , columnspan = 3)
    
    #player_label['text'] = "X"
    playgame(user_i, user_v)
    mainWindow.update()

label_place = Label(mainWindow,text="Where would you like to play?")
label_place.grid(row = 0 , column = 1 , columnspan = 3)
label_place.configure(font=("Times New Roman", 15, "italic"))

button1 = Button(mainWindow,text="1",height=4,width=8,font="Times 15 bold" , command= lambda: place_click(1)).grid(row = 1, column = 1)
button2 = Button(mainWindow,text="2",height=4,width=8,font="Times 15 bold" , command= lambda: place_click(2)).grid(row = 1, column = 2)
button3 = Button(mainWindow,text="3",height=4,width=8,font="Times 15 bold" , command= lambda: place_click(3)).grid(row = 1, column = 3)
button4 = Button(mainWindow,text="4",height=4,width=8,font="Times 15 bold" , command= lambda: place_click(4)).grid(row = 2, column = 1)
button5 = Button(mainWindow,text="5",height=4,width=8,font="Times 15 bold" , command= lambda: place_click(5)).grid(row = 2, column = 2)
button6 = Button(mainWindow,text="6",height=4,width=8,font="Times 15 bold" , command= lambda: place_click(6)).grid(row = 2, column = 3)
button7 = Button(mainWindow,text="7",height=4,width=8,font="Times 15 bold" , command= lambda: place_click(7)).grid(row = 3, column = 1)
button8 = Button(mainWindow,text="8",height=4,width=8,font="Times 15 bold" , command= lambda: place_click(8)).grid(row = 3, column = 2)
button9 = Button(mainWindow,text="9",height=4,width=8,font="Times 15 bold" , command= lambda: place_click(9)).grid(row = 3, column = 3)

label_place = Label(mainWindow,text="What value would you like to play?")
label_place.grid(row = 4 , column = 1 , columnspan = 3)
label_place.configure(font=("Times New Roman", 16, "italic"))

button_value1 = Button(mainWindow,text="1",height=4,width=8,font="Times 15 bold" , command= lambda: value_click(1)).grid(row = 5, column = 1)
button_value2 = Button(mainWindow,text="2",height=4,width=8,font="Times 15 bold" , command= lambda: value_click(2)).grid(row = 5, column = 2)
button_value3 = Button(mainWindow,text="3",height=4,width=8,font="Times 15 bold" , command= lambda: value_click(3)).grid(row = 5, column = 3)
button_value4 = Button(mainWindow,text="4",height=4,width=8,font="Times 15 bold" , command= lambda: value_click(4)).grid(row = 5, column = 4)
button_value5 = Button(mainWindow,text="5",height=4,width=8,font="Times 15 bold" , command= lambda: value_click(5)).grid(row = 5, column = 5)
button_value6 = Button(mainWindow,text="6",height=4,width=8,font="Times 15 bold" , command= lambda: value_click(6)).grid(row = 5, column = 6)
button_value7 = Button(mainWindow,text="7",height=4,width=8,font="Times 15 bold" , command= lambda: value_click(7)).grid(row = 5, column = 7)

player_label = Label(mainWindow,text="PLAYER: ")
player_label.grid(row = 1 , column = 4 , columnspan = 3)  
player_label.configure(font=("Times New Roman", 30, "bold"))

player_label = Label(mainWindow,text="X")
player_label.grid(row = 2 , column = 4 , columnspan = 3 , rowspan = 2)  
player_label.configure(font=("Times New Roman", 100, "bold"))

board_1 = Button(mainWindow,wraplength=5,text=spot1,height=4,width=8)
board_1.grid(row = 1 , column = 8 )  
board_1.configure(font=("Times New Roman", 15, "bold"))

board_2 = Button(mainWindow,wraplength=5,text=spot2,height=4,width=8)
board_2.grid(row = 1 , column = 9 )  
board_2.configure(font=("Times New Roman", 15, "bold"))

board_3 = Button(mainWindow,wraplength=5,text=spot3,height=4,width=8)
board_3.grid(row = 1 , column = 10 )  
board_3.configure(font=("Times New Roman", 15, "bold"))

board_4 = Button(mainWindow,wraplength=5,text=spot4,height=4,width=8)
board_4.grid(row = 2 , column = 8 )  
board_4.configure(font=("Times New Roman", 15, "bold"))

board_5 = Button(mainWindow,wraplength=5,text=spot5,height=4,width=8)
board_5.grid(row = 2 , column = 9 )  
board_5.configure(font=("Times New Roman", 15, "bold"))

board_6 = Button(mainWindow,wraplength=5,text=spot6,height=4,width=8)
board_6.grid(row = 2 , column = 10 )  
board_6.configure(font=("Times New Roman", 15, "bold"))

board_7 = Button(mainWindow,wraplength=5,text=spot7,height=4,width=8)
board_7.grid(row = 3 , column = 8 )  
board_7.configure(font=("Times New Roman", 15, "bold"))

board_8 = Button(mainWindow,wraplength=5,text=spot8,height=4,width=8)
board_8.grid(row = 3 , column = 9 )  
board_8.configure(font=("Times New Roman", 15, "bold"))

board_9 = Button(mainWindow,wraplength=5,text=spot9,height=4,width=8)
board_9.grid(row = 3 , column = 10 )  
board_9.configure(font=("Times New Roman", 15, "bold"))

label_over = Label(mainWindow,text="")
label_over.grid(row = 5 , column = 8 , columnspan = 3)
label_over.configure(font=("Times New Roman", 45, "italic"))

place_entry = Entry(mainWindow,width=50)
place_entry.grid(row = 6 , column =1 , columnspan = 3)

value_entry = Entry(mainWindow,width=50)
value_entry.grid(row = 7 , column =1 , columnspan = 3)

submit = Button(mainWindow,text = "Submit",command=submit)
submit.grid(row = 8 , column =1 , columnspan =3)


#lable1 = Label(mainWindow,text = "Hello").grid(row = 3, column =4,rowspan = 2 ,columnspan = 2)
label_p1 = Label(mainWindow,text = "X values: "+player1)
label_p1.grid(row=6,column=4)
label_p1.configure(font=("Times New Roman", 10, "bold"))

label_p2 = Label(mainWindow,text = "O values: " + player2)
label_p2.grid(row=7,column=4)
label_p2.configure(font=("Times New Roman", 10, "bold"))


def updatevariable():
    global board_1,board_2,board_3,board_4,board_5,board_6,board_7,board_8,board_9,spot1,spot2,spot3,spot4,spot5,spot6,spot7,spot8,spot9
    board_1['text'] = spot1
    board_2['text'] = spot2
    board_3['text'] = spot3
    board_4['text'] = spot4
    board_5['text'] = spot5
    board_6['text'] = spot6
    board_7['text'] = spot7
    board_8['text'] = spot8
    board_9['text'] = spot9
    label_p1['text'] ="X values: "+player1
    label_p2['text'] ="O values: "+player2

    if (playerx in str(spot1)):board_1['bg']="red"
    if (playerx in str(spot2)):board_2['bg']="red"
    if (playerx in str(spot3)):board_3['bg']="red"
    if (playerx in str(spot4)):board_4['bg']="red"
    if (playerx in str(spot5)):board_5['bg']="red"
    if (playerx in str(spot6)):board_6['bg']="red"
    if (playerx in str(spot7)):board_7['bg']="red"
    if (playerx in str(spot8)):board_8['bg']="red"
    if (playerx in str(spot9)):board_9['bg']="red"

    if(playero in str(spot1)):board_1['bg']="blue"
    if(playero in str(spot2)):board_2['bg']="blue"
    if(playero in str(spot3)):board_3['bg']="blue"
    if(playero in str(spot4)):board_4['bg']="blue"
    if(playero in str(spot5)):board_5['bg']="blue"
    if(playero in str(spot6)):board_6['bg']="blue"
    if(playero in str(spot7)):board_7['bg']="blue"
    if (playero in str( spot8)):board_8['bg']="blue"
    if (playero in str( spot9)):board_9['bg']="blue"

def printboard():
    
     print(Back.RESET + " "  + str(spot1) + Back.RESET + " | " + str(spot2) + Back.RESET + " | " +str(spot3) + " ")
     print(" --|---|---")
     print(" " + str(spot4) + Back.RESET + " | " + str(spot5) + Back.RESET + " | " + str(spot6) + " ") 
     print(" --|---|---")
     print(" " + str(spot7) + Back.RESET + " | " + str(spot8) + Back.RESET + " | " + str(spot9) + " ")
def playgame(user_in , user_va):
    global spot1,spot2,spot3,spot4,spot5,spot6,spot7,spot8,spot9,player,turns,win,user_value,backup_spot
    place=0
    if(end_game()):
        user_input = user_in
        if(player):
            #player_label['text'] = "X"
            if (user_input== '1' and spot1 == 1):
                print("\n")
                backup_spot = spot1
                spot1 = player1_value(user_va)
                if(spot1 is None):
                    spot1 = backup_spot
                printboard()
            elif (user_input== '2' and spot2 == 2):
                print("\n")
                backup_spot = spot2
                spot2 = player1_value(user_va)
                if(spot2 is None):
                    spot2 = backup_spot
                printboard()
            elif (user_input== '3' and spot3 == 3):
                print("\n")
                backup_spot = spot3
                spot3 = player1_value(user_va)
                if(spot3 is None):
                    spot3 = backup_spot
                printboard()
            elif (user_input== '4' and spot4 == 4):
                print("\n")
                backup_spot = spot4
                spot4 = player1_value(user_va)
                if(spot4 is None):
                    spot4 = backup_spot
                printboard()
            elif (user_input== '5' and spot5 == 5):
                print("\n")
                backup_spot = spot5
                spot5 = player1_value(user_va)
                if(spot5 is None):
                    spot5 = backup_spot
                printboard()
            elif (user_input== '6' and spot6 == 6):
                print("\n")
                backup_spot = spot6
                spot6 = player1_value(user_va)
                if(spot6 is None):
                    spot6 = backup_spot
                printboard()
            elif (user_input== '7' and spot7 == 7):
                print("\n")
                backup_spot = spot7
                spot7 = player1_value(user_va)
                if(spot7 is None):
                    spot7 = backup_spot
                printboard()
            elif (user_input== '8' and spot8 == 8):
                print("\n")
                backup_spot = spot8
                spot3 = player1_value(user_va)
                if(spot8 is None):
                    spot8 = backup_spot
                printboard()
            elif (user_input== '9' and spot9 == 9):
                print("\n")
                backup_spot = spot9
                spot9 = player1_value(user_va)
                if(spot9 is None):
                    spot9 = backup_spot
                printboard()
            elif (user_input== '1' and playero in spot1):
                print("\n")
                backup_spot = spot1
                spot1 = player1_value(user_va,spot1)
                if(spot1 is None):
                    spot1 = backup_spot
                printboard()
            elif (user_input== '2' and playero in spot2):
                print("\n")
                backup_spot = spot2
                spot2 = player1_value(user_va,spot2)
                if(spot2 is None):
                    spot2 = backup_spot
                printboard()
            elif (user_input== '3' and playero in spot3):
                print("\n")
                backup_spot = spot3
                spot3 = player1_value(user_va,spot3)
                if(spot3 is None):
                    spot3 = backup_spot
                printboard()
            elif (user_input== '4' and playero in spot4):
                print("\n")
                backup_spot = spot4
                spot4 = player1_value(user_va,spot4)
                if(spot4 is None):
                    spot4 = backup_spot
                printboard()
            elif (user_input== '5' and playero in spot5):
                print("\n")
                backup_spot = spot5
                spot5 = player1_value(user_va,spot5)
                if(spot5 is None):
                    spot5 = backup_spot
                printboard()
            elif (user_input== '6' and playero in spot6):
                print("\n")
                backup_spot = spot6
                spot6 = player1_value(user_va,spot6)
                if(spot6 is None):
                    spot6 = backup_spot
                printboard()
            elif (user_input== '7' and playero in spot7):
                print("\n")
                backup_spot = spot7
                spot7 = player1_value(user_va,spot7)
                if(spot7 is None):
                    spot7 = backup_spot
                printboard()
            elif (user_input== '8' and playero in spot8):
                print("\n")
                backup_spot = spot8
                spot8 = player1_value(user_va,spot8)
                if(spot8 is None):
                    spot8 = backup_spot
                printboard()
            elif (user_input== '9' and playero in spot9):
                print("\n")
                backup_spot = spot9
                spot9 = player1_value(user_va,spot9)
                if(spot9 is None):
                    spot9 = backup_spot
                printboard()

            
            else:
                print(Back.RED+"Invalid Input: Please enter a valid number")
                
            
        else:
            #player_label['text'] = 'X'
            
            if (user_input== '1' and spot1 == 1):
                print("\n")
                backup_spot = spot1
                spot1 = player2_value(user_va)
                if(spot1 is None):
                    spot1 = backup_spot
                printboard()
            elif (user_input== '2' and spot2 == 2):
                print("\n")
                backup_spot = spot2
                spot2 = player2_value(user_va)
                if(spot2 is None):
                    spot2 = backup_spot
                printboard()
            elif (user_input== '3' and spot3 == 3):
                print("\n")
                backup_spot = spot3
                spot3 = player2_value(user_va)
                if(spot3 is None):
                    spot3 = backup_spot
                printboard()
            elif (user_input== '4' and spot4 == 4):
                print("\n")
                backup_spot = spot4
                spot4 = player2_value(user_va)
                if(spot4 is None):
                    spot4 = backup_spot
                printboard()
            elif (user_input== '5' and spot5 == 5):
                print("\n")
                backup_spot = spot5
                spot5 = player2_value(user_va)
                if(spot5 is None):
                    spot5 = backup_spot
                printboard()
            elif (user_input== '6' and spot6 == 6):
                print("\n")
                backup_spot = spot6
                spot6 = player2_value(user_va)
                if(spot6 is None):
                    spot6 = backup_spot
                printboard()
            elif (user_input== '7' and spot7 == 7):
                print("\n")
                backup_spot = spot7
                spot7 = player2_value(user_va)
                if(spot7 is None):
                    spot7 = backup_spot
                printboard()
            elif (user_input== '8' and spot8 == 8):
                print("\n")
                backup_spot = spot8
                spot8 = player2_value(user_va)
                if(spot8 is None):
                    spot8 = backup_spot
                printboard()
            elif (user_input== '9' and spot9 == 9):
                print("\n")
                backup_spot = spot9
                spot9 = player2_value(user_va)
                if(spot9 is None):
                    spot9 = backup_spot
                printboard()
            elif (user_input== '1' and playerx in spot1):
                print("\n")
                backup_spot = spot1
                spot1 = player2_value(user_va,spot1)
                if(spot1 is None):
                    spot1 = backup_spot
                printboard()
            elif (user_input== '2' and playerx in spot2):
                print("\n")
                backup_spot = spot2
                spot2 = player2_value(user_va,spot2)
                if(spot2 is None):
                    spot2 = backup_spot
                printboard()
            elif (user_input== '3' and playerx in spot3):
                print("\n")
                backup_spot = spot3
                spot3 = player2_value(user_va,spot3)
                if(spot3 is None):
                    spot3 = backup_spot
                printboard()
            elif (user_input== '4' and playerx in spot4):
                print("\n")
                backup_spot = spot4
                spot4 = player2_value(user_va,spot4)
                if(spot4 is None):
                    spot4 = backup_spot
                printboard()
            elif (user_input== '5' and playerx in spot5):
                print("\n")
                backup_spot = spot5
                spot5 = player2_value(user_va,spot5)
                if(spot5 is None):
                    spot5 = backup_spot
                printboard()
            elif (user_input== '6' and playerx in spot6):
                print("\n")
                backup_spot = spot6
                spot6 = player2_value(user_va,spot6)
                if(spot6 is None):
                    spot6 = backup_spot
                printboard()
            elif (user_input== '7' and playerx in spot7):
                print("\n")
                backup_spot = spot7
                spot7 = player2_value(user_va,spot7)
                if(spot7 is None):
                    spot7 = backup_spot
                printboard()
            elif (user_input== '8' and playerx in spot8):
                print("\n")
                backup_spot = spot8
                spot8 = player2_value(user_va,spot8)
                if(spot8 is None):
                    spot8 = backup_spot
                printboard()
            elif (user_input== '9' and playerx in spot9):
                print("\n")
                backup_spot = spot9
                spot9 = player2_value(user_va,spot9)
                if(spot9 is None):
                    spot9 = backup_spot
                printboard()

            else:
                print(Back.BLUE + "Invalid Input: Please enter a valid number")
                #playgame()
            
    else:
        print(Fore.LIGHTYELLOW_EX+"Game Over")
        turns += 1
    updatevariable()
    check_winner()
def check_winner():
    global spot1,spot2,spot3,spot4,spot5,spot6,spot7,spot8,spot9,player,turns,win
    if(str(spot1).__contains__(playerx) and  str(spot2).__contains__(playerx) and  str(spot3).__contains__(playerx)): 
        label_over['text']="X wins"
        print(Back.RED + "Game over")
        turns = 10
    elif(str(spot4 ).__contains__(playerx) and str( spot5).__contains__(playerx) and str( spot6).__contains__(playerx)  ):
        label_over['text']="X wins"
        print(Back.RED + "Game over")
        turns = 10
    elif(str(spot7 ).__contains__(playerx) and str( spot8).__contains__(playerx) and str( spot9).__contains__(playerx) ):
        label_over['text']="X wins"
        print(Back.RED + "Game over")
        turns = 10
    elif(str(spot1 ).__contains__(playerx) and str( spot5).__contains__(playerx) and str( spot9).__contains__(playerx) ):
        label_over['text']="X wins"
        print(Back.RED + "Game over")
        turns = 10
    elif(str(spot3 ).__contains__(playerx) and str( spot5).__contains__(playerx) and str( spot7).__contains__(playerx) ):
        label_over['text']="X wins"
        print(Back.RED + "Game over")
        turns = 10
    elif(str(spot1 ).__contains__(playerx) and str( spot4).__contains__(playerx) and str( spot7).__contains__(playerx) ):
        label_over['text']="X wins"
        print(Back.RED + "Game over")
        turns = 10
    elif(str(spot2 ).__contains__(playerx) and str( spot5).__contains__(playerx) and str( spot8).__contains__(playerx) ):
        label_over['text']="X wins"
        print(Back.RED + "Game over")
        turns = 10
    elif(str(spot3 ).__contains__(playerx) and str( spot6).__contains__(playerx) and str( spot9).__contains__(playerx) ):
        label_over['text']="X wins"
        print(Back.RED + "Game over")
        turns = 10


    elif(str(spot1).__contains__(playero) and str( spot2).__contains__(playero) and str( spot3).__contains__(playero)): 
        label_over['text']="O wins"
        print(Back.BLUE + "Game over")
        turns = 10
    elif(str(spot4 ).__contains__(playero) and str( spot5).__contains__(playero) and str( spot6).__contains__(playero) ):
        label_over['text']="O wins"
        print(Back.BLUE + "Game over")
        turns = 10
    elif(str(spot7 ).__contains__(playero) and str( spot8).__contains__(playero) and str( spot9).__contains__(playero)):
        label_over['text']="O wins"
        print(Back.BLUE + "Game over")
        turns = 10
    elif(str(spot1 ).__contains__(playero) and str( spot5).__contains__(playero) and str( spot9).__contains__(playero)):
        label_over['text']="O wins"
        print(Back.BLUE + "Game over")
        turns = 10
    elif(str(spot3 ).__contains__(playero) and str( spot5).__contains__(playero) and str( spot7).__contains__(playero)):
        label_over['text']="O wins"
        print(Back.BLUE + "Game over")
        turns = 10
    elif(str(spot1 ).__contains__(playero) and str( spot4).__contains__(playero) and str( spot7).__contains__(playero)):
        label_over['text']="O wins"
        print(Back.BLUE + "Game over")
        turns = 10
    elif(str(spot2 ).__contains__(playero) and str( spot5).__contains__(playero) and str( spot8).__contains__(playero)):
        label_over['text']="O wins"
        print(Back.BLUE + "Game over")
        turns = 10
    elif(str(spot3 ).__contains__(playero) and str( spot6).__contains__(playero) and str( spot9).__contains__(playero)):
        label_over['text']="O wins"
        print(Back.BLUE + "Game over")
        turns = 10
def player1_value(user_val,spot_to_check=None):
    global spot1,spot2,spot3,spot4,spot5,spot6,spot7,spot8,spot9,player,turns,win,user_value,player1,player2
    print(player1)
    user_value=user_val
    if(player1.__contains__(user_value) and user_value  != ""):
        if(spot_to_check is None):
            player1 = player1.replace(user_value,'')
            spot = playerx + user_value
            player = False
            player_label['text']= "O"
            turns += 1
            return spot
        else:
            #$print(spot_to_check)
            #$spot_to_check = spot3
            #$print(type(spot_to_check))
            #$print(len(spot_to_check))
            #$print(spot_to_check[slice(5,7)])
            if(user_value > spot_to_check[slice(1,2)]):
                player1 = player1.replace(user_value,'')
                spot = playerx + user_value
                print(spot_to_check)
                player = False
                player_label['text']= "O"
                turns += 1
                return spot
            else:
                print("Invalid Number")
                #return 
    else:
        print("Invalid Number")
        #return 
def player2_value(user_val,spot_to_check = None):
    global spot1,spot2,spot3,spot4,spot5,spot6,spot7,spot8,spot9,player,turns,win,user_value,player1,player2
    print(player2)
    user_value= user_val

    if(player2.__contains__(user_value) and user_value is not None):
        if(spot_to_check is None):
            player2 = player2.replace(user_value,'')
            spot = playero + user_value
            player = True
            player_label['text']= "X"
            turns += 1
            
            return spot
        else:
            #print(spot_to_check)
            #spot_to_check = spot3
            #print(type(spot_to_check))
            #print(len(spot_to_check))
            #print(spot_to_check[slice(5,7)])
            if(user_value > spot_to_check[slice(1,2)]):
                player2 = player2.replace(user_value,'')
                spot = playero + user_value
                player = True
                player_label['text']= "X"
                turns += 1
                
                return spot
                
            else:
                print("Invalid Number")
                #playgame()
            
    else:
        print("Invalid Number")

def end_game():
    if(player1 is "" or player2 is ""):
        print(Fore.LIGHTYELLOW_EX+"Game Over!")
        return False
    elif (type(spot1)== str  and type(spot2)== str  and type(spot3)== str  and type(spot4)== str  and type(spot5)== str  and type(spot6)== str  and type(spot7)== str  and type(spot8)== str  and type(spot9) == str):
        return False
    else:
        return True
printboard()
def main():

    while(end_game()):

        #print("hello")
        playgame()

        check_winner()
        #print(user_value)
        #print(user_input)
        mainWindow.update()
        #print("hello")
        #mainWindow.after(100, main)

#mainWindow.after(100, main)
mainWindow.mainloop()





