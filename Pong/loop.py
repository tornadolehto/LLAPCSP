import pygame

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
screen.fill('black')

playerx = 100
playery = 310
pwidth = 10
pheight = 100
player = pygame.Rect(playerx,playery,pwidth,pheight)

radius = 30
bx = 640
by = 360
bdx = -10
bdy = -5

def running():
    global playerx,playery,pwidth,pheight,by,bx,bdx,bdy,radius

    keys = pygame.key.get_pressed()

    if keys[pygame.K_q]:
        pygame.quit()

    screen.fill('black')

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
           pygame.quit()

    if keys[pygame.K_UP]:
        if playery > 0:
            playery -= 15
    if keys[pygame.K_DOWN]:
        if playery < 620:
            playery += 15
    player = pygame.Rect(playerx,playery,pwidth,pheight)
    pygame.draw.rect(screen,'white',player)

    if by-radius <= 0 or by+radius >= 720:
        bdy *= -1
    if bx-radius == playerx+pwidth:
        if by > playery and by < playery + pheight:
            bdx *= -1
    if bx+radius > 1280:
        bdx *= -1
    if bx-radius < 0:
        pygame.quit()
    pygame.draw.circle(screen,'red',[bx,by],radius)
 
    bx += bdx
    by += bdy

    pygame.display.flip()

    clock.tick(60)

while True:
    running()
