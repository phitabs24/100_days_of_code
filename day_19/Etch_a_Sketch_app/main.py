# A Turtle based game using keyboard inputs to draw shapes.

import turtle as t
import random as r

t.title("Etch A Sketch App - Drawing Space")
tim = t.Turtle()

screen = t.Screen()
t.colormode(255)
tim.speed('fastest')


def move_forward():
    """
    Moves the turtle backwards by 10 units.

    No parameters.

    No return value.
    """
    tim.forward(10)


def move_backwards():
    """
    Moves the turtle backwards by 10 units.

    No parameters.

    No return value.
    """
    tim.back(10)


def clockwise():
    """
    Rotate the turtle 5 degrees to the right in the clockwise direction.
    """
    tim.right(5)


def anti_clockwise():
    """
    Rotate the turtle 5 degrees to the left in the counter-clockwise direction.
    """
    tim.left(5)


def clear_screen():
    """
    Clears the screen by resetting the turtle graphics to its initial state.
    """
    t.clear()
    tim.penup()
    tim.home()
    tim.pendown()


def draw():
    """
    Toggles the pen state of the turtle.

    This function checks if the turtle's pen is down or up. If the pen is down, it lifts it up.
    If the pen is up, it puts it down.

    Parameters:
    None

    Returns:
    None
    """
    if tim.isdown():
        tim.penup()
    else:
        tim.pendown()


def close():
    """
    Exit the program.

    This function is used to terminate the program and close the turtle graphics window.

    Parameters:
        None

    Returns:
        None
    """
    t.bye()


screen.listen()
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="d", fun=clockwise)
screen.onkey(key="a", fun=anti_clockwise)
screen.onkey(key="c", fun=clear_screen)
screen.onkey(key="p", fun=draw)
screen.onkey(key="End", fun=close)
screen.onclick(tim.goto)
tim.ondrag(tim.goto)

screen.mainloop()
