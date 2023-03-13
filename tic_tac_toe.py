board  = ['-','-','-','-','-','-','-','-','-','-']
Mark = 'X'

def DrawBoard():
     print(" %c %c %c " % (board[1],board[2],board[3]))
     print(" %c %c %c " % (board[4],board[5],board[6]))
     print(" %c %c %c " % (board[7],board[8],board[9]))
     print(30*"-")

for i in range(1,10):
    if i%2==1:      
        choice = int(input("Player 1 (X) turn\nEnter a position from 1 to 9\n"))
        board[choice] = 'X'
        DrawBoard()
    else:
        choice = int(input("Player 2 (O) turn\nEnter a position from 1 to 9\n"))
        board[choice] = 'O'
        DrawBoard()

    


