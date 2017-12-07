from pygame.locals import*
import pygame
import time

class dude:
	x=[] # List of snake segment's positions
	y=[]
	speed = 35
	direction=0 # direction determiner
	update_max_ctr=2 # A factor which determines the speed of the snake
	update_ctr =0
	
	def __init__(self,length):
		self.length = length
		self.x = [0]*self.length
		self.y = [0]*self.length
		#print(self.x)	
		
	def update(self):
	
	# Snake's head is at index 0;
	
		self.update_ctr = self.update_ctr + 1
		#print("Here in update",self.update_ctr)
		if self.update_ctr > self.update_max_ctr: # the more the max_ctr the slower the snake
 
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
	speed = 44
	
	def __init__(self,x,y):
		self.x = x * self.speed
		self.y = y * self.speed
	
	def draw(self, surface, image):
		surface.blit(image,(self.x, self.y))
class pygame_window:
	
	height = 600
	width = 800
	
	def __init__(self):
		self.running = True
		self.display = None
		self.image = None
		self.player = dude(8) #Base length
		self.apple = Apple(5,5)
		#print("Helo")
	
	def on_start(self):
		pygame.init()
		#print("Entered here")
		self.display = pygame.display.set_mode((self.width,self.height))
		pygame.display.set_caption('First Snake game')
		self.running = True
		self.image = pygame.image.load("snake.png").convert() # convert() -- Make loading things faster..
		self.apple_img = pygame.image.load("apple.png").convert()
		#print("on_start_completed")
			
	def on_loop(self): # Updates the positions
        	self.player.update()
        	pass
        
	def printer(self): # Fills the screen appropriately
		self.display.fill((0,0,0))
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
			#print("inside while loop")
			if (keys[K_RIGHT]):
				self.player.move_right()
				
			if (keys[K_LEFT]):
				self.player.move_left()
			
			if (keys[K_UP]):
				self.player.move_up()
			
			if (keys[K_DOWN]):
				#print("pressed down")
				self.player.move_down()
				
			if (keys[K_ESCAPE]): # Quit the game
				self.running = False
			
			self.on_loop()	
			self.printer() 
			time.sleep (100.0 / 1000.0); # Another factor which determines the speed of the snake.
		self.close() 

if __name__ == "__main__":
	game = pygame_window()
	game.on_execute()
			
		
		
	

