import pickle
import os.path


class Vehicles:
    def __init__(self, make, model, milage, price):
        self.make = make
        self.model = model
        self.milage = milage
        self.price = price

    def get_make(self):
        return self.make

    def get_model(self):
        return self.model

    def get_milage(self):
        return self.milage

    def get_price(self):
        return self.price

    def set_make(self, make):
        self.make = make

    def set_model(self, model):
        self.model = model

    def set_milage(self, milage):
        self.milage = milage

    def set_price(self, price):
        self.price = price

    def __str__(self):
        return f"{self.make}, {self.model}, {self.milage}, {self.price}"


class Car(Vehicles):
    def __init__(self, make, model, milage, price, doors):
        super().__init__(make, model, milage, price)
        self.doors = doors

    def get_doors(self):
        return self.doors

    def set_doors(self, doors):
        self.doors = doors

    def __str__(self):
        return f"{super().__str__()}, {self.doors}"


class Truck(Vehicles):
    def __init__(self, make, model, milage, price, drive_type):
        super().__init__(make, model, milage, price)
        self.drive_type = drive_type

    def get_drive_type(self):
        return self.drive_type

    def set_drive_type(self, drive_type):
        self.drive_type = drive_type

    def __str__(self):
        return f"{super().__str__()}, {self.drive_type}"


class SUV(Vehicles):
    def __init__(self, make, model, milage, price, pass_cap):
        super().__init__(make, model, milage, price)
        self.pass_cap = pass_cap

    def get_pass_cap(self):
        return self.pass_cap

    def set_pass_cap(self, pass_cap):
        self.pass_cap = pass_cap

    def __str__(self):
        return f"{super().__str__()}, {self.pass_cap}"


# This program creates a Car object, a Truck object,
# and an SUV object.


# Constants for the menu choices
NEW_CAR_CHOICE = 1
NEW_TRUCK_CHOICE = 2
NEW_SUV_CHOICE = 3
FIND_VEHICLE_CHOICE = 4
SHOW_VEHICLES_CHOICE = 5
QUIT_CHOICE = 6


def main():
    # Check if file already exists
    # Create empty list for vehicles
    if not os.path.isfile("vehicles.dat"):
        vehicles_list = []
    else:
        try:
            file = open("vehicles.dat", "rb")
            vehicles_list = pickle.load(file)
            print(vehicles_list)
        except EOFError:  # Catch eof error
            vehicles_list = []

        file.close()  # Close the input file

    # Create a Car object for a used 2001 BMW
    # with 70,000 miles, priced at $15,000, with
    # 4 doors.
    car = Car('BMW 320', 2001, 70000, 15000.0, 4)
    vehicles_list.append(car)
    # Create a Truck object for a used 2002
    # Toyota pickup with 40,000 miles, priced
    # at $12,000, with 4-wheel drive.
    truck = Truck('Toyota RAV4', 2002, 40000, 12000.0, '4WD')
    vehicles_list.append(truck)
    # Create an SUV object for a used 2000
    # Volvo with 30,000 miles, priced
    # at $18,500, with 5 passenger capacity.
    suv = SUV('Volvo XC60', 2010, 30000, 18500.0, 5)
    vehicles_list.append(suv)

    choice = 0
    while choice != QUIT_CHOICE:
        # display the menu.
        display_menu()

        # Get the user's choice.
        while True:
            try:
                choice = int(input('Enter your choice: '))
                if choice < 1 or choice > 6:
                    raise ValueError
                break
            except (ValueError) as error:
                print("Please enter a valid integer")

        # Perform the selected action.
        if choice == NEW_CAR_CHOICE:
            print('Input car data:')
            make = input("Make: ")
            while True:
                try:
                    model = input("Year: ")
                    if not model.isnumeric():
                        raise ValueError
                    break
                except (ValueError) as error:
                    print("Please enter integers only")
            while True:
                try:
                    milage = input("Milage: ")
                    if not milage.isnumeric():
                        raise ValueError
                    break
                except (ValueError) as error:
                    print("Please enter integers only")
            while True:
                try:
                    price = input("Price: ")
                    if not price.isnumeric():
                        raise ValueError
                    break
                except (ValueError) as error:
                    print("Please enter integers only")
            while True:
                try:
                    doors = input("Doors: ")
                    if not doors.isnumeric():
                        raise ValueError
                    break
                except (ValueError) as error:
                    print("Please enter integers only")
            car = Car(make, model, milage, price, doors)
            vehicles_list.append(car)
        elif choice == NEW_TRUCK_CHOICE:
            print('Add a new truck')
            print('Input truck data:')
            make = input("Make: ")
            while True:
                try:
                    model = input("Year: ")
                    if not model.isnumeric():
                        raise ValueError
                    break
                except (ValueError) as error:
                    print("Please enter integers only")
            while True:
                try:
                    milage = input("Milage: ")
                    if not milage.isnumeric():
                        raise ValueError
                    break
                except (ValueError) as error:
                    print("Please enter integers only")
            while True:
                try:
                    price = input("Price: ")
                    if not price.isnumeric():
                        raise ValueError
                    break
                except (ValueError) as error:
                    print("Please enter integers only")
            drive_type = input("Drive type: ")
            truck = Truck(make, model, milage, price, drive_type)
            vehicles_list.append(truck)
        elif choice == NEW_SUV_CHOICE:
            print('Add a new SUV')
            print('Input SUV data:')
            make = input("Make: ")
            while True:
                try:
                    model = input("Year: ")
                    if not model.isnumeric():
                        raise ValueError
                    break
                except (ValueError) as error:
                    print("Please enter integers only")
            while True:
                try:
                    milage = input("Milage: ")
                    if not milage.isnumeric():
                        raise ValueError
                    break
                except (ValueError) as error:
                    print("Please enter integers only")
            while True:
                try:
                    price = input("Price: ")
                    if not price.isnumeric():
                        raise ValueError
                    break
                except (ValueError) as error:
                    print("Please enter integers only")
            while True:
                try:
                    pass_cap = input("Passanger capacity: ")
                    if not pass_cap.isnumeric():
                        raise ValueError
                    break
                except (ValueError) as error:
                    print("Please enter integers only")
            suv = SUV(make, model, milage, price, pass_cap)
            vehicles_list.append(suv)
        elif choice == FIND_VEHICLE_CHOICE:
            print('Find vehicle by name')
            find_vehicle = input("Name of vehicle: ")
            # check if Make is in inventory
            for vehicle in vehicles_list:
                if vehicle.get_make() == find_vehicle:
                    print(vehicle)
        elif choice == SHOW_VEHICLES_CHOICE:
            # show all vehicles
            print('The following cars are in inventory:')
            for vehicle in vehicles_list:
                print(vehicle)
        elif choice == QUIT_CHOICE:
            print('Writing vehicles to file...')
            print('Exiting the program...')
            # Print to file
            file = open("vehicles.dat", "wb")
            vehicles_list.sort(key=lambda x: x.make)
            pickle.dump(vehicles_list, file)
            file.close()

        else:
            print('Error: invalid selection.')

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
