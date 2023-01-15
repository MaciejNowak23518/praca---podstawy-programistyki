import os    
import time   

board = [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']    
player = 1    
   
    
Win = 1    
Draw = -1    
Running = 0    
Stop = 1    
   
Game = Running    
Mark = 'X'    
   
#tak wygląda skrypt na plansze
def DrawBoard():    
    print(" %c | %c | %c " % (board[1],board[2],board[3]))    
    print("___|___|___")    
    print(" %c | %c | %c " % (board[4],board[5],board[6]))    
    print("___|___|___")    
    print(" %c | %c | %c " % (board[7],board[8],board[9]))    
    print("   |   |   ")    
   
  
def CheckPosition(x):    
    if(board[x] == ' '):    
        return True    
    else:    
        return False    
   
   
def CheckWin():    
    global Game    
    # wygrana przez ustawienie poziomo krzyzykow lub kolek  
    if(board[1] == board[2] and board[2] == board[3] and board[1] != ' '):    
        Game = Win    
    elif(board[4] == board[5] and board[5] == board[6] and board[4] != ' '):    
        Game = Win    
    elif(board[7] == board[8] and board[8] == board[9] and board[7] != ' '):    
        Game = Win    
    # wariant pionowy z wygraną  
    elif(board[1] == board[4] and board[4] == board[7] and board[1] != ' '):    
        Game = Win    
    elif(board[2] == board[5] and board[5] == board[8] and board[2] != ' '):    
        Game = Win    
    elif(board[3] == board[6] and board[6] == board[9] and board[3] != ' '):    
        Game=Win    
    # wariant wygranej na krzyż   
    elif(board[1] == board[5] and board[5] == board[9] and board[5] != ' '):    
        Game = Win    
    elif(board[3] == board[5] and board[5] == board[7] and board[5] != ' '):    
        Game=Win    
    # Remis  
    elif(board[1]!=' ' and board[2]!=' ' and board[3]!=' ' and board[4]!=' ' and board[5]!=' ' and board[6]!=' ' and board[7]!=' ' and board[8]!=' ' and board[9]!=' '):    
        Game=Draw    
    else:            
        Game=Running    
    
   
print("Gracz 1 [X] --- Gracz 2 [O]\n")    
print()    
print()    
print("prosze czekac...")    
time.sleep(3)    
while(Game == Running):    
    os.system('cls')    
    DrawBoard()    
    if(player % 2 != 0):    
        print("gracz 1 ")    
        Mark = 'X'    
    else:    
        print("gracz 2")    
        Mark = 'O'    
    choice = int(input("wpisz pozycje od 1-9 w ktorej chcesz postawic kolko lub krzyzyk : "))    
    if(CheckPosition(choice)):    
        board[choice] = Mark    
        player+=1    
        CheckWin()    
    
os.system('cls')    
DrawBoard()    
if(Game==Draw):    
    print("Remis!")    
elif(Game==Win):    
    player-=1    
    if(player%2!=0):    
        print("Gracz 1 wygral")    
    else:    
        print("Gracz 2 wygral")    