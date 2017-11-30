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

def draw_circle():
    window = turtle.Screen()
    window.bgcolor("yellow")

    angie = turtle.Turtle()
    angie.shape("arrow")
    angie.color("red")
    angie.circle(100)

    window.exitonclick()

def draw_triangle():
    window = turtle.Screen()
    window.bgcolor("yellow")

    anne = turtle.Turtle()
    anne.shape("arrow")
    anne.color("red")
    n = 0

    while n <= 2:
        anne.forward(100)
        anne.right(120)
        n += 1

    window.exitonclick()
    
draw_square()
#draw_circle()
#draw_triangle()
