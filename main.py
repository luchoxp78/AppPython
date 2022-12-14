from tkinter import * 
from tkinter import simpledialog
import os
import usuariosDao as usrDao
import funciones.funciones as util
import funciones.calculo as calc

def openAbmUsuario():
    os.system('python ./usuarioABM.py')

def test():
    lblImc["text"]=""
    lblImc["bg"]='SystemButtonFace'
    altura=simpledialog.askstring("Calculo de Masa Muscular", "Ingrese su altura metros ?", parent=root)
    peso=simpledialog.askstring("Calculo de Masa Muscular", "Ingrese su peso en kilos ?", parent=root)
    if altura is not None and peso is not None:
        respuesta=calc.calculoIMC(altura, peso)
        lista=respuesta.split(";")
        if lista[0] == "0":
            lblImc["test"]=lista[1]
            lblImc["fg"]="red"
        else:
            lblImc["text"]=lista[1]
            lblImc.config(fg=lista[0], bg="#707B7C")
    
    
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
btnCancelar=Button(text="Calcular IMC", command=test, width=20, bg="#7C9CE2", font=("Arial", 12))
btnCancelar.place(y=80, x=20)
lblImc=Label(text="", font=("Arial", 16), fg="blue")
lblImc.place(y=120, x=20)

root.mainloop()