s = input("Enter a floating point number: ")
k = s.find('.')
if k < 0:
   print("The number", s, "has no decimal point")
else: 
   print("The number of digits before the decimal point in", s,
      "is", s[0 : k]);