import tkinter as tk
import conexion as c  # --> archivo que conecta la BBDD
#---------------------------------------------------------------
# se crea ventana gráfica

ventana = tk.Tk()
ventana.title("My App")
ventana.geometry("1000x600+160+50")
ventana.resizable(0,0)


# --> creacion de BBDD y tablas<--
c.conectar()

#---------------------------------------------------------------
# -> para que la ventana se mantenga abierta
ventana.mainloop()