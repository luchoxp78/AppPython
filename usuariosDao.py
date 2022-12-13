import sqlite3
import funciones.funciones as util

conn = sqlite3.connect("base_datos/appDB.db")

def createDB():
    cursor = conn.cursor()
    try:
        cursor.execute(""" create table if not exists usuario(
            nombreUsuario text unique,
            email text primary key, 
            nombre text, 
            apellido text, 
            password text,
            fechaNacimiento text,
            direccion texto)""")
        util.addLog("Se creo la tabla usuario", "INFO")
    except sqlite3.OperationalError:
        util.addLog("La tabla ya existe en la base de datos", "ERROR")
        print ("La tabla ya existe en la db")
    finally:
        cursor.close()
    

def insertDB(datos):
    conn = sqlite3.connect("base_datos/appDB.db")
    cursor = conn.cursor()
    print(datos)
    try:
        cursor.execute("insert into usuario (nombreUsuario, email, nombre, apellido, password, fechaNacimiento, direccion) values(?,?,?,?,?,?,?)",
                       (datos[0], datos[1], datos[2], datos[3], datos[4], datos[5], datos[6]))
        conn.commit()
        util.addLog(f"Se inserto el Usuario {datos[0]}", "INFO")
        return "OK"
    except sqlite3.IntegrityError as ierr:
        util.addLog(str(ierr), "ERROR")
        print("Error al insertar en tabla usuarios\n" + str(ierr))
        return str("El usuario ya existe")
    except sqlite3.Error as err:
        util.addLog(str(err), "ERROR")
        print("Error al insertar en tabla usuarios\n" + str(err))
        return "Error al insertar"
    finally:
        cursor.close()

def updateDB(datos):
    conn = sqlite3.connect("base_datos/appDB.db")
    cursor = conn.cursor()
    print(datos)
    try:
        cursor.execute("update usuario set nombre=?, apellido=?, password=?, fechaNacimiento=?, direccion=? where email=?",
                       (datos[2], datos[3], datos[4], datos[5], datos[6], datos[1]))
        conn.commit()
        util.addLog(f"Se actualizó el Usuario {datos[1]}", "INFO")
        return "OK"
    except sqlite3.IntegrityError as ierr:
        util.addLog(str(ierr), "ERROR")
        print("Error al insertar en tabla usuarios\n" + str(ierr))
        return str("El usuario ya existe")
    except sqlite3.Error as err:
        util.addLog(str(err), "ERROR")
        print("Error al insertar en tabla usuarios\n" + str(err))
        return "Error al actualizar"
    finally:
        cursor.close()
    
def getUsuario(email, usr="email"):
    conn = sqlite3.connect("base_datos/appDB.db")
    cursor = conn.cursor()
    try:
        if usr == "email":
            cursor.execute("SELECT * FROM usuario WHERE email=?", (email,))
        else:
            cursor.execute("SELECT * FROM usuario WHERE nombreUsuario=?", (email,))
        util.addLog(f"Se encontro el Usuario {email}", "INFO")
        return cursor.fetchone()
    except sqlite3.Error as err:
        util.addLog(str(err), "ERROR")
        print("Error al consultar en tabla usuarios")
    finally:
        cursor.close()
    