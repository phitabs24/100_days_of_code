import turtle
from turtle import Turtle

MOVE_DISTANCE = 40
CENTER_POSITIONS = []
for i in range(-270, 300, 46):
    new_position = (0, i)
    CENTER_POSITIONS.append(new_position)


def end_game():
    """
    Closes the game and exits the program.

    This function is responsible for terminating the game and closing the program. It calls the `bye()` method from the `turtle` module to gracefully close the turtle graphics window.

    Parameters:
    None

    Returns:
    None
    """
    turtle.bye()


class Paddle(Turtle):

    def __init__(self, position):
        """Creates a snake with 3 segments."""
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.penup()
        self.setheading(90)
        self.goto(position)

    def up(self):
        """
        Moves the paddle upwards by a given distance.

        Returns:
            None
        """
        new_y = self.ycor() + MOVE_DISTANCE
        self.goto(self.xcor(), new_y)

    def down(self):
        """
        Moves the paddle downwards by a given distance.

        Returns:
            None
        """
        new_y = self.ycor() - MOVE_DISTANCE
        self.goto(self.xcor(), new_y)


class CenterDivision:

    def __init__(self):
        self.divisions = []
        self.center_division()

    def center_division(self):
        """
        Create and position white strips at the center of the screen to separate player areas.
        """
        for position in CENTER_POSITIONS:
            new_division = Turtle(shape="square")
            new_division.color("white")
            new_division.shapesize(stretch_wid=1, stretch_len=0.2)
            new_division.penup()
            new_division.goto(position)
            self.divisions.append(new_division)
