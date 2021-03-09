from turtle import Screen
from player import Player, player_img
from invader import Invader
from laser import Laser
from random import randint, choice
from rock import RockMaker, rock_img
from infoboard import Board
import time

bg_img = "images/spacebg.gif"

screen = Screen()
screen.setup(width=800, height=1000)
screen.title("Space Invaders")
screen.bgpic('images/space.gif')
screen.addshape(player_img)
screen.addshape(rock_img)

screen.tracer(0)

player = Player((0, -430), player_img)
board = Board()
screen.addshape("images/alien1.gif")
screen.addshape("images/alien2.gif")
screen.addshape("images/alien3.gif")

rockmaker = RockMaker()
enemies = ["images/alien1.gif", "images/alien2.gif", "images/alien3.gif"]
invaders = []

pos_x = 300
pos_y = 210
for i in range(9):
    invader = Invader((pos_x, pos_y), enemies[1])
    pos_x -= 70
    invaders.append(invader)

pos_x = 320
pos_y = 280
for i in range(10):
    invader = Invader((pos_x, pos_y), enemies[0])
    pos_x -= 70
    invaders.append(invader)

pos_x = 330
pos_y = 350
for i in range(10):
    invader = Invader((pos_x, pos_y), enemies[2])
    pos_x -= 70
    invaders.append(invader)

pos_x = 300
pos_y = 420
for i in range(9):
    invader = Invader((pos_x, pos_y), enemies[1])
    pos_x -= 70
    invaders.append(invader)

lasers = []

def shoot():
    laser = Laser((player.xcor(), player.ycor()+10), "Up")
    lasers.append(laser)

screen.listen()
screen.onkeypress(player.go_left, "Left")
screen.onkeypress(player.go_right, "Right")
screen.onkeypress(player.go_up, "Up")
screen.onkeypress(player.go_down, "Down")
screen.onkey(shoot, "space")

game_is_on = True
life = 3
invaders_pos = "right"
laser_speed = 10
screen.update()

while game_is_on:
    time.sleep(0.02)
    
    rockmaker.create_rock()
    rockmaker.move_rocks()
    # make sure player can't go out of game screen
    if player.xcor() > 380:
        player.goto(player.xcor()-20, player.ycor())
    if player.xcor() < -380:
        player.goto(player.xcor() + 20, player.ycor())
    if player.ycor() < -440:
        player.goto(player.xcor(), player.ycor() + 20 )

    # make invaders move right or left    
    random_number = randint(1, 50)
    if random_number == 5 or random_number == 10:
        if invaders_pos == "right":
            for invader in invaders:
                invader.go_right()
        else:
            for invader in invaders:
                invader.go_left()

    if invaders_pos == "right":
        invaders_pos = "left"
    else:
        invaders_pos = "right"
    # make invaders fire lasers
    if random_number == 15 or random_number == 20 or random_number == 25 or random_number == 30:
        random_invader = choice(invaders)
        x_cor = random_invader.xcor()
        y_cor = random_invader.ycor()
        laser = Laser((x_cor, y_cor), "Down")
        lasers.append(laser)
    
    for laser in lasers:
        laser.move(laser_speed)
    # after certain fired lasers, improve lasers speed 
    if len(lasers) % 25 == 0:
        laser_speed += 0.2
    # player gets hit
    for laser in lasers:
        if laser.distance(player) < 25 and laser.direction == "Down":
            life -= 1
            board.life -= 1
            board.update_scoreboard()
            laser.destroy()
            index = lasers.index(laser)
            lasers.pop(index)
        # invader gets hit   
        for invader in invaders:
            if laser.distance(invader) < 25 and laser.direction == "Up":
                invader.destroy()
                laser.destroy()
                i_index = invaders.index(invader)
                invaders.pop(i_index)
                l_index = lasers.index(laser)
                lasers.pop(l_index)
        # laser hits rock        
        for rock in rockmaker.all_rocks:
            if rock.distance(laser) < 25:
                rock.goto(2000,2000)
                laser.destroy()
                rockmaker.all_rocks.remove(rock)
                rockmaker.reserve_rocks.append(rock)
            if rock.distance(player) < 25:
                life -= 1 
                board.life -= 1
                board.update_scoreboard() 
                rock.goto(2000,2000)
                rockmaker.all_rocks.remove(rock)
                rockmaker.reserve_rocks.append(rock) 

    if life == 0:
        board.game_over()
        game_is_on = False
    
    if len(invaders) == 0:
        board.win_game() 
        game_is_on = False

    screen.update()


screen.exitonclick()