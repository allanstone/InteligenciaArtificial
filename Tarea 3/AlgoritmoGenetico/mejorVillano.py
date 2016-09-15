#!/usr/bin/env python3
#-*- coding: utf-8 -*-
"""
:platform: Unix, Windows
:synopsis: Este módulo implementa un algoritmo genético para crear al mejor villano.
.. module:: mejorVillano
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
	    Atributos:
	       - abilities: Una lista con los valores de las habilidades del villano

	    Se puede usar de la siguiente manera:
	        >>> darthVader=Villain()
            >>> darthVader.abilities
            [2,3,0,3,7,1,2,4,3,8]
            #También se puede pasar una lista:
            >>> kidBu=Villain([4,4,1,2,1,1,5,4,3,2])
            >>> kidBu.abilities
            [4,4,1,2,1,1,5,4,3,2]
    """

    def __init__(self,*abilities):
        '''
           Constructor de la clase  puede instanciar de dos maneras diferentes:
            -Sin parámetros, las habilidades se crearán aleatoriamente
            -Se pasan  una lista con los valores para las habilidades
            :param abilities: Lista con los valores de las habilidades.
            :type abilities: list.
        '''
        if abilities:
            self.abilities=abilities[0]
        else:
            abilities=[]
            for i in range(0,10):
                abilities.append(randint(0,9))
            self.abilities=abilities

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

def createGeneration(population):
    """
        Crea una nueva generación con un villano con valores seleccionados aleatoriamente de la población.

        :param population: Lista de villanos de la que se obtendrá el nuevo villano.
        :type population: list.
        :returns: Obj Villain-- Villano con valores seleccionados de la población.
    """
    abilities=[]
    for i in range(0,10):
        abilities.append(population[randint(0,len(population)-1)].abilities[i])
    return Villain(abilities)

def createCrossbreed(Villain1,Villain2):
    """
        Crea una nuevo villano de de la combinación de otros dos.

        :param Villain1: Villano del que se obtendrá un número aleatorio de habilidades.
        :type Villain1: Villain.
        :param Villain2: Villano del que se obtendrá el resto de las habilidades.
        :type Villain2: Villain.
        :returns: Obj Villain-- Villano con valores seleccionados de los otros dos.
    """
    abilities=[]
    split=randint(0,9)
    abilities=Villain1.abilities[:split]+Villain2.abilities[split:]
    return Villain(abilities)

def createNewPopulation(Villain1,Villain2):
    """
        Crea una nueva generación de villanos creados apartir de otros dos.

        :param Villain1: Villano del que se obtendrá un número aleatorio de habilidades.
        :type Villain1: Villain.
        :param Villain2: Villano del que se obtendrá el resto de las habilidades.
        :type Villain2: Villain.
        :returns: list-- Lista de nueva generación de villanos.
    """
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
