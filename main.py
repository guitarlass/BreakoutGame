from turtle import Screen, Turtle
from bar import Bar
from ball import Ball
from brick_line import BrickLine
import random

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=500)
screen.title("Breakout Game")
# screen.tracer(0)

bar = Bar(screen, (0, -230))


brick_line = BrickLine()
for brick_line_color in brick_line.brick_line_colors:
    brick_line.x_pos = -400
    brick_line.obj_no = 1
    brick_line.add_brick_line(brick_line_color)
    brick_line.y_pos += (brick_line.brick_width*20) + brick_line.brick_line_space

ball = Ball(screen, bar, brick_line)

# print(brick_lists["green"][0]["len"])

screen.listen()
screen.onkeypress(bar.go_right, "Right")
screen.onkeypress(bar.go_left, "Left")


ball.move_ball()

screen.onkey(ball.stop, "s")  # Press "s" to stop
screen.onkey(ball.start, "r")  # Press "r" to restart

# game_is_on = True
# while game_is_on:
#     screen.update()

screen.exitonclick()
