__autor__='Stiven Cardona'

from clases import *
from constantes import *
from recursos import *
import pygame
import random 
import sys 
#render es para agregar texto

def inicio(enemy,jugador):
    jugador.dir=11
    enemy.dir=2
    enemy.rect.y=40
    enemy.rect.x=random.randrange(0,ANCHO-enemy.m[enemy.dir][enemy.x].get_size()[0])
    enemys.add(enemy)
    general.add(enemy)
    for i in range(9):
        enemy.rect.y+=20
        pantalla.blit(fondo.image,[fondo.x,fondo.y])
        pantalla.blit(fondo1.image,[fondo1.x,fondo1.y])
        mapa.update()
        mapa.draw(pantalla)
        general.update()
        general.draw(pantalla)
        pygame.display.flip()
        reloj.tick(TIME)
    enemy.dir=0

def persecution(enemy,jugador):
    if enemy.x < len(enemy.m[1]) and enemy.x < len(enemy.m[7]):
        if not enemy.golpeo:
            enemy.dir=1
            if jugador.rect.x>enemy.rect.x+enemy.m[enemy.dir][enemy.x].get_size()[0]:
                enemy.var_x=5
                enemy.dir=1
                enemy.golpeo=False
                enemy.mover=True
                enemy.combo=False
                enemy.orien=True
            if jugador.rect.x+jugador.m[jugador.dir][jugador.x].get_size()[0]<enemy.rect.x:
                enemy.var_x=-5
                enemy.dir=1
                enemy.mover=True
                enemy.golpeo=False
                enemy.combo=False
                enemy.orien=False
            if jugador.rect.x<enemy.rect.x+enemy.m[enemy.dir][enemy.x].get_size()[0] and jugador.rect.x+jugador.m[jugador.dir][jugador.x].get_size()[0]>enemy.rect.x:
                enemy.var_x=0
                enemy.dir=7
                enemy.golpeo=False
                enemy.mover=False
                enemy.combo=True
        else:
            enemy.var_x=0
            enemy.dir=3
            enemy.golpeo=True
            enemy.mover=False
            enemy.combo=False
if __name__== '__main__':
    pygame.init()
    pygame.display.set_caption('Naruto ninja')
    pantalla=pygame.display.set_mode([ANCHO,ALTO])
    pantalla.fill(NEGRO)
    #en1=Enemys(260)
    en=Enemys(260)
    bl=Naruto(265)
    bl.rect.x=300
    prado=Prado()
    barranco=Barranco()
    arbol=Arboles()
    fondo1=Fondo(512,0)
    fondo=Fondo(0,0)
    jugadores=pygame.sprite.Group()
    enemys=pygame.sprite.Group()
    general=pygame.sprite.Group()
    mapa=pygame.sprite.Group()
    #general.add(en1
    general.add(bl)
    jugadores.add(bl)
    mapa.add(barranco)
    mapa.add(prado)
    mapa.add(arbol)
    #en1.rect.x=599
    existe=True
    reloj=pygame.time.Clock()
    general.draw(pantalla)
    pygame.display.flip()
    fin=False
    inicio(en,bl)
    number_enemys=5
    bl.dir=11
    en.dir=0
    actual=11
#    pygame.mixer.music.load("sound.mp3")
#    pygame.mixer.music.play(1)
    while not fin:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                sys.exit()
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_d or event.key==pygame.K_RIGHT:
                    bl.var_x=8
                    bl.var_y=0
                    bl.dir=6
                    bl.mover=True
                    bl.combo=False
                    bl.estatico=False
                    bl.orien=True
                    actual=bl.dir
                if event.key==pygame.K_a or event.key==pygame.K_LEFT:
                    bl.var_x=-8
                    bl.var_y=0
                    bl.dir=6
                    bl.mover=True
                    bl.combo=False
                    bl.estatico=False
                    bl.orien=False
                    actual=bl.dir
                if event.key==pygame.K_s or event.key==pygame.K_DOWN:
                    bl.var_x=0
                    bl.dir=11
                    bl.mover=False
                    bl.combo=False
                    bl.estatico=True
                    actual=bl.dir
                if event.key==pygame.K_SPACE:
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
                                reloj.tick(TIME)
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
                                reloj.tick(TIME)
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
                                reloj.tick(TIME)
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
                                reloj.tick(TIME)
                    actual=bl.dir
                if event.key==pygame.K_w:
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
                        reloj.tick(TIME)
                    actual=bl.dir
            if event.type==pygame.KEYUP:
                bl.var_x=0
                bl.dir=11
                bl.mover=False
                bl.estatico=True
                bl.combo=False
                bl.salto=False
                bl.subir=False
                bl.caer=False
                actual=bl.dir
            if event.type==pygame.MOUSEBUTTONDOWN:
                bl.estatico=False
                bl.mover=False
                bl.dir=0
                bl.salto=False
                bl.x=0
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
                        reloj.tick(TIME)
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
                        reloj.tick(TIME)
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
                        reloj.tick(TIME)
                actual=bl.dir
            if event.type==pygame.MOUSEBUTTONUP:
                bl.var_x=0
                bl.dir=11
                bl.mover=False
                bl.estatico=True
                bl.combo=False
                bl.salto=False
                bl.subir=False
                bl.caer=False
                actual=bl.dir
        persecution(en,bl)
        #persecution(en1,bl)
        col_je=pygame.sprite.spritecollide(bl,enemys,False)
        col_ej=pygame.sprite.spritecollide(en,jugadores,False)
        for element in col_je:
            if bl.dir==0 or bl.dir==1 or bl.dir==2:
                en.golpeo=True
                en.salud-=10
            else:
                en.golpeo=False
        for element in col_ej:
            if en.dir==7 and (bl.dir != 0 and bl.dir != 1 and bl.dir != 2) and number_enemys>0:
                bl.dir=12
            else:
                bl.dir=actual
        if en.salud <= 0 and existe:
            en.dir=4
            en.x=0
            en.mover=False
            en.golpeo=False
            en.combo=False
            pantalla.blit(fondo.image,[fondo.x,fondo.y])
            pantalla.blit(fondo1.image,[fondo1.x,fondo1.y])
            mapa.update()
            mapa.draw(pantalla)
            general.update()
            general.draw(pantalla)
            pygame.display.flip()
            reloj.tick(TIME)
            en.dir=5
            for i in range(len(en.m[en.dir])):
                en.x=i
                en.rect.x-=4
                en.rect.y+=4
                pantalla.blit(fondo.image,[fondo.x,fondo.y])
                pantalla.blit(fondo1.image,[fondo1.x,fondo1.y])
                mapa.update()
                mapa.draw(pantalla)
                general.update()
                general.draw(pantalla)
                pygame.display.flip()
                reloj.tick(5)
                existe=False
            general.remove(en)
            if number_enemys>0:
                en=Enemys(260)
                general.add(en)
                existe=True
                inicio(en,bl)
                number_enemys-=1
            else:
                existe=False
        pantalla.blit(fondo.image,[fondo.x,fondo.y])
        pantalla.blit(fondo1.image,[fondo1.x,fondo1.y])
        mapa.update()
        mapa.draw(pantalla)
        general.update()
        general.draw(pantalla)
        pygame.display.flip()
        bl.dir=actual
        reloj.tick(TIME)
        #bl.rect.x-=2
