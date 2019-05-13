def addnum(num1,num2):
	return (num1+num2)

def subnum(num1,num2):
	return (num1-num2)

def multnum(num1,num2):
	return (num1*num2)

def divnum(num1,num2):
	return (num1 / num2)

while (True):
    print ("Usage : - Press 'a' to add two numbers: ")
    print ("Usage : - Press 's' to substract two numbers: ")
    print ("Usage : - Press 'm' to multiply two numbers: ")
    print ("Usage : - Press 'd' to divide two numbers: ")
    print ("Usage : - Press 'x' to exit: ")

    choice = eval(input("Input Your Choice (a for add, s for substract, m for multplication, d for division, x for exit): "))

    if choice == "a":
        num_1 = eval(input("Input Number 1 : "))
        num_2 = eval(input("Input Number 2 : "))
        print(addnum(num_1,num_2))
    elif choice == "s":
        num_1 = eval(input("Input Number 1 : "))
        num_2 = eval(input("Input Number 2 : "))        
        print(subnum(num_1,num_2))
    elif choice == "m":
        num_1 = eval(input("Input Number 1 : "))
        num_2 = eval(input("Input Number 2 : "))        
        print(multnum(num_1,num_2))
    elif choice == "d":
        num_1 = eval(input("Input Number 1 : "))
        num_2 = eval(input("Input Number 2 : "))        
        print(divnum(num_1,num_2))
    elif choice == "x":
        break