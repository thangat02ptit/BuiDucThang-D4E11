def fibo(n):
    if n==0:
        return 1
    if n==1:
        return 1
    if n>1: 
        return (fibo(n-1) + fibo(n-2))
for i in range(5):
    print('month',i,':',fibo(i+1),'pair(s) of rabbit')