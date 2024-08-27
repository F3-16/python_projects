import pygame
import math
import sys
import numpy as np
from random import choice
pygame.init()

width = 1024
height = 768

pygame.display.set_caption("Cube")

screen = pygame.display.set_mode((width,height))

clock = pygame.time.Clock()
white = (255,255,255)
black = (0,0,0)
running = True  
angle = 0
point = [None for _ in range(8)]
point[0] =  np.array([1,1,1])
point[1] = np.array([-1,-1,-1])
point[2] = np.array([1,-1,1])
point[3] = np.array([1,1,-1])
point[4] = np.array([1,-1,-1])
point[5] = np.array([-1,1,-1])
point[6] = np.array([-1,-1,1])
point[7] = np.array([-1,1,1])
projection_matrix = np.array([[1,0,0],
                     [0,1,0], 
                     [0,0,0]])


while running:
    screen.fill(black)
     
    angle = -0.01
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    rotation_x = np.array([[1,0,0],
                          [0,math.cos(angle),-math.sin(angle)],
                          [0,math.sin(angle),math.cos(angle)]])
    rotation_y = np.array([[math.cos(angle),0,math.sin(angle)],
                          [0,1,0],
                          [-math.sin(angle),0,math.cos(angle)]])

    rotation_z  = np.array([[math.cos(angle),-math.sin(angle),0],
                          [math.sin(angle),math.cos(angle),0],
                          [0,0,1]])
    
    
    projected_points = []
    for i in range(len(point)):
        point[i] = np.matmul(rotation_x,point[i])
        point[i] = np.matmul(rotation_y,point[i])
        point[i] = np.matmul(rotation_z,point[i])
    

    
    for p in point:
        projected = np.matmul(projection_matrix,p)
        x = int(projected[0]*200+width//2)
        y = int(projected[1]*200+height//2)
        pygame.draw.circle(screen,white,(x,y),1)
        projected_points.append((x,y))
    
    pygame.draw.line(screen,'red',projected_points[0],projected_points[2],2)
    pygame.draw.line(screen,'green',projected_points[0],projected_points[7],2)
    pygame.draw.line(screen,'blue',projected_points[2],projected_points[6],2)
    pygame.draw.line(screen,'orange',projected_points[6],projected_points[7],2)
    pygame.draw.line(screen,'yellow',projected_points[3],projected_points[5],2)
    pygame.draw.line(screen,'purple',projected_points[3],projected_points[4],2)
    pygame.draw.line(screen,'grey',projected_points[5],projected_points[1],2)
    pygame.draw.line(screen,'aqua',projected_points[4],projected_points[1],2)
    

    pygame.draw.line(screen,'pink',projected_points[0],projected_points[3],2)
    pygame.draw.line(screen,'maroon',projected_points[7],projected_points[5],2)
    pygame.draw.line(screen,'beige',projected_points[2],projected_points[4],2)
    pygame.draw.line(screen,'green',projected_points[1],projected_points[6],2)



    pygame.display.update()
    clock.tick(60)
