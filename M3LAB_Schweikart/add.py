def add(num1,num2):
	"""
	>>> square(2)
	4
	>>> square(-2)
	4
	>>> square(-1)
	1
	"""
	return num1+num2
	
if __name__ == '__main__':
	import doctest
	print("Running test for square()")
	doctest.testmod()