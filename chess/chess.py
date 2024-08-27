import pygame
import sys

class Tile:
    def __init__(self,x,y,color):
        self.x  = x
        self.y  = y 
        self.occupied = False
        self.color = color
        self.piece = None
    
    def draw(self,screen):
        x = self.x * TILE
        y = self.y * TILE
        pygame.draw.rect(screen,self.color,(x,y,TILE,TILE))


    


pygame.init()
width = 480
height = 480
TILE = 60
cols,rows = width//TILE,height//TILE

screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("Chess")

clock = pygame.time.Clock()
running = True
board = []
helper = 0
check  = 0
for row in range(rows):
        for col in range(cols):
            color = (255,255,255) if (row+col) % 2== 0 else (128,128,128)
            board.append(Tile(col,row,color))

class Piece:

    
    def __init__(self,x,y,color,name):
        self.x = x
        self.y  = y
        self.color = color
        self.name = name 
        self.captured  = False


    def draw(self,screen):
        if not self.captured:
            piece_images = {
                    "pawn": ("pawn_w.png","pawn_b.png"),
                    "rook": ("rook_w.png","rook_b.png"),
                    "knight": ("knight_w.png","knight_b.png"),
                    "bishop": ("bishop_w.png","bishop_b.png"),
                    "queen": ("queen_w.png","queen_b.png"),
                    "king": ("king_w.png","king_b.png")
                }
                
            if self.name in piece_images and self.color == "white":
                img_path = f"pieces_img/{piece_images[self.name][0]}"
                img = pygame.image.load(img_path)
                screen.blit(img, (self.x*TILE, self.y*TILE))
            elif self.name in piece_images and self.color =="black":
                img_path = f"pieces_img/{piece_images[self.name][1]}"
                img = pygame.image.load(img_path)
                screen.blit(img,(self.x*TILE,self.y*TILE))
    def moves(self):
        if not self.captured:
            x = self.x
            y = self.y 
            possible_moves = []

            if self.name == "pawn":
                direction = -1 if self.color == "white" else 1
                if 0 <= y + direction < rows:
                    if not board[x + (y + direction) * cols].occupied:
                        possible_moves.append((x, y + direction))
                    if ((y == 1 and self.color == "black") or (y == 6 and self.color == "white")):
                        if not board[x + (y + 2 * direction) * cols].occupied and not board[x+(y+direction)*cols].occupied:
                            possible_moves.append((x, y + 2 * direction))

                    # Capture moves
                    if x - 1 >= 0 and board[x - 1 + (y + direction) * cols].occupied :
                        if board[x - 1 + (y + direction) * cols].piece.color != self.color:
                            possible_moves.append((x - 1, y + direction))
                    if x + 1 < cols and board[x + 1 + (y + direction) * cols].occupied:
                        if board[x + 1 + (y + direction) * cols].piece.color != self.color:
                            possible_moves.append((x + 1, y + direction))






            elif self.name == "rook":
                for coordinate_y_up in range(y-1,-1,-1):
                    if not board[x+coordinate_y_up*cols].occupied:
                        possible_moves.append((x,coordinate_y_up))
                    else:
                        # Move to capture opponent's piece
                        if board[x+coordinate_y_up*cols].piece.color != self.color:
                            possible_moves.append((x,coordinate_y_up))
                        break
                for coordinate_y_down in range(y+1,8):
                    if not board[x+coordinate_y_down*cols].occupied:
                        possible_moves.append((x,coordinate_y_down))
                    else:
                        # Move to capture opponet's piece
                        if board[x+coordinate_y_down*cols].piece.color != self.color:
                            possible_moves.append((x,coordinate_y_down))
                        break
                for coordinate_x_right in range(x+1,8):
                    if not board[coordinate_x_right+y*cols].occupied:
                        possible_moves.append((coordinate_x_right,y))
                    else:
                        # Move to capture opponent's piece
                        if board[coordinate_x_right+y*cols].piece.color != self.color:
                            possible_moves.append((coordinate_x_right,y))
                        break
                for coordinate_x_left in range(x-1,-1,-1):
                    if not board[coordinate_x_left+y*cols].occupied:
                        possible_moves.append((coordinate_x_left,y))

                    else:
                        # Move to capture opponent's piece
                        if board[coordinate_x_left+y*cols].piece.color != self.color:
                            possible_moves.append((coordinate_x_left,y))
                        break
            elif self.name == "knight":
                knight_moves = [
                    (1, -2), (-1, -2), (2, -1), (-2, -1),
                    (2, 1), (-2, 1), (1, 2), (-1, 2)
                ]
                for dx, dy in knight_moves:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < cols and 0 <= ny < rows:
                        if not board[nx + ny * cols].occupied or board[nx + ny * cols].piece.color != self.color:
                            possible_moves.append((nx, ny))  
                
            elif self.name == "bishop":
                directions = [(1, 1), (1, -1), (-1, 1), (-1, -1)]

                for dx, dy in directions:
                    nx, ny = x, y
                    while True:
                        nx += dx
                        ny += dy
                        if 0 <= nx < cols and 0 <= ny < cols:
                            index = nx + ny * cols
                            if not board[index].occupied:
                                possible_moves.append((nx, ny))
                            else:
                                if board[index].piece.color != self.color:
                                    possible_moves.append((nx, ny))
                                break
                        else:
                            break

            elif self.name == "queen":
                directions = [(1, 1), (1, -1), (-1, 1), (-1, -1)]

                for dx, dy in directions:
                    nx, ny = x, y
                    while True:
                        nx += dx
                        ny += dy
                        if 0 <= nx < cols and 0 <= ny < cols:
                            index = nx + ny * cols
                            if not board[index].occupied:
                                possible_moves.append((nx, ny))
                            else:
                                if board[index].piece.color != self.color:
                                    possible_moves.append((nx, ny))
                                break
                        else:
                            break
                for coordinate_y_up in range(y-1,-1,-1):
                    if not board[x+coordinate_y_up*cols].occupied:
                        possible_moves.append((x,coordinate_y_up))
                    else:
                        # Move to capture opponent's piece
                        if board[x+coordinate_y_up*cols].piece.color != self.color:
                            possible_moves.append((x,coordinate_y_up))
                        break
                for coordinate_y_down in range(y+1,8):
                    if not board[x+coordinate_y_down*cols].occupied:
                        possible_moves.append((x,coordinate_y_down))
                    else:
                        # Move to capture opponet's piece
                        if board[x+coordinate_y_down*cols].piece.color != self.color:
                            possible_moves.append((x,coordinate_y_down))
                        break
                for coordinate_x_right in range(x+1,8):
                    if not board[coordinate_x_right+y*cols].occupied:
                        possible_moves.append((coordinate_x_right,y))
                    else:
                        # Move to capture opponent's piece
                        if board[coordinate_x_right+y*cols].piece.color != self.color:
                            possible_moves.append((coordinate_x_right,y))
                        break
                for coordinate_x_left in range(x-1,-1,-1):
                    if not board[coordinate_x_left+y*cols].occupied:
                        possible_moves.append((coordinate_x_left,y))

                    else:
                        # Move to capture opponent's piece
                        if board[coordinate_x_left+y*cols].piece.color != self.color:
                            possible_moves.append((coordinate_x_left,y))
                        break
            

            elif self.name == "king":
                directions = [ (-1,-1),(0,-1),(1,-1),
                                (-1,0), (1,0),
                            (-1,1) , (0,1) ,(1,1) ] 
                for dx,dy in directions:
                    nx,ny = x,y 
                    nx+=dx
                    ny+=dy 
                    if 0<=nx<cols and 0<=ny<rows:
                        if not board[nx+ny*cols].occupied:
                            possible_moves.append((nx,ny))
                        else:
                            if board[nx+ny*cols].piece.color != self.color:
                                possible_moves.append((nx,ny))
                            
                    



            return possible_moves

                            


    def occupy(self):
        if not self.captured:
            tile = board[self.x+self.y*cols]
            tile.occupied = True
            tile.piece = self
    def vacate(self,x,y):
        if not self.captured:
            tile  = board[x+y*cols]
            tile.occupied = False
            tile.piece = None 
    def show_possible_moves(self):
        if not self.captured:
            for coordinate in self.moves():
                circle_x = coordinate[0]*60+30
                circle_y = coordinate[1]*60+30
                pygame.draw.circle(screen,'aqua',(circle_x,circle_y),20)
    

def king_in_check(color):
    king = white_king if color =="black" else white_king
    king_x, king_y = king.x,king.y 

    opponent_team = black_team if king.color == "white" else white_team

    if king != None:
        for piece in opponent_team:
            if (king_x,king_y) in piece.moves():
                return True 
        return False 
         

black_team  = [
    black_rook1 := Piece(0,0,"black","rook"),
    black_knight1 := Piece(1,0,"black","knight"),
    black_bishop1 := Piece(2,0,"black","bishop"),
    black_queen := Piece(3,0,"black","queen"),
    black_king := Piece(4,0,"black","king"),
    black_bishop2 := Piece(5,0,"black","bishop"),
    black_knight2  := Piece(6,0,"black","knight"),
    black_rook2 := Piece(7,0,"black","rook"),
    black_pawn1 := Piece(0,1,"black","pawn"),
    black_pawn2 := Piece(1,1,"black","pawn"),
    black_pawn3 := Piece(2,1,"black","pawn"),
    black_pawn4 := Piece(3,1,"black","pawn"),
    black_pawn5 := Piece(4,1,"black","pawn"),
    black_pawn6 := Piece(5,1,"black","pawn"),
    black_pawn7 := Piece(6,1,"black","pawn"),
    black_pawn8 := Piece(7,1,"black","pawn"),
]

white_team = [
    white_pawn1 := Piece(0,6,"white","pawn"),
    white_pawn2 := Piece(1,6,"white","pawn"),
    white_pawn3 := Piece(2,6,"white","pawn"),
    white_pawn4 := Piece(3,6,"white","pawn"),
    white_pawn5 := Piece(4,6,"white","pawn"),
    white_pawn6 := Piece(5,6,"white","pawn"),
    white_pawn7 := Piece(6,6,"white","pawn"),
    white_pawn8 := Piece(7,6,"white","pawn"),
    white_rook1 := Piece(0,7,"white","rook"),
    white_rook2 := Piece(7,7,"white","rook"),
    white_knight1 := Piece(1,7,"white","knight"),
    white_knight2 := Piece(6,7,"white","knight"),
    white_bishop1 := Piece(2,7,"white","bishop"),
    white_bishop2 := Piece(5,7,"white","bishop"),
    white_queen := Piece(3,7,"white","queen"),
    white_king := Piece(4,7,"white","king")
]





while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
           


    pressed_mouse_buttons = pygame.mouse.get_pressed()

    for tile in board:
        tile.draw(screen)



    for piece in white_team:
        piece.occupy()
        piece.draw(screen)

    for piece in black_team:
        piece.occupy()
        piece.draw(screen)


    
    if pressed_mouse_buttons[0] == 1 or helper == 1:
            if pressed_mouse_buttons[0] == 1:
                mouse_x_converted= pygame.mouse.get_pos()[0]//60
                mouse_y_converted= pygame.mouse.get_pos()[1]//60
                selected_tile = board[mouse_x_converted+mouse_y_converted*cols]
                selected_piece = selected_tile.piece
            helper = 1
            if selected_tile.occupied: 
                    selected_piece.show_possible_moves()
                    if pressed_mouse_buttons[2] == 1:
                        prev_x = selected_piece.x
                        prev_y = selected_piece.y
                        new_mouse_x_converted = pygame.mouse.get_pos()[0] // 60
                        new_mouse_y_converted = pygame.mouse.get_pos()[1] // 60
                        if (new_mouse_x_converted,new_mouse_y_converted) in selected_piece.moves(): 
                            selected_piece.x = new_mouse_x_converted
                            selected_piece.y = new_mouse_y_converted
                            target_tile = board[selected_piece.x+selected_piece.y*cols]
                            
                            pygame.mixer.music.load("sounds/move-self.mp3")
                            pygame.mixer.music.play()
                            
                            if   target_tile.piece != None and target_tile.piece.color != selected_piece.color:
                                pygame.mixer.music.load("sounds/capture.mp3") 
                                
                                pygame.mixer.music.play()
                                
                                target_tile.piece.captured = True
                            



                        selected_piece.vacate(prev_x,prev_y)
                        if king_in_check(selected_piece.color):
                            pygame.mixer.music.load("sounds/notify.mp3")
                            pygame.mixer.music.play()
   
    
    

       
            

    pygame.display.update()
    clock.tick(60)

