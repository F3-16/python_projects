import pygame
import sys
from pygame.math import Vector2
import random 
pygame.init()
WIDTH = 1920//2
HEIGHT = 1080//2
screen = pygame.display.set_mode((WIDTH,HEIGHT))
running = True
clock = pygame.time.Clock()
class Food:
    def __init__(self):
        self.spawnpoint_x = random.randint(0,WIDTH+1)
        self.spawnpoint_y = random.randint(0,HEIGHT+1)
    def get_new_pos(self):
        self.spawnpoint_x =random.randint(0,WIDTH+1)
        self.spawnpoint_y = random.randint(0,HEIGHT+1)
    def draw(self):
        pygame.draw.circle(screen,'Blue',(self.spawnpoint_x,self.spawnpoint_y),5)
food = Food()
class Snake:
    def __init__(self):
        self.body = [Vector2(5,9),Vector2(6,9),Vector2(7,9)]
        self.rightdirection= Vector2(1,0)
        self.leftdirection = Vector2(-1,0)
        self.updirection  = Vector2(0,-1)
        self.downdirection = Vector2(0,1)
    def draw(self):
        for segment in self.body:
            segment_rect = [segment.x*10,segment.y*10,10,10]
            pygame.draw.rect(screen,'Red',segment_rect)
    def update(self):
        if keys[pygame.K_w] and keys[pygame.K_s]!=1:
            self.body = self.body[:-1]
            new_head = self.body[0]+self.updirection 
            if new_head.y < 0 :
                new_head.y  = HEIGHT//10 +1
            self.body.insert(0,new_head)
        if keys[pygame.K_s] and keys[pygame.K_w]!=1:
            self.body = self.body[:-1]
            new_head = self.body[0]+self.downdirection
            if new_head.y >HEIGHT//10:
                new_head.y = 1
            self.body.insert(0,new_head)
        if keys[pygame.K_d] and keys[pygame.K_a]!=1:
            self.body = self.body[:-1]
            new_head =self.body[0]+self.rightdirection
            if new_head.x > WIDTH//10:
                new_head.x =1
            self.body.insert(0,new_head)
        if keys[pygame.K_a] and keys[pygame.K_d]!=1:
            self.body = self.body[:-1]
            new_head = self.body[0]+self.leftdirection
            if new_head.x < 0:
                new_head.x = WIDTH//10+1
            self.body.insert(0,new_head) 
snake = Snake()
while running:
    keys = pygame.key.get_pressed()
    screen.fill("Black")
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
    food.draw()
    snake.update()
    snake.draw()
    if (snake.body[0].x,snake.body[0].y) == (food.spawnpoint_x//10,food.spawnpoint_y//10):
        snake.body.insert(0,snake.body[0]+Vector2(1,0))
        food.get_new_pos()
    print(snake.body)
    clock.tick(10) 
    pygame.display.update()
