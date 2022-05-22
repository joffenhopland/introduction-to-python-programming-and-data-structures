# "Manuell" måte å bytte innnhold i variabler
x = 1
y = 2
print(x,y)
#swap (bytt)
z = x
x = y
y = z
print(x,y)

#The Python way..
x,y = y,x
print(x,y)
