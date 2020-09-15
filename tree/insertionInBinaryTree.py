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

def insertion(root, data):
    queue = []
    current = root
    queue.append(current)
    while(len(queue)):
        current = queue[0]
        queue.pop(0)
        if current.left is None:
            current.left = Node(data)
            break
        else:
            queue.append(current.left)
            
        
        if current.right is None:
            current.right = Node(data)
            break
        else:
            queue.append(current.right)

'''
        1
       / \
      2   3
     / \
    4   5
    queue = 4,5,6
'''
root = Node(1) 
root.left = Node(2) 
root.right = Node(3) 
root.left.left = Node(4) 
root.left.right = Node(5) 
inOrderTraversal(root)
print()
insertion(root, 6)
inOrderTraversal(root)

