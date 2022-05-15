from pygame import *
from random import randint
from time import time as timer


bg = display.set_mode([800,600])
display.set_caption('Ping Pong')

white = [255, 255, 255]
red = [255, 0, 0]
blue = [0,187,255]
pink = [210,0,210]
yellow = [255,210,0]

bg.fill(white)
display.update()

backcolor = white

background = input("What color would you like?:")
if background == 'red' or background == 'красный':
    backcolor = [255, 0, 0]
elif background == 'blue' or background == 'голубой':
    backcolor = blue
elif background == 'pink' or background == 'розовый':
    backcolor = pink
elif background == 'yellow' or background == 'жёлтый':
    backcolor = yellow

class sprites(sprite.Sprite):
    def __init__( self, pimage,  px, py, ix,iy, pspeed):
        super().__init__()
        self.image = transform.scale(image.load(pimage), (ix,iy))
        self.speed = pspeed
        self.rect = self.image.get_rect()
        self.rect.x = px
        self.rect.y = py
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(sprites):        
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_a] and self.rect.x > 10:
            self.rect.x -= self.speed
        if keys_pressed[K_LEFT] and self.rect.x > 10:
            self.rect.x -= self.speed
        if keys_pressed[K_d] and self.rect.x < 890:
            self.rect.x += self.speed
        if keys_pressed[K_RIGHT] and self.rect.x < 890:
            self.rect.x += self.speed


clock = time.Clock()
FPS = 144


running = True
while running:
    for i in event.get():
        if i.type == QUIT:
            running = False
            quit()
    bg.fill(backcolor)
    display.flip()
    display.update()
    clock.tick(FPS)