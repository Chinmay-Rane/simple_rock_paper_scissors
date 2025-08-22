import random


def play_again():

    again=input("Want to play again?: ")
    if(again=="yes"):
        main()
    elif(again=="no"):
        thx()
    
def thx():
    print("Thanks for playing")

guess = ("rock", "paper", "scissors")

def get_valid_move():
    move = input("Enter your move: ")
    while move not in guess:
        print("Invalid Input")
        move = input("Enter your move: ")
    return move
def main():
    move = get_valid_move()
    comp = random.choice(guess)

    print(f"Computer: {comp}")
    print(f"Your move: {move}")
    

    if(move==comp):
        print("Its a draw")
        result="draw"
    elif(move=="scissors" and comp=="paper"):
        print("You win")
        result="win"
    elif(move=="rock" and comp=="scissors"):
        print("You win")
        result="win"
    elif(move=="paper" and comp=="rock"):
        print("You win")
        result="win"
    elif(comp=="scissors" and move=="paper"):
        print("You Lose")
        result="lose"
    elif(comp=="rock" and move=="scissors"):
        print("You Lose")
        result="lose"
    elif(comp=="paper" and move=="rock"):
        print("You Lose")
        result="lose"
 
     # Read current streaks (create file if missing)
    try:
        with open("streaks.txt", "r") as f:
            lines = f.readlines()
            win = int(lines[0].strip())
            lose = int(lines[1].strip())
    except (FileNotFoundError, IndexError, ValueError):
        win = 0
        lose = 0

    # Update streaks
    if (result == "draw"):
        # Draw does not change streak
        pass
    elif (result == "win"):
        win += 1
        lose = 0
    elif (result == "lose"):
        lose += 1
        win = 0

    # Write back updated streaks
    with open("streaks.txt", "w") as f:
        f.write(f"{win}\n{lose}\n")
    if(result!="draw"):
        if(win==1):
            print("YOUR LOSING STREAK ENDED")
        if(lose==1):
            print("YOUR WINNING STREAK ENDED")
    if(lose>=2):
        print(f"YOU ARE ON A LOSING STREAK OF {lose}")

    if(win>=2):
        print(f"YOU ARE ON A WINNING STREAK OF {win}")
    if(lose>=2):
        print(f"YOU ARE ON A LOSING STREAK OF {lose}")
    play_again()
main()
