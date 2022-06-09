from turtle import Turtle


class ScreenLimit(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.speed("fastest")
        self.penup()
        self.goto(-270, -270)
        self.pendown()
        for _ in range(4):
            self.forward(540)
            self.left(90)

