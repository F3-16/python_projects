import pygame
import sys
from random import choice

W, H = 1200, 900
TILES = 20
cols, rows = W // TILES, H // TILES
screen = pygame.display.set_mode((W, H))
clock = pygame.time.Clock()
running = True

class Cell:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.visited = False
        self.walls = {
            'top': True,
            'bottom': True,
            'left': True,
            'right': True
        }

    def draw_current(self):
        pygame.draw.rect(screen,'red',(self.x*TILES,self.y*TILES,TILES,TILES))
    def draw(self):
        x = self.x * TILES
        y = self.y * TILES
        if self.visited:
            pygame.draw.rect(screen, 'white', (x, y, TILES, TILES))
        if self.walls['top']:
            pygame.draw.line(screen, 'black', (x, y), (x + TILES, y))
        if self.walls['bottom']:
            pygame.draw.line(screen, 'black', (x + TILES, y + TILES), (x, y + TILES))
        if self.walls['right']:
            pygame.draw.line(screen, 'black', (x + TILES, y), (x + TILES, y + TILES))
        if self.walls['left']:
            pygame.draw.line(screen, 'black', (x, y), (x, y + TILES))

    def check_cells(self, x, y):
        if x < 0 or x >= cols or y < 0 or y >= rows:
            return False
        return cells[x + y * cols]

    def check_neighbors(self):
        neighbors = []
        directions = [('top', 0, -1), ('right', 1, 0), ('bottom', 0, 1), ('left', -1, 0)]
        for direction, dx, dy in directions:
            neighbor = self.check_cells(self.x + dx, self.y + dy)
            if neighbor and not neighbor.visited:
                neighbors.append((direction, neighbor))
        return neighbors

def remove_wall(current_cell, next_cell, direction):
    opposite = {'top': 'bottom', 'bottom': 'top', 'left': 'right', 'right': 'left'}
    current_cell.walls[direction] = False
    next_cell.walls[opposite[direction]] = False

cells = [Cell(col, row) for row in range(rows) for col in range(cols)]
current_cell = cells[0]
current_cell.visited = True
visited_cells = [current_cell]

while running:
    screen.fill("grey")
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    [cell.draw() for cell in cells]
    current_cell.draw_current()
    neighbors = current_cell.check_neighbors()
    if neighbors:
        direction, next_cell = choice(neighbors)
        next_cell.visited = True
        remove_wall(current_cell, next_cell, direction)
        visited_cells.append(next_cell)
        current_cell = next_cell
    elif visited_cells:
        current_cell = visited_cells.pop()
    clock.tick(120)
    pygame.display.update()


