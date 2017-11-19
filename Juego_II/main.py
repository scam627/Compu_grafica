__autor__='Stiven Cardona'

from clases import *
from constantes import *
from recursos import *
import pygame
import random 
import sys 

def actualizar(pantalla,lls):
    for i in lls:
        i.update()
        i.draw(pantalla)
    pygame.display.flip()

def dibujar(pantalla,lo):
    t=0
    for i in lo:
        pantalla.blit(i.image,[CX[t],CY[t]])
        t+=1

def final_game(pantalla):
    muerto=pygame.image.load('Recursos/Objetos/gameover.jpg')
    pantalla.blit(muerto,[150,80])
    pygame.display.flip()

def inicio(enemy,jugador):
    jugador.dir=11
    enemy.dir=2
    enemy.rect.y=40
    enemy.rect.x=random.randrange(0,ANCHO-enemy.m[enemy.dir][enemy.x].get_size()[0])
    enemys.add(enemy)
    general.add(enemy)
    for i in range(9):
        enemy.rect.y+=20
        dibujar(pantalla,lo)
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
    lv=[]
    one=Vidas(20,270)
    two=Vidas(80,270)
    three=Vidas(140,270)
    lv.append(one)
    lv.append(two)
    lv.append(three)
    en=Enemys(260)
    bl=Naruto(265)
    bl.rect.x=300
    lo=[]
    prado=Prado()
    barranco=Barranco()
    arbol=Arboles()
    fondo=Fondo(0,0)
    fondoo=Fondo(512,0)
    lo.append(fondo)
    lo.append(fondoo)
    lo.append(arbol)
    lo.append(barranco)
    lo.append(prado)
    jugadores=pygame.sprite.Group()
    enemys=pygame.sprite.Group()
    lls=[]
    general=pygame.sprite.Group()
    lls.append(general)
    general.add(one)
    general.add(two)
    general.add(three)
    general.add(bl)
    jugadores.add(bl)
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
                                dibujar(pantalla,lo)
                                actualizar(pantalla,lls)
                                pygame.display.flip()
                                reloj.tick(TIME)
                        bl.dir=9
                        for j in range(6):
                            for i in range(len(bl.m[bl.dir])):    
                                bl.x=i
                                bl.rect.y+=bl.gravedad
                                dibujar(pantalla,lo)
                                actualizar(pantalla,lls)
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
                                dibujar(pantalla,lo)
                                actualizar(pantalla,lls)
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
                                dibujar(pantalla,lo)
                                actualizar(pantalla,lls)
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
                        dibujar(pantalla,lo)
                        actualizar(pantalla,lls)
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
                        dibujar(pantalla,lo)
                        actualizar(pantalla,lls)
                        pygame.display.flip()
                        reloj.tick(TIME)
                if pygame.mouse.get_pressed() == (0,1,0):
                    bl.dir=2
                    bl.x=0
                    for i in range(len(bl.m[bl.dir])):
                        bl.x=i
                        dibujar(pantalla,lo)
                        actualizar(pantalla,lls)
                        pygame.display.flip()
                        reloj.tick(TIME)
                if pygame.mouse.get_pressed() == (0,0,1):
                    bl.dir=1
                    bl.x=0
                    for i in range(len(bl.m[bl.dir])):
                        bl.x=i
                        dibujar(pantalla,lo)
                        actualizar(pantalla,lls)
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
                bl.salud-=2
            else:
                bl.dir=actual
        if bl.salud <= 0:
            if len(lv) > 0:
                lv[(len(lv)-1)].existo=False
                lv.pop()
                bl.salud=100
        if en.salud <= 0 and existe:
            en.dir=4
            en.x=0
            en.mover=False
            en.golpeo=False
            en.combo=False
            dibujar(pantalla,lo)
            actualizar(pantalla,lls)
            reloj.tick(TIME)
            en.dir=5
            for i in range(len(en.m[en.dir])):
                en.x=i
                en.rect.x-=4
                en.rect.y+=4
                dibujar(pantalla,lo)
                actualizar(pantalla,lls)
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
        if not GAMEOVER:
            if len(lv)==0:
                dibujar(pantalla,lo)
                actualizar(pantalla,lls)
                GAMEOVER=True
                print "gameover"
                reloj.tick(TIME)
            else:
                dibujar(pantalla,lo)
                actualizar(pantalla,lls)
        else:
            final_game(pantalla)
            print "Game Over"
        bl.dir=actual
        reloj.tick(TIME)
        #bl.rect.x-=2
