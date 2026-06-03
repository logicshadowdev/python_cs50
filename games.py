import random
def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])

def get_winner(player, computer):
    if player == computer:
        return "draw"
    elif (player == "rock" and computer == "scissors") or \
         (player == "scissors" and computer == "paper") or \
         (player == "paper" and computer == "rock"):
        return "player"
    else:
        return "computer"
    
player_score = 0
computer_score = 0
print("🎮 Rock Paper Scissors.\n")

while True:
    player = input("Enter rock, paper or scissors (q to quit): ")
    if player == "q":
        break
    if player not in ["rock", "paper", "scissors"]:
        print("Invalid Choice")
        continue
    computer = get_computer_choice()
    print(f"Computer chose: {computer}")

    winner = get_winner(player, computer)
    if winner == "draw":
        print("It's a draw")
    elif winner == "player":
        player_score +=1
        print("You win")
    else:
        computer_score +=1
        print("Computer win")
    print(f"\nScore - You: {player_score} | Computer: {computer_score}\n")
print(f"\n🏆 Final Score - You: {player_score} | Computer {computer_score}")