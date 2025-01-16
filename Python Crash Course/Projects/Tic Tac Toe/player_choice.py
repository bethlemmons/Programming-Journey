from space_check import space_check

# asks the player where they want to put a mark
def player_choice(board):
    position = 0

    while position not in [1, 2, 3, 4, 5, 6, 7, 8, 9] or not space_check(board, position):
        position = int(input('Choose your next position: (1-9) '))

    return position

    # next_position = int(input("Please indicate the next position you'd like to mark: "))
    #
    # if next_position == True in space_check:
    #     return next_position
    # else:
    #     return (f"{next_position} is already taken")
