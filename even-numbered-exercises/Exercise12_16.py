class Stack(list):
    def __init__(self):
        super().__init__()

    # Return true if the stack is empty
    def isEmpty(self):
        return len(self) == 0

    # Returns the element at the top of the stack
    # without removing it from the stack.
    def peek(self):
        if self.isEmpty():
            return None
        else:
            return self[len(self) - 1]

    # Stores an element into the top of the stack
    def push(self, value):
        self.append(value)

    # Removes the element at the top of the stack and returns it
    def pop(self):
        if self.isEmpty():
            return None
        else:
            temp = self[len(self) - 1]
            del self[len(self) - 1]
            return temp

    # Return the size of the stack
    def getSize(self):
        return len(self)


stack = Stack()
for i in range(5):
    s = input("Enter a string: ")
    stack.push(s)

while not stack.isEmpty():
    print(stack.pop())
