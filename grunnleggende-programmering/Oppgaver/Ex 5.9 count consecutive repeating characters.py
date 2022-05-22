# Ask user to enter string
# If string == 0 then quit
# 



s = input("Enter a string: ")
if len(s) == 0:
    print("Strengen må være på minst ett tegn")
    quit()
    
currentCount = 1
mostCount = 1
theLetter = s[0]

for i in range(0, len(s) - 1):
    if s[i] == s[i + 1]:
        currentCount += 1
    else:
        currentCount = 1
    if (currentCount > mostCount):
        mostCount = currentCount
        theLetter = s[i]
        
print(f'The number of consecutive repeating characters is {mostCount} and the letter is {theLetter}')
