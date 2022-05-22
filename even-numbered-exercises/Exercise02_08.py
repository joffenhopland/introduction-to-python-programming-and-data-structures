# Prompt the user to enter a degree in Celsius
mass = float(input("Enter the amount of water in kilograms: "))

initialTemperature = float(input("Enter the initial temperature: "))
    
finalTemperature = float(input("Enter the final temperature: "))

energy =  mass * (finalTemperature - initialTemperature) * 4184

print("The energy needed is", energy)