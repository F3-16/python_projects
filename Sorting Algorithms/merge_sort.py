import pygame
import random
import numpy as np
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
clock = pygame.Clock()
running = True
array_len = SCREEN_WIDTH
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
    
pygame.mixer.init()

def generate_tone(frequency, duration=50):
    """
    Generates a sound wave of a given frequency and plays it.
    """
    sample_rate = 44100  # Standard sample rate
    samples = np.sin(2 * np.pi * np.arange(sample_rate * duration / 1000) * frequency / sample_rate).astype(np.float32)

    # Convert to stereo by duplicating samples
    sound = np.column_stack((samples, samples))

    # Create a sound object and play it
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

def merge(array, start, mid, end):
    left_array = array[start:mid]
    right_array = array[mid:end]

    i = j = 0
    k = start

    while i < len(left_array) and j < len(right_array):
        if left_array[i].height <= right_array[j].height:
            array[k] = left_array[i]
            frequency = (array[k].height / max([x.height for x in array])) * 500 
            generate_tone(frequency)
            array[k].coordinate[0] = k * column_width
            i += 1
        else:
            array[k] = right_array[j]
            array[k].coordinate[0] = k * column_width
            frequency = (array[k].height / max([x.height for x in array])) * 500 
            generate_tone(frequency)
            j += 1
        draw_cols(screen)
        k += 1

    while i < len(left_array):
        array[k] = left_array[i]
        array[k].coordinate[0] = k * column_width
        frequency = (array[k].height / max([x.height for x in array])) * 500 
        generate_tone(frequency)
        draw_cols(screen)
        i += 1
        k += 1

    while j < len(right_array):
        array[k] = right_array[j]
        array[k].coordinate[0] = k * column_width
        frequency = (array[k].height / max([x.height for x in array])) * 500 
        generate_tone(frequency)
        draw_cols(screen)
        j += 1
        k += 1

    draw_cols(screen)


def merge_sort(array, start, end):
    if start + 1 < end:  # Fix base case
        mid = start + (end - start) // 2
        merge_sort(array, start, mid)
        merge_sort(array, mid, end)
        merge(array, start, mid, end)





arrayInitialize(array)
while running:
        
    for event in pygame.event.get():
        if event.type ==  pygame.QUIT:
            running = False

    if algo_run:
        merge_sort(array,0,len(array)-1)
        algo_run = False

    



pygame.quit()
s
