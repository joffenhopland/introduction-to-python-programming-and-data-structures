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

    counts = []
    for j in range(10): 
        counts.append(5 * [0])
        
    # Count A's, B's, C's, D's, and E's for each answer
    for i in range(len(answers)):
        for j in range(len(answers[i])): 
            counts[j][ord(answers[i][j]) - ord('A')] += 1

    for j in range(10):
        print("\nFor question #" + str(j + 1))
        for k in range(5): 
            print("Percentage of", chr(ord('A') + k), " is: ", str(counts[j][k] * 100 / 8.0) + '%')
            
main()