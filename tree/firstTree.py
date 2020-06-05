class Node:
	def __init__(self,key):
		self.lift = None;
		self.right = None;
		self.val = key


root = Node(1)

root.left = Node(2)
root.right = Node(3)

root.left.left = Node(4)
