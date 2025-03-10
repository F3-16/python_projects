import pygame
import random
import numpy as np
pygame.init()
pygame.mixer.init()
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
clock = pygame.Clock()
running = True
array_len = 400 
column_width = SCREEN_WIDTH/array_len
algo_run = True
array = []
class Column:
    def __init__(self,width,height_corresponding_value,coordinate):
        self.width = width
        self.height = height_corresponding_value
        self.coordinate = coordinate
        self.active = False
        self.color = "white"

    def draw(self,screen):
        pygame.draw.rect(screen,self.color,pygame.Rect(self.coordinate[0],self.coordinate[1]-self.height,self.width,self.height))

    def turnActive(self):
        self.color = "red"
    
    def remainSilent(self):
        self.color = "white"
    

def generate_tone(frequency, duration=50):

    sample_rate = 44100  # Standard sample rate
    samples = np.sin(2 * np.pi * np.arange(sample_rate * duration / 1000) * frequency / sample_rate).astype(np.float32)

    sound = np.column_stack((samples, samples))


    sound_obj = pygame.sndarray.make_sound((32767 * sound).astype(np.int16))
    sound_obj.play()
    
def arrayInitialize(array):
    for x in range(array_len):
        array.append(Column(column_width,random.randint(30,SCREEN_HEIGHT),[x*column_width,SCREEN_HEIGHT]))

def draw_cols(screen):
    screen.fill("black")
    for col in array:
        col.draw(screen)

    pygame.display.flip()
def bubbleSort(array):
    n = len(array)

    for i in range(n):

        swapped = False
        for j in range(0,n-i-1):
            if array[j].height > array[j+1].height:
                frequency = (array[j].height / max([x.height for x in array])) * 500 
                generate_tone(frequency)
                array[j].coordinate[0],array[j+1].coordinate[0] = array[j+1].coordinate[0],array[j].coordinate[0]
                array[j], array[j+1] = array[j+1],array[j]
                array[j+1].turnActive()
                draw_cols(screen)
                array[j+1].remainSilent()
                swapped = True


        if not swapped:
            algo_run = False
            break

arrayInitialize(array)
while running:
        
    for event in pygame.event.get():
        if event.type ==  pygame.QUIT:
            running = False

    if algo_run:
        bubbleSort(array)
        algo_run = False
    
pygame.quit()
