"""
	Creating stack
	push O(1)
	pop O(1)
"""

class Stack (object):

	def __init__(self):
		self.items = []
		
	def isEmpty(self):
		return not bool(self.items)
	
	def push(self, value):
		self.items.append(value)
		
	def pop(self):
		value = self.items.pop()
		if value:
			return	value
		else:
			print("stack is Empty")
	
	def size(self):
		return len(self.items)
	
	def peek(self):
		if self.items:
			return self.items[-1]
		else:
			return 'Stack is empty'

	def __repr__(self):
		return '{}'.format(self.items)

if __name__ == '__main__':
	stack = Stack()
	print('Stack is empty?', stack.isEmpty())
	# adding table of 2
	for i in range(2,21,2):
		stack.push(i)
	print('Stack Size',stack.size())
	print('Stack Peek',stack.peek())
	print('Pop  ', stack.pop())
	print('Stack Peek',stack.peek())
	print(stack)






