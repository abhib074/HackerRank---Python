n, k = input().split()
bill = input().split()
b = int(input())
ibill = []
for i in bill:
    ele=int(i)
    ibill.append(ele)
actual = sum(ibill)
ac = actual/len(ibill)
if(b>=ac):
    print(b-ac)
else:
    print("Hi")