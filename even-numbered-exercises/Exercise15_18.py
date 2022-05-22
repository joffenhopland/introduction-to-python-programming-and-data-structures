import time

# The function for finding the solution to move n disks
#   from fromTower to toTower with auxTower


def moveDisks(n, fromTower, toTower, auxTower):
    global count

    if n == 1:  # Stopping condition
        print("Move disk " + str(n) + " from " +
              fromTower + " to " + toTower)
        count += 1
    else:
        moveDisks(n - 1, fromTower, auxTower, toTower)
        print("Move disk " + str(n) + " from " +
              fromTower + " to " + toTower)
        count += 1
        moveDisks(n - 1, auxTower, toTower, fromTower)


count = 0
n = int(input("Enter number of disks: "))

# Find the solution recursively
print("The moves are:")
startTime = time.time()
moveDisks(n, 'A', 'B', 'C')
endTime = time.time()
elapsed = endTime - startTime
print("Number of moves is " + str(count))
print("It took", elapsed,  "seconds to run")
