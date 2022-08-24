import random

# def easy_mode():
#     num = random.randrange(1,100)
#     attempts = 10
#     while attempts != 0:
#         print(num)
#         print(f"You have {attempts} attempts remaining to guess the number correctly")
#         guess = int(input("Make a guess: "))
#         if guess < num:
#             print("Your guess was to low")
#             attempts -= 1
#         elif guess > num:
#             print("Your guess was to high")
#             attempts -= 1
#         elif guess == num:
#             print("Well done! You guessed correctly, now try 'hard' mode!")
#             exit()
#         else:
#             print("Your guess was not a number! Try again!")


# def hard_mode():
#     num = random.randrange(1,100)
#     attempts = 5
#     while attempts != 0:
#         print(num)
#         print(f"You have {attempts} attempts remaining to guess the number correctly")
#         guess = int(input("Make a guess: "))
#         if guess < num:
#             print("Your guess was to low")
#             attempts -= 1
#         elif guess > num:
#             print("Your guess was to high")
#             attempts -= 1
#         elif guess == num:
#             print("Well done! You guessed correctly! Ultra Extreme Hard Mode coming soon!"")
#             exit()
#         else:
#             print("Your guess was not a number! Try again!")



print("Welcome to The Number Guess Game!")

print("I am currently thinking of a number between 1 - 100")

difficulty = input("Please choose difficulty! Type 'easy' or 'hard': ")

if difficulty == "easy":
    attempts = 10
elif difficulty == "hard":
    attempts = 5

num = random.randrange(1,100)

while attempts != 0:
    print(num)
    print(f"You have {attempts} attempts remaining to guess the number correctly")
    guess = int(input("Make a guess: "))
    if guess < num:
        print("Your guess was to low")
        attempts -= 1
    elif guess > num:
        print("Your guess was to high")
        attempts -= 1
    elif guess == num:
        print("Well done! You guessed correctly!")
        exit()
    else:
        print("Your guess was not a number! Try again!")






# if difficulty.lower() == "easy":
#     easy_mode()
# elif difficulty.lower() == "hard":
#     hard_mode()