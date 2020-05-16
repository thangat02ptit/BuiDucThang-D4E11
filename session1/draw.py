from turtle import*
shape("turtle")
speed(-1)
color("green","red")
n = int(input())
for i in range(n):
    fd(100)
    left(360/n)
mainloop()