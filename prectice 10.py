import random

secret_number = random.randint(1, 20)
number_of_guesses = 0
max_guesses = 6

print("I am thinking of a number between 1 and 20.")
print(f"You have {max_guesses} guesses.")

while number_of_guesses < max_guesses:
    try:
        guess_str = input(f"Guess #{number_of_guesses + 1}: ")
        guess = int(guess_str)
        number_of_guesses += 1

        if guess == secret_number:
            print(f"Congrats! You guessed the right number ({secret_number}) in {number_of_guesses} guesses!")
            break
        elif abs(guess - secret_number) == 1:
            print("You are VERY close!")
        elif guess > secret_number:
            print("Your number is greater than the secret number.")
        elif guess < secret_number:
            print("Your number is less than the secret number.")

    except ValueError:
        print("Invalid input. Please enter a whole number.")

else:
    print(f"You ran out of guesses! The secret number was {secret_number}.")