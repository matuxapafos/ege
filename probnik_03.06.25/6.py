from turtle import *

tracer(0)
for i in range(10):
    fd(10*10)
    rt(45)

up()
for x in range(-30,30):
    for y in range(-30,30):
        goto(x*10,y*10)
        dot(5)

update()
exitonclick()