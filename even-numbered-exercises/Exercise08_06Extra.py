from math import sqrt

def main():
    # Students' answers to the questions
    answers = [
      ['A', 'B', 'A', 'C', 'C', 'D', 'E', 'E', 'A', 'D'],
      ['D', 'B', 'A', 'B', 'C', 'A', 'E', 'E', 'A', 'D'],
      ['E', 'D', 'D', 'A', 'C', 'B', 'E', 'E', 'A', 'D'],
      ['C', 'B', 'A', 'E', 'D', 'C', 'E', 'E', 'A', 'D'],
      ['A', 'B', 'D', 'C', 'C', 'D', 'E', 'E', 'A', 'D'],
      ['B', 'B', 'E', 'C', 'C', 'D', 'E', 'E', 'A', 'D'],
      ['B', 'B', 'A', 'C', 'C', 'D', 'E', 'E', 'A', 'D'],
      ['E', 'B', 'E', 'C', 'C', 'D', 'E', 'E', 'A', 'D']]

    # Key to the questions
    keys = ['D', 'B', 'D', 'C', 'C', 'D', 'A', 'E', 'A', 'D']
    correctCounts = len(answers) * [0]

    # Grade all answers
    for i in range(len(correctCounts)):
        # Grade one student
        for j in range(len(answers[i])):
            if answers[i][j] == keys[j]:
                correctCounts[i] += 1

    print("Max is", max(correctCounts))    
    print("Min is", min(correctCounts))    
    print("Mean is", sum(correctCounts) / len(correctCounts))
    print("Deviation is", deviation(correctCounts))
    
# Compute the deviation of values
def deviation(x):
    average = sum(x) / len(x)
    squareSum = 0

    for value in x:
        squareSum += (value - average) ** 2

    return sqrt(squareSum / (len(x) - 1))

main()
