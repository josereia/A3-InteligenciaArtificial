import sys
import pygame
pygame.init()


size = width, height = 1366, 720
screenColor = 0, 0, 0

screen = pygame.display.set_mode(size)

image = pygame.image.load("assets/card_top.png").convert_alpha()
w, h = image.get_size()
img = pygame.transform.smoothscale(image, (int(w*0.5), int(h*0.5)))

screen.fill(screenColor)
screen.blit(img, (0, 0))
pygame.display.flip()

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
