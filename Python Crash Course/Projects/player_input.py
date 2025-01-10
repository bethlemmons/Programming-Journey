# created to take in user input and validate formatting
def player_input():
    marker = ''

    # marker = input('Player 1: Would you like to be X or O? ').upper()

    # loops through to take input and verify formatting
    while not (marker == "X" or marker == 'O'):
        marker = input('Player 1: Would you like to be X or O? ').upper()
        # marker = input("Not a valid option. Please pick either X or O. ").upper()

        if marker == 'X':
            return ('X', 'O')
        elif marker == 'O':
            return('O', 'X')


# calls player_input function
# player_input()