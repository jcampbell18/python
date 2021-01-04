from turtle import Turtle

TEXT_MOVE = False
TEXT_ALIGN = "center"
TEXT_FONT = ("Courier", 20, "normal")


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("red")
        self.goto(0, 270)
        self.show_score()
        self.hideturtle()

    def show_score(self):
        self.clear()
        self.write(f"Score: {self.score}", TEXT_MOVE, TEXT_ALIGN, TEXT_FONT)

    def reset_score(self):
        self.score = 0

    def increase_score(self):
        self.score += 1
        self.show_score()

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", TEXT_MOVE, TEXT_ALIGN, TEXT_FONT)
