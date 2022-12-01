from tkinter import *
import funciones as util
import usuariosDao as usrDao



def click_save():
    nombreUsuario=txtUserName.get()
    if nombreUsuario.__len__() < 4 & userAbm.isEdit == FALSE:
        lblEstado["text"]="El usuario deve tener 4 caracteres"
        lblEstado["fg"]="red"
        txtUserName.focus()
        return
    email=txtEmail.get()
    if util.check(email) == False & userAbm.isEdit == FALSE:
        lblEstado["text"]="Complete un email valido"
        lblEstado["fg"]="red"
        txtEmail.focus()
        return
    nombre=txtNombre.get()
    if nombre.__len__() < 1:
        lblEstado["text"]="Complete el Nombre"
        lblEstado["fg"]="red"
        txtNombre.focus()
        return
    apellido=txtApellido.get()
    if apellido.__len__() < 1:
        lblEstado["text"]="Complete el Apellido"
        lblEstado["fg"]="red"
        txtApellido.focus()
        return
    clave = txtPassword.get()
    pwdHash=""
    if clave.__len__() < 6:
        lblEstado["text"]="La contraseña debe tener al menos 6 caracteres"
        lblEstado["fg"]="red"
        txtPassword.focus()
        return
    else:
        pwdHash=util.encript(clave)
    apellido=txtApellido.get()
    fecha=""
    if util.validarFecha(txtFechaNacimiento.get()) == False:
        lblEstado["text"]="El formato de Fecha es incorrecto"
        lblEstado["fg"]="red"
        txtFechaNacimiento.focus()
    else:
        fecha=txtFechaNacimiento.get()
    #Guardar en base
    usrDao.createDB()
    respuesta = ""
    if userAbm.isEdit == True:
        respuesta = usrDao.updateDB([nombreUsuario, email, nombre, apellido, pwdHash, fecha, txtDireccion.get()])
    else:
        respuesta = usrDao.insertDB([nombreUsuario, email, nombre, apellido, pwdHash, fecha, txtDireccion.get()])
    if(respuesta == "OK"):
        click_cancel("El usuario se agrego/actualizo !!!")
    else:
        lblEstado["text"]=respuesta
        lblEstado["fg"]="red"
        txtUserName.focus()

def set_text(entry, text):
    entry.delete(0,END)
    entry.insert(0,text)
    return

def searchUser():
    usuario=False
    email = txtEmail.get()
    usuario = txtUserName.get()
    if email.__len__() > 0 & util.check(email):
        usuario=usrDao.getUsuario(email)
    elif usuario.__len__() > 0:
        usuario=usrDao.getUsuario(usuario, "usr")
    else:
        lblEstado["text"]="Ingrese un argumento de busqueda"
        lblEstado["fg"]="red"
        txtUserName.focus()
    print(usuario)
    if usuario:
        set_text(txtUserName, usuario[0])
        set_text(txtEmail, usuario[1])
        set_text(txtNombre, usuario[2])
        set_text(txtApellido, usuario[3])
        set_text(txtPassword, usuario[4])
        set_text(txtFechaNacimiento, usuario[5])
        set_text(txtDireccion, usuario[6])
        txtUserName.config(state="disabled")
        txtEmail.config(state="disabled")
        userAbm.isEdit=True
    else:
         lblEstado["text"]="El Usuario no existe, verifique los datos"
         lblEstado["fg"]="red"
         txtEmail.focus()
         return

def click_cancel(mensaje="Ingreso cancelado", fg="black"):
    if userAbm.isEdit == True:
        userAbm.isEdit = False
        txtUserName.config(state="normal")
        txtEmail.config(state="normal")
    txtUserName.delete(0, END)
    txtEmail.delete(0, END)
    txtNombre.delete(0, END)
    txtApellido.delete(0, END)
    txtPassword.delete(0, END)
    txtFechaNacimiento.delete(0, END)
    txtDireccion.delete(0, END)
    txtUserName.focus()
    lblEstado["text"]=mensaje
    lblEstado["fg"]="black"

userAbm = Tk()
userAbm.title("ABM Usuarios")
userAbm.geometry("450x400")
userAbm.isEdit=FALSE
#----Inicio armado frm-------
lblTitulo=Label(text="ABM de Usuarios")
lblTitulo.config(font=("Arial", 16))
lblTitulo.place(y=10, x=100)
#----- Seccion UserName --------
lblUserName=Label(text="Usuario:")
lblUserName.place(y=40, x=20)
txtUserName = Entry(width=40)
txtUserName.place(y=40, x=100)
#----- Seccion Email --------
lblEmail=Label(text="Email:")
lblEmail.place(y=60, x=20)
txtEmail = Entry(width=40)
txtEmail.place(y=60, x=100)
#----- Seccion Nombre --------
lblNombre=Label(text="Nombre:")
lblNombre.place(y=80, x=20)
txtNombre = Entry(width=40)
txtNombre.place(y=80, x=100)
#----- Seccion Apellido --------
lblApellido=Label(text="Apellido:")
lblApellido.place(y=100, x=20)
txtApellido = Entry(width=40)
txtApellido.place(y=100, x=100)
#----- Seccion Contraseña --------
lblContraseña=Label(text="Contraseña:")
lblContraseña.place(y=120, x=20)
txtPassword = Entry(show="*")
txtPassword.place(y=120, x=100)
#----- Seccion Fecha de Nacimiento --------
lblFechaNacimiento=Label(text="Fecha Nac.:")
lblFechaNacimiento.place(y=140, x=20)
txtFechaNacimiento = Entry(width=20)
txtFechaNacimiento.place(y=140, x=100)
#----- Seccion Direccion --------
lblDireccion=Label(text="Direccion:")
lblDireccion.place(y=160, x=20)
txtDireccion = Entry(width=40)
txtDireccion.place(y=160, x=100)
lblEstado=Label(text="")
lblEstado.config(font=("Arial", 14))
lblEstado.place(y=220, x=50)
btnGuardar=Button(text="Guardar", command=click_save, width=20, bg="green", font=("Arial", 12))
btnGuardar.place(y=270, x=20)
btnCancelar=Button(text="Cancelar", command=click_cancel, width=20, bg="red", font=("Arial", 12))
btnCancelar.place(y=270, x=220)
btnGuardar=Button(text="Buscar", command=searchUser, width=20, bg="#7C9CE2", font=("Arial", 12))
btnGuardar.place(y=310, x=20)
txtUserName.focus()

userAbm.mainloop()