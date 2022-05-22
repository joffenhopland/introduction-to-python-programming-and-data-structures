# Demonstrerer flere måter å bruke print metoden på...
radius = int(input("Gi inn radius : "))
omkrets = radius * 2 * 3.14
print("Omkrets av en sirkel med radius " + str(radius) + " er " + str(omkrets))
print(f'Omkrets av en sirkel med radius {radius} er {omkrets:.1f}')
print("Omkrets av en sirkel med radius",radius,"er",omkrets)