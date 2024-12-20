import random
#importing random wow awesome 


#random \n are for the looks in the terminal - not so bunched up

def determine_winner(player_choice, computer_choice):
    '''Dictionary to determine the ways you can win and lose: i.e. the key wins against its values (Spock beats scissors and rock in line 12)'''

    rules = {
        "rock": ["scissors", "lizard"],
        "paper": ["rock", "spock"],
        "scissors": ["paper", "lizard"],
        "lizard": ["spock", "paper"],
        "spock": ["scissors", "rock"],
    }

    if player_choice == computer_choice:
        return "It's a tie!"
    # if the computer's choice is a value in the list of the key (player choice's) complementary value, the player wins
    elif computer_choice in rules[player_choice]:
        return "You win!"
    #if not found, the player loses (computer wins)
    else:
        return "Computer wins!"

def rpsls_game():
    choices = ["rock", "paper", "scissors", "lizard", "spock"]

    print("Welcome to Rock-Paper-Scissors-Lizard-Spock!")
    print("Choices: Rock, Paper, Scissors, Lizard, Spock")

    while True:
        player_choice = input("Enter your choice: ").lower()
        if player_choice not in choices:
            print("Invalid choice. Please try again.")
            continue

        computer_choice = random.choice(choices)
        print(f"Computer chose: {computer_choice}")

        result = determine_winner(player_choice, computer_choice)
        print(result)

        play_again = input("\n" + "Do you want to play again? (yes/no): ").lower()
        if play_again == "no" or play_again == "n":
            print("\n" + "Thanks for playing! Goodbye!")
            break

        else:
            print("\n")
            print("Choices: Rock, Paper, Scissors, Lizard, Spock")
            continue
            

if __name__ == "__main__":
    rpsls_game()
