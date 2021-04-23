l = []
k=[]
n = int(input())
for i in range(0,n):
    a = int(input())
    l.append(a)
    if l[i]==0:
        k.append(l[i])
        continue
    elif l[i]==1:
        k.append(l[i])
        continue
    elif l[i]==2:
        k.append(l[i])
        continue
print(k)