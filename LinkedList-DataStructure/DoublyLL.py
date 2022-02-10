class Node():
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList():
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
            newNode.prev = self.tail
            self.tail.next = newNode
            self.tail = newNode

    # Method - Print
    def printList(self):
        if self.head == None:
            print("DLL is empty")
        else:
            temp = self.head
            while(temp != None):
                print(temp.data)
                temp = temp.next


dll = DoublyLinkedList()

dll.append(10)
dll.append(20)
dll.append(-5)
dll.append(7)
dll.append(19)

dll.printList()
