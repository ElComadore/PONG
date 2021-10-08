import os
import pygame as pg

main_dir = os.path.split(os.path.abspath(__file__))[0]
data_dir = os.path.join(main_dir, "data")


def load_image(name, colourKey=None):
    fullname = os.path.join(data_dir, name)
    try:
        image = pg.image.load(fullname)
    except pg.error:
        print('Cannot load image dumbass: ', fullname)
        raise SystemExit(str(pg.get_error()))
    image = image.convert()
    if colourKey is not None:
        if colourKey == -1:
            colourKey = image.get_at((0, 0))
        image.set_colorkey(colourKey, pg.RLEACCEL)
    return image, image.get_rect()


def load_sound(name):
    class NoneSound:
        def play(self):
            pass

    if not pg.mixer or not pg.mixer.get_init():
        return NoneSound()
    fullname = os.path.join(data_dir, name)
    try:
        sound = pg.mixer.Sound(fullname)
    except pg.error:
        print("Cant play that sound dumbass: ", fullname)
        raise SystemExit(str(pg.get_error()))
    return sound