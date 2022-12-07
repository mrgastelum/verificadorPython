from tkinter import *
from PIL import ImageTk, Image
import json

codigo=""

def readjson():
    with open("productos.json") as json_file:
        return json.load(json_file).get("productos")

def key_pressed(event):
    global codigo
    if event.keysym == "Return":
        print(codigo)
        item = productos.setdefault(codigo, ["None", "0.00", "images/no encontrado.jpg"])
        codigo=""
        if item is not None:
            # loads the img from the product
            loadImg(item[-1])
            tagProd.config(text=item[0])
            tagPrice.config(text=item[1])
        else:
            loadImg("images/no encontrado.jpg")
    else:
        codigo+=event.keysym

def loadImg(imgPath):
    # imagen
    # PNG, JPEG and GIF
    render = ImageTk.PhotoImage(Image.open(imgPath))
    img = Label(ventana, image=render, width=500, height=500)
    img.image = render
    img.place(x=Vwidth/2 - 249, y=250)

productos = readjson()

ventana = Tk()
ventana.geometry("1000x800")
# ventana.attributes('-fullscreen', True)
ventana.update()

fuente = ("Arial", 18, "bold")
Vwidth = ventana.winfo_width()
Vheight = ventana.winfo_height()

loadImg("images\cbarras.gif")

# tag Titulo
tag1 = Label(ventana, text="Lector de productos", font=fuente)
tag1.place(x=Vwidth/2 - tag1.winfo_width()/2, y=5)
tag1.pack()

# tag Product
tagProd = Label(ventana, text="Producto "+str(Vwidth), font=fuente)
tagProd.pack()
tagProd.place(x=10, y=150)

# tag Price
tagPrice = Label(ventana, text="Precio "+str(Vheight), font=fuente)
tagPrice.pack()
tagPrice.place(x=10, y=195)

# event handler for Return key
ventana.bind('<Key>', key_pressed)

#Mainloop al final del codigo
ventana.mainloop()