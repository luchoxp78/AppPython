from tkinter import * 
import os
import usuariosDao as usrDao
import funciones.funciones as util

def openAbmUsuario():
    #root.destroy()
    os.system('python ./usuarioABM.py')

root = Tk()  
root.title("Formulario Principal")
root.geometry("450x400")
root.resizable(0, 0)
wtotal = root.winfo_screenwidth()
htotal = root.winfo_screenheight()
wventana = 450
hventana = 400
pwidth = round(wtotal/2-wventana/2)
pheight = round(htotal/2-hventana/2)
root.geometry(str(wventana)+"x"+str(hventana)+"+"+str(pwidth)+"+"+str(pheight)) 
btnGuardar=Button(text="ABM Usuario", command=openAbmUsuario, width=20, bg="#7C9CE2", font=("Arial", 12))
btnGuardar.place(y=40, x=20)
btnCancelar=Button(text="Funcion Sin Impl.", width=20, bg="#7C9CE2", font=("Arial", 12))
btnCancelar.place(y=80, x=20)

    

root.mainloop()