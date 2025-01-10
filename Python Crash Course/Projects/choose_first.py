# import random library
import random

# function that uses random library to determine which player goes first
def choose_first():

    if random.randint(0, 1) == 0:
        print("Player 2 goes first.")
    else:
        print("Player 1 goes first.")


# test choose_first function
# choose_first()