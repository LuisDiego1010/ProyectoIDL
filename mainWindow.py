from tkinter import *
import tkinter as tk
from tkinter import messagebox
import turtle


#******************Ventana Principal**********************
mainwindow = tk.Tk()
mainwindow.title('Menu principal: Codigo Hamming')
canvas_principal = tk.Canvas(mainwindow, width=850, height=500)
file=PhotoImage(file="resources//main.png",master=mainwindow)
canvas_principal.create_image(0,0,anchor=NW,image=file)
canvas_principal.pack()

#******************Creacion de ventanas(Inicio)************************
def openNewWindow_Hamming_Code():
    newWindow = tk.Toplevel(mainwindow)
    newWindow.title('Codigo Hamming')
    canvas_principal1 = tk.Canvas(newWindow, width=850, height=500)
    bg1=PhotoImage(file="resources//Hamming Code.png",master=newWindow)
    label2 = Label( canvas_principal1, image = bg1)
    label2.image = bg1
    label2.place(x = 0, y = 0)
    canvas_principal1.pack()

def openNewWindow_Conversion():
    newWindow2 = tk.Toplevel(mainwindow)
    newWindow2.title('Conversion')
    canvas_principal2 = tk.Canvas(newWindow2, width=850, height=500)
    #Cargar y colocar el fondo
    bg2 = PhotoImage(file = "resources//Conversion.png", master=newWindow2)
    label2 = Label( canvas_principal2, image = bg2)
    label2.image = bg2
    label2.place(x = 0, y = 0)
    #Solcitar al usuario el número en hexadecimal
    lbl_hex1 = tk.Label (canvas_principal2,text="Introduce un número hexadecimal de 3 dígitos: ", font=("Adobe Gothic Std B",12),background="#27363B",foreground="white" ).place(x=30,y=150)
    ent_hex1= tk.Entry(canvas_principal2,font=("Adobe Gothic Std B",12),width=25)
    ent_hex1.place(x=355,y=151)

        #******************Creación de tabla para mostrar datos***********************
    ent_hex = tk.Entry(canvas_principal2, width=12, justify="center")
    ent_hex.insert(0, "Hexadecimal")
    ent_octal = tk.Entry(canvas_principal2, width=12, justify="center")
    ent_octal.insert(0, "Octal")
    ent_decimal = tk.Entry(canvas_principal2, width=12, justify="center")
    ent_decimal.insert(0, "Decimal")
    ent_binario = tk.Entry(canvas_principal2, width=12, justify="center")
    ent_binario.insert(0, "Binario")
    hex_value = tk.Entry(canvas_principal2, width=12, justify="center")
    oct_value = tk.Entry(canvas_principal2, width=12, justify="center")
    dec_value = tk.Entry(canvas_principal2, width=12, justify="center")
    bin_value = tk.Entry(canvas_principal2, width=12, justify="center")
    ent__list = [ent_hex, ent_octal, ent_decimal, ent_binario, hex_value, oct_value, dec_value, bin_value]

    # Ubicamos los ent_ utilizando place
    ent_hex.place(x=30, y=200)
    ent_octal.place(x=110, y=200)
    ent_decimal.place(x=190, y=200)
    ent_binario.place(x=270, y=200)
    hex_value.place(x=30, y=225)
    oct_value.place(x=110, y=225)
    dec_value.place(x=190, y=225)
    bin_value.place(x=270, y=225)

    # Bloqueamos los ent_
    for ent_ in ent__list:
        ent_.config(state="disabled")        
    canvas_principal2.pack()

    def convertir():
        hex = ent_hex1.get()
        # Convertir el número hexadecimal a decimal
        try:            
            decimal = int(hex, 16)
        except:
            pass
        valido = False
        while not valido:
            if len(hex) == 3:
                valido = True
                for char in hex:
                    if char not in "0123456789abcdefABCDEF":
                        valido = False
                        break
                if decimal < 0 or decimal > 2047:
                    tk.messagebox.showerror(title="Error", message="El valor ingresado está fuera del rango permitido (000 - 7FF).")
                    break
                if valido:
                    hex_value.config(state="normal")
                    hex_value.delete(0, END)
                    hex_value.insert(0, hex)
                    hex_value.config(state="disabled")


                    # Convertir el número decimal a octal y binario
                    octal = oct(decimal)
                    binario = bin(decimal)

                    # Actualizar los campos de texto correspondientes
                    oct_value.config(state="normal")
                    oct_value.delete(0, END)
                    oct_value.insert(0, str(octal)[2:])
                    oct_value.config(state="disabled")

                    dec_value.config(state="normal")
                    dec_value.delete(0, END)
                    dec_value.insert(0, str(decimal))
                    dec_value.config(state="disabled")

                    bin_value.config(state="normal")
                    bin_value.delete(0, END)
                    bin_value.insert(0, str(binario)[2:])
                    bin_value.config(state="disabled")

                    print(binario)
                else:
                    tk.messagebox.showerror(title="Error", message="El valor ingresado no es un número hexadecimal válido.")
                    break
            else:
                tk.messagebox.showerror(title="Error", message="El valor ingresado no es un número hexadecimal válido.")
                break
        #***************Se define la logica del grafico NRZI******************
        def dibuja_NRZI(signal, alto_logico, bajo_logico, distancia):
            t.sety(bajo_logico)
            for i in signal:
                if i == '0':
                    t.forward(distancia)
                elif i == '1':
                    posx, posy = t.pos()
                    if bajo_logico - 1 < posy < bajo_logico + 1:
                        t.sety(alto_logico)
                    elif alto_logico - 1 < posy < alto_logico + 1:
                        t.sety(bajo_logico)
                    t.forward(distancia)
                    print(posy)

        #***************Dibuja los ejes en la ventana*************************
        def dibuja_ejes(len_X):
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

        #*********Creacion de linea graficadora*************************************
        def setTurtle(size, colour, speed, visibility):
            t.pensize(size)
            t.pencolor(colour)
            t.speed(speed)
            if not visibility:
                t.hideturtle()
                
        #**Ingresa la señal binaia y llama al as funciones para dibujar el grafico
        señal = str(binario)[2:]

        raiz = tk.Tk()
        raiz.title('Grafico NRZI')
        raiz.geometry('1000x300')
        cv = turtle.ScrolledCanvas(raiz, width=1000) 
        cv.pack()

        len_X, len_Y = 1000, 350
        default_settings = (2, 'red', 'slowest', False)
        invisiline = (1, 'black', 'fastest', False)

        screen = turtle.TurtleScreen(cv)
        screen.screensize(len_X, len_Y)
        t = turtle.RawTurtle(screen)

        dibuja_ejes(len_X)
        setTurtle(*default_settings)
        dibuja_NRZI(señal, 50, -50, 50)

        raiz.mainloop()                
    convert_btn= tk.Button(canvas_principal2, text="Convertir",command= convertir).place(x=590,y=150)
                
#******************Creacion de ventanas(FIN)************************

btn_create_window_Hamming = tk.Button(mainwindow,
             text ="Conversiones/NZRI",
             command = openNewWindow_Conversion)
btn_create_window_Hamming.place(x=480, y=400)

btn2_create_window_Conversion = tk.Button(mainwindow,
             text ="Codigo Hamming",
             command = openNewWindow_Hamming_Code)
btn2_create_window_Conversion.place(x=620, y=400)

mainwindow.mainloop()