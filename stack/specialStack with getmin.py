class Stack:
	def __init__(self):
		self.s1=[]
		self.s2=[]

	def push(self,data):
		if(len(self.s1)==0):
			self.s2.append(data)
			self.s1.append(data)

		else:
			if(data<self.s2[-1]):
				self.s2.append(data)
				self.s1.append(data)				
			else:
				self.s2.append(self.s2[-1])
				self.s1.append(data)

	def pop(self):
		if(len(self.s1)!=0):
			self.s2.pop()
			return self.s1.pop()
		return -1

	def getMin(self):
		return self.s2[-1]

	def printStack(self):
		print('s1',self.s1)
		print('s2',self.s2)
if __name__=='__main__':
	s=Stack()
	s.push(18)
	print('min is',s.getMin())
	s.push(19)
	print('min is',s.getMin())
	s.push(29)
	print('min is',s.getMin())

	s.push(15)
	print('min is',s.getMin())
	s.push(16)

	s.printStack()

	print('min is',s.getMin())
	print(s.pop())
	print('min is',s.getMin())
	print(s.pop())
	print('min is',s.getMin())
	print(s.pop())
	print('min is',s.getMin())
	s.printStack()



