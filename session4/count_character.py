c = input("enter a sentece: ")
count = {}
for i in c:
    if i in count:
        count[i] +=1
    else:
        count[i] = 1
sorted(count)
for i in count:
    if count[i] > 0:
        print(i,count[i])


