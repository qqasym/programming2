import pygame
import random
import time

pygame.font.init()
fps = 2
block = 20
fon = (0, 255, 204)
white = (255,255,255)
blue = (204,255,255)
header_color = (0,204,153)
red = (255,47,47)
snakec = (107,178,0)
count_blocks = 20
header_margin = 70
margin = 1
size = [block*count_blocks + 2 * block + margin * count_blocks,
        block * count_blocks + 2 * block + margin * count_blocks + header_margin]

game_over = False

font = pygame.font.SysFont("Merriweather-Black", 70)  # big font
font_small = pygame.font.SysFont("Merriweather-Black", 25)  # small font

score = 0
level = 0
timer = pygame.time.Clock()
screen = pygame.display.set_mode(size)


pygame.display.set_caption("MY SNAKE GAME")
 

class SnakeBlock:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def is_inside(self):
        return 0 <= self.x < block and 0 <= self.y < block
    def __eq__(self, other):
        return isinstance(other, SnakeBlock) and self.x == other.x and self.y == other.y
def random_block():

    x = random.randint(0, count_blocks-1)
    y = random.randint(0, count_blocks - 1)
    empty_block = SnakeBlock(x,y)

    while empty_block in snake_blocks:
        empty_block.x = random.randint(0, count_blocks-1)
        empty_block.y = random.randint(0, count_blocks-1)
        
    return empty_block

def draw_block(color, column, row):

    pygame.draw.rect(screen, color, [block + column * block + margin * (column+1),
                        header_margin+block + row * block + margin * (row+1), block, block])
    
def over_the_game(): # game over screen
    global game_over
    screen.fill((69, 172, 116))
    screen.blit(font.render('GAME OVER', True, white), (30, 170))
    screen.blit(font_small.render(f'Score: {score}', True, white), (32, 250))
    screen.blit(font_small.render(f'Level: {level}', True, white), (32, 275))
    pygame.display.update()
    time.sleep(5)
    game_over = True

    

snake_blocks = [ SnakeBlock(9,9), SnakeBlock(9,10)]
apple = random_block()
dr = br = 0
dc = bc = 1
run = True
while run:
    

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and dc != 0:
                br = -1
                bc = 0
            elif event.key == pygame.K_DOWN and dc != 0:
                br = 1
                bc = 0
            elif event.key == pygame.K_LEFT and dr!= 0:
                br = 0
                bc = -1
            elif event.key == pygame.K_RIGHT and dr != 0:
                br = 0
                bc = 1

    pygame.display.update()
            
    screen.fill(fon)
    pygame.draw.rect(screen, header_color, [0,0, size[0], header_margin] )

    screen.blit(font_small.render(f'Score: {score}', True, white), (block,block))
    screen.blit(font_small.render(f'Level: {level}', True, white), (block+230, block))

    for row in range(count_blocks):

        for column in range(count_blocks):

            if (row + column) %2 == 0:
                color = blue
            else:
                color = white
            draw_block(color,column,row)
    head = snake_blocks[-1]
    if not head.is_inside():
        over_the_game()
    
    draw_block(red, apple.x, apple.y)
    for blockk in snake_blocks:
        
        draw_block(snakec, blockk.x, blockk.y)
    
    pygame.display.flip()


    if head == apple:
        score+=1
        snake_blocks.append(apple)
        apple = random_block()
    if len(snake_blocks) % 4 == 0 and len(snake_blocks) != 0:
        level += 1
        fps += 2
    
    dr = br
    dc = bc

    new_head = SnakeBlock(head.x +  dr, head.y + dc)
    snake_blocks.append(new_head)
    snake_blocks.pop(0)
             

    timer.tick(fps)