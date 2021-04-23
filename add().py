user = []
n = int(input())
for i in range(n):
   country = input()
   user.append(country)
s = set(user)
len_s = len(s)
print(len_s)