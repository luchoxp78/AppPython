import sqlite3

conn = sqlite3.connect("BaseDatos/appDB.db")

def createDB():
    cursor = conn.cursor()
    try:
        cursor.execute(""" create table if not exists usuario(
            email text primary key, 
            nombre text, 
            apellido text, 
            password text,
            fechaNacimiento text,
            direccion texto)""")
        
    except sqlite3.OperationalError:
        print ("La tabla ya existe en la db")
    cursor.close()
    

def insertDB(datos):
    conn = sqlite3.connect("BaseDatos/appDB.db")
    cursor = conn.cursor()
    print(datos)
    try:
        cursor.execute("insert into usuario (email, nombre, apellido, password, fechaNacimiento, direccion) values(?,?,?,?,?,?)",
                       (datos[0], datos[1], datos[2], datos[3], datos[4], datos[5]))
        conn.commit()
    except sqlite3.OperationalError:
        print("Error al insertar en tabla usuarios")
    
    cursor.close()
    
def getUsuario(email):
    conn = sqlite3.connect("BaseDatos/appDB.db")
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT * FROM usuario WHERE email=?", (email,))
        return cursor.fetchone()
    except sqlite3.OperationalError:
        print("Error al consultar en tabla usuarios")
    
    cursor.close()
    