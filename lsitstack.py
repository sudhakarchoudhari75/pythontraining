def push(c_students,num2):
	c_students.append(num2)
	return(c_students)

def pop(c_students):
	num_std = c_students[0]
	c_students.remove(num_std)
	return (num_std)
	
def isfull(c_students):
	if len(c_students) == 10 :
		return(1)

def isempty(c_students):
	if len(c_students) == 0:
		return(1)

def main():
	c_students = []
    print(len(c_students))

	while (True):	
		print ("Usage : - Press '1' to push a number: ")
		print ("Usage : - Press '2' to pop: ")
		print ("Usage : - Press '3' to check if full: ")
		print ("Usage : - Press '4' to chcek if empty: ")
		print ("Usage : - Press '5' to exit: ")

		choice = eval(input("Input Your Choice (1 for push, 2 for pop, 3 for full, 4 for empty, 5 for exit): "))

		if choice == 1:
			if isfull(c_students) == 1:
				num_1 = eval(input("Input Number to push: "))			
				push(c_students,num_1)
				print(c_students)
			else:
				print("Stack is full!")
		elif choice == 2:
			if isempty(c_students) ==1:
				num_std = pop(c_students)
				print(num_std)
				print(c_students)
			else:
				print("Stack is empty!")
		elif choice == 3:
			if isfull(c_students) == 1:
				print("Stack is full!")
		elif choice == 4:
			if isfull(c_students,num1) == 1:
				print("Stack is full!")
		elif choice == 5:
			break

main()