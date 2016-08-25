#!/usr/bin/env python3
#-*- coding: utf-8 -*-

"""
:platform: Unix, Windows
:synopsis: Este módulo es usado para probar los metodos de criptografía.
.. module:: romanticoTest
.. module author::
    Garrido Valencia Alan
    Sánchez Baños Margarito
    Torres Ortiz Luis Miguel
    Zuñiga Hernandez Jonatan    
"""

import unittest
from romatico import romantic
from sympy import symbols

class TestRomantico(unittest.TestCase):
    """
        Esta clase es usada para pruebas del modulo romantico
    """
    r1=romantic("LA CRIPTOGRAFIA ES ROMANTICA")
    r2=romantic("Entscheidungsproblem")

    def testEncrypt1(self):
        """
        Prueba unitaria de encrypt1
        """
        self.r1.encrypt("HOLA")
        encrypted='ROFSACSLIGIRNACTAEMISAPRAOTS'
        self.assertEqual(self.r1.message ,encrypted)

    def testDencrypt1(self):
        """
        Prueba unitaria de encrypt1
        """
        self.r1.decrypt("HOLA")
        decrypted='LACRIPTOGRAFIAESROMANTICA'
        self.assertEqual(self.r1.message ,decrypted)

    # def testEncrypt2(self):
    #     """
    #     Prueba unitaria de encrypt2
    #     """
    #     self.r1.encrypt("turing")
    #     encrypted='hglSsuoScnbStdrSEesenipm'
    #     self.assertEqual(self.r2.message ,encrypted)
    # def testDencrypt2(self):
    #     """
    #     Prueba unitaria de encrypt2
    #     """
    #     self.r1.decrypt("turing")
    #     decrypted='Entscheidungsproblem'
    #     self.assertEqual(self.r2.message ,decrypted)
  

if __name__ == '__main__':
    unittest.main()
