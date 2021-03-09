from turtle import Turtle

player_img = "images/spaceship.gif"

class Player(Turtle):
    def __init__(self, position, image):
        super().__init__()
        self.penup()
        self.shape(image)
        self.goto(position)

    def go_left(self):
        new_x = self.xcor() - 20
        self.goto(new_x, self.ycor())
    
    def go_right(self):
        new_x = self.xcor() + 20
        self.goto(new_x, self.ycor())

    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)