import pygame
import random
import selection_sort

pygame.init()

width, high, x, y, rect_high, length, p = 800, 500, 5, 5, 10, 53, 0
win = pygame.display.set_mode((width, high))
pygame.display.set_caption("SELECTION SORT")
val = []

for i in range(0, length):
    val.append(random.randint(0, high - 10))\


running = True
while running:
    pygame.time.delay(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    win.fill((0, 0, 0))
    val = selection_sort.selection(val, p)
    for j in val:
        pygame.draw.rect(win, (255, 255, 255), (x, y, rect_high, j))
        pygame.display.update()
        x = x + 15
    
	p = p + 1
    if p == length - 1:
        p = 0
    
	x = 5



