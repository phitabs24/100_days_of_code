from turtle import Turtle
import random
import time

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FLOOR_LENGTH = 280
MOVE_DISTANCE = 20


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("white")
        self.speed("fastest")
        self.home()
        self.move_speed = 0.1
        self.x_move = MOVE_DISTANCE
        self.y_move = MOVE_DISTANCE

    def move(self):
        """
        Moves the object by updating its x and y coordinates.

        This method calculates the new x and y coordinates by adding the x_move and y_move values to the current x and y coordinates respectively. Then, it updates the object's position by calling the `goto` method with the new x and y coordinates.

        Parameters:
            None

        Returns:
            None
        """
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_off_wall(self):
        """
        Reverses the direction of movement when the ball collides with the top or bottom wall.

        This function does not take any parameters.

        This function does not return any value.
        """
        self.y_move *= -1

    def bounce_off_paddle(self):
        """
        Reverses the direction of movement when the ball collides with the paddle.

        This function does not take any parameters.

        This function does not return any value.
        """
        self.x_move *= -1
        self.move_speed *= 0.9

    def reset_position(self):
        self.goto(0, 0)
        self.move_speed = 0.1
        self.bounce_off_paddle()
