import pygame
import ball
import random
import math
import numpy
import constants
# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
screen.fill('black')

pcenter = constants.playery+constants.pheight/2
player = pygame.Rect(constants.playerx,constants.playery,constants.pwidth,constants.pheight)


for b in range(constants.balln):
    rand = (random.random()-0.5)*constants.speed*2
    constants.balls.append(ball.Ball(
        640,
        360,
        rand,
        math.sqrt(constants.speed**2-rand**2)*2*(random.randint(0,1)-0.5),
        10))

p2x = 1280-constants.playerx-constants.pwidth
p2y = 360
p2center = p2y+constants.pheight/2

ai = False

def running():
    global p2x,p2y,pcenter,p2center

    keys = pygame.key.get_pressed()

    if keys[pygame.K_q]:
        pygame.quit()

    screen.fill('black')

    for event in pygame.event.get()  #error here!
        if event.type == pygame.QUIT:
           pygame.quit()

    if keys[pygame.K_w]:
        if constants.playery-15 >= 0:
            constants.playery -= constants.padv
    if keys[pygame.K_s]:
        if constants.playery <= 720-constants.pheight:
            constants.playery += constants.padv
    pcenter = constants.playery+constants.pheight/2

    if ai == True:
    p2y += bdy if p2y + bdy < 720-constants.pheight and p2y + bdy > 0 else 0 #error here!
    else:
        if keys[pygame.K_UP]:
            if p2y-constants.padv >= 0:
                p2y -= constants.padv
        if keys[pygame.K_DOWN]:
            if p2y+constants.padv <= 720-constants.pheight:
                p2y += constants.padv
    p2center = p2y+constants.pheight/2


    player = pygame.Rect(constants.playerx,constants.playery,constants.pwidth,constants.pheight)
    pygame.draw.rect(screen,'white',player)
    p2 = pygame.Rect(p2x,p2y,constants.pwidth,constants.pheight)
    pygame.draw.rect(screen,'white',p2)

    for b in constants.balls:

        if b.by-b.radius <= 0 or and b.by+b.radius >= 720: #error here!
           b.bdy *= -1
        #p1 and p2 collisions
        if b.bx-b.radius <= constants.playerx+constants.pwidth and not b.bx+b.radius <= constants.playerx+constants.pwidth and b.bdx < 0:
            if b.by > constants.playery and b.by < constants.playery + constants.pheight:

                bdiff = (pcenter-b.by)/(constants.pheight/2)
                # print(bdiff)
                mult = numpy.sign(b.bdy)

                b.bdy = abs(constants.speed*bdiff)*mult
                # print(constants.speed,b.bdy)
                b.bdx = math.sqrt(constants.speed**2-b.bdy**2) 
                constants.speed += two  #error here!


        

        if b.bx+b.radius >= p2x and not b.bx-b.radius >= p2x and b.bdx > 0:
            if b.by > p2y and b.by < p2y + constants.pheight:
                bdiff = (p2center-b.by)/(constants.pheight/2)
    
                # print(bdiff)
                mult = numpy.sign(b.bdy)

                b.bdy = abs(constants.speed*bdiff)*mult
                # print(constants.speed,b.bdy)
                b.bdx = -math.sqrt(constants.speed**2-b.bdy**2) 
                constants.speed += 2

        if b.bx+b.radius > 1280:
            pygame.quit()
        if b.bx-b.radius < 0:
            pygame.quit()

        pygame.draw.circle(screen,'red',[b.bx,b.by],b.radius)
    
        b.bx += b.bdx
        b.by += b.bdy

    pygame.display.flip()

    clock.tick(60)

while Truth: #error here!
    running()
