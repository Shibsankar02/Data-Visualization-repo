import pygame
import sys

pygame.init()
width,height=600,400
screen=pygame.display.set_mode((width,height))
pygame.display.set_caption("Animated Circle")

white=(255,255,255)
blue=(0,0,255)

x,y=width//2, height//2
radius=20
speed=5

clock=pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type==pygame.quit:
            pygame.quit()
            sys.exit()
            
    keys=pygame.key.get_pressed()
    
    if keys[pygame.K_LEFT]:
        x-=speed
    if keys[pygame.K_RIGHT]:
        x+=speed
    if keys[pygame.K_UP]:
        y-=speed
    if keys[pygame.K_DOWN]:
        y+=speed
        
    x=max(radius,min(width-radius,x))
    y=max(radius,min(height-radius,y))
    
    screen.fill(white)
    pygame.draw.circle(screen,blue,(x,y),radius)
    
    pygame.display.update()
    clock.tick(60)