import pygame
import time
import random
pygame.init()

window_sit = (800, 600)
screen = pygame.display.set_mode(window_sit)
pygame.display.set_caption("Snake Game")

image = pygame.image.load("boat.png")
image_rect = image.get_rect()
image2 = pygame.image.load("boat.png")
image_rect2 = image2.get_rect()
run = True
speed = 5

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEMOTION:
            mouseX, mouseY = event.pos
            image_rect.x = mouseX - 20
            image_rect.y = mouseY - 20
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        if image_rect.x  > 0:
            image_rect.x -= speed
        else:
            image_rect.x = window_sit[0] - image_rect.width
    if keys[pygame.K_RIGHT]:
        if image_rect.x + image_rect.width < window_sit[0]:
            image_rect.x += speed
        else:
            image_rect.x = 0
    if keys[pygame.K_UP]:
        if image_rect.y > 0:
            image_rect.y -= speed
        else:
            image_rect.y = window_sit[1] - image_rect.height

    if keys[pygame.K_DOWN]:
        if image_rect.y + image_rect.height < window_sit[1]:
            image_rect.y += speed
        else:
            image_rect.y = 0
    if image_rect.colliderect(image_rect2):
        image_rect2.x = random.randint(0, window_sit[0] - image_rect2.width)
        image_rect2.y = random.randint(0, window_sit[1] - image_rect2.height)
    screen.fill((25, 0, 0))
    screen.blit(image, image_rect)
    screen.blit(image2, image_rect2)
    pygame.display.update()
    time.sleep(0.01)
pygame.quit()