# Number Guessing Game
# Uses Binary Search algorithm
# The computer guesses YOUR number using binary search (always finds it in max 7 tries for 1-100)

import random

def binary_search_guess(low, high, target):
    """
    Binary Search: always guess the middle of the remaining range.
    This guarantees finding any number between 1-100 in at most 7 guesses.
    """
    steps = []
    attempts = 0

    while low <= high:
        mid = (low + high) // 2   # guess the middle
        attempts += 1
        steps.append(f"  Attempt {attempts}: guessing {mid} (range {low}-{high})")

        if mid == target:
            steps.append(f"  Found! The number is {mid}")
            break
        elif mid < target:
            steps.append(f"  Too low! Search upper half: {mid+1}-{high}")
            low = mid + 1          # discard lower half
        else:
            steps.append(f"  Too high! Search lower half: {low}-{mid-1}")
            high = mid - 1         # discard upper half

    return attempts, steps


def player_guesses(secret):
    """Player tries to guess the computer's secret number."""
    print(f"\n  I'm thinking of a number between 1 and 100.")
    print(f"  Try to guess it!\n")
    attempts = 0

    while True:
        try:
            guess = int(input("  Your guess: "))
        except ValueError:
            print("  Please enter a valid number.")
            continue

        if guess < 1 or guess > 100:
            print("  Please guess between 1 and 100.")
            continue

        attempts += 1

        if guess == secret:
            print(f"\n  Correct! You got it in {attempts} attempt(s).")
            print(f"  Binary search would have done it in at most 7.")
            break
        elif guess < secret:
            print(f"  Too low! Try higher.")
        else:
            print(f"  Too high! Try lower.")


def computer_guesses():
    """Computer uses Binary Search to guess the player's number."""
    print("\n  Think of a number between 1 and 100. Don't tell me!")
    print("  I will use Binary Search to find it.\n")
    input("  Press Enter when you're ready...")

    low, high = 1, 100
    attempts = 0

    while low <= high:
        mid = (low + high) // 2
        attempts += 1
        print(f"\n  Attempt {attempts}: Is your number {mid}?")
        print("  Enter: H = too high, L = too low, Y = correct")

        while True:
            answer = input("  Your answer: ").strip().upper()
            if answer in ("H", "L", "Y"):
                break
            print("  Please enter H, L, or Y.")

        if answer == "Y":
            print(f"\n  I found your number ({mid}) in {attempts} attempt(s) using Binary Search!")
            break
        elif answer == "L":
            low = mid + 1
        else:
            high = mid - 1
    else:
        print("\n  Something went wrong — are you sure you followed the rules?")


def show_demo():
    """Show how binary search works step by step."""
    print("\n" + "="*50)
    print("  BINARY SEARCH DEMO")
    print("="*50)
    number = random.randint(1, 100)
    print(f"  Secret number: {number}")
    print(f"  Watching binary search find it...\n")
    attempts, steps = binary_search_guess(1, 100, number)
    for step in steps:
        print(step)
    print(f"\n  Done in {attempts} step(s)! Max possible = 7.")
    print("="*50)


def main():
    print("="*50)
    print("   NUMBER GUESSING GAME")
    print("   Algorithm: Binary Search")
    print("="*50)

    while True:
        print("\n  MENU")
        print("  1. You guess the computer's number")
        print("  2. Computer guesses your number (Binary Search)")
        print("  3. Watch Binary Search demo")
        print("  4. Quit")

        choice = input("\n  Choose (1/2/3/4): ").strip()

        if choice == "1":
            secret = random.randint(1, 100)
            player_guesses(secret)

        elif choice == "2":
            computer_guesses()

        elif choice == "3":
            show_demo()

        elif choice == "4":
            print("\n  Goodbye!\n")
            break

        else:
            print("  Invalid choice. Please enter 1, 2, 3, or 4.")


if __name__ == "__main__":
    main()
