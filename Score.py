import pygame as pg
from mediaHandling import load_image, load_sound


class Score(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.player1 = 0
        self.player2 = 0
        self.font = pg.font.Font(None, 72)
        self.scorerender()

    def player1Up(self):
        self.player1 = self.player1 + 1
        self.scorerender()

    def player2Up(self):
        self.player2 = self.player2 + 1
        self.scorerender()

    def scorerender(self):
        self.image = self.font.render(str(self.player1) + ' - ' + str(self.player2), 1, (255, 255, 255))
        self.rect = self.image.get_rect()
        self.rect.center = (pg.display.get_surface().get_rect().centerx, 50)