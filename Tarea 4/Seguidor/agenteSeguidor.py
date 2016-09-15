#!/usr/bin/env python3
#-*- coding: utf-8 -*-
"""
:platform: Unix, Windows
:synopsis: Este módulo define un agente de reflejo simple implementando un seguidor de linea con tres sensores y dos motores.
.. module:: agenteSeguidor
.. module author::
    Garrido Valencia Alan
    Sánchez Baños Margarito
    Torres Ortiz Luis Miguel
    Zuñiga Hernandez Jonatan    
"""

class Agent:
    """
	    Clase Agente.
        Esta clase define a nuestro agente de reflejo simple de la siguente manera.
	    Atributos:
	       - sensores: Un diccionario con el estado actual de cada sensor
           - motores: Un diccioario con el estado respuesta de los motores

	    Se puede usar de la siguiente manera:
	        >>> darthVader=Villain()
            >>> darthVader.abilities
            [2,3,0,3,7,1,2,4,3,8]
            #También se puede pasar una lista:
            >>> kidBu=Villain([4,4,1,2,1,1,5,4,3,2])
            >>> kidBu.abilities
            [4,4,1,2,1,1,5,4,3,2]
    """

    def __init__(self,*sensors):
        '''
           Constructor de la clase puede instanciar de dos maneras diferentes:
            -Sin parámetros, el agente empezará a girar en espiral ya que detecta que no hay línea
            -Se pasa directamente el estado de los sensores a a la funcion motion
            :param sensors: Lista con los valores de las habilidades.
            :type sensors: list.
        '''
        if sensors:
            self.sensors=sensors
            self.motion(sensors)
        else:
            self.sensors={'s1':False,'s2':False,'s3':False}
            self.motion(sensors)


    def motion(sensors):
        """
            Define la rotacion de los motores segun el estado de los sensores
        """
        if not sensors[0] and not sensors[1] and not sensors[2]:
            print("000")
        elif not sensors[0] and not sensors[1] and sensors[2]:
            print("001")
        elif not sensors[0] and sensors[1] and not sensors[2]:
            print("010")
        elif not sensors[0] and sensors[1] and sensors[2]:
            print("011")
        elif sensors[0] and not sensors[1] and not sensors[2]:
            print("100")
        elif sensors[0] and not sensors[1] and sensors[2]:
            print("101")
        elif sensors[0] and sensors[1] and not sensors[2]:
            print("110")
        elif sensors[0] and sensors[1] and sensors[2]:
            print("111")





class Mo(Agent):
    """docstring for Mo"""
    def __init__(self, arg):
        super(Mo, self).__init__()
        self.arg = arg
        
def populate(max):
    """
        Crea una población de villanos igual al valor que se le pasa como parámetro.

        :param max: Número máximo de villanos que se requiere.
        :type max: int.
        :returns: list population-- Lista con los villanos y sus valores.
    """
    population=[]
    for i in range(0,max):
        population.append(Villain())
    return population


if __name__ == '__main__':

