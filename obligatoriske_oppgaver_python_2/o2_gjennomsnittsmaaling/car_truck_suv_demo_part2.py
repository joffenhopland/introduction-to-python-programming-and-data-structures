import os.path
import vehicles
import pickle
import datetime

# Constants for the menu choice
NEW_CAR_CHOICE = 1
NEW_TRUCK_CHOICE = 2
NEW_SUV_CHOICE = 3
FIND_VEHICLE_CHOICE = 4
SHOW_VEHICLES_CHOICE = 5
CHECK_FOR_TICKET = 6
QUIT_CHOICE = 7


def main():
    if os.path.isfile("Cars2.dat"):
        vehicles_list = []
        inputFile = open("Cars2.dat", "rb")
        end_of_file = False
        while not end_of_file:
            try:
                car = pickle.load(inputFile)
                vehicles_list.append(car)
            except EOFError:
                end_of_file = True
        inputFile.close()

    else:
        vehicles_list = []

    car = vehicles.Car('BMW 320', 2001, 70000, 15000.0, "FY99401", 4)
    vehicles_list.append(car)

    truck = vehicles.Truck('Toyota RAV4', 2002, 40000,
                           12000.0, "DA49644", '4WD')
    vehicles_list.append(truck)

    suv = vehicles.SUV('Volvo XC60', 2010, 30000, 18500.0, "SY60306", 5)
    vehicles_list.append(suv)

    choice = 0
    while choice != QUIT_CHOICE:
        # display the menu.
        display_menu()

        # Get the user's choice.
        choice = int(input('Enter your choice: '))

        # Perform the selected action.
        if choice == NEW_CAR_CHOICE:
            car = menu1()
            vehicles_list.append(car)
            display_menu()

        elif choice == NEW_TRUCK_CHOICE:
            truck = menu2()
            vehicles_list.append(truck)
            display_menu()

        elif choice == NEW_SUV_CHOICE:
            suv = menu3()
            vehicles_list.append(suv)
            display_menu()
        elif choice == FIND_VEHICLE_CHOICE:
            menu4(vehicles_list)
        elif choice == SHOW_VEHICLES_CHOICE:
            # show all vehicles
            print('The following cars are in inventory:')
            for item in vehicles_list:
                print(item.__str__())

        elif choice == CHECK_FOR_TICKET:
            menu6(vehicles_list)
        elif choice == QUIT_CHOICE:
            print('Exiting the program...')
            sort_Close_List(vehicles_list)
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
    print('6) Check for ticket')
    print('7) Quit')


def menu1():
    print()
    print(f'Please enter the details for your car: ')
    merke = input(f'Fyll inn merke: ')
    modell = input(f'Fyll inn årsmodell: ')
    km = input(f'Fyll inn kilometerstand: ')
    pris = input(f'Fyll inn pris: ')
    regNr = input(f'Fyll inn registreringsnummer: ')
    dører = input(f'Hvor mange dører har bilen: ')
    car = vehicles.Car(merke, modell, km, pris, regNr, dører)
    return car


def menu2():
    print(f'Please enter the details for your Truck: ')
    merke = input(f'Fyll inn merke: ')
    modell = input(f'Fyll inn årsmodell :')
    km = input(f'Fyll inn kilometerstand: ')
    pris = input(f'Fyll inn pris: ')
    regNr = input(f'Fyll inn registreringsnummer: ')
    hjuldrift = input(f'4WD or 2WD?: ')
    truck = vehicles.Truck(merke, modell, km, pris, regNr, hjuldrift)
    return truck


def menu3():
    print(f'Please enter the details for your SUV: ')
    merke = input(f'Fyll inn merke: ')
    modell = input(f'Fyll inn årsmodell :')
    km = input(f'Fyll inn kilometerstand: ')
    pris = input(f'Fyll inn pris: ')
    regNr = input(f'Fyll inn registreringsnummer: ')
    passasjer = input(f'Fyll inn passasjer kapasitet: ')
    suv = vehicles.SUV(merke, modell, km, pris, regNr, passasjer)
    return suv


def menu4(vehicles_list):
    name = input(f'Name of Vehicle: ')
    name = name.upper()
    for i in range(0, len(vehicles_list)):
        if name in vehicles_list[i].getMerke().upper():
            print(vehicles_list[i].__str__())


def menu6(vehicle_list):
    file1 = "box_a.txt"
    file2 = "box_b.txt"
    speeding_Dictionary = list_speeders(
        file1, file2, 60, 5)  # legg inn listspeeders
    for i in range(len(vehicle_list)):
        if vehicle_list[i].getRegNr() in speeding_Dictionary:
            vehicle_list[i].setSpeedTicket(vehicle_list[i].getRegNr(), speeding_Dictionary.get(vehicle_list[i].getRegNr())[1],
                                           speeding_Dictionary.get(vehicle_list[i].getRegNr())[0], 60)


def sort_Close_List(vehicles_list):
    vehicles_list.sort(key=lambda x: x.getMerke())
    outputFile = open("Cars2.dat", "wb")
    for i in range(len(vehicles_list)):
        pickle.dump(vehicles_list[i], outputFile)
    outputFile.close()


def fileToDictionary(filename):
    if os.path.isfile(filename):
        inputFile = open(filename, "r")
        car_dictionary = {}

        line = inputFile.readline().split(",")
        while line != ['']:

            car_dictionary[line[0].strip()] = line[1].strip()
            line = inputFile.readline().split(",")

        inputFile.close()
    else:
        print(f'Sorry, the file does not exist')

    return car_dictionary


def list_speeders(filename_a, filename_b, speed_limit, distance):
    filename_a = fileToDictionary(filename_a)
    filename_b = fileToDictionary(filename_b)
    speeding_dictionary = {}

    for (reg_a, time_a), (reg_b, time_b) in zip(filename_a.items(), filename_b.items()):
        time_difference = datetime.datetime.strptime(
            time_b, '%Y-%m-%d %H:%M:%S') - datetime.datetime.strptime(time_a, '%Y-%m-%d %H:%M:%S')
        difference_in_hours = time_difference.total_seconds() / 3600
        avg_speed = distance / difference_in_hours

        if avg_speed > speed_limit * 1.05:
            speeding_dictionary[reg_a] = (f'{avg_speed:.3f}', f'{time_a}')

    return speeding_dictionary


# Call the main function.
if __name__ == '__main__':
    main()
