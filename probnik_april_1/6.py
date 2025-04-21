from turtle import *

screensize(5000,5000)
tracer = 0
k = 20
goto(0,0)
rt(315)
for i in range(7):
    fd(12*k)
    rt(45)
    fd(6*k)
    rt(135)

up()
for x in range(-10000,10000):
    for y in range(-10000,10000):
        goto(x*k,y*k)
        dot(4)

update()
exitonclick()