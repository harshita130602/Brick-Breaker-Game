import os
import time
from time import sleep
from screen import Screen
from paddle import Paddle
from ball import Ball
from random import randint
from input import Get, input_to
from powerups import Powerups, expand_paddle, shrink_paddle
from colorama import init, Fore, Back, Style



size = os.get_terminal_size()

screen = Screen(size[0], size[1])

b_width = int(screen.getGamewidth()/8)
powerup = []
# powerup += [expand_paddle(0,0)]
powerup += [expand_paddle(5*2, 5*b_width)]
# powerup += [expand_paddle(13,1*b_width)]

# for i in range(len(powerup)):
#     powerup[i].assignbrick(screen, bricks)

paddle = Paddle(int(size[0]/2))

x = paddle.getStartpaddle()
y = paddle.getStartpaddle() + paddle.getLength() - 1
mid = int((x + y)/2)
ball = Ball(screen.getGameheight()-2, randint(x, y), screen)

screen.levelup(screen,ball, paddle)
bricks = screen.initializeGamescreen()

x = 0
start_time = time.time()
l_start_time = time.time()
prev_time = time.time()
p_ball_time = time.time()
flag_f = 0
curr_fall_time = time.time()
p_fall_time = time.time()


Get().hide_cursor()
print("\033[2J")
while True:
    # if(screen.getlevel()!=0):
    #     bricks = screen.initializeGamescreen()
    curr_time = time.time()
    curr_fall_time = time.time()
    c_ball_time = time.time()


    if(curr_fall_time - l_start_time >= 5 and flag_f != 1):
        xclear = bricks[0].getXposition()
        for i in range(screen.getGamewidth()):
            screen.setGamescreen(xclear,i,Back.BLACK)

        for b in bricks:
            b.setXposition()
        flag_f = 1
        p_fall_time = curr_fall_time
    
    if(flag_f==1 and curr_fall_time - p_fall_time>=3):
        xclear = bricks[0].getXposition()
        for i in range(screen.getGamewidth()):
            screen.setGamescreen(xclear,i,Back.BLACK)

        for b in bricks:
            b.setXposition()
        p_fall_time = curr_fall_time        

    if(flag_f==1 and bricks[len(bricks)-1].getXposition() +1 == screen.getGameheight()-1):
        screen.gameover(paddle)

    for i in range(len(powerup)):
        powerup[i].checkactivity(bricks, paddle, screen)

    if(curr_time - prev_time >= 0.05):
        print("\033[0;0H")
        paddle.setTimetaken(int(curr_time-start_time))
        screen.printScreen(ball, paddle, powerup)
        prev_time = curr_time

    if(ball.getfree() == 1 and c_ball_time - p_ball_time >= ball.getSpeed()):
        ball.movement(screen, paddle, bricks)
        p_ball_time = c_ball_time

    inp = input_to(Get())
    if(inp == 'n' or inp == 'N'):
        bricks = screen.levelup(screen,ball, paddle)
    if(inp == None):
        inp = ""
    if (inp == ' ' or inp == ' '):
        if(ball.getfree() == 0):
            ball.release(screen, paddle)
    if (inp == 'a' or inp == 'A' or inp == 'd' or inp == 'D'):
        if(paddle.getStartpaddle() > 0 and paddle.getStartpaddle() + paddle.getLength() < screen.getGamewidth()):
            if(ball.getfree() == 0):
                ball.initializeBall(screen, inp)
        paddle.movement(screen, inp)
    if(inp == 'x' or inp == 'X'):
        exit()

    x += 1
