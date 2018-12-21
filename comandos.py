#!/usr/bin/python3

import funciones
import math

def listar_operaciones():
    print(comandos)


comandos = [
    "camino_mas",
    "camino_escalas",
    "centralidad_aprox",
    "recorrer_mundo_aprox",
    "listar_operaciones"
]

def camino_mas(modo, origen, destino, grafo):

    camino = funciones.camino_mas_modo(grafo, origen, destino, modo)

    print camino
    for v in camino:
        if v == grafo.obtener_codigo(destino):
            print v
        else:
            print v, "->",



def camino_escalas(grafo, origen, destino):

    recorrido = funciones.camino_minimo(grafo, origen, destino)

    for v in recorrido[0].keys():
        if v == destino:
            print(v)
        else:
            print(recorrido[0][v], "->")

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

        codigo_actual = grafo.obtener_codigo(actual)

        for ady in grafo.obtener_adyacentes(codigo_actual).keys():

            if ady == actual:
                continue

            ciudad_ady = grafo.obtener_ciudad(ady)
            if grafo.obtener_tiempo(codigo_actual, ady) < tiempo:
                tiempo = grafo.obtener_tiempo(codigo_actual, ciudad_ady)
                actual = ciudad_ady
        costo += tiempo
        visitados.append(codigo_actual)
        lugares_del_mundo.pop(codigo_actual)

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



