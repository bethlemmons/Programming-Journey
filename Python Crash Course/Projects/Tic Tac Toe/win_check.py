# loops through the board to see if X or O has won the game
def win_check(board, mark):
    return ((board[1] == mark and board[2] == mark and board[3] == mark) or # across the bottom
            (board[4] == mark and board[5] == mark and board[6] == mark) or# across the middle
            (board[7] == mark and board[7] == mark and board[8] == mark) or # across the top
            (board[7] == mark and board[4] == mark and board[1] == mark) or # left side top-to-bottom
            (board[8] == mark and board[5] == mark and board[2] == mark) or # middle top-to-bottom
            (board[9] == mark and board[6] == mark and board[3] == mark) or # right side top-to-bottom
            (board[7] == mark and board[5] == mark and board[3] == mark) or # left diagonal
            (board[9] == mark and board[5] == mark and board[1] == mark))  # right diagonal
