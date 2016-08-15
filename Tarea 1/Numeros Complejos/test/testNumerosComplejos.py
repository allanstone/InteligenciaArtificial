#!/usr/bin/env python3
#-*- coding: utf-8 -*-

from math import *
import sys
sys.path.append('../')

from numeroComplejo import *
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
          de los metodos de la clase numeroComplejo
          mediante los arreglos de datos definidos
          como entrada y esperando una salida, 
          representada en los for por la variable
          'should_be'.
"""


class testNumerosComplejos(unittest.TestCase):
    """Clase para pruebas unitarias de numeroComplejo
    
    Attributes:
        prueba_Angulo (array(complejo, resultado)): 
            Arreglo de prubas para testear el metodo de angulo
        prueba_divisiones (array(complejo, complejo, resultado)): 
            Arreglo de pruebas para testear el metodo de division
        prueba_Modulo (array(complejo, resultado)): 
            Arreglo de pruebas para testear el metodo de modulo
        prueba_multiplicacion (array(complejo, complejo, resultado)): 
            Arreglo de pruebas para testear el metodo de multiplicacion
        prueba_restas (array(complejo, complejo, resultado)): Description
            Arreglo de pruebas para testear el metodo de restas
        prueba_sumas (array(complejo, complejo, resultado)): 
            Arreglo de sumas para testear el metodo de modulo
    """
    prueba_Sumas=(
        (numeroComplejo(1,2),numeroComplejo(0,-1),complex(1,1)),
        (numeroComplejo(3,2),numeroComplejo(4,-1),complex(7,1))
        )

    prueba_Restas=(
        (numeroComplejo(1,2),numeroComplejo(0,-1),complex(1,3)),
        (numeroComplejo(3,2),numeroComplejo(4,-1),complex(-1,3))
        )

    prueba_Multiplicacion=(
        (numeroComplejo(1,2),numeroComplejo(0,-1),complex(2,-1)),
        (numeroComplejo(3,2),numeroComplejo(4,-1),complex(14,5))
        )
    
    prueba_Divisiones=(
        (numeroComplejo(1,2),numeroComplejo(0,-1),complex(-2,1)),
        (numeroComplejo(3,2),numeroComplejo(4,-1),complex(0.5882352941176471,0.6470588235294118))
        )

    prueba_Modulo=(
        (numeroComplejo(1,2),2.23606797749979),
        (numeroComplejo(3,2),3.605551275463989)
        )

    prueba_Angulo=(
        (numeroComplejo(0,-1),-1.5707963267948966),
        (numeroComplejo(4,-1),-0.24497866312686414)
        )


    def testingSumas(self):
        """
        Prueba unitaria de sumas
        """
        for a,b,should_be in self.prueba_Sumas:
            result = a.suma(b)
            self.assertEqual(should_be, result)

    def testingRestas(self):
        """
        Prueba unitaria de restas
        """
        for a,b,should_be in self.prueba_Restas:
            result = a.resta(b)
            self.assertEqual(should_be, result)

    def testingMultiplicaciones(self):
        """
        Prueba unitaria de multiplicaciones
        """
        for a,b,should_be in self.prueba_Multiplicacion:
            result = a.multiplica(b)
            self.assertEqual(should_be,result)
    
    def testingDivisiones(self):
        """
        Prueba unitaria de divisiones
        """
        for a,b,should_be in self.prueba_Divisiones:
            result = a.divide(b)
            self.assertEqual(should_be, result)

    def testingModulo(self):
        """
        Prueba unitaria de modulo
        """
        for a,should_be in self.prueba_Modulo:
            result = a.modulo()
            self.assertEqual(should_be, result)

    def testingAngulo(self):
        """
        Prueba unitaria de angulo
        """
        for a,should_be in self.prueba_Angulo:
            result = a.angulo()
            self.assertEqual(should_be, result)

if __name__ == '__main__':
    unittest.main()


        
        