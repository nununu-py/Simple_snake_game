from turtle import Screen
import time
from snake_body import Snake
from score_board import ScoreBoard
from food import Food
from screen_limit import ScreenLimit

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

the_snake = Snake()
the_food = Food()
score = ScoreBoard()
screen_limit = ScreenLimit()


screen.listen()
screen.onkey(the_snake.up, key="w")
screen.onkey(the_snake.down, key="s")
screen.onkey(the_snake.right, key="d")
screen.onkey(the_snake.left, key="a")

game_is_on = True

while game_is_on:

    if score.score > 3:
        time.sleep(0.1)
    else:
        time.sleep(0.5)

    screen.update()

    the_snake.move_snake()

    # detect collision with the food
    if the_snake.snake_head.distance(the_food) < 20:
        the_food.refresh()
        the_snake.extend_snake()
        score.increase_score()

    # detect collision with the screen
    if the_snake.snake_head.xcor() > 270 or the_snake.snake_head.xcor() < -270 or the_snake.snake_head.ycor() > 270 \
            or the_snake.snake_head.ycor() < -270:
        game_is_on = False
        score.game_over()

    # detect collision of the body
    # for body in the_snake.snake_body:
    #     if body == the_snake.snake_head:
    #         pass
    #     elif the_snake.snake_head.distance(body) < 10:
    #         game_is_on = False
    #         score.game_over()

    # - using list slicing

    for body in the_snake.snake_body[1:]:
        if the_snake.snake_head.distance(body) < 10:
            game_is_on = False
            score.game_over()

screen.exitonclick()
