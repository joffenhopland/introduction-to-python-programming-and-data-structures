import math

print(format("Degree", "<15s"), format("Sin", "<15s"), format("Cos", "<15s"))
for degree in range(0, 361):
    print(format(degree, "<15d"), format(math.sin(degree * math.pi / 180), "<15.4f"),
        format(math.cos(degree * math.pi / 180) / 180, "<15.4f"))