from brick import Brick
import random


class BrickLine():

    def __init__(self):
        self.brick_length = [10] # 4, 3, 2
        self.brick_space = 10
        self.brick_line_space = 10
        self.brick_line_colors = ['green']  # , 'yellow', 'orange', 'red'
        self.brick_lists = {color: [] for color in self.brick_line_colors}
        self.y_pos = 0
        self.x_pos = 0 # -400
        self.obj_no = 1
        self.end_line_pos = 2 # 400
        self.brick_width = 10 # 2
        self.bottom_y_pos_list = []

    def add_brick_line(self, brick_line_color):
        while self.x_pos < self.end_line_pos:
            random_len = random.choice(self.brick_length)
            self.x_pos = self.x_pos + (random_len * 20 / 2)
            print(f"({self.brick_width})")
            brick = Brick(random_len, self.brick_width, brick_line_color, (self.x_pos, self.y_pos))
            self.x_pos = self.x_pos + (random_len * 20 / 2) + self.brick_space
            self.brick_lists[brick_line_color].append(
                {"obj": brick, "len": random_len, "width": self.brick_width, "no": brick_line_color + str(self.obj_no)})
            self.obj_no += 1


    # def go_right(self):
    #     new_x_pos = self.xcor() + 20
    #     self.goto(new_x_pos, self.ycor())
    #
    # def go_left(self):
    #     new_x_pos = self.xcor() - 20
    #     self.goto(new_x_pos, self.ycor())
