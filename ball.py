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
        self.penup()
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
            self.screen.update()

    def collide_with_brick(self):
        for brick_line_color in self.brick_line.brick_line_colors:
            b = 0
            while b < len(self.brick_line.brick_lists[brick_line_color]):
                brick_data = self.brick_line.brick_lists[brick_line_color][b]
                brick_obj = brick_data["obj"]
                brick_y = brick_obj.ycor()
                brick_x = brick_obj.xcor()
                brick_len = brick_data["len"] * 20
                brick_width = brick_data["width"] * 20

                # Define the bounding box for the brick
                brick_left = brick_x - (brick_len / 2)
                brick_right = brick_x + (brick_len / 2)
                brick_top = brick_y + (brick_width / 2)
                brick_bottom = brick_y - (brick_width / 2)

                # Check if the ball is within the brick's bounding box
                if (brick_left <= self.xcor() <= brick_right) and (brick_bottom <= self.ycor() <= brick_top):
                    # brick_obj.hideturtle()
                    print("collide")
                    break
                    self.brick_line.brick_lists[brick_line_color].pop(b)
                else:
                    b += 1

    def handle_boundary_x(self):
        current_heading = self.heading()
        self.setheading(180 - current_heading)

    def handle_boundary_y(self):
        current_heading = self.heading()
        self.setheading(-current_heading)
