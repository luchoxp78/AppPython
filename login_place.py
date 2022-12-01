from tkinter import *
import usuariosDao as usrDao
import funciones as util
import os


def click_login():
    email=txtEmail.get()
    if email.count("@") == 1:
        if util.check(email) == False:
            lblEstado["text"]="Complete un email valido"
            lblEstado["fg"]="red"
            txtEmail.focus()
            return
    else:
        if email.__len__() < 4:
            lblEstado["text"]="El usuario debe tener al menos 4 caracteres"
            lblEstado["fg"]="red"
            txtEmail.focus()
            return
    clave=txtPassword.get()
    if clave.__len__() < 6:
        lblEstado["text"]="La contraseña debe tener al menos 6 caracteres"
        lblEstado["fg"]="red"
        txtPassword.focus()
        return
    usuario=False
    if email.count("@") == 1:
        usuario=usrDao.getUsuario(email)
    else:
        usuario=usrDao.getUsuario(email, "usr")
    print(usuario)
    if usuario:
        if util.chekPwd(clave, usuario[4]):
            print("HOLA USUARIO")
            loggin.destroy()
            os.system('python ./main.py')
        else:
             lblEstado["text"]="La contraseña ingresada es incorrecta"
             lblEstado["fg"]="red"
    else:
         lblEstado["text"]="El Usuario no existe, verifique los datos"
         lblEstado["fg"]="red"
         txtEmail.focus()
         return

def click_cancel():
    txtEmail.delete(0, END)
    txtPassword.delete(0, END)
    txtEmail.focus()
    lblEstado["text"]="Ingreso cancelado"
    lblEstado["fg"]="black"

loggin = Tk()
loggin.title("Formulario de Ingreso")
loggin.geometry("450x200")
#----Inicio armado frm-------
lblTitulo=Label(text="Ingreso")
lblTitulo.place(y=10, x=200)
lblTitulo.config(font=("Arial", 16))
#----- Seccion Email --------
lblEmail=Label(text="Usuario/Email:")
lblEmail.config(justify='right')
lblEmail.place(y=45, x=20)
txtEmail = Entry(width=40)
txtEmail.place(y=45, x=110)
#----- Seccion Contraseña --------
lblContraseña=Label(text="Contraseña:")
lblContraseña.config(justify='right')
lblContraseña.place(y=85, x=20)
txtPassword = Entry(width=40, show="*")
txtPassword.place(y=85, x=110)
lblEstado=Label(text="")
lblEstado.config(font=("Arial", 14))
lblEstado.place(y=130, x=30)
btnGuardar=Button(text="Ingresar", command=click_login, width=20, bg="green", font=("Arial", 12))
btnCancelar=Button(text="Cancelar", command=click_cancel, width=20, bg="red", font=("Arial", 12))
btnGuardar.place(y=160, x=20)
btnCancelar.place(y=160, x=220)
txtEmail.focus()

loggin.mainloop()
