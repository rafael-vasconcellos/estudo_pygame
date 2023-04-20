import pygame
from pygame.locals import *
from sys import exit

class rect():
    def __init__(self, color, pos):
        self.color = color
        self.start_pos = {"x": pos[0], "y": pos[1]}
        self.x = pos[0]
        self.y = pos[1]
        self.width = 100
        self.height = 100

width = 640
height = 480
box = rect((255, 0, 0), (320, 0))




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

    pygame.draw.rect(tela, box.color, (box.x, box.y, box.width, box.height))
    box.y += 1
    
    tela.blit(text_f1.render("moving", True, (255,255,255)), (width/2-50, 10))
    
    pygame.display.update()    
    if box.y > height:
        box.y = box.start_pos['y']


