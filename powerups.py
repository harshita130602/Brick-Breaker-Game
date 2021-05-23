class Powerups():
    def __init__(self, x, y):
        self._base_moving = 0
        self._base_activated = 0
        self._base_xposition = x
        self._base_yposition = y
        self._base_activetime = 0

    def getXposition(self):
        return self._base_xposition

    def getYposition(self):
        return self._base_yposition

    def getActivated(self):
        return self._base_activated

    def activate(self):
        self._base_activated = 1
        return

    def deactivate(self):
        self._base_activated = 0
        return

    def getactivetime(self):
        return self._base_activetime

    def addtime(self):
        self._base_activetime = self._base_activetime + 10
        return

    def reducetime(self):
        self._base_activetime -= 1
        return

    def getmoving(self):
        return self._base_moving


class expand_paddle(Powerups):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.shape = 'e'
        return

    def move(self, paddle, screen):
        if(self._base_moving == 0):
            self._base_moving = 1

        screen.setGamescreen(self._base_xposition, self._base_yposition, '')
        self._base_xposition += 1

        if(self._base_activated == 0 and self._base_moving == 1):
            if(self._base_xposition == screen.getGameheight()):
                self._base_moving = 0

            if(self._base_xposition == screen.getGameheight()-1 and self._base_yposition >= paddle.getStartpaddle() and self._base_yposition <= paddle.getStartpaddle() + paddle.getLength()):
                self._base_moving = 0
                self.addtime()

                paddle.setLength(paddle.getLength() + 5)

        screen.setGamescreen(self._base_xposition,
                             self._base_yposition, self.shape)
        return

    def remove(self, paddle, screen):
        if(self._base_activated == 1 and self._base_activetime <= 0):
            paddle.setLength(paddle.getLength() - 5)
            self.deactivate()
        return

    # def assignbrick(self, screen, bricks):
    #     for b in range(len(bricks)):
    #         if(bricks[b].getXposition() == self._base_xposition and bricks[b].getYposition() == self._base_yposition):
    #             bricks[b].assignpowerup(screen, self.shape)
    #     return

    def checkactivity(self,bricks,paddle,screen):
        for i in range(len(bricks)):
            if(bricks[i].getXposition() == self._base_xposition):
                if(bricks[i].getActivated()==0):
                    # exit()
                    self.move(paddle,screen)

    def getshape(self):
        return self.shape

class shrink_paddle(Powerups):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.shape = 's'
        return

    def move(self, paddle, screen):
        if(self._base_moving == 0):
            self._base_moving = 1

        self._base_xposition += 3

        if(self._base_activated == 0 and self._base_moving == 1):
            if(self._base_xposition == screen.getGameheight()):
                self._base_moving = 0

            if(self._base_xposition == paddle.getXposition()):
                self._base_moving = 0
                self.addtime()

                paddle.setLength(paddle.getLength() - 5)
        return

    def remove(self, paddle, screen):
        if(self._base_activated == 1 and self._base_activetime <= 0):
            paddle.setLength(paddle.getLength() + 5)
            self.deactivate()
        return
