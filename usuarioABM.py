from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
import funciones.funciones as util
import funciones.calculo as calc
import usuariosDao as usrDao

def click_save():
    nombreUsuario=txtUserName.get()
    if nombreUsuario.__len__() < 4 & userAbm.isEdit == FALSE:
        messagebox.showwarning(title="Loggin", message="El usuario deve tener 4 caracteres")
        txtUserName.focus()
        return
    email=txtEmail.get()
    if util.check(email) == False & userAbm.isEdit == FALSE:
        messagebox.showwarning(title="Loggin", message="Complete un email valido")
        txtEmail.focus()
        return
    nombre=txtNombre.get()
    if nombre.__len__() < 1:
        messagebox.showwarning(title="Loggin", message="Complete el Nombre")
        txtNombre.focus()
        return
    apellido=txtApellido.get()
    if apellido.__len__() < 1:
        messagebox.showwarning(title="Loggin", message="Complete el Apellido")
        txtApellido.focus()
        return
    clave = txtPassword.get()
    pwdHash=""
    if clave.__len__() < 6:
        messagebox.showwarning(title="Loggin", message="La contraseña debe tener al menos 6 caracteres")
        txtPassword.focus()
        return
    else:
        pwdHash=util.encript(clave)
    apellido=txtApellido.get()
    fecha=""
    if util.validarFecha(txtFechaNacimiento.get()) == False:
        messagebox.showwarning(title="Loggin", message="El formato de Fecha es incorrecto")
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
        messagebox.showinfo(title="Loggin", message="El usuario se agrego/actualizo !!!")
        click_cancel()
    else:
        messagebox.showerror(title="Loggin", message=respuesta)
        txtUserName.focus()

def set_text(entry, text):
    entry.delete(0,END)
    entry.insert(0,text)
    return

def fechaFocusOut(event):
    fecha=""
    if util.validarFecha(txtFechaNacimiento.get()) == False:
        messagebox.showwarning(title="Loggin", message="El formato de Fecha es incorrecto")
        set_text(txtFechaNacimiento, "")
        txtFechaNacimiento.focus()
    else:
        fecha=txtFechaNacimiento.get()
        lista=fecha.split("/")
        lblEdad["text"]=calc.calculoEdad(lista[0], lista[1], lista[2])

def searchUser():
    usuario=False
    email = txtEmail.get()
    usuario = txtUserName.get()
    if email.__len__() > 0 & util.check(email):
        usuario=usrDao.getUsuario(email)
    elif usuario.__len__() > 0:
        usuario=usrDao.getUsuario(usuario, "usr")
    else:
        messagebox.showwarning(title="Loggin", message="Ingrese un argumento de busqueda")
        txtUserName.focus()
        return
    if usuario:
        set_text(txtUserName, usuario[0])
        set_text(txtEmail, usuario[1])
        set_text(txtNombre, usuario[2])
        set_text(txtApellido, usuario[3])
        set_text(txtPassword, usuario[4])
        set_text(txtFechaNacimiento, usuario[5])
        set_text(txtDireccion, usuario[6])
        fecha=txtFechaNacimiento.get()
        lista=fecha.split("/")
        lblEdad["text"]=calc.calculoEdad(lista[0], lista[1], lista[2])
        txtUserName.config(state="disabled")
        txtEmail.config(state="disabled")
        userAbm.isEdit=True
    else:
        messagebox.showwarning(title="Loggin", message="El Usuario no existe, verifique los datos")
        txtEmail.focus()
        return

def click_cancel():
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
    lblEdad["text"]=""
    txtUserName.focus()

userAbm = Tk()
userAbm.title("ABM Usuarios")
userAbm.geometry("450x400")
userAbm.resizable(0, 0)
wtotal = userAbm.winfo_screenwidth()
htotal = userAbm.winfo_screenheight()
wventana = 450
hventana = 400
pwidth = round(wtotal/2-wventana/2)
pheight = round(htotal/2-hventana/2)
userAbm.geometry(str(wventana)+"x"+str(hventana)+"+"+str(pwidth)+"+"+str(pheight))
userAbm.isEdit=FALSE
#----Label on imagen --------
imagen=Image.open("Imagenes/users-group-icon.png")
img_resize=imagen.resize((100, 57))
img = ImageTk.PhotoImage(imagen)
lblImagen=Label(image=img)
lblImagen.place(y=10, x=10)
#----Inicio armado frm-------
lblTitulo=Label(text="ABM de Usuarios")
lblTitulo.config(font=("Arial", 16))
lblTitulo.place(y=10, x=100)
#----- Seccion UserName --------
lblUserName=Label(text="Usuario:")
lblUserName.place(y=70, x=20)
txtUserName = Entry(width=40)
txtUserName.place(y=70, x=100)
#----- Seccion Email --------
lblEmail=Label(text="Email:")
lblEmail.place(y=100, x=20)
txtEmail = Entry(width=40)
txtEmail.place(y=100, x=100)
#----- Seccion Nombre --------
lblNombre=Label(text="Nombre:")
lblNombre.place(y=130, x=20)
txtNombre = Entry(width=40)
txtNombre.place(y=130, x=100)
#----- Seccion Apellido --------
lblApellido=Label(text="Apellido:")
lblApellido.place(y=160, x=20)
txtApellido = Entry(width=40)
txtApellido.place(y=160, x=100)
#----- Seccion Contraseña --------
lblContraseña=Label(text="Contraseña:")
lblContraseña.place(y=190, x=20)
txtPassword = Entry(show="*")
txtPassword.place(y=190, x=100)
#----- Seccion Fecha de Nacimiento --------
lblFechaNacimiento=Label(text="Fecha Nac.:")
lblFechaNacimiento.place(y=220, x=20)
txtFechaNacimiento = Entry(width=20)
txtFechaNacimiento.place(y=220, x=100)
txtFechaNacimiento.bind("<FocusOut>", fechaFocusOut)
lblEdad=Label(text="", font=("Arial", 12), fg="blue")
lblEdad.place(y=220, x=230)
#----- Seccion Direccion --------
lblDireccion=Label(text="Direccion:")
lblDireccion.place(y=250, x=20)
txtDireccion = Entry(width=40)
txtDireccion.place(y=250, x=100)
btnGuardar=Button(text="Guardar", command=click_save, width=15, bg="#5DDA59", font=("Arial", 12))
btnGuardar.place(y=310, x=40)
btnBuscar=Button(text="Buscar", command=searchUser, width=15, bg="#7C9CE2", font=("Arial", 12))
btnBuscar.place(y=310, x=220)
btnCancelar=Button(text="Cancelar", command=click_cancel, width=15, bg="#EC4B32", font=("Arial", 12))
btnCancelar.place(y=350, x=40)

txtUserName.focus()

userAbm.mainloop()