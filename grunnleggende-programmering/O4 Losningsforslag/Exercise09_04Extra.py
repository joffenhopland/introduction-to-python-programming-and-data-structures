def main():
    board1 = EQ()
    board1.set(0, 2)
    board1.set(1, 4)
    board1.set(2, 7)
    board1.set(3, 1)
    board1.set(4, 0)
    board1.set(5, 3)
    board1.set(6, 6)
    board1.set(7, 5)
    print("Is board1 a correct eight queen placement?", 
        board1.isSolved())

    board2 = EQ([0, 4, 7, 5, 2, 6, 1, 3])
    if board2.isSolved():
        print("Eight queens are placed correctly in board2")
        board2.printBoard()
    else:
        print("Eight queens are placed incorrectly in board2")

class EQ:
    def __init__(self, queens = 8 * [-1]):
        self.queens = queens

    def get(self, i):
        return self.queens[i]

    def set(self, i, j):
        self.queens[i] = j

    def isSolved(self):
        for i in range(len(self.queens)):
            if not self.isValid(i, self.queens[i]):
                return False
        return True

    def printBoard(self):
        for i in range(len(self.queens)):
            for k in range(self.queens[i]):
                print("| ", end = "")
            print("|X", end = "")
            for k in range(self.queens[i] + 1, len(self.queens) + 1):
                print("| ", end = "")
            print()  

    # Return true if a queen can be placed at (row, column) 
    def isValid(self, row, column):
        for i in range(1, row + 1, 1):
            if (self.queens[row - i] == column # Check column
                or self.queens[row - i] == column - i # Check upleft diagonal
                or self.queens[row - i] == column + i): # Check upright diagonal
                return False #/ There is a conflict
        return True # No conflict
    
main()