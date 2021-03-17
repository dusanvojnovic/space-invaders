from turtle import Turtle

class Invader(Turtle):
    def __init__(self, position, image):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.shape(image)
        self.goto(position)
        self.showturtle()

    def go_right(self):
        new_x = self.xcor() + 10
        self.goto(new_x, self.ycor())

    def go_left(self):
        new_x = self.xcor() - 10
        self.goto(new_x, self.ycor())

    def destroy(self):
        self.goto(2000, 2000)
