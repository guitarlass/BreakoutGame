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

    def collide_with_brick(self):
        for brick_line_color in self.brick_line.brick_line_colors:
            b = 0
            while b < len(self.brick_line.brick_lists[brick_line_color]):
                brick_obj = self.brick_line.brick_lists[brick_line_color][b]["obj"]
                if self.distance(brick_obj) < 50:
                    brick_obj.hideturtle()
                b += 1
            print("-----")

    def handle_boundary_x(self):
        # Reverse the ball's x direction
        current_heading = self.heading()
        self.setheading(180 - current_heading)

    def handle_boundary_y(self):
        # Reverse the ball's y direction
        current_heading = self.heading()
        self.setheading(-current_heading)
