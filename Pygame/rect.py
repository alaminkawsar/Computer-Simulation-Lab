import pygame  
  
pygame.init()  
screen = pygame.display.set_mode((400, 300))  
done = True
  
while done:  
    for event in pygame.event.get():  
        if event.type == pygame.QUIT:  
            done = False 
    pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(30, 30, 60, 60))    
    pygame.display.update()
    
pygame.quit()