#doubly linked list data structure

class Node:
	def __init__(self, data):
		self.data = data
		self.prev = None
		self.next = None

class doubly_linked_list:
	def __init__(self):
		self.head = None
	
	#add new data node
	def add(self, data):
		node = Node(data)
		node.next = self.head
		if self.head is not None:
			self.head.prev = node
		self.head = node

	#traverse linked list
	def print(self,node):
		while(node is not None):
			print(node.data,"->", end="")
			node = node.next

	#insert new node at a position
	def insert(self, position, data):
		pos=1
		traverseNode = self.head
		if position == 1:
			self.add(data)
		newNode = Node(data)
		while(traverseNode.next is not None):
			if(pos==position-1):
				newNode.prev = traverseNode
				newNode.next = traverseNode.next
				newNode.next.prev = newNode
				newNode.prev.next = newNode
				break
			traverseNode = traverseNode.next
			pos+=1
		else:
			if(pos==position-1):
				traverseNode.next = newNode
				newNode.prev = traverseNode
			else: #pos>position:
				print("position does not exist")


	#appending a node
	def append(self, data):
		newNode = Node(data)
		if self.head == None:
			self.head = newNode
		node = self.head
		while(node.next is not None):
			node = node.next
		node.next = newNode
		newNode.prev = node

dll = doubly_linked_list()
dll.add(13)
#13
dll.add(156)
#156->13
dll.add(31)
#31->156->13
dll.add(92)
#92->13->156->13
dll.insert(6,44)
dll.print(dll.head)