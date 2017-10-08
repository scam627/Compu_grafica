import pygame
import random


#lista de colores basicos
ALTO=400
ANCHO=600
ROJO=(255,0,0)
BLANCO=(255,255,255)
NEGRO=(0,0,0)
AZUL=(59,131,189)
VERDE=(0,255,0)

class Flecha(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.image.load('Imagenes/flecha.png')
        self.rect=self.image.get_rect()
        self.var_y=-2
    def update(self):
        self.rect.y+=self.var_y
class Inicial(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.Surface([600,1])
        self.rect=self.image.get_rect()
        self.rect.x=0
        self.rect.y=0
class Final(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.image.load('Imagenes/final.png')
        self.rect=self.image.get_rect()
        self.rect.x=0
        self.rect.y=350

class Cereza_podrida(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.image.load('Imagenes/fruta_pod.png')
        self.rect=self.image.get_rect()
        self.rect.y=-random.randrange(0,300)
        self.rect.x=random.randrange(0,ANCHO-self.rect[2])
        self.var_y=2
    def update(self):
        self.rect.y+=self.var_y
        if self.rect.y>=ALTO-self.rect[3]:
            self.rect.y=-random.randrange(0,300)
            self.rect.x=random.randrange(0,ANCHO-self.rect[2])
        if self.rect.y<=0:
            self.var_y=2

class Cereza(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.image.load('Imagenes/fruta.png')
        self.time=10
        self.rect=self.image.get_rect()
        self.rect.y=-random.randrange(0,300)
        self.rect.x=random.randrange(0,ANCHO-self.rect[2])
        self.var_y=2
    def update(self):
        self.rect.y+=self.var_y
        if self.time > 0 and self.time <= 10:
            self.image=pygame.image.load('Imagenes/fruta.png')
            self.time-=1
        if self.time <= 20 and self.time > 10:
            self.image=pygame.image.load('Imagenes/fruta_o.png')
            self.time-=1
        if self.time == 0:
            self.time=20
        if self.rect.y>=ALTO-self.rect[3]:
            self.rect.y=-random.randrange(0,300)
            self.rect.x=random.randrange(0,ANCHO-self.rect[2])
        if self.rect.y<=0:
            self.var_y=2

class Jugador(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.image.load('Imagenes/jugador.png')
        self.time=20
        self.rect=self.image.get_rect()
        self.rect.x=0
        self.rect.y=300
        self.var_x=4
    def update(self):
        if self.time > 0 and self.time <= 10:
            self.image=pygame.image.load('Imagenes/jugador.png')
            self.time-=1
        if self.time <= 20 and self.time > 10:
            self.image=pygame.image.load('Imagenes/jugador_o.png')
            self.time-=1
        if self.time == 0:
            self.time=20
        self.rect.x+=self.var_x
        if self.rect.x>=ANCHO-20:
            self.var_x=-self.var_x
        if self.rect.x<=0-20:
            self.var_x=-self.var_x