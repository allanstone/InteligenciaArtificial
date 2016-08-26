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
        >>>from cypher import Cypher
	    >>>c=Cypher()
	    >>>print(c.cypher("LA CRIPTOGRAFIA ES ROMANTICA","HOLA"))
	    >>>print(c.decypher("ROFSACSLIGIRNACTAEMISAPRAOTS","HOLA"))
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
    	print(key,end='')
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

    def cypher(self,textToCypher,key,printMap=False):
        '''
        Cifra un texto con una llave bajo un algoritmo descrito
        
        :param textToCypher: Llave que se utiliza para cifrar
        :type textToCypher: .
        :param key: Llave que se utiliza para cifrar
        :type key: string.
        :param printMap: Parámetro opcional si se desea ver el mapa de carácteres
        :type printMap: string.
        :returns: string-- Cadena cifrada
        '''
        plain=textToCypher.replace(' ','')
        pad=len(plain)%len(key)
        textToCypher=plain+'S'*(len(key)-pad)
        if printMap:
        	self.printMap(textToCypher,key)
        charMap=self.chunking(textToCypher,len(key))
        newOrder=self.reorganize(key)
        newCharMap=self.reassembling(newOrder,charMap)
        cyphedText=self.joinCharMap(newCharMap,len(key))
        return cyphedText
    
    def unassamble(self,textToDecipher,key):
    	"""
        Toma el texto a decifrar y lo divide en cadenas del tamaño de la llave.
        :param textToDeCypher: Texto que se va a decifrar
        :type textToCypher: string.
        :param keyLen: Longitud de la llave
        :type keyLen: int.
        :returns: list -- Lista por comprensión de cadenas del tamaño de la llave
        """
    	chunkLen=int(len(textToDecipher)/len(key))
    	return(self.chunking(textToDecipher,chunkLen))

    def disrupt(self,key):
    	"""
        Toma la llave y la regresa el orden de indices original.
        :param key: Llave que se utiliza para cifrar
        :type key: string.
        :returns: list -- Regresa el orden de los indices de la llave ordenada
        """
    	oldOrder=[]
    	for char in key:
    		oldOrder.append(sorted(key).index(char))
    	return oldOrder

    def rematch(self,charMap,key):
    	"""
        Une de nuevo las cadenas del mapa de caracteres con el orden por renglon en vez de por columna

        :param charMap: Mapa de caracteres a reacomodar
        :type charMap: list.
        :param key: La llave con la que se cifró
        :type key: string.
        :returns: string -- Regresa el mapa de caracteres reacomodado
        """
    	newCharMap=[]
    	for index in range(0,len(charMap[0])):
    		for string in charMap:
    			newCharMap.append(string[index])
    			newCharMap[:len(key)] = [''.join(newCharMap[:len(key)])]
    	return newCharMap

    def attachCharMap(self,oldCharMap):
    	"""
        Une de nuevo las cadenas del charMap

        :param charMap: Mapa de caracteres a reensamblar
        :type charMap: list.
        :param keyLen: Longitud de la llave
        :type keyLen: int.
        :returns: string -- Regresa el texto cifrado
        """
    	return ''.join(oldCharMap)


    def decypher(self,textToDecipher,key,printMap=False):
        '''
        Cifra un texto con una llave bajo el algoritmo contrario.
        
        :param textToCypher: Llave que se utiliza para cifrar
        :type textToCypher: .
        :param key: Llave que se utiliza para cifrar
        :type key: string.
        :param printMap: Parámetro opcional si se desea ver el mapa de carácteres
        :type printMap: string.
        :returns: string-- Cadena cifrada
        '''
        if printMap:
        	self.printMap(textToDecipher,key)        
        charMap=self.unassamble(textToDecipher,key)
        newCharMap=self.rematch(charMap,key)
        if printMap:
        	print("")
        	self.printMap(newCharMap[0],''.join(sorted(key)))
        CharMap=self.chunking(newCharMap[0],len(key))
        oldOrder=self.disrupt(key)
        oldCharMap=self.reassembling(oldOrder,CharMap)
        decyphedText=self.attachCharMap(oldCharMap)
        return decyphedText


if __name__ == '__main__':
    c=Cypher()
    key="HOLA"
    strToCipher="LA CRIPTOGRAFIA ES ROMANTICA"
    strToDecipher="ROFSACSLIGIRNACTAEMISAPRAOTS"
    print("Llave: ",key,"\nCadena a cifrar: ",strToCipher)
    print("Cadena cifrada: ",c.cypher(strToCipher,key,True))
    print("Llave: ",key,"\nCadena a decifrar: ",strToDecipher)
    print("Cadena decifrada: ",c.decypher(strToDecipher,key,True))
    print("Awww  <3")


