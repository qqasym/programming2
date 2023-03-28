
import pygame
import datetime

pygame.init()
screen = pygame.display.set_mode((800, 600))
done = False
angle = 0

clock = pygame.time.Clock()
image = pygame.image.load('C:/Users/asusg/Downloads/M.png')
image2 = pygame.image.load('C:/Users/asusg/Downloads/left.png')
image1 = pygame.image.load('C:/Users/asusg/Downloads/right.png')
image = pygame.transform.scale( image, (800, 600))
image1 = pygame.transform.scale( image1, (500, 400))
image2 = pygame.transform.scale( image2, (300, 400))
while not done:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True
            
        now = datetime.datetime.now()
        second = int(now.second)
        minute = int(now.minute) 
        
        angle1 = angle - second * 6 
        angle2 = angle - minute * 6

        screen.blit(image, (0, 0))
        rotated_image = pygame.transform.rotate(image1, angle1)
        rotated_image1 = pygame.transform.rotate(image2, angle2)
        new_rect = rotated_image.get_rect(center = image.get_rect().center)
        new_rect1 = rotated_image1.get_rect(center = image.get_rect().center)
        screen.blit(rotated_image, new_rect)
        screen.blit(rotated_image1, new_rect1)
        pygame.display.flip()
        clock.tick(60)