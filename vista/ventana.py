import tkinter as tk
from tkinter import ttk
from ddbb.consultas import Paciente, crear_tabla, guardar_paciente, listar_pacientes, editar_paciente, borrar_paciente

# --> Se define paleta colores 
TITULOS = "#C93384"
SECONDARY = "#B794F4"
PRIMARY = "#ffc1ff"
BOTONES = "#805AD5"
#--------------------------------

class Frame (tk.Frame):
    def __init__(self, root = None):
        super().__init__(root, width=1000, height=600, bg=PRIMARY)
        self.root = root
        self.id_paciente = None
        self.pack()
       

        crear_tabla()
        self.titulo()
        self.etiquetas_label()
        self.etiquetas_entry()
        self.botones()
        self.bloquear_campos()
        self.mostrar_tabla()

    #--------------------------------
    #--> Etiquetas Label
    def titulo(self):
        self.etiqueta_titulo = tk.Label(self, text= " Centro de Estética", font=("Nunito", 28,  "bold"), fg=TITULOS, bg=PRIMARY)
        self.etiqueta_titulo.place(x=330, y=20 )
    #--------------------------------    
    def etiquetas_label(self):
        self.label_nombre = tk.Label(self, text = 'Nombre: ')
        self.label_nombre.config(bg=PRIMARY,fg=TITULOS,font= ("Nunito", 15, "bold"))
        self.label_nombre.place(x = 100, y = 110)

        self.label_nombre = tk.Label(self, text = 'Apellido: ')
        self.label_nombre.config(bg=PRIMARY,fg=TITULOS,font= ("Nunito", 15, "bold"))
        self.label_nombre.place(x = 100, y = 150)

        self.label_nombre = tk.Label(self, text = 'Dni: ')
        self.label_nombre.config(bg=PRIMARY,fg=TITULOS,font= ("Nunito", 15, "bold"))
        self.label_nombre.place(x = 100, y = 190)

        self.label_nombre = tk.Label(self, text = 'Celular: ')
        self.label_nombre.config(bg=PRIMARY,fg=TITULOS,font= ("Nunito", 15, "bold"))
        self.label_nombre.place(x = 520, y = 110)

        self.label_nombre = tk.Label(self, text = 'Email : ')
        self.label_nombre.config(bg=PRIMARY,fg=TITULOS,font= ("Nunito", 15, "bold"))
        self.label_nombre.place(x = 520, y = 150)
     #-----------------------------------------------
     #--> Etiquetas Entry
    def etiquetas_entry(self):
        self.nombre = tk.StringVar()
        self.entry_nombre = tk.Entry(self, textvariable = self.nombre)
        self.entry_nombre.config(width = 28, font = ('Arial', '12', 'bold'), fg=BOTONES)
        self.entry_nombre.place(x = 200, y = 110)

        self.apellido = tk.StringVar()
        self.entry_apellido = tk.Entry(self, textvariable = self.apellido)
        self.entry_apellido.config(width = 28, font = ('Arial', '12', 'bold'), fg=BOTONES)
        self.entry_apellido.place(x = 200, y = 150)

        self.dni = tk.StringVar()
        self.entry_dni = tk.Entry(self, textvariable = self.dni)
        self.entry_dni.config(width = 28, font = ('Arial', '12', 'bold'), fg=BOTONES)
        self.entry_dni.place(x = 200, y = 190)

        self.cel = tk.StringVar()
        self.entry_cel = tk.Entry(self, textvariable = self.cel)
        self.entry_cel.config(width = 28, font = ('Arial', '12', 'bold'), fg=BOTONES)
        self.entry_cel.place(x = 620, y = 110)

        self.mail = tk.StringVar()
        self.entry_mail = tk.Entry(self, textvariable = self.mail)
        self.entry_mail.config(width = 28, font = ('Arial', '12', 'bold'), fg=BOTONES)
        self.entry_mail.place(x = 620, y = 150)

        # x = listar_tratamientos()
        # y = []
        # for i in x:
        #     y.append(i[1])
    #-----------------------------------------------
    #--> Botones
    def botones(self):
        self.boton_nuevo = tk.Button (self, text = 'Nuevo', command = self.habilitar_campos)
        self.boton_nuevo.config(width = 18, font = ('Arial', '12', 'bold'), fg = '#FFFFFF', bg = SECONDARY, activebackground= BOTONES,cursor='hand2')
        self.boton_nuevo.place(x = 130, y = 260)

        self.boton_guardar = tk.Button (self, text = 'Guardar', command = self.guardar_campos)
        self.boton_guardar.config(width = 18, font = ('Arial', '12', 'bold'), fg = '#FFFFFF', bg = SECONDARY, activebackground= BOTONES, cursor='hand2')
        self.boton_guardar.place(x = 410, y = 260)

        self.boton_cancelar = tk.Button (self, text = 'Cancelar', command = self.bloquear_campos)
        self.boton_cancelar.config(width = 18, font = ('Arial', '12', 'bold'), fg = '#FFFFFF', bg = SECONDARY, activebackground= BOTONES, cursor='hand2')
        self.boton_cancelar.place(x = 690, y = 260)
    #-----------------------------------------------
    def guardar_campos(self):
        paciente = Paciente(    # -> se instancia la clase
            self.nombre.get(),
            self.apellido.get(),
            self.dni.get(),
            self.cel.get(),
            self.mail.get()
        )

        if self.id_paciente == None:
            guardar_paciente(paciente)
        else:
            editar_paciente(paciente,int(self.id_paciente))
        
        self.bloquear_campos()
        self.mostrar_tabla()        
    #-----------------------------------------------
    def habilitar_campos(self):
        self.entry_nombre.config (state= 'normal')
        self.entry_apellido.config (state='normal')
        self.entry_dni.config (state='normal')
        self.entry_cel.config (state='normal')
        self.entry_mail.config (state='normal')
        self.boton_guardar.config (state='normal')
        self.boton_cancelar.config (state='normal')
        self.boton_nuevo.config (state='disabled')
    #-----------------------------------------------
    def bloquear_campos(self):
        self.entry_nombre.config (state='disabled')
        self.entry_apellido.config (state='disabled')
        self.entry_dni.config (state='disabled')
        self.entry_cel.config (state='disabled')
        self.entry_mail.config (state='disabled')
        self.boton_guardar.config (state='disabled')
        self.boton_cancelar.config (state='disabled')
        self.boton_nuevo.config (state='normal')
        self.nombre.set('')
        self.apellido.set('')
        self.dni.set('')
        self.cel.set('')
        self.mail.set('')
        self.id_paciente = None
    #-----------------------------------------------
    def mostrar_tabla(self):

        self.lista_p = listar_pacientes()  # --> me trae el listado que capturo con el fetchall
        self.lista_p.reverse()             # --> invierte el orden sino aparecen en orden de agregado

        self.tabla = ttk.Treeview(self, column = ('Nombre', 'Apellido','Dni', 'Celular', 'Mail'))
        self.tabla.place(x =20, y = 310, width=960, height=220) 

        self.tabla.heading('#0', text = 'ID')
        self.tabla.heading('#1', text = 'Nombre')
        self.tabla.heading('#2', text = 'Apellido' )
        self.tabla.heading('#3', text = 'Dni')
        self.tabla.heading('#4', text = 'Celular')
        self.tabla.heading('#5', text = 'Mail')

        self.tabla.column ('#0', anchor = 'center', width = 30)
        self.tabla.column ('#1', anchor = 'center', width = 110)
        self.tabla.column ('#2', anchor = 'center', width = 110)
        self.tabla.column ('#3', anchor = 'center', width = 110)
        self.tabla.column ('#4', anchor = 'center', width = 110)
        self.tabla.column ('#5', anchor = 'center', width = 120)

        # --> iterar lista de pacientes
        for p in self.lista_p:                      
            self.tabla.insert('',0,text=p[0],   #  --> el [0] es el id
                               values = (p[1],p[2],p[3],p[4],p[5])) # --> inserta los valores en cada campo

        # --> Botones
        self.boton_modificar = tk.Button (self, text = 'Modificar', command=self.editar_registros)
        self.boton_modificar.config(width = 18, font = ('Arial', '12', 'bold'), fg = 'white', bg = SECONDARY,activebackground= BOTONES,cursor='hand2')
        self.boton_modificar.place(x = 220, y = 550)

        self.boton_eliminar = tk.Button (self, text = 'Eliminar', command = self.eliminar_registros)
        self.boton_eliminar.config(width = 18, font = ('Arial', '12', 'bold'), fg = 'white', bg = SECONDARY,activebackground= BOTONES,cursor='hand2')
        self.boton_eliminar.place(x = 550, y = 550)
    #-----------------------------------------------
    def editar_registros(self):
        try:
             self.id_paciente = self.tabla.item(self.tabla.selection())['text']

             self.nombre_paciente = self.tabla.item (self.tabla.selection())['values'][0]
             self.apellido_paciente = self.tabla.item(self.tabla.selection())['values'][1]
             self.dni_paciente = self.tabla.item(self.tabla.selection())['values'][2]
             self.cel_paciente = self.tabla.item(self.tabla.selection())['values'][3]
             self.mail_paciente = self.tabla.item(self.tabla.selection())['values'][4]

             self.habilitar_campos()

             self.nombre.set(self.nombre_paciente)
             self.apellido.set(self.apellido_paciente)
             self.dni.set (self.dni_paciente)
             self.cel.set(self.cel_paciente)
             self.mail.set(self.mail_paciente)

        except:
             pass    
    #-----------------------------------------------
    def eliminar_registros(self):
        self.id_paciente = self.tabla.item(self.tabla.selection())['text']

        borrar_paciente(int(self.id_paciente))

        self.mostrar_tabla()
#-----------------------------------------------
def barra_menu(root):
    barra_menu = tk.Menu(root)
    root.config(menu = barra_menu, width = 500 , height = 500)

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
    barra_menu.add_cascade (label='Salir', command=root.destroy)



    





