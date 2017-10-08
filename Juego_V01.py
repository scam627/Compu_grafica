import pygame
import random
from lb_juego import*


#lista de colores basicos
ALTO=400
ANCHO=600
ROJO=(255,0,0)
BLANCO=(255,255,255)
NEGRO=(0,0,0)
AZUL=(59,131,189)
VERDE=(0,255,0)

if __name__=='__main__':
    pygame.init()
    fuente=pygame.font.Font(None,36)
    pantalla=pygame.display.set_mode([ANCHO,ALTO])
    pantalla.fill(BLANCO)
    General=pygame.sprite.Group()
    Jugadores=pygame.sprite.Group()
    Frutas=pygame.sprite.Group()
    Frutas_all=pygame.sprite.Group()
    Flechas=pygame.sprite.Group()
    Frutas_Pod=pygame.sprite.Group()
    jugador=Jugador()
    final=Final()
    inicial=Inicial()
    General.add(jugador)
    General.add(final)
    Jugadores.add(jugador)
    cereza_st=False
    nc=0
    ncp=0
    v=5
    p=0
    reloj=pygame.time.Clock()
    fin_juego=False
    fin=False
    while not fin:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                fin=True
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_RIGHT:
                    jugador.var_x=4
                if event.key==pygame.K_LEFT:
                    jugador.var_x=-4
                if event.key==pygame.K_SPACE:
                    jugador.var_x=0
                if event.key==pygame.K_UP:
                    proyectil=Flecha()
                    proyectil.rect.x=jugador.rect.x+25
                    proyectil.rect.y=jugador.rect.y
                    Flechas.add(proyectil)
                    General.add(proyectil)
        if not fin_juego:
            pantalla.fill(BLANCO)
            General.update()
            General.draw(pantalla)
            pygame.draw.polygon(pantalla,AZUL,[[0,395],[v*100,395],[v*100,400],[0,400]])
            texto=fuente.render("Puntos= "+str(p),True,NEGRO)
            pantalla.blit(texto,[10,20])
            pygame.display.flip()
            lf_col=pygame.sprite.spritecollide(final,Frutas,True)
            li_col=pygame.sprite.spritecollide(inicial,Flechas,True)
            lff_col=pygame.sprite.groupcollide(Flechas,Frutas,True,True)
            lffp_col=pygame.sprite.groupcollide(Flechas,Frutas_Pod,True,True)
            lj_col=pygame.sprite.spritecollide(jugador,Frutas,True)
            if nc==5:
                cereza_pod=Cereza_podrida()
                Frutas_Pod.add(cereza_pod)
                General.add(cereza_pod)
                nc=0
            if not cereza_st:
                cereza=Cereza()
                Frutas.add(cereza)
                General.add(cereza)
                nc+=1
                cereza_st=True
            for element in lffp_col:
                p+=2
            for element in lff_col:
                p-=1
                cereza_st=False
            for element in lf_col:
                v-=1
                cereza_st=False
            for element in lj_col:
                p+=1
                cereza_st=False
            if v==0:
                fin_juego=True
            reloj.tick(60)
        else:
            texto=fuente.render("Fin del juego",True,BLANCO)
            pantalla.fill(NEGRO)
            pantalla.blit(texto,[330,280])
            pygame.display.flip()