class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

def inOrderTraversal(root):
    if root:
        inOrderTraversal(root.left)
        print(root.data, end=' ')
        inOrderTraversal(root.right)

def preOrderTraversal(root):
    if root:
        print(root.data, end=' ')
        preOrderTraversal(root.left)
        
        preOrderTraversal(root.right)

def postOrderTraversal(root):
    if root:
        
        postOrderTraversal(root.left)
        
        postOrderTraversal(root.right)
        print(root.data, end=' ')

root = Node(1) 
root.left = Node(2) 
root.right = Node(3) 
root.left.left = Node(4) 
root.left.right = Node(5) 

preOrderTraversal(root)
print()
inOrderTraversal(root)
print()
postOrderTraversal(root)