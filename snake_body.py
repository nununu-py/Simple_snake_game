from turtle import Turtle
STARTING_POSITION = ((20, 0), (0, 0), (0, -20))
MOVE_FORWARD = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.snake_body = []
        self.make_snake()
        self.snake_head = self.snake_body[0]

    def make_snake(self):
        for position in STARTING_POSITION:
            self.add_segment(position)

    def add_segment(self, position):
        my_snake = Turtle(shape="square")
        my_snake.penup()
        my_snake.color("white")
        my_snake.goto(position)
        self.snake_body.append(my_snake)

    def extend_snake(self):
        self.add_segment(self.snake_body[-1].position())

    def move_snake(self):
        for body in range(len(self.snake_body) - 1, 0, -1):
            new_x_cor = self.snake_body[body - 1].xcor()
            new_y_cor = self.snake_body[body - 1].ycor()
            self.snake_body[body].goto(new_x_cor, new_y_cor)
            self.snake_body[body].color("Orange")
        self.snake_head.forward(MOVE_FORWARD)

    def up(self):
        if self.snake_head.heading() != DOWN:
            self.snake_head.setheading(90)

    def down(self):
        if self.snake_head.heading() != UP:
            self.snake_head.setheading(270)

    def right(self):
        if self.snake_head.heading() != LEFT:
            self.snake_head.setheading(0)

    def left(self):
        if self.snake_head.heading() != RIGHT:
            self.snake_head.setheading(180)
