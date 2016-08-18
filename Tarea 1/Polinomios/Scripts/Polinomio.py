#!/usr/bin/env python3
#-*- coding: utf-8 -*-

from sympy import *

"""
:platform: Unix, Windows
synopsis:Este modulo implementa las operaciones con polinomios
.. module:: Polinomio
.. module author::
    Garrido Valencia Alan
    Sánchez Baños Margarito
    Torres Ortiz Luis Miguel
    Zuñiga Hernandez Jonatan
"""


class Polynomial:
    '''
        Esta clase implementa un polinomio de las con las siguientes características.
        Atributos:
           - variable: La variable independiente del polinomio
           - expresion: La expresión matemática que lo representa inicializado en cero
        Métodos:
           - add: Suma de polinomios
           - sub: Resta de polinomios
           - multi: Multiplicación de polinomios
           - divi: División de polinomios
           - integr: Integrar un polinomio
           - diff: Derivar un polinomio
           - integrDef: Integración definida

        Se puede usar de la siguiente manera:
            >>> import Polinomio as P
            >>> pol1=P.Polynomial('x',2)
            Dame el coefficient del termino x^2: 1
            Dame el coefficient del termino x^1: 4
            Dame el coefficient del termino x^0: 4
            1.0*x**2 + 4.0*x + 4.0
            #También se puede pasar una lista:
            >>> pol2=P.Polynomial('x',2,[1,4,4])
            1.0*x**2 + 4.0*x + 4.0
    '''
    def __init__(self, variable, grade,*coefficients):
        '''
           Constructor de la clase Polynomial puede instanciar de dos maneras diferentes:
            -Se pasan como parámetros el símbolo que se va a usar como variable y el grado
            -Se pasan los datos anteriores y una lista con los coeficientes
            :param variable: Símbolo que se usara como variable para el polinomio.
            :type variable: str.
            :param grade: Grado del exponente mayor del polinomio.
            :type grade: int.
            :param coefficients: Lista con los coeficientes.
            :type coefficients: list.
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
        """
            Evalua un punto en la expresíon del polinomio

            :param point: Punto a evaluar en la expresión del polinomio.
            :type point: float.
            :returns: float-- El resultado de evaluar la expresión.
        """
        return self.expresion.evalf(subs={self.variable:point})


    def add(self,pol):
        """
            Suma las expresiones matemáticas de dos polinomios regresando uno nuevo

            :param pol: Polinomio a que se sumará con el que invoca el método.
            :type pol: Obj Polynomial.
            :returns: Obj Polynomial-- El polinomio resultante.
        """
        return self.expresion+pol.expresion

    def sub(self,pol):
        """
            Resta la expresión del polinomio que ejecuta el método entre la del parámetro

            :param pol: Polinomio a que se sumará con el que invoca el método.
            :type pol: Obj Polynomial.
            :returns: Obj Polynomial-- El polinomio resultante.
        """
        return self.expresion-pol.expresion

    def mult(self,pol):
        """
            Multiplica las expresiones matemáticas de dos polinomios regresando uno nuevo

            :param pol: Polinomio a que se multiplicará con el que invoca el método.
            :type pol: Obj Polynomial.
            :returns: Obj Polynomial-- El polinomio resultante.
        """
        return expand(self.expresion*pol.expresion)

    def divi(self,pol):
        """
            Divide la expresión del polinomio que ejecuta el método entre la del parámetro

            :param pol: Polinomio a que se dividirá con el que invoca el método.
            :type pol: Obj Polynomial.
            :returns: Obj Polynomial-- El polinomio resultante.
        """
        return simplify(self.expresion/pol.expresion)

    def differ(self):
        """
            Deriva la expresión del polinomio con respecto a su variable independiente

            :returns: Obj Polynomial-- El polinomio resultante.
        """
        return diff(self.expresion,self.variable)

    def integr(self):
        """
            Integra la expresión del polinomio con respecto a su variable independiente

            :returns: Obj Polynomial-- El polinomio resultante.
        """
        return integrate(self.expresion,self.variable)

    def integrDef(self,a,b):
        """
            Integra la expresión del polinomio con respecto a su variable independiente en un rango definido
            
            :param a: Extremo de integración inferior.
            :type a: float.
            :param a: Extremo de integración superior.
            :type a: float.
            :returns: float-- El valor del área debajo de la curva que representa el polinomio.
        """
        return integrate(self.expresion,(self.variable,a,b))

if __name__ == '__main__':
    #Si el script se interpreta directamente puede probar directamente todos los métodos
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
