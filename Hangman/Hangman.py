from __future__ import print_function
from random import choice, randint
import utils_improved as utils
import time
import sys
import pdb

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
        prev_guesses: The letters already guessed so incorrect guesses aren't counted 2 times
    returns:
        The number of letters in guessed not in secret
    """
    return sum(list(map(lambda char: 1 if char not in secret and char not in \
            prev_guesses else 0, guessed)))
def play_game():
    secret_phrase = choice(utils.secret_list).lower()
    game_status = {
        "incorrect_letters_threshold":9,
        "print_vals":{
            "phrase_num":1,
            "guessed_letters":"",
            "avg_":0,
            "theme":"",
            "phrase":hangman_display("", secret_phrase)[0]
            
        },
        "prev_guess":set(),
        "num_correct_guesses": 0,
        "num_incorrect_guesses": 0
    }

    while game_status["incorrect_letters_threshold"] > 0:
        print(utils.hangman_ascii[max(game_status["incorrect_letters_threshold"]-1, 0)].format(**game_status["print_vals"]))
        try:
            guess = raw_input("Enter your guess: \n")
            output_str, correct_guess = hangman_display(guess+"".join(game_status["prev_guess"]), secret_phrase)
            game_status["print_vals"]["phrase"] = output_str
            game_status["print_vals"]["guessed_letters"] = ", ".join(game_status["prev_guess"])
            game_status["incorrect_letters_threshold"] -= return_incorrect_letters(guess, secret_phrase, game_status["prev_guess"])
            game_status["num_correct_guesses"] += len(correct_guess)
            game_status["num_incorrect_guesses"] += len(game_status["prev_guess"]) - len(correct_guess)
            try:
                game_status["print_vals"]["avg_"] = game_status["num_correct_guesses"]/len(game_status["prev_guess"])
            except ZeroDivisionError:
                game_status["print_vals"]["avg_"] = 0
            game_status["prev_guess"].update(guess)
            if game_status["print_vals"]["phrase"] == secret_phrase:
                print("You won!")
                break
            # pdb.set_trace()
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
            play_game()
play_game()