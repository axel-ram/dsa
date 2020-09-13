def maxSumByRotation(arr):
	j = 0
	n = len(arr)
	arrSum = sum(arr)
	
	tempSum = 0
	for i, a in enumerate(arr):
		tempSum += i*arr[i]
	res = tempSum

	for j in range(1, n):
		tempSum += arrSum - n*arr[n-j]
		res = max(res, tempSum)
	return res

arr = [10, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(maxSumByRotation(arr))