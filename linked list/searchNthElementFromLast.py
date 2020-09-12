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
	def searchNthElementFromLast(self, n):
		current = self.head
		if current == None:
			return -1
		cnt = 0
		while(current):
			current = current.next
			cnt += 1
		if n>cnt:
			return -1
		current = self.head
		for i in range(0, cnt-n):
			current = current.next
		return current.data
	def nthElementFromLast(self, n):
		mainElement = None
		current = self.head
		cnt = 0
		while(current):
			cnt += 1
			if cnt==1:
				mainElement = current
			elif cnt>n:
				mainElement = mainElement.next
			
				
			current = current.next
		return mainElement.data


llist = LinkedList() 
llist.push(10); 
llist.push(30); 
llist.push(11); 
llist.push(21); 
llist.push(14); 
print(llist.searchNthElementFromLast(4))
print(llist.nthElementFromLast(2))