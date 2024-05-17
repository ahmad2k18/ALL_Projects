import time

def start_game():
    print("Welcome to the Adventure Game!")
    time.sleep(1)
    print("You find yourself in a mysterious forest...")
    time.sleep(1)
    print("You must navigate through different scenarios and make choices that affect the outcome.")
    time.sleep(1)
    print("Let's begin!")
    time.sleep(1)
    scenario1()

def scenario1():
    print("\nYou encounter a fork in the road.")
    print("Do you take the left path or the right path? (left/right)")
    choice = input("Enter your choice: ").lower()
    if choice == "left":
        print("\nYou chose the left path...")
        time.sleep(1)
        print("You find a hidden treasure!")
        time.sleep(1)
        print("Congratulations! You win!")
    elif choice == "right":
        print("\nYou chose the right path...")
        time.sleep(1)
        print("You encounter a hungry bear...")
        time.sleep(1)
        print("You were eaten by the bear. Game over!")
    else:
        print("Invalid choice. Please enter 'left' or 'right'.")
        scenario1()

# Start the game
start_game()
