import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
	'''A class to represent a single alien in the fleet'''
	def __init__(self, ai_settings, screen):
		'''Initialize the Alien''' 
		super().__init__()
		self.ai_settings = ai_settings
		self.screen = screen

		#Load the alien image
		self.image = pygame.image.load('images/alien.bmp')
		self.rect = self.image.get_rect()

		#Position the alien
		self.rect.x = self.rect.width
		self.rect.y = self.rect.height

		#Get the position as float
		self.x = float(self.rect.x)
		self.y = float(self.rect.y)
	

	def blitme(self):
		'''Draw the alien'''
		self.screen.blit(self.image, self.rect)
		
