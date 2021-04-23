rows = int(input())
for i in range(1,rows,2): 
    print((i * ".|.").center(rows*3, "-"))
print("WELCOME".center(rows*3,"-"))
for i in range(rows-2,0,-2): 
    print((i * ".|.").center(rows*3, "-"))