x = eval(input ("Enter x: "))

for num in range(2,x):
	if num >= 1:
		for i in range(2,num):
			if ( num % i == 0 ):
				break
		else:
			print ( num )
