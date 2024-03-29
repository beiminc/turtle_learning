import turtle

t = turtle.Turtle()
t.hideturtle()

def start_point():
    t.penup()
    t.goto(-100, 200)
    t.pendown()
    t.speed(0)

def draw_body():
    t.pensize(5)
    t.left(180)
    t.color('black', 'yellow')
    t.begin_fill()
    for i in range(2):
        t.circle(50, 90)
        t.fd(200)
        t.circle(50, 90)
        t.fd(70)
    t.end_fill()

def draw_eyes():


    t.pensize(20)
    t.fd(10)
    t.right(90)
    t.pensize(5)
    
    t.color('black', 'white')
    t.begin_fill()
    t.circle(35)
    t.end_fill()
    p = t.pos()

    t.left(90)
    t.penup()
    t.fd(40)
    t.right(90)
    t.fd(10)
    t.left(90)
    t.pendown()
    t.color('black')
    t.begin_fill()
    t.circle(15)
    t.end_fill()

    t.penup()
    t.circle(15, 190)
    t.pendown()
    t.color('white')
    t.begin_fill()
    t.circle(7, -360)
    t.end_fill()
    
    t.penup()
    t.goto(p)
    t.left(170)
    t.fd(70)
    t.right(90)
    t.pendown()
    t.color('black', 'white')
    t.begin_fill()
    t.circle(35)
    t.end_fill()

    t.left(90)
    t.penup()
    t.fd(40)
    t.right(90)
    t.fd(10)
    t.left(90)
    t.pendown()
    t.color('black')
    t.begin_fill()
    t.circle(15)
    t.end_fill()

    t.penup()
    t.circle(15, 190)
    t.pendown()
    t.color('white')
    t.begin_fill()
    t.circle(7, -360)
    t.end_fill()


    t.penup()
    t.goto(p)
    t.left(170)
    t.fd(140)
    # t.right(90)
    t.pendown()
    t.color('black')
    t.pensize(1)
    t.fd(5)
    t.pensize(20)
    t.fd(13)

    t.pensize(5)

def draw_mouth():
    p1 = t.pos()
    t.color('black', 'white')
    t.begin_fill()
    t.circle(100, 28)
    t.penup()
    t.goto(p1)
    t.right(70)
    t.pendown()
    t.circle(30, 105)
    t.end_fill()
    
def draw_cloth(p):
    t.penup()
    t.fd(50)
    t.left(37)
    t.pendown()
    
    t.color('black', 'blue')
    t.begin_fill()
    t.fd(100)
    t.right(90)
    t.fd(60)
    t.left(90)
    t.fd(29)
    t.penup()
    t.right(90)
    t.fd(8)
    t.left(180)
    t.circle(50, -90)
    t.left(180)
    t.fd(33.5)
    p1 = t.pos()
    t.fd(33.5)
    t.left(180)
    t.circle(50, -90)
    t.right(180)
    t.fd(8)
    t.pendown()
    t.right(90)
    t.fd(33)
    t.left(90)
    t.fd(60)
    t.end_fill()

    t.penup()
    t.goto(p)
    t.right(120)
    t.pendown()

    t.color('black', 'blue')
    t.begin_fill()
    t.fd(60)
    t.right(90)
    t.fd(15)
    t.right(90)
    t.fd(50)
    t.right(60)
    t.fd(15)
    t.end_fill()

    t.penup()
    t.goto(p)
    t.right(90)
    t.fd(170)
    t.left(210)
    t.pendown()

    t.color('black', 'blue')
    t.begin_fill()
    t.fd(60)
    t.left(90)
    t.fd(15)
    t.left(90)
    t.fd(50)
    t.left(60)
    t.fd(15)
    t.end_fill()

    t.penup()
    t.goto(p1)
    t.pendown()
    t.pensize(2)
    t.fd(40)

    t.pensize(5)

    t.penup()
    t.fd(50)
    t.left(90)
    t.fd(28)
    t.pendown()

    p2 = t.pos()
    t.left(180)
    t.fd(60)

    t.penup()
    t.goto(p2)
    t.pendown()

    t.right(90)
    t.fd(5)
    t.circle(30, 180)
    t.fd(5)

    return p1

def draw_hands():
    p = t.pos()
    t.color('black','yellow')
    t.begin_fill()
    t.right(45)
    t.fd(30)
    for i in range(20):
        t.left(5)
        t.fd(1)
    t.fd(20)
    t.end_fill()

    t.penup()
    t.goto(p)
    t.right(55)
    t.fd(24)
    t.right(45)
    t.pendown()
    t.fd(10)

    t.penup()
    t.goto(p)
    t.left(135)
    t.fd(170)
    t.pendown()
    
    p1 = t.pos()
    t.color('black','yellow')
    t.begin_fill()
    t.right(45)
    t.fd(30)
    for i in range(20):
        t.right(5)
        t.fd(1)
    t.fd(20)
    t.end_fill()

    t.penup()
    t.goto(p1)
    t.left(55)
    t.fd(24)
    t.left(45)
    t.pendown()
    t.fd(10)

def draw_feet(p):

    t.penup()
    t.goto(p)
    t.right(135)
    t.fd(5)
    t.pendown()

    t.color('black')
    t.begin_fill()
    t.left(90)
    t.fd(30)
    t.right(90)
    t.fd(40)

    for i in range(15):
        t.right(6)
        t.fd(1)
    t.fd(2)
    for i in range(15):
        t.right(6)
        t.fd(1)
    t.fd(7)
    t.left(90)
    t.fd(7)
    t.end_fill()

    t.penup()
    t.goto(p)
    t.right(90)
    t.fd(5)
    t.pendown()

    t.color('black')
    t.begin_fill()
    t.right(90)
    t.fd(30)
    t.left(90)
    t.fd(40)

    for i in range(15):
        t.left(6)
        t.fd(1)
    t.fd(2)
    for i in range(15):
        t.left(6)
        t.fd(1)
    t.fd(7)
    t.right(90)
    t.fd(7)
    t.end_fill()

def draw_hair():
    p = t.pos()
    t.left(40)
    t.circle(40, 60)
    t.penup()
    t.goto(p)
    t.pendown()
    t.right(40)
    t.circle(60, 65)

    t.penup()
    t.goto(p)
    t.pendown()
    t.right(340)
    t.circle(40, -60)
    t.penup()
    t.goto(p)
    t.pendown()
    t.left(40)
    t.circle(50, -65)
    

def minions():
    turtle.tracer(0)

    start_point()
    draw_body()
    t.penup()
    t.circle(50,90)
    t.fd(30)
    t.left(90)
    t.pendown()

    p1 = t.pos()
    draw_eyes()

    t.penup()
    t.goto(p1)
    t.right(90)
    t.fd(70)
    p2 = t.pos()
    t.left(90)
    t.fd(70)
    t.pendown()
    
    draw_mouth()

    t.penup()
    t.goto(p2)
    t.right(100)
    t.pendown()
    p3 = draw_cloth(p2)

    t.penup()
    t.goto(p2)
    t.left(180)
    t.fd(17)
    t.pendown()
    draw_hands()


    draw_feet(p3)

    t.penup()
    t.goto(p3)
    t.fd(300)
    t.pendown()

    draw_hair()

    turtle.update()

    turtle.exitonclick()

if __name__ == "__main__":
    minions()
