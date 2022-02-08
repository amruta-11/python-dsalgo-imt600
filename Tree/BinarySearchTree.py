# Creating a binary search tree

# Tree Node class
class Node():
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

class BinarySearchTree():
    def __init__(self):
        self.root = None

    # Method - Insert
    def insert(self, value):
        newNode = Node(value)

        if self.root == None:
            self.root = newNode
        else:
            currentNode = self.root
            while(True):
                if value < currentNode.value:
                    if(not currentNode.left):
                        currentNode.left = newNode
                        break
                    currentNode = currentNode.left
                else:
                    if(not currentNode.right):
                        currentNode.right = newNode
                        break
                    currentNode = currentNode.right

    # Method - Lookup
    def lookup(self, value):
        if self.root == None:
            return False
        else:
            currentNode = self.root
            while(currentNode):
                if value < currentNode.value:
                    currentNode = currentNode.left
                elif value > currentNode.value:
                    currentNode = currentNode.right
                elif currentNode.value == value:
                    return True
        return False

    # Method - Remove


bst = BinarySearchTree()

bst.insert(10)
bst.insert(14)
bst.insert(16)
bst.insert(8)
bst.insert(5)

print(bst.lookup())
