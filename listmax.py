lst = eval(input("Input List of Numbers: "))
lenlist = len(lst)

max1 = 0

for i in range (1,lenlist):
    num1 = lst[i -1]

    if  max1 > num1:
        max2 = max1
    else:
        max1 = num1

print(max2)