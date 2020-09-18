class Node:
	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None
def inorderTraverse(root):
	if root:
		inorderTraverse(root.left)
		print(root.data, end=' ')
		inorderTraverse(root.right)

def deletion(root, delNode):
	current = root
	queue = []
	queue.append(current)
	while(len(queue)):
		current = queue.pop(0)
		if current.left == delNode:
			current.left = None
		if current.right == delNode:
			current.right = None
		if current.left:
			queue.append(current.left)
		if current.right:
			queue.append(current.right)


def bfs(root, data):
	if root is None:
		return None
	if root.left == None and root.right == None:
		if root.data == data:
			return None
		else:
			return root
	current = root
	queue = []
	queue.append(current)
	temp = None
	while(len(queue)):
		current = queue.pop(0)
		if current.data == data:
			temp = current
		if current.left:
			queue.append(current.left)
		if current.right:
			queue.append(current.right)
	

	temp.data = current.data
	deletion(root, current)

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)

inorderTraverse(root)
print()
bfs(root, 2)
inorderTraverse(root)