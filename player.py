import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("assets/player.png")
        self.rect = self.image.get_rect()
        self.rect.x = 100
        self.rect.y = 280
        self.velocity = 5
        self.life = 3

    def blit(self, screen):
        screen.blit(self.image, self.rect)

    def move_left(self):
        self.rect.x -= self.velocity

    def move_right(self):
        self.rect.x += self.velocity

    def collide(self, tacos):
        return pygame.sprite.spritecollide(self, tacos, True)

    def isDead(self):
        return not bool(self.life)
