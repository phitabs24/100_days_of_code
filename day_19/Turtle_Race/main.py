import turtle as t
import random as r

t.title("Turtle Race App - By Philemon")
screen = t.Screen()
screen.setup(width=500, height=400)

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
turtles = []
# r.shuffle(colors)
y_positions = [-100, -60, -20, 20, 60, 100]
for turtle in range(0, 6):
    new_turtle = t.Turtle(shape="turtle")
    new_turtle.color(colors[turtle])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_positions[turtle])
    # new_turtle.pendown()
    turtles.append(new_turtle)

user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? "
                                                          "Enter a rainbow color: ").lower()
is_race_on = False

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")
        random_distance = r.randint(0, 10)
        turtle.forward(random_distance)

screen.exitonclick()
