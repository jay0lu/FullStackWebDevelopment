import turtle

def draw_square(some_turtle):
    for x in range(0,4):
        some_turtle.forward(100)
        some_turtle.right(90)

def draw_circle(some_turtle):
    some_turtle.circle(100)

def draw_triangle(some_turtle):
    for x in range(0,3):
        some_turtle.forward(100)
        some_turtle.right(120)


def draw_art():
    window = turtle.Screen()
    window.bgcolor("red")

    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("yellow")
    brad.speed(2)
    for i in range(0,36):
        draw_square(brad)
        brad.right(10)

    # angie = turtle.Turtle()
    # angie.shape("arrow")
    # angie.color("blue")
    # draw_circle(angie)
    #
    # draw_triangle(brad)

    window.exitonclick()

draw_art()
