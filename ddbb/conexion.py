import sqlite3
#------------------------------------------------------------
class Conexion():
    def __init__(self):
        # self.base_de_datos = 'ddbb/tp.db'  
        self.conexion = sqlite3.connect("tp.db")
        self.cursor = self.conexion.cursor()

    def cerrar_conexion(self):
        self.conexion.commit()
        self.conexion.close()



