import sqlite3
#--------------------------------------------------------------------

# ----> CONEXION <----
def conectar ():
    mi_conexion = sqlite3.connect ("tp.bd")    # -> almaceno en variable la conexion que crea la BBDD
    cursor = mi_conexion.cursor()

# ----> CREA TABLAS pacientes, tratamientos y pacientes_tratamientos<----
    try:
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
              NOMBRE TEXT NOT NULL,
              FECHA DATE NOT NULL,
              ESTADO TEXT NOT NULL,
              PRODUCTOS DOMICILIARIOS TEXT NOT NULL 
              );

              CREATE TABLE IF NOT EXISTS pacientes_tratamientos
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
        cursor.executescript(sql)   # para ejecutar multiples instrucciones... sino sería execute. ❌
        cursor.close()
        return mi_conexion
    
    except Exception as e:
        print (f"Error de Conexión --> ❌ {e} ❌")
        
    finally:
        cursor.close()

