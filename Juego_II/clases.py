__autor__='Stiven Cardona'

import pygame as pg
from constantes import *

class Bosque(pg.sprite.Sprite):
	def __init__(self):
		pg.sprite.Sprite.__init__(self)
		self.name='Recursos/Mapas/forest.png'
		self.sheet=pg.image.load(self.name).convert_alpha()

class Fondo(Bosque):
	def __init__(self,x,y):
		Bosque.__init__(self)
		self.image=self.sheet.subsurface((12,13,512,512))
		self.rect=self.image.get_rect()
		self.x=x
		self.y=y
	def update(self):
		self.rect.x=self.x
		self.rect.y=self.y
class Arboles(Bosque):
	def __init__(self):
		Bosque.__init__(self)
		self.image=self.sheet.subsurface((11,547,630,250))
		self.rect=self.image.get_rect()
	def update(self):
		self.rect.x=0
		self.rect.y=0
class Prado(Bosque):
	def __init__(self):
		Bosque.__init__(self)
		self.image=self.sheet.subsurface((11,930,630,90))
		self.rect=self.image.get_rect()
	def update(self):
		self.rect.x=0
		self.rect.y=209
class Barranco(Bosque):
	def __init__(self):
		Bosque.__init__(self)
		self.image=self.sheet.subsurface((11,805,630,120))
		self.rect=self.image.get_rect()
	def update(self):
		self.rect.x=0
		self.rect.y=260


class Naruto(pg.sprite.Sprite):
    def __init__(self,d):
        pg.sprite.Sprite.__init__(self)
        self.name='Recursos/Personajes/naruto.png'
       	self.init_constantes()
       	self.init_bool_variables()
       	self.init_variables(d)

    def update(self):
        if self.mover :
        	self.movimiento()
    	if self.estatico:  
    			self.quieto()
        if self.rect.x>=ANCHO-self.rect[2]:
            self.var_x=0
        if self.rect.x<=0:
            self.rect.x=0
            self.var_x=0
        if not self.orien:
    		self.image=self.m[self.dir+12][self.x]
    	else:
    		self.image=self.m[self.dir][self.x]

    def init_bool_variables(self):
    	print "Iniciando valores booleanos"
    	self.mover=False
    	self.estatico=True
    	self.combo=False
    	self.orien=True
    	self.subir=False
    	self.caer=False

    def init_variables(self,d):
    	print "Iniciando valores variables"
    	self.my=d
    	self.dir=11
    	self.x=0
    	self.vel_x=0
    	self.vel_y=0
    	self.get_mat()
    	self.image=self.m[self.dir][self.x]
        self.rect=self.image.get_rect()
        self.rect.y=self.my-self.image.get_size()[1]
        self.var_x=0

    def init_constantes(self):
    	print "Iniciando valores constantes"
    	self.gravedad=5
    	self.max_y_salto=112
    	self.sheet=pg.image.load('naruto.png').convert_alpha()

    def get_mat(self):
		ancho_img,alto_img=self.sheet.get_size()
		row_img=[]
		self.m=[]
		recorte=self.sheet.subsurface((0,0,56,48))
		row_img.append(recorte)
		recorte=self.sheet.subsurface((58,0,56,48))
		row_img.append(recorte)
		recorte=self.sheet.subsurface((116,0,56,48))
		row_img.append(recorte)
		recorte=self.sheet.subsurface((174,0,56,48))
		row_img.append(recorte)
		self.m.append(row_img)
		row_img=[]
		recorte=self.sheet.subsurface((0,50,48,48))
		row_img.append(recorte)
		recorte=self.sheet.subsurface((50,50,48,48))
		row_img.append(recorte)
		recorte=self.sheet.subsurface((100,50,48,48))
		row_img.append(recorte)
		recorte=self.sheet.subsurface((150,50,48,48))
		row_img.append(recorte)
		self.m.append(row_img)
		row_img=[]
		recorte=self.sheet.subsurface((0,100,48,48))
		row_img.append(recorte)
		recorte=self.sheet.subsurface((50,100,48,48))
		row_img.append(recorte)
		recorte=self.sheet.subsurface((100,100,48,48))
		row_img.append(recorte)
		recorte=self.sheet.subsurface((150,100,48,48))
		row_img.append(recorte)
		self.m.append(row_img)
		row_img=[]
		recorte=self.sheet.subsurface((0,150,40,56))
		row_img.append(recorte)
		recorte=self.sheet.subsurface((42,150,40,56))
		row_img.append(recorte)
		recorte=self.sheet.subsurface((84,150,40,56))
		row_img.append(recorte)
		recorte=self.sheet.subsurface((126,150,40,56))
		row_img.append(recorte)
		recorte=self.sheet.subsurface((168,150,40,56))
		row_img.append(recorte)
		self.m.append(row_img)
		row_img=[]
		recorte=self.sheet.subsurface((0,208,40,48))
		row_img.append(recorte)
		recorte=self.sheet.subsurface((42,208,40,48))
		row_img.append(recorte)
		recorte=self.sheet.subsurface((84,208,40,48))
		row_img.append(recorte)
		recorte=self.sheet.subsurface((126,208,40,48))
		row_img.append(recorte)
		recorte=self.sheet.subsurface((168,208,40,48))
		row_img.append(recorte)
		self.m.append(row_img)
		row_img=[]
		recorte=self.sheet.subsurface((0,258,48,52))
		row_img.append(recorte)
		recorte=self.sheet.subsurface((50,258,48,52))
		row_img.append(recorte)
		recorte=self.sheet.subsurface((100,258,48,52))
		row_img.append(recorte)
		recorte=self.sheet.subsurface((150,258,48,52))
		row_img.append(recorte)
		self.m.append(row_img)
		row_img=[]
		recorte=self.sheet.subsurface((0,312,48,48))
		row_img.append(recorte)
		recorte=self.sheet.subsurface((50,312,48,48))
		row_img.append(recorte)
		recorte=self.sheet.subsurface((100,312,48,48))
		row_img.append(recorte)
		recorte=self.sheet.subsurface((150,312,48,48))
		row_img.append(recorte)
		recorte=self.sheet.subsurface((200,312,48,48))
		row_img.append(recorte)
		recorte=self.sheet.subsurface((250,312,48,48))
		row_img.append(recorte)
		self.m.append(row_img)
		row_img=[]
		recorte=self.sheet.subsurface((0,362,32,40))
		row_img.append(recorte)
		self.m.append(row_img)
		row_img=[]
		recorte=self.sheet.subsurface((0,404,32,48))
		row_img.append(recorte)
		recorte=self.sheet.subsurface((34,404,32,48))
		row_img.append(recorte)    
		self.m.append(row_img)
		row_img=[]
		recorte=self.sheet.subsurface((0,454,40,48))
		row_img.append(recorte)
		recorte=self.sheet.subsurface((42,454,40,48))
		row_img.append(recorte)    
		self.m.append(row_img)
		row_img=[]
		recorte=self.sheet.subsurface((0,504,32,56))
		row_img.append(recorte)
		recorte=self.sheet.subsurface((34,504,32,56))
		row_img.append(recorte)    
		recorte=self.sheet.subsurface((68,504,32,56))
		row_img.append(recorte)
		recorte=self.sheet.subsurface((102,504,32,56))
		row_img.append(recorte)
		self.m.append(row_img)
		row_img=[]
		recorte=self.sheet.subsurface((0,562,32,48))
		row_img.append(recorte)
		recorte=self.sheet.subsurface((34,562,32,48))
		row_img.append(recorte)    
		recorte=self.sheet.subsurface((68,562,32,48))
		row_img.append(recorte)
		recorte=self.sheet.subsurface((102,562,32,48))
		row_img.append(recorte)
		recorte=self.sheet.subsurface((136,562,32,48))
		row_img.append(recorte)
		recorte=self.sheet.subsurface((170,562,32,48))
		row_img.append(recorte)
		self.m.append(row_img)
		row_img=[]
		recorte=self.sheet.subsurface((910,0,56,48))
		row_img.append(recorte)
		recorte=self.sheet.subsurface((852,0,56,48))
		row_img.append(recorte)
		recorte=self.sheet.subsurface((794,0,56,48))
		row_img.append(recorte)
		recorte=self.sheet.subsurface((736,0,56,48))
		row_img.append(recorte)
		self.m.append(row_img)
		row_img=[]
		recorte=self.sheet.subsurface((918,50,48,48))
		row_img.append(recorte)
		recorte=self.sheet.subsurface((868,50,48,48))
		row_img.append(recorte)
		recorte=self.sheet.subsurface((818,50,48,48))
		row_img.append(recorte)
		recorte=self.sheet.subsurface((768,50,48,48))
		row_img.append(recorte)
		self.m.append(row_img)
		row_img=[]
		recorte=self.sheet.subsurface((918,100,48,48))
		row_img.append(recorte)
		recorte=self.sheet.subsurface((868,100,48,48))
		row_img.append(recorte)
		recorte=self.sheet.subsurface((818,100,48,48))
		row_img.append(recorte)
		recorte=self.sheet.subsurface((768,100,48,48))
		row_img.append(recorte)
		self.m.append(row_img)
		row_img=[]
		recorte=self.sheet.subsurface((926,150,40,56))
		row_img.append(recorte)
		recorte=self.sheet.subsurface((884,150,40,56))
		row_img.append(recorte)
		recorte=self.sheet.subsurface((842,150,40,56))
		row_img.append(recorte)
		recorte=self.sheet.subsurface((800,150,40,56))
		row_img.append(recorte)
		recorte=self.sheet.subsurface((758,150,40,56))
		row_img.append(recorte)
		self.m.append(row_img)
		row_img=[]
		recorte=self.sheet.subsurface((926,208,40,48))
		row_img.append(recorte)
		recorte=self.sheet.subsurface((884,208,40,48))
		row_img.append(recorte)
		recorte=self.sheet.subsurface((842,208,40,48))
		row_img.append(recorte)
		recorte=self.sheet.subsurface((800,208,40,48))
		row_img.append(recorte)
		recorte=self.sheet.subsurface((758,208,40,48))
		row_img.append(recorte)
		self.m.append(row_img)
		row_img=[]
		recorte=self.sheet.subsurface((918,258,48,52))
		row_img.append(recorte)
		recorte=self.sheet.subsurface((868,258,48,52))
		row_img.append(recorte)
		recorte=self.sheet.subsurface((818,258,48,52))
		row_img.append(recorte)
		recorte=self.sheet.subsurface((768,258,48,52))
		row_img.append(recorte)
		self.m.append(row_img)
		row_img=[]
		recorte=self.sheet.subsurface((918,312,48,48))
		row_img.append(recorte)
		recorte=self.sheet.subsurface((868,312,48,48))
		row_img.append(recorte)
		recorte=self.sheet.subsurface((818,312,48,48))
		row_img.append(recorte)
		recorte=self.sheet.subsurface((768,312,48,48))
		row_img.append(recorte)
		recorte=self.sheet.subsurface((718,312,48,48))
		row_img.append(recorte)
		recorte=self.sheet.subsurface((668,312,48,48))
		row_img.append(recorte)
		self.m.append(row_img)
		row_img=[]
		recorte=self.sheet.subsurface((934,362,32,40))
		row_img.append(recorte)
		self.m.append(row_img)
		row_img=[]
		recorte=self.sheet.subsurface((934,404,32,48))
		row_img.append(recorte)
		recorte=self.sheet.subsurface((900,404,32,48))
		row_img.append(recorte)    
		self.m.append(row_img)
		row_img=[]
		recorte=self.sheet.subsurface((926,454,40,48))
		row_img.append(recorte)
		recorte=self.sheet.subsurface((884,454,40,48))
		row_img.append(recorte)    
		self.m.append(row_img)
		row_img=[]
		recorte=self.sheet.subsurface((934,504,32,56))
		row_img.append(recorte)
		recorte=self.sheet.subsurface((900,504,32,56))
		row_img.append(recorte)    
		recorte=self.sheet.subsurface((866,504,32,56))
		row_img.append(recorte)
		recorte=self.sheet.subsurface((832,504,32,56))
		row_img.append(recorte)
		self.m.append(row_img)
		row_img=[]
		recorte=self.sheet.subsurface((934,562,32,48))
		row_img.append(recorte)
		recorte=self.sheet.subsurface((900,562,32,48))
		row_img.append(recorte)    
		recorte=self.sheet.subsurface((866,562,32,48))
		row_img.append(recorte)
		recorte=self.sheet.subsurface((832,562,32,48))
		row_img.append(recorte)
		recorte=self.sheet.subsurface((798,562,32,48))
		row_img.append(recorte)
		recorte=self.sheet.subsurface((764,562,32,48))
		row_img.append(recorte)
		self.m.append(row_img)


    def movimiento(self):
    	self.rect.x+=self.var_x
    	self.rect.y=self.my-self.image.get_size()[1]
    	if self.x < len(self.m[self.dir])-1:
            self.x+=1
        else:
            self.x=0

    def quieto(self):
    	if self.x < len(self.m[self.dir])-1:
            self.x+=1
        else:
            self.x=0

