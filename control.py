import pygame
from pygame.locals import *
from sys import exit
from random import randint

class rect():
    def __init__(self, color, pos):
        self.color = color
        self.start_pos = {"x": pos[0], "y": pos[1]}
        self.x = pos[0]
        self.y = pos[1]
        self.width = 50
        self.height = 50


width = 640
height = 480
box = rect((255, 0, 0), (320, 0))
box2 = rect((255, 255, 0), (width*0.75, height*0.75))




pygame.init()
tela = pygame.display.set_mode((width, height))
pygame.display.set_caption('Título')
text_f1 = pygame.font.SysFont('arial', 40)

clock = pygame.time.Clock()


while True:
    # clock.tick()
    tela.fill( (0,0,0) )
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

    if pygame.key.get_pressed()[K_a] and box.x - 3 >= 0:
        box.x -= 3
    if pygame.key.get_pressed()[K_d] and box.x + 3 <= width - box.width:
        box.x += 3
    if pygame.key.get_pressed()[K_w] and box.y - 3 >= 0:
        box.y -= 3
    if pygame.key.get_pressed()[K_s] and box.y + 3 <= height - box.height:
        box.y += 3
    
    box.draw = pygame.draw.rect(tela, box.color, (box.x, box.y, box.width, box.height))
    box2.draw = pygame.draw.rect(tela, box2.color, (box2.x, box2.y, box2.width, box2.height))
    
    if box.draw.colliderect(box2.draw):
        box2.x = randint(0, width - box2.width)
        box2.y = randint(0, height - box2.height)
    
    tela.blit(text_f1.render("colisão", True, (255,255,255)), (width/2-50, 10))
    pygame.display.update()




"""if event.type == KEYDOWN:
            if event.key == K_a and box.x - 20 >= 0:
                box.x -= 20
            if event.key == K_d and box.x + 20 <= width:
                box.x += 20
            if event.key == K_w and box.y - 20 >= 0:
                box.y -= 20
            if event.key == K_s and box.y + 20 <= height:
                box.y += 20"""
