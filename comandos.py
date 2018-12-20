#!/usr/bin/python3

import funciones

def listar_operaciones():
    print("nueva_aerolinea")
    print("caminos_mas")
    print("camino_escalas")

comandos = {"listar_operaciones": listar_operaciones,
            "caminos_mas" : camino_mas}

def camino_mas(modo, origen, destino, grafo):

    padres = funciones.camino_mas_rapido(grafo, origen, destino, modo)
    print(origen, "->")
    for key, values in padres:
        print(padres[key], "->")
    print(destino)

def camino_escalas(origen, destino, grafo):

    recorrido = funciones.camino_minimo(grafo, origen, destino)
    print(origen, "->")
    for key, velues in recorrido:
        print(recorrido[key], "->")
    print(destino)

def centralidad_aprox(grafo, n):

    cent = funciones.centralidad(grafo)
    i = 0

    for key, values in cent:
        if i == n:
            return
        print(cent[key])
        if i < n-1
            print(',')


