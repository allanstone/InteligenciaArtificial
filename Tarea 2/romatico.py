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
    Class to encrypt and decrypt romantically
    
    Attributes:
        matrix (dict): Description
        message (TYPE): Description
        - message: message to be encrypted
    
    Methods:
       - encrypt: encrypts the message sent to construct the object with the key sent
       - decrypt: decrypts the message sent to construct the object with the key sent
    """
    def __init__(self, message):
        """Summary
        
        Args:
            message (TYPE): Description
        """
        self.message = message.replace(' ','')

    def encrypt(self, key):
        """Summary
        
        Args:
            key (TYPE): Description
        
        Returns:
            TYPE: Description
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
        """Summary
        
        Args:
            key (TYPE): Description
        
        Returns:
            TYPE: Description
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
        """Summary
        
        Args:
            key (TYPE): Description
        
        Returns:
            TYPE: Description
        """
        self.matrix = {}
        for i in range(0,len(key)):
            self.matrix[key[i]] = []

    def __str__(self):
        """Summary
        
        Returns:
            TYPE: Description
        """
        return "Message: "+self.message


r = romantic("LA CRIPTOGRAFIA ES ROMANTICA")
r.encrypt("HOLA")
print(r)
r.decrypt("hola")
print(r)