import turtle
from turtle import Screen

from paddle import Paddle, end_game, CenterDivision
from ball import Ball
from scoreboard import Scoreboard
import time

PADDLE_POSITIONS = [(-380, 0), (370, 0)]
# create a screen and set the background color to black

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("The ball Game by phitabs24")
screen.tracer(0)

# create a snake, food and scoreboard
l_paddle = Paddle(PADDLE_POSITIONS[0])
r_paddle = Paddle(PADDLE_POSITIONS[1])
division = CenterDivision()
score = Scoreboard()

# screen.update()

screen.listen()

screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")
screen.onkey(end_game, "Escape")

ball = Ball()

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()

    # detect collision with roof and floor
    if ball.ycor() > 290 or ball.ycor() < -290:
        ball.bounce_off_wall()

    # detect collision with paddle
    if (ball.distance(l_paddle) < 50 and ball.xcor() < -350) or (
            ball.distance(r_paddle) < 50 and ball.xcor() > 350):
        ball.bounce_off_paddle()
    elif ball.xcor() > 400:
        score.increase_score1()
        ball.reset_position()
    elif ball.xcor() < -400:
        score.increase_score2()
        ball.reset_position()
    if score.score1 == 11 or score.score2 == 11:
        if score.score1 == 11:
            player = "Player 1"
        else:
            player = "Player 2"
        game_is_on = False
        score.game_over(player)

# screen.onkey(turtle.mainloop, "Enter")
turtle.mainloop()
