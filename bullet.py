import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
	""""This class models a bullet that comes from main spaceship"""
	
	def __init__(self, ai_settings, screen, ship):
		"""Initialize attributes"""
		super(Bullet, self).__init__()
		self.screen = screen
		
		#create bullet at (0,0) and then set correct position.
		
		self.rect = pygame.Rect(0, 0, ai_settings.bullet_width, 
			ai_settings.bullet_height)
			
		self.rect.centerx = ship.rect.centerx
		self.rect.top = ship.rect.top
		
		#store bullet's position as decimal value
		
		self.y = float(self.rect.y)
		
		self.color = ai_settings.bullet_color
		self.speed_factor = ai_settings.bullet_speed_factor
		
	def update(self):
		"""Move bulle up the screen"""
		#Update decimal position of the bullet
		
		self.y -= self.speed_factor
		
		#update rect position
		
		self.rect.y = self.y
		
	def draw_bullet(self):
		"""Draw bullet to the screen"""
		pygame.draw.rect(self.screen, self.color, self.rect)
