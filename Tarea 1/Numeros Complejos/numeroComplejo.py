#!/usr/bin/env python3
#-*- coding: utf-8 -*-

from math import *
from cmath import polar

"""
module::  
    numeroComplejo
module authors::
    Garrido Valencia Alan
    Sánchez Baños Margarito
    Torres Ortiz Luis Miguel
    Zuñiga Hernandez Jonatan
synopsis: 
    Este modulo implementa las clases para operaciones con 
    numeros complejos.
"""

class numeroComplejo():
    def __init__(self,a,b):
        self.cplx=complex(a,b)

    def __str__(self):
        return "{:.2f}".format(self.cplx)

    def modulo(self):
        '''
            mod= sqrt(cplx.real^2+cplx.imag^2)
        '''
        return abs(self.cplx)
        #return abs(self.cplx)

    def angulo(self):
        '''
            ang= atan(cplx.imag/cplx.real)
            ang= polar(cplx)[1] en radianes
            
        '''
        return atan2(self.cplx.imag,self.cplx.real)

    def suma(self,cplx):
        return self.cplx+cplx.cplx

    def resta(self,cplx):
        return self.cplx-cplx.cplx

    def multiplica(self,cplx):
        return self.cplx*cplx.cplx

    def divide(self,cplx):
        return self.cplx/cplx.cplx

    def potencia(self,grado):
        return self.cplx*cplx.cplx


        

if __name__ == '__main__':
    #Operaciones con complejos
    cplx1=numeroComplejo(1,2)
    cplx2=numeroComplejo(0,-1)

    print("Operaciones con Complejos")
    print("Suma de %s con %s = %s" %(cplx1,cplx2,cplx1.suma(cplx2)))
    print("Resta de %s con %s = %s" %(cplx1,cplx2,cplx1.resta(cplx2)))
    print("Multiplicacion de %s con %s = %s" %(cplx1,cplx2,cplx1.multiplica(cplx2)))
    print("Division de %s con %s = %s" %(cplx1,cplx2,cplx1.divide(cplx2)))
    print("Módulo de %s = %s" %(cplx1,cplx1.modulo()))
    print("Ángulo de %s = %s" %(cplx2,cplx2.angulo()))

