dict1 = dict()
def fib(n):

	if n in dict1:
		return dict1[n]
		
	if n <= 2:
		f = 1
	else:
		f = fib(n-1) + fib(n-2)
	dict1[n] = f
	return f
print(fib(100))
