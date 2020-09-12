'''
1. given sorted and rotated array
2. find the element
Approach - 
	[1] Find the pivot element whose next element is less
	[2] Divide array in 2 parts and apply binary search for the target number on divided 
	    individual arrays.
'''
def binarySearch(arr, l, r, target):
	if l > r:
		return -1
	mid = l + (r-l)//2
	if target == arr[mid]:
		# print(mid)
		return mid
	if target > arr[mid]:
		# print(target, arr[mid])
		return binarySearch(arr, (mid+1), r, target)
	
	return binarySearch(arr, l, (mid-1), target)


def findPivot(arr, l, r):
	#base case
	if r < l:
		return -1
	if l == r:
		return l
	
	mid = l+(r-l)//2
	if mid < r and arr[mid] > arr[mid+1]:
		return mid
	if mid > l and arr[mid] < arr[mid-1]:
		return mid-1
	if arr[l] >= arr[mid]:
		return findPivot(arr, l, mid-1)
	return findPivot(arr, mid+1, r)

def findInSortedRotatedArray(arr, target):
	n = len(arr)
	pivot = findPivot(arr, 0, n-1)
	# print(pivot)
	if pivot == -1:
		binarySearch(arr, 0, n-1, target)
	if arr[pivot] == target:
		return pivot
	if arr[0] <= target:
		return binarySearch(arr, 0, pivot-1,target)

	return binarySearch(arr, pivot+1, n-1, target)

arr = [3,1,2]
target = 2

print(findInSortedRotatedArray(arr, target))