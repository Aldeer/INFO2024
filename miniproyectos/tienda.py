from os import system

from tkinter import Tk
from tkinter import Frame
from tkinter import Button
from tkinter import Entry
from tkinter import Toplevel
from tkinter import LabelFrame
from tkinter.ttk import Treeview

from tkinter import StringVar
from tkinter import DoubleVar
from tkinter import IntVar

from tkinter.constants import NSEW


BASE_DATOS = list([
    {"codigo":"b-001", "producto":"coca-cola 1L", "precio": 3600.0, "stock": 10},
    {"codigo":"b-001", "producto":"coca-cola 2 1/4L", "precio": 3600.0, "stock": 10},
    {"codigo":"b-001", "producto":"coca-cola 3L", "precio": 3600.0, "stock": 10},
])


system("cls") # limpia antes de comenzar el programa

########## INICIO DE LA APLICACION ##########
root = Tk() # instancia de la ventana principal
root.title("Tienda - CRUD") # conf. titulo win principal
root.geometry("600x600") # conf. tamaño ventana
root.resizable(False, False) # desactiva el redimensionado de ventana

########## FUNCIONES DE LA APLICACION ##########

def formulario_registro(root:Tk) -> None:
    """
    Crea una ventana con un formulario de registro. Recibe como argumento
    la ventana princpal de la aplicacion.
    -parametros:
        -root: Tk
    """
    ########## DEFINICION DE VARIABLES LOCALES ##########
    codigo = StringVar() # variable de campo codigo
    producto = StringVar() # variable de campo producto
    precio = DoubleVar() # variable de campo precio
    stock = IntVar() # variable de campo stock
    
    formulario_win = Toplevel(root) # vetana secundaria para formulario
    formulario_win.grab_set() # activacion de modal
    formulario_win.resizable(False, False) # redimension desactivado

    ########## DEFINICION DE ETIQUETAS ##########
    codigo_lbl = LabelFrame(formulario_win) # etiqueta codigo
    producto_lbl = LabelFrame(formulario_win) # etiqueta producto
    precio_lbl = LabelFrame(formulario_win) # etiqueta precio
    stock_lbl = LabelFrame(formulario_win) # etiqueta stock

    ########## DEFINICION DE INPUTS ##########
    codigo_inp = Entry(codigo_lbl, textvariable=codigo) # input con variable de control
    producto_inp = Entry(producto_lbl, textvariable=producto) # input con variable de control
    precio_inp = Entry(precio_lbl, textvariable=precio) # input con variable de control
    stock_inp = Entry(stock_lbl, textvariable=stock) # input con variable de control

    ########## DEFINICION DE BOTONES ##########
    guardar_btn = Button(formulario_win) # boton de guardado de registro
    cancelar_btn = Button(formulario_win) # boton de cancelar registro

    ########## CONFIGURACION DE WIDGETS ##########

    # CONFIGURACION GRID
    formulario_win.grid_columnconfigure(0, weight=3) # proporcion columna 0
    formulario_win.grid_columnconfigure(1, weight=1) # proporcion columna 1
    formulario_win.grid_rowconfigure(4, weight=1) # proporcion fila 3

    # VENTANA SECUNDARIA
    formulario_win.configure(bg="green") # color de fondo
    
    # ETIQUETAS
    codigo_lbl.configure(text="Codigo") # conf. etiqueta
    codigo_lbl.configure(padx=10, pady=10) # conf. padding

    producto_lbl.configure(text="Nombre producto") # conf. etiqueta
    producto_lbl.configure(padx=10, pady=10) # conf. padding

    precio_lbl.configure(text="Precio") # conf. etiqueta
    precio_lbl.configure(padx=10, pady=10) # conf. padding

    stock_lbl.configure(text="Stock") # conf. etiqueta
    stock_lbl.configure(padx=10, pady=10) # conf. padding

    # INPUTS
    """ codigo_inp.configure(width=20) # ancho del input
    producto_inp.configure(width=40) # ancho del input
    precio_inp.configure(width=20) # ancho del input
    stock_inp.configure(width=20) # ancho del input """

    # BOTONES
    guardar_btn.configure(text="GUARDAR", width=20) # etiqueta del boton
    cancelar_btn.configure(text="CANCELAR", width=20) # etiqueta del boton

    ########## EVENTOS ##########
    guardar_btn.bind("<Button-1>", None) # click guardar
    cancelar_btn.bind("<Button-1>",lambda e: formulario_win.destroy()) # click cancelar

    ########## POSICIONES DE LOS WIDGETS ##########

    # ETIQUETAS
    # dimensiones y padding de las etiquetas de los campos
    codigo_lbl.grid(row=0, column=0, padx=10, pady=5, sticky=NSEW)
    producto_lbl.grid(row=1, column=0, columnspan=2, padx=10, pady=5, sticky=NSEW)
    precio_lbl.grid(row=2, column=0, columnspan=2, padx=10, pady=5, sticky=NSEW)
    stock_lbl.grid(row=3, column=0, columnspan=2, padx=10, pady=5, sticky=NSEW)

    # INPUTS
    codigo_inp.grid()
    producto_inp.grid(sticky=NSEW)
    precio_inp.grid()
    stock_inp.grid()

    # BOTONES
    guardar_btn.grid(row=4, column=0, padx=10, pady=5,sticky=NSEW)
    cancelar_btn.grid(row=4, column=1, padx=10, pady=5, sticky=NSEW)



########## WIDGETS ##########

# frames de la ventana principal
botones_frm = Frame(root) # frame donde van los botones
buscador_frm = Frame(root) # frame donde va el buscador
tabla_frm = Frame(root) # frame donde va la tabla

# botones de botones_frm
registrar_btn = Button(botones_frm) # btn para abrir formulario de registro
editar_btn = Button(botones_frm) # btn para editar registro
eliminar_btn = Button(botones_frm) # btn para eliminar registro

# input buscador
buscador_inp = Entry(buscador_frm) # input para buscar registro

# Tabla de registros
tabla_registros = Treeview(tabla_frm) # tabla para mostrar registros

########## CONFIGURACIONES DE LOS WIDGETS ##########

# CONFIGURACION GRID DE LA VENTANA PRINCIPAL
root.grid_columnconfigure(0, weight=1) # proporcion columna 0 ventana princiapl
root.grid_rowconfigure(0, weight=1) # proporcion fila 0 ventana principal
root.grid_rowconfigure(1, weight=1) # proporcion fila 1 ventana principal
root.grid_rowconfigure(2, weight=5) # proporcion fila 2 ventana principal

# CONFIG. GRID DE LOS FRAMES
botones_frm.grid_columnconfigure(0, weight=1) # proporcion columna 0
botones_frm.grid_columnconfigure(1, weight=1) # proporcion columna 1
botones_frm.grid_columnconfigure(2, weight=1) # proporcion columna 2
botones_frm.grid_rowconfigure(0, weight=1) # proporcion fila 0

buscador_frm.grid_columnconfigure(0, weight=1) # proporcion columna 0
buscador_frm.grid_rowconfigure(0, weight=1) # proporcion fila 0

tabla_frm.grid_columnconfigure(0, weight=1) # proporcion columna 0
tabla_frm.grid_rowconfigure(0, weight=1) # proporcion fila 0

# CONFIGURACION FRAMES
botones_frm.configure(bg="red") # conf. color de fondo

buscador_frm.configure(bg="yellow") # conf. color de fondo

tabla_frm.configure(bg="green") # conf. color de fondo

# BOTON REGISTRAR
registrar_btn.configure(text="REGISTRAR") # etiqueta del boton
registrar_btn.configure(width=10) # alto y ancho boton

# CONF. BOTON EDITAR
editar_btn.configure(text="EDITAR") # conf. etiqueta del boton
editar_btn.configure(width=10) # alto y ancho boton

# CONF. BOTON ELIMINAR
eliminar_btn.configure(text="ELIMINAR") # conf. etiqueta del boton
eliminar_btn.configure(width=10) # conf. alto y ancho boton

########## EVENTOS VENTANA PRINCIPAL ##########

# BOTONES
registrar_btn.bind("<Button-1>",lambda e: formulario_registro(root))


########## POSICIONES DE LOS ELEMENTOS ##########
# FRAMES
botones_frm.grid(row=0, column=0, sticky=NSEW) # mostrar widget con expansion
buscador_frm.grid(row=1, column=0, sticky=NSEW) # mostrar widget con expansion
tabla_frm.grid(row=2, column=0, sticky=NSEW) # mostrar frame tabla con expansion

# BOTONES
registrar_btn.grid(row=0, column=0) # mostrar boton registrar 
editar_btn.grid(row=0, column=1) # mostrar boton editar registro
eliminar_btn.grid(row=0, column=2) # mostrar boton de eliminar registro

# BUSCADOR
buscador_inp.grid(row=0, column=0) # mostrar input buscador

# TABLA
tabla_registros.grid(row=0, column=0, padx=10, pady=10, sticky=NSEW) # mostrar tabla 


root.mainloop() # crea el bucle de la aplicacion