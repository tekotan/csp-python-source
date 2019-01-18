from __future__ import print_function

""" 1.3.7 """
# 4:
def days():
    ''' This function will print the days of the week then print the 5th, 6th and 
        7th day of September
    '''
    for day in 'MTWRFSS': 
        print(day + 'day')
    for day in range(5,8):
        print('It is the ' + str(day) + 'th of September')
# 5:


import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import random

def picks():
    a = [] # make an empty list
    # Why all the brackets below? 
    # a += [  brackets here to add an iterable onto a list]
    #    random.choice(   [brackets here to choose from a list])

    a += [random.choice([1, 3, 10])]
    for choices in range(5):
        a += [random.choice([1, 3, 10])]

    plt.hist(a)
    plt.savefig('./picks')

# 6a:

def roll_hundred_pair():
    """ Creates a histogram on 100 rolls of a dice """
    rolls = []
    for roll in range(100):
        rolls.append(random.randint(1,6))
    plt.hist(rolls)
    plt.savefig('./roll_hundred_pair')

# 6b:

def dice(num_rolls):
    """ 
    Rolls a dice n number of times 
    
    args:
        num_rolls: Number of times to roll dice
    returns: sum of dice rolls
    """
    total_roll = 0
    for roll in num_rolls:
        total_roll += random.randint(1,6)
    print("Roll was {}".format(total_roll))

# 7
def validate():
    guess = '1' # initialization with a bad guess
    answer = 'hangman word'
    while guess not in answer:
        guess = raw_input('Name a letter in \''+answer+'\': ')
    print('Thank you!')

# Ans: Line 2 is nessessary because if the guess was initialized as a 0, then 
# the while loop will never start because the contition is false already. A more 
# reliable way to do this is to initialize guess as an empty string

import random

def guess_winner(players=('Amy', 'Bill', 'Cathy', 'Dale')):
    '''Summarize the function in this docstring.
    
    Provide descriptions for the arguments and say what type each one is.
    Describe the type and meaning of the value returned.
    '''
    winner = random.choice(players) 

    ####
    # This section prints out all of the players playing the lottery
    ####
    print('Guess which of these people won the lottery: ',end='')
    for p in players[:len(players)-1]:# index will choose all players except for the last one
        print(p+', ', end='')
    print(players[len(players)-1]) # this prints the last player

    ####
    # This section of code handles the user guessing the player that won
    ####
    guesses = 1 
    while raw_input() != winner:
        print('Guess again!')
        guesses += 1
    print('You guessed in', guesses, 'guesses!')
    return guesses

# 9:

def goguess():
    """
    Function that handles a guessing game with numbers
    """
    number = random.randint(1, 20)
    guess = ""
    num_guesses = 0
    while guess != number:
        guess = int(raw_input("I Have a number between 1 and 20 inclusive \n Guess : "))
        if guess > number:
            print("{} is too high".format(guess))
        else:
            print("{} is too low".format(guess))
        num_guesses += 1
    print("Right! My Number is {}! You guessed in {} guesses!".format(number, num_guesses))
#10: if the number was changed to 1 to 6000, one would need 6000 guesses to be sure.

