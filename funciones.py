import re
import bcrypt as crypt


mySalt=crypt.gensalt()

def validarFecha(fecha):
    lista=fecha
    lista=lista.replace("-", "/")
    barras=lista.count("/")
    if barras != 2:
        return True
    else:
        return False

def check(email):
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    # pass the regular expression
    # and the string into the fullmatch() method
    if(re.fullmatch(regex, email)):
        print("Valid Email")
        return False
    else:
        print("Invalid Email")
        return True
    
def encript(clave):
    
    return crypt.hashpw(clave.encode(), mySalt)

def chekPwd(clave, hashPwd):
    if crypt.checkpw(clave.encode(), hashPwd):
        return True
    else:
	    return False