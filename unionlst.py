def unionlist(lst1, lst2):
    lst = lst1

    for i in lst2:
        if i  not in lst2:
            lst.append(i)

    return(lst)
    
def main():
    lst1 = []
    lst2 = []
    lst1 = eval(input("Input List1 of Numbers: "))
    lst2 = eval(input("Input List2 of Numbers: "))
    print(lst1)
    print(lst2)
    lst = unionlist(lst1,lst2)
    print(lst)

main()