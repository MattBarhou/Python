import random
from art import logo

random_number = random.randint(1, 100)


attempts = 0


def play_game(attempts):
    while attempts != 0 and guess != random_number:
        print(f"You have {attempts} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        if guess == random_number:
            print(f"You got it! The answer was {random_number}")
            break
        elif guess > random_number:
            print("Too high.")
        else:
            print("Too low.")
        attempts -= 1
        if attempts == 0:
            print("You've run out of guesses, you lose.")
        else:
            print("Guess again.")


print(logo)
print("Welcome to the number guessing game!")
print("I'm thinking of a number between 1 and 100")

difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

if difficulty == "easy":
    attempts = 10
elif difficulty == "hard":
    attempts = 5
    

play_game(attempts)
    