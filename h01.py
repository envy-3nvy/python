import turtle

#liigu kuhugi
turtle.penup()
turtle.goto(-400,200)
turtle.pendown()
#kolmnurk
for i in range(3): #tsükkel 3x
    turtle.fd(200)
    turtle.lt(120)
#liigu palun konn
turtle.penup()
turtle.goto(0,0)
turtle.pendown()
#ruut
for i in range(4):
    turtle.fd(150)
    turtle.lt(90)

turtle.penup()
turtle.goto(200,-200)
turtle.pendown()
#A täht
turtle.fd(130)
turtle.rt(45)
turtle.fd(50)
turtle.bk(150)
turtle.rt(85)
turtle.fd(150)


turtle.done()