from tkinter import *
from PIL import ImageTk, Image
import requests

codigo=""

def key_pressed(event):
    global codigo
    if event.keysym == "Return":
        print(codigo)
        URL = "http://127.0.0.1/python/api/index2.php?codigo=" + codigo
        Respuesta = requests.get(URL)
        #print(Respuesta.json())

        Datos = Respuesta.json()
        print(Datos["Status"])
        
        codigo=""
        if Datos["Status"] == 200:
            loadImg("" + Datos["Imagen"])
            labelProducto.config(text="Nombre del Producto: " + Datos["Nombre"])
            labelPrecio.config(text="Precio: " + Datos ["Precio"])
            print(Datos["Nombre"])
            print(Datos["Precio"])
            print(Datos["Imagen"])
        else:
            loadImg("img/no encontrado.jpg")
            labelProducto.config(text="Producto no encontrado")
            #labelPrecio.config(text="")
    else:
        codigo+=event.keysym

def loadImg(imgPath):
    render = ImageTk.PhotoImage(Image.open(imgPath))
    img = Label(Ventana, image=render, width=500, height=500)
    img.image = render
    img.place(x=Vwidth/2 - 250, y=250)
    #productos = readjson()

#Ventana
Ventana = Tk()
Ventana.geometry("1000x800")
Ventana.title("CBarras Verificador")
Ventana.update()

#Estilo
Titulos = ("Arial", 18, "bold")
Subtitulos = ("Arial", 18, "bold")

Vwidth = Ventana.winfo_width()
Vheight = Ventana.winfo_height()
loadImg("img/cbarras.gif")

#Label1
labelTitulo = Label(Ventana, text = "CBarras Verificador de precios", font = Titulos)
labelTitulo.pack()
labelTitulo.place(x = Vwidth / 3.5 - labelTitulo.winfo_width() / 3.5, y = 50)

#Label2
labelProducto = Label(Ventana, text = "Producto: " + str(Vwidth), font = Subtitulos)
labelProducto.pack()
labelProducto.place(x = 15, y = 100)

#Label3
labelPrecio = Label(Ventana, text = "Precio: " + str(Vheight), font = Subtitulos)
labelPrecio.pack()
labelPrecio.place(x = 15, y = 150)

#Mainloop
Ventana.bind('<Key>', key_pressed)
Ventana.mainloop()