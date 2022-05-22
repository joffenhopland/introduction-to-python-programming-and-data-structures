import random

vehiclePlateNumber = ""
for i in range(7):
    ch = chr(ord('A') + random.randint(0, 25)) if random.randint(0, 1) == 0  \
        else chr(ord('0') + random.randint(0, 9))
    vehiclePlateNumber += ch
    
print("A random vehicle plate number:", vehiclePlateNumber)
