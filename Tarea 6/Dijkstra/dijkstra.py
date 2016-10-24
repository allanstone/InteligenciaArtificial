#!/usr/bin/env python3
#-*- coding: utf-8 -*-
"""
:platform: Unix, Windows
:synopsis: Este módulo define un objeto implementando una gráfica y el algoritmo spf de Dijstra.
.. module:: agenteSeguidor
.. module author::
    Garrido Valencia Alan
    Sánchez Baños Margarito
    Torres Ortiz Luis Miguel
    Zuñiga Hernandez Jonatan    
"""
import heapq
import sys

class Graph:
    
    def __init__(self):
        self.vertices = {}
        
    def addVertex(self, name, edges):
        self.vertices[name] = edges
    
    def shortestPathFirst(self, start, finish):
        distances = {} # Diccionario de distancias
        previous = {}  # Diccionario de nodos previos para la ruta optimo
        nodes = [] # Lista de prioridad

        for vertex in self.vertices:
            if vertex == start: 
                # Distancia a inicial de cero
                distances[vertex] = 0
                heapq.heappush(nodes, [0, vertex])
            else:
                distances[vertex] = sys.maxsize
                heapq.heappush(nodes, [sys.maxsize, vertex])
            previous[vertex] = None
        
        while nodes:
            smallest = heapq.heappop(nodes)[1] # vertice en la grafica con la menor distancia
            if smallest == finish: 
                path = []
                while previous[smallest]: 
                    path.append(smallest)
                    smallest = previous[smallest]
                return path
            if distances[smallest] == sys.maxsize: 
                break
            
            for neighbor in self.vertices[smallest]: 
                alt = distances[smallest] + self.vertices[smallest][neighbor] 
                if alt < distances[neighbor]: 
                    distances[neighbor] = alt
                    previous[neighbor] = smallest
                    for n in nodes:
                        if n[1] == neighbor:
                            n[0] = alt
                            break
                    heapq.heapify(nodes)
        return distances
        
    def __str__(self):
        return str(self.vertices)

if __name__ == '__main__':
    g = Graph()
    g.addVertex('A', {'B': 7, 'C': 8})
    g.addVertex('B', {'A': 7, 'F': 2})
    g.addVertex('C', {'A': 8, 'F': 6, 'G': 4})
    g.addVertex('D', {'F': 8})
    g.addVertex('E', {'H': 1})
    g.addVertex('F', {'B': 2, 'C': 6, 'D': 8, 'G': 9, 'H': 3})
    g.addVertex('G', {'C': 4, 'F': 9})
    g.addVertex('H', {'E': 1, 'F': 3})
    print(g.shortestPathFirst('A', 'H'))


