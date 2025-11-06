import random

def guess_the_number():
    print("🎯 Welcome to Guess the Number!")
    print("Choose a difficulty level:")
    print("1. Easy (1–50, 10 attempts)")
    print("2. Medium (1–100, 7 attempts)")
    print("3. Hard (1–200, 5 attempts)")

    # Choose difficulty
    while True:
        choice = input("Enter your choice (1, 2, or 3): ").strip()
        if choice == "1":
            max_attempts = 10
            number_to_guess = random.randint(1, 50)
            upper_limit = 50
            break
        elif choice == "2":
            max_attempts = 7
            number_to_guess = random.randint(1, 100)
            upper_limit = 100
            break
        elif choice == "3":
            max_attempts = 5
            number_to_guess = random.randint(1, 200)
            upper_limit = 200
            break
        else:
            print("⚠️ Invalid choice. Please enter 1, 2, or 3.")

    print(f"\nI'm thinking of a number between 1 and {upper_limit}.")
    
    attempts = 0

    while attempts < max_attempts:
        try:
            guess = int(input(f"Attempt {attempts + 1}/{max_attempts} - Enter your guess: "))
            attempts += 1
            
            if guess < number_to_guess:
                print("Too low! Try again.")
            elif guess > number_to_guess:
                print("Too high! Try again.")
            else:
                print(f"🎉 Congratulations! You guessed it in {attempts} attempts.")
                break
        except ValueError:
            print("⚠️ Please enter a valid number!")
    
    else:
        print(f"😢 Out of attempts! The number was {number_to_guess}.")

if __name__ == "__main__":
    guess_the_number()
