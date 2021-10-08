import pygame as pg
import numpy as np
from mediaHandling import load_image, load_sound


class Ball(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image, self.rect = load_image('ball.png', -1)
        self.area = pg.display.get_surface().get_rect()
        self.rect.center = self.area.center
        self.velocity = (np.array((-1, 1))[np.random.randint(0, 2)]*5, np.array((-1, 1))[np.random.randint(0, 2)]*5)

    def update(self, paddleGroupList, score, sound):
        boop = load_sound('boop.wav')
        oldVel = self.__getattribute__('velocity')

        if self.rect.top < self.area.top:
            self.velocity = (self.velocity[0], -self.velocity[1])
            self.rect.top = 0
        elif self.rect.bottom > self.area.bottom:
            self.velocity = (self.velocity[0], -self.velocity[1])
            self.rect.bottom = self.area.bottom

        elif self.rect.right < self.area.left:
            score.player2Up()
            self.reset()

        elif self.rect.left > self.area.right:
            score.player1Up()
            self.reset()

        for paddle in paddleGroupList:
            if paddle.rect.colliderect(self.rect):

                self.velocity = (-1 * self.velocity[0]*(2-np.power(abs(self.velocity[0]/12), 1./10)), self.velocity[1] + (int(paddle.down) - int(paddle.up)) * 2.5)

                if self.rect.right > paddle.rect.left > self.rect.left:
                    self.rect.right = paddle.rect.left + np.floor(abs(self.velocity[0]))

                elif self.rect.left < paddle.rect.right < self.rect.right:
                    self.rect.left = paddle.rect.right - np.floor(abs(self.velocity[0]))

        if oldVel != self.velocity and sound:
            boop.play()

        newpos = self.rect.move(np.ceil(self.velocity[0]), np.ceil(self.velocity[1]))

        self.rect = newpos

    def reset(self):
        self.rect.center = self.area.center
        self.velocity = (np.array((-1, 1))[np.random.randint(0, 2)]*5, np.array((-1, 1))[np.random.randint(0, 2)]*5)

    def getvelocity(self):
        return self.velocity