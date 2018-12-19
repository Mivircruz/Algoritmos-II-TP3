#!/usr/bin/python3

import funciones
def listar_operaciones():
    print ("nueva_aerolinea")

comandos = {"listar_operaciones": listar_operaciones}

def camino_mas(modo, origen, destino, grafo):
    
    if modo == "rapido":
        padres = funciones.camino_mas_rapido(grafo, origen, destino)
        print origen "->"
        for kes,values in padres:
            print padres[key] "->"
        print destino