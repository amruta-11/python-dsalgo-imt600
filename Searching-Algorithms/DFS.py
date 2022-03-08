# Tree Node class
class Node():
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

def dfsTraversal(root: Node):
    if root == None:
        return[]
    
    l = []    
    l+=dfsTraversal(root.left)
    l.append(root.value)
    l+=dfsTraversal(root.right)
    return(l)


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

bst = BinarySearchTree()
bst.insert(10)
bst.insert(14)
bst.insert(16)
bst.insert(8)
bst.insert(9)
bst.insert(5)

print(dfsTraversal(bst.root))