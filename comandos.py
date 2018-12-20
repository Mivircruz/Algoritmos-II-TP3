#!/usr/bin/python3

import funciones

def listar_operaciones():
    print("nueva_aerolinea")
    print("caminos_mas")

comandos = {"listar_operaciones": listar_operaciones,
            "caminos_mas" : camino_mas}

def camino_mas(modo, origen, destino, grafo):
    
    if modo == "rapido":
        padres = funciones.camino_mas_rapido(grafo, origen, destino)
        print(origen, "->")
        for key, values in padres:
            print(padres[key], "->")
        print(destino)