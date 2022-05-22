import os
import pickle
import datetime


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
            speeding_dictionary[reg_a] = (f'{avg_speed:.3f}, {time_a}')

    return speeding_dictionary
