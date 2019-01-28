"""
Module that holds all answers and hidden variables
"""

secret_list = [
    "hello world",
    "home",
    "CSP projects are fun",
]
hangman_ascii = [
"""
   ____
  |    |      Phrase #:    {phrase_num}
  |    o      Guessed : {guessed_letters}
  |   /|\     Average :  {avg_}%
  |    |
  |   / \
 _|_
|   |______
|          |
|__________|
 
Theme  : {theme}
Phrase: {phrase}
""",
"""
   ____
  |    |      Phrase #:    {phrase_num}
  |    o      Guessed : {guessed_letters}
  |   /|\     Average :  {avg_}%
  |    |
  |   / 
 _|_
|   |______
|          |
|__________|
 
Theme  : {theme}
Phrase: {phrase}
""",
"""
   ____
  |    |      Phrase #:    {phrase_num}
  |    o      Guessed : {guessed_letters}
  |   /|\     Average :  {avg_}%
  |    |
  |   
 _|_
|   |______
|          |
|__________|
 
Theme  : {theme}
Phrase: {phrase}
""",
"""
   ____
  |    |      Phrase #:    {phrase_num}
  |    o      Guessed : {guessed_letters}
  |   /|\     Average :  {avg_}%
  |    
  |   
 _|_
|   |______
|          |
|__________|
 
Theme  : {theme}
Phrase: {phrase}
""",
"""
   ____
  |    |      Phrase #:    {phrase_num}
  |    o      Guessed : {guessed_letters}
  |   /|      Average :  {avg_}%
  |    
  |   
 _|_
|   |______
|          |
|__________|
 
Theme  : {theme}
Phrase: {phrase}
""",
"""
   ____
  |    |      Phrase #:    {phrase_num}
  |    o      Guessed : {guessed_letters}
  |   /       Average :  {avg_}%
  |    
  |   
 _|_
|   |______
|          |
|__________|
 
Theme  : {theme}
Phrase: {phrase}
""",
"""
   ____
  |    |      Phrase #:    {phrase_num}
  |    o      Guessed : {guessed_letters}
  |           Average :  {avg_}%
  |    
  |   
 _|_
|   |______
|          |
|__________|
 
Theme  : {theme}
Phrase: {phrase}
""",
"""
   ____
  |    |      Phrase #:    {phrase_num}
  |           Guessed : {guessed_letters}
  |           Average :  {avg_}%
  |    
  |   
 _|_
|   |______
|          |
|__________|
 
Theme  : {theme}
Phrase: {phrase}
""",
"""
   ____
  |           Phrase #:    {phrase_num}
  |           Guessed : {guessed_letters}
  |           Average :  {avg_}%
  |    
  |   
 _|_
|   |______
|          |
|__________|
 
Theme  : {theme}
Phrase: {phrase}
""",
]