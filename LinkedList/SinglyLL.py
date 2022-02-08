
# Linked List is a collection of nodes.
# Nodes hold two properties - the data and reference to the next node, so first creating the node class and using it in Linked List class
# Node class
class Node():
    def __init__(self, data):
        self.data = data
        self.next = None

# LL has a head (first element) and the tail (last element) properties.
# The methods that a linked List can have include append, insert, prepend, print, delete, etc
# Linked List Class
class LinkedList():
    def __init__(self):
        self.head = None
        self.tail = self.head

    # Method - Append
    def append(self, data):
        newNode = Node(data)
        if self.head == None:
            self.head = newNode
            self.tail = self.head
        else:
            self.tail.next = newNode
            self.tail = newNode

    # Method - Prepend
    def prepend(self, data):
        newNode = Node(data)
        if self.head == None:
            self.head == newNode
            self.tail == newNode
        else:
            temp = self.head
            self.head = newNode
            self.head.next = temp

    # Method - Insert
    def insert(self, index, value):
        newNode = Node(value)
        if index == 0:
            temp = self.head
            self.head = newNode
            newNode.next = temp
        else:
            counter = 0
            currentNode = self.head
            while(counter != index-1):
                currentNode = currentNode.next
                counter += 1
            temp = currentNode.next
            currentNode.next = newNode
            newNode.next = temp

    # Method - Remove at index
    def removeAtIndex(self, index):
        if index == 0:
            self.head = self.head.next
        else:
            counter = 0
            previous = self.head
            while(counter != index-1):
                previous = previous.next
                counter += 1

            deleteNode = previous.next
            previous.next = deleteNode.next

    # Method - Reverse
    # 1 > 2 > 3 > 4 > 5
    # Very Important

    def reverseLL(self):
        if (!self.head.next):
            return(self.head)
        first = this.head
        second = first.next
        while(second):
            third = second.next
            second.next = first
            first = second
            second = third




    # Method - Print
    def printList(self):
        if self.head == None:
            print("LL is empty")
        else:
            temp = self.head
            while(temp != None):
                print(temp.data)
                temp = temp.next


l1 = LinkedList()

l1.append(5)
l1.append(10)
l1.append(15)

l1.prepend(1)
l1.prepend(-5)

# l1.insert(3, 100)

l1.removeAtIndex(3)
l1.removeAtIndex(0)

l1.printList()
