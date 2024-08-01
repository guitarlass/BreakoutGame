from turtle import Turtle
import turtle
import random


class Ball(Turtle):

    def __init__(self, screen, bar, brick_line):
        super().__init__()
        self.bar = bar
        self.screen = screen
        self.brick_line = brick_line
        self.hideturtle()
        self.color("blue")
        self.shape("circle")
        # self.penup()
        self.ball_speed = 3
        self.speed(50)
        self.towards_cor = None
        self.goto(0, -205)
        self.showturtle()

    def move_ball(self):
        # Get random coordinates
        xy_cor = ['x', 'y']
        x_or_y = random.choice(xy_cor)

        if x_or_y == 'x':
            target_x = self.screen.window_width() // 2 + 20
            target_y = random.randint(-(self.screen.window_height() - 150) // 2, (self.screen.window_height()) // 2)
            self.towards_cor = "x"
        else:
            target_y = self.screen.window_height() // 2 + 20
            target_x = random.randint(-self.screen.window_width() // 2, self.screen.window_width() // 2)
            self.towards_cor = "y"

        # Calculate the distance to move
        distance = self.distance(target_x, target_y)

        # Set the direction towards the random location
        self.setheading(self.towards(target_x, target_y))

        # Move the ball at the specified speed
        while True:
            # print(str(self.xcor())+", "+str(self.ycor()))
            self.forward(self.ball_speed)
            if self.xcor() > 380 or self.xcor() < -380:
                self.handle_boundary_x()
            if self.ycor() > 237:
                self.handle_boundary_y()
            if self.distance(self.bar) < 101 and self.ycor() < -210:
                self.handle_boundary_y()

            # for single_brick_list in self.brick_line.brick_lists:
            self.collide_with_brick()
            # break
            self.screen.update()

    def draw_square(self, x1, y1, x2, y2, color):
        turtle.penup()
        turtle.goto(x1, y1)
        turtle.pendown()
        turtle.color(color)
        for _ in range(2):
            turtle.forward(x2 - x1)
            turtle.left(90)
            turtle.forward(y2 - y1)
            turtle.left(90)

    def collide_with_brick(self):
        for brick_line_color in self.brick_line.brick_line_colors:
            b = 0
            while b < len(self.brick_line.brick_lists[brick_line_color]):
                brick_data = self.brick_line.brick_lists[brick_line_color][b]
                brick_obj = brick_data["obj"]

                half_width = brick_data["width"] * 20 /2
                half_height = brick_data["len"] * 20/2

                if (brick_obj.xcor() - half_width < self.xcor() < brick_obj.xcor() + half_width and
                        brick_obj.ycor() - half_height < self.ycor() < brick_obj.ycor() + half_height):
                    print("collide")

                    # top_left, top_right, bottom_left, bottom_right = brick_obj.get_square_corners()
                    # tlx, tly = top_left
                    # btx, bly = bottom_left
                    #
                    # trx, tr_y = top_right
                    # brx, bry = bottom_right

                    # if (tlx >= self.xcor() and tly >= self.ycor() >= bly) or (trx >= self.xcor() and tr_y >= self.ycor() >= bry):
                    #     print("bounce x")
                    #
                    #
                    # brick_y = brick_obj.ycor()
                    # brick_x = brick_obj.xcor()
                    # brick_len = brick_data["len"] * 20
                    # brick_width = brick_data["width"] * 20
                    #
                    # # Define the bounding box for the brick
                    # brick_left = brick_x - (brick_len / 2)
                    # brick_right = brick_x + (brick_len / 2)
                    # brick_top = brick_y + (brick_width / 2)
                    # brick_bottom = brick_y - (brick_width / 2)

                    # print(f"ball : {self.xcor()}, {self.ycor()}")
                    # Check if the ball is within the brick's bounding box
                    # if (brick_left <= self.xcor() <= brick_right) and (brick_bottom <= self.ycor() <= brick_top):
                    # brick_obj.hideturtle()
                    # print("collide")
                    #
                    # print(f"brick : l-{brick_left}, r-{brick_right}")
                    # print(f"brick : t-{brick_top}, b-{brick_bottom}")
                    # self.brick_line.brick_lists[brick_line_color].pop(b)
                    #
                    # if self.ycor() in self.brick_line.bottom_y_pos_list:
                    #     self.handle_boundary_x()
                    #     print("x")
                    # else:
                    #     self.handle_boundary_y()
                    #     print("y")

                    self.increase_ball_speed(brick_line_color)

                else:
                    b += 1
                    # side_length_x = 20 * self.brick_line.brick_lists[brick_line_color][b]["len"]
                    # side_length_y = 20 * self.brick_line.brick_lists[brick_line_color][b]["width"]
                    #
                    # # Get the corners of the brick
                    # top_left, top_right, bottom_left, bottom_right = brick_obj.get_square_corners(side_length_x,
                    #                                                                               side_length_y)
                    #
                    # # Extract the coordinates
                    # tlx, tly = top_left
                    # trx, try_ = top_right
                    # blx, bly = bottom_left
                    # brx, bry = bottom_right
                    #
                    # # Check if the ball's position is within the brick's bounding box
                    # if (tlx <= self.xcor() <= trx) and (bly <= self.ycor() <= tly):
                    #     print(f"Collide with brick {self.brick_line.brick_lists[brick_line_color][b]['no']}")
                    #     brick_obj.hideturtle()
                    #     self.brick_line.brick_lists[brick_line_color].pop(b)
                    #     continue  # Skip incrementing b as the current brick is removed
                    # b += 1

    def increase_ball_speed(self, brick_line_color):
        if brick_line_color == "green":
            self.ball_speed = 3
        elif brick_line_color == "yellow":
            self.ball_speed = 5
        elif brick_line_color == "orange":
            self.ball_speed = 7
        elif brick_line_color == "red":
            self.ball_speed = 9

    def handle_boundary_x(self):
        current_heading = self.heading()
        self.setheading(180 - current_heading)

    def handle_boundary_y(self):
        current_heading = self.heading()
        self.setheading(-current_heading)
