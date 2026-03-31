import pygame
import ball
import random
import math
import numpy
# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
screen.fill('black')

padv = 15
balln = 1
balls = []
playerx = 150
playery = 310
pwidth = 10
pheight = 100
pcenter = playery+pheight/2
player = pygame.Rect(playerx,playery,pwidth,pheight)
speed = 5

for b in range(balln):
    rand = (random.random()-0.5)*speed*2
    balls.append(ball.Ball(
        640,
        360,
        rand,
        math.sqrt(speed**2-rand**2)*2*(random.randint(0,1)-0.5),
        10))

p2x = 1280-playerx-pwidth
p2y = 360
p2center = p2y+pheight/2

ai = False

def running():
    global playerx,playery,pwidth,pheight,p2x,p2y,padv,balls,pcenter,p2center,speed

    keys = pygame.key.get_pressed()

    if keys[pygame.K_q]:
        pygame.quit()

    screen.fill('black')

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
           pygame.quit()

    if keys[pygame.K_w]:
        if playery-15 >= 0:
            playery -= padv
    if keys[pygame.K_s]:
        if playery <= 720-pheight:
            playery += padv
    pcenter = playery+pheight/2

    if ai == True: #fix
            p2y += bdy if p2y + bdy < 720-pheight and p2y + bdy > 0 else 0
    else:
        if keys[pygame.K_UP]:
            if p2y-padv >= 0:
                p2y -= padv
        if keys[pygame.K_DOWN]:
            if p2y+padv <= 720-pheight:
                p2y += padv
    p2center = p2y+pheight/2


    player = pygame.Rect(playerx,playery,pwidth,pheight)
    pygame.draw.rect(screen,'white',player)
    p2 = pygame.Rect(p2x,p2y,pwidth,pheight)
    pygame.draw.rect(screen,'white',p2)

    for b in balls:

        if b.by-b.radius <= 0 or b.by+b.radius >= 720:
           b.bdy *= -1
        #p1 and p2 collisions
        if b.bx-b.radius <= playerx+pwidth and not b.bx+b.radius <= playerx+pwidth and b.bdx < 0:
            if b.by > playery and b.by < playery + pheight:

                bdiff = (pcenter-b.by)/(pheight/2)
                # print(bdiff)
                mult = numpy.sign(b.bdy)

                b.bdy = abs(speed*bdiff)*mult
                # print(speed,b.bdy)
                b.bdx = math.sqrt(speed**2-b.bdy**2) 
                speed += 2


        

        if b.bx+b.radius >= p2x and not b.bx-b.radius >= p2x and b.bdx > 0:
            if b.by > p2y and b.by < p2y + pheight:
                bdiff = (p2center-b.by)/(pheight/2)
    
                # print(bdiff)
                mult = numpy.sign(b.bdy)

                b.bdy = abs(speed*bdiff)*mult
                # print(speed,b.bdy)
                b.bdx = -math.sqrt(speed**2-b.bdy**2) 
                speed += 2

        if b.bx+b.radius > 1280:
            pygame.quit()
        if b.bx-b.radius < 0:
            pygame.quit()

        pygame.draw.circle(screen,'red',[b.bx,b.by],b.radius)
    
        b.bx += b.bdx
        b.by += b.bdy

    pygame.display.flip()

    clock.tick(60)

while True:
    running()
