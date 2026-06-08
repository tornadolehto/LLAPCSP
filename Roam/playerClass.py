import pygame
import os
import math

class Player:
    shape = 'circle'
    heading = None
    x = None
    y = None

    def __init__(self,radius,heading,x,y):
        self.heading = heading
        self.radius = radius
        self.x=x
        self.y=y
    
    def rotate(self,degrees):
        self.heading += degrees
    
    def move(self,speed):
        self.x += math.cos(self.heading)*180/math.pi*speed
        self.y += math.sin(self.heading)*180/math.pi*speed



