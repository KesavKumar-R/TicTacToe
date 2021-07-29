def display_board(board):
    print(board[7]+' | '+board[8]+' | '+board[9])
    print(board[4]+' | '+board[5]+' | '+board[6])
    print(board[1]+' | '+board[2]+' | '+board[3])

def player_input():
    marker=''
    while marker!='x' and marker!='o':
        marker=input('Player1 :Enter X or O')
    if marker=='x':
        return ('x','o')
    elif marker=='o':
        return('o','x')

def place_marker(board,position,marker):
    board[position]=marker

def win_check(board,mark):
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or # across the top
    (board[4] == mark and board[5] == mark and board[6] == mark) or # across the middle
    (board[1] == mark and board[2] == mark and board[3] == mark) or # across the bottom
    (board[7] == mark and board[4] == mark and board[1] == mark) or # down the middle
    (board[8] == mark and board[5] == mark and board[2] == mark) or # down the middle
    (board[9] == mark and board[6] == mark and board[3] == mark) or # down the right side
    (board[7] == mark and board[5] == mark and board[3] == mark) or # diagonal
    (board[9] == mark and board[5] == mark and board[1] == mark)) # diagonal


# In[6]:


import random
def choose_first():
    if random.randint(0,1)==0:
        return 'player2'
    else:
        return 'player1'




def space_check(board,position):
    return board[position]==' '




def full_board(board):
    for i in range(1,10):
        if space_check(board,i):
            return False
    return True    





def position_check(board):
    position=0
    while position not in range(1,11) or space_check(board,position)==True :
        position=input('Enter Number Between 1 to 9')
        if int(position)<10:
            return int(position)
    


def replay():
    return input('do u need to play again?y or n').lower().startswith('y')


print('WELCOME TO TIC TAC TOE')
while True:
    board=[' ']*10
    board[0]='*'
    display_board(board)
    print('Choose the marker X or O')
    player1,player2=player_input()
    start=choose_first()
    play_game=input('Ready to Play the Game: Y or N')
    if play_game=='y':
        game_on=True
    elif play_game=='n':
        game_on==False
    print(f'{start} will start first')    
    while game_on:
        if start=='player1':
            display_board(board)
            position=position_check(board)
            place_marker(board,position,player1)
            if win_check(board,player1)==True:
                print('PLAYER 1 HAS WON')
                game_on=False
            else:    
                if full_board(board)==True:
                    print('TIE GAME')
                    game_on=False
                else:
                    start='player2'
        if start=='player2':
            display_board(board)
            position=position_check(board)
            place_marker(board,position,player2)
            if win_check(board,player2)==True:
                print('PLAYER 2 HAS WON')
                game_on=False
            else:    
                if full_board(board)==True:
                    print('TIE GAME')
                    game_on==False
                else:
                    start='player1'
    display_board(board)
    if not replay():
        break
                             
                












