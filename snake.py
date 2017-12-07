from pygame.locals import*
import pygame
import time

class dude:
  # Initial co-ordinates of dude
  	def __init__(self):
		self.x = 10
		self.y = 10
		self.speed = 0.5;
	# Movement methods
	def move_right(self):
		#print(self.speed)	
		self.x = self.x + self.speed
	def move_left(self):
		self.x = self.x - self.speed
	def move_up(self):
		self.y = self.y - self.speed
	def move_down(self):
		self.y = self.y + self.speed

class pygame_window:
	
	height = 600
	width = 800
	player = 0
	
	def __init__(self):
		self.running = True
		self.display = None
		self.image = None
		self.player = dude()
	
	def on_start(self):
		pygame.init()
		self.display = pygame.display.set_mode((self.width,self.height))
		pygame.display.set_caption('First Snake game')
		self.running = True
		self.image = pygame.image.load("snake.png").convert() # convert() -- Make loading things faster..
			
	def printer(self):
		self.display.fill((0,0,0)) # Color with [R,G,B] tuple ranging from [0,255];
		self.display.blit(self.image,(self.player.x,self.player.y))
		pygame.display.flip();
		
	def close(self):
		pygame.quit()
			
	def on_execute(self):
		if self.on_start() == False:
			self.running = False
		while(self.running):
			pygame.event.pump()
			keys = pygame.key.get_pressed()
			
			if (keys[K_RIGHT]):
				self.player.move_right()
				
			if (keys[K_LEFT]):
				self.player.move_left()
			
			if (keys[K_UP]):
				self.player.move_up()
			
			if (keys[K_DOWN]):
				self.player.move_down()
				
			if (keys[K_ESCAPE]): # Quit the game
				self.running = False
				
			self.printer() # Fills the screen appropriately
		self.close() 

if __name__ == "__main__":
	game = pygame_window()
	game.on_execute()
			
		
		
	

