from colorama import init, Fore, Back, Style
from random import randint
import os

class Ball():
    def __init__(self, x, y,screen):
        self.__xposition = x
        self.__yposition = y
        self.__xvelocity = 1
        self.__yvelocity = 1
        self.__speed = screen.getGameheight()/100
        self.__free = 0

    def getfree(self):
        return self.__free

    def getXposition(self):
        return self.__xposition

    def getYposition(self):
        return self.__yposition

    def getXvelocity(self):
        return self.__xvelocity

    def getYvelocity(self):
        return self.__yvelocity

    def getSpeed(self):
        return self.__speed

    def setfree(self,ch):
        self.__free = ch

    def setXposition(self,ch):
        self.__xposition = ch

    def setYposition(self,ch):
        self.__yposition = ch

    def setXvelocity(self,ch):
        self.__xvelocity = ch

    def setYvelocity(self,ch):
        self.__yvelocity = ch

    def setSpeed(self,ch):
        self.__speed = ch

    def initializeBall(self, screen, inp):
        self.removeBall(screen)
        if(inp == 'a' or inp == 'A'):
            self.__yposition -= 1
        elif(inp == 'd' or inp == 'D'):
            self.__yposition += 1
        screen.setGamescreen(self.__xposition, self.__yposition, 'O')

    def setBall(self, screen, x, y):
        screen.setGamescreen(x, y, 'O')
        return

    def removeBall(self, screen):
        screen.setGamescreen(self.__xposition, self.__yposition, Back.BLACK)
        return

    def CollisionwithWall(self, paddle, screen, ch):
        # k1 = min(self.__xposition, self.__xposition + self.__xvelocity)
        # k2 = max(self.__xposition, self.__xposition + self.__xvelocity)
        # k3 = min(self.__yposition, self.__yposition + self.__yvelocity)
        # k4 = max(self.__yposition, self.__yposition + self.__yvelocity)
        # for i in range(k1, k2):
        #     for j in range(k3, k4):
        #         if(j >= screen.getGamewidth() -1):
        #             self.__yvelocity = -self.__yvelocity
        #             break
        #         elif(j <= 0):
        #             self.__yvelocity = -self.__yvelocity
        #             break
        #         elif(i <= 0):
        #             self.__xvelocity = -1 * self.__xvelocity
        #             break
        #         if( j != k4):
        #             break

        if(ch == 'd'):
            paddle.setLive()
            paddle.removepaddle(screen)
            paddle.setStartpaddle(int(screen.getGamewidth()/2))
            if(paddle.getLives() <= 0):
                screen.gameover(paddle)
            x = paddle.getStartpaddle() 
            y = paddle.getStartpaddle() + paddle.getLength() -1
            # mid = int((x + y)/2)
            self.__free = 0
            self.__xposition = screen.getGameheight()-2
            self.__yposition = randint(x, y)
            self.__xvelocity = 1
            self.__yvelocity = 1

        if(ch == 'u'):
            self.__xvelocity = -self.__xvelocity
            self.__xposition = self.__xposition + self.__xvelocity

        if(ch == 'r'):
            self.__yvelocity = -self.__yvelocity
            self.__yposition = self.__yposition + self.__yvelocity
        # print('\nchanged:')
        # print(self.__xposition)
        # print(self.__yposition)
        if(ch == 'l'):
            self.__yvelocity = -self.__yvelocity
            self.__yposition = self.__yposition + self.__yvelocity        
        return
    
    def CollisionwithPaddle(self,screen,paddle):
        # exit()
        x = paddle.getStartpaddle() 
        y = paddle.getStartpaddle() + paddle.getLength() -1
        mid = int((x + y)/2)
        diff = abs(mid - self.__yposition)
        if(self.__yposition < mid):
            self.__yvelocity = (self.__yvelocity - diff)
        else:
            self.__yvelocity = (self.__yvelocity + diff)

        self.__xvelocity = -self.__xvelocity
        return

    def loopCheck(self, screen,paddle, bricks):
        # print('\nin:')
        # print(self.__xposition)
        # print(self.__yposition)
        # print(screen.getGameheight())
        # print(screen.getGamewidth())
        xp = self.__xposition 
        yp = self.__yposition 
        xv = self.__xvelocity 
        yv = self.__yvelocity

        if(xv < 0 ):
            a1 = xp + xv
            a2 = xp
        # elif(xv ==0):
        #     a1 = xp + xv
        #     a2 =yp +1
        else:
            a1 = xp
            a2 = xp + xv

        if(yv < 0 ):
            b1 = yp + yv 
            b2 = yp
        # elif(yv == 0):
        #     b1 = yp + yv 
        #     b2 = yp+ 1
        else:
            b1 = yp
            b2 = yp + yv
        
        biczz =len(bricks)
        flag = 0
        # print('looooop')
        while a1 < a2:
            # print(a1)
            while b1 < b2:
                # print(b1) 
                for i in range(len(bricks)):
                    # print(str(self.__xvelocity) + ' ' +str(self.__yvelocity))
                    if(bricks[i].getActivated() == 1):
                        # biczz +=1
                        # print(str(bricks[i].getXposition()) + ' ' +str(bricks[i].getYposition()))
                        if(a1 >= bricks[i].getXposition() and a1 <= bricks[i].getXposition() + 1 and b1 >= bricks[i].getYposition() and b1<= bricks[i].getYposition() + int(screen.getGamewidth()/8) ):
                            # print('x')
                            flag =1
                            if(bricks[i].getStrength() != 9):
                                biczz -=1
                                if(biczz == 0):
                                    screen.levelup(screen,self,paddle)
                                    # screen.gameover(paddle)
                                    return
                                bricks[i].collision(screen,paddle,bricks)
                            # self.__xposition = a1
                            # self.__yvelocity = -self.__yvelocity
                            if(xv < 0 and yv < 0 or xv >= 0 and yv >= 0):
                                # self.__yposition = b1
                                self.__xvelocity = -self.__xvelocity
                            elif(xv < 0 and yv >= 0 or xv >= 0 and yv < 0):
                                # self.__xposition = a1
                                self.__yvelocity = -self.__yvelocity
                            return
                    # screen.gridchange(paddle)
                b1 +=1
            a1 +=1

    def collisionCheck(self, screen, paddle,bricks):
        # print('\nin:')
        # print(self.__xposition)
        # print(self.__yposition)
        if(self.__xposition < 0):
            self.CollisionwithWall(paddle, screen, 'u')
        if(self.__xposition >= screen.getGameheight()):
            self.CollisionwithWall(paddle, screen, 'd') 
        if(self.__yposition >= screen.getGamewidth()- 1):
            self.CollisionwithWall(paddle, screen, 'r')
        if(self.__yposition < 0):
            self.CollisionwithWall(paddle, screen, 'l')
        if(self.__xposition >= screen.getGameheight() -1 and (self.__yposition >= paddle.getStartpaddle() and self.__yposition < paddle.getStartpaddle() + paddle.getLength() )):
            self.CollisionwithPaddle(screen,paddle)
        # self.loopCheck(screen, bricks)
        return

    def release(self, screen, paddle):
        x = paddle.getStartpaddle()
        l = paddle.getLength()
        mid = int((x + (x+l))/2)

        self.__xvelocity = -1 * self.__xvelocity
        if(self.__yposition < mid):
            self.__yvelocity = -1 * self.__yvelocity
        else:
            self.__yvelocity = self.__yvelocity
        
        self.__free = 1
        # print('release')
        # print(self.__xposition)
        # print(self.__yposition)
        return

    def movement(self, screen, paddle, bricks):
        self.removeBall(screen)
        self.__xposition += self.__xvelocity
        self.__yposition += self.__yvelocity
        # print('move')
        # print(self.__xposition)
        # print(self.__yposition)
        self.collisionCheck(screen, paddle,bricks)
        self.loopCheck(screen,paddle, bricks)
        self.setBall(screen, self.__xposition, self.__yposition)
       
        return