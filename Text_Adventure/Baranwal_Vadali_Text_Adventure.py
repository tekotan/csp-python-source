""" Text Adventure """
from __future__ import print_function
import time
import sys
import random

def play_story():
    """
    Function that will package the complete story
    """ 

    def question_1():
        """
        Function will package question 1 and will allow it to be called multiple 
        times
        """
        response = raw_input("Do you want the instructions? (Yes/No) \n").lower()
        if response == "yes":
            print("Great, This game is based on the responses you input. \
                    Please write your answer the same way that it is written on the \
                    question. However, captalization does not matter")
        elif response == "no":
            print("Ok, exiting!")
            sys.exit()
        else:
            print("Please enter either a Yes or a No")
            question_1()
    
    
    def question_2():
        """
        Function will package question 2 and hold all the story line and question
        for the game, also allowing it to be called if needed
        """
        time.sleep(2)
        print("\nNEWS REPORT: Two Kids are missing Baltic forest. With the \
            canabalistic witch lurking around, the only thing that we can do for \
            the kids is pray. They are a brother and sister, calling by the names \
            Hansel and Gretel!")
        response = raw_input("Do you want to be Hansel or Gretel? \n").lower()
        if response == "hansel":
            print("Welcome Hansel! \n")
            name = "Hansel"
        elif response == "gretel":
            print("Ok, you are Gretel \n")
            name = "Gretal"
        else:
            print("Please enter a name \n")
            question_2()
    
    
    def question_3():
        """
        Function holds and packages question 3 in order to be called when needed
        using raw_input and if then statments
        """
        response = raw_input("We need to leave this forest. How do you think we will\
            leave it. I don't know if I should go  \nStraight \nLeft \nRight\
            \n").lower()
        if response == "straight":
            print("You walked straight:")
            time.sleep(1)
            print("Look! There is a dragon, we need to ru..")
            time.sleep(1)
            print("The dragon had dinner today!")
            leave = raw_input("Do you want to leave? (Yes/No) \n")
            if leave == "yes":
                print ("Thank you for being the dragons lunch today")
                sys.exit()
            else:
                print("Restarting the game! \n")
                play_story()
        elif response == "left":
            print("You walked left:")
            time.sleep(1)
            print("where are we, it looks dark. Help us! Help ... (Crack)")
            time.sleep(1)
            print("The siblings were never seen again")
            leave = raw_input("Do you want to leave? (Yes/No) \n")
            if leave in yes:
                print ("Thank you for being the dragons lunch today")
                sys.exit()
            else:
                print("Restarting the game! \n")
                play_story()
        elif response == "right":
            print("You walked right:")
            time.sleep(1)
            print("Look! A candy house is up yonder. Let us see if we can get some \
                food! Should we go? \n")
        else:
            print("Please enter a direction")
            question_3()
    
    
    def question_4():
        """
        Function packages code for question 4 in order to it to be called and 
        hold the raw_inputs and responses of the game
        """
        response = raw_input("Do you want to go to the candy house (Yes/No) \
                            \n").lower()
        if response == "yes":
            print("Great, lets go to the candy house")
            time.sleep(1)
        elif response == "no":
            leave = raw_input("Do you want to leave? (Yes/No) \n").lower()
            print("But, we won't have shelter. Okay, fine!")
            time.sleep(1)
            print("A few months later...")
            time.sleep(2)
            print("Hansel! Brother Hansel! Wake up! We need to get food! Brother\
                get up. Brother, brother!!")
            time.sleep(1)
            if leave != "no":
                print("I need to leave this place! Help me! Help me!")
                time.sleep(1)
                sys.exit()
            else:
                print("Okay. Look, there is a time machine. I must go back in \
                        time to help save my brother! I hope it works! I\'m \
                        coming brotherrrr!")
                question_4()
        else:
            print("Please enter either a Yes or a No")
            question_4()
    
    
    def question_5():
        """
        Function holds and packages code of question 5 that holds the code and 
        story using raw_inputs, if then statments and using a variable response
        """
        print("I am hungry, can we have some candy. I believe that we need \
            food! \n")
        response = raw_input("Do you want to eat the candy? (Yes/No) \n").lower()
        if response == "yes":
            print("Great, lets have some candy!")
            return False
        elif response in no:
            leave = raw_input("Do you want to leave? (Yes/No) \n")
            if leave != "No":
                print("I do not believe that eating is the good answer. I say \
                    that we leave this tisby land and find our way home. ")
                time.sleep(1)
                sys.exit()
            else:
                print("Okay...")
                question_5()
        else:
            print("Please enter either a Yes or a No")
            question_5()
    
    
    def question_6():
        """
        Function holds the code and packages it since it is using print, if then 
        statements and also raw_imputs, creating leave and response variables
        """
        print(" \nWe ate too much candy. I can't move. \n")
        time.sleep(1)
        print("Enter the witch \n")
        time.sleep(0.5)
        print("Welcome children! Are you enjoying my house. Wuah Wuah Wuah!")
        time.sleep(0.5)
        print("Someone help us! Gretel run for your life!")
        time.sleep(0.5)
        print("Witch: I can\'t let that happen")
        time.sleep(1)
        print("Gretel, save me! The witch captured me!")
        if name == "Hansel":
            print("You were locked up in the dungeon, getting ready to be eaten")
        else:
            response = raw_input("Do you want to save Hansel!? \n").lower()
            if response == "yes":
                print("You are a valued girl. Worthy to be a knight! Go quick! \n")
                time.sleep(1)
                print("Gretel ran back into the house, ready for the battle! \n")
            elif response == "no":
                print("You ran away from the house, leaving your brother behind \
                        and allowing him to burn alive \n")
                sys.exit()
            else:
                print("You didn't answer in time, killing your brother!")
                sys.exit()

    def question_7():
        """
        Function packages the code of question 7 in order for it to be called by
        and uses the variable name and it will create different situations based 
        on the character
        """
        response = raw_input("Do you want to talk to the witch \n").lower()
        if name == "Hansel":
            if response == "yes":
                print("Ms.Witch, please don't eat me. I am small and scrawny, \
                    weak and bony, not got enough for you to eat. Give me a chance \
                    to survive, or I will be your feast.")
                time.sleep(0, 7)
                print("Little boy, I will give you a chance to survive if you \
                    answer a riddle, do you wan to do it""")
            elif response == "no":
                print("Why don't you want to talk to me! Well, you won't be able \
                to talk soon. Bye, bye boy! ")
                sys.exit()
            else:
                print("Boy! You have no options. You will die in my pot. You will \
                    be a great pie for me. ")
                sys.exit()
        else:
            if response == "yes":
                print("Ms.Witch, please don't eat my brother. He is small and \
                    scrawny, weak and bony, not got enough for you to eat. \
                    Give him a chance to survive, or we will be your feast.")
                time.sleep(0, 7)
                print("Little girl, I will give you a chance to survive if you \
                    answer a riddle, do you wan to do it")
            elif response == "no":
                print("You enter the room:")
                time.sleep(1)
                print("You came to the oven, seeing Hansel \n \
                    \"I\'m here brother! I here to save you\" \n")
                time.sleep(0.7)
                print("The witch saw you! \n \" Why hello girl! You can also be a \
                    beautiful pie. Be with your brother!\" ")
                time.sleep(0.7)
                print("You looks at Hansel, but the witch swiftly goes and captured \
                    you. You joined Hansel in the pot. You plan FAILED ")
            else:
                print("You were thinking too long, letting the Witch boil Hansel!")
    
    
    def question_8():
        """
        Function holds and packages code of the riddle in order to create the 
        ending of the game using the riddle answers. This is using a raw_input 
        and having multiple riddles
        """
        print("Here is the riddle: \n")
        riddle_1 = "My first is often at the front door. \n \
                My second is found in the cereal family. \n \
                My third is what most people want. \n \
                My whole is one of the United States. \n"
        riddle_2 = "My life can be measured in hours, \n \
                    I serve by being devoured. \n \
                    Thin, I am quick \n \
                    Fat, I am slow \n \
                    Wind is my foe."
        riddle_3 = "It is greater than God and more evil than the devil. \
                    The poor have it, the rich need it and if you eat it you’ll \
                    die. What is it?"
        riddle_4 = "What always runs but never walks, often murmurs, never \
                    talks, has a bed but never sleeps, has a mouth but never eats?"
        riddle_5 = "What begins and has no end? What is the ending of all that \
                    begins?"
        riddle_list = [riddle_1, riddle_2, riddle_3, riddle_4, riddle_5]
        riddle_ans = ["matrimony", "candle" , "nothing" , "river", "death"]
        riddle = random.choice(riddle_list)
        riddle_num = riddle_list.index(riddle)
        print(riddle)
        response = raw_input("Answer:         ").lower()
        
        if response == riddle_ans[riddle_num]:
            print("Congratulation! You got the right answer! However, I \
                        am going to eat you! You kids will be stuck here forever.\
                        You will never win. That is why I am a bad witch! ")
            print("Crash! The door breaks! Comes in is a voracious dragon. \
                        Fire coming everywhere. It came to save you, since you \
                        didn't wake it up when it was sleeping in his cave!")
            sys.exit()
        else:
            print("Sorry! That is Wrong. Bye, Bye!!!!")
            sys.exit()

    print("It wasn't a dark and stormy night, but a nice and beautiful day. \
        Two kids are walking with their father, walking into the woods. \
        But then, due to their idiotic father, they got lost in the forest by \
        themselves. Scared, they need your help!! \n")
    time.sleep(2)
    print("This is created by Sragvi Vadali and Tanish Baranwal \n")
    name = ""
    question_1()
    question_2()
    question_3()
    question_4()
    question_5()
    question_6()
    question_7()
    question_8()

play_story()