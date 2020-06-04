import pygame
from random import randint

tacos = pygame.image.load("assets/tacos.png")


class Tacos(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.transform.scale(tacos, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.x = randint(0, 550)
        self.rect.y = 0

    def move(self, player):
        self.rect.y += 5
        if self.rect.y >= 400:
            player.life -= 1
            self.kill()
