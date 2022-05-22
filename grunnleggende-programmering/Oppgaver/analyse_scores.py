numbers = "2 5 6 5 42 3 23 5 43 2 -4"
items = numbers.split()
numbers_list = [int(x) for x in items]

average = sum(numbers_list) / len(numbers_list)
scores_over_equal_avg = 0
scores_under_agv = 0

for i in numbers_list:
    if i >= average:
        scores_over_equal_avg += 1
    else:
        scores_under_agv += 1

print(f"Average is {average}")
print(
    f"Number of scores above or equal to the average: {scores_over_equal_avg}")
print(f"Number of scores below the average: {scores_under_agv}")
