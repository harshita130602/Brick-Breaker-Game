from colorama import init, Fore, Back, Style
import os

class Paddle():
    def __init__(self, positionpaddle):
        self.__live = 3
        self.__score = 0
        self.__timetaken = 0
        self.__startpaddle = positionpaddle
        self.__length = 15

    def getLives(self):
        return self.__live

    def setLive(self):
        os.system('aplay -q ./sounds/lose_live.wav&')
        self.__live -= 1
        return

    def setStartpaddle(self, x):
        self.__startpaddle = x
        return

    def getScore(self):
        return self.__score

    def setScore(self, inc):
        self.__score = self.__score + inc
        return

    def getTimetaken(self):
        return self.__timetaken

    def setTimetaken(self,time):
        self.__timetaken = time
        return

    def getStartpaddle(self):
        return self.__startpaddle

    def getLength(self):
        return self.__length

    def setLength(self, l):
        self.__length = l
        return

    def removepaddle(self,screen):
        for i in range(self.__startpaddle, self.__startpaddle + self.__length):
            screen.setGamescreen(screen.getGameheight()-1, i, Back.BLACK)
        return

    def movement(self, screen, inp):
        # for i in range(self.__startpaddle, self.__startpaddle + self.__length):
        #     screen.setGamescreen(screen.getGameheight()-1, i, Back.BLACK)
        if(inp == 'a' or inp == 'A'):
            if(self.__startpaddle > 0):
                screen.setGamescreen(screen.getGameheight() - 1, self.__startpaddle - 1, Back.CYAN)
                screen.setGamescreen(screen.getGameheight() - 1, self.__startpaddle + self.__length - 1, Back.BLACK)
                self.__startpaddle -= 1
        if(inp == 'd' or inp == 'D'):
            if(self.__startpaddle + self.__length < screen.getGamewidth()):
                screen.setGamescreen(
                    screen.getGameheight() - 1, self.__startpaddle, Back.BLACK)
                screen.setGamescreen(screen.getGameheight(
                ) - 1, self.__startpaddle + self.__length - 1, Back.CYAN)
                self.__startpaddle += 1
        return
