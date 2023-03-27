import turtle
import tkinter as tk


class NRZ_I:

    def __init__(misma, señal: str):
        misma.signal = señal
        misma.alto_logico = 50
        misma.bajo_logico = -50
        misma.distancia = 50

    def dibuja(misma):
        t.sety(misma.alto_logico)
        for i in misma.signal:
            if i == '0':
                misma.zero()
            elif i == '1':
                misma.uno()

    def zero(misma):
        t.forward(misma.distancia)

    def uno(misma):
        posx, posy = t.pos()
        if misma.bajo_logico - 1 < posy < misma.bajo_logico + 1:
            t.sety(misma.alto_logico)
        elif misma.alto_logico - 1 < posy < misma.alto_logico + 1:
            t.sety(misma.bajo_logico)
        t.forward(misma.distancia)
        print(posy)
        
def dibujaejes():
    def dibujalineas(distancia):
        for i in range(distancia // 50):
            t.forward(50)
            t.dot(5)
        t.backward(distancia)

    t.hideturtle()
    t.speed('fastest')
    t.setx(-len_X // 2 + 100)
    dibujalineas(len_X)
    t.rt(90)
    dibujalineas(100)
    t.rt(180)
    dibujalineas(100)
    t.rt(90)


def setTurtle(size, colour, speed, visibility):
    t.pensize(size)
    t.pencolor(colour)
    t.speed(speed)
    if not visibility:
        t.hideturtle()


print('Ingrese señal binaria')
señal = input()

root = tk.Tk()
root.title('Grafico NRZI')
root.geometry('1000x300')
cv = turtle.ScrolledCanvas(root, width=1000) 
cv.pack()

len_X, len_Y = 1000, 350
default_settings = (2, 'red', 'slowest', False)
invisiline = (1, 'black', 'fastest', False)
grafico = NRZ_I(señal)

screen = turtle.TurtleScreen(cv)
screen.screensize(len_X, len_Y)
t = turtle.RawTurtle(screen)

dibujaejes()
setTurtle(*default_settings)
grafico.dibuja()

root.mainloop()