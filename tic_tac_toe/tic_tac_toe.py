board  = ['-','-','-','-','-','-','-','-','-','-']


#Draws Game Board
def DrawBoard():
     print(" %c %c %c " % (board[1],board[2],board[3]))
     print(" %c %c %c " % (board[4],board[5],board[6]))
     print(" %c %c %c " % (board[7],board[8],board[9]))
     print(30*"-")

#This Function Checks position is empty or not    
def CheckChoise(x):    
    if(board[x] == ' ' and board[x] >= 1 and board[x]<=9):    
        return True    
    else:    
        return False

#Checks if player won
def CheckWin():
     if(board[1] == board[2] and board[2] == board[3] and board[1] != ' '):
          print("Win")
#          Game = Win
     elif(board[4] == board[5] and board[5] == board[6] and board[4] != ' '):
          print("Win")
#          Game = Win
#     elif(board[7] == board[8] and board[8] == board[9] and board[7] != ' '):
#          Game = Win    
#Vertical Winning Condition
#     elif(board[1] == board[4] and board[4] == board[7] and board[1] != ' '):
#          Game = Win
#     elif(board[2] == board[5] and board[5] == board[8] and board[2] != ' '):
#          Game = Win
#     elif(board[3] == board[6] and board[6] == board[9] and board[3] != ' '):
#          Game=Win    
#Diagonal Winning Condition
#     elif(board[1] == board[5] and board[5] == board[9] and board[5] != ' '):
#          Game = Win
#     elif(board[3] == board[5] and board[5] == board[7] and board[5] != ' '):
#          Game=Win    
#Match Tie or Draw Condition
#     elif(board[1]!=' ' and board[2]!=' ' and board[3]!=' ' and board[4]!=' ' and board[5]!=' ' and board[6]!=' ' and board[7]!=' ' and board[8]!=' ' and board[9]!=' '):
#          Game=Draw
#     else:
#          Game=Running


for i in range(1,10):
    if i%2==1:      
        choice = int(input("Player 1 (X) turn\nEnter a position from 1 to 9\n"))
        board[choice] = 'X'
        DrawBoard()
        CheckWin()
    else:
        choice = int(input("Player 2 (O) turn\nEnter a position from 1 to 9\n"))
        board[choice] = 'O'
        DrawBoard()
        CheckWin()

    


