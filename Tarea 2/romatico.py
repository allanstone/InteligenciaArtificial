#!/usr/local/bin/python3
#-*- coding: utf-8 -*-

"""
:platform: Unix, Windows
:synopsis: This module implements encryption and decryption romantic
.. module:: romantic
.. module author::
    Garrido Valencia Alan
    Sánchez Baños Margarito
    Torres Ortiz Luis Miguel
    Zuñiga Hernandez Jonatan
"""
class romantic:
    """
    Clase para cifrar y decifrar romanticamente
    
    Attributes:
        matrix (dict): Matriz usada para la substitución
        message (TYPE): Description
        - message: message to be encrypted
    
    Methods:
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
    def __init__(self, message):
        """
        Constructor muy romántico que quita los espacios de la cadena a cifrar
        
        :param message: Mensaje a cifrar
        :type message: string.
    
        """
        self.message = message.replace(' ','')

    def encrypt(self, key):
        """
        Realiza el método de cifrado mediante una matriz interna
        
        :param key: Llave que se utiliza para cifrar
        :type key: string.
        :returns: self.message -- Resultado del cifrado

        """
        encrypted = ""
        self.setKey(key)
        inserted = 0
        while len(self.message)%len(key) != 0:
            self.message+="S"
        while inserted < len(self.message):
            for i in range(0,len(key)):
                self.matrix[key[i]].append(self.message[inserted])
                inserted+=1
        for x in self.matrix:
            for y in range(0, len(self.matrix[x])):
                encrypted+=self.matrix[x][y]
        self.message = encrypted
        return self.message

    def decrypt(self, key):
        """
        Realiza el método de decifrado mediante contrario al de crypt
        
        :param key: Llave que se utiliza para decifrar
        :type key: string.
        :returns: self.message -- Resultado del decifrado

        """

        self.setKey(key)
        descrifrado=""
        aux = sorted(key)
        if len(self.message) % len(key) != 0:
            return "The key to decipher not work, try a different"
        l = len(self.message) / len(key)
        cont=0
        for x in range(0,len(aux)):
            r=cont+l
            for y in range(cont,r):
                self.matrix[aux[x]].append(self.message[y])
                cont+=1
        for i in range(0,len(self.matrix[key[0]])):
            for j in key:
                descrifrado+=self.matrix[j][i]
        self.message = descrifrado
        return self.message

    def setKey(self, key):
        """
        Agrega a un diccionario los caracteres de la llave como valores clave y los asocia con una lista vacia
        
        :param key: Llave que se utiliza para decifrar
        :type key: string.

        """
        self.matrix = {}
        for i in range(0,len(key)):
            self.matrix[key[i]] = []

    def __str__(self):
        """
        Método mágico que imprime el mensaje si este es cifrado o decifrado
.
        :returns: self.message -- El mensaje original o el cifrado
        """
        return "Message: "+self.message
