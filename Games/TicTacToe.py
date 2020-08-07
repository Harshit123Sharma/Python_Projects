from IPython.display import clear_output
import random


#Function to display Board.
def basic_board():
    clear_output()
    print('  1  |  2  |  3')
    print('-----------------')
    print('  4  |  5  |  6')
    print('-----------------')
    print('  7  |  8  |  9')


def show_board(board):
    clear_output()
    print('  ' + board[1] + '  |  ' + board[2] + '  |  ' + board[3])
    print('-----------------')
    print('  ' + board[4] + '  |  ' + board[5] + '  |  ' + board[6])
    print('-----------------')
    print('  ' + board[7] + '  |  ' + board[8] + '  |  ' + board[9])


def user_input():
    mark = ''

    while not (mark == 'X' or mark == 'O'):
        mark = input('\nPlayer 1: Do you want to be X or O? ').upper()

    if mark == 'X':
        return ('X', 'O')
    elif mark == 'O':
        return ('O', 'X')
    elif (mark != 'X' and mark != 'O') :
        print('\nNot in choice, choose again from option given -_- ')


def place_mark(board, marker, position):
    board[position] = marker    


def check_for_win(board,mark):
    
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or # across the top
    (board[4] == mark and board[5] == mark and board[6] == mark) or # across the middle
    (board[1] == mark and board[2] == mark and board[3] == mark) or # across the bottom
    (board[7] == mark and board[4] == mark and board[1] == mark) or # down the middle
    (board[8] == mark and board[5] == mark and board[2] == mark) or # down the middle
    (board[9] == mark and board[6] == mark and board[3] == mark) or # down the right side
    (board[7] == mark and board[5] == mark and board[3] == mark) or # diagonal check
    (board[9] == mark and board[5] == mark and board[1] == mark)) # diagonal check


def choose_first():
    if random.randint(0, 1) == 1:
        return 'Player 2'
    else:
        return 'Player 1'


def check_for_space(board, position):
    
    return board[position] == ' '    


def full_board_check(board):
    for i in range(1,10):
        if check_for_space(board, i):
            return False
    return True  


def player_choice(board):
    position = 0
    
    while position not in [1,2,3,4,5,6,7,8,9] or not check_for_space(board, position):
        position = int(input('Choose your next position (1-9) : '))
        if position == random.randint(1,10):
            return position 
        else:
            print('Not in choice, choose again -_- ')
    return position        


def play_again():
    
    return input('Do you want to play again? Enter Yes or No : ').lower().startswith('y')  


def game_play():
    print('Welcome to Tic Tac Toe!')
    basic_board()

    while True:
        # Reset the board
        board = [' ']*10
        player1_mark, player2_mark = user_input()
        turn = choose_first()
        print(turn + ' will go first.')
    
        play_game = input('Are you ready to play? Enter Yes or No.')
        if play_game == 'n' or play_game == 'N' or play_game == 'no' or play_game == 'No' or play_game == 'NO':
            break
    
        if play_game.lower()[0] == 'y':
          game_on = True
        else:
          game_on = False

        while game_on:
            if turn == 'Player 1':
                # Player1's turn.
            
                show_board(board)
                position = player_choice(board)
                place_mark(board, player1_mark, position)

                if check_for_win(board, player1_mark):
                    show_board(board)
                    print('Congratulations! You have won the game!')
                    game_on = False
                else:
                    if full_board_check(board):
                        show_board(board)
                        print('The game is a draw!')
                        break
                    else:
                        turn = 'Player 2'

            else:
                # Player2's turn.
            
                show_board(board)
                position = player_choice(board)
                place_mark(board, player2_mark, position)

                if check_for_win(board, player2_mark):
                    show_board(board)
                    print('Player 2 has won!')
                    game_on = False
                else:
                    if full_board_check(board):
                        show_board(board)
                        print('The game is a draw!')
                        break
                    else:
                        turn = 'Player 1'

        if not play_again():
            break  


game_play()         