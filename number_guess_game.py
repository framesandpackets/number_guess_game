import random

#ASCII ART GENERATED AT: https://fsymbols.com/generators/carty/

banner = """ 

░█████╗░██╗░░░░░██╗    ███╗░░██╗██╗░░░██╗███╗░░░███╗██████╗░███████╗██████╗░
██╔══██╗██║░░░░░██║    ████╗░██║██║░░░██║████╗░████║██╔══██╗██╔════╝██╔══██╗
██║░░╚═╝██║░░░░░██║    ██╔██╗██║██║░░░██║██╔████╔██║██████╦╝█████╗░░██████╔╝
██║░░██╗██║░░░░░██║    ██║╚████║██║░░░██║██║╚██╔╝██║██╔══██╗██╔══╝░░██╔══██╗
╚█████╔╝███████╗██║    ██║░╚███║╚██████╔╝██║░╚═╝░██║██████╦╝███████╗██║░░██║
░╚════╝░╚══════╝╚═╝    ╚═╝░░╚══╝░╚═════╝░╚═╝░░░░░╚═╝╚═════╝░╚══════╝╚═╝░░╚═╝

░██████╗░██╗░░░██╗███████╗░██████╗░██████╗  ░██████╗░░█████╗░███╗░░░███╗███████╗██╗
██╔════╝░██║░░░██║██╔════╝██╔════╝██╔════╝  ██╔════╝░██╔══██╗████╗░████║██╔════╝██║
██║░░██╗░██║░░░██║█████╗░░╚█████╗░╚█████╗░  ██║░░██╗░███████║██╔████╔██║█████╗░░██║
██║░░╚██╗██║░░░██║██╔══╝░░░╚═══██╗░╚═══██╗  ██║░░╚██╗██╔══██║██║╚██╔╝██║██╔══╝░░╚═╝
╚██████╔╝╚██████╔╝███████╗██████╔╝██████╔╝  ╚██████╔╝██║░░██║██║░╚═╝░██║███████╗██╗
░╚═════╝░░╚═════╝░╚══════╝╚═════╝░╚═════╝░  ░╚═════╝░╚═╝░░╚═╝╚═╝░░░░░╚═╝╚══════╝╚═╝

"""

#CHANCES PLATER GETS IN EASY MODE:
EASY_ATTEMPTS = 10

#CHANCES PLATER GETS IN EASY MODE:
HARD_ATTEMPTS = 5

#FUNCTION THAT CHECKS HOW MANY ATTEMPTS TO ASSIGN TO THE USER
def difficulty_check():
    difficulty = input("\nPlease choose difficulty! Type 'easy' or 'hard': ")
    if difficulty.lower() == "easy":
        return EASY_ATTEMPTS
    elif difficulty.lower() == "hard":
        return HARD_ATTEMPTS


#MAIN GAME FUNCTION
def number_game():

    print(banner)

    print("Hello, I'm thinking of a number between 1 - 100!")

    #ASSIGNING ATTEMPTS TO USER
    attempts = difficulty_check()

    #GENERATING NUMBER BETWEEN 1- 100
    num = random.randrange(1,100)


    #### THIS NEEDS A LITTLE MORE WORK AND CLEAN UP! ####
    while attempts != 0:
        #DEBUG: LETS YOU SEE THE RANDOMLY GENERATED NUMBER
        # print(num)    
        print(f"You have {attempts} attempts remaining to guess the number correctly")
        guess = int(input("Make a guess: "))
        if guess < num:
            print("Your guess was to low")
            attempts -= 1
        elif guess > num:
            print("Your guess was to high")
            attempts -= 1
        elif guess == num:
            print(f"Well done! The number was {num}, You guessed correctly!")
            exit()
        else:
            print("Your guess was not a number! Try again!")

number_game()

