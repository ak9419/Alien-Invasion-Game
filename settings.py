class Settings():
	"""This class contains all the ingame steeings for Alien Invasion 
	game."""
	
	def __init__(self):
		
		# Screen Settings
		self.screen_width = 1200
		self.screen_height = 600
		self.bg_color = (120, 120, 120)
		
		#ship speed settings
		self.ship_speed_factor = 1.5
		
		#bullet settings
		self.bullet_speed_factor = 1
		self.bullet_width = 3
		self.bullet_height = 15
		self.bullet_color = (60, 60, 60)
		self.bullets_allowed = 3
