# Prompt the user to enter weight in pounds
weight = float(input("Enter weight in pounds: "))

# Prompt the user to enter height in inches
height = float(input("Enter height in inches: "))

bmi = weight * 0.45359237 / (height * 0.0254 * height * 0.0254)
    
print("BMI is", bmi)
