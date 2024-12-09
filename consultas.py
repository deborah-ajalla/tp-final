import sqlite3

def guardar_paciente(paciente):
    mi_conexion = sqlite3.connect ("tp.db") 
    cursor = mi_conexion.cursor()

    sql= f'''
             INSERT INTO pacientes(Nombre,Apellido,Dni, Celular, Mail)
             VALUES('{paciente.nombre}','{paciente.apellido}',{paciente.dni},{paciente.cel},{paciente.mail});
        '''
    try:
        cursor.execute(sql)
    except:
        pass
    finally:
        cursor.close()

def editar_paciente(paciente, id):
    mi_conexion = sqlite3.connect ("tp.db") 
    cursor = mi_conexion.cursor()

    sql= f'''
             UPDATE Peliculas
             SET Nombre = '{pelicula.nombre}', Duracion = '{pelicula.duracion}', Genero = {pelicula.genero}
              WHERE ID = {id}
             ;
         '''
    try:
        cursor.execute(sql)
    except:
        pass
    finally:
        cursor.close()
