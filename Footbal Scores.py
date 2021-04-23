c=int(0)
a = []
b = []
n = int(input("NO. of elements in A"))
for i in range(n):
    score_a = int(input("Score of A"))
    a.append(score_a)
q = int(input("no. of elements in B"))
for j in range(q):
    score_b = int(input("Score of B"))
    b.append(score_b)
for z in range(0,len(b)):
    if(b[z]<=a[z]):
        c=c+1
        print(c)

