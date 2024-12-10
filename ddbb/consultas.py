from .conexion import Conexion
#------------------------------------------
def crear_tabla():
    cone = Conexion()

    sql = """
              CREATE TABLE IF NOT EXISTS pacientes
             (
              ID INTEGER PRIMARY KEY AUTOINCREMENT,
              NOMBRE TEXT NOT NULL,
              APELLIDO TEXT NOT NULL,
              DNI TEXT NOT NULL UNIQUE,
              CELULAR TEXT NOT NULL UNIQUE,
              MAIL TEXT NOT NULL UNIQUE
              );

               CREATE TABLE IF NOT EXISTS tratamientos
             (
              ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
              NOMBRE TEXT NOT NULL
              );

              CREATE TABLE IF NOT EXISTS tratamientos_pacientes
             (
              ID INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,
              DIAGNOSTICO TEXT NOT NULL UNIQUE,
              AVANCES TEXT NOT NULL UNIQUE,
              ID_PACIENTES INTEGER,
              ID_TRATAMIENTOS INTEGER,
              FOREIGN KEY(ID_PACIENTES) REFERENCES pacientes(id),
              FOREIGN KEY(ID_TRATAMIENTOS) REFERENCES tratamientos(id)
              )

           """
    try:
        cone.cursor.executescript(sql)
    except:
        pass
    finally:
        cone.cerrar_conexion()

#------------------------------------------
class Paciente():

    def __init__(self, nombre, apellido, dni, cel, mail):
        self.id_paciente = None
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
        self.cel = cel
        self.mail = mail

    def __str__(self):
        return f'Paciente[{self.nombre}, {self.apellido}, {self.dni}, {self.cel}, {self.mail}]'
#------------------------------------------
def guardar_paciente(paciente):
    cone = Conexion()

    sql= f'''
             INSERT INTO pacientes(Nombre,Apellido,Dni, Celular, Mail)
             VALUES('{paciente.nombre}','{paciente.apellido}','{paciente.dni}','{paciente.cel}','{paciente.mail}');
        '''
    try:
        cone.cursor.execute(sql)
    except:
        pass
    finally:
        cone.cerrar_conexion()
#------------------------------------------
def listar_pacientes():
    cone = Conexion()
    listar_pacientes = []
   
    sql = f'''
            SELECT * FROM pacientes as p
           
          '''
    try:
        cone.cursor.execute(sql)
        listar_pacientes = cone.cursor.fetchall()

        return listar_pacientes
    except:
        pass
    finally:
       cone.cerrar_conexion()
#------------------------------------------
def listar_tratamientos():
    cone = Conexion()

    listar_tratamiento = []

    sql = f'''
           SELECT * FROM tratamientos;
          '''
    try:
        cone.cursor.execute(sql)
        listar_tratamiento = cone.cursor.fetchall()

        return listar_tratamiento
    except:
        pass
    finally:
        cone.cerrar_conexion()
#------------------------------------------
def editar_paciente(paciente, id):
    cone = Conexion()
    
    sql= f'''
             UPDATE pacientes
             SET Nombre = '{paciente.nombre}', Apellido = '{paciente.apellido}', Dni = '{paciente.dni}', Cel = '{paciente.cel}', Mail = '{paciente.mail}'
              WHERE ID = {id}
             ;
         '''
    try:
        cone.cursor.execute(sql)
    except:
        pass
    finally:
        cone.cerrar_conexion()
#------------------------------------------
def borrar_paciente(id):
    cone = Conexion()

    sql= f'''
         DELETE FROM pacientes WHERE ID = {id};
         '''
    try:
        cone.cursor.execute(sql)
    except:
        pass
    finally:
        cone.cerrar_conexion()

