import random
from words import word_list
from logo import logo

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

chosen_word = random.choice(word_list)
letter_list = ['_' for _ in chosen_word]

isCorrect = False
lives = 6

print(logo)

while "_" in letter_list:
    guess = input("Guess a letter: ").lower()
    
    if guess in letter_list:
        print("You've already guessed that letter.")
        continue

        
    for i, letter in enumerate(chosen_word):
        if letter == guess:
            letter_list[i] = guess
            isCorrect = True
    
    if isCorrect == True:
        print("Correct!")
        isCorrect = False
    else:
        print("Incorrect!")
        lives -= 1
        
    print(" ".join(letter_list))
    
    
    if lives == 0:
        print("You lose!")
        print(f"The word was {chosen_word}")
        break
            
    if "_" not in letter_list:
        print("You win!")
        
    print(stages[lives])
            
       
   
print(letter_list)
