from turtle import Turtle
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

        # Set the direction towards the random location
        self.setheading(self.towards(target_x, target_y))

        # Move the ball at the specified speed
        while True:
            self.forward(self.ball_speed)
            if self.xcor() > 380 or self.xcor() < -380:
                self.handle_boundary_x()
            if self.ycor() > 237:
                self.handle_boundary_y()
            if self.distance(self.bar) < 101 and self.ycor() < -210:
                self.handle_boundary_y()

            # for single_brick_list in self.brick_line.brick_lists:
            self.collide_with_brick()

            self.screen.update()

    def collide_with_brick(self):
        for brick_line_color in self.brick_line.brick_line_colors:
            b = 0
            while b < len(self.brick_line.brick_lists[brick_line_color]):
                brick_data = self.brick_line.brick_lists[brick_line_color][b]
                brick_obj = brick_data["obj"]

                half_width = brick_data["width"] * 20 / 2
                half_height = brick_data["len"] * 20 / 2

                if (brick_obj.xcor() - half_width < self.xcor() < brick_obj.xcor() + half_width and
                        brick_obj.ycor() - half_height < self.ycor() < brick_obj.ycor() + half_height):
                    # Determine which direction the collision occurred from
                    if abs(self.xcor() - brick_obj.xcor()) > abs(self.ycor() - brick_obj.ycor()):
                        self.handle_boundary_x()
                        # Adjust position to avoid sticking
                        if self.xcor() > brick_obj.xcor():
                            self.setx(brick_obj.xcor() + half_width + 1)
                        else:
                            self.setx(brick_obj.xcor() - half_width - 1)
                    else:
                        self.handle_boundary_y()
                        # Adjust position to avoid sticking
                        if self.ycor() > brick_obj.ycor():
                            self.sety(brick_obj.ycor() + half_height + 1)
                        else:
                            self.sety(brick_obj.ycor() - half_height - 1)

                    # Remove the brick from the list after collision
                    # self.brick_line.brick_lists[brick_line_color].pop(b)
                    # brick_obj.hideturtle()

                    # Increase ball speed
                    self.increase_ball_speed(brick_line_color)

                self.increase_ball_speed(brick_line_color)

                b += 1

    def handle_boundary_x(self):
        current_heading = self.heading()
        self.setheading(180 - current_heading)

    def handle_boundary_y(self):
        current_heading = self.heading()
        self.setheading(-current_heading)

    def increase_ball_speed(self, brick_line_color):
        if brick_line_color == "green":
            self.ball_speed = 3
        elif brick_line_color == "yellow":
            self.ball_speed = 5
        elif brick_line_color == "orange":
            self.ball_speed = 7
        elif brick_line_color == "red":
            self.ball_speed = 9
