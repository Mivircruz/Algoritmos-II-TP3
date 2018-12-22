#!/usr/bin/python3

import sys
import comandos
import grafo as g

def conexiones(aeropuertos, vuelos):

    grafo = g.Grafo()

    for linea in aeropuertos:

        info_aeropuerto = linea.split(",")
        grafo.agregar_vertice(info_aeropuerto[0], info_aeropuerto[1], info_aeropuerto[2], info_aeropuerto[3])

    for linea in vuelos:
        info_vuelo = linea.split(",")
        grafo.agregar_arista(info_vuelo[0], info_vuelo[1], info_vuelo[2], info_vuelo[3], info_vuelo[4])

    return grafo


def main():

    aeropuerto = open(sys.argv[1], "r")
    vuelos = open(sys.argv[2], "r")

    grafo = conexiones(aeropuerto, vuelos)

   # sys.argv[1].close()
   # sys.argv[2].close()

    linea = sys.stdin.readline().rstrip('\n')

    while len(linea) > 0:
        a_ejecutar = linea.split(" ")

        if a_ejecutar[0] not in comandos.comandos.keys():
            print("Error")
            continue
        else:
            comandos.comandos.get(a_ejecutar[0])(grafo, linea)

        linea = sys.stdin.readline().rstrip('\n')

main()
