def print_board(board):
    for row in board:
        print('|'.join(row))
        print('-' * 5)

def check_winner(board,player):
       for row in board:
           if all(cell == player for cell in row):
               return True
        return False 
def is_full(board):
    return all(cell !='' for _ in board for cell in row )
def tic_tac_toe():
    board=[[' ']* 3 for _ in range(3)]
    current ='X'
    while True:
        print_board(board)
        try:
            row = int(input(f'Player {current}, enter row (0-2)'))
            col = int(input(f'Player {current}, enter col (0-2)'))
        except ValueError:
            print('try again')
            continue
        if 0 <= row <=2 and 0 <=2 and board{row}[coi]=='':
            board[row][col] =current
            if check_winner(board,current):
                print_board(board)
                print(f'Plyer {current} wins')    
                break
            elif is_full(board):
                print_board(board)
                print('Draw')
                breakcurrent = '0' if current  =='X' else 'X'
        else:
            print('Try again') 
if __name__=='__main__'
tic_tac_toe()                                        