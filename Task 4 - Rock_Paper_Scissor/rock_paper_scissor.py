import random

choices = ["rock", "paper", "scissors"]

user_score = 0
computer_score = 0
round_number = 1

def get_computer_choice():
    return random.choice(choices)

def get_user_choice():
    while True:
        user_input = input("Enter Rock, Paper, or Scissors: ").lower()
        if user_input in choices:
            return user_input
        print("Invalid input! Please choose rock, paper, or scissors.")

def determine_winner(user, computer):
    if user == computer:
        return "tie"
    elif (user == "rock" and computer == "scissors") or \
         (user == "scissors" and computer == "paper") or \
         (user == "paper" and computer == "rock"):
        return "user"
    else:
        return "computer"

while True:
    print(f"\n--- Round {round_number} ---")
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()

    print(f"You chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")

    winner = determine_winner(user_choice, computer_choice)
    
    if winner == "tie":
        print("It's a tie!")
    elif winner == "user":
        print("You win this round!")
        user_score += 1
    else:
        print("Computer wins this round!")
        computer_score += 1

    print(f"Score → You: {user_score} | Computer: {computer_score}")

    
    play_again = input("\nDo you want to play again? (y/n): ").lower()
    if play_again != "y":
        print("\nThanks for playing! Final Score:")
        print(f"You: {user_score} | Computer: {computer_score}")
        break

    round_number += 1