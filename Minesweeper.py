import pygame
import random


def save_file(file_name,grid,grid_size):
    infile=open(f"{file_name}.txt","w")
    
    for i in range(grid_size):
        for j in range(grid_size):
            infile.write(f"{grid[i][j]}\n")
    infile.close()

def get_file(file_name,grid,grid_size):
    result = False
    try:
        infile=open(f"{file_name}.txt","r")
        content=infile.readlines()
        count=0
        for line in content:
            grid[count//grid_size][count%grid_size]=int(line)
            #print (f"{count//grid_size},{count%grid_size}={int(line)}")
            count+=1
        result = True
    except:
        print("File not found") 
    
    return result


### Initiate mines locations 
def get_mines(grid,grid_size,mines_num):
    for i in range (mines_num):
       x=random.randint(0,grid_size-1)
       y=random.randint(0,grid_size-1)
         # print(x,y) 
       grid[x][y]=9


### Get Count of mines
def count_mines(i,j,grid,grid_size):
    count=0
    for x in range(i-1,i+2):
        for y in range(j-1,j+2):
            if x>=0 and y>=0 and  (x,y)!=(i,j)and x<grid_size and y<grid_size:
               
                if grid[x][y]==9:

                   count+=1
    return count

### Set number indicators
def set_count(grid,grid_size):
     for x in range(0,grid_size):
        for y in range(0,grid_size):
            if grid[x][y]!=9:
                count=count_mines(x,y,grid,grid_size)
                grid[x][y]=count
   

### Constants
WIDTH, HEIGHT = 600, 600
GRID_SIZE = 9  # 9x9 grid
CELL_SIZE = WIDTH // GRID_SIZE
MINE_NUM = 7
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (128, 128, 128)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN= (0,255, 0)
### Game preparing.....
#######################

grid=[[0 for i in range(GRID_SIZE) ]for j in range (GRID_SIZE) ] 

found = False
file_name=input("enter your name: ")

response_mode=False
welcome_mode=True
newGame = True
found = get_file(file_name,grid,GRID_SIZE)
if found :
    quis=input("do you want continue the old game (y/n) ? ")
    if quis=="y":
        newGame=False
    

if newGame:
    get_mines(grid,GRID_SIZE,MINE_NUM)
    set_count(grid,GRID_SIZE)

#print(grid)
#quit()

# Pygame init...
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Minesweeper")

# Game loop
running = True

game_over = False

response_text=""
def show_prompt():
    
    font = pygame.font.Font(None, 36)
    text = font.render("Save (S), Exit (E), Continue (C): " + response_text, True, BLACK)
    rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    screen.fill(WHITE)
    screen.blit(text, rect)
    pygame.display.flip()

def Welcome_prompt():
    
    font = pygame.font.Font(None, 36)
    text = font.render(f"Welcome {file_name} , please press any key to start" + response_text, True, BLUE)
    rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    screen.fill(WHITE)
    screen.blit(text, rect)
    pygame.display.flip()

while running:
    
    if response_mode:
        show_prompt()

    if welcome_mode:
        Welcome_prompt()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            if not game_over:
                response_mode = True
            else:
                running = False
        
        if event.type == pygame.KEYDOWN:
            if response_mode:
                if event.key == pygame.K_RETURN:  # Submit response
                    response_mode = False
                    if response_text.upper() == "S":
                        save_file(file_name, grid, GRID_SIZE)
                        running = False
                    elif response_text.upper() == "E":
                        running = False
                    elif response_text.upper() == "C":
                        pass
                    response_text = ""
                elif event.key == pygame.K_BACKSPACE:  # Edit response
                    response_text = response_text[:-1]
                else:  # Append character
                    response_text += event.unicode
            elif welcome_mode:
                welcome_mode =False
            elif event.key == pygame.K_ESCAPE:
                response_mode = True
    
        
        if event.type == pygame.MOUSEBUTTONDOWN and not game_over and not response_mode and not welcome_mode:
            x, y = pygame.mouse.get_pos()
            #print (x,y)
            grid_x = x // CELL_SIZE
            grid_y = y // CELL_SIZE
            #print(grid_x,grid_y)
            if event.button == 1: #Left Click
                #print(f"grid valu:{grid[grid_x][grid_y]}")
                if grid[grid_x][grid_y]<10 and grid[grid_x][grid_y]!=9:
                    grid[grid_x][grid_y]+=10
                #revealed[grid_x][grid_y] = True
                if grid[grid_x][grid_y] == 9:
                    game_over = True
                    
            elif event.button == 3: #Right Click (flag)
                if grid[grid_x][grid_y]<10 :
                    grid[grid_x][grid_y]+=20
                elif grid[grid_x][grid_y]>=20:
                    grid[grid_x][grid_y]-=20
            
    win=True
    for x in range(GRID_SIZE):
        for y in range(GRID_SIZE):
            if grid[x][y]<9:
                win=False
    if win:
        game_over=True


    if not  response_mode and not welcome_mode: 
        screen.fill(WHITE)


        for x in range(GRID_SIZE):
            for y in range(GRID_SIZE):
                rect = pygame.Rect(x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE)
                pygame.draw.rect(screen, GRAY, rect, 3)  # Cell border
                #if revealed[x][y] or game_over:
                if grid[x][y]>=10 or game_over:
                    if grid[x][y] == 9:
                        pygame.draw.circle(screen, BLUE, rect.center, CELL_SIZE // 3) #Mine
                    elif grid[x][y] >= 20:
                        pygame.draw.circle(screen, RED, rect.center, CELL_SIZE // 3,5) #Mine
                    elif grid[x][y] > 10 or (game_over and  grid[x][y]>0 and grid[x][y]<10):
                        font = pygame.font.Font(None, 36)
                        num = grid[x][y]
                        if num>=10:
                            num= num-10
                        text = font.render(str(num), True, BLACK)
                        if num==2:
                            text = font.render(str(num), True, BLUE)
                        elif num==3:
                            text = font.render(str(num), True, GREEN)
                        elif num==4: 
                            text = font.render(str(num), True, RED)                           
                        text_rect = text.get_rect(center=rect.center)
                        screen.blit(text, text_rect)
                    else:
                        pygame.draw.rect(screen, GRAY, rect)    
        
        #HHHJHKJHK
        if game_over:
            font = pygame.font.Font(None, 90)
            text = font.render( "GAME OVER ", True,RED )
            if win:
                text = font.render( "YOU WIN!", True,RED )
            text_rect = text.get_rect(center=(300,300))
            screen.blit(text, text_rect)

        pygame.display.flip()

pygame.quit()