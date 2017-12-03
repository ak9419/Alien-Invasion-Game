import pygame

from settings import Settings
from ship import Ship
import game_functions as gf

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
	
	#make main ship
	ship = Ship(ai_set, screen)
	
	#start main loop of game
	while True:
		
		gf.check_events(ship)
		ship.update()
		gf.update_screen(ai_set, screen, ship)
	
run_game()
