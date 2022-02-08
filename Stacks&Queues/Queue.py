# Creating a queue from an array is very inefficient as we have to move the indexes of all the items when enqueue and dequeue operations are performed

# So we will just perform Queue Implementation using Linked List


# Node class
class Node():
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue():
    def __init__(self):
        self.first = None
        self.last = None
        self.length = 0

    # First element of the Queue
    def Peek(self):
        if self.length == 0:
            return(None)
        else:
            return(self.first)

    def Enqueue(self, value):
        newNode = Node(value)
        if self.length == 0:
            self.first = newNode
            self.last = newNode
            self.length += 1
        else:
            self.last.next = newNode
            self.last = newNode
            self.length += 1

    def Dequeue(self):
        if self.length == 0:
            return(None)
        elif self.length == 1:
            self.last = None
        else:
            self.first = self.first.next
            self.length -= 1

q = Queue()

q.Enqueue("abc")
q.Enqueue("google")
q.Enqueue("twitter")
q.Enqueue("uw")
