import pygame
from pygame.locals import *
from player import Player
from projectile import Tacos

pygame.init()

screen = pygame.display.set_mode((600, 400))

run = True

player = Player()

clock = pygame.time.Clock()

all_tacos = pygame.sprite.Group()

t = 0

score = 0

sound = pygame.mixer.Sound("assets/yummy.wav")

font = pygame.font.SysFont("Arial", 30)

font_go = pygame.font.SysFont("Arial", 50)

while run:
    screen.fill((255, 255, 255))
    if not player.isDead():
        key = pygame.key.get_pressed()
        if key[K_LEFT]:
            player.move_left()
        if key[K_RIGHT]:
            player.move_right()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        player.blit(screen)
        all_tacos.draw(screen)
        score_surf = font.render(f"Score : {score}", True, (0, 0, 0))
        life_surf = font.render(f"Life : {player.life}", True, (0, 0, 0))
        screen.blit(score_surf, (0, 0))
        screen.blit(life_surf, (screen.get_width() - life_surf.get_width(), 0))

        for i in all_tacos:
            i.move(player)

        if t % 120 == 0:
            all_tacos.add(Tacos())

        if player.collide(all_tacos):
            sound.stop()
            sound.play()
            score += 1
    else:
        go_surf = font_go.render("Game Over", True, (0, 0, 0))
        score_surf = font.render(f"Score : {score}", True, (0, 0, 0))
        screen.blit(score_surf, (screen.get_width() // 2 - score_surf.get_width() // 2, screen.get_height() // 3*2))
        screen.blit(go_surf, (screen.get_width()//2 - go_surf.get_width()//2, screen.get_height()//3))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == 13:
                    player = Player()
                    all_tacos = pygame.sprite.Group()

    clock.tick(60)
    t += 1
    pygame.display.flip()


pygame.quit()
