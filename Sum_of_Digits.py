n = int(input())
while(n>0):
    num = int(input())
    sum = 0
    div = 0
    while(num != 0):
        div = num%10
        sum=sum+div
        num=num//10
    print(sum)
    n=n-1