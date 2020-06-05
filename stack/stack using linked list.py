class StackNode:
	def __init__(self,data):
		self.data=data
		self.next=None

class Stack:
	def __init__(self):
		self.root = None

	def isEmpty(self):
		return True if self.root is None else False

	def push(self,data):
		newNode = StackNode(data)
		newNode.next=self.root
		newNode.data = data
		self.root=newNode
		print(data,"pushed")

	def pop(self):
		if (self.isEmpty()):
			return -1
		temp=self.root
		self.root=self.root.next
		popped=temp.data
		return popped

	def peek(self):
		if(self.isEmpty()):
			return -1

		return self.root.data

stack=Stack()
stack.push(10)
stack.push(20)
stack.push(30)

print(stack.pop())
print(stack.peek())