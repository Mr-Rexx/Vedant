import turtle
import colorsys
t=turtle.Turtle()
turtle.bgbolor('black')
turtle.tracer(14)
t.pensize(4)

def F():
    t.up()
    t.goto(9,0)
    t.down()
    h=0
    n=78
    for i in range(460):
        c=colorsys.hsv_to_rgb(h,1,1)
        h+=1/n
        t.color(c)
        t.fillcolor("black")
        t.begin_fill()
        t.rt(56)
        t.fd(i)
        t.circle(-24)
        t.end_fill()
        t.circle(23,5.1)

F()
turtle.done        


 