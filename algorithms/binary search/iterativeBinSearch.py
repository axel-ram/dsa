def binarySearch(arr, element):
	low, high = 0, len(arr)
	while(low <= high):
		mid = (low + high)//2
		if element == arr[mid]:
			return mid
		elif element > arr[mid]:
			low = mid + 1
		else:
			high = mid - 1
			
	return 0
	

ans = binarySearch([3,6,8,12,14,17,25,29,31,36,42,47,53,55,62], 17)
print(ans+1)
	
