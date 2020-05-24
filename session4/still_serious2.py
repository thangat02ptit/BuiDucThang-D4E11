number = [1,2,3,4,1,2,3,5,1,5,8]
#with using count()
n = int(input("enter a number: "))
print(n,'appears',number.count(n),'time in my list')
#without using count()
kount = 0
for i in number:
    if n == i:
        kount+=1
print(n,'appears',kount,'time in my list')