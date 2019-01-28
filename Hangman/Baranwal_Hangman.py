from __future__ import print_function
from random import choice, randint
import utils
import time
import sys

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
                    char_in_secret in guessed or char_in_secret == " " else \
                    "-", secret)))
    return display_val, filter(lambda char: char != "-", display_val), 
def return_incorrect_letters(guessed, secret, prev_guesses):
    """
    Function that gives the incorrect letters in the guess
    args:
        guessed: The letters that is guessed
        secret: The correct hangman phrase
    returns:
        The number of letters in guessed not in secret
    """
    return sum(list(map(lambda char: 1 if char not in secret and char not in \
            prev_guesses else 0, guessed)))
def hangman():
    incorrect_letters_threshold = 10
    prev_incorrect_letters = set()
    first_iter = True
    prev_guess = ""
    print("You have 10 total incorrect letters that you can guess \n")
    secret_phrase = choice(utils.secret_list).lower()
    while incorrect_letters_threshold > 0:
        try:
            guess = raw_input("Enter your guess: \n")
            print("Calculating Results:\n")
            time.sleep(0.5)
            output_str, correct_guess = hangman_display(guess+prev_guess, secret_phrase)
            prev_guess += correct_guess
            incorrect_letters_threshold -= return_incorrect_letters(guess, secret_phrase, prev_incorrect_letters)
            if output_str != secret_phrase or incorrect_letters_threshold<1:
                if not first_iter:
                    print("You have already guessed {}!".format(", ".join(filter(lambda char: char in prev_incorrect_letters, guess))))
                prev_incorrect_letters.update(guess)
                print("You have {} more incorrect letters".format(max(incorrect_letters_threshold, 0)))
                print(output_str)
            else:
                print("You won!")
                print("The phrase was {}".format(secret_phrase))
                break
            if first_iter:
                first_iter = False
        except KeyboardInterrupt:
            print("\nYou exited the game")
            break
    else:
        _, letters_right = hangman_display(secret_phrase, output_str)
        if secret_phrase == output_str:
            print("Sorry, you got the right answer but guessed too many incorrect letters")
            print("The message was {}".format(secret_phrase))
        else:
            print("Sorry, you ran out of tries\n")
            print("The message was {}".format(secret_phrase))
            print("You needed the letters {} to win".format(", ".join(set(filter(lambda \
                                        char: char not in letters_right, secret_phrase)))))
        print("\n\n\n\n")
        replay = raw_input("Do you want to play again?")
        if replay.lower() == "yes":
            hangman()
hangman()