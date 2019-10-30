from turtle import *

def start():
    speed(0)   
    pensize(5)

def nose(x,y):
    pu()
    goto(x, y)
    pd()
    dot(12, 'deep pink')

def eye(x,y):
    pu()
    goto(x, y)
    pd()
    color('hot pink', 'white')
    begin_fill()
    circle(20)
    end_fill()
    pu()
    goto(x-7, y-20)
    dot(15, 'black')

def ear(p, d):
    pu()
    goto(p)
    setheading(120)
    pd()

    color('hot pink', 'light pink')
    begin_fill()
    fd(30)
    circle(15, 180)
    fd(d)
    end_fill()

    home()

def face():
    pu()
    goto(-55, 80)
    pd()
    dot(60, 'hot pink')

def mouth():
    pu()
    goto(70, 80)
    pd()

    color('orange red')
    setheading(90)
    circle(40, -180)


def head():
    # 耳朵
    ear((-50.00,186.60), 31)
    ear((-0.00,200.00), 16)

    pu()
    goto(100,100)
    pd()

    # 头型
    color('hot pink', 'light pink')
    setheading(270)
    begin_fill()
    circle(-100, 270)
    circle(-1000, 10)
    circle(-30,540)
    goto(100,100)
    end_fill()

    # 鼻
    nose(160, 155)
    nose(178, 160)

    # 眼睛
    eye(-10, 170)
    eye(60, 180)

    #脸蛋
    face()

    # 嘴巴
    mouth()

def cloth():
    pu()
    home()
    goto(100,100)
    setheading(270)
    circle(-100, 140)
    setheading(240)
    pd()

    color('red', 'orange red')
    begin_fill()
    for i in range(180):
        right(-0.1)
        fd(1)
    setheading(0)
    p = pos()
    fd(250)
    left(100)
    for i in range(160):
        right(-0.1)
        fd(1)
    pu()
    setheading(217)
    circle(-100, 90)
    pd()
    end_fill()

def hand(x,y, angle):
    pu()
    goto(x,y)
    setheading(angle)
    pd()

    color('light pink')
    fd(85)
    bk(25)
    left(40)
    fd(25)
    bk(25)
    right(80)
    fd(25)

def hands():
    hand(-102, -4, 200)
    hand(75, -4, 340)

def foot(x,y):
    pu()
    goto(x,y)
    setheading(270)
    pd()

    color('hot pink')
    fd(40)

    color('black')
    begin_fill()
    setheading(180)
    circle(5, 180)
    fd(45)
    circle(7,185)
    fd(45)
    end_fill()



def feet():
    foot(-70, -128)
    foot(10, -128) 

def main():
    tracer(0)
    start()
    head()
    cloth()
    hands()
    feet()

    update()
    exitonclick()

if __name__ == "__main__":
    main()