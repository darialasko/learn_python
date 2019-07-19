from random import randint

#player1 = input("What is your choice? ")
#player2 = input("What is your choice? ")
# if player1 and player2:
#    rock = "rock"
#    paper = "paper"
#    scissors = "scissors"
#    if player1 == rock and player2 == paper or player1 == scissors and player2 == rock or player1 == paper and player2 == scissors:
#        print("player2 wins")
#    elif player2 == rock and player1 == paper or player2 == scissors and player1 == rock or player2 == paper and player1 == scissors:
#        print("player1 wins")
#    else:
#        print("tie")
# else:
#    print("Something went wrong")


player_wins = 0
computer_wins = 0
winning_score = 4

while computer_wins < winning_score and player_wins < winning_score:

    print(f"Your score: {player_wins}  Computer score: {computer_wins}")
    print("...rock...\n...paper...\n...scissors...")

    p1 = input("Make your choice: ").lower()
    if p1 == "quit" or p1 == "q":
        break
    rand_num = randint(0, 2)
    if (rand_num == 0):
        p2 = "rock"
    elif (rand_num == 1):
        p2 = "paper"
    else:
        p2 = "scissors"
    print(f"The computer plays: {p2}")

    if p1 == p2:
        print("Its a tie!")
    elif p1 == "rock":
        if p2 == "paper":
            print("Computer has point!")
            computer_wins += 1
        else:
            print("You have a point!")
            player_wins += 1
    elif p1 == "paper":
        if computer_wins == "scissors":
            print("Computer has point!")
            computer_wins += 1
        else:
            print("You have a point!")
            player_wins += 1
    elif (p1 == "scissors"):
        if (computer_wins == "rock"):
            print("Computer has point!")
            computer_wins += 1
        else:
            print("You have a point!")
            player_wins += 1
    else:
        print("Please enter the valid move")

if player_wins > computer_wins:
    print("Congratulations!")
elif player_wins == computer_wins:
    print("Its a tie")
else:
    print("Computer wins!")

print(f"Final score: you: {player_wins}  computer: {computer_wins}")
