import turtle

def heartHeartHeart():
    m = turtle.Turtle()
    m.speed(0)

    m.color('red')
    m.begin_fill()
    m.left(140)
    m.forward(112)
    for i in range(200):
        m.right(1)
        m.forward(1)    
    m.left(120)
    for i in range(200):
        m.right(1)
        m.forward(1)  
    
    m.forward(112)
    
    # m.right(40)
    # m.forward(180)

    m.end_fill()

    turtle.exitonclick()

heartHeartHeart()