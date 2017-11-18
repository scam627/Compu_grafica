__autor__='Stiven Cardona'

from clases import *
from constantes import *
import pygame
import random 
import sys 
#render es para agregar texto

if __name__== '__main__':
    pygame.init()
    pygame.display.set_caption('Naruto ninja')
    pantalla=pygame.display.set_mode([ANCHO,ALTO])
    pantalla.fill(NEGRO)
    bl=Naruto(265)
    prado=Prado()
    barranco=Barranco()
    arbol=Arboles()
    fondo1=Fondo(512,0)
    fondo=Fondo(0,0)
    general=pygame.sprite.Group()
    mapa=pygame.sprite.Group()
    general.add(bl)
    mapa.add(barranco)
    mapa.add(prado)
    mapa.add(arbol)
    reloj=pygame.time.Clock()
    general.draw(pantalla)
    pygame.display.flip()
    fin=False
#    pygame.mixer.music.load("sound.mp3")
#    pygame.mixer.music.play(1)
    while not fin:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                sys.exit()
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_w:
                    bl.var_x=0
                    bl.dir=11
                    bl.mover=False
                    bl.combo=False
                    bl.estatico=True
                if event.key==pygame.K_d or event.key==pygame.K_RIGHT:
                    bl.var_x=8
                    bl.var_y=0
                    bl.dir=6
                    bl.mover=True
                    bl.combo=False
                    bl.estatico=False
                    bl.orien=True
                if event.key==pygame.K_a or event.key==pygame.K_LEFT:
                    bl.var_x=-8
                    bl.var_y=0
                    bl.dir=6
                    bl.mover=True
                    bl.combo=False
                    bl.estatico=False
                    bl.orien=False
                if event.key==pygame.K_s or event.key==pygame.K_DOWN:
                    bl.var_x=0
                    bl.dir=11
                    bl.mover=False
                    bl.combo=False
                    bl.estatico=True
                if event.key==pygame.K_w or event.key==pygame.K_UP:
                    bl.estatico=True
                    bl.salto=True
                    bl.dir=8
                    if not bl.mover:
                        for j in range(6):
                            for i in range(len(bl.m[bl.dir])):    
                                bl.x=i
                                bl.rect.y-=bl.gravedad
                                pantalla.blit(fondo.image,[fondo.x,fondo.y])
                                pantalla.blit(fondo1.image,[fondo1.x,fondo1.y])
                                mapa.update()
                                mapa.draw(pantalla)
                                general.update()
                                general.draw(pantalla)
                                pygame.display.flip()
                                reloj.tick(30)
                        bl.dir=9
                        for j in range(6):
                            for i in range(len(bl.m[bl.dir])):    
                                bl.x=i
                                bl.rect.y+=bl.gravedad
                                pantalla.blit(fondo.image,[fondo.x,fondo.y])
                                pantalla.blit(fondo1.image,[fondo1.x,fondo1.y])
                                mapa.update()
                                mapa.draw(pantalla)
                                general.update()
                                general.draw(pantalla)
                                pygame.display.flip()
                                reloj.tick(30)
                    else:
                        bl.mover=False
                        for j in range(6):
                            for i in range(len(bl.m[bl.dir])):    
                                bl.x=i
                                if bl.orien:
                                    bl.rect.x+=VAL_X[i]
                                    bl.rect.y-=VAL_Y[i]
                                else:
                                    bl.rect.x-=VAL_X[i]
                                    bl.rect.y-=VAL_Y[i]
                                pantalla.blit(fondo.image,[fondo.x,fondo.y])
                                pantalla.blit(fondo1.image,[fondo1.x,fondo1.y])
                                mapa.update()
                                mapa.draw(pantalla)
                                general.update()
                                general.draw(pantalla)
                                pygame.display.flip()
                                reloj.tick(30)
                        bl.dir=9
                        for j in range(6):
                            for i in range(len(bl.m[bl.dir])):    
                                bl.x=i
                                if bl.orien:
                                    bl.rect.x+=VAL_X[i]
                                    bl.rect.y+=VAL_Y[i]
                                else:
                                    bl.rect.x-=VAL_X[i]
                                    bl.rect.y+=VAL_Y[i]
                                pantalla.blit(fondo.image,[fondo.x,fondo.y])
                                pantalla.blit(fondo1.image,[fondo1.x,fondo1.y])
                                mapa.update()
                                mapa.draw(pantalla)
                                general.update()
                                general.draw(pantalla)
                                pygame.display.flip()
                                reloj.tick(30)
                if event.key==pygame.K_SPACE:
                        bl.estatico=True
                        bl.mover=False
                        bl.dir=0
                        bl.salto=False
                        bl.x=0
                        for i in range(len(bl.m[bl.dir])):
                            bl.x=i
                            pantalla.blit(fondo.image,[fondo.x,fondo.y])
                            pantalla.blit(fondo1.image,[fondo1.x,fondo1.y])
                            mapa.update()
                            mapa.draw(pantalla)
                            general.update()
                            general.draw(pantalla)
                            pygame.display.flip()
                            reloj.tick(8)
            if event.type==pygame.KEYUP:
                bl.var_x=0
                bl.dir=11
                bl.mover=False
                bl.estatico=True
                bl.combo=False
                bl.salto=False
                bl.subir=False
                bl.caer=False
            if event.type==pygame.MOUSEBUTTONDOWN:
                bl.estatico=True
                bl.mover=False
                bl.dir=0
                bl.salto=False
                bl.x=0
                print pygame.mouse.get_pressed()
                if pygame.mouse.get_pressed() == (1,0,0):
                    for i in range(len(bl.m[bl.dir])):
                        bl.x=i
                        pantalla.blit(fondo.image,[fondo.x,fondo.y])
                        pantalla.blit(fondo1.image,[fondo1.x,fondo1.y])
                        mapa.update()
                        mapa.draw(pantalla)
                        general.update()
                        general.draw(pantalla)
                        pygame.display.flip()
                        reloj.tick(8)
                if pygame.mouse.get_pressed() == (0,1,0):
                    bl.dir=2
                    bl.x=0
                    for i in range(len(bl.m[bl.dir])):
                        bl.x=i
                        pantalla.blit(fondo.image,[fondo.x,fondo.y])
                        pantalla.blit(fondo1.image,[fondo1.x,fondo1.y])
                        mapa.update()
                        mapa.draw(pantalla)
                        general.update()
                        general.draw(pantalla)
                        pygame.display.flip()
                        reloj.tick(8)
                if pygame.mouse.get_pressed() == (0,0,1):
                    bl.dir=1
                    bl.x=0
                    for i in range(len(bl.m[bl.dir])):
                        bl.x=i
                        pantalla.blit(fondo.image,[fondo.x,fondo.y])
                        pantalla.blit(fondo1.image,[fondo1.x,fondo1.y])
                        mapa.update()
                        mapa.draw(pantalla)
                        general.update()
                        general.draw(pantalla)
                        pygame.display.flip()
                        reloj.tick(8)
                bl.dir=11
        pantalla.blit(fondo.image,[fondo.x,fondo.y])
        pantalla.blit(fondo1.image,[fondo1.x,fondo1.y])
        mapa.update()
        mapa.draw(pantalla)
        general.update()
        general.draw(pantalla)
        pygame.display.flip()
        reloj.tick(10)
        #bl.rect.x-=2
