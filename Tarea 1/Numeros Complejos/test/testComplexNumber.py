#!/usr/bin/env python3
#-*- coding: utf-8 -*-

from math import *
import sys
sys.path.append('../')

from complexNumber import *
import unittest

"""
module::  
    testNumerosComplejos
module authors::
    Garrido Valencia Alan
    Sánchez Baños Margarito
    Torres Ortiz Luis Miguel
    Zuñiga Hernandez Jonatan
synopsis: Este modulo implementa pruebas unitarias
          de los metodos de la clase complexNumber
          mediante los arreglos de datos definidos
          como entrada y esperando una salida, 
          representada en los for por la variable
          'should_be'.
"""


class testComplexNumber(unittest.TestCase):
    """Clase para pruebas unitarias de complexNumber
    
    Attributes:
        tesing_angle (array(complejo, resultado)): 
            Arreglo de prubas para testear el metodo de angulo
        testing_div (array(complejo, complejo, resultado)): 
            Arreglo de pruebas para testear el metodo de division
        testing_mod (array(complejo, resultado)): 
            Arreglo de pruebas para testear el metodo de modulo
        testing_mult (array(complejo, complejo, resultado)): 
            Arreglo de pruebas para testear el metodo de multiplicacion
        testing_sub (array(complejo, complejo, resultado)): Description
            Arreglo de pruebas para testear el metodo de restas
        testing_add (array(complejo, complejo, resultado)): 
            Arreglo de sumas para testear el metodo de modulo
    """
    testing_add=(
        (complexNumber(1,2),complexNumber(0,-1),complex(1,1)),
        (complexNumber(3,2),complexNumber(4,-1),complex(7,1))
        )

    testing_sub=(
        (complexNumber(1,2),complexNumber(0,-1),complex(1,3)),
        (complexNumber(3,2),complexNumber(4,-1),complex(-1,3))
        )

    testing_mult=(
        (complexNumber(1,2),complexNumber(0,-1),complex(2,-1)),
        (complexNumber(3,2),complexNumber(4,-1),complex(14,5))
        )
    
    testing_div=(
        (complexNumber(1,2),complexNumber(0,-1),complex(-2,1)),
        (complexNumber(3,2),complexNumber(4,-1),complex(0.5882352941176471,0.6470588235294118))
        )

    testing_pot=(
        (complexNumber(1,2),3,complex(-11,-2)),
        (complexNumber(3,2),2,complex(5,12))
        )

    testing_mod=(
        (complexNumber(1,2),2.23606797749979),
        (complexNumber(3,2),3.605551275463989)
        )

    testing_angle=(
        (complexNumber(0,-1),-1.5707963267948966),
        (complexNumber(4,-1),-0.24497866312686414)
        )


    def testingAdd(self):
        """
        Prueba unitaria de sumas
        """
        for a,b,should_be in self.testing_add:
            result = a.add(b)
            self.assertEqual(should_be, result)

    def testingSub(self):
        """
        Prueba unitaria de restas
        """
        for a,b,should_be in self.testing_sub:
            result = a.sub(b)
            self.assertEqual(should_be, result)

    def testingMult(self):
        """
        Prueba unitaria de multiplicaciones
        """
        for a,b,should_be in self.testing_mult:
            result = a.mult(b)
            self.assertEqual(should_be,result)
    
    def testingDivi(self):
        """
        Prueba unitaria de divisiones
        """
        for a,b,should_be in self.testing_div:
            result = a.divi(b)
            self.assertEqual(should_be, result)

    def testingPot(self):
        """
        Prueba unitaria de potencia
        """
        for a,b,should_be in self.testing_pot:
            result = a.pot(b)
            self.assertEqual(should_be, result)


    def testingMod(self):
        """
        Prueba unitaria de modulo
        """
        for a,should_be in self.testing_mod:
            result = a.mod()
            self.assertEqual(should_be, result)

    def testingAngule(self):
        """
        Prueba unitaria de angulo
        """
        for a,should_be in self.testing_angle:
            result = a.angle()
            self.assertEqual(should_be, result)

if __name__ == '__main__':
    unittest.main()


        
        