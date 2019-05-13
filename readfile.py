import io

f = input("Enter File Name :- ")
fd = io.FileIO(f)

line = fd.readline()
minline = len(line))

while line != b'':    
    if minline > maxline:
        print(line)
        line = fd.readline()    
        