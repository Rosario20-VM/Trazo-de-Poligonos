#MARIA DEL ROSARIO VALENTIN MONTIEL
import matplotlib.pyplot as plt

def RectanguloDDA():
    x1=2
    y1=6
    x2=10
    y2=6
    x3=2
    y3=10
    x4=2
    y4=6
    dx= abs(x2-x1)
    dy= abs(y2-y1)
    steps=0
    color='r.'

    if (dx)> (dy):
        steps=(dx)
    else:
        steps=(dy)
    xInc = float(dx / steps)
    yInc = float(dy / steps)

    xInc = round(xInc,1)
    yInc = round(yInc,1)

    dx1= abs(x3-x1)
    dy1= abs(y3-y1)
    steps1=0
    color='r.'

    if (dx1)> (dy1):
        steps1=(dx1)
    else:
        steps1=(dy1)
    xInc1 = float(dx1/ steps1)
    yInc1 = float(dy1 / steps1)

    xInc1 = round(xInc1,1)
    yInc1 = round(yInc1,1)

    for i in range(0, int(steps + 1)):
        plt.plot(round(x1),round(y1),color)
        plt.plot(round(x3),round(y3),color)
        x1+=xInc
        y1+=yInc
        x3+=xInc
        y3+=yInc

    for i in range(0, int(steps1 +1)):
        plt.plot(round(x1),round(y1),color)
        plt.plot(round(x4),round(y4),color)
        x4+=xInc1
        y4+=yInc1
        x1+=xInc1
        y1+=yInc1
            
    plt.show()


def RectanguloBresenham():
    color='r.'
    x1=2
    y1=6
    x2=10
    y2=6
    x3=2
    y3=10
    x4=10
    y4=10
    
    dx= abs(x2-x1)
    dy= abs(y2-y1)
    p = 2*dy - dx
    x=x1
    y=y1

    dx1= abs(x4-x3)
    dy1= abs(y4-y3)
    p1 = 2*dy1 - dx1
    xa=x3
    ya=y3

    dx2= abs(x3-x1)
    dy2= abs(y3-y1)
    p2= 2*dy2 - dx2 
    xb=x1
    yb=y1


    dx3= abs(x4-x2)
    dy3= abs(y4-y2)
    p3= 2*dy3 - dx3
    xc=x2
    yc=y2

    for i in range(x, x2):
        plt.plot(round(x),round(y), color)
        if p < 0:
            x= x + 1
            p = p + 2* dy
        else:
            p = p + (2*dy) - (2*dx)
            y=y+1

    for i in range(xa, x4):
        plt.plot(round(xa),round(ya), color)
        if p1 < 0:
            xa= xa+ 1
            p1 = p1 + 2* dy1
        else:
            p1 = p1 + (2*dy1) - (2*dx1)
            ya=ya+1
    
    for i in range(yb, y3):
        plt.plot(round(xb),round(yb), color)
        if p2 < 0:
            xb= xb + 1
            p2 = p2 + 2* dy2
        else:
            p2 = p2 + (2*dy2) - (2*dx2)
            yb = yb+1

    for i in range(yc, y4+1):
        plt.plot(round(xc),round(yc), color)
        if p3 < 0:
            xc= xc + 1
            p3 = p3 + 2* dy3
        else:
            p3 = p3 + (2*dy3) - (2*dx3)
            yc = yc+1
       

    plt.show()

if __name__ == '__main__':

    print("""
    1) Algoritmo DDA
    2) Algoritmo Bresenham
    """)
    opcion=input ("selecciona la opcion: ")

    if opcion == "1":
        RectanguloDDA()
    else:
        RectanguloBresenham()
