from random import choice

# Create a list of play options
options = ["Rock", "Paper", "Scissors"]

def get_computer_choice():
    return choice(options)

def get_user_choice():
    user_input = input("Enter your choice (Rock, Paper, Scissors): ")
    if user_input in options:
        return user_input
    else:
        print("Invalid choice. Please choose Rock, Paper, or Scissors.")
        return get_user_choice()

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == "Rock" and computer_choice == "Scissors") or \
         (user_choice == "Paper" and computer_choice == "Rock") or \
         (user_choice == "Scissors" and computer_choice == "Paper"):
        return f"You win! {user_choice} beats {computer_choice}"
    else:
        return f"You lose! {computer_choice} beats {user_choice}"

def play_game():
    while True:
        computer_choice = get_computer_choice()
        user_choice = get_user_choice()
        print(determine_winner(user_choice, computer_choice))
        play_again = input("Do you want to play again? (y/n): ").lower()
        if play_again != 'y':
            print("Thanks for playing!")
            break

# Start the game
play_game()
