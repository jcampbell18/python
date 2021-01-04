from turtle import Turtle
import random


MARGIN = 20


class Food(Turtle):

    def __init__(self, max_xcor, max_ycor):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("green")
        self.speed("fastest")

        self.adjusted_width = max_xcor - MARGIN
        self.adjusted_height = max_ycor - MARGIN

        random_x = random.randint(-1 * self.adjusted_width, self.adjusted_width)
        random_y = random.randint(-1 * self.adjusted_height, self.adjusted_height)
        self.goto(random_x, random_y)

    def refresh(self):
        random_x = random.randint(-1 * self.adjusted_width, self.adjusted_width)
        random_y = random.randint(-1 * self.adjusted_height, self.adjusted_height)
        self.goto(random_x, random_y)
