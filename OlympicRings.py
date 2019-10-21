import turtle

turtle.hideturtle()
turtle.penup()
turtle.bk(300)
turtle.pendown()
p = turtle.pos()
colors=['blue','black','red','yellow','green']  
pos=[p, (p[0]+230, p[1]), (p[0]+460, p[1]), (p[0]+115, p[1]-100), (p[0]+345, p[1]-100)]

def ring(i):
    turtle.penup()
    turtle.goto(pos[i])
    turtle.pendown()

    turtle.color(colors[i])
    turtle.circle(100)

def OlympicsRings():
    turtle.pensize(10)
    for i in range(5):
        ring(i)

    turtle.exitonclick()

OlympicsRings()