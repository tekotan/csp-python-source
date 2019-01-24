def hangman_display(guessed, secret):
    """
    Function that handles the display function of the hangman game
    args:
        guessed: The letters that is guessed
        secret: The correct hangman phrase
    returns:
        The string with the correctly guessed letters with dashes in place
    """
    return "".join(list(map(lambda y: y if y in guessed else "-", secret)))
def return_incorrect_letters(guessed, secret):
    """
    Function that gives the incorrect letters in the guess
    args:
        guessed: The letters that is guessed
        secret: The correct hangman phrase
    returns:
        The number of letters in guessed not in secret
    """
    return sum(list(map(lambda x: 1 if x not in secret else 0)))
incorrect_letters = 10
secret = "abcd"
while incorrect_letters > 0:
    try:
        guess = raw_input("enter your guess")
        
            incorrect_letters -= return_incorrect_letters(guess, secret)
        

