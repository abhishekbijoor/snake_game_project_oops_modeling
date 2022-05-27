from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Ariel", 28, "normal")


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("score.txt", "r") as file:
            temp = file.read()
            if temp == "":
                self.highscore = 0
            else:
                self.highscore = int(temp)
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_score()

    def increase_score(self):
        self.score += 1

    def update_score(self):
        self.increase_score()
        self.clear()
        self.write(f"Score = {self.score} HighScore = {self.highscore}", align= ALIGNMENT, font=FONT)

    def game_over(self):
        self.clear()
        if self.highscore < self.score:
            with open("score.txt", "w") as file:
                file.write(str(self.score))
        else:
            with open("score.txt", "w") as file:
                file.write(str(self.highscore))

        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)


