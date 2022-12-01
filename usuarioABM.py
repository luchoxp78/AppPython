from tkinter import *
import funciones as util
import usuariosDao as usrDao

def click_save():
    email=txtEmail.get()
    if util.check(email) == False:
        lblEstado["text"]="Complete un email valido"
        txtEmail.focus()
        return
    nombre=txtNombre.get()
    if nombre.__len__() < 1:
        lblEstado["text"]="Complete el Nombre"
        txtNombre.focus()
        return
    apellido=txtApellido.get()
    if apellido.__len__() < 1:
        lblEstado["text"]="Complete el Apellido"
        txtApellido.focus()
        return
    clave = txtPassword.get()
    pwdHash=""
    if clave.__len__() < 6:
        lblEstado["text"]="La contraseña debe tener al menos 6 caracteres"
        txtPassword.focus()
        return
    else:
        pwdHash=util.encode(clave)
    apellido=txtApellido.get()
    fecha=""
    if util.validarFecha(txtFechaNacimiento.get()):
        lblEstado["text"]="El formato de Fecha es incorrecto"
        txtFechaNacimiento.focus()
    else:
        fecha=txtFechaNacimiento.get()
    #Guardar en base
    usrDao.createDB()
    usrDao.insertDB([email, nombre, apellido, pwdHash, fecha, txtDireccion.get()])
    

def click_cancel():
    txtEmail.delete(0, END)
    txtNombre.delete(0, END)
    txtApellido.delete(0, END)
    txtPassword.delete(0, END)
    txtFechaNacimiento.delete(0, END)
    txtDireccion.delete(0, END)
    txtEmail.focus()
    lblEstado["text"]="Cancelando"
    

userAbm = Tk()
userAbm.title("ABM Usuarios")
userAbm.geometry("450x400")

#----Inicio armado frm-------
miFrame = Frame()
miFrame.pack()
lblTitulo=Label(miFrame, text="ABM de Usuarios")
lblTitulo.grid(row=0, column=0, columnspan=2)
lblTitulo.config(font=("Arial", 16))
#----- Seccion Email --------
lblEmail=Label(miFrame, text="Email:")
lblEmail.grid(row=1, column=0)
lblEmail.config(padx=10, pady=10)
txtEmail = Entry(miFrame, width=40)
txtEmail.grid(pady=5, row=1, column=1)
#----- Seccion Nombre --------
lblNombre=Label(miFrame, text="Nombre:")
lblNombre.grid(row=2, column=0)
lblNombre.config(padx=10, pady=10)
txtNombre = Entry(miFrame, width=40)
txtNombre.grid(pady=5, row=2, column=1)
#----- Seccion Apellido --------
lblApellido=Label(miFrame, text="Apellido:")
lblApellido.grid(row=3, column=0)
lblApellido.config(padx=10, pady=10)
txtApellido = Entry(miFrame, width=40)
txtApellido.grid(pady=5, row=3, column=1)
#----- Seccion Contraseña --------
lblContraseña=Label(miFrame, text="Contraseña:")
lblContraseña.grid(row=4, column=0)
lblContraseña.config(padx=10, pady=10)
txtPassword = Entry(miFrame, width=40, show="*")
txtPassword.grid(pady=5, row=4, column=1)
#----- Seccion Fecha de Nacimiento --------
lblFechaNacimiento=Label(miFrame, text="Fecha Nac.:")
lblFechaNacimiento.grid(row=5, column=0)
lblFechaNacimiento.config(padx=10, pady=10)
txtFechaNacimiento = Entry(miFrame, width=20)
txtFechaNacimiento.grid(padx=1, row=5, column=1)
#----- Seccion Direccion --------
lblDireccion=Label(miFrame, text="Direccion:")
lblDireccion.grid(row=6, column=0)
lblDireccion.config(padx=10, pady=10)
txtDireccion = Entry(miFrame, width=40)
txtDireccion.grid(pady=5, row=6, column=1)
lblEstado=Label(miFrame, text="")
lblEstado.grid(padx=5, pady=5, row=7, column=0, columnspan=2)
btnGuardar=Button(miFrame, text="Guardar", command=click_save, width=20)
btnCancelar=Button(miFrame, text="Cancelar", command=click_cancel, width=20)
btnGuardar.grid(padx=5, row=8, column=0)
btnCancelar.grid(padx=20, row=8, column=1)


userAbm.mainloop()