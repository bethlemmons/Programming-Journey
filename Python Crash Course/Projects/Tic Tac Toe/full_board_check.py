from space_check import space_check


# function that checks if the board is full and returns a boolean value. True if full, False otherwise
def full_board_check(board):
    for i in range(1,10):
        if space_check(board,i):
            return False
    return True