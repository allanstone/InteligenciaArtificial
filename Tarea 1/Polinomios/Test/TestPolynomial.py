#!/usr/bin/env python3
#-*- coding: utf-8 -*-

"""
.. module:: testPolynomial  
.. moduleauthor:: Garrido Valencia Alan
:synopsis: Este es un modulo de pruebas unitarias para el modulo Polynomio.

"""

import unittest
from ..Scripts.Polinomio import Polynomial
from sympy import symbols

class TestPolynomial(unittest.TestCase):

    variable='x'
    pol1=Polynomial(variable,2,[2,4,20])
    pol2=Polynomial(variable,2,[4,40,100])    
    pol3=Polynomial(variable,1,[1,5])

    def testInstance(self):
        x=symbols(self.variable)
        exp=2.0*x**2+4.0*x+20
        self.assertEqual(self.pol1.expresion ,exp)

    def testValue(self):
        x=symbols(self.variable)
        value=26
        self.assertEqual(self.pol1.pointValue(1),value)

    def testSum(self):
        x=symbols(self.variable)
        exp=6.0*x**2+44.0*x+120
        self.assertEqual(self.pol1.add(self.pol2),exp)

    def testRes(self):
        x=symbols(self.variable)
        exp=(-2.0)*x**2-36.0*x-80.0
        self.assertEqual(self.pol1.sub(self.pol2),exp)

    def testMul(self):
        x=symbols(self.variable)
        exp=8.0*x**4+96.0*x**3+440.0*x**2+1200.0*x+2000.0
        self.assertEqual(self.pol1.mult(self.pol2),exp)

    def testDiv(self):
        x=symbols(self.variable)
        exp=4.0*x+20.0
        self.assertEqual(self.pol2.divi(self.pol3),exp)

    def testdiffer(self):
        x=symbols(self.variable)
        exp=8.0*x + 40.0
        self.assertEqual(self.pol2.differ(),exp)

    def testIntegr(self):
        x=symbols(self.variable)
        exp=(2/3)*x**3 + 2.0*x**2 + 20.0*x
        self.assertEqual(self.pol1.integr(),exp)

    def testIntegrDef(self):
        value=6.50
        self.assertEqual(self.pol3.integrDef(1,2),value)


if __name__ == '__main__':
    unittest.main()
