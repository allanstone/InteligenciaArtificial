#!/usr/bin/env python3
"""
:platform: Unix, Windows
synopsis:Este modulo implementa las clases para operaciones con numeros complejos.
.. module:: complexNumber
.. module author::
    Garrido Valencia Alan
    Sánchez Baños Margarito
    Torres Ortiz Luis Miguel
    Zuñiga Hernandez Jonatan    
"""
#-*- coding: utf-8 -*-

from sympy import atan2


class complexNumber:
    '''
    Esta clase implementa un numero complejo de las con las siguientes características.
    
    Atributos:
           - cplx: numero complejo guardado con el objeto
        Métodos:
           - __str__: Formatea el numero complejo para imprimirlo
           - mod: Obtiene el modulo del numero complejo
           - angle: Obtiene el angulo del numero complejo
           - add: Suma un numero complejo
           - sub: Resta un numero complejo
           - mult: multiplica un numero complejo
           - divi: divide un numero complejo
           - pot: Eleva a una potencia el numero complejo
    
    Se puede usar de la siguiente manera:
        >>> import complexNumber as c
        >>> num1 = c.complexNumber(1,3)
        >>> num2 = c.complexNumber(1,3)
        >>> print(num1)
        1.00+3.00j
        >>> num1.add(num2)
        (2+6j)
    '''
    def __init__(self,a,b):
        '''
        Constructor de la clase complexNumber se instancia con dos parametrso:
         -Se pasa como parametro la parte real
         -Se pasa como parametro la parte imaginaria
         :param a: Parte real del numero complejo.
         :type a: float.
         :param b: Parte imaginaria del numero complejo.
         :type b: float.
        
        Args:
            a (float): Parte real del numero complejo
            b (float): Parte imaginaria del numero complejo
        '''
        self.cplx=complex(a,b)

    def __str__(self):
        """
        Metodo para imprimir un numero complejo
        
        :returns: string-- cadena con un formato establecido con dos decimales
        """
        return "{:.2f}".format(self.cplx)

    def mod(self):
        '''
        Realiza el modulo del numero complejo de la siguiente manera
        mod= sqrt(cplx.real^2+cplx.imag^2)
        
        :returns: float-- modulo del numero complejo
        '''
        return abs(self.cplx)

    def angle(self):
        '''
        realiza el calculo del angulo del numero complejo de la siguiente manera
        ang= atan(cplx.imag/cplx.real)
        ang= polar(cplx)[1] en radianes

        :returns: float-- angulo del numero complejo
        '''
        return atan2(self.cplx.imag,self.cplx.real)

    def add(self,cplx):
        """Realiza la suma del numero complejo
        con otro recibido como parametro
        
        :param cplx: Numero complejo a sumar
        :type cplx: Obj complexNumber.
        :returns: Obj complexNumber-- Suma de los dos numeros complejos.
        """
        return self.cplx+cplx.cplx

    def sub(self,cplx):
        """Realiza la resta del numero complejo
        recibido como parametro
        
        :param cplx: Numero complejo a restar
        :type cplx: Obj complexNumber.
        :returns: Obj complexNumber-- Resta de los numeros complejos
        """
        return self.cplx-cplx.cplx

    def mult(self,cplx):
        """Realiza la multiplicación del numero
        complejo recibido como parametro
        
        :param cplx: Numero complejo a multiplicar
        :type cplx: Obj complexNumber.
        :returns: Obj complexNumber-- multiplicación de numeros complejos
        """
        return self.cplx*cplx.cplx

    def divi(self,cplx):
        """Realiza la división entre el numero complejo
        recibido como parametro
        
        :param cplx: Numero complejo por el cual dividir
        :type cplx: Obj complexNumber.
        :returns: Obj complexNumber-- División entre los dos numero complejos
        """
        return self.cplx/cplx.cplx

    def pot(self,grado):
        """Realiza la potenciación del numero complejo
        
        :param grado: Potencia a cual elevar el numero
        :type grado: integer.
        :returns: Obj complexNumber-- Numero complejo elevado a el grado
        """
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
    print("Módulo de %s = %s" %(cplx2,cplx2.mod()))
    print("Ángulo de %s = %s" %(cplx2,cplx2.angle()))

