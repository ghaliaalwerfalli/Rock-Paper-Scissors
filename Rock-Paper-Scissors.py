## BUG : if player's input any number other than 0,1,2 the game wont exit OR wont show invalid input and prompts asking user's input again

import random
import time

## importing random so computer can choose in range of 0 to 2, each belong to rock,paper and scissors variables
## import time to give the player time to read the text before a new round starts


still_working = True  ### Flag for while loop
while still_working:  ### while TRUE

    rock = '''
        _______
    ---'   ____)
          (_____)
          (_____)
          (____)
    ---.__(___)
    '''

    paper = '''
        _______
    ---'   ____)____
              ______)
              _______)
             _______)
    ---.__________)
    '''

    scissors = '''
        _______
    ---'   ____)____
              ______)
           __________)
          (____)
    ---.__(___)
    '''
    
    ### Above are ASCII art making the script game a bit interactive and each art is stored to a relatable variable
    
    print("")
    print("Welcome to a game of Rock Paper Scissors against a computer.\n")
    user = int(input("Choose a selection:\nType 0 rock, 1 paper and 2 scissors.\nYour choice is: "))
    ### This section assigns user's input to one variable between 3 choices
    ### Player makes their choice:
    if user == 0:
        print(rock)
    elif user == 1:
        print(paper)
    elif user == 2:
        print(scissors)
    else:
        ("You typed an invalid number. You lose!")

    ### Prompts computers choice using random.randint(0,2) and assigns the random choice to one variable of 3 choices
    print("Computer's choice is: ")
    comp = random.randint(0,2)
    if comp == 0:
        print(rock)
    elif comp == 1:
        print(paper)
    elif comp == 2:
        print(scissors)

    ## After player and computer chooses, a comparision between choices happen here:
    if user == 0:
        if comp == 0:
            print("It is a draw")
        elif comp == 1:
            print("You lose!")
        elif comp == 2:
            print("You win!")
    elif user == 1:
        if comp == 0:
            print("You win!")
        elif comp == 1:
            print("It is a draw")
        elif comp == 2:
            print("You lose!")
    elif user == 2:
        if comp == 0:
            print("You lose!")
        elif comp == 1:
            print("You win!")
        elif comp == 2:
            print("It is a draw")
    else:
      ("You typed an invalid number. You lose!")
    
    
    user_continue = input("Do you wish to continue playing? [Y/n]: ").lower()
    if user_continue == 'y':
        still_working = True
        print("")
        print("starting over in 2 seconds...")
        time.sleep(2)
    else:
        print("Thank you for playing :)")
        still_working = False

 



