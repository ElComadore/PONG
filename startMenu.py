import pygame as pg
from mediaHandling import load_image, load_sound


class gameMode(pg.sprite.Sprite):
    def __init__(self, mode, centerPos):
        pg.sprite.Sprite.__init__(self)
        self.font = pg.font.Font(None, 72)
        self.mode = mode
        self.image = self.font.render(mode, True, (255, 255, 255))
        self.rect = self.image.get_rect()
        self.rect.center = centerPos

    def isHovered(self, colour):
        self.image = self.font.render(self.mode, True, colour)

    def notHovered(self):
        self.image = self.font.render(self.mode, True, (255,255,255))

class soundOption(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.screen = pg.display.get_surface()

        self.fullImage, self.fullRect = load_image('SoundOption.png')
        self.rect = pg.Rect(0, 0, self.fullImage.get_width(), self.fullImage.get_width())
        self.soundOffRect = pg.Rect(0, self.fullImage.get_width(), self.fullImage.get_width(), self.fullImage.get_width())

        self.image = pg.Surface(self.rect.size)
        self.image.blit(self.fullImage, (0, 0))
        self.rect.topright = self.screen.get_rect().topright
        self.soundOn = True

    def muteToggle(self):
        if self.soundOn:
            self.image.blit(self.fullImage, (0, 0), self.soundOffRect)
            self.soundOn = False
        else:
            self.image.blit(self.fullImage, (0, 0))
            self.soundOn = True
