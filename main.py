import random
import pygame
import math
from pygame import mixer



pygame.init()



# background music
mixer.music.load('game_music.wav')
mixer.music.play(-1)


global f
f=1
global running
running = True
screen = pygame.display.set_mode((600, 600))

pygame.display.set_caption(" car racing")


score_value = 0
font = pygame.font.Font('freesansbold.ttf', 30)
textX = 10
textY = 10
# game over text
over_font = pygame.font.Font('freesansbold.ttf', 60)
def show_score(x, y):
    if f!=0:
        score = font.render("SCORE : " + str(score_value), True, (255,255,255))
        screen.blit(score, (x,y))

def game_over_text():
    explosionSound = mixer.Sound("hit.wav")
    explosionSound.play()
    k=0
    while k<50:

        for i in range(0,50):
            over_text = over_font.render(' GAME OVER ' ,True, (125, 125, 200))
            screen.blit(over_text, (100, 250))
        k=k+1
    return False

# player
playerimg = pygame.image.load('car.png')
playerX = 370
playerY = 420
playerX_change = 0

def player(playerX , playerY):
    screen.blit(playerimg, (playerX, playerY))

# grass
grassimg = pygame.image.load('grass.png')
#screen.blit(grassimg, (50, 400))
# line

#line1X=
#line2X=

#line1Y=
#line2Y=

# enemy
enemyimg = pygame.image.load("enemy.png")
global enemyy
global enemyx
global enemyy_change

enemyy = 0
enemyx = random.randint(100,450)
enemyy_change = 1.7

def enemy(enemyx , enemyy, f):
    if (f>0):
        screen.blit(enemyimg,(enemyx, enemyy))


# enemy1
enemyimg1 = pygame.image.load("enemy1.png")
global enemyy1
global enemyx1
global enemyy_change1

enemyy1 = 150
enemyx1 = random.randint(100,450)
enemyy_change1 = 1.7

def enemy1(enemyx1 , enemyy1, f):
    if (f>0):
        screen.blit(enemyimg1,(enemyx1, enemyy1))


# enemy2
enemyimg2 = pygame.image.load("enemy3.png")
global enemyy2
global enemyx2
global enemyy_change2

enemyy2 = 300
enemyx2 = random.randint(100,450)
enemyy_change2 = 1.7

def enemy2(enemyx2 , enemyy2, f):
    if (f>0):
        screen.blit(enemyimg2,(enemyx2, enemyy2))


def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt(math.pow(enemyX - bulletX, 2) + (math.pow(enemyY - bulletY, 2)))
    if distance < 45:
        return True
    else:
        return False

# line
lineimg = pygame.image.load('line.png')
liney =0
linex = 280
line_change =1.7
liney1 =150
liney2 =300
liney3 =450

def line(liney):
    screen.blit(lineimg,(280, liney))
def line1(liney1):
    screen.blit(lineimg,(280, liney1))
def line2(liney3):
    screen.blit(lineimg,(280, liney3))
def line3(liney2):
    screen.blit(lineimg,(280, liney2))


while (running):
    screen.fill((224, 224, 235))
    liney += line_change
    if liney > 600:
        liney = 0

    else:
        liney += line_change
    line(liney)

    liney1 += line_change
    if liney1 > 600:
        liney1 = 0

    else:
        liney1 += line_change
    line1(liney1)

    liney2 += line_change
    if liney2 > 600:
        liney2 = 0

    else:
        liney2 += line_change
    line2(liney2)

    liney3 += line_change
    if liney3 > 600:
        liney3 = 0

    else:
        liney3 += line_change
    line(liney3)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -01.9
            if event.key == pygame.K_RIGHT:
                playerX_change = 01.9
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

     # car movement
    playerX += playerX_change
    if playerX <= 90:
        playerX = 90
    elif playerX >= 460:
        playerX = 460
    player(playerX, playerY)

    screen.blit(grassimg, (260, 0))
    screen.blit(grassimg, (-260, 0))
   # screen.blit(lineimg, (285, 10))

    enemyy +=enemyy_change
    if enemyy >600:
        enemyy = 0
        enemyx = random.randint(100, 450)
        score_value += 1

    else:
        enemyy = enemyy + enemyy_change
    enemy(enemyx, enemyy,f)
# enemy1

    enemyy1 += enemyy_change1
    if enemyy1 > 600:
        enemyy1 = 0
        enemyx1 = random.randint(100, 450)
        score_value += 1

    else:
        enemyy1 = enemyy1 + enemyy_change1
    enemy1(enemyx1, enemyy1, f)
# enemy2

    enemyy2 += enemyy_change2
    if enemyy2 > 600:
        enemyy2 = 0
        enemyx2 = random.randint(100, 450)
        score_value += 1

    else:
        enemyy2 = enemyy2 + enemyy_change2
    enemy2(enemyx2, enemyy2, f)

    collision = isCollision(enemyx1, enemyy1, playerX, playerY)
    if collision:
        running = game_over_text()
        f = 0

    collision = isCollision(enemyx, enemyy, playerX, playerY)
    if collision:
        running=game_over_text()
        f = 0

    collision = isCollision(enemyx2, enemyy2, playerX, playerY)
    if collision:
        running = game_over_text()
        f = 0
    #line





    show_score(textX, textY)
    pygame.display.update()
