from pygame.locals import*
import pygame
import time
import random

class dude:
	x=[0] 
	y=[0]
	speed = 35
	length =3
	direction=0 # direction determiner
	update_max_ctr=0 # A factor which determines the speed of the snake
	update_ctr =0
	
	def __init__(self,length):
		self.length = length
		for i in range(0,2000): # Predefining snake's length 
			self.x.append(-100)
			self.y.append(-100)
		
		# To prevent initial collision
		self.x[1] = 1*40
		self.x[2] = 2*40
		
	def update(self):
		
		self.update_ctr = self.update_ctr + 1
		
		if self.update_ctr > self.update_max_ctr: # the more the max_ctr the slower the snake
 			
 			# Snake's head is at index 0;
            # Previous positions
			for i in range(self.length-1,0,-1):
				self.x[i] = self.x[i-1]
				self.y[i] = self.y[i-1]
 
            # Head position
			if self.direction == 0:
				self.x[0] = self.x[0] + self.speed
			if self.direction == 1:
				self.x[0] = self.x[0] - self.speed
			if self.direction == 2:
				self.y[0] = self.y[0] - self.speed
			if self.direction == 3:
				self.y[0] = self.y[0] + self.speed
 
			self.update_ctr = 0
	
	# Movement methods
	def move_right(self):	
		self.direction = 0
	def move_left(self):
		self.direction = 1
	def move_up(self):
		self.direction = 2
	def move_down(self):
		self.direction = 3
		
	def draw(self,surface,image): # Snake segments
		for i in range(0,self.length):
			surface.blit(image,(self.x[i],self.y[i]))
			
class Apple:
	
	x=0
	y=0
	speed = 35
	
	def __init__(self,x,y):
		self.x = x * self.speed
		self.y = y * self.speed
	
	def draw(self, surface, image):
		surface.blit(image,(self.x, self.y))

def collision(x1,y1,x2,y2,bsize):

	if x1>=x2 and x1<=x2+bsize:
		if y1>=y2 and y1<=y2+bsize:
			return True
	return False
	  
class pygame_window:
	
	height = 1000
	width = 1000
	
	def __init__(self):
		self.running = True
		self.display = None
		self.image = None
		self.player = dude(3) #Base length
		self.apple = Apple(5,5)
	
	
	def on_start(self):
		pygame.init()
		pygame.mixer.init()
		self.display = pygame.display.set_mode((self.width,self.height))
		pygame.display.set_caption('First Snake game')
		pygame.mixer.music.load('music.mp3')
		pygame.mixer.music.play(-1, 0.0)
		pygame.mixer.music.set_volume(0.5)
		self.running = True
		self.image = pygame.image.load("snake.png").convert() # convert() -- Make loading things faster..
		self.apple_img = pygame.image.load("apple.png").convert()
			
	def on_loop(self): # Updates the positions
        	
        	self.player.update()
        	
        	# If snake collides with the apple
        	for i in range(self.player.length):
        		if collision(self.apple.x,self.apple.y,self.player.x[i], self.player.y[i],30):
		            self.apple.x = random.randint(2,9) * 35
		            self.apple.y = random.randint(2,9) * 35
		            self.player.length = self.player.length + 1
			
		    # If snake touches itself
			for i in range(2,self.player.length):
				if collision(self.player.x[0],self.player.y[0],self.player.x[i], self.player.y[i],30):
					print("You lose! Collision: ")
					print("x[0] (" + str(self.player.x[0]) + "," + str(self.player.y[0]) + ")")
					print("x[" + str(i) + "] (" + str(self.player.x[i]) + "," + str(self.player.y[i]) + ")")
					exit(0)
		 
	    	pass
        
	def printer(self): # Fills the screen appropriately
		self.display.fill((0,0,0))
		self.display.blit(pygame.image.load("Back.png").convert(),(0,0))
		self.player.draw(self.display, self.image)
		self.apple.draw(self.display, self.apple_img)
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
			
			self.on_loop()	
			self.printer() 
			time.sleep (25.0 / 1000.0); # Another factor which determines the speed of the snake.
		
		self.close() 

if __name__ == "__main__":
	game = pygame_window()
	game.on_execute()
			
		
		
	

