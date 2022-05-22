s = input("Enter a string: ")
maxOccurrenceCount = 1
maxOccurrenceChar = s[0]
currentOccurrenceCount = 1;
currentCh = s[0]
for i in range(0, len(s) - 1):
    if currentCh == s[i + 1]:
        currentOccurrenceCount += 1
  
    if currentCh != s[i + 1] or (i == len(s) - 2 and currentCh == s[i + 1]): 
        if currentOccurrenceCount > maxOccurrenceCount:
            maxOccurrenceCount = currentOccurrenceCount
            maxOccurrenceChar = currentCh

        currentCh = s[i + 1]
        currentOccurrenceCount = 1

print("The first longest consecutive repeating character substring is", end = ' ')
for i in range(0, maxOccurrenceCount):
    print(maxOccurrenceChar, end ='')
