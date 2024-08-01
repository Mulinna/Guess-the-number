import random
from art import logo
print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number from 1 to 100")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
choice = random.randint(1, 100)
EASY_LIVES = 10
HARD_LIVES = 5

def difficulty_level(difficulty):
  if difficulty == "easy":
    return EASY_LIVES 
  elif difficulty == "hard":
    return HARD_LIVES

def game(choice, lives):
  while lives > 0:
    guess = int(input("Make a guess: "))
    if guess > choice:
      lives -= 1
      print("Too high! Guess again!")
      print(f"You have {lives} attempts remaining to guess the number")
    elif guess < choice:
      lives -= 1
      print("Too low! Guess again!")
      print(f"You have {lives} attempts remaining to guess the number")
    elif guess == choice:
      print(f"You got it! The answer was {choice}")
      return
  if lives == 0:
    print("Game over! You ran out of guesses!")

if difficulty == "easy":
    game(choice, difficulty_level("easy"))

elif difficulty == "hard":
    game(choice, difficulty_level("hard"))
