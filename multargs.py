def add(*args):
	print(type(args))
	sum=0
	for x in args:
		sum += x
	return sum


a = add(10,20,30,40)
print(a)
