"""
Module that holds all functions and hidden variables
"""
#####################################################################################
################# Classes and Functions for the Hangman Game ########################
#####################################################################################
class GameStatus(object):
    """
    Class that holds all game values for the course of a cycle of the hangman game

    """
    def __init__(self, **kwargs):
        """
        Function that initializes the class with attributes as the args
        args:
            Any and all values to store into the game_status object
        returns:
        None
        """
        for key, value in kwargs.items():
            if not hasattr(self, key):
                setattr(self, key, value)
                

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
#####################################################################################
########################### Lists with Words and Ascii ##############################
#####################################################################################
secret_dict = {
    "Sragvi":"Person in the Class that asks a lot of questions",
    "Vedant":"Person in the Class ",
    "Conner":"Calls Sragvi Shrugs",
    "Tanish":"Python Programmer",
    "Abhi":"Friends with Rohan",
    "Vincent":"A Senior",
    "Ryan":"Partner with Connor",
    "Rohan":"Friends with Abhi",
    "Andrea":"Likes Anime",
    "Riya":"Comes late to class",
    "Anurag":"Partners with Vedant",
    "Anika":"Partners with Andrea",
    "Diego":"Programs in Java",
    "Michael":"Asian",
}
hangman_ascii = [
"""
   ____
  |    |    
  |    o      
  |   /|\    
  |    |
  |    |
  |   / \    
 _|_         
|   |______
|          |
|__________|
""",
"""
   ____
  |    |  
  |    o   
  |   /|\ 
  |    |
  |    |
  |   / 
 _|_
|   |______
|          |
|__________|
""",
"""
   ____
  |    |   
  |    o   
  |   /|\  
  |    |
  |    |
  |   
 _|_
|   |______
|          |
|__________|
""",
"""
   ____
  |    |   
  |    o   
  |   /|\   
  |    |
  |   
 _|_
|   |______
|          |
|__________|
""",
"""
   ____
  |    |    
  |    o     
  |   /|\   
  |    
  |   
 _|_
|   |______
|          |
|__________|
""",
"""
   ____
  |    |    
  |    o     
  |   /|   
  |    
  |   
 _|_
|   |______
|          |
|__________|
""",
"""
   ____
  |    |  
  |    o   
  |   /    
  |    
  |   
 _|_
|   |______
|          |
|__________|
""",
"""
   ____
  |    |   
  |    o   
  |        
  |    
  |   
 _|_
|   |______
|          |
|__________|
""",
"""
   ____
  |    |  
  |     
  |       
  |           
  |           
 _|_          
|   |______
|          |
|__________|
""",
"""
   ____
  |         
  |         
  |       
  |    
  |   
 _|_
|   |______
|          |
|__________|
""",
]