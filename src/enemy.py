import pygame as pg
from util import load_image
from config import Config
import math
import random


class Enemy(pg.sprite.Sprite):
    def __init__(self, player, game):
        self.player = player
        self.game = game
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load(load_image("enemy30x50.gif"))
        self.rect = self.image.get_rect(center=(
            random.randint(50, Config.SCREEN_WIDTH.value - 60),
            random.randint(50, Config.SCREEN_HEIGHT.value - 120)
        ))
        self.direction = player.direction
        self.direction[0] = -self.direction[0]
        self.pos = pg.Vector2(self.rect.center)
        self.speed = 5

    def update(self):
        if not self.alive():
            return
        self.move()
        for bullet in self.game.bullets:
            if self.rect.colliderect(bullet.rect):
                self.kill()
                bullet.kill()
                bullet.rect.x = -300
                self.game.points += 1

    def move(self):
        dirvect = pg.math.Vector2(
            self.player.rect.x - self.rect.x,
            self.player.rect.y - self.rect.y
        )
        
        if dirvect.x != 0 or dirvect.y != 0:
            dirvect.normalize()
            dirvect.scale_to_length(self.speed)
            self.rect.move_ip(dirvect)
        