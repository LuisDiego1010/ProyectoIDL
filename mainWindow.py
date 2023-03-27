from tkinter import *
import tkinter as tk
from PIL import ImageTk, Image

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
    lbl_hex = tk.Label (canvas_principal2,text="Introduce un número hexadecimal de 3 dígitos: ", font=("Adobe Gothic Std B",12),background="#27363B",foreground="white" ).place(x=30,y=150)
    ent_hex= tk.Entry(canvas_principal2,font=("Adobe Gothic Std B",12),width=25)
    ent_hex.place(x=355,y=151)
    def get_value():
        hex=ent_hex.get()
        print(hex)
    convert_btn= tk.Button(canvas_principal2, text="Convertir",command= get_value).place(x=590,y=150)

    #Mostrar los resultados en forma de tabla
    hexadecimal_lbl = tk.Label(canvas_principal2, text="Hexadecimal",font=("Adobe Gothic Std B",10),background="#27363B",foreground="white" )
    octal_lbl = tk.Label(canvas_principal2, text="Octal",font=("Adobe Gothic Std B",10),background="#27363B",foreground="white" )
    decimal_lbl = tk.Label(canvas_principal2, text="Decimal",font=("Adobe Gothic Std B",10),background="#27363B",foreground="white" )
    binario_lbl = tk.Label(canvas_principal2, text="Binario",font=("Adobe Gothic Std B",10),background="#27363B",foreground="white" )

    hexadecimal_lbl.place(x=30, y=200)
    octal_lbl.place(x=110, y=200)
    decimal_lbl.place(x=150, y=200)
    binario_lbl.place(x=205, y=200)


    canvas_principal2.pack()
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