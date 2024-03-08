from data import *
is_served = True
profit = 0

def compare_choice(maintain_choice):
    if maintain_choice == 'off':
        return False
    elif maintain_choice == 'report':
        print(f"Water: {resources['water']}ml\nMilk: {resources['milk']}ml\nCoffee: {resources['coffee']}g\nMoney: ${profit}")
        
def check_resources(drink):
    #Get the specific drink data
    drink_data = MENU[drink]
    
    #Loop through the ingredients of the drink and check if there are enough resources
    for drink_type, amount in drink_data['ingredients'].items():
        if resources[drink_type] < amount:
            print(f"Sorry there is not enough {amount}.")
            return False
    return True

def calculate_change():
    print("Please insert coins.")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))
    total = (quarters * 0.25) + (dimes * 0.10) + (nickles * 0.05) + (pennies * 0.01)
    return total

def purchase_drink(drink, total):
    drink_cost = MENU[drink]['cost']
    if total > drink_cost:
        change = total - drink_cost
        print(f"Here is ${change:.2f} in change.")
        print(f"Here is your {drink} ☕️. Enjoy!")
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


while is_served:
    drink_choice = input("What would you like? (espresso/latte/cappuccino): ")
    
    #Check if maintainers want the machine off
    result = compare_choice(drink_choice)
    
    if result == False:
        is_served = False
        break
    else:
       if check_resources(drink_choice):
           #Store the total amount inserted
          total_amount = calculate_change()
          #Check if the user has enough money to purchase the drink
          if purchase_drink(drink_choice, total_amount):
                #Update the profit
                profit += MENU[drink_choice]['cost']
                #Update the resources
                for drink_type, amount in MENU[drink_choice]['ingredients'].items():
                    resources[drink_type] -= amount
                