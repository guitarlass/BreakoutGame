from turtle import Turtle


class Bar(Turtle):

    def __init__(self, screen, position):
        super().__init__()
        self.screen = screen
        self.color("white")
        self.shape("square")
        self.hideturtle()
        self.shapesize(stretch_len=10, stretch_wid=1)
        self.penup()
        self.goto(position)
        self.showturtle()


    def go_right(self):
        new_x_pos = self.xcor() + 20
        self.goto(new_x_pos, self.ycor())
        # self.screen.update()

    def go_left(self):
        new_x_pos = self.xcor() - 20
        self.goto(new_x_pos, self.ycor())
        # self.screen.update()
