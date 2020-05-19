sheepsize = [5,7,300,90,24,50,75]
print(sheepsize)
print("now my biggest sheep has size",max(sheepsize),"let's shear it")
sheepsize[sheepsize.index(max(sheepsize))] = 8
print("after shearing, here is my flock")
print(sheepsize)
for j in range(1,4):
    print("MONTH ",j)
    for i in range(len(sheepsize)):
        sheepsize[i]+=50
    print("one month has pass, now here is my flock")
    print(sheepsize)
    print("now my biggest sheep has size",max(sheepsize),"let's shear it")
    sheepsize[sheepsize.index(max(sheepsize))] = 8
    print("after shearing, here is my flock")
    print(sheepsize)
total = 0
for i in range(len(sheepsize)):
    total+=sheepsize[i]
print("my flock has size in total:",total)
print("i would get",total,"* 2$ =",total*2,"$")
    