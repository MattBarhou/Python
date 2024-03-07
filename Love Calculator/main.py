print("Welcome to the Love Calculator!")
name1 = input("Enter your name: ")
name2 = input("Enter their name: ")
combinedname = name1 + name2
t = combinedname.lower().count("t")
r = combinedname.lower().count("r")
u = combinedname.lower().count("u")
e = combinedname.lower().count("e")
totaltrue = t + r + u + e
l = combinedname.lower().count("l")
o = combinedname.lower().count("o")
v = combinedname.lower().count("v")
e = combinedname.lower().count("e")
lovecount = l + o + v + e
total = int(str(totaltrue) + str(lovecount))

if total <= 10 or total >= 90:
    print(f"Your score is {total}, you go together like coke and mentos.") 
if total >= 40 and total <= 50:
    print(f"Your score is {total}, you are alright together.")
else:
    print(f"Your score is {total}.")


