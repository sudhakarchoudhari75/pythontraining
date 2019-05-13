def addnum(a, b , c = 0, d = 0, e = 0):
	return a + b + c + d + e

if __name__=='__main__':
	no1 = eval(input("Input No 1: "))
	no2 = eval(input("Input No 2: "))
	no3 = eval(input("Input No 3: "))
	no4 = eval(input("Input No 4: "))
	no5 = eval(input("Input No 5: "))
	x = addnum(no1, no2, no3, no4, no5)
	print (x)
