from random import randint

number = randint(1, 10)

while True:
    guess = input("Guess a number between 1 and 10: ")
    guess = int(guess)
    if guess > number:
        print("Too high, try again!")
    elif guess < number:
        print("Too low, try again!")
    else:
        print("YOU WON!")
        keep_playing = input("Do you want to keep playing?(y/n) ")
        if keep_playing == "y":
            number = randint(1, 10)
            guess = None
        else:
            print("Thanks for a game")
            break
