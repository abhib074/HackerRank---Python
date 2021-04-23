w_cash = float(input())
a_bal = float(input())
c=1
#while(c>0):
if(w_cash%5==0 and w_cash<a_bal):
    rate = c*0.5   
    c=c+1
print(a_bal-w_cash-rate)

