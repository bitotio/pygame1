import pygame
pygame.init()
import random



screen = pygame.display.set_mode ( (640, 480))
screen.fill((255, 255,255))
for _ in range (10) :
    x = random.randint(0, 640)
    y = random.randint(0, 480)
    radius = random.randint (10, 100)
    color = (random.randint(0, 255), random.randint(0, 255),random. randint(0, 255))
    pygame.draw.circle(screen, color, (x, y), radius)

pygame.display.flip()
running = True
while running:
    for event in pygame. event.get() :
        if event. type == pygame.QUIT:
            running = False
pygame.quit()