import random


# Create a deal_card() function that uses the List below to *return* a random card.
#11 is the Ace.
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def deal_card():
    random_num = random.choice(cards)
    return random_num


def calculate_score(cards = []):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
        
    return sum(cards)


def compare(user_score, computer_score):
    if user_score == computer_score:
        return "Draw"
    elif computer_score == 0:
        return "Lose, opponent has Blackjack"
    elif user_score == 0:
        return "Win with a Blackjack"
    elif user_score > 21:
        return "You went over. You lose"
    elif computer_score > 21:
        return "Opponent went over. You win"
    elif user_score > computer_score:
        return "You win"
    elif user_score < computer_score:
        return "You lose"


def play_game():
# Deal the user and computer 2 cards each using deal_card() and append().
    user_cards = []
    computer_cards = []
    game_over = False


#Deal the user and computer 2 cards each using deal_card() and append().
    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())
    
      
    while not game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Computer's first card: {computer_cards[0]}")


        #Check if the user or computer has blackjack (0) or if the user's score is over 21. If so, then the game ends.
        if user_score == 0 or computer_score == 0 or user_score > 21:
            game_over = True

        #If the game has not ended, ask the user if they want to draw another card. 
        # If yes, then use the deal_card() function to add another card to the user_cards List.
        else:
            another_card = input("Do you want to draw another card? Type 'y' or 'n': ").lower()

        #If the user wants another card then deal a new card and calculate the new score.  
            if another_card == 'y':
                user_cards.append(deal_card())
                user_score = calculate_score(user_cards)
            else:
                game_over = True
                print(f"Your final hand: {user_cards}, final score: {user_score}")
            
    #The computer should then keep drawing cards as long as it has a score less than 17.
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))
    
while input("Do you want to play Blackjack? Type 'y' or 'n': ").lower() == 'y':
    play_game()
    

