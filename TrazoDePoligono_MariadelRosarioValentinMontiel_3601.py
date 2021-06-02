print("TRAZO DE POLIGONOS")
from turtle import *
from subprocess import *
import subprocess 

def DDA():

    def OKI(n):
        try:
            n=int(n)
        except:
            n=OKI(input("Caracter no valido: "))
        return n
    def OK(n):
        try:
            n=float(n)
        except:
            n=OK(input("Caracter no valido: "))
        return n
    def ns(c):
        while c!=("s") and c!=("n"):
            print(chr(7));c=input("Escribe solo \'n\' o \'s\' según su opción: ")
        return(c)
    def set_color(cf):
        try:
            t.screen.bgcolor(cf)
        except:
            cf=set_color(input("Color no valido: "))
        return cf
    def set_color2(ct):
        try:
            t.color(ct)
        except:
            ct=set_color2(input("Color no valido: "))
        return ct 
    preg=ns(input("¿Desea graficar?: "))
    if preg==("s"):
        subprocess.call(["cmd.exe","/C","cls"])
        t=Turtle()
        t.hideturtle()
        while True:
            print("DIBUJANDO POLIGONOS")
            cf=set_color(input("Indica el color del fondo: "))
            ct=set_color2(input("Indica el color del contorno: "))
            while ct==cf:
                ct=set_color2(input("Especifica un color diferente para el contorno: "))
                coordenada_x=5
                coordenada_y=20
                t.color(cf)
                t.setx(coordenada_x)
                t.sety(coordenada_y)
                t.color(ct) 
            gt=OK(input("Indica el grosor de la línea: "))
            t.pensize(gt)
            n=OKI(input("Indica el número de lados del polígono: "))
            ln=OK(input("Indica la longitud del lado: "))
            ang=180-(((n-2)/n)*180)
            for i in range(n):
                t.left(ang)
                t.fd(ln)
            conti=ns(input("¿Dibujar nuevo poligono?: "))
            if conti==("s"):
                t.clear()
                subprocess.call(["cmd.exe","/C","cls"])
            else:
                break
def Bresenham():

    def OKI(n):
        try:
            n=int(n)
        except:
            n=OKI(input("Caracter no valido: "))
        return n
    def OK(n):
        try:
            n=float(n)
        except:
            n=OK(input("Caracter no valido: "))
        return n
    def ns(c):
        while c!=("s") and c!=("n"):
            print(chr(7));c=input("Escribe solo \'n\' o \'s\' según su opción: ")
        return(c)
    def set_color(cf):
        try:
            t.screen.bgcolor(cf)
        except:
            cf=set_color(input("Color no valido: "))
        return cf
    def set_color2(ct):
        try:
            t.color(ct)
        except:
            ct=set_color2(input("Color no valido: "))
        return ct 
    preg=ns(input("¿Desea graficar?: "))
    if preg==("s"):
        subprocess.call(["cmd.exe","/C","cls"])
        t=Turtle()
        t.hideturtle()
        while True:
            print("DIBUJANDO POLIGONOS")
            cf=set_color(input("Indica el color del fondo: "))
            ct=set_color2(input("Indica el color del contorno: "))
            while ct==cf:
                ct=set_color2(input("Especifica un color diferente para el contorno: "))
                coordenada_x=0
                coordenada_y=0
                t.color(cf)
                t.setx(coordenada_x)
                t.sety(coordenada_y)
                t.color(ct) 
            gt=OK(input("Indica el grosor de la línea: "))
            t.pensize(gt)
            n=OKI(input("Indica el número de lados del polígono: "))
            ln=OK(input("Indica la longitud del lado: "))
            ang=180-(((n-2)/n)*180)
            for i in range(n):
                t.left(ang)
                t.fd(ln)
            conti=ns(input("¿Dibujar nuevo poligono?: "))
            if conti==("s"):
                t.clear()
                subprocess.call(["cmd.exe","/C","cls"])
            else:
                break
if __name__ == '__main__':
    print("""
    1) Algoritmo DDA
    2) Algoritmo Bresenham
    """)
    Opcion=input("selecciona la opcion: ")
    if Opcion == "1":
        DDA()
    else:
        Bresenham()
       