""" 1.3.6 """
# 1-3: N/A
# 4:
("this", "is", "super", "boring")

# 5: A convention Mr. Brown requires is always writing docstrings for functions 
# and using comments to answer questions, and he has not specified any conventions

# 6a: Output will be "b", just like string indexing
# 6b: Output will be ("a", "b"), just like string slicing

# 7a: True, becuase tuple b will not be updated to use the change in a
# 7b: 15, because the tuple was reassigned values with a, so it reflects the change

# 8: The output will be ["b", 3], because slicing is the same with lists as well

# 9: False, because the value is no ling the int 3, but the str 3 with is not equal.

# 10a: ["a", "b", "3", 4, 5], because the list was concantenated to values
# 10b: ["a", "b", "3", [4, 5]], because the ilist was appended to the end of values

# 11: The data types are different for the addition

# 12: This will return 18, because it will multiply a by 3 then set a to the result

# 13: N/A

# 14:
from random import randint

roll_two_dice = lambda: randint(1,6)+randint(1,6)

""" Conclusion """

# 1: a, b, and c are strings, tuples and lists respectively, each a completely 
# different data type with unique system representations and methods

# 2: Everything cannot be represented as an int because they do not have the 
# properties of an integer and must be encoded in different ways

""" 
Summary (Question 3)

Python functions can be used to package code for use later on. They can take 
arguments and return values. Python programmers can utilize stdin and stdout 
to write interactive and comprehensive programs that allow the user to understand 
what is happening. Python has 5 major data types, str, int, float, tuple, list, 
and dict, each with a different representation as bits, and each with unique 
methods and functions that can be used to manipulate them.
"""

#1.3.6 Function Test
print(roll_two_dice())