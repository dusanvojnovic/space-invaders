from turtle import Turtle

class Laser(Turtle):
    def __init__(self, position, direction):
        super().__init__()
        self.position = position
        self.direction = direction
        self.fillcolor("#f0a500")
        self.shape("square")
        self.shapesize(stretch_wid=0.3, stretch_len=1)
        self.laser_heading()
        self.penup()
        self.new_heading = self.heading()
        self.speed("fastest")

    def laser_heading(self):
        self.penup()
        self.goto(self.position[0], self.position[1])
        if self.direction == "Up":
            self.new_heading = 90
        else:
            self.new_heading = 270
        self.setheading(self.new_heading)

    def move(self,speed):
        self.forward(speed)
    
    def destroy(self):
        self.penup()
        self.goto(2000, 2000)

