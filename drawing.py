import turtle

def draw_square():
    window = turtle.Screen()
    window.bgcolor("yellow")

    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("blue")
    brad.speed(10)
    
    for i in range (1,37):
        brad.right(10)
        for x in range (1, 5):
            brad.forward(100)
            brad.right(90)
       
    window.exitonclick()

draw_square()
