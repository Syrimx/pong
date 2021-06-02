import pygame
from pygame.locals import *
from random import *
#------------------
#Variables
BLACK = ((0,0,0))
WIDTH = 500
HEIGHT = 250
RUN = True
PlayerCounter = 0
Player2Counter = 0

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Pong')
#pygame.image.load()
#-----------------
class Player():
	x_1 = 10
	y_1 = 100
	x_2 = 480
	y_2 = 100
	width = 10
	height = 50
	speed = 0.5
	pspeed = 0.15
	x_minus = 1
	y_minus = 1
	
	def draw(self):
		pygame.draw.rect(screen, ((255,255,255)), (self.x_1, self.y_1, self.width, self.height))
		
	def draw2(self):
		pygame.draw.rect(screen, ((255,255,255)), (self.x_2, self.y_2, self.width, self.height))

p = Player()
#----------------
class Ball():
	x_minus = -1
	y_minus = -1
	color = ((255,255,255))
	x = 250
	y = 125
	width = 5
	height = 5
	speed = 0.15
	with open('ball.csv', 'a') as d:
		d.write('x  y  px  py\n')
		d.close()
	
	def draw(self):
		pygame.draw.rect(screen, (self.color), (self.x, self.y, self.width, self.height))

	def text(self):
		pass
	
	def deep(self):
		with open('ball.csv', 'a') as d:
			d.write('{0}  {1}  {2}  {3} \n'.format(self.x,self.y,p.x_2,p.y_2))
			if RUN == False:
				d.close()
			
t = Ball()
#----------------------
while RUN:
	screen.fill(BLACK)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			RUN = False
#----------------------
	#LOGIC
	#Player Movement
	keys = pygame.key.get_pressed()
	if keys[pygame.K_w]:
		p.y_1 += -p.speed
	if keys[pygame.K_s]:
		p.y_1 += p.speed
	#Player Collider
	if p.y_1 <= HEIGHT-HEIGHT:
		p.y_1 = HEIGHT-HEIGHT
	if p.y_1 >= HEIGHT-50:
		p.y_1 = HEIGHT-50
	#----------------
	#Player2 Movement
	p.y_2 += p.pspeed * p.y_minus
	
	#Player2 Collider
	if p.y_2 < 0:
		p.y_minus = 1
	if p.y_2 > 200:
		p.y_minus = -1
#--------------------
	#Ball Movement
	t.x += t.speed * t.x_minus
	t.y += t.speed * t.y_minus
	#-----------------
	#Floor Collider
	if t.y < 0:
		t.y + 10
		t.y_minus = 1
	#Roof Collider
	if t.y > 245:
		t.y - 10
		t.y_minus = -1
	#Player Collider
	if t.x < (WIDTH-WIDTH+20):
		if (p.y_1 < t.y < (p.y_1+50)):
			t.x_minus = 1
	
	#Player2 Collider
	if t.x > (WIDTH-20):
		if (p.y_2 < t.y < (p.y_2+50)):
			t.x_minus = -1

	#-----------------
	#Width Collider
	#Right
	if t.x > 495:
		t.x = 250
		t.y = 125
		t.draw()
		PlayerCounter += 1
	#Left
	if t.x < 0:
		t.y = 125
		t.x = 250
		t.draw()
		Player2Counter += 1
#--------------------
	#DRAW
	#Text

	#Ball
	t.draw()
	#P1
	p.draw()
	#P2
	p.draw2()
#--------------------
	#Deep Learning/Collecting Data
	t.deep()
#--------------------
	pygame.display.update()
pygame.quit()
