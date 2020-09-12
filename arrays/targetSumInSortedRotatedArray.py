def findPivot(arr, l, r):
	if l > r:
		return -1
	if l==r:
		return l

	mid = l + (r-l)//2
	if mid < r and arr[mid] > arr[mid+1]:
		return mid
	if mid > l and arr[mid-1] > arr[mid]:
		return mid-1
	if arr[l] >= arr[mid]:
		return findPivot(arr, l, mid-1)
	return findPivot(arr, mid+1, r)
def findPair(arr, target):
	n = len(arr)
	pivot = findPivot(arr, 0, n-1)
	l = pivot+1
	h = pivot
	while(l!=h):
		if arr[l]+arr[h] == target:
			return [l,h]
		elif arr[l]+arr[h] > target:
			h = (h-1) % n
		else:
			l = (l+1) % n
	return -1

arr = [11, 15, 26, 38, 9, 10]
target = 35
print(findPair(arr, target))