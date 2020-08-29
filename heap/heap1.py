#!user/bin/python3
parent = lambda n: n//2
lchild = lambda n: n*2
rchild = lambda n: n*2+1

maxheap = [50,30,20,15,10,8,16]
'''
[1] check with parent
[2] if parent bigger then swap
[3] update index and check again if parent is bigger
[3] if not end loop
'''
def insert(heap, element):
	#time talen is O(log n)
	heap.append(element)
	index = len(heap)-1
	parent = lambda i: (i-1)//2
	lc = lambda i: 2*i+1
	rc = lambda i: 2*i+2
	while(index != 0):
		print(index)
		if heap[index] > heap[parent(index)]:
			heap[index], heap[parent(index)] = heap[parent(index)],heap[index]
			index = parent(index)
		else:
			break

def delete(heap, n):
	'''
	[1] swap root with last element
	[2] push down the element
	[3] if children bigger
	[4] 	right children bigger then swap with it
	[5] 	left child is bigger then swap with it
	[6] 	if no one bigger then return last element

	'''
	parent = lambda i: (i-1)//2
	lc = lambda i: 2*i+1
	rc = lambda i: 2*i+2
	heap[0], heap[n-1] = heap[n-1], heap[0]
	n -= 1
	index=0

	while(True):
		if heap[lc(index)] > heap[rc(index)]:
			childValue = heap[lc(index)]
			childIndex = lc(index)
		else:
			childValue = heap[rc(index)]
			childIndex = rc(index)
		if childValue > heap[index]:
			heap[index], heap[childIndex] = heap[childIndex], heap[index]
			index = childIndex
		else:
			break
		if rc(index) >= n or lc(index) >= n:
			break
	print(n)
	return heap[n]


	    
insert(maxheap, 60)
print(maxheap)
print(len(maxheap))
# print(delete(maxheap, 8))
# print(maxheap)
# print(delete(maxheap, 7))
# print(maxheap)
# print(delete(maxheap, 6))
# print(maxheap)
for i in range(len(maxheap)):
	print(delete(maxheap, len(maxheap)-i))
	print(maxheap)


