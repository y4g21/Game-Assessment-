import random

def guess_the_number():
    print("🎯 Welcome to Guess the Number!")
    print("I'm thinking of a number between 1 and 100.")
    
    number_to_guess = random.randint(1, 100)
    max_attempts = 7
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
