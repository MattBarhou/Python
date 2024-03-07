from logo import logo

continue_bidding = True
bidder = []
print(logo)

while continue_bidding:
    name = input("What is your name? ")
    bid = int(input("What's your bid? $"))

    bidder.append({"name": name, "bid": bid})

    more_bidders = input("Are there any other bidders? Type 'yes' or 'no'. ").lower()
    
    if more_bidders == 'no':
        continue_bidding = False
        break


    
max_bid = max(bidder, key=lambda x:x['bid'])
        
print(f"The winner is {max_bid['name']} with a bid of ${max_bid['bid']}.")
    
    