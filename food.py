from turtle import Turtle
import random


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.color("blue")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        random_x_cor = random.randint(-260, 260)
        random_y_cor = random.randint(-260, 260)
        self.goto(random_x_cor, random_y_cor)
