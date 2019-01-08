""" 1.3.5 """

# 1-4: N/A
slogan = 'My school is the best'
# 5:
#str
#'My school is the best'

# int can represent the number 6 mill

# 6: The first line works because concatenation can only work with iterables of 
# same type, and the second line is attempting to concat an int and a str.

# 7:
# 'h' is the 7th to last character

# This indexing works just like lists where the index starts at 0, negative 
# indicies start with -1

# 8:
#'hool is the best'
# 8: Slicing
slogan[17:]

#9:
slogan[:13] + "really fun"
# [Out]: 'My school is really fun'

# 10a: out is 7 because len counts all of the characters in the string
# 10b: out is theate because in slicing the end number is exclusive, so the last
# character will not be included in the print

# 11: since 'test goo' is in the string in that specific order, it returns True

# 12:

def how_eligible(essay):
    """
    Function that checks the eligibility of a string by checking if it has a 
    question, a quote, a compound sentence, and an exclamation with marks of 
    '?', '"', ',', and '!', respectively
    
    args:
        essay: string from which the function checks the punctuation in
    returns:
        the eligibility from 1 to 4
    """
    eligibility_requirements = ['?', '"', ',', '!']
    return len(set(filter((lambda x: x in eligibility_requirements), essay)))
    
""" Assignment Check """
print(how_eligible('This? "Yes." No, not really!'))
print(how_eligible('Really, not a compound sentence.'))
