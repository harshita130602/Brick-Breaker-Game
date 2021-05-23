import numpy as np
from colorama import init, Fore, Back, Style
from bricks import Brick, nakli_brick, sasti_brick, birla_brick, ambuja_brick,rdx_brick, rainbow_brick
from ball import Ball
from input import Get
from powerups import Powerups, expand_paddle, shrink_paddle
from random import randint
import os

class Screen():

    def __init__(self, display_width, display_height):
        self.__displaywidth = display_width
        self.__displayheight = display_height
        self.__gamewidth = display_width
        self.__gameheight = display_height - 7
        self.grid_c = 0
        self.grid = []
        self.row_layout = 0
        self.col_layout = 0

        self.__game = []
        self.bricks = []
        self.rainind = []

    def levelup(self,screen,ball,paddle):
        os.system('aplay -q ./sounds/level_up.wav&')
        if(self.grid_c>=1):
            paddle.removepaddle(screen)
            paddle.setStartpaddle(int(screen.getGamewidth()/2))
            x = paddle.getStartpaddle() 
            y = paddle.getStartpaddle() + paddle.getLength() -1
            # mid = int((x + y)/2)
            ball.setfree(0)
            ball.setXposition(screen.getGameheight()-2)
            ball.setYposition(randint(x, y))
            ball.setXvelocity(1)
            ball.setYvelocity(1)


        self.grid_c += 1
        print(self.grid_c)
        bricks = self.gridchange(paddle)
        return bricks

    def getlevel(self):
        return self.grid_c

    def gridchange(self,paddle):
        if(self.grid_c==1):
            self.grid = [
                    [1, 2, 3, 100, 2, 3, 1, 2],
                    [2, 3, 9, 2, 9, 2, 3, 1],
                    [1, 15, 15, 15, 15, 15, 15, 2],
                    [2, 1, 9, 2, 9, 2, 3, 1],
                    [1, 3, 2, 9, 2, 3, 1, 2],
                    [2, 1, 3, 2, 3, 2, 3, 1],
                    ]

            self.row_layout = len(self.grid) 
            self.col_layout = len(self.grid[0])

        if(self.grid_c ==2):
            self.grid = [[2, 3, 100, 2, 3, 1],
                    [3, 9, 2, 9, 2, 3],
                    [15, 15, 15, 15, 15, 15],
                    [1, 9, 2, 9, 2, 3],
                    [3, 2, 9, 2, 3, 1],
                    ]
            self.row_layout = len(self.grid)
            self.col_layout = len(self.grid[0])

        if(self.grid_c ==3):
            self.grid = [[2, 3, 100, 2, 3, 1,2],
                    [3, 9, 2, 9, 2, 3,1],
                    [15, 15, 15, 15, 15, 15,2],
                    [1, 9, 2, 9, 2, 3,1],
                    [3, 2, 9, 2, 3, 1,2],
                    [1, 3, 2, 3, 2, 3,1],
                    [2, 3, 100, 2, 3, 1,2],
                    ]
            self.row_layout = len(self.grid)
            self.col_layout = len(self.grid[0])  

        if(self.grid_c == 4):
            self.gameover(paddle) 

        # print(self.grid)
        bricks = self.initializeGamescreen()
        return bricks       

    def getDisplaywidth(self):
        return self.__displaywidth

    def getDisplayheight(self):
        return self.__displayheight

    def getGamewidth(self):
        return self.__gamewidth

    def getGameheight(self):
        return self.__gameheight

    def setGamescreen(self, x, y, ch):
        self.__game[x][y] = ch
        return

    def initializeGamescreen(self):
        self.__game = []
        self.bricks = []
        self.rainind = []
        brick_width = int(self.__gamewidth / 8)

        nakli = []
        sasti = []
        birla = []
        ambuja = []
        rdx = []
        rainbow = []
        for i in range(self.row_layout):
            for j in range(self.col_layout):
                if(self.grid[i][j] == 1):
                    self.bricks += [nakli_brick(i * 2, j * brick_width)]
                    nakli += [nakli_brick(i * 2, j * brick_width)]
                if(self.grid[i][j] == 2):
                    self.bricks += [sasti_brick(i * 2, j * brick_width)]
                    sasti += [sasti_brick(i * 2, j * brick_width)]
                if(self.grid[i][j] == 3):
                    self.bricks += [birla_brick(i * 2, j * brick_width)]
                    birla += [birla_brick(i * 2, j * brick_width)]
                if(self.grid[i][j] == 9):
                    self.bricks += [ambuja_brick(i * 2, j * brick_width)]
                    ambuja += [ambuja_brick(i * 2, j * brick_width)]
                if(self.grid[i][j] == 15):
                    self.bricks += [rdx_brick(i * 2, j * brick_width)]
                    rdx += [rdx_brick(i * 2, j * brick_width)]
                if(self.grid[i][j] == 100):
                    self.bricks += [rainbow_brick(i * 2, j * brick_width)]
                    rainbow += [rainbow_brick(i * 2, j * brick_width)]

        for i in range(self.__gameheight):
            curr_row = []
            for j in range(self.__gamewidth):
                curr_row.append(Back.BLACK)
            self.__game += [curr_row]
        self.__game = np.asarray(self.__game)
        return self.bricks

    def getGame(self):
        return self.__game

    def printScreen(self, ball, paddle, powerup):

        for s in self.bricks:
            if(s.israin()==1):
                s.changecolor()

        # header

        current_row = "ARCADE GAME : Player1"
        print(Fore.WHITE + Back.BLUE + Style.BRIGHT +
              current_row.center(self.__displaywidth)+Style.RESET_ALL)
        current_row = " "
        print(Fore.WHITE + Back.BLUE + Style.BRIGHT +
              current_row.center(self.__displaywidth))

        # scorecard
        current_row = ("Lives: " + str(paddle.getLives()) + " | " + "Score: " +
                       str(paddle.getScore()) + " | " + "Time: " + str(paddle.getTimetaken()))
        print(Fore.WHITE + Back.RED + Style.BRIGHT +
              current_row.center(self.__displaywidth) + Style.RESET_ALL)
        # print(Back.BLACK + Back.RESET)
        
        for i in range(self.__displaywidth):
            print(Back.BLACK + " ", end='')

        # bricks layout
        brick_width = int(self.__displaywidth / 8)

        x = 0
        while x < len(self.bricks):
            for i in range(brick_width):
                for b in range(brick_width):
                    if self.bricks[x].getStrength() <= 0:
                        self.__game[self.bricks[x].getXposition()][self.bricks[x].getYposition() + b] = Back.BLACK
                        self.__game[self.bricks[x].getXposition() + 1][self.bricks[x].getYposition() + b] = Back.BLACK
                    else:
                        self.__game[self.bricks[x].getXposition()][self.bricks[x].getYposition() + b] = self.bricks[x].getColor()
                        self.__game[self.bricks[x].getXposition() + 1][self.bricks[x].getYposition() + b] = self.bricks[x].getColor()
            x += 1

        # ball
        self.__game[ball.getXposition()][ball.getYposition()] ='O'

        # #power up
        # for i in range(len(powerup)):
        #     # if(powerup[i].getActivated() == 1):
        #     self.__game[powerup[i].getXposition()][powerup[i].getYposition()] =  powerup[i].getshape()
            
        # paddle line
        x = paddle.getStartpaddle()
        while x < paddle.getStartpaddle() + paddle.getLength():
            self.__game[self.__gameheight-1][x] = Back.CYAN
            x += 1

        # print
        for i in range(self.__gameheight):
            num = self.__gamewidth
            if(i==ball.getXposition() and i != self.__gameheight -1):
                num = self.__gamewidth -1
            for j in range(num):
                print(self.__game[i][j] + " ", end='')


        # footer
        print(Back.WHITE + Fore.RED + Style.BRIGHT +
              "A: left | D: right | <space>: release ball | X: quit" + Style.RESET_ALL)

        return

    def gameover(self,paddle):
        os.system('aplay -q ./sounds/game_over.wav&')
        print("\033[2J")
        print(Fore.CYAN + Style.BRIGHT + "                                                     ".center(self.__displaywidth))
        print(Fore.CYAN + Style.BRIGHT + "  _____                         ____                 ".center(self.__displaywidth))
        print(Fore.CYAN + Style.BRIGHT + " / ____|                       / __ \                ".center(self.__displaywidth))
        print(Fore.CYAN + Style.BRIGHT + "| |  __  __ _ _ __ ___   ___  | |  | |_   _____ _ __ ".center(self.__displaywidth))
        print(Fore.CYAN + Style.BRIGHT + "| | |_ |/ _` | '_ ` _ \ / _ \ | |  | \ \ / / _ \ '__|".center(self.__displaywidth))
        print(Fore.CYAN + Style.BRIGHT + "| |__| | (_| | | | | | |  __/ | |__| |\ V /  __/ |   ".center(self.__displaywidth))
        print(Fore.CYAN + Style.BRIGHT + " \_____|\__,_|_| |_| |_|\___|  \____/  \_/ \___|_|   ".center(self.__displaywidth))
        print(Fore.CYAN + Style.BRIGHT + "                                                     ".center(self.__displaywidth))
        print(Fore.CYAN + Style.BRIGHT + "                                                     ".center(self.__displaywidth))
        print(Fore.WHITE + Back.RED + Style.BRIGHT +("Lives: " + str(paddle.getLives()) + " | " + "Score: " + str(paddle.getScore()) + " | " + "Time: " + str(paddle.getTimetaken())).center(self.__displaywidth) + Style.RESET_ALL)
        #SCORE
        Get().show_cursor()
        exit()
        return