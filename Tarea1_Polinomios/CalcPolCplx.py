#!/usr/bin/env python3
#-*- coding: utf-8 -*-

"""
.. module:: CalcPolCplx   
.. moduleauthor:: Garrido Valencia Alan
:synopsis: Este modulo implementa las clases para operaciones con polinomios y complejos.

"""

from math import *
from cmath import polar
from sympy import *


class CalcPol:
	'''
	Linea de documentacion de la clase CalcPol
	'''
	def __init__(self, variable, grado,*coeficientes):
		'''
		Constructor de CalcPol
		'''
		self.variable=symbols(variable)
		self.expresion=0
		if coeficientes:
			for coeficiente in coeficientes[0]:
				self.expresion+=float(coeficiente)*self.variable**grado
				grado-=1
		else:
			for exponente in range(grado,-1,-1):
				coeficiente=float(input("Dame el coeficiente del termino %s^%d: " % (variable,exponente)))
				self.expresion+=coeficiente*self.variable**exponente
		print(self.expresion)

	def valorPunto(self,punto):
		return self.expresion.evalf(subs={self.variable:punto})


	def sumaPol(self,pol):
		return self.expresion+pol.expresion

	def restaPol(self,pol):
		return self.expresion-pol.expresion

	def multiPol(self,pol):
		return expand(self.expresion*pol.expresion)

	def diviPol(self,pol):
		return expand(self.expresion/pol.expresion)

	def derivaPol(self):
		return diff(self.expresion,self.variable)

	def integraPol(self):
		return integrate(self.expresion,self.variable)

class CalcCplx():
	"""
	docstring for CalcCplx
	"""
	def __init__(self,a,b):
		self.cplx=complex(a,b)

	def __str__(self):
		return "{:.2f}".format(self.cplx)

	def modCplx(self):
		'''
			mod= sqrt(cplx.real^2+cplx.imag^2)
		'''
		return abs(self.cplx)
		#return abs(self.cplx)

	def angCplx(self):
		'''
			ang= atan(cplx.imag/cplx.real)
			ang= polar(cplx)[1] en radianes
			
		'''
		return atan2(self.cplx.imag,self.cplx.real)

	def sumaCplx(self,cplx):
		return self.cplx+cplx.cplx

	def restaCplx(self,cplx):
		return self.cplx-cplx.cplx

	def multiCplx(self,cplx):
		return self.cplx*cplx.cplx

	def diviCplx(self,cplx):
		return self.cplx/cplx.cplx

	def potCplx(self,grado):
		return self.cplx*cplx.cplx


		

if __name__ == '__main__':
	"""
	grado1=int(input("Dame el grado del primer polinomio:"))
	variable1=input("Dame el nombre de la variable independiente: ")[0]
	grado2=int(input("Dame el grado del segundo polinomio:"))
	variable2=input("Dame el nombre de la variable independiente: ")[0]
	#instanciamos dos polinomios
	pol1=CalcPol(variable1,grado1)
	pol2=CalcPol(variable2,grado2)
	#Evaluamos en un punto
	punto=float(input("Dame el valor a evaluar para el primer polinomio: "))
	print("Operaciones con Polinomios")
	print("Valor en %s con %s=%.2f: %.2f" %(pol1.expresion,variable1,punto,pol1.valorPunto(punto)))
	#Hacemos todas las operaciones posiles
	print("Suma de %s con %s = %s "%(pol1.expresion,pol2.expresion,pol1.sumaPol(pol2)))
	print("Resta de %s con %s = %s "%(pol1.expresion,pol2.expresion,pol1.restaPol(pol2)))
	print("Multiplicacion de %s con %s = %s "%(pol1.expresion,pol2.expresion,pol1.multiPol(pol2)))
	print("Division de %s con %s = %s "%(pol1.expresion,pol2.expresion,pol1.diviPol(pol2)))
	#Integral y derivada
	print("Derivada de %s respecto a %s = %s "%(pol1.expresion,pol1.variable,pol1.derivaPol()))
	print("Integral de %s respecto a %s = %s "%(pol2.expresion,pol2.variable,pol2.integraPol()))
	"""
	#Operaciones con complejos

	cplx1=CalcCplx(1,2)
	cplx2=CalcCplx(0,-1)
	print("Operaciones con Complejos")
	print("Suma de %s con %s = %s" %(cplx1,cplx2,cplx1.sumaCplx(cplx2)))
	print("Resta de %s con %s = %s" %(cplx1,cplx2,cplx1.restaCplx(cplx2)))
	print("Multiplicacion de %s con %s = %s" %(cplx1,cplx2,cplx1.multiCplx(cplx2)))
	print("Division de %s con %s = %s" %(cplx1,cplx2,cplx1.diviCplx(cplx2)))
	print("Módulo de %s = %s" %(cplx1,cplx1.modCplx()))
	print("Ángulo de %s = %s" %(cplx2,cplx2.angCplx()))



