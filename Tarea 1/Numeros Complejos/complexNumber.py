#!/usr/bin/env python3
#-*- coding: utf-8 -*-

from math import *
from cmath import polar

"""
module::  
    complexNumber
module authors::
    Garrido Valencia Alan
    Sánchez Baños Margarito
    Torres Ortiz Luis Miguel
    Zuñiga Hernandez Jonatan
synopsis: 
    Este mod implementa las clases para operaciones con 
    numeros complejos.
"""

class complexNumber():
    def __init__(self,a,b):
        self.cplx=complex(a,b)

    def __str__(self):
        return "{:.2f}".format(self.cplx)

    def mod(self):
        '''
            mod= sqrt(cplx.real^2+cplx.imag^2)
        '''
        return abs(self.cplx)
        #return abs(self.cplx)

    def angle(self):
        '''
            ang= atan(cplx.imag/cplx.real)
            ang= polar(cplx)[1] en radianes
            
        '''
        return atan2(self.cplx.imag,self.cplx.real)

    def add(self,cplx):
        return self.cplx+cplx.cplx

    def sub(self,cplx):
        return self.cplx-cplx.cplx

    def mult(self,cplx):
        return self.cplx*cplx.cplx

    def divi(self,cplx):
        return self.cplx/cplx.cplx

    def pot(self,grado):
        return self.cplx**grado


        

if __name__ == '__main__':
    #Operaciones con complejos
    cplx1=complexNumber(1,2)
    cplx2=complexNumber(0,-1)

    print("Operaciones con Complejos")
    print("Suma de %s con %s = %s" %(cplx1,cplx2,cplx1.add(cplx2)))
    print("Resta de %s con %s = %s" %(cplx1,cplx2,cplx1.sub(cplx2)))
    print("Multiplicacion de %s con %s = %s" %(cplx1,cplx2,cplx1.mult(cplx2)))
    print("Division de %s con %s = %s" %(cplx1,cplx2,cplx1.divi(cplx2)))
    print("Potencia de %s ^3 = %s" %(cplx1,cplx1.pot(3)))
    print("Módulo de %s = %s" %(cplx1,cplx1.mod()))
    print("Ángulo de %s = %s" %(cplx1,cplx1.angle()))

