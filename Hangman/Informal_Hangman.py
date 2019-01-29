from __future__ import print_function

import time
import sys

from random import choice, randint

import utils

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
            prev_guesses else 0, set(guessed))))
def hangman():
    """
    Function that handles the entire hangman game
    
    returns:
        None
    """
    output_str = ""
    incorrect_letters_threshold = 10
    prev_incorrect_letters = set()
    first_iter = True
    prev_guess = ""
    print("----------------Welcome to the Class Hangman Game----------------")
    print("---The theme of this game is the names of people in this class---")
    print("------Lets See How Well You Know the People in Our Class---------")
    print("---You have 10 total incorrect letters that you can guess--------\n")
    secret_phrase = choice(utils.secret_list).lower()
    print("Phrase: {}".format(hangman_display("", secret_phrase)[0]))
    # print("Testing Phrase: {}".format(secret_phrase)) # Will be removed after testing
    win = False
    while incorrect_letters_threshold > 0 and not win:
        try:
            guess = raw_input("Enter your guess: \n").lower()
            print("Calculating Results:\n")
            time.sleep(0.5)
            output_str, correct_guess = hangman_display(guess+prev_guess, secret_phrase)
            prev_guess += correct_guess
            incorrect_letters_threshold -= return_incorrect_letters(guess, secret_phrase, \
                                            prev_incorrect_letters)
            if output_str != secret_phrase or incorrect_letters_threshold<1:
                if not first_iter:
                    already_guessed = set(filter(lambda char: char in prev_incorrect_letters, \
                                        guess))
                    if len(already_guessed) != 0:
                        print("You have already guessed {}!".format(\
                                ", ".join(already_guessed)))
                prev_incorrect_letters.update(guess)
                print("You have {} more incorrect letters".format(\
                            max(incorrect_letters_threshold, 0)))
                print(output_str)
            else:
                print("You won!")
                if incorrect_letters_threshold > 7:
                    print("Wow, you are a master at the names in this class!")
                elif 7 > incorrect_letters_threshold > 4:
                    print("You are pretty good at names in this class!")
                elif 4 > incorrect_letters_threshold > 2:
                    print("Dang, you must be having a really bad day! You barely guessed {}'s name!".format(secret_phrase))
                else:
                    print("Wow, you really suck at names, find a new class!")
                print("The phrase was {}".format(secret_phrase))
                win = True
            if first_iter:
                first_iter = False
        except KeyboardInterrupt:
            print("\nYou exited the game")
            break
        sys.stdout.flush()
    else:
        if not win:
            _, letters_right = hangman_display(secret_phrase, output_str)
            if secret_phrase == output_str:
                print("Sorry, you got the right answer but guessed too many incorrect letters")
                print("The message was {}".format(secret_phrase))
            else:
                print("Sorry, you ran out of tries\n")
                print("The message was {}".format(secret_phrase))
                print("You needed the letters {} to win".format(", ".join(set(filter(lambda \
                                            char: char not in letters_right, secret_phrase)))))
            print("\n\n")
        replay = raw_input("Do you want to play again?").lower()
        if replay.lower() in ["yes", "y"]:
            hangman()
hangman()