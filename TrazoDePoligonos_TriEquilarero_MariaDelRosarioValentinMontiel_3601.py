#MARIA DEL ROSARIO VALENTIN MONTIEL
import matplotlib.pyplot as plt

def TrianguloEquiDDA():
    x1=3
    y1=4
    x2=8
    y2=9
    dx = x2-x1
    dy = y2-y1
    color="r."

    if dx !=0 :
        m = dy / dx
    else:
        print("Operacion no hecha")
    if(dx > dy):
        steps = dx
    else:
        steps = dy
    xinc = dx / steps
    yinc = dy / steps

    plt.plot(x1,y1,color)
    i=1

    while(i<=steps):
        x1 = x1 + xinc
        y1 = y1 + yinc
        x=round(x1)
        y=round(y1)
        i+=1
        print(x,y)
        plt.plot(x,y,color)

    x1=3
    y1=4
    x3=13
    y3=4
    dx = x3-x1
    dy = y3-y1
    if dx !=0 :
        m = dy / dx
    else:
        print("Operacion no hecha")
    if(dx > dy):
        steps = dx
    else:
        steps = dy
    xinc = dx / steps
    yinc = dy / steps

    if yinc !=0 :
         print("Operacion hecha")
    else:
        print("Operacion no hecha")
    plt.plot(x1,y1,color)
    i=1
    while(i<=steps):
        x1 = x1 + xinc
        y1 = y1 + yinc
        x=round(x1)
        y=round(y1)
        i+=1
        plt.plot(x,y,color)
    x3=13
    y3=4
    x2=8
    y2=9
    dx = x2-x3
    dy = y2-y3
    if dx !=0 :
        m = dy / dx
    else:
        print("Operacion no hecha")
    if(dx > dy):
        steps = dx
    else:
        steps = dy
    xinc = dx / steps
    yinc = dy / steps
    
    if xinc !=0 :
         print("Operacion hecha")
    else:
        print("Operacion no hecha")
    if yinc !=0 :
         print("Operacion hecha")
    else:
        print("Operacion no hecha")
    plt.plot(x1,y1,color)
    i=1
    while(i<=steps):
        x1 = x1 + xinc
        y1 = y1 + yinc 
        x=round(x1)
        y=round(y1)
        i+=1
        plt.plot(x,y,color)
    plt.show()
def TrianguloEquiBresenhams():
    x1 = 3
    y1 = 4
    x2 = 8
    y2 = 9
    dx = x2-x1
    dy = y2-y1
    p = 2*dy - dx
    color="r."
    plt.plot(x1,y1,color)
    
    while(x1<x2):
        plt.plot(x1,y1,color)
        x1=x1+1
        if p<0:
            p=p+2*dy
        else:
            p=p + (2*dy)-(2*dx)
            y1=y1+1

    x1 = 3
    y1 = 4
    x2 = 13
    y2 = 4
    dx = x2-x1
    dy = y2-y1
    p = 2*dy - dx
    plt.plot(x1,y1,color)
    while(x1<x2):
        plt.plot(x1,y1,color)
        x1=x1+1
        if p<0:
            p=p+2*dy
        else:
            p=p + (2*dy)-(2*dx)
            y1=y1+1

    x1=8
    y1=9
    x2=13
    y2=4
    dx = x2-x1
    dy = y2-y1
    p = 2*dy - dx
    plt.plot(x2,y2,color)
    while(x1<x2):
        plt.plot(x1,y1,color)
        x1=x1+1
        if dy<0:
            if p<0:
                p=p+2*dy
                y1=y1-1
            else:
                p=p + (2*dy)-(2*dx)
        else:
            if p<0:
                p=p+2*dy
            else:
                p = p + (2*dy)-(2*dx)
                y1=y1+1
    plt.show()
    
if __name__ == '__main__':
    print("""
    1) Algoritmo DDA
    2) Algoritmo Bresenham
    """)
    opcion=input ("selecciona la opcion: ")

    if opcion == "1":
        TrianguloEquiDDA()
    else:
        TrianguloEquiBresenhams()
