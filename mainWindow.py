import tkinter as tk

#******************Ventana Principal**********************
mainwindow = tk.Tk()
mainwindow.title('Menu principal: Codigo Hamming')
canvas_principal = tk.Canvas(mainwindow, width=250, height=100)
canvas_principal.pack()
#******************Ventana Principal**********************

#******************Creacion de ventanas(Inicio)************************
def openNewWindow_Hamming_Code():
    newWindow = tk.Toplevel(mainwindow)
    newWindow.title('Codigo Hamming')
    #newWindow.geometry("960x540")    
    canvas_principal1 = tk.Canvas(newWindow, width=500, height=450)
    canvas_principal1.pack()
    texto1 = tk.Label(newWindow, text= "This is a new window")
    texto1.pack()

def openNewWindow_Conversion():
    newWindow2 = tk.Toplevel(mainwindow)
    newWindow2.title('Conversion')
    #newWindow2.geometry("960x540")
    canvas_principal2 = tk.Canvas(newWindow2, width=500, height=450)
    canvas_principal2.pack()
    texto2 = tk.Label(newWindow2, text= "This is a new window")
    texto2.pack()

#******************Creacion de ventanas(FIN)************************

label = tk.Label(mainwindow, text = "This is the main window")
label.pack(pady = 10)

btn_create_window_Hamming = tk.Button(mainwindow,
             text ="Conversiones",
             command = openNewWindow_Conversion)
btn_create_window_Hamming.place(x=85, y=10)

btn2_create_window_Conversion = tk.Button(mainwindow,
             text ="Codigo Hamming",
             command = openNewWindow_Hamming_Code)
btn2_create_window_Conversion.place(x=75, y=50)
#top = Toplevel()


mainwindow.mainloop()