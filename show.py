import pygame
import random
import sort_algo

pygame.init()

width, high, x, y, rect_high, length, p = 800, 500, 5, 5, 10, 53, 0
win = pygame.display.set_mode((width, high))
pygame.display.set_caption("SORT VISUALIZER")
val = []

for i in range(0, length):
    val.append(random.randint(0, high - 10))

print("what sorting technique you wanna run \n1. selection \n2. bubble")
choice = int(input())

running = True
while running:
    pygame.time.delay(200)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    win.fill((0, 0, 0))

    if choice == 1:
        val = sort_algo.selection(val, p)
    else:
        val = sort_algo.bubble(val, p)

    for j in val:
        pygame.draw.rect(win, (255, 255, 255), (x, y, rect_high, j))
        pygame.display.update()
        x = x + 15

    p = p+1
    if p == len(val)-1:
        p = 0

    x = 5




