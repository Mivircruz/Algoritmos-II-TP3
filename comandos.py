# !/usr/bin/python3

import funciones as f
import math


def listar_operaciones():
    for funcion in comandos:
        if funcion != "listar_operaciones":
            print funcion



comandos = [
    "camino_mas",
    "camino_escalas",
    "centralidad_aprox",
    "recorrer_mundo_aprox",
    "vacaciones",
    "listar_operaciones"
]


def camino_mas(grafo, origen, destino, modo):
    arbol = f.prim(grafo, origen, modo)
    padres, dist = f.bfs(arbol, arbol.obtener_codigo(origen))
    lista = []
    lista.append(grafo.obtener_codigo(destino))
    v = lista[0]

    while v!= grafo.obtener_codigo(origen):
        v = padres[v]
        lista.append(v)


    while lista:
        if len(lista) == 1:
            print lista.pop()

        else:
            print lista.pop(), "->",



def camino_escalas(grafo, origen, destino):
    padres, orden = f.bfs(grafo, grafo.obtener_codigo(origen))
    v = padres[grafo.obtener_codigo(destino)]
    lista = []
    lista.append(grafo.obtener_codigo(destino))

    while v != grafo.obtener_codigo(origen):
        lista.append(v)
        v = padres[v]

    if v != padres[grafo.obtener_codigo(destino)]:
        lista.append(v)

    while lista:
        if len(lista) == 1:
            print lista.pop()

        else:
            print lista.pop(), "->",


def centralidad_aprox(grafo, n):
    cent = funciones.centralidad(grafo)
    i = 1

    for key, values in cent:
        print(cent[key])
        if i < n:
            print(',')
        i += 1
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
        if i < len(visitados) - 1:
            print("->")
    print("Costo: ", costo)


def vacaciones(grafo, origen, n):
    padres = {}
    padres[grafo.obtener_codigo(origen)] = None

    funciones.recorrido_vacaciones(grafo, origen, padres, 0, origen, n)

# for key, values in padres:
#    print(values)
#   print("->")
