import pygame
from pygame.sprite import Group

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
	
	#Make group to store bullets in
	bullets = Group()
	
	#start main loop of game
	while True:
		
		gf.check_events(ai_set, screen, ship, bullets)
		ship.update()
		gf.update_bullets(bullets)		
		#print(len(bullets))
		gf.update_screen(ai_set, screen, ship, bullets)
		
	
run_game()
