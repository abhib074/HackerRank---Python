l={}
for _ in range(int(input())):
    name = input()
    score = float(input())
    l.update({name:score})
    
slist=sorted(l.values())
#print(slist)
for i in range(0,len(slist)):
    if(i==0): 
        minval=slist[i]
    elif(slist[i]>minval):
        minval=slist[i]
        #print(minval)
        break
#print(l)
for k in sorted(l.keys()):
    if(l[k]==minval):
        print(k)