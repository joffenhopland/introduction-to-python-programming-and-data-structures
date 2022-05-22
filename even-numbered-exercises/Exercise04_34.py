s1 = input("Enter the first city: ")
s2 = input("Enter the second city: ")
s3 = input("Enter the third city: ")

if s1 > s2:
  # Swap s1 with s2
  temp = s1
  s1 = s2
  s2 = temp

if s2 > s3:
  # Swap s2 with s3
  temp = s2
  s2 = s3
  s3 = temp

if s1 > s2:
  # Swap s1 with s2
  temp = s1
  s1 = s2
  s2 = temp

print("The three cities in alphabetical order are", s1, s2, s3)
