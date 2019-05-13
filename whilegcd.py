x = eval(input ("Enter x: "))
y = eval(input ("Enter y: "))

while (x != y):
	if ( x > y):
		x = x - y;
	else:
		y = y - x
print (x)
