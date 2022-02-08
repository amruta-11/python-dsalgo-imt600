# Stack LinkedList Implementation

# Node class
class Node():
    def __init__(self, data):
        self.data = data
        self.next = None

class StackLL():
    def __init__(self):
        self.top = None
        self.bottom = None
        self.length = 0

    def peek(self):
        return(self.top)

    def push(self, value):
        newNode = Node(value)
        if self.length == 0:
            self.bottom = newNode
            self.top = newNode
            self.length += 1
        else:
            temp = self.top
            self.top = newNode
            self.top.next = temp
            self.length += 1
        return(self)

    def isEmpty(self):
        if self.length == 0:
            return(True)
        else:
            return(False)


    def pop(self):
        if self.isEmpty():
            return("Stack is empty")
        else:
            self.top = self.top.next
            self.length -= 1


    def printList(self):
        if self.top == None:
            print("Stack is empty")
        else:
            temp = self.top
            while(temp):
                print(temp.data)
                temp = temp.next


stack = StackLL()

stack.push("google")
stack.push("twitter")
stack.push("ztom")
stack.push("udemy")
stack.push("uw")


stack.pop()

stack.printList()
