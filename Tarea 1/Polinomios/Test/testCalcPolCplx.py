#!/usr/bin/env python3
#-*- coding: utf-8 -*-

"""
.. module:: testCalcPolCplx   
.. moduleauthor:: Garrido Valencia Alan
:synopsis: Este es un modulo de pruebas unitarias para CalcPolCplx.

"""

import unittest
from ..Scripts.CalcPolCplx import CalcPol
from sympy import symbols

class TestCalcPolCplx(unittest.TestCase):

    variable='x'
    pol1=CalcPol(variable,2,[2,4,20])
    pol2=CalcPol(variable,2,[4,40,100])    
    pol3=CalcPol(variable,1,[1,5])

    def testInstance(self):
        x=symbols(self.variable)
        exp=2.0*x**2+4.0*x+20
        self.assertEqual(self.pol1.expresion ,exp)

    def testValue(self):
        x=symbols(self.variable)
        value=26
        self.assertEqual(self.pol1.valorPunto(1),value)

    def testSum(self):
        x=symbols(self.variable)
        exp=6.0*x**2+44.0*x+120
        self.assertEqual(self.pol1.sumaPol(self.pol2),exp)

    def testRes(self):
        x=symbols(self.variable)
        exp=(-2.0)*x**2-36.0*x-80.0
        self.assertEqual(self.pol1.restaPol(self.pol2),exp)

    def testMul(self):
        x=symbols(self.variable)
        exp=8.0*x**4+96.0*x**3+440.0*x**2+1200.0*x+2000.0
        self.assertEqual(self.pol1.multiPol(self.pol2),exp)

    def testDiv(self):
        x=symbols(self.variable)
        exp=4.0*x+20.0
        self.assertEqual(self.pol2.diviPol(self.pol3),exp)


if __name__ == '__main__':
    unittest.main()
