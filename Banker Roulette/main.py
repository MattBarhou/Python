import random
names = ["Angela", "Ben", "Jenny", "Michael", "Chloe"]
length = len(names)
randomnum = random.randint(0, length - 1)

print(f'{names[randomnum]} has to pay the bill today!')