def mergesort(A, l, h):
	# [1] check if l > h
	# [2] if no then divide the array in half
	# [3] find mid
	# [4] run two hald merge sort func calls
	# [5] after this run merge func to merge sorted array
	if l < h:
		mid = (l+h)//2
		mergesort(A, l, mid)
		mergesort(A, mid+1, h)
		merge(A, l, mid, h)
	
	
def merge(arr,l,m,h):
	print(l,m,h)
	arr1 = arr[l:m+1]
	arr2 = arr[m+1:h+1]
	n1 = m+1-l
	n2 = h-m
	print(n1,n2,arr1,arr2	)
	i = j = 0
	k = l
	while i < n1 and j < n2:
		if arr1[i] < arr2[j]:
			arr[k] = arr1[i]
			i+=1
		else:
			arr[k] = arr2[j]
			j+=1
		k+=1
	while i < n1:
		arr[k] = arr1[i]
		i+=1
		k+=1
	while j < n2:
		arr[k] = arr2[j]
		j+=1
	
arr = [9,3,7,5,6,4,8,2]
mergesort(arr, 0, len(arr)-1)
print(arr)
