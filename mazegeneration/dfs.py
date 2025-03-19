import pygame
import random 

SCREEN_HEIGHT = 1920
SCREEN_WIDTH = 1080
cellLength = 2
COLS,ROWS = SCREEN_WIDTH//cellLength, SCREEN_HEIGHT//cellLength
window = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
running = True
cells = []

class Cell:

    def __init__(self,cx,cy):
        self.x = cx
        self.y = cy
        self.isVisited = False 
        self.walls = {
            "top":True,
            "bottom":True,
            "left":True,
            "right":True
        }
        self.isActive = False



    def draw(self,window):
        transformedX = self.x*cellLength
        transformedY = self.y*cellLength

        if(self.isVisited):
            pygame.draw.rect(window,"white",(transformedX,transformedY,cellLength,cellLength))
        if(self.isActive):
            pygame.draw.rect(window,"red",(transformedX,transformedY,cellLength,cellLength))
            self.isActive = False

        if(self.walls["top"]):
            pygame.draw.line(window,"black",(transformedX,transformedY),(transformedX+cellLength,transformedY))
        if(self.walls["left"]):
            pygame.draw.line(window,"black",(transformedX,transformedY),(transformedX,transformedY+cellLength))
        if(self.walls["bottom"]):
            pygame.draw.line(window,"black",(transformedX,transformedY+cellLength),(transformedX+cellLength,transformedY+cellLength))
        if(self.walls["right"]):
            pygame.draw.line(window,"black",(transformedX+cellLength,transformedY),(transformedX+cellLength,transformedY+cellLength))

    def getCellAt(self,x,y):
        if x<0 or x>=COLS or y<0 or y >=ROWS:
            return False
        return cells[x+y*COLS]
    def getUnvisitedNeighbors(self):

        neighbors = []

        directions = [('top',0,-1),('right',1,0),('bottom',0,1),('left',-1,0)]
        for direction,dx,dy in directions:
            neighbor = self.getCellAt(self.x+dx,self.y+dy)
            if neighbor and not neighbor.isVisited:
                neighbors.append((direction,neighbor))
        
        return neighbors
    



def removeWall(currentCell,nextCell,direction):

    oppposite = {"top":"bottom","left":"right","bottom":"top","right":"left"}
    currentCell.walls[direction] = False
    nextCell.walls[oppposite[direction]] = False



cells = [Cell(x,y) for y in range(ROWS) for x in range(COLS)]

currentCell = cells[0]
currentCell.isVisited = True
currentCell.isActive = True
visitedCells = [currentCell]
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    window.fill("Grey")

    neighbors  = currentCell.getUnvisitedNeighbors()
    if neighbors:
        direction,nextCell = random.choice(neighbors)
        nextCell.isVisited = True
        removeWall(currentCell,nextCell,direction)
        visitedCells.append(nextCell)
        currentCell = nextCell
        currentCell.isActive = True
    elif visitedCells:
        currentCell = visitedCells.pop()
        currentCell.isActive = True

    [cell.draw(window) for cell in cells]


    pygame.display.update()
