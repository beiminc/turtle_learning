from turtle import *

def start():
    hideturtle()
    speed(0)  
    pensize(5)

def wall():
    pu()
    goto(-300, 300)
    pd()

    setheading(270)
    fd(500)

def bottom():
    pu()
    home()
    goto(-300, 200)
    setheading(240)
    pd()

    # face
    circle(100, -230)
    
    # body
    pu()
    goto(-187.52,53.41)
    setheading(290)
    pd()
    fd(270)

    # face
    pu()
    goto(-150, 130)
    pd()
    dot(40, 'pink')

    #arm
    pu()
    goto(-270, 40)
    setheading(60)
    pd()
    fd(90)
    setheading(-70)
    circle(30, -265)
    setheading(-120)
    fd(90)

    #eye
    pu()
    goto(-165, 180)
    setheading(-10)
    pd()
    fd(30)
    setheading(-150)
    fd(37)

def top():
    pu()
    goto(-40,53.41)
    setheading(-40)
    pd()

    # face
    circle(110, -280)

    #arm
    pu()
    goto(-40,53.41)
    setheading(179)
    pd()
    fd(148)

    pu()
    goto(-40, 17)
    setheading(177)
    pd()
    fd(135)

    pu()
    goto(104.31,55.93)
    setheading(-40)
    pd()
    fd(30)
    for i in range(40):
        right(2)
        fd(1)
    fd(20)
    right(180)
    circle(10, -180)
    right(180)
    fd(20)
    left(90)
    fd(30)

    # body
    pu()
    goto(-40, 17)
    setheading(280)
    pd()
    fd(225)

    pu()
    goto(123.05, -17.05)
    setheading(-70)
    pd()
    fd(180)

    # eye
    pu()
    goto(-50, 160)
    setheading(-20)
    pd()
    fd(30)
    setheading(-170)
    fd(30)

    pu()
    goto(30, 150)
    setheading(10)
    pd()
    fd(30)
    
    pu()
    goto(33, 145)
    setheading(-80)
    pd()
    dot(12, 'black')
    
    # mouth
    pu()
    goto(-30, 100)
    setheading(-60)
    pd()
    circle(50, 120)

    # face
    pu()
    goto(-50, 110)
    pd()
    dot(30, 'pink')

    pu()
    goto(80, 110)
    pd()
    dot(30, 'pink')


def main():
    tracer(0)
    start()

    wall()
    bottom()
    top()

    update()
    exitonclick()

if __name__ == "__main__":
    main()