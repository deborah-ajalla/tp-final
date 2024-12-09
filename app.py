import tkinter as tk
import conexion as c  # --> archivo que conecta la BBDD
from consultas import guardar_paciente
from tkinter import messagebox, ttk
import sys
#---------------------------------------------------------------
# --> Se define paleta colores 
TITULOS = "#C93384"
SECONDARY = "#B794F4"
PRIMARY = "#ffc1ff"
BOTONES = "#805AD5"
# se crea ventana gráfica
ventana = tk.Tk()
ventana.title("Centro de Estética")
ventana.geometry("1000x600+160+50")
ventana.resizable(0,0)
ventana.config(bg= PRIMARY)
#-----------------------------------------------
# --> creacion de BBDD y tablas<--
c.conectar()
#-----------------------------------------------
etiqueta_titulo = tk.Label(ventana, text= " Centro de Estética", 
                           font=("Nunito", 28,  "bold"),
                           fg=TITULOS, bg=PRIMARY)
etiqueta_titulo.place(x=330, y=20 )
#-----------------------------------------------
# --> Pestañas Menú
barra_menu = tk.Menu(ventana)
ventana.config( menu=barra_menu, width=500, height=500)
menu_inicio = tk.Menu(barra_menu, tearoff=0)
opciones_1 = tk.Menu (barra_menu, tearoff=0)
opciones_2 = tk.Menu(barra_menu, tearoff=0)
opciones_3 = tk.Menu(barra_menu, tearoff=0)
submenu_listados= tk.Menu(barra_menu, tearoff=0)
submenu_tratamientos= tk.Menu(barra_menu, tearoff=0)
barra_menu.add_cascade (label='Paciente', menu=opciones_1)
opciones_1.add_command(label= 'Cargar Datos')
opciones_1.add_command(label= 'Buscar')
opciones_1.add_command(label= 'Modificar Datos')
opciones_1.add_command(label= 'Eliminar')

barra_menu.add_cascade (label='Tratamiento', menu=opciones_2)
opciones_2.add_command (label= 'Cargar')

barra_menu.add_cascade (label='Listados', menu=opciones_3)
opciones_3.add_cascade (label= 'Pacientes',menu= submenu_listados)
submenu_listados.add_command(label='Por ID')
submenu_listados.add_command(label='Por DNI')
submenu_listados.add_command(label='Por Apellido')

opciones_3.add_cascade (label= 'Tratamientos', menu=submenu_tratamientos)
submenu_tratamientos.add_command(label='Totales')
submenu_tratamientos.add_command(label='Con Info de Pacientes')

barra_menu.add_cascade (label='Busqueda', menu=menu_inicio)
barra_menu.add_cascade (label='Salir', command=ventana.destroy)
#-----------------------------------------------
#--> Etiquetas Label
label_nombre = tk.Label(ventana, text = 'Nombre: ')
label_nombre.config(bg=PRIMARY,fg=TITULOS,font= ("Nunito", 15, "bold"))
label_nombre.place(x = 100, y = 110)

label_apellido = tk.Label(ventana, text = 'Apellido: ')
label_apellido.config(bg=PRIMARY,fg=TITULOS,font= ("Nunito", 15, "bold"))
label_apellido.place(x = 100, y = 150)

label_dni = tk.Label(ventana, text = 'Dni: ')
label_dni.config(bg=PRIMARY,fg=TITULOS,font= ("Nunito", 15, "bold"))
label_dni.place(x = 100, y = 190)

label_cel = tk.Label(ventana, text = 'Celular: ')
label_cel.config(bg=PRIMARY,fg=TITULOS,font= ("Nunito", 15, "bold"))
label_cel.place(x = 520, y = 110)

label_mail = tk.Label(ventana, text = 'Email : ')
label_mail.config(bg=PRIMARY,fg=TITULOS,font= ("Nunito", 15, "bold"))
label_mail.place(x = 520, y = 150)
#-----------------------------------------------
# --> Etiquetas Entry
nombre = tk.StringVar()
entry_nombre = tk.Entry(ventana, textvariable = nombre)
entry_nombre.config(width = 28, font = ('Arial', '12', 'bold'), fg=BOTONES)
entry_nombre.place(x = 200, y = 110)

apellido = tk.StringVar()
entry_apellido = tk.Entry(ventana, textvariable = apellido)
entry_apellido.config(width = 28, font = ('Arial', '12', 'bold'), fg=BOTONES)
entry_apellido.place(x = 200, y = 150)

dni = tk.StringVar()
entry_dni = tk.Entry(ventana, textvariable = dni)
entry_dni.config(width = 28, font = ('Arial', '12', 'bold'), fg=BOTONES)
entry_dni.place(x = 200, y = 190)

cel = tk.StringVar()
entry_cel = tk.Entry(ventana, textvariable = cel)
entry_cel.config(width = 28, font = ('Arial', '12', 'bold'), fg=BOTONES)
entry_cel.place(x = 620, y = 110)

mail = tk.StringVar()
entry_mail = tk.Entry(ventana, textvariable = mail)
entry_mail.config(width = 28, font = ('Arial', '12', 'bold'), fg=BOTONES)
entry_mail.place(x = 620, y = 150)
#-----------------------------------------------
# --> Botones
boton_nuevo = tk.Button (ventana, text = 'Nuevo', command = habilitar_campos)
boton_nuevo.config(width = 18, font = ('Arial', '12', 'bold'), fg = 'white', bg = SECONDARY)
boton_nuevo.place(x = 130, y = 260)

boton_guardar = tk.Button (ventana, text = 'Guardar', command = "")
boton_guardar.config(width = 18, font = ('Arial', '12', 'bold'), fg = 'white', bg = SECONDARY)
boton_guardar.place(x = 410, y = 260)

boton_cancelar = tk.Button (ventana, text = 'Cancelar', command = bloquear_campos)
boton_cancelar.config(width = 18, font = ('Arial', '12', 'bold'), fg = 'white', bg = SECONDARY)
boton_cancelar.place(x = 690, y = 260)

#-----------------------------------------------
# --> Creacion de la tabla Gráfica 
tabla = ttk.Treeview (ventana, column = ('Nombre', 'Apellido','Dni', 'Celular', 'Mail'))
tabla.place(x =20, y = 310, width=960, height=220)

tabla.heading('#0', text = 'Id')
tabla.heading('#1', text = 'Nombre')
tabla.heading('#2', text = 'Apellido' )
tabla.heading('#3', text = 'Dni')
tabla.heading('#4', text = 'Celular')
tabla.heading('#5', text = 'Mail')

tabla.column ('#0', anchor = 'center', width = 30)
tabla.column ('#1', anchor = 'center', width = 110)
tabla.column ('#2', anchor = 'center', width = 110)
tabla.column ('#3', anchor = 'center', width = 110)
tabla.column ('#4', anchor = 'center', width = 110)
tabla.column ('#5', anchor = 'center', width = 120)
#-----------------------------------------------
# --> Botones
boton_modificar = tk.Button (ventana, text = 'Modificar', command = "")
boton_modificar.config(width = 18, font = ('Arial', '12', 'bold'), fg = 'white', bg = SECONDARY)
boton_modificar.place(x = 220, y = 550)

boton_eliminar = tk.Button (ventana, text = 'Eliminar', command = "")
boton_eliminar.config(width = 18, font = ('Arial', '12', 'bold'), fg = 'white', bg = SECONDARY)
boton_eliminar.place(x = 550, y = 550)
#---------------------------------------------------------------
# --> FUNCIONES <-- 
def guardar_campos(paciente):
    paciente = pacientes(
        nombre.get(),
        apellido.get(),
        dni.get(),
        cel.get(),
        mail.get()
    )

    if id_paciente == None:
        guardar_paciente(pacientes)
    else:
        editar_paciente(paciente,int(id_paciente))

    bloquear_campos()
    mostrar_tabla()


def bloquear_campos():    
    entry_nombre.config(state='disabled')    
    entry_apellido.config(state='disabled')    
    entry_dni.config(state='disabled')    
    entry_cel.config(state='disabled')  
    entry_mail.config(state='disabled')  
    boton_guardar.config(state='disabled')    
    boton_cancelar.config(state='disabled')    
    boton_nuevo.config(state='normal')
    nombre.set('')
    apellido.set('')
    dni.set('')
    cel.set('')
    mail.set('')
 
    id_paciente = None


def habilitar_campos():    
    entry_nombre.config(state='normal')    
    entry_apellido.config(state='normal')    
    entry_dni.config(state='normal')    
    entry_cel.config(state='normal')
    entry_mail.config(state='normal')
    boton_guardar.config(state='normal')    
    boton_cancelar.config(state='normal')    
    boton_nuevo.config(state='disabled')
#-----------------------------------------------
# -> para que la ventana se mantenga abierta
ventana.mainloop()