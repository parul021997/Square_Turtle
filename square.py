import turtle as t
import random as r
kaddu=t.Turtle()
win=t.getscreen()
win.bgcolor("black")
win.title("My LOve")
kaddu.color("white")
kaddu.speed(0)
x=10
l=["red","white"]
while True:
    
    for i in range(50):
        r.shuffle(l)
        kaddu.color(l[0])
        kaddu.lt(90)
        kaddu.fd(x)
        x+=10

win.mainloop()    
    

