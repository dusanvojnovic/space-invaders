from turtle import Turtle

class Board(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.life = 3
        self.hideturtle()
        self.update_scoreboard()
    
    def update_scoreboard(self):
        self.clear()
        self.goto(-370, 450)
        self.write(f"Life's remaining: {self.life}", align="left", font = ("Courier", 20, "normal"))
        
    def game_over(self):
        self.goto(0, 0)
        self.write(f"\tOops, Game Over!\nInvaders destroyed your spaceship!", align="center", font= ("Courier", 20, "bold"))

    def win_game(self):
        self.goto(0, 0)
        self.write(f"\tYou have won!\nAll Invaders ships are destroyed!", align="center", font= ("Courier", 20, "bold"))