import random
choices = ['rock', 'paper', 'scissors']

user_score = 0
computer_score = 0

print("🎮 Welcome to Rock, Paper, Scissors Game!")
print("Instructions: Type 'rock', 'paper', or 'scissors' to play. Type 'exit' to quit.\n")

while True:
    
    user_choice = input("Your choice (rock/paper/scissors): ").lower()

    if user_choice == 'exit':
        print("Thanks for playing!")
        print(f"Final Score ➤ You: {user_score}, Computer: {computer_score}")
        break

    if user_choice not in choices:
        print("Invalid choice. Please try again.")
        continue

    
    computer_choice = random.choice(choices)
    print(f"Computer chose: {computer_choice}")

    
    if user_choice == computer_choice:
        print("It's a tie!")
    elif (
        (user_choice == 'rock' and computer_choice == 'scissors') or
        (user_choice == 'paper' and computer_choice == 'rock') or
        (user_choice == 'scissors' and computer_choice == 'paper')
    ):
        print("✅ You win this round!")
        user_score += 1
    else:
        print("❌ You lose this round.")
        computer_score += 1

    
    print(f"Score ➤ You: {user_score}, Computer: {computer_score}\n")
