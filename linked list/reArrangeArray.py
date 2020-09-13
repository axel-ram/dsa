def rearrangeArray(arr):
	n = len(arr)
	res = [-1]*n
	
	for i in range(n):
		if arr[i] >-1 and arr[i] <n:
			res[arr[i]] = arr[i]
	return res
def rearrangeArray2(arr):
	n = len(arr)
	j = k = 0
	for i in range(n):
		if arr[i] != -1 and arr[i] != i:
			x = arr[i]
			while(arr[x] != -1 and arr[x]!= x):
				arr[x], x = x, arr[x]
			arr[x] = x
			if arr[i] != i:
				arr[i] = -1






arr = [-1, -1, 6, 1, 9, 3, 2, -1, 4, -1]
print(rearrangeArray(arr))
print(rearrangeArray2(arr))
print(arr)
print(rearrangeArray([19, 7, 0, 3, 18, 15, 12, 6, 1, 8, 11, 10, 9, 5, 13, 16, 2, 14, 17, 4]))