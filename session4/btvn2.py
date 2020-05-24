from turtle import*
speed(0)
color('blue')
edge = 5
for i in range(40):
    for i in range(4):
        fd(edge)
        left(90)
    left(360/30)
    edge += 3
mainloop()