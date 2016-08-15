#!/usr/bin/env python3
#-*- coding: utf-8 -*-

from math import *
from sympy import *

"""
module::  
     Polynomial
module author::
    Garrido Valencia Alan
    Sánchez Baños Margarito
    Torres Ortiz Luis Miguel
    Zuñiga Hernandez Jonatan
synopsis: 
    Este modulo implementa las operaciones con polinomios
"""


class Polynomial:
    '''
    Linea de documentacion de la clase  Polynomial
    '''
    def __init__(self, variable, grade,*coefficients):
        '''
        Constructor de  Polynomial
        '''
        self.variable=symbols(variable)
        self.expresion=0
        if coefficients:
            for coefficient in coefficients[0]:
                self.expresion+=float(coefficient)*self.variable**grade
                grade-=1
        else:
            for exponente in range(grade,-1,-1):
                coefficient=float(input("Dame el coefficient del termino %s^%d: " % (variable,exponente)))
                self.expresion+=coefficient*self.variable**exponente
        print(self.expresion)

    def pointValue(self,point):
        return self.expresion.evalf(subs={self.variable:point})


    def add(self,pol):
        return self.expresion+pol.expresion

    def sub(self,pol):
        return self.expresion-pol.expresion

    def mult(self,pol):
        return expand(self.expresion*pol.expresion)

    def divi(self,pol):
        return simplify(self.expresion/pol.expresion)

    def differ(self):
        return diff(self.expresion,self.variable)

    def integr(self):
        return integrate(self.expresion,self.variable)

    def integrDef(self,a,b):
        return integrate(self.expresion,(self.variable,a,b))

if __name__ == '__main__':
    grade1=int(input("Dame el grado del primer  Polinomio:"))
    variable1=input("Dame el nombre de la variable independiente: ")[0]
    grade2=int(input("Dame el grado del segundo  Polinomio:"))
    variable2=input("Dame el nombre de la variable independiente: ")[0]
    #instanciamos dos  Polynomials
    pol1= Polynomial(variable1,grade1)
    pol2= Polynomial(variable2,grade2)
    #Evaluamos en un point
    point=float(input("Dame el valor a evaluar para el primer polinomio: "))
    print("Operaciones con  Polinomios")
    print("Valor en %s con %s=%.2f: %.2f" %(pol1.expresion,variable1,point,pol1.pointValue(point)))
    #Hacemos todas las operaciones posiles
    print("Suma de %s con %s = %s "%(pol1.expresion,pol2.expresion,pol1.add(pol2)))
    print("Resta de %s con %s = %s "%(pol1.expresion,pol2.expresion,pol1.sub(pol2)))
    print("Multiplicación de %s con %s = %s "%(pol1.expresion,pol2.expresion,pol1.mult(pol2)))
    print("División de %s con %s = %s "%(pol1.expresion,pol2.expresion,pol1.divi(pol2)))
    #Integral y derivada
    print("Derivada de %s respecto a %s = %s "%(pol1.expresion,pol1.variable,pol1.differ()))
    print("Integral de %s respecto a %s = %s "%(pol2.expresion,pol2.variable,pol2.integr()))
    print("Integral definida de %s de %d a %d = %s "%(pol2.expresion,0,2,pol2.integrDef(0,2)))
