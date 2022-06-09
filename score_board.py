from turtle import Turtle


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        x_coordinate = 0
        y_coordinate = 280
        self.penup()
        self.color("yellow")
        self.hideturtle()
        self.goto(x_coordinate, y_coordinate)
        self.score = 0
        self.write(arg=f"Your Score : {self.score}", move=False, align="center", font=("Arial", 11, "normal"))

    def increase_score(self):
        self.clear()
        self.score += 1
        self.write(arg=f"Your Score : {self.score}", move=False, align="center", font=("Arial", 11, "normal"))

    def game_over(self):
        self.goto(0, 0)
        self.write(arg=f"GAME OVER", move=False, align="center", font=("Arial", 11, "normal"))
