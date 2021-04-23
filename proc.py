s = input()
p = input()
#s = s[::-1]
t = ''
for c in s:
  t+=chr((ord(c)+5-ord('A'))%26 + ord('A'))
  

def removeSpaces(string): 
    string = string.replace(' ','') 
    string = string.replace(',','')
    return string.lower()
def check(t, p):
     
    # the sorted strings are checked 
    if(sorted(t)== sorted(p)):
        print("Yes",end='') 
    else:
        print("No",end='')         
         
check(t, p)