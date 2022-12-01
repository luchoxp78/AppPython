import sqlite3

conn = sqlite3.connect("BaseDatos/appDB.db")

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
        
    except sqlite3.OperationalError:
        print ("La tabla ya existe en la db")
    finally:
        cursor.close()
    

def insertDB(datos):
    conn = sqlite3.connect("BaseDatos/appDB.db")
    cursor = conn.cursor()
    print(datos)
    try:
        cursor.execute("insert into usuario (nombreUsuario, email, nombre, apellido, password, fechaNacimiento, direccion) values(?,?,?,?,?,?,?)",
                       (datos[0], datos[1], datos[2], datos[3], datos[4], datos[5], datos[6]))
        conn.commit()
        return "OK"
    except sqlite3.IntegrityError as ierr:
        print("Error al insertar en tabla usuarios\n" + str(ierr))
        return str("El usuario ya existe")
    except sqlite3.Error as err:
        print("Error al insertar en tabla usuarios\n" + str(err))
        return "Error al insertar"
    finally:
        cursor.close()

def updateDB(datos):
    conn = sqlite3.connect("BaseDatos/appDB.db")
    cursor = conn.cursor()
    print(datos)
    try:
        cursor.execute("update usuario set nombre=?, apellido=?, password=?, fechaNacimiento=?, direccion=? where email=?",
                       (datos[2], datos[3], datos[4], datos[5], datos[6], datos[1]))
        conn.commit()
        return "OK"
    except sqlite3.IntegrityError as ierr:
        print("Error al insertar en tabla usuarios\n" + str(ierr))
        return str("El usuario ya existe")
    except sqlite3.Error as err:
        print("Error al insertar en tabla usuarios\n" + str(err))
        return "Error al actualizar"
    finally:
        cursor.close()
    
def getUsuario(email, usr="email"):
    conn = sqlite3.connect("BaseDatos/appDB.db")
    cursor = conn.cursor()
    try:
        if usr == "email":
            cursor.execute("SELECT * FROM usuario WHERE email=?", (email,))
        else:
            cursor.execute("SELECT * FROM usuario WHERE nombreUsuario=?", (email,))
        
        return cursor.fetchone()
    except sqlite3.OperationalError:
        print("Error al consultar en tabla usuarios")
    finally:
        cursor.close()
    