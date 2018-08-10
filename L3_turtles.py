import turtle

def draw_triangle(some_turtle, length, ori, recurse):
    max = some_turtle
    recurse = recurse + 1

    for i in range(0,3):
        if recurse < 4:
            max.forward(length/2)
            max.left(120)
            draw_triangle(max, length/2, 0, recurse)
            max.right(120)
            max.forward(length/2)
        else:
            max.forward(length)

        if ori == 1:
            max.left(120)
        else:
            max.right(120)

def draw_art():
    window = turtle.Screen()
    window.bgcolor('white')

    brad = turtle.Turtle()
    brad.shape('turtle')
    brad.color('blue')
    brad.speed(3)

    for i in range(0,3):
        draw_triangle(brad, 50, 1, 0)
        brad.left(120)

    window.exitonclick()

draw_art()
