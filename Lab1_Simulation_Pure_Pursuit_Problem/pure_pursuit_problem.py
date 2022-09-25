import numpy as np
import random
import matplotlib.pyplot as plt

from scipy import rand

vf = 20
t = 0
flag = 1
caught_thresh = 100

escapped_thresh = 900

xf = random.randint(0,1000)
yf = random.randint(0,1000)

bomber_x = []
bomber_y = []
figther_x = []
figther_y = []
figther_x.append(xf)
figther_y.append(yf)

while(flag):
    xb = random.randint(0,1000)
    yb = random.randint(0,1000)

    bomber_x.append(xb)
    bomber_y.append(yb)
    
    dist = np.sqrt((xb-xf)**2+(yb-yf)**2)
    print("distance ={}".format(dist))
    if dist < caught_thresh:
        flag = 0
        print("target caught")
        print("Step ={}".format(t))

    elif dist>escapped_thresh:
        flag=0
        print("Escapped")
        print("Step ={}".format(t))

    else:
        sin = (yb-yf)/dist
        cos = (xb-xf)/dist
        
        t = t+1
        xf = xf + vf*cos
        yf = yf + vf*sin
    figther_x.append(xf)
    figther_y.append(yf)
    
plt.plot(figther_x,figther_y,'r*')
plt.plot(bomber_x,bomber_y,'b*')
plt.show()



#print(xb,yb)


