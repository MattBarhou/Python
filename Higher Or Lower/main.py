from design import *
import random
from data import data

score = 0
continue_game = True

def compare_followers(followers1, followers2, user_choice):
    # If followers1 is greater than followers2, return True if user_choice is 'a', else return False
    if followers1 > followers2:
        return user_choice == 'a'
    else:
        # If followers2 is greater than followers1, return True if user_choice is 'b', else return False
        return user_choice == 'b'
    
    
person2 = random.choice(data)

print(logo)
while continue_game:
    
    #Assign person2 to person1 and get a new person2, so that the person which was correct in the last round is now compared with a new person
    person1 = person2
    person2 = random.choice(data)

    # Keep looping until we get two different people
    while person1 == person2:
        person2 = random.choice(data)

    followers1 = person1['follower_count']
    followers2 = person2['follower_count']
    
    print(f"Compare A: {person1['name']}, a {person1['description']}, from {person1['country']}.")
    print(vs)
    print(f"Against B: {person2['name']}, a {person2['description']}, from {person2['country']}.")

    user_choice = input("Who has more followers? Type 'A' or 'B': ").lower()

    #Function to compare the followers and return a boolean
    compare_result = compare_followers(followers1, followers2, user_choice)
    
    if compare_result:
        score += 1
        print(f"You're right! Current score: {score}.")
    else:
        continue_game = False
        print(f"Sorry, that's wrong. Final score: {score}")


    





