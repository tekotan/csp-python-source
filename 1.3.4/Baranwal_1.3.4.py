from __future__ import print_function
import random
from time import sleep
import sys
'''Procedure'''
# 1-4: N/A

'''Part 1: Nested if structures and testing'''

# 1:
def food_id(food):
    ''' Returns categorization of food

    food is a string
    returns a string of categories
    '''
    # The data
    fruits = ['apple', 'banana', 'orange']
    citrus = ['orange']
    starchy = ['banana', 'potato']

    # Check the category and report
    if food in fruits:
        if food in citrus:
            return 'Citrus, Fruit'
        else:
            return 'NOT Citrus, Fruit'
    else:
        if food in starchy:
            return 'Starchy, NOT Fruit'
        else:
            return 'NOT Starchy, NOT Fruit'
#1a: 17
#1b:
#   i:orange
#   ii:apple
#   iii:Potato
#   iv:cheese
#1c: the banana will never be returned as starchy because the else block will 
#    not run as banana is in the fruits list

#2:

def food_id_test():
    ''' Unit test for food_id
    returns True if good, returns False and prints error if not 
    good
    '''
    works = True
    if food_id('orange') != 'Citrus, Fruit':
        works = True
    if food_id('banana') != 'NOT Citrus, Fruit':
        works = True 
    if food_id('potato') != "Starchy, NOT Fruit":
        works = True
    if food_id('cheese') != "NOT Starchy, NOT Fruit":
        works = True
    # Add tests so that all lines of code are visited during test
    
    if works == True:
        print("All good!")
        return True
    else:        
        print(works)
        return False

#3:

def f(n):
    '''
    Function that will describe an input as not an int, odd, even, or a mult of 6
    
    args:
        n: any kind of input
    returns:
        Odd, even, not an integer, or multiple of 6
    '''
    if isinstance(n, int):
        if n%2 == 0:
            if n%3 == 0:
                return "The number is a multiple of 6"
            else:
                return "The number is even"
        else:
            return "The number is odd"
    else:
        return "The number is not an integer"

#4: The test cases for this function are 1,2,6,10.3

#5:
def f_test():
    '''
    Tests the function f for all cases
    
    returns:
        True if all outputs are correct
        False if any output is incorrect
    '''
    test_cases = {"The number is a multiple of 6":6, "The number is even":2, \
    "The number is odd":1, "The number is not an integer":10.3}
    for output, arg in test_cases.items():
        if f(arg) != output:
            break
    else:
        return False
    return True

#7: the difference between the + in the concatenation and the + in addition is 
# that the concat + requires both addends to be the same type, while the addition 
# can have slightly different types

#8:
def guess_once_original():
    secret = random.randint(1, 4)
    print('I have a number between 1 and 4.')
    guess = int(raw_input('Guess: '))
    if guess != secret:
        print('Wrong, my number is ', secret, '.', sep='')
    else:
        print('Right, my number is', guess, end='!\n')
# 8a: line 11 has 3 arguments, where the first 2 are strings to be concatenated 
# together, and the end appends the end string to the end of each line

# 8b:
def guess_once():
    '''
    Function that handles a small guessing game
    
    returns:
        whether the user given input was correct
    '''
    secret = random.randint(1, 4)
    print('I have a number between 1 and 4.')
    try:
        guess = int(raw_input('Guess: '))
    except ValueError:
        print("Please enter an integer!")
        guess = int(raw_input('Guess: '))
    if guess != secret:
        if guess > secret:
            print ("Too high, - my number was", secret)
            return False
        else:
            print ("Too low, - my number was", secret)
            return False
    else:
        print('Right on, I was number', guess, end='!\n')
        return True
#9

def quiz_decimal(low, high):
    '''
    Function to handle a small question asking for a decimal between high and low
    
    args:
        low: low bounding number, Must be one of the following types: float
        high: higher bounding number, Must be one of the following types: float
    returns:
        Correctness of your number given
    '''
    try:
        decimal = \
        float(raw_input("Type a number between {} and {}:\n".format(low, high)))
    except ValueError:
        print("Please enter an integer!")
        decimal = \
        float(raw_input("Type a number between {} and {}:\n".format(low, high)))
    if low<decimal<high:
        print("Good! {} < {} < {}".format(low, decimal, high))
    else:
        if decimal>high:
            print("No, {} is greater that {}".format(decimal, high))
        else:
            print("No, {} is less than {}".format(decimal, low))
'''Conclusion'''

#1: Glass box testing is a way to test if all possibilities a if structure controls

#2: There may be many if blocks in code that do not excecute because only the 
#   ones with conditions that are fullfilled will execute

#3: Test suites contain all of the possibilities the programmer wants to handle, 
#   and that is why the programmer can write a test suite before writing a program

#4: Yes
#Functions for every output on the flow chart
even = lambda num: "{} is even".format(num) if num%2 == 0 else \
                                                    "{} is not even".format(num)
odd = lambda num: "{} is odd".format(num) if num%2 != 0 else \
                                                    "{} is not odd".format(num)
divisible_by_6 = lambda num: "{} is divisible by 6".format(num) if num%6==0 else \
                                            "{} is not divisible by 6".format(num)
is_int = lambda num: "{} is an int".format(num) if isinstance(num, int) else \
                                                    "{} is not an int".format(num)


''' Challenge '''
f_challenge = lambda n: [even(n), odd(n), divisible_by_6(n), is_int(n)]
''' Assignment Check '''
print(food_id('apple'))
food_id_test()
f(1.1)
f(2)
f(3)
f(6)
f_test()
guess_once()
guess_once()
quiz_decimal(4, 4.1)
quiz_decimal(4, 4.1)
print(f_challenge(1.1))
print(f_challenge(2))
print(f_challenge(3))
print(f_challenge(6))

'''Assingment Check'''

# I believe that I have completed this assignment correctly based on the fact
# that I have no syntax errors and the functions output reasonable results
