#!/usr/bin/python3

import funciones
import math

def listar_operaciones():
    print comandos


comandos = [
    "camino_mas",
    "camino_escalas",
    "centralidad_aprox",
    "reccorer_mundo_aprox",
    "listar_operaciones"
]

def camino_mas(modo, origen, destino, grafo):

    camino = funciones.camino_mas_modo(grafo, origen, destino, modo)
    print origen, "->",
    for v in camino:
        if v == destino:
            print v
        else:
            print v, "->",


def camino_escalas(grafo, origen, destino):

    recorrido = funciones.camino_minimo(grafo, origen, destino)
    print origen, "->",
    print recorrido
    for v in recorrido[0].keys():
        if v == destino:
            print v
        else:
            print recorrido[0][v], "->",

def centralidad_aprox(grafo, n):

    cent = funciones.centralidad(grafo)
    i = 1

    for key, values in cent:
        print(cent[key])
        if i < n:
            print(',')
        i+=1
        if i == n:
            return

def recorrer_mundo_aprox(grafo, origen):

    lugares_del_mundo = grafo.obtener_todos_vertices()
    tiempo = float('inf')
    actual = origen
    visitados = []
    costo = 0

    while lugares_del_mundo:
        for w, values in vertice.obtener_adyacente(grafo.obtener_vertice(grafo, actual)):
            if grafo.obtener_tiempo(grafo, v, w) < tiempo:
                tiempo = grafo.obtener_tiempo(grafo, v, w)
            actual = w
            costo += tiempo
        visitados.append(actual)
        lugares_del_mundo.remove(actual)

    for i in range(0, len(visitados)):
        print(visitados[i])
        if i < len(visitados)-1:
            print("->")
    print("Costo: ", costo)




def vacaciones(grafo, origen, n):
    visitados = set()
    padres = {}
    padres[origen] = None
    funciones.recorrido_vacaciones(grafo, origen, visitados, padres, 0, origen, n)

    for i in range(0, len(visitados)):
        print(visitados[i])
        if i < len(visitados)-1:
            print("->")



