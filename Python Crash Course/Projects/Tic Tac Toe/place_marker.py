from display_board import display_board

# places a mark on in position on the board
def place_marker(board, marker, position):
    board[position] = marker

# checks if place_marker works
# test_board = ['#','X','O','X','O','X','O','X','O','X']
# place_marker(test_board,"#",8)
# display_board(test_board)
