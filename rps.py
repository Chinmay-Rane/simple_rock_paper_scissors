import random

guess = ("rock", "paper", "scissors")

def get_valid_move():
    move = input("Enter your move: ")
    while move not in guess:
        print("Invalid Input")
        move = input("Enter your move: ")
    return move

move = get_valid_move()
comp = random.choice(guess)

print(f"Computer: {comp}")
print(f"Your move: {move}")

if(move==comp):
    print("Its a draw")
elif(move=="scissors" and comp=="paper"):
    print("You win")
elif(move=="rock" and comp=="scissors"):
    print("You win")
elif(move=="paper" and comp=="rock"):
    print("You win")
elif(comp=="scissors" and move=="paper"):
    print("You Lose")
elif(comp=="rock" and move=="scissors"):
    print("You Lose")
elif(comp=="paper" and move=="rock"):
    print("You Lose")