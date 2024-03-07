print("Welcome to the tip calculator.")
totalbill = float(input("What was the total bill? $"))
tip = float(input("What percentage tip would you like to give? 10, 12, or 15? "))
totalpeople = float(input("How many people are splitting the bill? "))

total = float((totalbill / totalpeople) * (tip / 100 + 1))
print(f"Each person should pay: ${total:.2f}")