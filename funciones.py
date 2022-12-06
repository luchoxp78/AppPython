import re
import bcrypt as crypt
import datetime as date

mySalt=crypt.gensalt()

def validarFecha(fecha):
    lista=fecha
    lista=lista.replace("-", "/")
    barras=lista.count("/")
    if barras != 2:
        return False
    else:
        return True

def check(email):
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    # pass the regular expression
    # and the string into the fullmatch() method
    if(re.fullmatch(regex, email)):
        print("Valid Email")
        return True
    else:
        print("Invalid Email")
        return False
    
def encript(clave):
    
    return crypt.hashpw(clave.encode(), mySalt)

def chekPwd(clave, hashPwd):
    if crypt.checkpw(clave.encode(), hashPwd):
        return True
    else:
	    return False

def addLog(mensaje):
    x = date.datetime.now()
    fecha= x.strftime("%d")+'/'+x.strftime('%m')+'/'+x.strftime('%Y')+' '+x.strftime('%H')+':'+x.strftime('%M')+':'+x.strftime('%S')
    archivo=open("log/log_app.log","a")
    archivo.write(fecha+' '+mensaje+"\n")
    archivo.close()
