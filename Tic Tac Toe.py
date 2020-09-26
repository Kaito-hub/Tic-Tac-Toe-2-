import pygame

pygame.init()

screen_size = 500
screen = pygame.display.set_mode((500,600))
white = (255,255,255)
screen.fill(white)

pygame.display.set_caption("Tic Tac Toe")

black = (0,0,0)
width = screen_size // 3

font = pygame.font.Font('freesansbold.ttf', width)
win_font = pygame.font.Font('freesansbold.ttf', 100)


class Spot:
    def __init__(self,row,col):
        self.row = row
        self.col = col
        self.x = row*width
        self.y = col*width
        self.x_t = False
        self.o_t = False

    def X_T(self):
        self.x_t = True

    def O_T(self):
        self.o_t = True

    def draw_x(self):
        text = font.render("X",True,black,white)
        textRect = text.get_rect()
        textRect.center = (self.x + 80,self.y + 85)
        screen.blit(text,textRect)

    def draw_o(self):
        text = font.render("O",True,black,white)
        textRect = text.get_rect()
        textRect.center = (self.x + 80,self.y + 85)
        screen.blit(text,textRect)

def make_grid():
    grid = []
    for i in range(3):
        grid.append([])
        for j in range(3):
            spot = Spot(i,j)
            grid[i].append(spot)

    return grid

def draw_grid():
    for i in range(4):
        pygame.draw.line(screen,black,(i*width,0),(i*width,screen_size))
        for j in range(3):
            pygame.draw.line(screen,black,(0,i*width),(screen_size,i*width))

def clicked_pos(pos):
    x,y = pos
    row = x // width
    col = y // width

    return row,col

def O_WON():
    text = win_font.render("O WON",True,black,white)
    textRect = text.get_rect()
    textRect.center = (250,550)
    screen.blit(text,textRect)

def X_WON():
    text = win_font.render("X WON",True,black,white)
    textRect = text.get_rect()
    textRect.center = (250,550)
    screen.blit(text,textRect)

def DRAW():
    text = win_font.render("DRAW",True,black,white)
    textRect = text.get_rect()
    textRect.center = (250,550)
    screen.blit(text,textRect)
    

grid = make_grid()
count = 2
O = False
X = False

running = True
while running:
    draw_grid()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        try:
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row,col = clicked_pos(pos)
                spot = grid[row][col]

                if count%2 == 0 and not spot.o_t and not spot.x_t:
                    X = spot
                    X.draw_x()
                    spot.X_T()
                    count += 1

                    
                elif count%2 == 1 and not spot.x_t and not spot.o_t:
                    O = spot
                    O.draw_o()
                    spot.O_T()
                    count += 1

                for i in range(3):
                    if grid[0][i].x_t and grid[1][i].x_t and grid[2][i].x_t:
                        X_WON()
                    elif grid[i][0].x_t and grid[i][1].x_t and grid[i][2].x_t:
                        X_WON()
                if grid[0][0].x_t and grid[1][1].x_t and grid[2][2].x_t:
                    X_WON()
                elif grid[2][0].x_t and grid[1][1].x_t and grid[0][2].x_t:
                    X_WON()
                elif count == 11:
                    DRAW()
                    break

                for i in range(3):
                    if grid[0][i].o_t and grid[1][i].o_t and grid[2][i].o_t:
                        O_WON()
                    elif grid[i][0].o_t and grid[i][1].o_t and grid[i][2].o_t:
                        O_WON()
                if grid[0][0].o_t and grid[1][1].o_t and grid[2][2].o_t:
                    O_WON()
                elif grid[2][0].o_t and grid[1][1].o_t and grid[0][2].o_t:
                    O_WON()
                elif count == 11:
                    DRAW()
                    break

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    grid = make_grid()
                    screen.fill(white)
                    draw_grid()
                    count = 2
                    
        except IndexError:
            print("You are clicking out of place")

    pygame.display.update()

pygame.quit()
