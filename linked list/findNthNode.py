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

	def findNthNode(self,index):
		current = self.head
		i=0
		
		while(current!=None):
			if i == index :
				return current.data
			current = current.next
			i += 1
		return -1

llist = LinkedList() 
llist.push(10); 
llist.push(30); 
llist.push(11); 
llist.push(21); 
llist.push(14); 
print(llist.findNthNode(1))