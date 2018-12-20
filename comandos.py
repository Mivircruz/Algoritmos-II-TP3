#!/usr/bin/python3

import funciones

def listar_operaciones():
    print(comandos)

comandos = [
    "camino_mas" ,
    "camino_escalas",
    "centralidad_aprox"
]

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
    i = 1

    for key, values in cent:
        print(cent[key])
        if i < n:
            print(',')
        i+=1
        if i == n:
            return


