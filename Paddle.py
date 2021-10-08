import pygame as pg
from mediaHandling import load_image, load_sound


class Paddle(pg.sprite.Sprite):
    def __init__(self, player):
        pg.sprite.Sprite.__init__(self)
        self.image, self.rect = load_image('paddle.png', -1)
        self.area = pg.display.get_surface().get_rect()
        if player == 1:
            self.rect.center = (self.area.left + 50, self.area.centery)
        else:
            self.rect.center = (self.area.right - 50, self.area.centery)
        self.step = 5
        self.up = False
        self.down = False

    def update(self):
        if self.down:
            newpos = self.rect.move(0, self.step)
            if not self.area.contains(newpos):
                if self.rect.bottom > self.area.bottom:
                    newpos = self.rect.move(0, self.step - (self.rect.bottom - self.area.bottom))
                    self.rect = newpos
                    return
            self.rect = newpos
        elif self.up:
            newpos = self.rect.move(0, -self.step)
            if not self.area.contains(newpos):
                if self.rect.top < self.area.top:
                    newpos = self.rect.move(0, -(self.step - (self.area.top - self.rect.top)))
                    self.rect = newpos
                    return
            self.rect = newpos
        else:
            pass

    def aiUpdate(self, ball):
        if self.rect.centery < ball.rect.centery:
            self.up = 0
            self.down = 1
        elif self.rect.centery > ball.rect.centery:
            self.up = 1
            self.down = 0

    def changeUp(self):
        self.up = not self.up

    def changeDown(self):
        self.down = not self.down