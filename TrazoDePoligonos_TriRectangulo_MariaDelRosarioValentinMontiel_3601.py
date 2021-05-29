import matplotlib.pyplot as plt

def TrianguloRecDDA():
    x1=4
    y1=5
    x2=14
    y2=5
    color="r."
    dx = x2-x1
    dy = y2-y1
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
        plt.plot(x,y,color)

    x3=14
    y3=10
    x2=14
    y2=5
    dx = x3-x2
    dy = y3-y2
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

    x1=4
    y1=5
    x3=14
    y3=10
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


def TrianguloRecBresenham():

    x1=4
    y1=5
    x2=14
    y2=5
    color="r."
    dx = x2-x1
    dy = y2-y1
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
        plt.plot(x,y,color)

    x3=14
    y3=10
    x2=14
    y2=5
    dx = x3-x2
    dy = y3-y2
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

    x1=4
    y1=5
    x3=14
    y3=10
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

if __name__ == '__main__':
    print("""
    1) Algoritmo DDA
    2) Algoritmo Bresenham
    """)
    opcion=input ("selecciona la opcion: ")

    if opcion == "1":
        TrianguloRecDDA()
    else:
        TrianguloRecBresenham()
