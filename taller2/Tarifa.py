'''
Created on Jan 11, 2015

@author: enrique
'''

from datetime import datetime, timedelta
from decimal import Decimal

def Eldiatermino(fecha,hora):
    if 0 <= fecha.hour + hora <=12:
        return True
    return False

def VerificarReserva(fi,ff):
    dif = ff - fi
    if dif.days == 0:
        if dif.seconds//3600 == 0:
            if dif.seconds%3600 >= 15:
                return True
            return False
        return True
    elif dif.days < 3:
        return True
    elif dif.days == 3:
        if dif.seconds//3600 == 0:
            if (dif.seconds%3600)*60 == 0:
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
    tarifa = 0
    dif = ff - fi
    hora = dif.seconds//3600
    if dif.seconds%3600 != 0:
        hora+=1
    if dif.days == 0:
        if (EsNoche(fi) == False) & (EsNoche(ff) == False):
            if (ff.hour == 6) & (fi.hour > ff.hour):
                tarifa = hora*t2
            else:
                tarifa = hora*t1
        elif (EsNoche(fi) == True) & (EsNoche(ff) == True):
            tarifa = hora*t2
        elif (EsNoche(fi) == False) & (EsNoche(ff) == True):
            hora2 = ff.hour - 18
            if ff.minute != 0:
                hora2 += 1
            hora -= hora2
            hora2 -= 1
            tarifa = hora*t1 + max(t1,t2) + hora2*t2
        elif (EsNoche(fi) == True) & (EsNoche(ff) == False):
            hora2 = ff.hour - 6
            if ff.minute != 0:
                hora2 += 1
            hora -= hora2
            hora2 -= 1
            tarifa = hora*t2 + max(t1,t2) + hora2*t1
    elif dif.days != 0:
            if (EsNoche(fi) == False) & (fi.hour != 18):
                hora3 = 18 - fi.hour
                hora4 = hora3
                if fi.minute != 0:
                    tarifa += max(t1,t2)
                    hora4 +=1
                if Eldiatermino(fi, hora4):
                    fi = fi + timedelta(hours = hora4)
                    fi = fi + timedelta(days = 1)
                else:
                    fi = fi + timedelta(hours = hora4)
                tarifa += hora3*t1 + CalcularTarifa(fi, ff, t1, t2)
            else:
                hora3 = fi.hour - 6
                hora4 = hora3 
                if fi.minute != 0:
                    tarifa += max(t1,t2) 
                    hora4 +=1
                if Eldiatermino(fi, hora4):
                    fi = fi + timedelta(hours = hora4)
                    fi = fi + timedelta(days = 1)
                else:
                    fi = fi + timedelta(hours = hora4)
                tarifa += hora3*t2 + CalcularTarifa(fi, ff, t1, t2) 
    tarifa = Decimal(tarifa)
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
    td = Decimal(td)
    assert(td > 0)
    tn = input("Introduzca tasa nocturna: ")
    tn = Decimal(tn)
    assert(tn > 0)
    tarifa = CalcularTarifa(fi, ff, td, tn)
    tarifa = Decimal(tarifa)
    print ("Su tarifa es: %d" %tarifa)