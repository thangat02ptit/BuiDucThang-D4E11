from turtle import*
n = int(input("enter your number:"))
shape("turtle")
color("red","yellow")
for i in range(3,n+1):
    for j in range(i):
        fd(100)
        lt(360/i)
mainloop()