from __future__ import print_function
import secret

def hangman_display(guessed, secret):
    """
    Function that handles the display function of the hangman game
    args:
        guessed: The letters that is guessed
        secret: The correct hangman phrase
    returns:
        The string with the correctly guessed letters with dashes in place
    """
    display_val = "".join(list(map(lambda char_in_secret: char_in_secret if \
                    char_in_secret in guessed else " " if char_in_secret == " " else \
                    "-", secret)))
    return display_val, filter(lambda char: char != "-", display_val)
def return_incorrect_letters(guessed, secret):
    """
    Function that gives the incorrect letters in the guess
    args:
        guessed: The letters that is guessed
        secret: The correct hangman phrase
    returns:
        The number of letters in guessed not in secret
    """
    return sum(list(map(lambda x: 1 if x not in secret else 0, guessed)))
incorrect_letters = 10
prev_guess = ""
print("You have 10 total incorrect letters that you can guess \n")
while incorrect_letters > 0:
    try:
        guess = raw_input("Enter your guess: \n")
        output_str, correct_guess = hangman_display(guess+prev_guess, secret.secret)
        prev_guess += correct_guess
        if output_str != secret.secret:
            incorrect_letters -= return_incorrect_letters(guess, secret.secret)
            print("You have {} more incorrect letters".format(incorrect_letters))
            print(output_str)
        else:
            print("You won!")
            break
    except KeyboardInterrupt:
        print("\nYou exited the game")
        break
else:
    print("Sorry, you ran out of tries")
    
        

