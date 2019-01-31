from __future__ import print_function

import time
import sys

from random import choice, randint

import utils

def hangman():
    """
    Function that handles the entire hangman game
    
    returns:
        None
    """
    name, hint = choice(list(utils.secret_dict.items()))
    name = name.lower()
    hint = hint.lower()
    game_vals = utils.GameStatus(output_str="", incorrect_letters_threshold=9, \
                    prev_incorrect_letters=set(), first_iter=True, prev_guess="", \
                    name=name, hint=hint, win=False, got_hint=False)
    print("----------------Welcome to the Class Hangman Game----------------")
    print("---The theme of this game is the names of people in this class---")
    print("------Lets See How Well You Know the People in Our Class---------")
    print("---You have {} total incorrect letters that you can guess--------\n"\
                .format(game_vals.incorrect_letters_threshold))
    print("Phrase: {}".format(utils.hangman_display("", game_vals.name)[0]))
    # print("Testing Phrase: {}".format(game_vals.name)) # Will be removed after testing
    while game_vals.incorrect_letters_threshold > 0 and not game_vals.win:
        try:
            guess = raw_input("Enter your guess: \n").lower()
            if guess == "hint":
                print("You are requesting a hint!")
                print("Please note that by doing this you must guess the name immediately, without any mistakes")
                get_hint = raw_input("Are you sure you want the hint?\n")
                if get_hint in ["y", "yes"]:
                    print("Your Hint is: {}".format(game_vals.hint))
                    print("You now must guess the name without mistakes!")
                    game_vals.incorrect_letters_threshold = 1
                    game_vals.got_hint = True
            else:
                print("Calculating Results:\n")
                time.sleep(0.5)
                game_vals.output_str, correct_guess = utils.hangman_display(guess+game_vals.prev_guess, game_vals.name)
                game_vals.prev_guess += correct_guess
                game_vals.incorrect_letters_threshold -= utils.return_incorrect_letters(guess, game_vals.name, \
                                                game_vals.prev_incorrect_letters)
                if game_vals.output_str != game_vals.name or game_vals.incorrect_letters_threshold<1:
                    if not game_vals.first_iter:
                        already_guessed = set(filter(lambda char: char in game_vals.prev_incorrect_letters, \
                                            guess))
                        if len(already_guessed) != 0:
                            print("You have already guessed {}!".format(\
                                    ", ".join(already_guessed)))
                    game_vals.prev_incorrect_letters.update(guess)
                    # print("You have {} more incorrect letters".format(\
                    #             max(game_vals.incorrect_letters_threshold, 0)))
                    print(utils.hangman_ascii[max(game_vals.incorrect_letters_threshold-1, 0)])
                    print(game_vals.output_str)
                else:
                    print("You won!")
                    if game_vals.incorrect_letters_threshold > 7:
                        print("Wow, you are a master at the names in this class!")
                    elif 7 > game_vals.incorrect_letters_threshold > 4 or game_vals.got_hint:
                        print("You are pretty good at names in this class!")
                    elif 4 > game_vals.incorrect_letters_threshold > 2:
                        print("Dang, you must be having a really bad day! You barely guessed {}'s \
                        name!".format(game_vals.name))
                    else:
                        print("Wow, you really suck at names, find a new class!")
                    print("The phrase was {}".format(game_vals.name))
                    game_vals.win = True
                if game_vals.first_iter:
                    game_vals.first_iter = False
        except KeyboardInterrupt:
            print("\nYou exited the game")
            break
        sys.stdout.flush()
    else:
        if not game_vals.win:
            _, letters_right = utils.hangman_display(game_vals.name, game_vals.output_str)
            if game_vals.name == game_vals.output_str:
                print("Sorry, you got the right answer but guessed too many incorrect letters")
                print("The message was {}".format(game_vals.name))
            else:
                print(utils.hangman_ascii[0])
                print("Sorry, you ran out of tries\n")
                print("The message was {}".format(game_vals.name))
                print("You needed the letters {} to win".format(", ".join(set(filter(lambda \
                                            char: char not in letters_right, game_vals.name)))))
            print("\n\n")
        try:
            replay = raw_input("Do you want to play again?\n").lower()
            if replay.lower() in ["yes", "y"]:
                hangman()
        except KeyboardInterrupt:
            print("\nYou exited the game")
hangman()