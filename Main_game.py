from pygame import *
import random


class GameSprite(sprite.Sprite):
    def __init__(self, p_image, speed, player_x, player_y, size_x, size_y):
        super().__init__()
        self.image = transform.scale(image.load(p_image), (size_x, size_y))
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


class Player(GameSprite):
    def update_l(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w] and self.rect.x < 630:
            self.rect.x += self.speed
        if keys_pressed[K_s] and self.rect.x > 5:
            self.rect.x -= self.speed

    def update_r(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_UP] and self.rect.x < 630:
            self.rect.x += self.speed
        if keys_pressed[K_DOWN] and self.rect.x > 5:
            self.rect.x -= self.speed


window = display.set_mode((700, 700))
display.set_caption('Space Wars')
window.fill((42, 174, 40))

game = True
run = False

FPS = 60
clock = time.Clock()

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    clock.tick(FPS)
    display.update()