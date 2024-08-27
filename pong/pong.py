import pygame
import sys
import random
import math
pygame.init()
W = 1200
H = 900
screen = pygame.display.set_mode((W,H))
pygame.display.set_caption('Ping Pong')
clock = pygame.time.Clock()
running = True
class AIPlayer:
    def __init__(self, player, pong):
        self.player = player
        self.pong = pong

    def move(self):
        if self.pong.y < self.player.y + self.player.height // 2:
            self.player.y -= 10
        elif self.pong.y > self.player.y + self.player.height // 2:
            self.player.y += 10


class Player:
    def __init__(self,x,y,width,height,color):
        self.x  = x
        self.y =  y
        self.width = width
        self.height  = height 
        self.color  = color
    
    def draw(self):
        pygame.draw.rect(screen,self.color,(self.x,self.y,self.width,self.height))

player1 = Player(50,50,50,300,'red')
player2 = Player(1100,50,50,300,'blue')
sound = pygame.mixer.music.load('mixkit-game-ball-tap-2073.wav')
class Pong:
    def __init__(self,x,y,radius):
        self.x = x
        self.y = y
        self.radius = radius 
        self.x_speed = random.choice([-10,8])
        self.y_speed = random.choice([-10,8])
    def check_collide(self):
        if self.x -self.radius <= player1.x+player1.width and (self.y in range(player1.y,player1.y+player1.height+1)):
            return 'collision with player1'
        elif  self.x+self.radius >= player2.x - player2.width and (self.y in range(player2.y,player2.y+player2.height+1)):
            return 'collision with player2'
        return None
    def move(self):
        self.x += self.x_speed
        self.y += self.y_speed
        if self.y - self.radius <= 0 or self.y + self.radius >= H:
                self.y_speed = -self.y_speed
    def bounce(self):
        if self.check_collide():
            if self.check_collide() == 'collision with player1':
                pygame.mixer.music.play()
                print('collision1')
                norm = [1,0]
            elif self.check_collide() == 'collision with player2':
                print('collision2')
                pygame.mixer.music.play()
                norm = [-1,0]
            dot_product  = self.x_speed*norm[0]+self.y_speed*norm[1]
            self.x_speed -= 2*dot_product*norm[0]
            self.y_speed -= 2*dot_product*norm[1]
    def draw(self):
        pygame.draw.circle(screen,'yellow',(self.x,self.y),self.radius)


    def call(self):
        self.x = 600
        self.y = 450
pong  = Pong(600,450,20)
score_player1 = 0
score_player2 = 0
font = pygame.font.Font(None, 74)
ai_player = AIPlayer(player2, pong)
while running:
    screen.fill('Black')
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and not player1.y<0:
        player1.y -= 20
    if keys[pygame.K_s] and not player1.y+player1.height>H:
        player1.y += 20
    moves = ['w','s']
    move  = random.choice(moves)
    if keys[pygame.K_j]  and not player2.y <0:
        player2.y -= 20
    if keys[pygame.K_k]  and not player2.y+player2.height>H:
        player2.y += 20
    if pong.x < 0 :
        score_player2 += 1
        pong.call()
    elif pong.x > W :
        score_player1 += 1
        pong.call()
    
    ai_player.move()
    player1.draw()
    player2.draw()
    pong.draw()
    pong.move()
    pong.bounce()
    score_text_player1 = font.render(str(score_player1), True, (255, 255, 255))
    score_text_player2 = font.render(str(score_player2), True, (255, 255, 255))
    screen.blit(score_text_player1, (W // 4, 50))
    screen.blit(score_text_player2, (3 * W // 4, 50))
    pygame.display.update()
    clock.tick(60)
