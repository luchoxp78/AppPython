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