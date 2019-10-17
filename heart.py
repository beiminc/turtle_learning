import turtle

def heartHeartHeart():
    turtle.speed(0)

    turtle.color('red')
    turtle.begin_fill()
    turtle.left(140)
    turtle.forward(111.65)
    for i in range(200):
        turtle.right(1)
        turtle.forward(1)    
    turtle.left(120)
    for i in range(200):
        turtle.right(1)
        turtle.forward(1)  
    
    turtle.forward(111.65)
    
    # turtle.right(40)
    # turtle.forward(180)

    turtle.end_fill()

    turtle.exitonclick()

heartHeartHeart()