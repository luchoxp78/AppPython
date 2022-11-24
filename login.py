from tkinter import *
import usuariosDao as usrDao
import funciones as util
import os


def click_login():
    email=txtEmail.get()
    if util.check(email):
        lblEstado["text"]="Complete un email valido"
        txtEmail.focus()
        return
    clave=txtPassword.get()
    if clave.__len__() < 6:
        lblEstado["text"]="La contraseña debe tener al menos 6 caracteres"
        txtPassword.focus()
        return
    usuario=usrDao.getUsuario(email)
    print(usuario)
    if usuario:
        if util.chekPwd(clave, usuario[3]):
            print("HOLA USUARIO")
            root.destroy()
            
            os.system("python -u ./ususarioABM.py")
        else:
             lblEstado["text"]="La contraseña ingresada es incorrecta"
    else:
         lblEstado["text"]="El Usuario no existe, verifique los datos"
         txtEmail.focus()
         return

def click_cancel():
    txtEmail.delete(0, END)
    txtPassword.delete(0, END)
    txtEmail.focus()
    lblEstado["text"]="Cancelando"

root = Tk()
root.title("Formulario de INgreso")
root.geometry("450x200")
#----Inicio armado frm-------
miFrame = Frame()
miFrame.pack()
lblTitulo=Label(miFrame, text="Ingreso")
lblTitulo.grid(row=0, column=0, columnspan=2)
lblTitulo.config(font=("Arial", 16))
#----- Seccion Email --------
lblEmail=Label(miFrame, text="Email:")
lblEmail.grid(row=1, column=0)
lblEmail.config(padx=10, pady=10)
txtEmail = Entry(miFrame, width=40)
txtEmail.grid(pady=5, row=1, column=1)
#----- Seccion Contraseña --------
lblContraseña=Label(miFrame, text="Contraseña:")
lblContraseña.grid(row=4, column=0)
lblContraseña.config(padx=10, pady=10)
txtPassword = Entry(miFrame, width=40, show="*")
txtPassword.grid(pady=5, row=4, column=1)
lblEstado=Label(miFrame, text="")
lblEstado.grid(padx=5, pady=5, row=7, column=0, columnspan=2)
btnGuardar=Button(miFrame, text="Ingresar", command=click_login, width=20)
btnCancelar=Button(miFrame, text="Cancelar", command=click_cancel, width=20)
btnGuardar.grid(padx=5, row=8, column=0)
btnCancelar.grid(padx=20, row=8, column=1)

root.mainloop()
