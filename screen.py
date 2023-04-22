import pygame
from pygame.locals import *
from sys import exit

width = 640
height = 480

pygame.init()
tela = pygame.display.set_mode((width, height))
pygame.display.set_caption('Título')
text = pygame.font.SysFont('arial', 40)
print(QUIT)


while True:
    tela.fill( (0,0,0) )
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

    pygame.draw.rect(tela, (250, 0, 0), (250, 200, 100, 100))
    pygame.draw.circle(tela, (0, 0, 255), (200, 320), 40)
    pygame.draw.line(tela, (255, 255, 0), (0, 250), (480, 250), 5)
    
    tela.blit(text.render("Texto", True, (255,255,255)), (width/2-50, 10))
    pygame.display.update()
