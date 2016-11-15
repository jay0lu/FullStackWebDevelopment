import turtle

def draw_triangle(some_turtle):
    for i in range(0,3):
        some_turtle.forward(100)
        some_turtle.right(120)

def draw_square(some_turtle):
    for x in range(0,4):
        some_turtle.forward(30)
        some_turtle.right(90)

def draw_flower():
    window = turtle.Screen()

    jay = turtle.Turtle()
    jay.shape("circle")
    jay.color("blue")
    jay.speed(10)

    tom = turtle.Turtle()
    tom.shape("circle")
    tom.color("green")
    tom.speed(10)

    for i in range (0,36):
        draw_triangle(jay)
        jay.right(10)
        draw_square(tom)
        tom.right(10)

    jay.right(90)
    jay.forward(240)

    window.exitonclick()


draw_flower()
