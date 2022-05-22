numbers_raw = input("Enter numbers: ")
list1 = numbers_raw.split()

list2 = []
for number in list1:
    if number not in list2:
        list2.append(number)
    else:
        continue
    
numbers_distinct = ""
numbers_distinct = numbers_distinct.join(list2)

print(f"the disttinct numbers are: {numbers_distinct}")
