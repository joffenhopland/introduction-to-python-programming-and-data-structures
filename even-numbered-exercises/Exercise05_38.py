s1 = input("Enter s1: ")
s2 = input("Enter s2: ")

s3 = ""
for i in range(min(len(s1), len(s2))):
    if s1[i] == s2[i]:
        s3 += s1[i];
    else:
        break

if len(s3) == 0:
    print("No common prefix")
else:
    print("The common prefix is", s3)