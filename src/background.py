import pygame as pg
from util import load_image
from config import Config


class Background(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load(load_image("back1974x730.png"))
        self.rect = self.image.get_rect()