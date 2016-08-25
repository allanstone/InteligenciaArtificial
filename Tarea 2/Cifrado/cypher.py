#!/usr/bin/env python3
#-*- coding: utf-8 -*-

"""
:platform: Unix, Windows
:synopsis: Este módulo define una clase para cifrar y decifrar.
.. module:: complexNumber
.. module author::
    Garrido Valencia Alan
    Sánchez Baños Margarito
    Torres Ortiz Luis Miguel
    Zuñiga Hernandez Jonatan    
"""


class Cypher:
    '''
    Esta clase implementa un método de cifrado.
    
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
    
    def __init__(self,a,b):
     
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
        #self.cplx=complex(a,b)
    def printMap(self,textToCipher,key):
    	start=0
    	print(key)
    	for end in range(0,len(textToCipher)+1,len(key)):
    		print(textToCipher[start:end])
    		start=end

    def chunking(self,textToCipher, keyLen):
    	return ([textToCipher[pos:pos+keyLen] for pos in range(0,len(textToCipher),keyLen)])

    def reorganize(self,key):
    	#return([key.index(char) for char in sorted(key)])
    	newOrder=[]
    	for char in sorted(key):
    		newOrder.append(key.index(char))
    	return newOrder

    def reassembling(self,newOrder,charMap):
    	newCharMap=[]
    	for string in charMap:
    		newCharMap.append(''.join([str(string[index]) for index in newOrder]))
    	return newCharMap

    def joinCharMap(self,charMap,keyLen):
    	cyphedText=[]
    	for i in range(0,keyLen):
    		[cyphedText.append(string[i]) for string in charMap]
    	print(''.join(cyphedText))






    def cypher(self,text,key):
        '''
        Realiza el modulo del numero complejo de la siguiente manera
        mod= sqrt(cplx.real^2+cplx.imag^2)
        
        :returns: float-- modulo del numero complejo
        '''
        plain=text.replace(' ','')
        pad=len(plain)%len(key)
        textToCipher=plain+'S'*(len(key)-pad)
        self.printMap(textToCipher,key)
        charMap=self.chunking(textToCipher,len(key))
        newOrder=self.reorganize(key)
        print()
        newCharMap=self.reassembling(newOrder,charMap)
        self.joinCharMap(newCharMap,len(key))







        return textToCipher
        
        

if __name__ == '__main__':
    c=Cypher()
    print(c.cypher("la criptografia es romantica","hola"))
