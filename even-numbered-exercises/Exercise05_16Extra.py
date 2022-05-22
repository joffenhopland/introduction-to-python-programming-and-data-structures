import random

countPlayer1 = 0
countPlayer2 = 0

for i in range(0, 1000001):
    count = 0
    while count <= 1 and count >= -1:
        # Generate scissor, rock, paper
        computerNumber = random.randint(0, 2)
  
        # Prompt the user to enter scissor, rock, or paper
        userNumber = random.randint(0, 2) # input.nextInt()
  
        # Check the guess
        if computerNumber == 0:
            if userNumber == 1:
                count += 1
            elif userNumber == 2:
                count -= 1
        elif computerNumber == 1:
            if userNumber == 0:
                count -= 1
            elif userNumber == 2:
                count += 1
        if computerNumber == 2:
            if userNumber == 0:
                count += 1
            elif userNumber == 1:
                count -= 1
  
    if count > 1:
        countPlayer1 += 1
    else:
        countPlayer2 += 1
    
print("Player1 won", countPlayer1, "times")
print("Player2 won", countPlayer2, "times")

