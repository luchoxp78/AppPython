from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
import usuariosDao as usrDao
import funciones as util
import os


def click_login():
    email=txtEmail.get()
    if email.count("@") == 1:
        if util.check(email) == False:
            messagebox.showwarning(title="Loggin", message="Ingrese un email valido")
            txtEmail.focus()
            return
    else:
        if email.__len__() < 4:
            messagebox.showwarning(title="Loggin", message="El usuario debe tener al menos 4 caracteres")
            txtEmail.focus()
            return
    clave=txtPassword.get()
    if clave.__len__() < 6:
        messagebox.showwarning(title="Loggin", message="La contraseña debe tener al menos 6 caracteres")
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
            loggin.destroy()
            os.system('python ./main.py')
        else:
            messagebox.showwarning(title="Loggin", message="La contraseña ingresada es incorrecta")
    else:
        messagebox.showwarning(title="Loggin", message="El usuario no existe, verifique los datos")
        txtEmail.focus()
        click_cancel()
        return

def click_cancel():
    txtEmail.delete(0, END)
    txtPassword.delete(0, END)
    txtEmail.focus()

loggin = Tk()
loggin.title("Formulario de Ingreso")
loggin.geometry("450x200")
loggin.resizable(0, 0)
wtotal = loggin.winfo_screenwidth()
htotal = loggin.winfo_screenheight()
wventana = 450
hventana = 200
pwidth = round(wtotal/2-wventana/2)
pheight = round(htotal/2-hventana/2)
loggin.geometry(str(wventana)+"x"+str(hventana)+"+"+str(pwidth)+"+"+str(pheight))

#----Label on imagen --------
imagen=Image.open("Imagenes/user-login-icon.png")
img_resize=imagen.resize((106, 121))
img = ImageTk.PhotoImage(img_resize)
lblImagen=Label(image=img)
lblImagen.place(y=10, x=330)
#----Inicio armado frm-------
lblTitulo=Label(text="Ingreso")
lblTitulo.place(y=10, x=200)
lblTitulo.config(font=("Arial", 16))
#----- Seccion Email --------
lblEmail=Label(text="Usuario/Email:")
lblEmail.config(justify='right')
lblEmail.place(y=45, x=20)
txtEmail = Entry(width=30)
txtEmail.place(y=45, x=110)
#----- Seccion Contraseña --------
lblContraseña=Label(text="Contraseña:",justify="center")
lblContraseña.place(y=85, x=20)
txtPassword = Entry(width=30, show="*")
txtPassword.place(y=85, x=110)
btnGuardar=Button(text="Ingresar", command=click_login, width=20, bg="#5DDA59", font=("Arial", 12))
btnCancelar=Button(text="Cancelar", command=click_cancel, width=20, bg="#EC4B32", font=("Arial", 12))
btnGuardar.place(y=160, x=20)
btnCancelar.place(y=160, x=220)
txtEmail.focus()

loggin.mainloop()
