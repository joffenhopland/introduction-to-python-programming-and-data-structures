distance = float(input("Enter the driving distance: "))
milesPerGallon = float(input("Enter miles per gallon: "))
pricePerGallon = float(input("Enter price per gallon: "))
print("The cost of driving is $" + str((distance / milesPerGallon) * pricePerGallon))