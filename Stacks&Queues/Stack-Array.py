# Stack Array Implementation

class Stack():
    def __init__(self):
        self.arr = []

    # Peek
    def peek(self):
        return(self.arr[len(self.arr)-1])

    # Push
    def push(self, value):
        self.arr.append(value)

    def isEmpty(self):
        if len(self.arr) == 0:
            return(True)
        else:
            return(False)

    def pop(self):
        if self.isEmpty():
            return("Stack is empty")
        else:
            return(self.arr.pop())

stack = Stack()

stack.push("google")
stack.push("uw")
stack.push("linkedin")
stack.push("ig")

stack.pop()

print(stack.arr)

print(stack.peek())
