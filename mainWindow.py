from tkinter import *
import tkinter as tk
from tkinter import messagebox
import turtle
import Hammin_code

#Color & fonts
bg_color='#296ABC'
text_color = '#CDE6F5'
btn_color = '#ACF39D'
t_font ='Times New Roman'
t_font_size = 18
subt_font_size = 16
small_text_size = 12

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
    canvas_principal1 = tk.Canvas(newWindow, width=895, height=500, background='#000000')
    bg1=PhotoImage(file="resources//Hamming Code.png",master=newWindow)
    label3 = Label( canvas_principal1,image=bg1,background='#000000')
    label3.image = bg1
    label3.place(x = 0, y = 0)
    print(binario_ext[2:]) #Valor binario extraído
    text_label = tk.Label( canvas_principal1, text="El número binario es:", font=(t_font,subt_font_size), background="#2A5FB7").place(x = 350, y = 150)
    bin_label = tk.Label( canvas_principal1, text= binario_ext,font=(t_font,subt_font_size), background="#2A5FB7").place(x = 380, y = 190)
    text2_label = tk.Label( canvas_principal1, text="Escoge la paridad:", font=(t_font,subt_font_size), background="#2A5FB7").place(x = 360, y = 230)
    parity = BooleanVar()
    odd = Radiobutton(canvas_principal1,text="Odd parity", variable=parity, value=False , font=(t_font,subt_font_size),fg='#000000',highlightcolor=btn_color, background="#2A5FB7")
    odd.place(x=380,y=300)
    even = Radiobutton(canvas_principal1,text="Even parity", variable=parity, value=True , font=(t_font,subt_font_size),fg='#000000',highlightcolor=btn_color, background="#2A5FB7")
    even.place(x=380,y=270)
    

    '''
This function tries to invoke the Hamming encoding module, and after getting the response, 
it proceeds to create the encoding table. 
In case of failure, it displays an alert to the user to handle different error cases.
'''
    def encode():
        try:
            int(binario_ext,2)
            encoded = Hammin_code.hamming_encode(binario_ext,parity.get())
            create_new_encription(encoded)
        except:
            if binario_ext == "":
                tk.messagebox.showwarning(title="Alert!", message="Por favor introduzca un número binario")
            else:
                tk.messagebox.showerror(title="Error!", message="Número binario inválido")

    def encode_bitdif():
        try:
            int(valorFinalString,2)
            encoded = Hammin_code.hamming_encode(valorFinalString,parity.get())
            create_new_encription(encoded)
        except:
            if binario_ext == "":
                tk.messagebox.showwarning(title="Alert!", message="Por favor introduzca un número binario")
            else:
                tk.messagebox.showerror(title="Error!", message="Número binario inválido")

    '''
    This function tries to make a call to the Hamming encoding check module, 
    to execute with the response to execute the creation of the encoding check table. 
    If it fails it displays an alert to the user for different error cases.
    '''
    def check():
        try:
            int(binario_ext,2)
            checked = Hammin_code.check_hamming_encode(binario_ext,parity.get())
            create_new_check(checked[0],checked[1],int(parity.get()))
        except:
            if binario_ext == "":
                tk.messagebox.showwarning(title="Alert!", message="Por favor introduzca un número binario")
            elif len(binario_ext) == 1:
                tk.messagebox.showerror(title="Error!", message="El número binario deber ser de mayor logintud")
            else:
                tk.messagebox.showerror(title="Error!", message="Número binario inválido")



    '''
   This function creates and displays a coding table according to the data in list

    @param list: A list of encoding returned by Hammin_code.py

    '''
    def create_new_encription(list):

        # find total number of rows and
        # columns in list
        global valorFinalString
        total_rows = len(list)+1
        total_columns = len(list[-1])+1

        window_w = (total_columns-1)*37 + 188
        window_h = total_rows*27

        new_encript = Toplevel()
        new_encript.resizable(False, False)
        new_encript.title('Encoded number')
        new_encript.geometry("%dx%d+0+0" % (window_w, window_h))

        # Canvas
        encript_canvas = Canvas(new_encript, width= window_w, height=window_h, bg=bg_color)
        encript_canvas.place(x=-2, y=-2)

        d=0
        p=0
        
        for i in range(total_rows):
                for j in range(total_columns):

                    #(0,0)
                    if i==0 and j==0:
                        Entry(encript_canvas, width=17, fg=text_color, background=bg_color,
                                    font=(t_font,subt_font_size,'bold')).grid(row=i,column=j)

                    #(1,0)
                    elif i==1 and j==0:
                        e = Entry(encript_canvas, width=17, fg=text_color, background=bg_color,
                                    font=(t_font,subt_font_size,'bold'))
                        e.grid(row=i,column=j)
                        e.insert(END, "Input(No parity)")
                        p=0
                        d=0

                    #(p's column)
                    elif i!=0 and i!=1 and  j==0 and i != total_rows - 1:
                        e = Entry(encript_canvas, width=17, fg=text_color, background=bg_color,
                                    font=(t_font,subt_font_size,'bold'))
                        e.grid(row=i, column=j)
                        e.insert(END, "p" + str(i-1))

                    #(n,0)
                    elif i == total_rows-1 and j==0:
                        e = Entry(encript_canvas, width=17, fg=text_color, background=bg_color,
                                    font=(t_font,subt_font_size,'bold'))
                        e.grid(row=i,column=j)
                        e.insert(END, "Output(with parity)")

                    #(p & d row)
                    elif i==0 and j!=0:
                        e = Entry(encript_canvas, width=3, fg=text_color, background=bg_color,
                                    font=(t_font,subt_font_size,'bold'))
                        
                        e.grid(row=i, column=j)
                        if j == 2**p:
                            e.insert(END, "p" + str(p+1))
                            p=p+1
                        else:
                            d=d+1
                            e.insert(END, "d" + str(d))
                    
                    #(input string)
                    elif i==1 and j!=0:
                        if j != 2**p:
                            e = Entry(encript_canvas, width=3, fg=text_color, background=bg_color,
                                        font=(t_font,subt_font_size,'bold'))
                            e.grid(row=i, column=j)
                            e.insert(END,list[0][d])    
                            d=d+1
                        else:
                            e = Entry(encript_canvas, width=3, fg=text_color, background=bg_color,
                                        font=(t_font,subt_font_size,'bold'))
                            e.grid(row=i, column=j)
                            p=p+1
                        
                    #(output string)
                    elif i==total_rows-1:
                        e = Entry(encript_canvas, width=3, fg=text_color, background=bg_color,
                                    font=(t_font,subt_font_size,'bold'))
                        
                        e.grid(row=i, column=j)
                        e.insert(END,list[-1][j-1])
                        
                    
                    #(inner lists)
                    else:
                        e = Entry(encript_canvas, width=3, fg=text_color, background=bg_color,
                                    font=(t_font,subt_font_size,'bold'))
                        
                        e.grid(row=i, column=j)
                        e.insert(END,list[i-1][j-1])
                        #print(list[-1])
                        valor_final_string = str(list[-1])
                        valorFinalString = valor_final_string
                        
                        #print(valor_final_string)
                        print(valorFinalString)

    '''
    This function alerts the user if errors are found in a coding and where.
    It also creates and displays a coding check table according to the data in list.

    @param list: A list of encodings returned by Hammin_code.py.

    @param error: The bit position where the error is.

    @param parity: A boolean with the parity of the encoding (even = true ; odd = false)

    '''
    def create_new_check(list,error,parity):
        if error == 0: 
            tk.messagebox.showinfo(title="Success!", message="Ningún error encontrado")
        else:
            tk.messagebox.showerror(title="Error detected!",message="Error encontrado en el bit #" + str(error))

        # find total number of rows and
        # columns in list
        total_rows = len(list)+1
        total_columns = len(list[0])+3

        window_w = (total_columns-3)*37 + (110*3)
        window_h = total_rows*27

        new_check = Toplevel()
        new_check.resizable(False, False)
        new_check.title('Checked parity')
        new_check.geometry("%dx%d+0+0" % (window_w, window_h))

        # Canvas
        check_canvas = Canvas(new_check, width= window_w, height=window_h, bg=bg_color)
        check_canvas.place(x=-2, y=-2)

        d=0
        p=0
        
        for i in range(total_rows):
                for j in range(total_columns):

                    #(0,0)
                    if i==0 and j==0:
                        Entry(check_canvas, width=10, fg=text_color, background=bg_color,
                                    font=(t_font,subt_font_size,'bold')).grid(row=i,column=j)
                    #(1,0)
                    elif i==1 and j==0:
                        e = Entry(check_canvas, width=10, fg=text_color, background=bg_color,
                                    font=(t_font,subt_font_size,'bold'))
                        e.grid(row=i,column=j)
                        e.insert(END, "Input")
                        p=0
                        d=0

                    #(0,m-1)
                    elif i==0 and j==total_columns-1:
                        e = Entry(check_canvas, width=10, fg=text_color, background=bg_color,
                                    font=(t_font,subt_font_size,'bold'))
                        e.grid(row=i,column=j)
                        e.insert(END, "Parity Bit")

                    #(0,m-2)
                    elif i==0 and j==total_columns-2:
                        e = Entry(check_canvas, width=10, fg=text_color, background=bg_color,
                                    font=(t_font,subt_font_size,'bold'))
                        e.grid(row=i,column=j)
                        e.insert(END, "Parity check")

                    #(1,m-1)
                    elif i==1 and j==total_columns-1:
                        e = Entry(check_canvas, width=10, fg=text_color, background=bg_color,
                                    font=(t_font,subt_font_size,'bold'))
                        e.grid(row=i,column=j)

                    #(2,m-2)
                    elif i==1 and j==total_columns-2:
                        e = Entry(check_canvas, width=10, fg=text_color, background=bg_color,
                                    font=(t_font,subt_font_size,'bold'))
                        e.grid(row=i,column=j)
                        e.insert(END, str(parity))

                    #(p's column)
                    elif i!=0 and i!=1 and j==0:
                        e = Entry(check_canvas, width=10, fg=text_color, background=bg_color,
                                    font=(t_font,subt_font_size,'bold'))
                        e.grid(row=i, column=j)
                        e.insert(END, "p" + str(i-1))

                    #(p & d row)
                    elif i==0 and j!=0:
                        e = Entry(check_canvas, width=3, fg=text_color, background=bg_color,
                                    font=(t_font,subt_font_size,'bold'))
                        
                        e.grid(row=i, column=j)
                        if j == 2**p:
                            e.insert(END, "p" + str(p+1))
                            p=p+1
                        else:
                            d=d+1
                            e.insert(END, "d" + str(d))
                    
                    elif i==1 and j!=0 and j < total_columns-2:
                        e = Entry(check_canvas, width=3, fg=text_color, background=bg_color,
                                    font=(t_font,subt_font_size,'bold'))
                        
                        e.grid(row=i, column=j)
                        e.insert(END,list[0][j-1])
                        
                    else:

                        this_list = list[i-1]

                        if j == total_columns-1:
                            e = Entry(check_canvas, width=10, fg=text_color, background=bg_color,
                                        font=(t_font,subt_font_size,'bold'))
                            e.grid(row=i, column=j)
                            e.insert(END,this_list[0])

                        elif j == total_columns-2:
                            e = Entry(check_canvas, width=10, fg=text_color, background=bg_color,
                                        font=(t_font,subt_font_size,'bold'))
                            e.grid(row=i, column=j)
                            e.insert(END,this_list[1])

                        else:
                            e = Entry(check_canvas, width=3, fg=text_color, background=bg_color,
                                        font=(t_font,subt_font_size,'bold'))
                            e.grid(row=i, column=j)
                            e.insert(END,this_list[2][j-1])
    encode_btn = Button(canvas_principal1, text="Codificar", command=encode, font=(t_font, subt_font_size), fg='black', bg='lightblue', activebackground='lightblue', activeforeground='black')
    encode_btn.config(height=2, width=15, relief='raised', bd=2, highlightthickness=0)
    encode_btn.place(x=150, y=350)

    encode_btn = Button(canvas_principal1, text="Revisar", command=check, font=(t_font, subt_font_size), fg='black', bg='lightblue', activebackground='lightblue', activeforeground='black')
    encode_btn.config(height=2, width=15, relief='raised', bd=2, highlightthickness=0)
    encode_btn.place(x=350, y=350)

    encode_btn3 = Button(canvas_principal1, text="Codificar con bit diferente", command=openNewWindow_Prueba, font=(t_font, subt_font_size), fg='black', bg='lightblue', activebackground='lightblue', activeforeground='black')
    encode_btn3.config(height=2, width=20, relief='raised', bd=2, highlightthickness=0)
    encode_btn3.place(x=550, y=350)

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
        global binario_ext
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
                    binario = bin(decimal) #Extraer este valor y almacenarlo en la ventana Hamming
                    binario_ext = binario[2:]
                   

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

def openNewWindow_Prueba():
    global numeroBitCambiado
    
    newWindow = tk.Toplevel()
    newWindow.title('Prueba')
    newWindow.geometry("300x300")
    label1 = tk.Label(newWindow, text="Valor conseguido anteriormente: " ,font=(t_font,subt_font_size), background="#2A5FB7")
    label1.place(x = 10, y = 10)
    label3 = tk.Label(newWindow, text=valorFinalString ,font=(t_font,subt_font_size), background="#2A5FB7")
    label3.place(x = 10, y = 40)
    label2 = tk.Label(newWindow, text="Escriba todo el número con el bit que desee cambiar ")
    label2.place(x = 10, y = 100)
    ent_valor_bit_cambiado= tk.Entry(newWindow,font=("Adobe Gothic Std B",12),width=25)
    ent_valor_bit_cambiado.place(x=10,y=150)
    
    def guardar():
        global binario_ext
        bit_cambiado = ent_valor_bit_cambiado.get()
        binario_ext = bit_cambiado

    bit_regresar_btn = tk.Button(newWindow,
             text ="Regresar a Ventana Hamming",
             command = openNewWindow_Hamming_Code)
    bit_regresar_btn.place(x = 10, y = 250)

    bit_camb_btn = tk.Button(newWindow,
             text ="Guardar",
             command = guardar)
    bit_camb_btn.place(x = 10, y = 200)

    

    

                
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