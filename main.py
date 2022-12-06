from tkinter import * 
import os
import usuariosDao as usrDao
import funciones as util

def openAbmUsuario():
    #root.destroy()
    os.system('python ./usuarioABM_place.py')

root = Tk()  
root.title("Formulario Principal")
root.geometry("450x400")  
btnGuardar=Button(text="ABM Usuario", command=openAbmUsuario, width=20, bg="#7C9CE2", font=("Arial", 12))
btnGuardar.place(y=40, x=20)
btnCancelar=Button(text="Otra Funcion", width=20, bg="#7C9CE2", font=("Arial", 12))
btnCancelar.place(y=80, x=20)

    

root.mainloop()