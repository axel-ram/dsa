def rearrangePosNeg(arr):
	'''
	first split array in pos and neg using pivot point
	lets say pivot number is 0
	i=0
	while(j<n){
		if j<0:
			swap(arr[i], arr[j])
			i += 1
		j+=1
	}
	'''
	n = len(arr)
	pivot = 0
	i=j=0
	while(j<n):
		if arr[j]<0:
			arr[i], arr[j] = arr[j], arr[i]
			i+=1
		j+=1
	'''
	start with neg and positive numbers indexes
	swap alternate neg with positive till all pos or neg are not consumed
	increase pos with 1
	increase neg with 2
	'''
	pos = i
	neg = 0

	while(pos<n and neg<pos and arr[neg] <0):
		arr[neg], arr[pos] = arr[pos], arr[neg]
		neg+=2
		pos+=1
	print(arr)

arr = [-1, 2, -3, 4, 5, 6, -7, 8, 9]
rearrangePosNeg(arr)
rearrangePosNeg([0, 0, 1, -1])