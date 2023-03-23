#BMI calculator
weight= float(input("Enter your weight: "))
height= float(input("Enter your height(meters): "))
height= height**2
#print(height)
results= weight // height

if results < 18.5:
    print(f"Your BMI is {results}. You are underweight")
elif results >= 18.5 and results <24.9:
    print(f"Your BMI is {results}. You are healthy")
elif results >= 25 and results < 29.9:
    print(f"Your BMI is {results}. You are overweight")
elif results >= 30 and results <34.9:
    print(f"Your BMI is {results}. You are obesity (class I)")
elif results >= 35 and results <39.9:
    print(f"Your BMI is {results}. You are obesity (class II)")
elif results >= 40:
    print(f"Your BMI is {results}. You are in extreme obesity(exercise more)")

