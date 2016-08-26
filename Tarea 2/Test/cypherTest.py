#!/usr/bin/env python3
#-*- coding: utf-8 -*-
"""
:platform: Unix, Windows
:synopsis: Este módulo es usado para probar los metodos de criptografía.
.. module:: cypherTest
.. module author::
    Garrido Valencia Alan
    Sánchez Baños Margarito
    Torres Ortiz Luis Miguel
    Zuñiga Hernandez Jonatan    
"""

import unittest
import sys
sys.path.append('../')
from Cifrado.cypher import Cypher

class TestCypher(unittest.TestCase):
    """
        Esta clase es usada para pruebas del modulo romantico
    """

    key1="HOLA"
    strToCipher1="LA CRIPTOGRAFIA ES ROMANTICA"
    strToDecipher1="ROFSACSLIGIRNACTAEMISAPRAOTS"
    key2="turing"
    strToCipher2="Entscheidungsproblem"
    strToDecipher2="hglSsuoScnbStdrSEesenipm"
    c1=Cypher()
    c2=Cypher()

    def testEncrypt1(self):
        """
        Prueba unitaria de encrypt1
        """
        encrypted='ROFSACSLIGIRNACTAEMISAPRAOTS'
        self.assertEqual(self.c1.cypher(self.strToCipher1,self.key1) ,encrypted)

    def testDencrypt1(self):
        """
        Prueba unitaria de encrypt1
        """
        decrypted='LACRIPTOGRAFIAESROMANTICASSS'
        self.assertEqual(self.c1.decypher(self.strToDecipher1,self.key1) ,decrypted)

    def testEncrypt2(self):
        """
        Prueba unitaria de encrypt2
        """
        encrypted='hglSsuoScnbStdrSEesenipm'
        self.assertEqual(self.c2.cypher(self.strToCipher2,self.key2) ,encrypted)
    def testDencrypt2(self):
        """
        Prueba unitaria de encrypt2
        """
        decrypted='EntscheidungsproblemSSSS'
        self.assertEqual(self.c2.decypher(self.strToDecipher2,self.key2) ,decrypted)
  

if __name__ == '__main__':
    unittest.main()
