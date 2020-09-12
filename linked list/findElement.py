class Node:
	def __init__(self, data):
		self.data = data
		self.next = None

class LinkedList:
	def __init__(self):
		self.head = None
	def push(self, data):
		new = Node(data)
		new.next = self.head
		self.head = new
	def search(self, key):
		li = self.head
		if li==None:
			return False
		while(li):
			if li.data == key:
				return True
			li = li.next
		return False
	def recursiveSearch(self, node, key):
		if node==None:
			return False
		if node.data == key:
			return True
		else:
			return self.recursiveSearch(node.next, key) 

llist = LinkedList() 
llist.push(10); 
llist.push(30); 
llist.push(11); 
llist.push(21); 
llist.push(14); 
print(llist.search(11))
print(llist.recursiveSearch(llist.head, 14))
llist2 = LinkedList()
print(llist2.search(11))