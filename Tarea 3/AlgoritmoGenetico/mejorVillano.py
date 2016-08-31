#!/usr/bin/env python3
#-*- coding: utf-8 -*-
"""
:platform: Unix, Windows
:synopsis: Este módulo define implementa un algoritmo genético para crear al mejor villano.
.. module:: complexNumber
.. module author::
    Garrido Valencia Alan
    Sánchez Baños Margarito
    Torres Ortiz Luis Miguel
    Zuñiga Hernandez Jonatan    
"""
from random import randint

class Villain:
    """
	    Clase villano.
	    Metodos:
	       - encrypt: Cifra el mensaje pasado al constructor con la llave

	    Se puede usar de la siguiente manera:
	        >>> 
    """

    def __init__(self,*abilities):
        """
            Constructor de Villain
        """
        if abilities:
            self.abilities=abilities[0]
        else:
            abilities=[]
            for i in range(0,10):
                abilities.append(randint(0,9))
            self.abilities=abilities

def populate(max):
    population=[]
    for i in range(0,max):
        population.append(Villain())
    return population

def createGeneration(population):
    abilities=[]
    for i in range(0,10):
        abilities.append(population[randint(0,len(population)-1)].abilities[i])
    return Villain(abilities)

def createCrossbreed(Villain1,Villain2):
    abilities=[]
    split=randint(0,9)
    abilities=Villain1.abilities[:split]+Villain2.abilities[split:]
    return Villain(abilities)

def createNewPopulation(Villain1,Villain2):
    newPopulation=[]
    for newVillain in range(0,10):
        newPopulation.append(createCrossbreed(megamente,sedusa))
    return newPopulation



if __name__ == '__main__':
    population=populate(100)
    for villain in population:
        print(villain.abilities)
    print("Cantidad de la poblacion: ",len(population))
    megamente=createGeneration(population)
    print("Las habilidades de Megamente son: %s" %(megamente.abilities))
    sedusa=createGeneration(population)
    print("Las habilidades de  Sedusa   son: %s" %(sedusa.abilities))
    sedumente=createCrossbreed(megamente,sedusa)
    print("Las habilidades de Sedumente son: %s" %(sedumente.abilities))

    newPopulation=createNewPopulation(megamente,sedusa)
    for seduvillain in newPopulation:
        print(seduvillain.abilities)
    sedumente1=createGeneration(newPopulation)
    print("Las habilidades de Sedumente1 son: %s" %(sedumente1.abilities))
    sedumente2=createGeneration(population)
    print("Las habilidades de Sedumente2 son: %s" %(sedumente2.abilities))
    drDoofenshmirtz=createCrossbreed(sedumente1,sedumente2)
    print("Las habilidades del mejor villano son: %s" %(drDoofenshmirtz.abilities))
