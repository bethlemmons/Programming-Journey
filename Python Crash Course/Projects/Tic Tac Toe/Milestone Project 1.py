from player_choice import player_choice
from replay import replay
from full_board_check import full_board_check
from space_check import space_check
from choose_first import choose_first
from win_check import win_check
from place_marker import place_marker
from display_board import display_board
from player_input import player_input

print("Welcome to Tick-Tack-Toe!")

while True:
    # reset the board
    play_game = input('Are you ready to play? Y/N? ')
    theBoard = [' '] * 10
    player1_marker, player2_marker = player_input()
    turn = choose_first()
    # print(turn + ' will go first.')

    # play_game = input('Are you ready to play? Y/N? ')

    if play_game.lower()[0] == 'y':
        game_on = True
    else:
        game_on = False

    while game_on:
        if turn == "Player 1":
            # player_1's turn

            display_board(theBoard)
            position = player_choice(theBoard)
            place_marker(theBoard, player1_marker, position)

            if win_check(theBoard, player1_marker):
                display_board(theBoard)
                print('Congratulations! You have won the game!')
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('The game is a draw!')
                else:
                    turn = 'Player 2'

        else:
            # player_2's turn

            display_board(theBoard)
            position = player_choice(theBoard)
            place_marker(theBoard, player2_marker, position)

            if win_check(theBoard, player2_marker):
                display_board(theBoard)
                print('Player 2 has won!')
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player 1'

    if not replay():
        break
