import random

logo = """_____                        ________            _   __                __             
  / ____/_  _____  __________   /_  __/ /_  ___     / | / /_  ______ ___  / /_  ___  _____
 / / __/ / / / _ \/ ___/ ___/    / / / __ \/ _ \   /  |/ / / / / __ `__ \/ __ \/ _ \/ ___/
/ /_/ / /_/ /  __(__  |__  )    / / / / / /  __/  / /|  / /_/ / / / / / / /_/ /  __/ /    
\____/\__,_/\___/____/____/    /_/ /_/ /_/\___/  /_/ |_/\__,_/_/ /_/ /_/_.___/\___/_/     
                                                                                          
"""
print(logo)

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
number = random.randint(1, 100)
print(f"NUMBER = {number}")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")

if difficulty == "easy":
    attempts = 10
else:
    attempts = 5 

print(f"You have {attempts} remaining to guess the number.")

while attempts > 0:
  guess = int(input("Make a guess: "))
  if guess > number:
      attempts -= 1
      print("Too high.")
      print(f"You have {attempts} remaining to guess the number.")
  elif guess < number:
      attempts -= 1
      print("Too low.")
      print(f"You have {attempts} remaining to guess the number.")
  else:
      print(f"You got it! The answer was {number}.")