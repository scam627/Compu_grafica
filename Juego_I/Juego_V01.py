import pygame
import random
from lb_juego import*

#Dimensiones de la pantalla
ALTO=400
ANCHO=600
#lista de colores basicos
ROJO=(255,0,0)
SALMON=(240,99,99)
BLANCO=(255,255,255)
NEGRO=(0,0,0)
AZUL=(59,131,189)
VERDE=(0,255,0)

if __name__=='__main__':
    #Inicializacion de la aplicacion en pygame
    pygame.init()
    #Declaracion del tipo de fuente
    fuente=pygame.font.Font(None,36)
    #Declaracion de la pantalla y sus caracteristicas
    pantalla=pygame.display.set_mode([ANCHO,ALTO])
    pantalla.fill(BLANCO)
    #Declaracion de los grupos de sprites que usaremos
    General=pygame.sprite.Group()
    Jugadores=pygame.sprite.Group()
    Frutas=pygame.sprite.Group()
    Frutas_all=pygame.sprite.Group()
    Flechas=pygame.sprite.Group()
    Frutas_Pod=pygame.sprite.Group()
    #Objetos globales que seran usados
    jugador=Jugador()
    final=Final()
    inicial=Inicial()
    General.add(inicial)
    General.add(jugador)
    General.add(final)
    Jugadores.add(jugador)
    #Declaracion de las variables locales
    cereza_st=False
    pausa=False
    nc=0
    ncp=0
    vida=3
    salud=340
    var=4
    p=0
    np=0
    reloj=pygame.time.Clock()
    fin_juego=False
    fin=False
    #Ciclo en el que sera ejecutado el programa
    while not fin:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                fin=True
            #Deteccion de los eventos de teclado
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_RIGHT:
                    jugador.var_x=var
                if event.key==pygame.K_LEFT:
                    jugador.var_x=-var
                if event.key==pygame.K_SPACE:
                    jugador.var_x=0
                if event.key==pygame.K_UP:
                    proyectil=Flecha()
                    proyectil.rect.x=jugador.rect.x+25
                    proyectil.rect.y=jugador.rect.y
                    Flechas.add(proyectil)
                    General.add(proyectil)
                if event.key==pygame.K_p:
                    if pausa:
                        pausa=False
                    else:
                        pausa=True
        if not fin_juego and not pausa:
            #Dibujando cada objeto en pantalla
            pantalla.fill(BLANCO)
            General.update()
            General.draw(pantalla)
            #Control de las barras de salud y vida
            if salud < 20:
                salud = 340
                vida-=1
            pygame.draw.polygon(pantalla,AZUL,[[0,395],[vida*100,395],[vida*100,400],[0,400]])
            pygame.draw.polygon(pantalla,SALMON,[[10,20],[10,salud],[5,salud],[5,20]])
            points=fuente.render("Puntos= "+str(p),True,NEGRO)
            pantalla.blit(points,[10,360])
            #Actualizacion de la pantalla
            pygame.display.flip()
            #Declaracion de las listas de colision
            lf_col=pygame.sprite.spritecollide(final,Frutas,True)
            li_col=pygame.sprite.spritecollide(inicial,Flechas,True)
            lff_col=pygame.sprite.groupcollide(Flechas,Frutas,True,True)
            lffp_col=pygame.sprite.groupcollide(Flechas,Frutas_Pod,True,True)
            lj_col=pygame.sprite.spritecollide(jugador,Frutas,True)
            ljp_col=pygame.sprite.spritecollide(jugador,Frutas_Pod,True)
            #Control de los puntajes
            if nc==5:
                cereza_pod=Cereza_podrida()
                Frutas_Pod.add(cereza_pod)
                General.add(cereza_pod)
                nc=0
            if np>=10 and vida < 6 :
                vida+=1;
                np=0
            if p>=15 and p<30:
                var=5
                for element in Frutas:
                    element.var_y=3
                for element in Frutas_Pod:
                    element.var_y=3
            if p>=30:
                var=7
                for element in Frutas:
                    element.var_y=5
                for element in Frutas_Pod:
                    element.var_y=5
            #Dibujando las cerezas
            if not cereza_st:
                cereza=Cereza()
                Frutas.add(cereza)
                General.add(cereza)
                nc+=1
                cereza_st=True
            #Declarando acciones que realizara cada lista de colision
            for element in lffp_col:
                p+=2
                np+=2
                if salud+50 > 340:
                    salud=340
                else:
                    salud+=50
            for element in lff_col:
                p-=1
                np-=1
                cereza_st=False
            for element in lf_col:
                p-=1
                np-=1
                cereza_st=False
            for element in lj_col:
                p+=1
                np+=1
                if salud+50 >= 340:
                    salud=340
                else:
                    salud+=50
                cereza_st=False
            for element in ljp_col:
                vida-=1
            #Definiendo el estado bajo el cual se acaba el juego
            if vida==0:
                fin_juego=True
            salud-=0.3
            reloj.tick(60)
        else:
            #Estado de pausa
            if pausa and not fin_juego:
                texto=fuente.render("Pausa",True,NEGRO)
                pantalla.blit(texto,[330,280])
                pygame.display.flip()
            #Estado de fin de juego
            if fin_juego:
                texto=fuente.render("Fin del juego",True,BLANCO)
                pantalla.fill(NEGRO)
                pantalla.blit(texto,[330,280])
                pygame.display.flip()
