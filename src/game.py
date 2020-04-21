import pygame as pg
from colors import Colors
from config import Config
from player import Player
from enemy import Enemy
from background import Background


class Game:
    def __init__(self, width = 1365, height = 730):
        self.screen = pg.display.set_mode(
            (Config.SCREEN_WIDTH.value, Config.SCREEN_HEIGHT.value),
            pg.FULLSCREEN
        )
        self.clock: pg.time.Clock = pg.time.Clock()
        self.running = True
        self.fps = Config.FPS.value
        self.sprites = pg.sprite.Group()
        self.player = Player(self.screen, self)
        self.points = 0
        self.dt = 0
        self.bullets = []
        self.enemys = []
        self.back = Background()
        
        self.sprites.add(self.player)
        pg.display.set_caption("Tales of Dungeon")
        self.text_points = pg.font.Font(None, 30).render(
            "Pontos: {}".format(self.points),
            True,
            Colors.WHITE.value
        )
        self.text_lifes = pg.font.Font(None, 30).render(
            "Vidas: {}".format(self.player.life),
            True,
            Colors.WHITE.value
        )

    def add_enemy(self):
        enemy = Enemy(self.player, self)
        self.sprites.add(enemy)
        self.enemys.append(enemy)

    def run(self):
        time = 0
        time_spawn = 1
        while self.running:
            self.dt = self.clock.tick(self.fps)
            self.text_points = pg.font.Font(None, 30).render(
                "Pontos: {}".format(self.points),
                True,
                Colors.WHITE.value
            )
            self.text_lifes = pg.font.Font(None, 30).render(
                "Vidas: {}".format(self.player.life),
                True,
                Colors.WHITE.value
            )

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.running = False
                if event.type == pg.MOUSEBUTTONDOWN:
                    self.player.attack(self)

            if self.player.life == 0:
                self.running = False

            if time >= 50:
                time_spawn += 0.1
                time = 0
                self.add_enemy()
            
            self.sprites.update()
            self.screen.fill(Colors.BLACK.value)
            self.screen.blit(self.back.image, self.back.rect)
            self.screen.blit(self.text_points, (0, 0))
            self.screen.blit(self.text_lifes, (150, 0))
            self.sprites.draw(self.screen)
            pg.display.flip()
            time += time_spawn