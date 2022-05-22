# This program creates a Car object, a Truck object,
# and an SUV object.
import vehicles
import pickle
import os

# Constants for the menu choices
NEW_CAR_CHOICE = 1
NEW_TRUCK_CHOICE = 2
NEW_SUV_CHOICE = 3
FIND_VEHICLE_CHOICE = 4
SHOW_VEHICLES_CHOICE = 5
QUIT_CHOICE = 6

def main():
    # Create list for vehicles
    try:    
        if os.path.isfile("vehicles.dat"):
            with open("vehicles.dat", "rb") as vehicleFile:
                vehicles_list = pickle.load(vehicleFile)
        else:
            vehicles_list = []
    except Exception as err:
        print(err)

        

    #Add new cars
    car = vehicles.Car('BMW 320', 2001, 70000, 15000.0, 4)
    vehicles_list.append(car)
    truck = vehicles.Truck('Toyota RAV4', 2002, 40000, 12000.0, "4WD")
    vehicles_list.append(truck)
    suv = vehicles.SUV('Volvo XC60', 2010, 30000, 18500.0, 5)
    vehicles_list.append(suv)
    
    choice = 0
    while choice != QUIT_CHOICE:
        # display the menu.
        display_menu()

        # Get the user's choice.
        try:
            choice = int(input('Enter your choice: '))
        except ValueError:
            pass

        # Perform the selected action.
        if choice == NEW_CAR_CHOICE:
            newVehicle(vehicles_list, "Car")
        elif choice == NEW_TRUCK_CHOICE:
            newVehicle(vehicles_list, "Truck")
        elif choice == NEW_SUV_CHOICE:
            newVehicle(vehicles_list, "SUV")
        elif choice == FIND_VEHICLE_CHOICE:
            searchVehicle(vehicles_list)
        elif choice == SHOW_VEHICLES_CHOICE:
            #show all vehicles
            print('\nThe following cars are in inventory:')
            for item in vehicles_list:
                print(item)
        elif choice == QUIT_CHOICE:
            print('Exiting the program...') 
            save(vehicles_list) 
        else:
            print('Error: invalid selection.')    
    
def save(vehicles_list):
    vehicles_list.sort(key=lambda x: x.make)
    with open("vehicles.dat", "wb") as saveFile:
        pickle.dump(vehicles_list, saveFile)

def newVehicle(vehicleList, vehicleType):
    while True:
        try:
            make = str(input("Make: "))       
            year = int(input("Year: "))
            milage = int(input("Milage: "))
            price = float(input("Price: "))                  

            if vehicleType == "Car":
                special = int(input("Doors: "))
                vehicleList.append(vehicles.Car(make, year, milage, price, special))

            elif vehicleType == "Truck":
                special = input("Drive Type: ")
                vehicleList.append(vehicles.Truck(make, year, milage, price, special))

            elif vehicleType == "SUV":
                special = int(input("Number of passengers: "))
                vehicleList.append(vehicles.SUV(make, year, milage, price, special))
        
        except ValueError:
            print("Please input correct value...")
            break      
        break
    
def searchVehicle(vehicleList):
    vehicleName = input("Name of vehicle: ")
    for vehicle in vehicleList:
        if vehicleName.lower() in vehicle.get_make().lower():
            print(vehicle.__str__())
        else:
            print("Car not in list")
    
# The display_menu function displays a menu.
def display_menu():
    print('        MENU')
    print('1) New car')
    print('2) New truck')
    print('3) New SUV')
    print('4) Find vehicles by make')
    print('5) Show all vehicles')
    print('6) Quit')     

# Call the main function.
if __name__ == '__main__':
      main()