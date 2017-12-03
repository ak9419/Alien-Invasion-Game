import sys

import pygame

def check_events(ship):
	"""Check for game events like ,ouseclick or keyboard"""
	
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
				sys.exit()
				
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_RIGHT:
				#move the ship right
				ship.moving_right = True
				
			elif event.key == pygame.K_LEFT:
				#move the ship right
				ship.moving_left = True
				
		elif event.type == pygame.KEYUP:
			if event.key == pygame.K_RIGHT:
				#move the ship right
				ship.moving_right = False
			
			elif event.key == pygame.K_LEFT:
				#move the ship right
				ship.moving_left = False

def update_screen(ai_settings, screen, ship):
	"""Updates images on screen and flips new screen"""
	
	#Redraw screen during each pass through loop
	screen.fill(ai_settings.bg_color)
	ship.blitme()
	
	#Make the most recently drawn screen visible
	pygame.display.flip()
