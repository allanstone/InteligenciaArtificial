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
	       - sensors: Un diccionario con el estado actual de cada sensor.
           - motors: Un diccioario con el estado respuesta de los motores.

	    Se puede usar de la siguiente manera:
	        >>> walle=Agent()
            Giro rápido en espiral
            #También se puede pasar el estado de los sensores:
            >>> eva=Agent([0,1,0])
            
            >>> 
    """

    def __init__(self,*sensors):
        '''
           Constructor de la clase puede instanciar de dos maneras diferentes:
            -Sin parámetros, el agente empezará a girar en espiral ya que detecta que no hay línea
            -Se pasa directamente el estado de los sensores a a la funcion motion
            :param sensors: Diccionario con el estado de los sensores que son valores booleanos.
            :type sensors: dict.
        '''
        self.motors={'m1':1,'m2':1}
        if sensors:
            self.sensors=sensors
            self.motion()
        else:
            self.sensors={'s1':False,'s2':False,'s3':False}
            self.motion()

    def sense(self,line):
        """
            Sensa la línea mediante tres puntos y actualiza el estado de los sensores.
            :param line: Puntos de la linea que pueden ser apreciados, serán leídos de un archivo.
            :type line: list.
            :returns: dict. sensors-- Diccionario con el estado de los sensores.
        """
        for key,view in zip(self.sensors.keys(),line):
            self.sensors[key]=bool(view)
        return self.sensors



    def motion(self):
        """
            Define la rotacion de los motores según el estado de los sensores.

            :returns: dict. motors-- Diccionario con el estado de los motores.
        """
        if not self.sensors['s1'] and not self.sensors['s1'] and not self.sensors['s2']:
            print("Giro rápido en espiral")
            self.motors[0]=2
            self.motors[1]=1
        elif not self.sensors['s1'] and not self.sensors['s1'] and self.sensors['s2']:
            print("Giro a la derecha")
            self.motors[0]=1
            self.motors[1]=0
        elif not self.sensors['s1'] and self.sensors['s1'] and not self.sensors['s2']:
            print("Sigue de frente")
            self.motors[0]=2
            self.motors[1]=1
        elif not self.sensors['s1'] and self.sensors['s1'] and self.sensors['s2']:
            print("Giro a la derecha")
            self.motors[0]=1
            self.motors[1]=0
        elif self.sensors['s1'] and not self.sensors['s1'] and not self.sensors['s2']:
            print("Giro a la izquierda")
            self.motors[0]=0
            self.motors[1]=1
        elif self.sensors['s1'] and not self.sensors['s1'] and self.sensors['s2']:
            print("Giro rápido en espiral")
            self.motors[0]=2
            self.motors[1]=1
        elif self.sensors['s1'] and self.sensors['s1'] and not self.sensors['s2']:
            print("Giro a la izquierda")
            self.motors[0]=0
            self.motors[1]=1
        elif self.sensors['s1'] and self.sensors['s1'] and self.sensors['s2']:
            print("Giro rápido en espiral")
            self.motors[0]=2
            self.motors[1]=1
        return self.motors


class Mo(Agent):
    """
    Clase Mo.
    Esta clase hereda de la clase Agent y define al mismo agente de reflejo simple pero agrega otro sensor para detectar la suciedad.
    Atributos:
       - cleaner: Un booleano que detecta si en su camino hay suciedad y activar el limpiador.
    """
    def __init__(self, *sensors, cleaner):
        super(Mo, self).__init__(*sensors)
        self.cleaner = cleaner
        
def getLine(fileL):
    stripedLine=[]
    with open(fileL,'r') as f:
        for line in f:
            stripedLine.append([int(a) for a in line.strip(" \t\r\n").split(',')])
    return stripedLine


if __name__ == '__main__':
    lineToFollow=getLine("linea.txt")
    a1=Agent()
    for line in lineToFollow:
        print(a1.sense(line))
        a1.motion()



