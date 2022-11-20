import numpy as np
import pygame
# define range (X,Y) cordinates and N number of points
X = 900
Y = 900
N = 100
escappedThreshold = 900

caughtThreshold = 100
t = N

# take bomber coordinates, predefined path coordinates from (0 to X,0 to Y)
xb = np.random.randint(0,X,size=N)
yb = np.random.randint(0,Y,size=N)

# take initial position for fighter and initial velocity
xf = []
yf = []
xf.append(300)
yf.append(100)
vf = 50

# calculate fighter coordinates and find escape or caught situation
isCaught = False

for i in range(0,N):
    dist = np.sqrt((yf[i]-yb[i])**2+(xf[i]-xb[i])**2)
    
    if(dist<=caughtThreshold):
        isCaught = True
        t=i
        break
    
    elif dist>=escappedThreshold:
        t=i
        break
    
    sin = (yb[i]-yf[i])/dist
    cos = (xb[i]-xf[i])/dist
    xf.append(xf[i] + vf*cos)
    yf.append(yf[i] + vf*sin)
    


# using pygame for visualization
pygame.init()
pygame.display.set_caption("Pure Pursuit Problem Visualization")
screenSize = (1400,1000)
screen = pygame.display.set_mode(screenSize)

f = pygame.font.get_fonts()[0]
font = pygame.font.SysFont(f,32)
positionText1 = font.render("Boomber Caught",True,(255,255,255),(0,0,0))
positionText2 = font.render("Boomber Escapped",True,(255,255,255),(0,0,0))
textRect1 = positionText1.get_rect()
textRect2 = positionText2.get_rect()
textPosition = (X/2,Y/2)
textRect1.center = textPosition
textRect2.center = textPosition

running = True;
while running:
    screen.fill((150,0,0))
    pygame.time.delay(50)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            for i in range(0,t):
                pygame.draw.line(screen,(55,100,30), (xf[i],yf[i]), (xf[i+1],yf[i+1]), 4)
                pygame.draw.circle(screen, (55,100,30),(xf[i+1],yf[i+1]), 4)
                
                pygame.draw.line(screen,(155,100,200), (xb[i],yb[i]), (xb[i+1],yb[i+1]), 4)
                pygame.draw.circle(screen,(155,100,200),(xb[i+1],yb[i+1]), 4)
                
                pygame.time.delay(500)
                pygame.display.update()
if isCaught:
    screen.blit(positionText1,textRect1)
    pygame.draw.line(screen,(255,0,0), (xb[t],yb[t]), (xf[t],yf[t]), 4)
else:
    screen.blit(positionText2,textRect2)
pygame.display.update()
    
pygame.time.delay(5000)
pygame.quit()