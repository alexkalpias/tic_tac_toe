board  = ['-','-','-','-','-','-','-','-','-','-']
print("TIC TAC TOE GAME\n----------------")
print("Positions:\n1 2 3 \n4 5 6 \n7 8 9\n----------------\n\n")

#Draws Game Board
def DrawBoard():
     print(" %c %c %c " % (board[1],board[2],board[3]))
     print(" %c %c %c " % (board[4],board[5],board[6]))
     print(" %c %c %c " % (board[7],board[8],board[9]))
     print(30*"-")

#Checks if player won
def CheckWin():     
    #Horizontal winning condition    
    if(board[1] == board[2] and board[2] == board[3] and board[1] != '-'):
         print("Winnner is:")
         return True
    elif(board[4] == board[5] and board[5] == board[6] and board[4] != '-'):    
         print("Winnner is:")
         return True
    elif(board[7] == board[8] and board[8] == board[9] and board[7] != '-'):    
         print("Winnner is:")
         return True
    #Vertical Winning Condition    
    elif(board[1] == board[4] and board[4] == board[7] and board[1] != '-'):    
         print("Winnner is:")
         return True  
    elif(board[2] == board[5] and board[5] == board[8] and board[2] != '-'):    
         print("Winnner is:")
         return True    
    elif(board[3] == board[6] and board[6] == board[9] and board[3] != '-'):    
         print("Winnner is:")
         return True    
    #Diagonal Winning Condition    
    elif(board[1] == board[5] and board[5] == board[9] and board[5] != '-'):    
         print("Winnner is:")
         return True    
    elif(board[3] == board[5] and board[5] == board[7] and board[5] != '-'):    
         print("Winnner is:")
         return True    
    #Match Tie or Draw Condition    
    elif(board[1]!='-' and board[2]!='-' and board[3]!='-' and board[4]!='-' and board[5]!='-' and board[6]!='-' and board[7]!='-' and board[8]!='-' and board[9]!='-'):    
         print("We have a draw\n\n\n")
         return False    

def AvoidToLose():
     #Horizontal winning condition  
     if(board[1] == board[2] == 'X' and board[3] == '-'):
        board[3] = 'O'
        return True
     elif(board[2] == board[3] == 'X' and board[1] == '-'):
          board[1] = 'O'
          return True
     elif(board[1] == board[3] == 'X' and board[2] == '-'):
          board[2] = 'O'
          return True
     elif(board[4] == board[5] == 'X' and board[6] == '-'):
          board[6] = 'O'
          return True
     elif(board[5] == board[6] == 'X' and board[4] == '-'):
          board[4] = 'O'
          return True
     elif(board[4] == board[6] == 'X') and board[5] == '-':
          board[5] = 'O'
          return True
     elif(board[7] == board[8] == 'X' and board[9] == '-'):
          board[9] = 'O'
          return True
     elif(board[8] == board[9] == 'X' and board[7] == '-'):
          board[7] = 'O'
          return True
     elif(board[7] == board[9] == 'X' and board[8] == '-'):
          board[8] = 'O'
          return True
     #Vertical Winning Condition
     elif(board[1] == board[4] == 'X' and board[7] == '-'):
          board[7] = 'O'
          return True
     elif(board[4] == board[7] == 'X' and board[1] == '-'):
          board[1] = 'O'
          return True
     elif(board[1] == board[7] == 'X' and board[4] == '-'):
          board[4] = 'O'
          return True
     elif(board[2] == board[5] == 'X' and board[8] == '-'):
          board[8] = 'O'
          return True
     elif(board[5] == board[8] == 'X' and board[2] == '-'):
          board[2] = 'O'
          return True
     elif(board[2] == board[8] == 'X' and board[5] == '-'):
          board[5] = 'O'
          return True
     elif(board[3] == board[6] == 'X' and board[9] == '-'):
          board[9] = 'O'
          return True
     elif(board[6] == board[9] == 'X' and board[3] == '-'):
          board[3] = 'O'
          return True
     elif(board[3] == board[9] == 'X' and board[6] == '-'):
          board[6] = 'O'
          return True    
    #Diagonal Winning Condition 
     elif(board[1] == board[5] == 'X' and board[9] == '-'):
          board[9] = 'O'
          return True
     elif(board[1] == board[9] == 'X' and board[5] == '-'):
          board[5] = 'O'
          return True
     elif(board[5] == board[9] == 'X' and board[1] == '-'):
          board[1] = 'O'
          return True
     elif(board[3] == board[5] == 'X' and board[7] == '-'):
          board[7] = 'O'
          return True
     elif(board[5] == board[7] == 'X' and board[3] == '-'):
          board[3] = 'O'
          return True
     elif(board[3] == board[7] == 'X' and board[5] == '-'):
          board[5] = 'O'
          return True   

def TrytoWin():
     #Horizontal winning condition  
     if(board[1] == board[2] == 'O' and board[3] == '-'):
        board[3] = 'O'
        return True
     elif(board[2] == board[3] == 'O' and board[1] == '-'):
          board[1] = 'O'
          return True
     elif(board[1] == board[3] == 'O' and board[2] == '-'):
          board[2] = 'O'
          return True
     elif(board[4] == board[5] == 'O' and board[6] == '-'):
          board[6] = 'O'
          return True
     elif(board[5] == board[6] == 'O' and board[4] == '-'):
          board[4] = 'O'
          return True
     elif(board[4] == board[6] == 'O' and board[5] == '-'):
          board[5] = 'O'
          return True
     elif(board[7] == board[8] == 'O' and board[9] == '-'):
          board[9] = 'O'
          return True
     elif(board[8] == board[9] == 'O' and board[7] == '-'):
          board[7] = 'O'
          return True
     elif(board[7] == board[9] == 'O' and board[8] == '-'):
          board[8] = 'O'
          return True
     #Vertical Winning Condition
     elif(board[1] == board[4] == 'O' and board[7] == '-'):
          board[7] = 'O'
          return True
     elif(board[4] == board[7] == 'O' and board[1] == '-'):
          board[1] = 'O'
          return True
     elif(board[1] == board[7] == 'O' and board[4] == '-'):
          board[4] = 'O'
          return True
     elif(board[2] == board[5] == 'O' and board[8] == '-'):
          board[8] = 'O'
          return True
     elif(board[5] == board[8] == 'O' and board[2] == '-'):
          board[2] = 'O'
          return True
     elif(board[2] == board[8] == 'O' and board[5] == '-'):
          board[5] = 'O'
          return True
     elif(board[3] == board[6] == 'O' and board[9] == '-'):
          board[9] = 'O'
          return True
     elif(board[6] == board[9] == 'O' and board[3] == '-'):
          board[3] = 'O'
          return True
     elif(board[3] == board[9] == 'O' and board[6] == '-'):
          board[6] = 'O'
          return True    
    #Diagonal Winning Condition 
     elif(board[1] == board[5] == 'O' and board[9] == '-'):
          board[9] = 'O'
          return True
     elif(board[1] == board[9] == 'O' and board[5] == '-'):
          board[5] = 'O'
          return True
     elif(board[5] == board[9] == 'O' and board[1] == '-'):
          board[1] = 'O'
          return True
     elif(board[3] == board[5] == 'O' and board[7] == '-'):
          board[7] = 'O'
          return True
     elif(board[5] == board[7] == 'O' and board[3] == '-'):
          board[3] = 'O'
          return True
     elif(board[3] == board[7] == 'O' and board[5] == '-'):
          board[5] = 'O'
          return True   

def ChooseRandom():
     if board[2] == '-':
          print("Player 2 (O) turn")
          board[2] = 'O'
          return True
     elif board[4] == '-':
          print("Player 2 (O) turn")
          board[4] = 'O'
          return True
     elif board[8] == '-':
          print("Player 2 (O) turn")
          board[8] = 'O'
          return True
     elif board[6] == '-':
          print("Player 2 (O) turn")
          board[6] = 'O'
          return True
     elif board[1] == '-':
          print("Player 2 (O) turn")
          board[1] = 'O'
          return True
     elif board[3] == '-':
          print("Player 2 (O) turn")
          board[3] = 'O'
          return True
     elif board[7] == '-':
          print("Player 2 (O) turn")
          board[7] = 'O'
          return True
     elif board[9] == '-':
          print("Player 2 (O) turn")
          board[9] = 'O'
          return True
     

#Main
for i in range(1,10):
     if i%2==1:
          choice = int(input("Player 1 (X) turn\nEnter a position from 1 to 9\n"))
          while choice < 1 or choice > 9 or board[choice] != '-':
               choice = int(input("Player 1 (X) turn\nWrong Position!!!\nPlease enter a position from 1 to 9:\n"))
          board[choice] = 'X'
          DrawBoard()
          if CheckWin() == True:
               print("Player 1\n\n\n")
               break
     
#AI Player
     else:
          if i == 2 and board[5] == '-':
               print("Player 2 (O) turn")
               board[5] = 'O'
          elif TrytoWin() == True:
               print("Player 2 (O) turn")
          elif AvoidToLose() == True:
               print("Player 2 (O) turn")
          else:
               ChooseRandom()
               
          DrawBoard()
          if CheckWin() == True:
               print("Player 2\n\n\n")
               break


     
