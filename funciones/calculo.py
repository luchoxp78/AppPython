from datetime import datetime

def calculoEdad(dia,mes,ano):
    dia=int(dia)
    mes=int(mes)
    ano=int(ano)
    d=datetime.now()
    anoActual=d.year
    mesActual=d.month
    diaActual=d.day
    if mes==mesActual and dia>diaActual:
        edad=anoActual-ano-1
    elif mes>mesActual:
        edad=anoActual-ano-1
    else:
        edad=anoActual-ano
    return str(edad)

def calculoIMC(alturaE, pesoE):
    peso=pesoE.replace(",", ".")
    altura=alturaE.replace(",", ".")
    mensaje=""
    try:
        imc=float(peso)/float(altura)**2
        imc=round(imc, 2)
        if imc>18 and imc<=25:
            mensaje="green"
        elif imc>25 and imc<=30:
            mensaje="yellow"
        else:
            mensaje="red"
        mensaje=mensaje + f";Su indice de masa corporal es {imc}"
        return mensaje
    except:
        mensaje="0;Solo se aceptan numeros, intente nuevamente"
        return mensaje