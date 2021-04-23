cpy = []
for i in range(int(input())):
    cmnd = input().split()
    for i in range(1,len(cmnd)):
        cmnd[i] = int(cmnd[i])
        
    if (cmnd[0] == "append"):
        cpy.append(cmnd[1])
    elif (cmnd[0] == "insert"):
        cpy.insert(cmnd[1], cmnd[2])
    elif (cmnd[0] == "remove"):
        cpy.remove(cmnd[1])
    elif (cmnd[0] == "sort"):
        cpy.sort()
    elif (cmnd[0] == "pop"):
        cpy.pop()
    elif (cmnd[0] == "reverse"):
        cpy.reverse()
    elif (cmnd[0] == "print"):
        print(cpy)