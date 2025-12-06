import random

def play_game():
    print("🎲 Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 50.")
    print("Try to guess it in as few attempts as possible.\n")

    secret_number = random.randint(1, 50)
    attempts = 0

    while True:
        try:
            guess = int(input("Enter your guess (1–50): "))
        except ValueError:
            print("Please enter a valid whole number.")
            continue

        if guess < 1 or guess > 50:
            print("Your guess must be between 1 and 50.")
            continue

        attempts += 1

        if guess < secret_number:
            print("Too low! Try again.\n")
        elif guess > secret_number:
            print("Too high! Try again.\n")
        else:
            print(f"✅ Correct! The number was {secret_number}.")
            print(f"🎉 You guessed it in {attempts} attempts.")
            break

if __name__ == "__main__":
    play_game()
