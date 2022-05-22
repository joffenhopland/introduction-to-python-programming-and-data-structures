#Solution 1
'''
for i in range(1, 6 + 1):
    # Print leading space
    for j in range(6 - i, 0, -1):
        print("  ", end = "")
      
    for j in range(i, 0, -1):
        print(j, end = " ")

    print()
'''

#Solution 2
for i in range(1, 6 + 1):
    for j in range(6, 0, -1): 
       print(j if j <= i else " ", end = " ")
    print()
