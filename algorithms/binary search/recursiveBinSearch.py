def rBinSearch(arr, low, high, element):
	if low == high:
		if arr[low] == element:
			return low
		else:
			return 0
	else:
		mid = (low + high)//2
		if element == arr[mid]:
			return mid
		elif element > arr[mid]:
			return rBinSearch(arr, mid+1, high, element)
		else:
			return rBinSearch(arr, low, mid-1, element)

ans = rBinSearch([3,6,8,12,14,17,25,29,31,36,42,47,53,55,62], 0, 15, 17)
print(ans+1)
