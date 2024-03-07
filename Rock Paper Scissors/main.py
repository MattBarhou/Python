import random
random_integer = random.randint(0, 2)
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
alloptions = [rock, paper, scissors]
choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
if choice >= 3 and choice < 0:
    print("Invalid Input!")
else:
    print(alloptions[choice])
    print(f"Computer chose:\n{alloptions[random_integer]}")

    if random_integer == 0 and choice == 2:
        print("You lose!")
    elif choice == 0 and random_integer == 2:
        print("You win!")
    elif random_integer == choice:
        print("Its a draw!")
    elif random_integer > choice:
        print("You lose!")
    elif choice > random_integer:
        print("You win!")


