print("Thank you for choosing Pizza Palace Deliveries!")
size = input("What size pizza do you want? S, M, or L: ")
pepperoni = input("Do you want pepperoni? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")
total = 0

if size == 'S':
    total = 15
    if extra_cheese == 'Y':
        total += 1
if size == 'M':
    total = 20
    if pepperoni == 'Y':
        if extra_cheese == 'Y':
            total += 3
if size == 'L':
    total = 25
    if pepperoni == 'Y':
        total += 3
        if extra_cheese == 'Y':
            total += 1
            
print(f'Your final bill is ${total}')
    

    