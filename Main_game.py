from pygame import *
import time as secs
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
        if keys_pressed[K_s] and self.rect.y < 550:
            self.rect.y += self.speed
        if keys_pressed[K_w] and self.rect.y > 10:
            self.rect.y -= self.speed

    def update_r(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_DOWN] and self.rect.y < 550:
            self.rect.y += self.speed
        if keys_pressed[K_UP] and self.rect.y > 10:
            self.rect.y -= self.speed



window = display.set_mode((700, 700))
display.set_caption('Ping-Pong')
window.fill((0, 0, 0))

platfrom_1 = Player('pongform.png', 5, 20, 40, 50, 150)
platfrom_2 = Player('pongform.png', 5, 640, 40, 50, 150)

pong_ball = GameSprite('circle.png', 10, 350, 350,70,70)


game = True
run = False

FPS = 60
clock = time.Clock()

speed_x = 3
speed_y = 3

delay = 0

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if not run:
        window.fill((0, 0, 0))
        platfrom_1.update_l()
        platfrom_2.update_r()
        if delay > 100:
            pong_ball.rect.x += speed_x
            pong_ball.rect.y += speed_y
        if pong_ball.rect.x >= 700 or pong_ball.rect.x <= 0:
            run = True
        if sprite.collide_rect(pong_ball, platfrom_1) or sprite.collide_rect(pong_ball, platfrom_2):
            speed_x *= -1
        if pong_ball.rect.y >= 665 or pong_ball.rect.y <= 35:
            speed_y *= -1

        pong_ball.reset()
        platfrom_1.reset()
        platfrom_2.reset()
        delay += 1
        clock.tick(FPS)
        display.update()