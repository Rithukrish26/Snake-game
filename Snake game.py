import pygame
import random

pygame.init()

screen_width = 800
screen_height = 600

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Pygame Basics")

background_color = (0,0,0)
snakecolour = (3,244,120)
block = 10
snake = [(100,100)]
speed = 10
time = pygame.time.Clock()
direction = (speed,0)
score = 0
food = (random.randint(0, screen_width // block - 10) * block,
        random.randint(0, screen_height // block - 10) * block)

running = True
while running:
   for event in pygame.event.get():
       if event.type == pygame.QUIT:
           running = False
       elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                direction = (block,0)
            if event.key == pygame.K_LEFT:
                direction = (-block,0)
            if event.key == pygame.K_DOWN:
                direction = (0,block)
            if event.key == pygame.K_UP:
                direction = (0,-block)
   newpos = (snake[0][0] + direction[0], snake[0][1] + direction[1])
   screen.fill(background_color)
   if newpos[0]<0 or newpos[0]>=screen_width or newpos[1]<0 or newpos[1]>=screen_height:
       running = False
   if newpos == food:
       food = (random.randint(0, screen_width // block - 1) * block,
               random.randint(0, screen_height // block - 1) * block)
       score += 1
       print ("Score:",score)
   else:
       snake.pop()
   snake.insert(0,newpos)
   for a in snake:
       pygame.draw.rect(screen, snakecolour, (a[0], a[1], block, block))
   pygame.draw.rect(screen, "White", (food[0],food[1],block,block), 8)
   pygame.display.flip()
   time.tick(10)