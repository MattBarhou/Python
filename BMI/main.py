weight = float(input("Enter your weight in KG: "))
height = float(input("Enter your height in meters: "))
result = weight / height ** 2

if result >= 37:
    print(f"Your BMI is {result:.2f}. You are clinically obese.")
elif result >= 32:
    print(f"Your BMI is {result:.2f}. You are obese.")
elif result >= 28:
    print(f"Your BMI is {result:.2f}. You are slightly overweight.")
elif result >=22:
    print(f"Your BMI is {result:.2f}. You are normal weight.")
else:
    print(f'Your BMI is {result:.2f}. You are underweight.')