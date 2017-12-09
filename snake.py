from pygame.locals import *
from random import randint
import pygame
import time
 
class dude:
    x = [0]
    y = [0]
    step = 35
    length = 3
    direction=0 # direction determiner
    update_max_ctr=1 # A factor which determines the speed of the snakeupdate_max_ctr = 2
    update_ctr = 0
 
    def __init__(self, length):
       self.length = length
       for i in range(0,2000):  # Predefining snake's length 
           self.x.append(-100)
           self.y.append(-100)
 
       # To prevent initial collision
       self.x[0] = 1*35
       self.y[0] = 4*35
 
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
                self.x[0] = self.x[0] + self.step
            if self.direction == 1:
                self.x[0] = self.x[0] - self.step
            if self.direction == 2:
                self.y[0] = self.y[0] - self.step
            if self.direction == 3:
                self.y[0] = self.y[0] + self.step
 
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
 
    def draw(self, surface, image): # Snake segments
    	#print("called")
        for i in range(0,self.length):
            surface.blit(image,(self.x[i],self.y[i])) 
 
class Enemy:
    x = [0]
    y = [0]
    step = 35
    length = 3
    direction=0 # direction determiner
    update_max_ctr=1 # A factor which determines the speed of the snakeupdate_max_ctr = 2
    update_ctr = 0
 
    def __init__(self, length):
       self.length = length
       for i in range(0,2000):  # Predefining snake's length 
           self.x.append(-100)
           self.y.append(-100)
 
       # To prevent initial collision
       self.x[0] = 1*35
       self.y[0] = 2*35
 
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
                self.x[0] = self.x[0] + self.step
            if self.direction == 1:
                self.x[0] = self.x[0] - self.step
            if self.direction == 2:
                self.y[0] = self.y[0] - self.step
            if self.direction == 3:
                self.y[0] = self.y[0] + self.step
 
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
 
    def draw(self, surface, image): # Snake segments
    	#print("called")
        for i in range(0,self.length):
            surface.blit(image,(self.x[i],self.y[i])) 
 
    def target(self,dx,dy):
        if self.x[0] > dx:
            self.move_left()
 
        if self.x[0] < dx:
            self.move_right()
 
        if self.x[0] == dx:
            if self.y[0] < dy:
                self.move_down()
 
            if self.y[0] > dy:
                self.move_up()
 
 
class Apple:
    x = 0
    y = 0
    step = 35
 
    def __init__(self,x,y):
        self.x = x * self.step
        self.y = y * self.step
 
    def draw(self, surface, image):
        surface.blit(image,(self.x, self.y)) 
        
        
def collision(x1,y1,x2,y2,bsize):
    if x1 >= x2 and x1 <= x2 + bsize:
        if y1 >= y2 and y1 <= y2 + bsize:
            return True
    return False
 
class pygame_window:
 
    windowWidth = 1000
    windowHeight = 1000
    player = 0
    apple = 0
 
    def __init__(self):
        self.running = True
        self.display = None
        self.image = None
        self.apple_img = None
        self.enemy_img = None
        self.player = dude(3) #Base length 
        self.apple = Apple(8,5)
        self.enemy = Enemy(5) #enemy 
        
        print "You're the one operating RED snake and BLACK one is CPU"
        print "YOU ---- RED"
        print "CPU ---- BLACK" + '\n'
        time.sleep (2)
        
        #statistics of the game
        
        self.total = 1
        self.score = 0
 
    def start(self):
        pygame.init()
        self.display = pygame.display.set_mode((self.windowWidth,self.windowHeight), pygame.HWSURFACE)
 
        pygame.display.set_caption('First snake game')
        self.running = True
        self.image = pygame.image.load("snake.png").convert() # convert() -- Make loading things faster..
        self.apple_img = pygame.image.load("apple.png").convert()
        self.enemy_img = pygame.image.load("Enemy.png").convert()
        pygame.mixer.init()
        pygame.mixer.music.load('music.mp3')
        pygame.mixer.music.play(-1, 0.0)
        pygame.mixer.music.set_volume(0.5)
 
    # Updates the positions
    def on_loop(self):
        self.enemy.target(self.apple.x, self.apple.y)
        self.player.update()
        self.enemy.update()
 
        # If snake collides with apple
        for i in range(0,self.player.length):
			flag = 0	
			if collision(self.apple.x,self.apple.y,self.player.x[i], self.player.y[i],25):
				flag = flag + 1
				self.apple.x = randint(2,9) * 70
				self.apple.y = randint(2,9) * 70
				self.player.length = self.player.length + 1
				if flag == 1:
					self.score = self.score + 1
					self.total = self.total + 1

        # If enemy collides with the apple
        for i in range(0,self.enemy.length):
        	flag = 0
        	if collision(self.apple.x,self.apple.y,self.enemy.x[i], self.enemy.y[i],25):
				flag = flag + 1
				self.apple.x = randint(2,9) * 70
				self.apple.y = randint(2,9) * 70
				if flag == 1:
					self.total = self.total + 1
                
 
        # If snake collides itself
        for i in range(2,self.player.length):
            if collision(self.player.x[0],self.player.y[0],self.player.x[i], self.player.y[i],25):
                print "You lose! Collision: "
                print "Head collided with Segment no." + str(i) + '\n'
                #print "x[" + str(i) + "] (" + str(self.player.x[i]) + "," + str(self.player.y[i]) + ")"  
                print "Your ate " + str(self.score) + " out of " + str(self.total) + " apples";
                print "Your agility:" + str(round(self.score/float(self.total),2)) + '\n'
                exit(0)
 
        pass
 
    def printer(self):  # Fills the screen appropriately
        self.display.fill((0,0,0))
        self.display.blit(pygame.image.load("Back.png").convert(),(0,0))
        font = pygame.font.Font(None, 24)
        survivedtext = font.render("Total Apples : " + str(self.total)+ ", Your score : " + str(self.score)+" and Agility: " + str(round(self.score/float(self.total),2)),True,(255,0,0))
        textRect = survivedtext.get_rect()
        textRect.topright=[950,5]
        self.display.blit(survivedtext, textRect)
        
        self.player.draw(self.display, self.image)
        self.apple.draw(self.display, self.apple_img)
        self.enemy.draw(self.display, self.enemy_img)
        pygame.display.flip()
 
    def close(self):  # Quit the game
    	print "Your ate " + str(self.score) + " out of " + str(self.total) + " apples";
        print "Your agility:" + str(round(self.score/float(self.total),2)) + '\n'
        pygame.quit()
 
    def on_execute(self):
        if self.start() == False:
            self.running = False
 
        while( self.running ):
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
 
            if (keys[K_ESCAPE]):  # Quit the game
                self.running = False
 
            self.on_loop()
            self.printer()
 
            time.sleep (10.0 / 1000.0); # Another factor which determines the speed of the snake.
        self.close()

if __name__ == "__main__" :
    game = pygame_window()
    game.on_execute()
