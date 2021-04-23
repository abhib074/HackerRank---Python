n = int(input())
for i in range(n):
    string = input()
    if(string[i]==string[i+1]):
        print("good")
    else:
        print("bad")