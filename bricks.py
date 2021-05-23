from colorama import init, Fore, Back, Style
from powerups import Powerups, expand_paddle
import random
import os

colormap = {
    0: Back.BLACK,
    1: Back.MAGENTA,
    2: Back.RED,
    3: Back.YELLOW,
    9: Back.WHITE,
    15: Back.BLUE,
}


class Brick():
    def __init__(self, x, y):
        self._base_xposition = x
        self._base_yposition = y
        self._base_activated = 1
        self._base_powerup = ''
        self._base_strength = 0
        self._base_color = colormap[self._base_strength]
        self._base_israin = 0

    def getXposition(self):
        return self._base_xposition

    def getYposition(self):
        return self._base_yposition

    def setXposition(self):
        self._base_xposition +=1

    def getActivated(self):
        return self._base_activated

    def setActivated(self):
        self._base_activated = 0
        return

    def setstrength(self):
        self._base_strength = 0
        return

    def setcolor(self):
        self._base_color = Back.BLACK
        return

    def israin(self):
        return self._base_israin


class nakli_brick(Brick):
    def __init__(self, x, y):
        super().__init__(x, y)
        self._base_strength = 1
        self._base_color = colormap[self._base_strength]
        return

    def collision(self, screen, paddle, bricks):
        os.system('aplay -q ./sounds/collision.wav&')
        paddle.setScore(10)
        self._base_strength -= 1
        self._base_color = colormap[self._base_strength]
        if(self._base_strength <= 0):
            self._base_activated = 0
        # self.setpowerup(screen)
        return

    def getStrength(self):
        return self._base_strength

    def getColor(self):
        return self._base_color


class sasti_brick(Brick):
    def __init__(self, x, y):
        super().__init__(x, y)
        self._base_strength = 2
        self._base_color = colormap[self._base_strength]
        return

    def collision(self, screen, paddle, bricks):
        os.system('aplay -q ./sounds/collision.wav&')
        paddle.setScore(10)
        self._base_strength -= 1
        self._base_color = colormap[self._base_strength]
        if(self._base_strength <= 0):
            self._base_activated = 0
        # self.setpowerup(screen)
        return

    def getStrength(self):
        return self._base_strength

    def getColor(self):
        return self._base_color


class birla_brick(Brick):
    def __init__(self, x, y):
        super().__init__(x, y)
        self._base_strength = 3
        self._base_color = colormap[self._base_strength]
        return

    def collision(self, screen, paddle, bricks):
        os.system('aplay -q ./sounds/collision.wav&')
        paddle.setScore(10)
        self._base_strength -= 1
        self._base_color = colormap[self._base_strength]
        if(self._base_strength <= 0):
            self._base_activated = 0
        # self.setpowerup(screen)
        return

    def getStrength(self):
        return self._base_strength

    def getColor(self):
        return self._base_color

class rainbow_brick(Brick):
    def __init__(self, x, y):
        super().__init__(x, y)
        self._base_strength = random.randint(1,3)           #change
        self._base_color = colormap[self._base_strength]
        self.__nocol = 0
        self._base_israin = 1
        return

    def changecolor(self):
        if(self.__nocol==0):
            self._base_strength = random.randint(1,3)
            self._base_color = colormap[self._base_strength]
        return 
    
    def collision(self, screen, paddle, bricks):
        os.system('aplay -q ./sounds/collision.wav&')
        self.__nocol +=1
        paddle.setScore(10)
        self._base_strength -= 1
        self._base_color = colormap[self._base_strength]
        if(self._base_strength <= 0):
            self._base_activated = 0
        # self.setpowerup(screen)
        return 

    def getStrength(self):
        return self._base_strength

    def getColor(self):
        return self._base_color

class ambuja_brick(Brick):
    def __init__(self, x, y):
        super().__init__(x, y)
        self._base_strength = 9
        self._base_color = colormap[self._base_strength]
        return

    def getStrength(self):
        return self._base_strength

    def getColor(self):
        return self._base_color


class rdx_brick(Brick):
    def __init__(self, x, y):
        super().__init__(x, y)
        self._base_strength = 15
        self._base_color = colormap[self._base_strength]
        return

    def collision(self, screen, paddle, bricks):
        os.system('aplay -q ./sounds/collision.wav&')
        
        paddle.setScore(240)
        rdx = []
        for i in range(len(bricks)):
            if(bricks[i].getStrength() == 15):
                rdx += [bricks[i]]

        b = screen.getGamewidth()/8

        a = [[[-2, -b], [-2, 0], [-2, -b]],
             [[0, -b], [0, 0], [0, b]],
             [[2, -b], [2, 0], [2, b]]]

        # for r in range(len(rdx)):
        #     for k in range(3):
        #         for j in range(3):
        #             xc = rdx[r].getXposition() + a[k][j][0]
        #             yc = rdx[r].getYposition() + a[k][j][0]

        #             print(str(xc) + ' ' + str(yc) )

        # for r in range(len(rdx)):
        #     for k in range(3):
        #         for j in range(3):
        #             xc = rdx[r].getXposition() + a[k][j][0]
        #             yc = rdx[r].getYposition() + a[k][j][0]
        #         for i in range(len(bricks)):
        #             if(bricks[i].getXposition() == xc and bricks[i].getYposition() == yc):
        #                 bricks[i].setstrength()
        #                 bricks[i].setcolor()
        #                 bricks[i].setActivated()
               

        for j in range(len(rdx)):
            xp = rdx[j].getXposition() - 2
            yp = rdx[j].getYposition()
            # print(xp)
            for i in range(len(bricks)):
                if(bricks[i].getXposition() == xp and bricks[i].getYposition() == yp):
                    # print(bricks[i].getXposition())
                    bricks[i].setstrength()
                    bricks[i].setcolor()
                    bricks[i].setActivated()

        for j in range(len(rdx)):
            xp = rdx[j].getXposition() + 2
            yp = rdx[j].getYposition()
            for i in range(len(bricks)):
                if(bricks[i].getXposition() == xp and bricks[i].getYposition() == yp):
                    bricks[i].setstrength()
                    bricks[i].setcolor()
                    bricks[i].setActivated()

        for j in range(len(rdx)):
            xp = rdx[j].getXposition()
            yp = rdx[j].getYposition() + b
            for i in range(len(bricks)):
                if(bricks[i].getXposition() == xp and bricks[i].getYposition() == yp):
                    bricks[i].setstrength()
                    bricks[i].setcolor()
                    bricks[i].setActivated()

        for j in range(len(rdx)):
            xp = rdx[j].getXposition()
            yp = rdx[j].getYposition() - b
            for i in range(len(bricks)):
                if(bricks[i].getXposition() == xp and bricks[i].getYposition() == yp):
                    bricks[i].setstrength()
                    bricks[i].setcolor()
                    bricks[i].setActivated()

        for j in range(len(rdx)):
            xp = rdx[j].getXposition() + 2
            yp = rdx[j].getYposition() + b
            for i in range(len(bricks)):
                if(bricks[i].getXposition() == xp and bricks[i].getYposition() == yp):
                    bricks[i].setstrength()
                    bricks[i].setcolor()
                    bricks[i].setActivated()

        for j in range(len(rdx)):
            xp = rdx[j].getXposition() - 2
            yp = rdx[j].getYposition() - b
            for i in range(len(bricks)):
                if(bricks[i].getXposition() == xp and bricks[i].getYposition() == yp):
                    bricks[i].setstrength()
                    bricks[i].setcolor()
                    bricks[i].setActivated()

        for j in range(len(rdx)):
            xp = rdx[j].getXposition() + 2
            yp = rdx[j].getYposition() - b
            for i in range(len(bricks)):
                if(bricks[i].getXposition() == xp and bricks[i].getYposition() == yp):
                    bricks[i].setstrength()
                    bricks[i].setcolor()
                    bricks[i].setActivated()

        for j in range(len(rdx)):
            xp = rdx[j].getXposition() - 2
            yp = rdx[j].getYposition() + b
            for i in range(len(bricks)):
                if(bricks[i].getXposition() == xp and bricks[i].getYposition() == yp):
                    bricks[i].setstrength()
                    bricks[i].setcolor()
                    bricks[i].setActivated()

        for j in range(len(rdx)):
            xp = rdx[j].getXposition()
            yp = rdx[j].getYposition()
            for i in range(len(bricks)):
                if(bricks[i].getXposition() == xp and bricks[i].getYposition == yp):
                    bricks[i].setstrength()
                    bricks[i].setcolor()
                    bricks[i].setActivated()

        return

    def getStrength(self):
        return self._base_strength

    def getColor(self):
        return self._base_color
