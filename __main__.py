from os.path import dirname
import pygame, sys, time, random
from pygame.locals import *

pygame.init()
pygame.display.quit()
pygame.display.init()

FPS = 60
FramePerSec = pygame.time.Clock()

BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Screen information
info = pygame.display.Info()
SCREEN_WIDTH = info.current_w
SCREEN_HEIGHT = info.current_h

DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.FULLSCREEN)
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("Game")

def make_house():
    old_ie = 0
    for x, (ie, i) in zip('12345123451234512345123451234512345', zip('00000111112222233333444445555566666', [0, 1, 2, 3, 4, 40, 41, 42, 43, 44, 80, 81, 82, 83, 84, 120, 121, 122, 123, 124, 160, 161, 162, 163, 164])):
        i = i + 6
        y = int(ie)
        if y == 6:
            for x in range(6):
                DISPLAYSURF.blit(pygame.image.load(dirname(__file__) + '/texures/overworld/tile000', (((int(x) + 6) + 10) * 16, (8 + y) * 16)))
        DISPLAYSURF.blit(pygame.image.load(dirname(__file__) + '/texures/overworld/tile' + '0' * (3 - len(str(i))) + str(i) + '.png'), (((int(x) + 6) + 10) * 16, (8 + y) * 16))
        old_ie = ie

g1_list = []
g2_list = []
g3_list = []
g4_list = []
g4_16d_list = []

for y in range(0, SCREEN_HEIGHT, 16):
    for x in range(0, SCREEN_WIDTH, 16):
        if random.randint(0, 20) == 20:
            g1_list.append((x, y))

for y in range(0, SCREEN_HEIGHT, 16):
    for x in range(0, SCREEN_WIDTH, 16):
        if random.randint(0, 200) == 200:
            if (x, y) not in g1_list:
                g2_list.append((x, y))

for y in range(0, SCREEN_HEIGHT, 16):
    for x in range(0, SCREEN_WIDTH, 16):
        if random.randint(0, 8) == 8:
                g3_list.append((x, y))

for y in range(0, SCREEN_HEIGHT, 16):
    for x in range(0, SCREEN_WIDTH, 16):
        if random.randint(0, 70) == 70:
            g4_16d_list.append((int(x / 16), int(y / 16)))
            g4_list.append((x, y))

bg_img = pygame.image.load(dirname(__file__) + '/texures/overworld/tile000.png')
bg_img_2 = pygame.image.load(dirname(__file__) + '/texures/overworld/tile562.png')
bg_img_3 = pygame.image.load(dirname(__file__) + '/texures/overworld/tile147.png')
bg_img_4 = pygame.image.load(dirname(__file__) + '/texures/overworld/tile407.png')

tree_tl = pygame.image.load(dirname(__file__) + '/texures/overworld/tile645.png')
tree_bl = pygame.image.load(dirname(__file__) + '/texures/overworld/tile646.png')
tree_tr = pygame.image.load(dirname(__file__) + '/texures/overworld/tile685.png')
tree_br = pygame.image.load(dirname(__file__) + '/texures/overworld/tile686.png')

gui_heart = [pygame.transform.scale(pygame.image.load(dirname(__file__) + '/texures/Heart_5.png'), (32, 32)), pygame.transform.scale(pygame.image.load(dirname(__file__) + '/texures/Heart_4.png'), (32, 32)), pygame.transform.scale(pygame.image.load(dirname(__file__) + '/texures/Heart_3.png'), (32, 32)), pygame.transform.scale(pygame.image.load(dirname(__file__) + '/texures/Heart_2.png'), (32, 32)), pygame.transform.scale(pygame.image.load(dirname(__file__) + '/texures/Heart_1.png'), (32, 32))]

gui_heart.reverse()

def reload():
    for y in range(0, SCREEN_HEIGHT, 16):
        for x in range(0, SCREEN_WIDTH, 16):
            DISPLAYSURF.blit(bg_img, (x, y))

    for i in g3_list:
        DISPLAYSURF.blit(bg_img_4, i)

    for i in g1_list:
        DISPLAYSURF.blit(bg_img_2, i)

    for i in g2_list:
        DISPLAYSURF.blit(bg_img_3, i)

    for i in g4_list:
        DISPLAYSURF.blit(tree_tl, (i[0], i[1]))
        DISPLAYSURF.blit(tree_tr, (i[0], i[1] + 16))
        DISPLAYSURF.blit(tree_bl, (i[0] + 16, i[1]))
        DISPLAYSURF.blit(tree_br, (i[0] + 16, i[1] + 16))
    make_house()
    DISPLAYSURF.blit(gui_heart[P1.health], (16, 16))
    pygame.display.update()

class Player(pygame.sprite.Sprite):
    global FPS
    def __init__(self):
        super().__init__()
        self.isJump = False
        self.health = 0
        self.image = pygame.image.load(dirname(__file__) + "/texures/player_stand_forwards.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)

    def update(self):
        global FPS
        pressed_keys = pygame.key.get_pressed()
        old_location = (self.rect.x, self.rect.y)
        if self.rect.top > 0:
            if pressed_keys[K_UP]:
                self.rect.move_ip(0, -5)
                for i in range(1, 3):
                    self.image = pygame.image.load(dirname(__file__) + "/texures/player_walk_backwards_" + str(i) + '.png')

        if self.rect.top < SCREEN_HEIGHT:
            if pressed_keys[K_DOWN]:
                self.rect.move_ip(0, 5)
                for i in range(1, 3):
                    self.image = pygame.image.load(dirname(__file__) + "/texures/player_walk_forwards_" + str(i) + '.png')

        if self.rect.left > 0:
            if pressed_keys[K_LEFT]:
                self.rect.move_ip(-5, 0)
                for i in range(1, 3):
                    self.image = pygame.image.load(dirname(__file__) + "/texures/player_walk_left_" + str(i) + '.png')

        if self.rect.right < SCREEN_WIDTH:
            if pressed_keys[K_RIGHT]:
                self.rect.move_ip(5, 0)
                for i in range(1, 3):
                    self.image = pygame.image.load(dirname(__file__) + "/texures/player_walk_right_" + str(i) + '.png')

        if pressed_keys[K_SPACE]:
            for i in range(40):
                self.rect.move_ip(0, -1)
                P1.draw(DISPLAYSURF)
                make_house()
                pygame.display.update()
            for i in range(20):
                pygame.time.delay(5)
                self.rect.move_ip(0, 2)
                P1.draw(DISPLAYSURF)
                make_house()
                pygame.display.update()
            

        pygame.draw.line(DISPLAYSURF, (255, 255, 255), old_location, (self.rect.x, self.rect.y), 2)
        DISPLAYSURF.blit(gui_heart[P1.health], (16, 16))

    def draw(self, surface):
        surface.blit(self.image, self.rect)

P1 = Player()

while True:
    reload()
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    P1.update()
    P1.draw(DISPLAYSURF)
    DISPLAYSURF.blit(gui_heart[P1.health], (16, 16))
    make_house()
    pygame.display.update()
    FramePerSec.tick(FPS)