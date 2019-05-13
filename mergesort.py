def sortlist(lst):
    for passnum in range(len(lst)-1,0,-1):
        for i in range(passnum):
            if lst[i] > lst[i+1]:
                temp = lst[i]
                lst[i] = lst[i+1]
                lst[i+1] = temp

    return(lst)
    
def main():
    lst = []
    lst1 = []
    lst = eval(input("Input List1 of Numbers: "))
    lst1 = eval(input("Input List2 of Numbers: "))
    print(lst)
    print(lst1)
    lst = sortlist(sortlist(lst) + sortlist(lst1))
    print(lst)

main()