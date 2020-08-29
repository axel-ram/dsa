def fib(n):
	dict1 = dict()
	for k in range(n+1):
		if k<=2: dict1[k]=1
		else: dict1[k] = dict1[k-1]+dict1[k-2]
	
	return dict1[n]

print(fib(100000))
