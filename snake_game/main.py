from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time

# customize screen
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
MAX_XCOR = SCREEN_WIDTH / 2
MAX_YCOR = SCREEN_HEIGHT / 2
PROXIMITY = 15

screen = Screen()
screen.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)
screen.listen()

# create snake body
snake = Snake()

# create snake food
food = Food(MAX_XCOR, MAX_YCOR)

# create scoreboard
score_board = ScoreBoard()

# move the snake
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

# detect collision with food
    if snake.head.distance(food) < PROXIMITY:
        food.refresh()
        score_board.increase_score()
        snake.grow()

# detect collision with wall
    if snake.head.xcor() > MAX_XCOR or snake.head.xcor() < -1 * MAX_XCOR or \
            snake.head.ycor() > MAX_YCOR or snake.head.ycor() < -1 * MAX_YCOR:
        game_is_on = False
        score_board.game_over()

# detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            score_board.game_over()

screen.exitonclick()
