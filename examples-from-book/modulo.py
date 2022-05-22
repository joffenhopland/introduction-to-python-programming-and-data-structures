# Demonstrerer bruk av modulo operatoren

print("10 % 10 blir", 10 % 10 )
print("10 % 5 blir", 10 % 5)
print("10 % 6 blir", 10 % 6)
print("11 % 10 blir", 11 % 10)
print("9 % 10 blir", 9 % 10)

# Liketall eller oddetall?
tall = int(input("Gi inn et tall: "))
if (tall % 2 == 0):
    print(f'{tall} er et liketall')
else:
    print(f'{tall} er et oddetall')