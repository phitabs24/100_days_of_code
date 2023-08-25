# import turtle as t
#
# # timmy = Turtle()
# #
# # # change timmy shape
# # timmy.shape("turtle")
# #
# # # make timmy to draw a triangle
# # timmy.forward(100)
# # timmy.left(120)
# # timmy.forward(100)
# # timmy.left(120)
# # timmy.forward(100)
#
# # a colorful spiral
# # for steps in range(100):
# #     for c in ('blue', 'red', 'green'):
# #         color(c)
# #         forward(steps)
# #         right(30)
#
# # draw a colorful star shape
# # t.color('red')
# # t.fillcolor('blue')
# # t.begin_fill()
# # for _ in range(4):
# #     t.forward(100)
# #     t.left(90)
# # t.end_fill()
# from turtle import *
# import random
#
# # t = Turtle()
# # t.pensize(2)
# # angle = [120, 90, 72, 60, 51.42857142857143, 45, 40, 36, 30, -120, -90, -72, -60, -51.42857142857143, -45, -40, -36, -30]
# # sides = [3, 4, 5, 6, 7, 8, 9, 10, 12, 3, 4, 5, 6, 7, 8, 9, 10, 12]
# # color = ['red', 'blue', 'lawngreen', 'gold', 'hotpink', 'firebrick1', 'mediumvioletred', 'mediumblue', 'DarkOrchid3',
# #          'red', 'blue', 'lawngreen', 'gold', 'hotpink', 'firebrick1', 'mediumvioletred', 'mediumblue', 'DarkOrchid3',
# #          'yellow', 'gold', 'orange', 'red', 'maroon', 'violet', 'magenta', 'purple', 'navy', 'blue', 'skyblue', 'cyan',
# #          'turquoise', 'lightgreen', 'green', 'darkgreen', 'chocolate', 'brown', 'black', 'gray', 'white']
# # n = 0
# # for side in sides:
# #     for _ in range(side):
# #         t.pencolor(color[n])
# #         t.forward(100)
# #         t.right(angle[n])
# #     n += 1
#
#
# # Turtle challange 4
#
# colormode(255)
#
#
# def random_color() -> tuple:
#     """
#     Generates a random RGB color.
#
#     Returns:
#         tuple: A tuple representing the RGB color. Each element of the tuple is an integer between 0 and 255.
#     """
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     r_color = (r, g, b)
#     return r_color
#
#
# pensize(15)
# speed(10)
# for _ in range(200):
#     pencolor(random_color())
#     angle = random.choice([0, 90, 180, 270])
#     forward(30)
#     setheading(angle)
#

# project 5

from turtle import *
import random
colormode(255)

while True:
    for angle in range(0, 365, 5):
        speed(500)
        pencolor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        circle(100)
        setheading(angle)
        if angle == 360:
            clear()
exitonclick()
