import pygame as pg
from util import load_image


class Bullet(pg.sprite.Sprite):
    def __init__(self, player, game):
        pg.sprite.Sprite.__init__(self)
        self.game = game
        self.angle = player.angle
        self.image = pg.image.load(load_image("bullet30x16.png"))
        self.org = self.image.copy()
        self.rect = self.image.get_rect(center = player.rect.center)
        self.direction = player.direction
        self.pos = pg.Vector2(self.rect.center)

        self.image = pg.transform.rotate(self.org, self.angle)
        self.rect = self.image.get_rect(center=self.rect.center)

    def update(self):
        if not self.alive():
            return
        self.image = pg.transform.rotate(self.org, self.angle)
        self.rect = self.image.get_rect(center=self.rect.center)
        self.move()
        if not pg.display.get_surface().get_rect().contains(self.rect):
            self.kill()

    def move(self):
        self.pos += self.direction * (self.game.dt * 0.5)
        self.rect.center = self.pos