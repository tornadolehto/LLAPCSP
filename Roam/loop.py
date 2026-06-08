import pygame
import os
import playerClass
import line
import math
running = True
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
mspeed = 0.1
vmask = 5

character = playerClass.Player(10,0,500,500)

while running:
    screen.fill('white')
    velocity = line.Line((character.x,character.y),())

    keys = pygame.key.get_pressed()

    if keys[pygame.K_q]:
        pygame.quit()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
           pygame.quit()

    if keys[pygame.K_a]:
        character.rotate(-0.05)
    if keys[pygame.K_d]:
        character.rotate(0.05)

    speed = 0
    if keys[pygame.K_w]: #implement second order movement
        speed = mspeed
        character.move(speed)
    if keys[pygame.K_s]:
        speed = -mspeed
        character.move(speed)

    pygame.draw.line(
                 screen,'red',
                (character.x,character.y),
                (character.x + math.cos(character.heading)*180/math.pi*speed*vmask, character.y + math.sin(character.heading)*180/math.pi*speed*vmask),
                5
                )
    print(character.x,character.y)
    

   

    pygame.display.flip()

    clock.tick(20)