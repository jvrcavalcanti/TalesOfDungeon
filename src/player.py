import pygame as pg
from util import load_image
from config import Config
from bullet import Bullet
import math


class Player(pg.sprite.Sprite):
    def __init__(self, screen, game):
        pg.sprite.Sprite.__init__(self)
        self.screen = screen
        self.game = game
        self.image = pg.image.load(load_image("player50x50.png"))
        self.org = self.image.copy()
        self.slash = pg.image.load(load_image("slash370x240.png"))
        self.rect = self.image.get_rect()
        self.velocity = 10
        self.rect.x = Config.SCREEN_WIDTH.value / 2
        self.rect.y = Config.SCREEN_HEIGHT.value / 2
        self.life = 5


        mx, my = pg.mouse.get_pos()
        self.angle = (180 / math.pi) * math.atan2(self.rect.x - mx, self.rect.y - my)
        self.direction = pg.Vector2(1, 0)
        self.post = pg.Vector2(self.rect.center)

    def update(self):
        key = pg.key.get_pressed()
        self.handle_key_press(key)

        for enemy in self.game.enemys:
            if self.rect.colliderect(enemy.rect) and enemy.alive():
                enemy.kill()
                enemy.rect.x = 1500
                self.life -= 1

        mx, my = pg.mouse.get_pos()
        self.angle = (180 / math.pi) * -math.atan2(my - self.rect.y, mx - self.rect.x)
        self.direction = pg.Vector2(1, 0).rotate(-self.angle)

        self.image = pg.image.load(load_image("player50x50.png"))
        if self.angle > 0 and self.angle > 90 or self.angle < 0 and self.angle < -90:
            self.image = pg.image.load(load_image("player2_50x50.png"))
            

        # Gira image
        # self.image = pg.transform.rotate(self.org, self.angle)
        # self.rect = self.image.get_rect(center=self.rect.center)

    def attack(self, game):
        bul = Bullet(self, game)
        self.game.sprites.add(bul)
        self.game.bullets.append(bul)

    def handle_key_press(self, key):
        if key[pg.K_w]:
            self.move(0, -1)
        if key[pg.K_s]:
            self.move(0, 1)
        if key[pg.K_d]:
            self.move(1, 0)
        if key[pg.K_a]:
            self.move(-1, 0)
        if key[pg.K_SPACE]:
            self.attack()

    def move(self, x, y):
        new_x = self.rect.x + (x * self.velocity)
        new_y = self.rect.y + (y * self.velocity)
        if new_x >= 0 and new_x < Config.SCREEN_WIDTH.value - 30:
            self.rect.x = new_x
        if new_y >= 0 and new_y < Config.SCREEN_HEIGHT.value - 60:
            self.rect.y = new_y