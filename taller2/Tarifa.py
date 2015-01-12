'''
Created on Jan 11, 2015

@author: enrique
'''

from datetime import datetime

def VerificarFecha(fecha):
    return 0

def VerificarReserva(fi,ff):
    dif = ff - fi
    if dif.day == 0:
        if dif.hour == 0:
            if dif.minute >= 15:
                return True
            return False
        return True
    elif dif.day < 3:
        return True
    elif dif.day == 3:
        if dif.hour == 0:
            if dif.minute == 0:
                return True
            return False
        return False
    return False

def EsNoche(hora):
    if 6 <= hora.hour < 18:
        return False
    elif hora.hour == 18:
        if hora.minute > 0:
            return True
        return False
    return True

def CalcularTarifa(fi,ff,t1,t2):
    dif = ff - fi
    hora = dif.hour
    if dif.minute != 0:
        hora+=1
    if dif.days == 0:
        if (EsNoche(fi) == False) & (EsNoche(ff) == False):
            tarifa = hora*t1
        elif (EsNoche(fi) == True) & (EsNoche(fi) == True):
            tarifa = hora*t2
        elif (EsNoche(fi) == False) & (EsNoche(fi) == True):
            hora2 = ff.hour - 18
            if hora2.minute != 0:
                hora2 += 1
            hora -= hora2
            tarifa = hora*t1 + hora2*max(t1,t2)
        elif (EsNoche(fi) == True) & (EsNoche(fi) == False):
            hora2 = ff.hour - 6
            if hora2.minute != 0:
                hora2 += 1
            hora -= hora2
            tarifa = hora*t2 + hora2*max(t1,t2)
    return tarifa

if __name__ == '__main__':
    
    formato = '%d/%m/%Y %H:%M'
    
    fi = raw_input("Introduzca fecha y hora del inicio de la reservacion (dd/mm/aaaa hh:mm): ")
    fi = str(fi)
    fi = datetime.strptime(fi, formato)
    ff = raw_input("Introduzca fecha y hora de la finalizacion de la reservacion (dd/mm/aaaa hh:mm): ")
    ff = str(ff)
    ff = datetime.strptime(ff, formato)
    assert(VerificarReserva(fi, ff))
    td = input("Introduzca tasa diurna: ")
    assert(td > 0)
    tn = input("Introduzca tasa nocturna: ")
    assert(tn > 0)