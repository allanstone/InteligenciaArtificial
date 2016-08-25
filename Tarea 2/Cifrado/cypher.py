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
    """
    Clase para cifrar y decifrar romanticamente
    
    Metodos:
       - encrypt: Cifra el mensaje pasado al constructor con la llave
       - decrypt: Deifra el mensaje pasado al constructor con la llave

    Se puede usar de la siguiente manera:
        >>> from romantico import romantic
        >>>r =romantic("LA CRIPTOGRAFIA ES ROMANTICA")
        >>>r.encrypt("HOLA")
        >>>print(r)
        Message: ROFSACSLIGIRNACTAEMISAPRAOTS
        >>>r.decrypt("hola")
        >>>print(r)
        Message: LACRIPTOGRAFIAESROMANTICASSS
    """
    def printMap(self,textToCypher,key):
    	"""
        Imprime el mapa de caracteres.
        :param textToCypher: Texto que se va a cifrar
        :type textToCypher: string.
        :param key: Llave que se utiliza para cifrar
        :type key: string.
        """
    	start=0
    	print(key)
    	for end in range(0,len(textToCypher)+1,len(key)):
    		print(textToCypher[start:end])
    		start=end

    def chunking(self,textToCypher, keyLen):
    	"""
        Toma el texto a cifrar y lo divide en cadenas del tamaño de la llave.
        :param textToCypher: Texto que se va a cifrar
        :type textToCypher: string.
        :param keyLen: Longitud de la llave
        :type keyLen: int.
        :returns: list -- Lista por comprensión de cadenas del tamaño de la llave
        """
    	return ([textToCypher[pos:pos+keyLen] for pos in range(0,len(textToCypher),keyLen)])

    def reorganize(self,key):
    	"""
        Toma la llave y la regresa ordenada en orden alfabetico.
        :param key: Llave que se utiliza para cifrar
        :type key: string.
        :returns: list -- Regresa el orden de los indices de la llave ordenada
        """
    	newOrder=[]
    	for char in sorted(key):
    		newOrder.append(key.index(char))
    	return newOrder

    def reassembling(self,newOrder,charMap):
    	"""
        Utiliza el orden de indices para cambiar cada una de las cadenas del charMap

        :param newOrder: Orden de indices que cambiará para cada cadena
        :type newOrder: list.
        :param charMap: Mapa de caracteres a reensamblar
        :type charMap: list.
        :returns: list -- Regresa el orden de los indices de la llave ordenada
        """
    	newCharMap=[]
    	for string in charMap:
    		newCharMap.append(''.join([str(string[index]) for index in newOrder]))
    	return newCharMap

    def joinCharMap(self,charMap,keyLen):
    	"""
        Une de nuevo las cadenas del charMap

        :param charMap: Mapa de caracteres a reensamblar
        :type charMap: list.
        :param keyLen: Longitud de la llave
        :type keyLen: int.
        :returns: string -- Regresa el texto cifrado
        """
    	cyphedText=[]
    	for i in range(0,keyLen):
    		[cyphedText.append(string[i]) for string in charMap]
    	return ''.join(cyphedText)

    def cypher(self,textToCypher,key):
        '''
        Cifra un texto con una llave bajo un algoritmo descrito
        
        :param textToCypher: Llave que se utiliza para cifrar
        :type textToCypher: .
        :param key: Llave que se utiliza para cifrar
        :type key: string.
        :returns: string-- Cadena cifrada
        '''
        plain=textToCypher.replace(' ','')
        pad=len(plain)%len(key)
        textToCypher=plain+'S'*(len(key)-pad)
        self.printMap(textToCypher,key)
        charMap=self.chunking(textToCypher,len(key))
        newOrder=self.reorganize(key)
        print()
        newCharMap=self.reassembling(newOrder,charMap)
        cyphedText=self.joinCharMap(newCharMap,len(key))
        return cyphedText
    
    def unassamble(self,textToDecipher,key):
    	chunkLen=int(len(textToDecipher)/len(key))
    	return(self.chunking(textToDecipher,chunkLen))

    def disrupt(self,key):
    	"""
        Toma la llave y la regresa el orden de indices original.
        :param key: Llave que se utiliza para cifrar
        :type key: string.
        :returns: list -- Regresa el orden de los indices de la llave ordenada
        """
    	newOrder=[]
    	for char in key:
    		newOrder.append(key.index(char))
    	return newOrder 

    def rematch(self,oldOrder,charMap):
    	oldString=[]
    	for i in oldOrder:
    		[oldString.append(string[index]) for string in charMap]
    	return ''.join(cyphedText)

    def decypher(self,textToDecipher,key):
        '''
        Cifra un texto con una llave bajo el algoritmo contrario.
        
        :param textToCypher: Llave que se utiliza para cifrar
        :type textToCypher: .
        :param key: Llave que se utiliza para cifrar
        :type key: string.
        :returns: string-- Cadena cifrada
        '''
        self.printMap(textToDecipher,key)
        oldOrder=self.disrupt(key)
        charMap=self.unassamble(textToDecipher,key)
        print(charMap)
        newCharMap=self.rematch(oldOrder,charMap)
        print(newCharMap)



if __name__ == '__main__':
    c=Cypher()
    #print(c.cypher("La criptografia es romantica","hola"))
    c.decypher("ROFSACSLIGIRNACTAEMISAPRAOTS","HOLA")
    #print(c.decypher("La criptografia es romantica","hola"))

