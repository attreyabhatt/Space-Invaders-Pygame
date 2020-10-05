import math
import random

import pygame
from pygame import mixer
import time
bullet_state = "ready"

def start(screen,background,Message = None):
 over_font = pygame.font.Font('freesansbold.ttf', 64)

 score = "0"
 if(Message):
 	score = Message
 score1 = over_font.render("Last Score : " + str(score), True, (255, 255, 255))
		   
 s = True
 '''pygame.init()

# create the screen
 screen = pygame.display.set_mode((800, 600))


# Background
 background = pygame.image.load('background.png')
 pygame.display.set_caption("Space Invader")'''
 print("start")
 startbutton = pygame.image.load('play-button.png')
 while(s):
  screen.fill((0, 0, 0))
    # Background Image
  screen.blit(background, (0, 0))
  screen.blit(startbutton, (400, 300))
  score = "0"
  if(Message):
   score = Message
   score1 = over_font.render("Last Score : " + str(score), True, (255, 255, 255))

   screen.blit(score1, (0, 0))

  mouse = pygame.mouse.get_pos() 

  pygame.display.update()
  for event in pygame.event.get():
         if event.type == pygame.QUIT:
          print("quit the game")
          s = False
         if event.type == pygame.MOUSEBUTTONDOWN: 

              
            #if the mouse is clicked on the 
            # button the game is terminated 
            if 400 <= mouse[0] <= 432 and 300 <= mouse[1] <= 332: 
             
             
             rungame(screen,background) 


# Intialize the pygame
def rungame(screen,background):
		global bullet_state
		

		# create the screen
		


		# Background
		

		# Sound
		#mixer.music.load("background.wav")
		#mixer.music.play(-1)

		# Caption and Icon
		
		#icon = pygame.image.load('ufo.png')
		#pygame.display.set_icon(icon)

		# Player
		print("start game ")
		playerImg = pygame.image.load('player.png')
		playerX = 370
		playerY = 480
		playerX_change = 0
		angle = 180

		# Enemy
		enemyImg = []
		enemyX = []
		enemyY = []
		enemyX_change = []
		enemyY_change = []
		num_of_enemies = 4

		for i in range(num_of_enemies):
		    enemyImg.append(pygame.image.load('enemy.png'))
		    enemyX.append(random.randint(0, 736))
		    enemyY.append(random.randint(50, 150))
		    enemyX_change.append(4)
		    enemyY_change.append(40)

		#Rocket enemy
		rocketenemyImg = []
		rocketenemyX = []
		rocketenemyY = []
		rocketenemyX_change = []
		rocketenemyY_change = []
		num_of_rocketenemies = 3

		for j in range(num_of_enemies):
		    rocketenemyImg.append(pygame.image.load('enemy_spaceship.png'))
		    rocketenemyX.append(random.randint(0, 736))
		    rocketenemyY.append(random.randint(50, 150))
		    rocketenemyX_change.append(4)
		    rocketenemyY_change.append(40)
		for i in range(num_of_rocketenemies):
		    angle = 180
		    rocketenemyImg[i] = pygame.transform.rotate(rocketenemyImg[i], angle)

		#rocketbullet
		#ready
		#fire
		enemybulletImg = pygame.image.load('enemy_bullet.png')
		enemy_bulletX = 0
		enemy_bulletY = 480
		enemy_bulletX_change = 0
		enemy_bulletY_change = 10
		enemy_bullet_state = "ready"





		# Bullet

		# Ready - You can't see the bullet on the screen
		# Fire - The bullet is currently moving

		bulletImg = pygame.image.load('bullet.png')
		bulletX = 0
		bulletY = 480
		bulletX_change = 0
		bulletY_change = 10
		


		#enemy bulllet
		#enemy_ready = you can't see the bullet
		#enemy_fire = you can see now
		enemy_bulletImg = pygame.image.load('bullet.png')
		angle = 180
		enemy_bulletImg = pygame.transform.rotate(enemy_bulletImg, angle)
		enemy_bulletX = 0
		enemy_bulletY = 800
		enemy_bulletX_change = 0
		enemy_bulletY_change =12
		enemy_bullet_state = "ready"
		# Score

		score_value = 0
		font = pygame.font.Font('freesansbold.ttf', 32)

		textX = 10
		testY = 10

		# Game Over
		over_font = pygame.font.Font('freesansbold.ttf', 64)

		# 
		def show_score(x, y):
		    score = font.render("Score : " + str(score_value), True, (255, 255, 255))
		    screen.blit(score, (x, y))


		def game_over_text():
		    over_text = over_font.render("GAME OVER", True, (255, 255, 255))
		    screen.blit(over_text, (200, 250))
		    
		    running  = False
		    return



		def player(x, y,explosion = 0):

		        screen.blit(playerImg, (x, y))

		        #global playerImg =pygame.image.load('explosion.png')
		        #screen.blit(playerImg, (x, y))



		def enemy(x, y, i):

		    screen.blit(enemyImg[i], (x, y))
		def rocket_enemy(x,y,i):

		        screen.blit(rocketenemyImg[i],(x,y))


		def fire_bullet(x, y):
		    global bullet_state

		    bullet_state = "fire"
		    print(bullet_state)
		    screen.blit(bulletImg,(x + 16, y + 10))
		def enemy_firebullet(x,y):
		    global enemy_bullet_state
		    enemy_bullet_state = "fire"
		    screen.blit(enemy_bulletImg, (x + 16, y + 10))


		def isCollision(enemyX, enemyY, bulletX, bulletY):
		    distance = math.sqrt(math.pow(enemyX - bulletX, 2) + (math.pow(enemyY - bulletY, 2)))
		    if distance < 27:
		        return True
		    else:
		        return False
		def iscollision_with_player(playerX, playerY, enemy_bulletX, enemy_bulletY):
		    distance = math.sqrt(math.pow(playerX - enemy_bulletX, 2) + (math.pow(playerY - enemy_bulletY, 2)))
		    if distance < 20:
		        return True
		    else:
		        return False




		# Game Loop
		running = True
		while running:

		    # RGB = Red, Green, Blue
		    screen.fill((0, 0, 0))
		    # Background Image
		    screen.blit(background, (0, 0))
		    for event in pygame.event.get():
		        if event.type == pygame.QUIT:
		            running = False

		        # if keystroke is pressed check whether its right or left
		        if event.type == pygame.KEYDOWN:
		            if event.key == pygame.K_LEFT:
		                playerX_change = -5
		            if event.key == pygame.K_RIGHT:
		                playerX_change = 5
		            if event.key == pygame.K_SPACE:
		               print("shot ready")
		               if bullet_state == "ready":
		               	 print("here")
		                    #bulletSound = mixer.Sound("laser.wav")
		                    #bulletSound.play()
		                    # Get the current x cordinate of the spaceship
		                 bulletX = playerX
		                 fire_bullet(bulletX, bulletY)
		        print(bullet_state)

		        if event.type == pygame.KEYUP:
		            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
		                playerX_change = 0

		    # 5 = 5 + -0.1 -> 5 = 5 - 0.1
		    # 5 = 5 + 0.1

		    playerX += playerX_change
		    if playerX <= 0:
		        playerX = 0
		    elif playerX >= 736:
		        playerX = 736

		    # Enemy Movement
		    for i in range(num_of_enemies):

		        # Game Over
		        if enemyY[i] > 500:
		            for j in range(num_of_enemies):
		                enemyY[j] = 2000
		            game_over_text()


		        enemyX[i] += enemyX_change[i]
		        if enemyX[i] <= 0:
		            enemyX_change[i] = 4
		            enemyY[i] += enemyY_change[i]
		        elif enemyX[i] >= 736:
		            enemyX_change[i] = -4
		            enemyY[i] += enemyY_change[i]







		    #rocket_enemy_movement
		    for i in range(num_of_rocketenemies):
		        #print(num_of_rocketenemies)

		        rocketenemyX[i] += enemyX_change[i]
		        if rocketenemyX[i] <= 0:
		            enemyX_change[i] = 4
		        elif(rocketenemyX[i] >= 736):
		            enemyX_change[i] = -4


		        # Collision
		        collision = isCollision(enemyX[i], enemyY[i], bulletX, bulletY)
		        collision_with_player = iscollision_with_player(playerX,playerY,enemy_bulletX,enemy_bulletY)
		        if( collision_with_player):
		            enemy_bulletY = 2000
		            for j in range(num_of_enemies):
		                enemyY[j] = 2000
		            for  j in range(num_of_rocketenemies):
		                rocketenemyY[j] = 2000
		            player(playerX,playerY,1)
		            game_over_text()


		        if collision:
		            #explosionSound = mixer.Sound("explosion.wav")
		            #explosionSound.play()
		            bulletY = 480
		            bullet_state = "ready"
		            score_value += 1
		            enemyX[i] = random.randint(0, 736)
		            enemyY[i] = random.randint(50, 150)
		        collision = isCollision(rocketenemyX[i], rocketenemyY[i], bulletX, bulletY)
		        if collision:
		            #explosionSound = mixer.Sound("explosion.wav")
		            #explosionSound.play()
		            bulletY = 480
		            bullet_state = "ready"
		            score_value += 1
		            rocketenemyX[i] = random.randint(0, 736)
		            rocketenemyY[i] = random.randint(50, 150)


		        enemy(enemyX[i], enemyY[i], i)
		        rocket_enemy(rocketenemyX[i],rocketenemyY[i],i)


		    # Bullet Movement
		    if bulletY <= 0:
		        bulletY = 480
		        bullet_state = "ready"
		        print(bullet_state)

		    if bullet_state == "fire":
		     print("here shotted")
		     fire_bullet(bulletX, bulletY)
		     bulletY -= bulletY_change



		    if(enemy_bullet_state == "ready"):
		        num = random.randint(0, 2)
		        enemy_bulletX = rocketenemyX[num]
		        enemy_bulletY = rocketenemyY[num]
		        enemy_bullet_state = "fire"

		        #enemybulletfire
		    if(enemy_bulletY>= 589):
		        num = random.randint(0, 2)
		        enemy_bulletX = rocketenemyX[num]
		        enemy_bulletY = rocketenemyY[num]




		    enemy_firebullet(enemy_bulletX,enemy_bulletY)
		    enemy_bulletY += enemy_bulletY_change



		    player(playerX, playerY)
		    show_score(textX, testY)
		    pygame.display.update()
if __name__ == '__main__':
	pygame.init()

# create the screen
	screen = pygame.display.set_mode((800, 600))


# Background
	background = pygame.image.load('background.png')
	pygame.display.set_caption("Space Invader")
	start(screen,background)
	