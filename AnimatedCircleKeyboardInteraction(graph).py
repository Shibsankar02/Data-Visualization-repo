import pygame

pygame.init()

width,height=600,400
screen=pygame.display.set_mode((width,height))
pygame.display.set_caption("Animated Circle")

x,y=width//2,height//2
radius=20
speed=5

running=True
while running:
    pygame.time.delay(30)
    
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
            
    keys=pygame.key.get_pressed()
    
    if keys[pygame.K_LEFT]:
        x-=speed
    if keys[pygame.K_RIGHT]:
        x+=speed
    if keys[pygame.K_UP]:
        y-=speed
    if keys[pygame.K_DOWN]:
        y+=speed
    
    screen.fill((0,0,0))
    
    pygame.draw.circle(screen,(0,255,0),(x,y),radius)
    
    pygame.display.update()
    
pygame.quit()