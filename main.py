import pygame
import math
import random
from pygame import mixer
#INITAIALIZE
pygame.init()

#CREATE A SCREEN
screen = pygame.display.set_mode((800,600))

#background
background =pygame.image.load('background.png')

#background music
mixer.music.load('highway intro.wav')
mixer.music.play(-1)

# TITLE AND ICON
pygame.display.set_caption("SPACE INVADERS")
icon = pygame.image.load('spaceship.png')
pygame.display.set_icon(icon)

# PLAYER
playerimg =pygame.image.load('space-invaders.png')
playerx = 370
playery = 480
xchange = 0

#enemy
enemyimg = []
enemyx = []
enemyy = []
exchange = []
eychange = []
numofenemy = 6
for i in range(numofenemy):
    enemyimg.append(pygame.image.load('space-ship.png'))
    enemyx.append(random.randint(0,735))
    enemyy.append(random.randint(50,150))
    exchange.append(4)
    eychange.append(20)

#bullet
bulletimg =pygame.image.load('bullet.png')
bulletx = 0
bullety = 480
bxchange = 0
bychange = 10
bulletstate = "ready"

#score
scorevalue =0
font = pygame.font.Font('freesansbold.ttf', 32)
textx = 10
texty = 10
over = pygame.font.Font('freesansbold.ttf', 64)

def gameovertxt():
    overtxt = over.render("GAME OVER",True,(255,255,255))
    screen.blit(overtxt, (200,250))

def showscore(x,y):
    score = font.render("Score :"+ str(scorevalue),True,(255,255,255))
    screen.blit(score, (x,y))
def player (x,y ):
    screen.blit(playerimg, (x,y))
def enemy (x,y,i):
    screen.blit(enemyimg[i], (x,y))

def fire(x,y):
    global  bulletstate
    bulletstate = "fire"
    screen.blit(bulletimg, (x+16,y+16))

def collision (enemyx,enemyy,bulletx,bullety):
    distance =  math.sqrt((math.pow((enemyx - bulletx),2))+ (math.pow((enemyy-bullety),2)))
    if distance < 27 :
        return True
    else:
        return False


#SCREEN EXIT LOOP
running = True
while running:
     screen.fill((2,0,0))
     screen.blit(background , (0,0))

     for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # if keystroke is pressed check weather its rigth or left
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                xchange=-5
            if event.key == pygame.K_RIGHT:
               xchange=5
            if event.key == pygame.K_SPACE:
                if bulletstate is "ready":
                    bulletsound = mixer.Sound('gun-gunshot-02.wav')
                    bulletsound.play()
                    bulletx = playerx
                    fire(bulletx,bullety)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT :
                xchange=0




                # cheching for boundaries

     playerx+=xchange
     if playerx <=0:
         playerx=0
     elif playerx>= 736:
        playerx=736
     
     for i in range(numofenemy):

         #gameover
         if enemyy[i] > 440 :
             for j in range(numofenemy):
                    enemyy[j] = 2000
             gameovertxt()
             break

         enemyx[i]+=exchange[i]
         if enemyx[i] <=0:
            exchange[i]=10
            enemyy[i]+=eychange[i]
         elif enemyx[i]>= 736:
            exchange[i] = -10
            enemyy[i]+=eychange[i]
            # collision
         coll = collision(enemyx[i], enemyy[i], bulletx, bullety)  
         if coll:
            collsound = mixer.Sound('mixkit-arcade-chiptune-explosion-1691.wav')
            collsound.play()
            bullety = 480
            bulletstate ="ready"
            scorevalue += 1
            enemyx[i] = random.randint(0,735)
            enemyy[i] = random.randint(50,150)

         enemy(enemyx[i],enemyy[i],i)

        

        #bullet movement
     if bullety <=0:
         bullety =480
         bulletstate = "ready"
     
     if bulletstate is "fire":
        fire(bulletx, bullety)
        bullety -= bychange
      
     
        
     player(playerx,playery)
     showscore(textx, texty)
     pygame.display.update()