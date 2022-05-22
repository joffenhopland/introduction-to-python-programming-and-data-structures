import random

outputFile = open("Salary.txt", "w")

N = 1000
for i in range(N):
    outputFile.write("FirstName" + str(i + 1) + " ")
    outputFile.write("LastName" + str(i + 1) + " ")
    
    rank = random.randint(0, 2)
    if rank == 0:
        outputFile.write("assistant ")
        output.write(str(round(random.random() * 30000 + 50000, 2)))
    elif rank == 1:
        outputFile.write("associate ")
        outputFile.write(str(round(random.random() * 50000 + 60000, 2)))
    else:
        outputFile.write("full ")
        outputFile.write(str(round(random.random() * 55000 + 75000, 2)))

    if  i < N - 1:
        outputFile.write("\n")

outputFile.close()