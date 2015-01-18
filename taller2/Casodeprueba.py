'''
Created on Jan 18, 2015

@author: maria-esthervidal
'''

import unittest
from Tarifa import *
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

class TestFecha(unittest.TestCase):
    
    def testresv(self):
        
        formato = '%d/%m/%Y %H:%M'
        
        fi = datetime.strptime("01/01/2015 17:45", formato)
        ff = datetime.strptime("01/01/2015 18:00", formato)
        tarifa = CalcularTarifa(fi, ff, 50, 100)
        self.assertEquals(tarifa, 50)
        
        fi = datetime.strptime("01/01/2015 17:45", formato)
        ff = datetime.strptime("01/01/2015 18:01", formato)
        tarifa = CalcularTarifa(fi, ff, 50, 100)
        self.assertEquals(tarifa, 100)
        
        fi = datetime.strptime("01/01/2015 06:00", formato)
        ff = datetime.strptime("01/01/2015 18:00", formato)
        tarifa = CalcularTarifa(fi, ff, 50, 100)
        self.assertEquals(tarifa, 600)
        
        fi = datetime.strptime("01/01/2015 06:00", formato)
        ff = datetime.strptime("02/01/2015 06:00", formato)
        tarifa = CalcularTarifa(fi, ff, 50, 100)
        self.assertEquals(tarifa, 1800)
        
        fi = datetime.strptime("01/01/2015 17:00", formato)
        ff = datetime.strptime("01/01/2015 18:01", formato)
        tarifa = CalcularTarifa(fi, ff, 50, 100)
        self.assertEquals(tarifa, 150)
        
        fi = datetime.strptime("01/01/2015 18:01", formato)
        ff = datetime.strptime("02/01/2015 05:59", formato)
        tarifa = CalcularTarifa(fi, ff, 50, 100)
        self.assertEquals(tarifa, 1200)
        
        fi = datetime.strptime("01/01/2015 18:00", formato)
        ff = datetime.strptime("04/01/2015 18:00", formato)
        tarifa = CalcularTarifa(fi, ff, 50, 100)
        self.assertEquals(tarifa, 5400)
        
        fi = datetime.strptime("01/01/2015 06:00", formato)
        ff = datetime.strptime("04/01/2015 06:00", formato)
        tarifa = CalcularTarifa(fi, ff, 50, 100)
        self.assertEquals(tarifa, 5400)
        
        fi = datetime.strptime("01/01/2015 18:00", formato)
        ff = datetime.strptime("04/01/2015 06:00", formato)
        tarifa = CalcularTarifa(fi, ff, 50, 100)
        self.assertEquals(tarifa, 4800)
        