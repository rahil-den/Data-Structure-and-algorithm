import random

def get_random():
    return random.randint(1,20)

def user_guess():
    while True:
        try:
            guess = int(input("Take a guess: "))
            if 1<= guess <= 20:
                return guess
            else:
                print("Please enter a number between 1 and 20.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def main():
    print("Welcome to the number guessing game!")
    print("Yout have got 7 attempts to guess the correct number.")

    attempts = 7
    random_number = get_random()
    while attempts > 0:
        guess = user_guess()
        if guess == random_number:
            print("Congratulations! You've guessed the correct number.")
            break
        else:
            attempts -= 1
            print(f"Wrong guess! You have {attempts} attempts left.")

    if attempts == 0:
        print(f"Sorry, you've used all your attempts. The correct number was {random_number}.")

if __name__ == "__main__":
    main()
# The above code is a simple number guessing game where the user has to guess a random number between 1 and 20. 
# The user has 7 attempts to guess the correct number. If the user guesses correctly, a congratulatory message is displayed.
# If the user fails to guess the number within the given attempts, a message is displayed showing the correct number.