import sys

import pygame

from settings import Settings

def run_game():
	"""Initialize game screen and create object and start main 
	loop of the game."""
	
	#Initialize game screen
	pygame.init()
	
	ai_set = Settings()
	screen = pygame.display.set_mode((ai_set.screen_width, ai_set.screen_height))
	
	pygame.display.set_caption("Alien Invasion!!")
	
	#Set backgroung color
	bg_color = ai_set.bg_color
	
	#start main loop of game
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
		
		screen.fill(bg_color)
			
		pygame.display.flip()
	
run_game()
