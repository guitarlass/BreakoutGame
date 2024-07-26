from turtle import Turtle


class Brick(Turtle):

    def __init__(self, height, width, color, position):
        super().__init__()
        self.hideturtle()
        self.color(color)
        self.shape("square")
        self.shapesize(stretch_len=height, stretch_wid=width)
        self.penup()
        self.goto(position)
        self.showturtle()
        self.brick_length = [4, 3, 2]
        self.brick_space = 10
        self.brick_line_space = 10
        self.brick_lines = ['green', 'yellow', 'orange', 'red']
        self.brick_lists = {color: [] for color in self.brick_lines}

    # def go_right(self):
    #     new_x_pos = self.xcor() + 20
    #     self.goto(new_x_pos, self.ycor())
    #
    # def go_left(self):
    #     new_x_pos = self.xcor() - 20
    #     self.goto(new_x_pos, self.ycor())
