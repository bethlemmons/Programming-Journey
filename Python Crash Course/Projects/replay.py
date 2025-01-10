# asks player if they want to play again
def replay():
    return input('Do you want to play again? Enter Yes or No: ').lower().startswith('y')