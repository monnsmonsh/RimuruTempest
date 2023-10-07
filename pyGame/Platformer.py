#phyton 3.12
import pygame
from pygame.locals import *

pygame.init()

screen_width = 1920	
screen_heigth = 1080	

screen =pygame.display.set_mode((screen_width, screen_heigth))
pygame.display.set_caption('Platformer')

#def variable de juego
tile_size =200

#cargamos img
sun_img = pygame.image.load('img/sun.png')
bg_img = pygame.image.load('img/sky.png')



def draw_grid():
	for line in range(0, 6):
		pygame.draw.line(screen, (255, 255, 255), (0, line * tile_size), (screen_width, line * tile_size))
		pygame.draw.line(screen, (255, 255, 255), (line * tile_size, 0), (line * tile_size, screen_height))

class World():
	def __init__(self,data):
		#cargamos img
		dirt_img = pygame.image.load('img/dirt.png')
		#grass_img = pygame.image.load('img/grass.png')

		for row in data:
			for tile in row:
				if tile == 1:
					img = pygame.transform.scale(dirt_img,)


#world
world_data=[
[1, 1, 1, 1, 1],
[1, 0, 0, 0, 1],
[1, 0, 0, 0, 1],
[1, 0, 0, 0, 1],
[1, 1, 1, 1, 1],
]

run = True
while run:
	
	screen.blit(bg_img, (0, 0))
	screen.blit(sun_img,(100,100))

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False

	pygame.display.update()

pygame.quit()