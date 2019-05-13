def turnOffbits(num, pos, numbits):
        num1 = (2**numbits) - 1
        num2 = num1 << (pos - numbits)
        num3 = ~num2

        answer = num & num3
        return (answer)

def turnOnbits(num, pos, numbits):
        num1 = (2**numbits) - 1
        num2 = num1 << (pos - numbits)
        
        answer = num | num2
        return (answer)

def togglebits(num, pos, numbits):
        num1 = (2**numbits) - 1
        num2 = num1 << (pos - numbits)
        
        answer = num ^ num2
        return (answer)


no1 = eval(input("Input No : "))
pos1 = eval(input("Position to toggle from : "))
bitstog = eval(input("Bits to toggle : "))

ans1 = turnOffbits(no1, pos1, bitstog)
ans2 = turnOnbits(no1, pos1, bitstog)
ans3 = togglebits(no1, pos1, bitstog)

print (ans1)
print (ans2)
print (ans3)