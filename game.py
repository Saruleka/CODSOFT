import random
import time

def computer():
    options = ["rock", "paper", "scissors"]
    return random.choice(options)

def getting_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "tie"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        return "user"
    else:
        return "computer"

print("Rock, Paper, Scissors Game".center(100))
def play_game():
    user_score = 0
    computer_score = 0

    max_rounds = int(input("Enter the maximum number of rounds: "))

    for round_count in range(1, max_rounds + 1):
        try:
            user_choice = input(f"Round {round_count}/{max_rounds} - Choose rock, paper, or scissors: ").lower()
        except ValueError:
            print("Error!!Enter a Choice")

        while user_choice not in ["rock", "paper", "scissors"]:
            print("Invalid input. Please choose rock, paper, or scissors.")
            user_choice = input(f"Round {round_count}/{max_rounds} - Choose rock, paper, or scissors: ").lower()

        computer_choice = computer()
        print(f"Computer chose: {computer_choice}")

        winner = getting_winner(user_choice, computer_choice)

        time.sleep(0.1)

        if winner == "tie":
            print("It's a tie!")
        elif winner == "user":
            print("You win this round!")
            user_score += 1
        else:
            print("Computer wins this round!")
            computer_score += 1
        
        time.sleep(0.1)
        print(f"Score after round {round_count}\n".center(100))
        print(f"You : {user_score} \nComputer : {computer_score}")

    print("\nGame Over!".center(100))
    print(f"Final Score:\nYou : {user_score} \nComputer : {computer_score}\n")

    if user_score > computer_score:
        print("Congratulations, you are the winner!")
    elif computer_score > user_score:
        print("Computer wins! Better luck next time!")
    else:
        print("It's an overall tie!")

while True:
    play_game()
    replay = input("Do you want to play again? (yes/no): ").lower()
    if replay != "yes":
        break

print("Thanks for playing!")