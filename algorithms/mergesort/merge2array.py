'''
merge 2 sorted arrays
'''
arr1 = [2, 8, 15, 18]
arr2 = [5, 9, 12, 17, 20, 24]

def merge(arr1, arr2, m, n):
	i=0
	j=0
	k=0
	#new array declaration
	arr3 = [0]*(m+n)
	while(i < m and j < n):
		print(i,j,k)
		if arr1[i] > arr2[j]:
			
			arr3[k] = arr2[j]
			j+=1
			k+=1
		else:
			arr3[k] = arr1[i]
			i+=1
			k+=1
	for x in range(i,m):
		arr3[k]=arr1[x]
		k+=1
	for x in range(j,n):
		arr3[k]=arr2[x]
		k+=1
	return arr3		

print(merge(arr1, arr2, len(arr1), len(arr2)))

