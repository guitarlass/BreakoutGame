from turtle import Turtle


class Brick(Turtle):

    def __init__(self, height, width, color, position):
        super().__init__()
        self.height = height
        self.width = width
        self.hideturtle()
        self.color(color)
        self.shape("square")
        self.shapesize(stretch_len=height, stretch_wid=width)
        self.penup()
        self.goto(position)
        self.showturtle()
        # self.brick_length = [4, 3, 2]
        # self.brick_space = 10
        # self.brick_line_space = 10
        # self.brick_lines = ['green'] # , 'yellow', 'orange', 'red'
        # self.brick_lists = {color: [] for color in self.brick_lines}

    def get_square_corners(self, side_length_x, side_length_y):
        center_x, center_y = self.xcor(), self.ycor()
        half_side_x = side_length_x / 2
        half_side_y = side_length_y / 2

        top_left = (center_x - half_side_x, center_y + half_side_y)
        top_right = (center_x + half_side_x, center_y + half_side_y)
        bottom_left = (center_x - half_side_x, center_y - half_side_y)
        bottom_right = (center_x + half_side_x, center_y - half_side_y)

        return top_left, top_right, bottom_left, bottom_right

    # def go_right(self):
    #     new_x_pos = self.xcor() + 20
    #     self.goto(new_x_pos, self.ycor())
    #
    # def go_left(self):
    #     new_x_pos = self.xcor() - 20
    #     self.goto(new_x_pos, self.ycor())
