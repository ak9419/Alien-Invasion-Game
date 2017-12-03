import sys

import pygame

def check_keydown_events(event, ship):
	"""Check for game events like ,ouseclick or keyboard"""
	if event.key == pygame.K_RIGHT:
		#move the ship right
		ship.moving_right = True
				
	elif event.key == pygame.K_LEFT:
		#move the ship right
		ship.moving_left = True
				
def check_keyup_events(event, ship):
	"""Respond to key releases"""
	if event.key == pygame.K_RIGHT:
		#move the ship right
		ship.moving_right = False
			
	elif event.key == pygame.K_LEFT:
		#move the ship right
		ship.moving_left = False
		
def check_events(ship):
	"""Respond to key presses and mouse events"""
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
				sys.exit()
		
		elif event.type == pygame.KEYDOWN:
			check_keydown_events(event, ship)
			
		elif event.type == pygame.KEYUP:
			check_keyup_events(event, ship)


def update_screen(ai_settings, screen, ship):
	"""Updates images on screen and flips new screen"""
	
	#Redraw screen during each pass through loop
	screen.fill(ai_settings.bg_color)
	ship.blitme()
	
	#Make the most recently drawn screen visible
	pygame.display.flip()
