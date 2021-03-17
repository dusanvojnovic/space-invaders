from turtle import Turtle
from random import randint

rock_img = "images/rock.gif"

class RockMaker:
    def __init__(self):
        self.all_rocks = []
        self.reserve_rocks = []
        self.speed = 6

    def create_rock(self, image = rock_img):
        rand_chance = randint(1, 25)
        if rand_chance == 1 or rand_chance == 10:
            if self.reserve_rocks:
                new_rock = self.reserve_rocks.pop()
            else:
                new_rock = Turtle()
                new_rock.shape(image)
                new_rock.penup()
            random_y = randint(-410, 190)
            new_rock.goto(450, random_y)
            self.all_rocks.append(new_rock)

    def move_rocks(self):
        for rock in self.all_rocks:
            rock.backward(self.speed)
            if rock.xcor() < -450:
                self.all_rocks.remove(rock)
                self.reserve_rocks.append(rock)

    

                