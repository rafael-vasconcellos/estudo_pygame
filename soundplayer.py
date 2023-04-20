import pygame
from pygame.locals import *
from sys import exit
from random import randint
import urllib.request
from bs4 import BeautifulSoup

class mouse_event:
    def __init__(self, parent, callback):
        self.status = False
        self.action = lambda: callback(parent)

class rect:
    def __init__(self, pos, dimensions, visibility=True, color=(255, 0, 0), callback=None):
        self.color = color
        self.pos = pos
        self.width = dimensions[0]
        self.height = dimensions[1]
        
        self.visibility = visibility
        self.clicked = mouse_event(self, callback)
    
    @property
    def visible(self):
        if callable(self.visibility):
            return self.visibility()
        else:
            return self.visibility
    
    @property
    def x(self):
        if callable(self.pos):
            return self.pos()[0]
        elif isinstance(self.pos, tuple):
            return self.pos[0]

    @property
    def y(self):
        if callable(self.pos):
            return self.pos()[1]
        elif isinstance(self.pos, tuple):
            return self.pos[1]
        
def draw(obj):
    return pygame.draw.rect(tela, obj.color, (obj.x, obj.y, obj.width, obj.height))

def click(mouse_pos):
    if pygame.mouse.get_pressed()[0]: # 0: left, 1: mid, 2: right
        return mouse_pos
    else:
        return False
    
def control(self):
    play.clicked.status = False
    play.visibility = False
    pause1.visibility = True
    
    if self.clicked.playing:
        pygame.mixer.music.unpause()
    else:
        pygame.mixer.music.play(-1)
        self.clicked.playing = True


width = 640
height = 480
container = rect( pos=(10,10), dimensions=(width-20, height-20), color=(30,144,255), visibility=True )
play = rect( 
    pos=lambda: (container.x+container.width/2-52, container.y+container.height/2-26), 
    callback=control, dimensions=(40, 50)
)

play.clicked.playing = False
pause1 = rect( 
    pos=play.pos, dimensions=(20, 50), visibility=False,
    callback= lambda parent: (
                setattr(pause1.clicked, 'status', False),
                setattr(play, 'visibility', True),
                setattr(pause1, 'visibility', False),
                pygame.mixer.music.pause()
    )
)

pause2 = rect( 
    pos=lambda: (pause1.x+pause1.width+5, pause1.y), 
    dimensions=(pause1.width, pause1.height), 
    visibility=lambda: pause1.visible
)

stop = rect( 
    pos=lambda: (play.x+play.width+15, pause2.y), dimensions=(50, 50) 
)




pygame.init()
tela = pygame.display.set_mode((width, height))
pygame.display.set_caption('Título')
text_f1 = pygame.font.SysFont('arial', 40)

clock = pygame.time.Clock()
print('Downloading song...')
html = urllib.request.urlopen("https://anonfiles.com/S4Dbs8m3zd/guignol_mp3")
soup = BeautifulSoup(html, "html.parser")
urllib.request.urlretrieve(  soup.find(id="download-url").get('href'), "guignol.mp3"  )
pygame.mixer.music.load("guignol.mp3", "mp3")
# https://anonfiles.com/S4Dbs8m3zd/guignol_mp3


while True:
    # clock.tick()
    # self.rect.collidepoint(pos), mouse_pos.draw.colliderect
    tela.fill( (0,0,0) )
    container_draw = draw(container) if container.visible else None
    stop_draw = draw(stop)

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        if event.type == KEYDOWN and event.key == K_SPACE:
            container.width = randint(100, width-20)
            container.height = randint(100, height-20)

    tela.blit(text_f1.render("Sound player", True, (255,255,255)), (container.width/2-100, container.y+10))
    mouse_pos = pygame.mouse.get_pos()




    if play.visible:
        play_draw = pygame.draw.polygon( tela, (255, 0, 0), 
            ( 
                (play.x,play.y),  (play.x+play.width,play.y+play.height/2),  (play.x,play.y+play.height) 
            ) )

        if play_draw.collidepoint(mouse_pos):
            if click(mouse_pos):
                play.clicked.status = click(mouse_pos)
            elif play.clicked.status:
                play.clicked.action()


    if pause1.visible and pause2.visible:
        pause_draw = [ draw(pause1), draw(pause2) ]
    
        if pause_draw[0].collidepoint(mouse_pos) or pause_draw[1].collidepoint(mouse_pos):
            if click(mouse_pos):
                pause1.clicked.status = click(mouse_pos)
            elif pause1.clicked.status:
                pause1.clicked.action()

    if stop_draw.collidepoint(mouse_pos):
        if click(mouse_pos):
            stop.clicked.status = click(mouse_pos)
        elif stop.clicked.status:
            play.clicked.playing = False
            stop.clicked.status = False
            pause1.clicked.action()
            pygame.mixer.music.stop()
    
    pygame.display.update()



