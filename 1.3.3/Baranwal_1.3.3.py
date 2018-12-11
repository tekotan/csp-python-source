from __future__ import print_function
'''Procedure '''
#1-5: N/a

'''Part 1: Conditionals'''

# 6a. Prediction: True
#     My prediction was correct

# 6b: Prediction: True
#     My prediction was correct

# 7:
x, y = (65, 40)
x>40 and x <130 and y>100 and y<120

'''Part 2: if-else structure in print() function'''
#9a Prediction: 
def age_limit_output(age):
    '''Step 9a if-else example'''
    AGE_LIMIT = 13          # convention: use CAPS for constants
    if age < AGE_LIMIT:
        print(age, 'is below the age limit.')
    else:
        print(age, 'is old enough.')
    print(' Minimum age is ', AGE_LIMIT) 

#       Line 1: 10 is below the age limit, because 10 is less than 13
#       Line 2: 16 is old enough, because 16 is above 13.

#9b:

def report_grade(percent):
    '''This funtion will determine whether a percent grade shows mastery
        args: 
            percent: grade percent of your grade
        returns:
            Whether a grade shows mastery
        raises:
            TypeError: Raises error if percent arg is not given
    '''
    if percent > 80:
        print("A grade of {} percent indicates mastery\nKeep up the good work!".format(percent))
    else: 
        print("A grade of {} percent does not indicate mastery\nSeek extra practice or help.".format(percent))

'''Part 3: the in operator'''

# 10:
#   Predictions:
#       True
#       False

#11
def letter_in_word(guess, word):
    '''
    Function to check if a letter is in the word word
        args:
            color: letter to check
            secret: string from which to check
        returns:
            Boolean
    '''
    if guess in word:
        return True
    else:
        return False
# 12
def hint(color, secret):
    '''
    Function to check if a color is in the list secret
        args:
            color: color to check
            secret: list of colors from which to check
        returns:
            The color {color} IS in the secret sequence of colors. OR
            The color {color} IS NOT in the secret sequence of colors.
    '''
    if color in secret:
        print("The color {} IS in the secret sequence of colors.".format(color))
    else:
        print("The color {} IS NOT in the secret sequence of colors.".format(color))

'''Conclusion'''
# 1:
#   The indented lines of code after the if, else, or elif blocks indicate the code to run if the conditional is True, or for the else if no conditional is true

# 2:
#   The boolean operators I have learned are ==, <=, >=, and some others are !=, <, and >.

# 3:
'''
Ira: Her first statement is correct, because if else blocks should only contain 
unique commands, but her second statement is incorrect because only one of the 
blocks will run due to the conditional

Jayla: Her first statement is correct, because if else blocks should only contain 
unique commands, and her second statement is also correct for the fact that the 
command is redundant when it needs to be changed

Kendra: Her first statement is correct, because if else blocks should only contain 
unique commands, but her second statment is a very precise due to the fact that 
one extra line of code makes nearly no difference in file size
'''

# Assignment Check


#1.3.3 Function Test
age_limit_output(10)
age_limit_output(16)
report_grade(79)
report_grade(85)
print(letter_in_word('t', 'secret hangman phrase'))
secret = ['red','red','yellow','yellow','black']
hint('red', secret)
hint('green', secret)

# Reflection: Based on the output I feel that I have completed this assignment 
# correctly based on the fact that there was no syntax error and the output matches the answers in the document